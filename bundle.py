#!/usr/bin/env python3
"""Assemble a selected module set into one attachment-ready Markdown file.

Many approved assistants accept a small number of attachments and no repository
access. This tool turns a bundle into a single self-describing file, rewrites
cross-module links so they resolve inside that file, and explicitly marks every
reference to a module that was not included. It never edits the toolkit itself.

Usage:
    python3 bundle.py --list
    python3 bundle.py --bundle research
    python3 bundle.py --modules 00,03,07,09 --name mailbox-lite
    python3 bundle.py --bundle full --budget 120000

Output is deterministic: identical inputs produce a byte-identical file.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TOOLKIT = ROOT / "toolkit"
DEFAULT_OUT = ROOT / "build"
REPO_URL = "https://github.com/maxmoran23/simple-toolkit"

# Characters per token. A deliberately coarse public estimate used only to warn
# about attachment limits; it is not a tokenizer and must not be cited as one.
CHARS_PER_TOKEN = 4

# The controlling bundle registry. `toolkit/10-use-case-recipes.md` is the
# operational index; README and module 10 must agree with this table, which
# validate.py enforces.
BUNDLES: dict[str, dict[str, object]] = {
    "core": {
        "label": "Core analysis",
        "modules": ["00", "07", "09"],
        "fits": "provided materials, no external research or structured population",
    },
    "research": {
        "label": "Research and OSINT",
        "modules": ["00", "01", "02", "07", "09"],
        "fits": "public-source research, regulatory scans, background intelligence",
    },
    "mailbox": {
        "label": "Mailbox intelligence",
        "modules": ["00", "03", "06", "07", "09"],
        "fits": "inbox, shared mailbox, chat, ticket, or intake corpus",
    },
    "entity": {
        "label": "Entity and financial-crime",
        "modules": ["00", "01", "02", "04", "05", "07", "09"],
        "fits": "entity, sanctions/PEP, adverse information, typology, case review",
    },
    "investigation": {
        "label": "Investigation and case review",
        "modules": ["00", "01", "02", "04", "05", "06", "07", "09"],
        "fits": "case work that also depends on structured transaction or record data",
    },
    "controls": {
        "label": "Data and controls",
        "modules": ["00", "05", "06", "07", "09"],
        "fits": "controls, testing, CDEs, lineage, issues, model/data review",
    },
    "reporting": {
        "label": "Reporting and dashboards",
        "modules": ["00", "06", "07", "09"],
        "fits": "memo, workbook, deck, dashboard, or maintained tracker",
    },
    "operation": {
        "label": "Maintained operation",
        "modules": ["00", "06", "08", "09", "11"],
        "fits": "recurring tracker or monitored workflow; add the domain modules the task needs",
    },
    "full": {
        "label": "Full system",
        "modules": [f"{n:02d}" for n in range(12)],
        "fits": "project knowledge base or complex cross-domain operation",
    },
}

ROOT_DOCS = {"README.md", "AGENTS.md"}
PLAIN_FILES = {"LICENSE", "NOTICE"}
LINK = re.compile(r"(?P<bang>!?)\[(?P<text>[^\]\n]*)\]\((?P<target>[^)\n]+)\)")


def module_files() -> dict[str, Path]:
    """Map two-digit module number to its file, derived from disk."""
    found: dict[str, Path] = {}
    for path in sorted(TOOLKIT.glob("*.md")):
        match = re.match(r"(\d{2})-", path.name)
        if match:
            found[match.group(1)] = path
    return found


def module_title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def anchor_for(number: str) -> str:
    return f"module-{number}"


def release_string() -> str:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    match = re.search(r"Current release: `(?P<v>[^`]+)`", text)
    return match.group("v") if match else "unversioned"


def resolve_target(target: str) -> tuple[str | None, str]:
    """Classify a link target. Returns (kind, fragment).

    kind is a module number, a root document name, a plain file name, or None
    when the link is external or unrecognized.
    """
    path_part, _, fragment = target.partition("#")
    path_part = path_part.strip()
    if not path_part:
        return None, fragment
    if "://" in path_part or path_part.startswith("mailto:"):
        return None, fragment
    name = path_part.split("/")[-1]
    match = re.match(r"(\d{2})-.*\.md$", name)
    if match:
        return match.group(1), fragment
    if name in ROOT_DOCS or name in PLAIN_FILES:
        return name, fragment
    return None, fragment


def rewrite_links(
    text: str, included: set[str], files: dict[str, Path]
) -> tuple[str, int, int]:
    """Point in-bundle links at in-file anchors; flag out-of-bundle links.

    Out-of-bundle links keep a working absolute target so the reader can still
    reach the source, but carry a `(not loaded)` marker so neither a person nor
    an assistant treats the referenced rule as available context.

    Returns the rewritten text plus counts of internal rewrites and of
    references marked as not loaded.
    """
    rewired = 0
    flagged = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal rewired, flagged
        target = match.group("target").strip()
        label = match.group("text")
        kind, _ = resolve_target(target)
        if kind is None:
            return match.group(0)

        if kind in included:
            rewired += 1
            return f"[{label}](#{anchor_for(kind)})"

        flagged += 1
        if kind in ROOT_DOCS or kind in PLAIN_FILES:
            return f"[{label}]({REPO_URL}/blob/main/{kind}) (not loaded)"
        path = files.get(kind)
        location = f"toolkit/{path.name}" if path else "toolkit/"
        return f"[{label}]({REPO_URL}/blob/main/{location}) (not loaded)"

    return LINK.sub(replace, text), rewired, flagged


def demote_headings(text: str) -> str:
    """Drop the module H1 and push every remaining heading down one level.

    The bundle supplies its own H1, so module headings shift to keep a single
    document outline. Text inside fenced blocks is left untouched.
    """
    out: list[str] = []
    in_fence = False
    seen_h1 = False
    for line in text.splitlines():
        if re.match(r"^\s*(`{3,}|~{3,})", line):
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence and line.startswith("# ") and not seen_h1:
            seen_h1 = True
            continue
        if not in_fence and re.match(r"^#{1,5} ", line):
            out.append("#" + line)
            continue
        out.append(line)
    return "\n".join(out)


def build(modules: list[str], name: str, budget: int | None) -> tuple[str, dict[str, int]]:
    files = module_files()
    missing = [m for m in modules if m not in files]
    if missing:
        raise SystemExit(f"error: unknown module(s): {', '.join(missing)}")

    included = set(modules)
    release = release_string()

    parts: list[str] = []
    total_rewired = 0
    total_flagged = 0

    contents: list[str] = []
    for number in modules:
        path = files[number]
        title = module_title(path)
        contents.append(f"| `{number}` | {title} | [jump](#{anchor_for(number)}) |")

    header = [
        f"# Simple Toolkit — {name} bundle",
        "",
        "Generated file. Do not hand-edit; regenerate with `bundle.py` instead.",
        "",
        f"- Source release: `{release}`",
        f"- Source repository: {REPO_URL}",
        f"- Modules included: {', '.join(f'`{m}`' for m in modules)}",
        "",
        "This bundle contains only the modules listed below. A link marked",
        "`(not loaded)` points to a real file in the source repository whose content",
        "is **not** in this bundle: do not treat it as available guidance or infer",
        "what it says. If a task depends on an absent module, load that module before",
        "relying on the rule.",
        "",
        "| Module | Title | Location |",
        "|---|---|---|",
        *contents,
        "",
    ]
    parts.append("\n".join(header))

    for number in modules:
        path = files[number]
        title = module_title(path)
        raw = path.read_text(encoding="utf-8")
        body, rewired, flagged = rewrite_links(raw, included, files)
        total_rewired += rewired
        total_flagged += flagged
        parts.append(
            f'<a id="{anchor_for(number)}"></a>\n\n'
            f"## Module {number} — {title}\n\n"
            f"{demote_headings(body).strip()}\n"
        )

    text = "\n".join(parts).rstrip() + "\n"
    stats = {
        "modules": len(modules),
        "chars": len(text),
        "words": len(text.split()),
        "lines": len(text.splitlines()),
        "tokens": len(text) // CHARS_PER_TOKEN,
        "links_rewired": total_rewired,
        "links_flagged": total_flagged,
    }
    if budget is not None and stats["tokens"] > budget:
        stats["over_budget"] = stats["tokens"] - budget
    return text, stats


def list_bundles() -> None:
    files = module_files()
    print(f"{'Bundle':<15} {'Modules':<32} {'~Tokens':>9}  Fits")
    print("-" * 100)
    for key, spec in BUNDLES.items():
        mods = list(spec["modules"])  # type: ignore[arg-type]
        chars = sum(len(files[m].read_text(encoding="utf-8")) for m in mods if m in files)
        print(
            f"{key:<15} {','.join(mods):<32} {chars // CHARS_PER_TOKEN:>9,}  {spec['fits']}"
        )
    print(
        "\nToken figures are coarse estimates at "
        f"{CHARS_PER_TOKEN} characters per token, for attachment sizing only."
    )


def selftest() -> int:
    """Assert the invariants every generated bundle must hold.

    A bundle is handed to an assistant as a single source of truth, so a dangling
    module link or a lost heading level is a correctness defect, not cosmetics.
    """
    failures: list[str] = []
    # A surviving relative target is the defect. Absolute links to files that were
    # deliberately left out are correct: they are marked as not included and still
    # reach the real file.
    dangling = re.compile(r"\]\((?!#|https://|mailto:)[^)\n]*\.md[^)\n]*\)")

    for key, spec in sorted(BUNDLES.items()):
        modules = list(spec["modules"])  # type: ignore[arg-type]
        text, stats = build(modules, key, None)

        again, _ = build(modules, key, None)
        if again != text:
            failures.append(f"{key}: output is not deterministic")

        for match in dangling.finditer(text):
            failures.append(f"{key}: unresolved file link {match.group(0)}")

        in_fence = False
        h1 = 0
        for line in text.splitlines():
            if re.match(r"^\s*(`{3,}|~{3,})", line):
                in_fence = not in_fence
                continue
            if not in_fence and line.startswith("# "):
                h1 += 1
        if h1 != 1:
            failures.append(f"{key}: expected exactly 1 document H1, found {h1}")

        for number in modules:
            if f'<a id="{anchor_for(number)}"></a>' not in text:
                failures.append(f"{key}: missing anchor for module {number}")

        print(
            f"  {key:<15} modules={stats['modules']:<3} "
            f"~{stats['tokens']:>7,} tok  rewired={stats['links_rewired']:<4} "
            f"flagged={stats['links_flagged']}"
        )

    if failures:
        print(f"\nFAIL: {len(failures)} bundle self-test error(s)")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"\nPASS: {len(BUNDLES)} bundles build deterministically with no unresolved links")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Assemble Simple Toolkit modules into one attachable file."
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--bundle", choices=sorted(BUNDLES), help="named bundle to build")
    group.add_argument("--modules", help="comma-separated module numbers, e.g. 00,03,07")
    group.add_argument("--list", action="store_true", help="list bundles and their sizes")
    group.add_argument("--selftest", action="store_true", help="verify every bundle builds correctly")
    parser.add_argument("--name", help="override the output name")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="output directory")
    parser.add_argument("--budget", type=int, help="warn if the bundle exceeds this token estimate")
    parser.add_argument("--stdout", action="store_true", help="write to stdout instead of a file")
    args = parser.parse_args()

    if args.selftest:
        return selftest()

    if args.list or not (args.bundle or args.modules):
        list_bundles()
        return 0

    if args.bundle:
        modules = list(BUNDLES[args.bundle]["modules"])  # type: ignore[arg-type]
        name = args.name or args.bundle
    else:
        modules = [m.strip().zfill(2) for m in args.modules.split(",") if m.strip()]
        name = args.name or "custom"

    seen: set[str] = set()
    ordered = [m for m in sorted(modules) if not (m in seen or seen.add(m))]

    text, stats = build(ordered, name, args.budget)

    if args.stdout:
        sys.stdout.write(text)
    else:
        args.out.mkdir(parents=True, exist_ok=True)
        destination = args.out / f"simple-toolkit-{name}.md"
        destination.write_text(text, encoding="utf-8")
        print(f"wrote {destination.relative_to(ROOT)}")

    print(
        f"- modules: {stats['modules']} ({', '.join(ordered)})\n"
        f"- lines / words / characters: {stats['lines']:,} / {stats['words']:,} / {stats['chars']:,}\n"
        f"- estimated tokens: ~{stats['tokens']:,} (at {CHARS_PER_TOKEN} chars/token)\n"
        f"- cross-module links rewired to in-file anchors: {stats['links_rewired']:,}\n"
        f"- references marked as not included: {stats['links_flagged']:,}"
    )
    if "over_budget" in stats:
        print(
            f"WARNING: bundle exceeds the stated budget by ~{stats['over_budget']:,} tokens.\n"
            "         Drop a module or split the work. Content was NOT truncated:\n"
            "         a silently shortened bundle would misrepresent its own coverage."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
