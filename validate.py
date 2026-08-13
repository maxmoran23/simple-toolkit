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

REQUIRED_ROOT_FILES = {"README.md", "AGENTS.md", "LICENSE", ".gitignore"}
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
        if ".git" not in path.parts
    }


def check_inventory(files: dict[str, Path], errors: list[str]) -> None:
    actual = set(files)
    missing = sorted(EXPECTED_MARKDOWN - actual)
    extra = sorted(actual - EXPECTED_MARKDOWN)
    if missing:
        fail(errors, f"missing Markdown files: {', '.join(missing)}")
    if extra:
        fail(errors, f"unexpected Markdown files: {', '.join(extra)}")
    for name in sorted(REQUIRED_ROOT_FILES):
        if not (ROOT / name).is_file():
            fail(errors, f"missing required root file: {name}")


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


def main() -> int:
    errors: list[str] = []
    files = markdown_files()
    check_inventory(files, errors)
    lines, words = check_text(files, errors)
    internal, external = check_links(files, errors)
    check_readme(files, errors)
    sources, tiers = check_registry(files, errors)
    check_terminology(files, errors)

    if errors:
        print(f"FAIL: {len(errors)} validation error(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: Simple Toolkit validation")
    print(f"- Markdown files: {len(files)}")
    print(f"- Lines / words: {lines:,} / {words:,}")
    print(f"- Internal / external links: {internal:,} / {external:,}")
    print(f"- OSINT source entries: {sources:,}")
    print("- Source tiers: " + ", ".join(f"{tier}={count}" for tier, count in tiers.items()))
    print("- Privacy, unfinished-marker, emoji, HTTPS, fence, inventory, and terminology checks: passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
