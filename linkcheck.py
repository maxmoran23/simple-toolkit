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
import socket
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

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

# The reachability probe presents itself as an ordinary desktop browser so the
# outcome approximates what the section 10.3 manual check would observe.
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)
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
    for match in validate.SOURCE_ROW.finditer(text):
        end = text.find("\n", match.start())
        line = text[match.start() : end if end != -1 else len(text)]
        link = validate.MARKDOWN_LINK.search(line)
        if not link:
            continue
        target = link.group("target").strip()
        if target.startswith("https://"):
            rows.append({"id": match.group("id"), "tier": match.group("tier"), "url": target})
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


def probe(url: str, timeout: float) -> tuple[str, str]:
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, headers=HEADERS, method=method)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                status = getattr(response, "status", None) or response.getcode()
                return classify_status(status, moved=response.geturl() != url)
        except urllib.error.HTTPError as exc:
            if method == "HEAD" and exc.code in HEAD_RETRY_CODES:
                continue
            return classify_status(exc.code, moved=False)
        except Exception as exc:  # noqa: BLE001 - every failure becomes a report row
            return classify_exception(exc)
    return ERROR, "no response"


def resolved_json_path(raw: str) -> Path:
    """Reports may only be written under the gitignored build directory."""
    candidate = Path(raw)
    resolved = (candidate if candidate.is_absolute() else ROOT / candidate).resolve()
    build = BUILD.resolve()
    if resolved != build and build not in resolved.parents:
        raise SystemExit(f"--json path must stay under {build}")
    return resolved


def print_footer(counts: Counter, checked: int, elapsed: float) -> None:
    summary = " ".join(f"{key}={counts.get(key, 0)}" for key in (OK, REDIRECT, BLOCKED, ERROR, TIMEOUT))
    print(f"\nChecked {checked} URLs in {elapsed:.1f}s: {summary}")
    print(f"NOTE: {BLOCKED_NOTE}")
    print(f"DISCLAIMER: {DISCLAIMER}")


def run_report(args: argparse.Namespace) -> int:
    json_path = resolved_json_path(args.json) if args.json else None
    rows = register_rows()
    if args.ids:
        wanted = {token.strip() for token in args.ids.split(",") if token.strip()}
        unknown = sorted(wanted - {row["id"] for row in rows})
        if unknown:
            raise SystemExit(f"unknown register IDs: {', '.join(unknown)}")
        rows = [row for row in rows if row["id"] in wanted]
    if not rows:
        raise SystemExit("no register rows selected")

    started = time.monotonic()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(probe, row["url"], args.timeout): row for row in rows}
        for future in as_completed(futures):
            row = futures[future]
            row["status"], row["detail"] = future.result()
    elapsed = time.monotonic() - started

    rows.sort(key=lambda row: row["id"])
    for row in rows:
        print(f"{row['id']}  {row['status']:<8}  {row['detail']:<28}  {row['url']}")
    counts = Counter(row["status"] for row in rows)
    print_footer(counts, len(rows), elapsed)

    if json_path:
        json_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "timeout_seconds": args.timeout,
            "counts": dict(sorted(counts.items())),
            "results": rows,
            "disclaimer": DISCLAIMER,
            "blocked_note": BLOCKED_NOTE,
        }
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"JSON report written to {json_path}")

    if args.strict and (counts.get(ERROR) or counts.get(TIMEOUT)):
        return 1
    return 0


def run_single(args: argparse.Namespace) -> int:
    status, detail = probe(args.url, args.timeout)
    print(f"{status}  {detail}  {args.url}")
    print_footer(Counter([status]), 1, 0.0)
    if args.strict and status in (ERROR, TIMEOUT):
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
    except SystemExit:
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
    parser.add_argument("--ids", help="comma-separated register IDs to check (default: all)")
    parser.add_argument("--url", help="check a single ad-hoc URL instead of the register")
    parser.add_argument("--timeout", type=float, default=10.0, help="per-request timeout in seconds")
    parser.add_argument("--workers", type=int, default=8, help="concurrent requests")
    parser.add_argument("--json", help="also write a JSON report (must resolve under build/)")
    parser.add_argument("--strict", action="store_true", help="exit 1 if any ERROR or TIMEOUT")
    parser.add_argument("--selftest", action="store_true", help="run offline assertions and exit")
    args = parser.parse_args()

    if args.selftest:
        return selftest()
    if args.url:
        return run_single(args)
    return run_report(args)


if __name__ == "__main__":
    sys.exit(main())
