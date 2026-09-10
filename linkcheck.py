#!/usr/bin/env python3
"""On-demand reachability reporter for the OSINT source register.

Answers one narrow question: does each registered URL currently answer, and
how. It exists to execute the link portion of the maintenance cadence in
`toolkit/02-osint-source-register.md` section 10 and deliberately refuses the
larger claim. A working link does not establish that the underlying record is
current, complete, applicable, or authentic; content currency remains a manual
review outcome under section 10.3 and module 11, never an HTTP status.

Deliberately not wired into continuous integration: reachability depends on
network position, time, and each target's bot posture, and the CI gate stays
deterministic and offline. An anti-bot denial (HTTP 403/429) is reported as
BLOCKED, not failure, because section 10.3 requires recording the access
outcome without treating anti-bot denial as source retirement.
"""

from __future__ import annotations

import argparse
import json
import hashlib
import math
import re
import socket
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

from bundle import atomic_write

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import validate  # noqa: E402  (single source of truth for row and link parsing)

REGISTER = ROOT / "toolkit" / "02-osint-source-register.md"
BUILD = ROOT / "build"

OK = "OK"
REDIRECT = "REDIRECT"
BLOCKED = "BLOCKED"
ERROR = "ERROR"
TIMEOUT = "TIMEOUT"

# Identify the probe honestly; browser access may produce a different outcome.
USER_AGENT = "SimpleToolkit-Linkcheck/1.3 (+https://github.com/maxmoran23/simple-toolkit)"
HEADERS = {"User-Agent": USER_AGENT, "Accept": "*/*"}
# Servers that reject HEAD outright get one GET retry; a 403/429 stays BLOCKED.
HEAD_RETRY_CODES = {400, 405, 501}

DISCLAIMER = (
    "A working link does not establish that the underlying record is current, "
    "complete, applicable, or authentic."
)
BLOCKED_NOTE = (
    "BLOCKED records an access outcome only; anti-bot denial is not source "
    "retirement (toolkit/02 section 10.3)."
)


def register_rows() -> list[dict[str, str]]:
    """Return id, tier, and https target for every register row with a link."""
    text = REGISTER.read_text(encoding="utf-8")
    rows: list[dict[str, str]] = []
    ids = set()
    candidates = list(re.finditer(r"(?m)^\|\s*(\d{2}\.\d{3})\s*\|", text))
    for candidate in candidates:
        if validate.SOURCE_ROW.match(text, candidate.start()) is None:
            raise ValueError(f"register ID {candidate[1]} has an invalid tier or row format")
    for match in validate.SOURCE_ROW.finditer(text):
        source_id = match.group("id")
        if source_id in ids:
            raise ValueError(f"duplicate register ID: {source_id}")
        ids.add(source_id)
        end = text.find("\n", match.start())
        line = text[match.start() : end if end != -1 else len(text)]
        found = list(validate.md.links(line))
        if len(found) != 1:
            raise ValueError(f"register ID {source_id} must contain exactly one source link")
        target = found[0].target
        validate_url(target)
        rows.append({"id": source_id, "tier": match.group("tier"), "url": target})
    return rows


def classify_status(status: int, moved: bool) -> tuple[str, str]:
    if status in (403, 429):
        return BLOCKED, f"HTTP {status}"
    if 300 <= status < 400:
        return REDIRECT, f"HTTP {status}"
    if 200 <= status < 300:
        if moved:
            return REDIRECT, "followed redirect"
        return OK, f"HTTP {status}"
    return ERROR, f"HTTP {status}"


def classify_exception(exc: BaseException) -> tuple[str, str]:
    if isinstance(exc, urllib.error.HTTPError):
        return classify_status(exc.code, moved=False)
    if isinstance(exc, (socket.timeout, TimeoutError)):
        return TIMEOUT, "request timed out"
    if isinstance(exc, urllib.error.URLError):
        if isinstance(exc.reason, (socket.timeout, TimeoutError)):
            return TIMEOUT, "request timed out"
        return ERROR, str(exc.reason)
    return ERROR, f"{type(exc).__name__}: {exc}"


def validate_url(url: str) -> None:
    try:
        parsed = urlsplit(url)
        valid = (parsed.scheme == "https" and parsed.hostname and not parsed.username
                 and not parsed.password and parsed.port != 0
                 and not any(ord(c) < 33 for c in url))
    except ValueError:
        valid = False
    if not valid:
        raise ValueError("URL must use HTTPS, a valid host/port, and no credentials or whitespace")


class SafeRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        validate_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def probe(url: str, timeout: float) -> tuple[str, str]:
    opener = urllib.request.build_opener(SafeRedirectHandler())
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, headers=HEADERS, method=method)
        try:
            with opener.open(request, timeout=timeout) as response:
                status = getattr(response, "status", None) or response.getcode()
                return classify_status(status, moved=response.geturl() != url)
        except urllib.error.HTTPError as exc:
            exc.close()
            if method == "HEAD" and exc.code in HEAD_RETRY_CODES:
                continue
            return classify_status(exc.code, moved=False)
        except Exception as exc:  # noqa: BLE001 - every failure becomes a report row
            return classify_exception(exc)
    return ERROR, "no response"


def resolved_json_path(raw: str) -> Path:
    """Reports may only be written under the gitignored build directory."""
    if BUILD.is_symlink():
        raise ValueError("build/ must be a real directory, not a symlink")
    candidate = Path(raw)
    resolved = (candidate if candidate.is_absolute() else ROOT / candidate).resolve()
    build = BUILD.resolve()
    if build not in resolved.parents or resolved.suffix.lower() != ".json":
        raise ValueError("--json must name a .json file under build/")
    return resolved


def print_footer(counts: Counter, checked: int, elapsed: float) -> None:
    summary = " ".join(f"{key}={counts.get(key, 0)}" for key in (OK, REDIRECT, BLOCKED, ERROR, TIMEOUT))
    print(f"\nChecked {checked} URLs in {elapsed:.1f}s: {summary}")
    print(f"NOTE: {BLOCKED_NOTE}")
    print(f"DISCLAIMER: {DISCLAIMER}")


def run_report(args: argparse.Namespace) -> int:
    json_path = resolved_json_path(args.json) if args.json else None
    rows = ([{"id": "ad-hoc", "tier": "", "url": args.url}] if args.url else register_rows())
    if args.ids:
        wanted = {token.strip() for token in args.ids.split(",") if token.strip()}
        if not wanted:
            raise ValueError("--ids must contain at least one register ID")
        unknown = sorted(wanted - {row["id"] for row in rows})
        if unknown:
            raise ValueError(f"unknown register IDs: {', '.join(unknown)}")
        rows = [row for row in rows if row["id"] in wanted]
    if not rows:
        raise ValueError("no register rows selected")

    started = time.monotonic()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        urls = sorted({row["url"] for row in rows})
        futures = {pool.submit(probe, url, args.timeout): url for url in urls}
        results = {futures[future]: future.result() for future in as_completed(futures)}
        for row in rows:
            row["status"], row["detail"] = results[row["url"]]
    elapsed = time.monotonic() - started

    rows.sort(key=lambda row: row["id"])
    for row in rows:
        print(f"{row['id']}  {row['status']:<8}  {row['detail']:<28}  {row['url']}")
    counts = Counter(row["status"] for row in rows)
    print_footer(counts, len(rows), elapsed)

    if json_path:
        json_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "schema_version": 1,
            "selected_rows": len(rows),
            "unique_urls_probed": len(urls),
            "register_sha256": None if args.url else hashlib.sha256(REGISTER.read_bytes()).hexdigest(),
            "user_agent": USER_AGENT,
            "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "timeout_seconds": args.timeout,
            "counts": dict(sorted(counts.items())),
            "results": rows,
            "disclaimer": DISCLAIMER,
            "blocked_note": BLOCKED_NOTE,
        }
        atomic_write(json_path, json.dumps(payload, indent=2) + "\n")
        print(f"JSON report written to {json_path}")

    if args.strict and (counts.get(ERROR) or counts.get(TIMEOUT)):
        return 1
    return 0



def selftest() -> int:
    """Offline assertions only: classifier table, extraction, and guardrails."""
    failures: list[str] = []

    def check(name: str, actual: object, expected: object) -> None:
        if actual != expected:
            failures.append(f"{name}: got {actual!r}, expected {expected!r}")

    check("200", classify_status(200, moved=False), (OK, "HTTP 200"))
    check("204", classify_status(204, moved=False), (OK, "HTTP 204"))
    check("followed redirect", classify_status(200, moved=True), (REDIRECT, "followed redirect"))
    check("301", classify_status(301, moved=False), (REDIRECT, "HTTP 301"))
    check("403", classify_status(403, moved=False), (BLOCKED, "HTTP 403"))
    check("429", classify_status(429, moved=False), (BLOCKED, "HTTP 429"))
    check("404", classify_status(404, moved=False), (ERROR, "HTTP 404"))
    check("503", classify_status(503, moved=False), (ERROR, "HTTP 503"))
    http_403 = urllib.error.HTTPError("https://example.com/", 403, "Forbidden", None, None)
    check("HTTPError 403", classify_exception(http_403), (BLOCKED, "HTTP 403"))
    check("socket timeout", classify_exception(socket.timeout())[0], TIMEOUT)
    check("wrapped timeout", classify_exception(urllib.error.URLError(TimeoutError()))[0], TIMEOUT)
    check("dns failure", classify_exception(urllib.error.URLError("nodename not provided"))[0], ERROR)

    rows = register_rows()
    if len(rows) < 400:
        failures.append(f"register extraction found only {len(rows)} linked rows")
    ids = [row["id"] for row in rows]
    if len(ids) != len(set(ids)):
        failures.append("register extraction produced duplicate IDs")
    if any(not row["url"].startswith("https://") for row in rows):
        failures.append("register extraction produced a non-https URL")

    # The tool must carry the register's own limitation sentence verbatim.
    if DISCLAIMER not in REGISTER.read_text(encoding="utf-8"):
        failures.append("disclaimer sentence no longer matches toolkit/02")

    try:
        resolved_json_path("/etc/simple-toolkit-should-never-write-here.json")
        failures.append("json path guard accepted a path outside build/")
    except ValueError:
        pass

    if failures:
        print(f"FAIL: {len(failures)} selftest error(s)")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"PASS: linkcheck selftest ({len(rows)} linked register rows; classifier and guards verified)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--ids", help="comma-separated register IDs to check (default: all)")
    group.add_argument("--url", help="check a single ad-hoc URL instead of the register")
    parser.add_argument("--timeout", type=float, default=10.0, help="per-request timeout in seconds")
    parser.add_argument("--workers", type=int, default=8, help="concurrent requests")
    parser.add_argument("--json", help="also write a JSON report (must resolve under build/)")
    parser.add_argument("--strict", action="store_true", help="exit 1 if any ERROR or TIMEOUT")
    group.add_argument("--selftest", action="store_true", help="run offline assertions and exit")
    args = parser.parse_args()

    if not math.isfinite(args.timeout) or not 0 < args.timeout <= 120:
        parser.error("--timeout must be finite and greater than 0, at most 120 seconds")
    if not 1 <= args.workers <= 32:
        parser.error("--workers must be between 1 and 32")
    if args.selftest:
        return selftest()
    try:
        if args.url:
            validate_url(args.url)
        return run_report(args)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    sys.exit(main())
