#!/usr/bin/env python3
"""Deterministic structural, navigation, privacy, and registry checks."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent

EXPECTED_MARKDOWN = {
    "README.md",
    "AGENTS.md",
    "toolkit/00-operating-system.md",
    "toolkit/01-evidence-research-standard.md",
    "toolkit/02-osint-source-register.md",
    "toolkit/03-mailbox-communications.md",
    "toolkit/04-intelligence-fincrime-frameworks.md",
    "toolkit/05-investigation-control-methods.md",
    "toolkit/06-data-quality-governance.md",
    "toolkit/07-output-templates.md",
    "toolkit/08-automation-orchestration.md",
    "toolkit/09-quality-assurance.md",
    "toolkit/10-use-case-recipes.md",
    "toolkit/11-deployment-security-maintenance.md",
}

REQUIRED_FILES = {
    "README.md",
    "AGENTS.md",
    "LICENSE",
    "NOTICE",
    ".gitignore",
    "validate.py",
    "bundle.py",
    "linkcheck.py",
    ".github/workflows/validate.yml",
}
# Generated output lives here and is never committed or validated as content.
IGNORED_DIRS = {".git", "build"}
HEADING = re.compile(r"^#{1,6} ")
BUDGET_ROW = re.compile(r"^\| `(?P<file>\d{2}-[a-z-]+\.md)` \| (?P<words>[\d,]+) \|", re.MULTILINE)
BUDGET_TOTAL = re.compile(r"^\| \*\*All twelve modules\*\* \| \*\*(?P<words>[\d,]+)\*\* \|", re.MULTILINE)
BUNDLE_TOKENS = re.compile(r"~(?P<k>\d+)k")
# Approximate token figures are rounded by hand; allow drift below this width.
TOKEN_TOLERANCE_K = 2
MODULE_LINKS = [f"toolkit/{number:02d}-" for number in range(12)]
SOURCE_ROW = re.compile(r"^\| (?P<id>\d{2}\.\d{3}) \| (?P<tier>T1|T2|T3|TX) \|", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"!?\[[^\]\n]*\]\((?P<target>[^)\n]+)\)")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})", re.MULTILINE)
EMAIL = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
EMOJI = re.compile(
    "["
    "\U0001F000-\U0001FAFF"
    "\U0001FC00-\U0001FFFF"
    "]"
)

PROHIBITED = {
    "named employer": re.compile(r"(?i)\bmorgan\s+stanley\b"),
    "private macOS path": re.compile(r"/Users/"),
    "private email fragment": re.compile(r"(?i)maxpatmoran|icloud\.com"),
    "unfinished marker": re.compile(r"(?i)\b(?:TODO|TBD|lorem ipsum)\b"),
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def markdown_files() -> dict[str, Path]:
    return {
        path.relative_to(ROOT).as_posix(): path
        for path in ROOT.rglob("*.md")
        if not IGNORED_DIRS.intersection(path.parts)
    }


def strip_fences(text: str) -> list[str]:
    """Return only the lines outside fenced code blocks.

    Template payload inside fences frequently contains heading-shaped lines. They
    are content, not document structure, and must not be treated as headings.
    """
    lines: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            lines.append(line)
    return lines


def check_headings(files: dict[str, Path], errors: list[str]) -> int:
    """Enforce the duplicate-heading rule stated in AGENTS.md maintenance."""
    total = 0
    for rel, path in sorted(files.items()):
        headings = [
            line.strip()
            for line in strip_fences(path.read_text(encoding="utf-8"))
            if HEADING.match(line)
        ]
        total += len(headings)
        duplicates = sorted(h for h, count in Counter(headings).items() if count > 1)
        if duplicates:
            shown = ", ".join(duplicates[:3])
            fail(errors, f"{rel}: duplicate heading(s): {shown}")
    return total


def check_bundles(files: dict[str, Path], errors: list[str]) -> int:
    """Keep bundle.py, the README table, and module 10 in exact agreement.

    Three places describe the same bundle registry. Without this gate they drift,
    and a user loading a bundle from the wrong table gets silently reduced
    coverage.
    """
    bundle_path = ROOT / "bundle.py"
    if not bundle_path.is_file():
        return 0
    namespace: dict[str, object] = {"__file__": str(bundle_path), "__name__": "_bundle"}
    try:
        exec(compile(bundle_path.read_text(encoding="utf-8"), str(bundle_path), "exec"), namespace)
    except Exception as exc:  # pragma: no cover - surfaced as a validation error
        fail(errors, f"bundle.py: failed to load bundle registry: {exc}")
        return 0

    bundles = namespace.get("BUNDLES")
    chars_per_token = namespace.get("CHARS_PER_TOKEN", 4)
    if not isinstance(bundles, dict):
        fail(errors, "bundle.py: BUNDLES registry missing or malformed")
        return 0

    modules = {
        rel.split("/")[-1][:2]: path
        for rel, path in files.items()
        if rel.startswith("toolkit/")
    }
    readme = files["README.md"].read_text(encoding="utf-8")
    recipes = files["toolkit/10-use-case-recipes.md"].read_text(encoding="utf-8")

    for key, spec in sorted(bundles.items()):
        members = list(spec["modules"])
        # `full` is written as a range in prose; compare the others literally.
        if key != "full":
            rendered = ", ".join(f"`{m}`" for m in members)
            for label, text in (("README.md", readme), ("toolkit/10-use-case-recipes.md", recipes)):
                if rendered not in text:
                    fail(errors, f"{label}: bundle `{key}` module list does not match bundle.py")

        estimate = sum(len(modules[m].read_text(encoding="utf-8")) for m in members if m in modules)
        expected_k = round(estimate / chars_per_token / 1000)
        for label, text in (("README.md", readme), ("toolkit/10-use-case-recipes.md", recipes)):
            row = next(
                (line for line in text.splitlines() if f"`{key}`" in line and "~" in line),
                None,
            )
            if row is None:
                fail(errors, f"{label}: bundle `{key}` has no context-size row")
                continue
            stated = BUNDLE_TOKENS.search(row)
            if not stated:
                fail(errors, f"{label}: bundle `{key}` row has no ~Nk context figure")
                continue
            if abs(int(stated.group("k")) - expected_k) > TOKEN_TOLERANCE_K:
                fail(
                    errors,
                    f"{label}: bundle `{key}` states ~{stated.group('k')}k context; "
                    f"disk implies ~{expected_k}k",
                )
    return len(bundles)


def check_budget_table(files: dict[str, Path], errors: list[str]) -> None:
    """Word counts published in the README must equal the files on disk."""
    readme = files["README.md"].read_text(encoding="utf-8")
    rows = list(BUDGET_ROW.finditer(readme))
    if not rows:
        fail(errors, "README.md: context budget table missing")
        return

    listed = 0
    for match in rows:
        name = match.group("file")
        stated = int(match.group("words").replace(",", ""))
        path = files.get(f"toolkit/{name}")
        if path is None:
            fail(errors, f"README.md: context budget lists unknown module {name}")
            continue
        actual = len(path.read_text(encoding="utf-8").split())
        listed += actual
        if stated != actual:
            fail(errors, f"README.md: {name} listed at {stated:,} words; disk has {actual:,}")

    expected_modules = len(EXPECTED_MARKDOWN) - 2
    if len(rows) != expected_modules:
        fail(errors, f"README.md: context budget covers {len(rows)} of {expected_modules} modules")

    total = BUDGET_TOTAL.search(readme)
    if not total:
        fail(errors, "README.md: context budget total row missing")
    elif int(total.group("words").replace(",", "")) != listed:
        fail(
            errors,
            f"README.md: context budget total is {total.group('words')}; "
            f"modules sum to {listed:,}",
        )


def check_inventory(files: dict[str, Path], errors: list[str]) -> None:
    actual = set(files)
    missing = sorted(EXPECTED_MARKDOWN - actual)
    extra = sorted(actual - EXPECTED_MARKDOWN)
    if missing:
        fail(errors, f"missing Markdown files: {', '.join(missing)}")
    if extra:
        fail(errors, f"unexpected Markdown files: {', '.join(extra)}")
    for name in sorted(REQUIRED_FILES):
        if not (ROOT / name).is_file():
            fail(errors, f"missing required file: {name}")


def check_text(files: dict[str, Path], errors: list[str]) -> tuple[int, int]:
    total_lines = 0
    total_words = 0
    for rel, path in sorted(files.items()):
        text = path.read_text(encoding="utf-8")
        total_lines += len(text.splitlines())
        total_words += len(re.findall(r"\S+", text))
        if not text.startswith("# "):
            fail(errors, f"{rel}: must start with one H1")
        if len(text.splitlines()) < 40:
            fail(errors, f"{rel}: unexpectedly short")
        if text.count("\x00"):
            fail(errors, f"{rel}: contains NUL bytes")
        if EMAIL.search(text):
            fail(errors, f"{rel}: contains an email-shaped value")
        if EMOJI.search(text):
            fail(errors, f"{rel}: contains emoji-range characters")
        for label, pattern in PROHIBITED.items():
            match = pattern.search(text)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                fail(errors, f"{rel}:{line}: prohibited {label}")

        fences = FENCE.findall(text)
        if len(fences) % 2:
            fail(errors, f"{rel}: unbalanced fenced code blocks")
    return total_lines, total_words


def clean_link_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    # Optional Markdown title: (path "title"). None are required by this repo.
    target = re.split(r"\s+[\"']", target, maxsplit=1)[0]
    return unquote(target)


def check_links(files: dict[str, Path], errors: list[str]) -> tuple[int, int]:
    internal = 0
    external = 0
    for rel, path in sorted(files.items()):
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            target = clean_link_target(match.group("target"))
            if not target or target.startswith("#"):
                continue
            if target.startswith(("https://", "mailto:", "data:")):
                external += 1
                continue
            if target.startswith("http://"):
                line = text.count("\n", 0, match.start()) + 1
                fail(errors, f"{rel}:{line}: external links must use HTTPS: {target}")
                continue
            if "://" in target:
                external += 1
                continue
            internal += 1
            path_part = target.split("#", 1)[0].split("?", 1)[0]
            if not path_part:
                continue
            resolved = (path.parent / path_part).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                line = text.count("\n", 0, match.start()) + 1
                fail(errors, f"{rel}:{line}: relative link escapes repository: {target}")
                continue
            if not resolved.exists():
                line = text.count("\n", 0, match.start()) + 1
                fail(errors, f"{rel}:{line}: broken internal link: {target}")
    return internal, external


def check_readme(files: dict[str, Path], errors: list[str]) -> None:
    readme = files.get("README.md")
    if not readme:
        return
    text = readme.read_text(encoding="utf-8")
    for prefix in MODULE_LINKS:
        if prefix not in text:
            fail(errors, f"README.md: missing module link prefix {prefix}")


def check_registry(files: dict[str, Path], errors: list[str]) -> tuple[int, dict[str, int]]:
    path = files.get("toolkit/02-osint-source-register.md")
    if not path:
        return 0, {}
    text = path.read_text(encoding="utf-8")
    matches = list(SOURCE_ROW.finditer(text))
    ids = [match.group("id") for match in matches]
    tiers = Counter(match.group("tier") for match in matches)
    duplicates = sorted(source_id for source_id, count in Counter(ids).items() if count > 1)
    if duplicates:
        fail(errors, f"source register has duplicate IDs: {', '.join(duplicates)}")
    if len(ids) < 400:
        fail(errors, f"source register has {len(ids)} entries; expected at least 400")
    domains = {source_id.split(".", 1)[0] for source_id in ids}
    expected_domains = {f"{number:02d}" for number in range(1, 20)}
    missing = sorted(expected_domains - domains)
    if missing:
        fail(errors, f"source register missing domains: {', '.join(missing)}")
    for number in range(1, 20):
        if f"### 8.{number} " not in text:
            fail(errors, f"source register missing section 8.{number}")

    # Every row must carry the full nine-cell schema with a real Use and a real
    # Limits value. A row without an honest limitation invites over-reliance.
    for match in matches:
        source_id = match.group("id")
        end = text.find("\n", match.start())
        line = text[match.start() : end if end != -1 else len(text)].strip()
        if not line.endswith("|"):
            fail(errors, f"source register row {source_id}: row does not end with a cell delimiter")
            continue
        cells = [cell.strip() for cell in line[1:-1].split("|")]
        if len(cells) != 9:
            fail(errors, f"source register row {source_id}: has {len(cells)} cells; expected 9")
            continue
        if not cells[5]:
            fail(errors, f"source register row {source_id}: empty Use cell")
        if not cells[8]:
            fail(errors, f"source register row {source_id}: empty Limits cell")

    # Workflow packs cite rows by ID; a cited ID that no longer resolves sends
    # the reader to nothing.
    packs = re.search(r"(?ms)^## 9\. Workflow source packs$.*?(?=^## )", text)
    if packs is None:
        fail(errors, "source register missing section 9 workflow packs")
    else:
        cited = set(re.findall(r"\b\d{2}\.\d{3}\b", packs.group(0)))
        unknown = sorted(cited - set(ids))
        if unknown:
            fail(errors, f"source register workflow packs cite unknown IDs: {', '.join(unknown)}")
    return len(ids), dict(sorted(tiers.items()))


def check_terminology(files: dict[str, Path], errors: list[str]) -> None:
    patterns = {
        "SPECULATIVE used as a confidence rating": re.compile(
            r"(?i)\bconfidence(?:\s+(?:rating|tier|label|score))?\s*[:=]\s*SPECULATIVE\b"
        ),
        "UNRESOLVED used as a confidence rating": re.compile(
            r"(?im)(?:\bconfidence(?:\s+(?:rating|tier|label|score))?\s*[:=]\s*UNRESOLVED\b|\bUNRESOLVED\s+confidence\b)"
        ),
    }
    for rel, path in sorted(files.items()):
        text = path.read_text(encoding="utf-8")
        for label, pattern in patterns.items():
            match = pattern.search(text)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                fail(errors, f"{rel}:{line}: {label}")


def check_release_controls(files: dict[str, Path], errors: list[str]) -> None:
    readme = files.get("README.md")
    deployment = files.get("toolkit/11-deployment-security-maintenance.md")
    agents = files.get("AGENTS.md")
    workflow = ROOT / ".github/workflows/validate.yml"

    version = None
    if readme:
        match = re.search(r"Current release: `(v\d+\.\d+\.\d+)`", readme.read_text(encoding="utf-8"))
        if not match:
            fail(errors, "README.md: missing or malformed current release record")
        else:
            version = match.group(1)
    if deployment:
        text = deployment.read_text(encoding="utf-8")
        # The release the README advertises must have a record in module 11.
        if version and f"| Version and date | `{version}`;" not in text:
            fail(
                errors,
                f"toolkit/11-deployment-security-maintenance.md: no release record for {version}",
            )
        if "## Initial release record" not in text or "| Rollback release |" not in text:
            fail(errors, "toolkit/11-deployment-security-maintenance.md: incomplete initial release record")
        if "github.com/maxmoran23/maxmoran23" in text:
            fail(errors, "toolkit/11-deployment-security-maintenance.md: unrelated profile repository disclosed")
    if agents:
        equation = (
            "items_received_or_identified\n"
            "= processed\n"
            "+ duplicates\n"
            "+ excluded_by_rule\n"
            "+ unparsed\n"
            "+ inaccessible\n"
            "+ deferred"
        )
        if equation not in agents.read_text(encoding="utf-8"):
            fail(errors, "AGENTS.md: canonical completeness equation missing")

    if workflow.is_file():
        text = workflow.read_text(encoding="utf-8")
        uses = re.findall(r"(?m)^\s*-\s+uses:\s+[^@\s]+@([^\s#]+)", text)
        if not uses:
            fail(errors, ".github/workflows/validate.yml: no external actions found")
        for ref in uses:
            if not re.fullmatch(r"[0-9a-f]{40}", ref):
                fail(errors, f".github/workflows/validate.yml: action ref is not pinned to a commit: {ref}")


def main() -> int:
    errors: list[str] = []
    files = markdown_files()
    check_inventory(files, errors)
    lines, words = check_text(files, errors)
    internal, external = check_links(files, errors)
    check_readme(files, errors)
    sources, tiers = check_registry(files, errors)
    check_terminology(files, errors)
    check_release_controls(files, errors)
    headings = check_headings(files, errors)

    bundles = 0
    if {"README.md", "toolkit/10-use-case-recipes.md"} <= set(files):
        bundles = check_bundles(files, errors)
        check_budget_table(files, errors)

    if errors:
        print(f"FAIL: {len(errors)} validation error(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: Simple Toolkit validation")
    print(f"- Markdown files: {len(files)}")
    print(f"- Lines / words: {lines:,} / {words:,}")
    print(f"- Unique headings (fence-aware): {headings:,}")
    print(f"- Internal / external links: {internal:,} / {external:,}")
    print(f"- OSINT source entries: {sources:,}")
    print("- Source tiers: " + ", ".join(f"{tier}={count}" for tier, count in tiers.items()))
    print(f"- Bundles reconciled across bundle.py, README, and module 10: {bundles}")
    print("- Context budget word counts match disk: passed")
    print("- Register row completeness and workflow-pack ID resolution: passed")
    print("- Privacy, unfinished-marker, emoji, HTTPS, fence, inventory, terminology, and release-control checks: passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
