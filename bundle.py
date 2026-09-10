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
import hashlib
import json
import os
import tempfile
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit, unquote

import markdown_utils as md

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
            number = match.group(1)
            if number in found:
                raise ValueError(f"duplicate module number: {number}")
            if path.is_symlink():
                raise ValueError(f"module must not be a symlink: {path.name}")
            found[number] = path
    return found


def module_title(path: Path, text: str | None = None) -> str:
    for line in (text if text is not None else path.read_text(encoding="utf-8")).splitlines():
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
    path_part = unquote(path_part.strip())
    fragment = unquote(fragment)
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


def section_map(number: str, text: str) -> dict[str, str]:
    return {anchor: anchor_for(number) if level == 1 else f"module-{number}-{anchor}"
            for _, level, _, anchor in md.headings(text)}


def rewrite_links(text: str, included: set[str], files: dict[str, Path],
                  current: str | None = None,
                  source_texts: dict[str, str] | None = None) -> tuple[str, int, int]:
    """Preserve section destinations and leave fenced/inline examples unchanged."""
    rewired = flagged = 0
    parts, cursor = [], 0
    for link in md.links(text):
        target = link.target
        kind, fragment = resolve_target(target)
        if target.startswith("#") and current:
            kind = current
        if kind is None:
            continue
        if kind in files and not target.startswith("#"):
            name = unquote(target.split("#", 1)[0]).split("/")[-1]
            if name != files[kind].name:
                raise ValueError(f"unknown linked module filename: {name}")
        label = ("!" if link.image else "") + f"[{link.label}]"
        if kind in included:
            anchor = anchor_for(kind)
            if fragment:
                mapping = section_map(kind, source_texts[kind] if source_texts is not None else files[kind].read_text(encoding="utf-8"))
                if fragment not in mapping:
                    raise ValueError(f"module {current or '?'}: missing section {kind}#{fragment}")
                anchor = mapping[fragment]
            replacement = f"{label}(#{anchor})"
            rewired += 1
        else:
            if kind in ROOT_DOCS or kind in PLAIN_FILES:
                location = kind
            else:
                path = files.get(kind)
                if path is None:
                    raise ValueError(f"unknown linked module: {kind}")
                location = f"toolkit/{path.name}"
            suffix = f"#{fragment}" if fragment else ""
            replacement = f"{label}({REPO_URL}/blob/main/{location}{suffix}) (not loaded)"
            flagged += 1
        parts.extend((text[cursor:link.start], replacement))
        cursor = link.end
    parts.append(text[cursor:])
    return "".join(parts), rewired, flagged


def demote_headings(text: str, number: str | None = None,
                    required: set[str] | None = None,
                    source_text: str | None = None) -> str:
    """Demote document headings and assign stable, module-scoped section IDs."""
    # Link rewriting can change visible heading text; identity belongs to the source.
    original = text if source_text is None else source_text
    heading_rows = {index: (level, label, anchor) for index, level, label, anchor in md.headings(original)}
    out = []
    seen_h1 = False
    for index, line in enumerate(text.splitlines()):
        heading = heading_rows.get(index)
        if heading:
            level, label, anchor = heading
            rendered = md.HEADING.match(line.rstrip())
            if rendered:
                label = rendered[2]
            if level == 1 and not seen_h1:
                seen_h1 = True
                continue
            if number and (required is None or anchor in required):
                out.append(f'<a id="module-{number}-{anchor}"></a>')
                out.append("")
            line = "#" * min(level + 1, 6) + " " + label
        out.append(line)
    return "\n".join(out)


def estimate_tokens(text: str) -> int:
    return (len(text) + CHARS_PER_TOKEN - 1) // CHARS_PER_TOKEN


def atomic_write(destination: Path, content: str) -> None:
    """Replace only after the complete UTF-8 payload is written successfully."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".simple-toolkit-", dir=destination.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
        os.replace(temporary, destination)
    finally:
        Path(temporary).unlink(missing_ok=True)


def source_domain_sections(text: str) -> dict[str, dict[str, object]]:
    """Locate complete registry tables using parsed headings, never text slicing guesses."""
    headings = list(md.headings(text))
    registry = next((i for i, row in enumerate(headings) if row[1:3] == (2, "8. Registry")), None)
    if registry is None:
        raise ValueError("source register is missing section 8. Registry")
    following = headings[registry + 1:]
    ending = next((row[0] for row in following if row[1] <= 2), len(text.splitlines()))
    starts = []
    for line, level, label, anchor in following:
        if line >= ending:
            break
        if level == 3:
            match = re.fullmatch(r"8\.([1-9][0-9]?) (.+)", label)
            if not match:
                raise ValueError(f"unrecognized source domain heading: {label}")
            starts.append((line, match[1].zfill(2), match[2], anchor))
    if not starts or len({row[1] for row in starts}) != len(starts):
        raise ValueError("source register needs distinct numbered domain tables")
    lines = text.splitlines(keepends=True)
    sections = {}
    for i, (start, code, label, anchor) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else ending
        section = "".join(lines[start:end])
        rows = len(re.findall(r"^\| \d{2}\.\d{3} \|", section, re.MULTILINE))
        if not rows:
            raise ValueError(f"source domain {code} has no source rows")
        sections[code] = {"title": label, "anchor": anchor, "start": start, "end": end,
                          "rows": rows, "estimated_tokens": estimate_tokens(section)}
    return sections


def select_source_domains(source_texts: dict[str, str], requested: list[str]) -> dict[str, object]:
    """Retain all register governance plus the requested tables and explicit dependencies."""
    if "02" not in source_texts:
        raise ValueError("--source-domains requires module 02 in the bundle")
    sections = source_domain_sections(source_texts["02"])
    if not requested or len(set(requested)) != len(requested):
        raise ValueError("select at least one source domain, without duplicates")
    unknown = [code for code in requested if code not in sections]
    if unknown:
        raise ValueError(f"unknown source domain(s): {', '.join(unknown)}; use --list-source-domains")
    original = source_texts["02"]
    lines = original.splitlines(keepends=True)
    owners = {anchor: code for line, _, _, anchor in md.headings(original)
              for code, row in sections.items() if row["start"] <= line < row["end"]}
    retained = set(requested)

    def subset() -> str:
        omitted = {line for code, row in sections.items() if code not in retained
                   for line in range(row["start"], row["end"])}
        return "".join(line for i, line in enumerate(lines) if i not in omitted)

    while True:
        source_texts["02"] = subset()
        needed = set()
        for number, text in source_texts.items():
            for link in md.links(text):
                kind, fragment = resolve_target(link.target)
                if link.target.startswith("#"):
                    kind = number
                if kind == "02" and fragment in owners:
                    needed.add(owners[fragment])
        if needed <= retained:
            break
        retained |= needed
    return {"requested_domains": sorted(requested), "included_domains": sorted(retained),
            "dependency_domains": sorted(retained - set(requested)),
            "omitted_domains": sorted(set(sections) - retained),
            "included_source_rows": sum(sections[code]["rows"] for code in retained),
            "total_source_rows": sum(row["rows"] for row in sections.values()),
            "selection_rule": "complete domain tables; retain explicit fragment dependencies and all non-registry guidance"}


def list_source_domains() -> None:
    files = module_files()
    for code, row in source_domain_sections(files["02"].read_text(encoding="utf-8")).items():
        print(f"{code}  {row['rows']:>3} sources  ~{row['estimated_tokens']:>5,} tokens  {row['title']}")
    print("Table sizes exclude retained governance and bundle overhead; estimates use characters/4.")


def build(modules: list[str], name: str, budget: int | None,
          source_domains: list[str] | None = None) -> tuple[str, dict[str, object]]:
    if not modules or len(set(modules)) != len(modules):
        raise ValueError("select at least one module, without duplicates")
    if not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_-]{0,63}", name):
        raise ValueError("name must be 1-64 letters, digits, hyphens or underscores")
    if budget is not None and budget <= 0:
        raise ValueError("budget must be positive")
    files = module_files()
    missing = [m for m in modules if m not in files]
    if missing:
        raise ValueError(f"unknown module(s): {', '.join(missing)}")

    # Freeze each input once so fingerprints describe the bytes actually assembled.
    raw_sources = {m: files[m].read_bytes() for m in modules}
    source_texts = {m: raw.decode("utf-8").replace("\r\n", "\n") for m, raw in raw_sources.items()}
    selection = select_source_domains(source_texts, source_domains) if source_domains is not None else None
    included = set(modules)
    required_sections: dict[str, set[str]] = {m: set() for m in modules}
    for source in modules:
        for link in md.links(source_texts[source]):
            kind, fragment = resolve_target(link.target)
            if link.target.startswith("#"):
                kind = source
            if kind in included and fragment:
                required_sections[kind].add(fragment)
    release = release_string()
    source_rows = [f"- `toolkit/{files[m].name}`: `{hashlib.sha256(raw_sources[m]).hexdigest()}`" for m in modules]

    parts: list[str] = []
    total_rewired = 0
    total_flagged = 0

    contents: list[str] = []
    for number in modules:
        path = files[number]
        title = module_title(path, source_texts[number])
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
        "- Required governance modules absent: " + (", ".join(f"`{m}`" for m in ("00", "09") if m not in included) or "none"),
        "",
        "Source SHA-256 fingerprints (identify input bytes; do not certify content quality):",
        *source_rows,
        "",
        "| Module | Title | Location |",
        "|---|---|---|",
        *contents,
        "",
    ]
    if selection is not None:
        header.extend([
            "### Focused source register",
            "",
            "- Requested source domains: " + ", ".join(selection["requested_domains"]),
            "- Included source domains: " + ", ".join(selection["included_domains"]),
            "- Domains added for explicit section dependencies: " + (", ".join(selection["dependency_domains"]) or "none"),
            "- Source domains omitted: " + (", ".join(selection["omitted_domains"]) or "none"),
            f"- Source rows included: {selection['included_source_rows']} of {selection['total_source_rows']}",
            "",
            "Only these domain tables are loaded. All source-selection rules, fallback chains,",
            "taxonomy, workflow packs, maintenance controls, and limitations remain intact.",
            "Those retained methods can name sources outside this selection. Load any additional",
            "domain the task requires before relying on its entries; selection does not establish",
            "complete task coverage or current source verification. Source hashes identify the",
            "complete original files; the output hash and domain selection identify this extract.",
            "",
        ])
    parts.append("\n".join(header))

    for number in modules:
        path = files[number]
        title = module_title(path, source_texts[number])
        raw = source_texts[number]
        body, rewired, flagged = rewrite_links(raw, included, files, number, source_texts)
        total_rewired += rewired
        total_flagged += flagged
        parts.append(
            f'<a id="{anchor_for(number)}"></a>\n\n'
            f"## Module {number} — {title}\n\n"
            f"{demote_headings(body, number, required_sections[number], raw).strip()}\n"
        )

    text = "\n".join(parts).rstrip() + "\n"
    stats = {
        "modules": len(modules),
        "chars": len(text),
        "words": len(text.split()),
        "lines": len(text.splitlines()),
        "tokens": estimate_tokens(text),
        "links_rewired": total_rewired,
        "links_flagged": total_flagged,
    }
    if selection is not None:
        stats["source_selection"] = selection
    if budget is not None and stats["tokens"] > budget:
        stats["over_budget"] = stats["tokens"] - budget
    return text, stats


def list_bundles() -> None:
    files = module_files()
    print(f"{'Bundle':<15} {'Modules':<32} {'~Tokens':>9}  Fits")
    print("-" * 100)
    for key, spec in BUNDLES.items():
        mods = list(spec["modules"])  # type: ignore[arg-type]
        _, stats = build(mods, key, None)
        print(
            f"{key:<15} {','.join(mods):<32} {stats['tokens']:>9,}  {spec['fits']}"
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

        for match in dangling.finditer(md.visible_text(text)):
            failures.append(f"{key}: unresolved file link {match.group(0)}")

        h1 = sum(level == 1 for _, level, _, _ in md.headings(text))
        ids = md.anchors(text)
        for link in md.links(text):
            if link.target.startswith("#") and link.target[1:] not in ids:
                failures.append(f"{key}: unresolved fragment {link.target}")
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
    group.add_argument("--list-source-domains", action="store_true", help="list module 02 domain selectors and table sizes")
    group.add_argument("--selftest", action="store_true", help="verify every bundle builds correctly")
    parser.add_argument("--source-domains", help="include only selected module 02 tables, e.g. 01,16; retains all register governance")
    parser.add_argument("--name", help="override the output name")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="output directory")
    parser.add_argument("--budget", type=int, help="warn if the bundle exceeds this token estimate")
    parser.add_argument("--strict-budget", action="store_true", help="exit 1 without output if over --budget")
    parser.add_argument("--manifest", action="store_true", help="write a deterministic JSON provenance sidecar")
    parser.add_argument("--stdout", action="store_true", help="write to stdout instead of a file")
    args = parser.parse_args()
    if args.budget is not None and args.budget <= 0:
        parser.error("--budget must be positive")
    if args.strict_budget and args.budget is None:
        parser.error("--strict-budget requires --budget")
    if args.manifest and args.stdout:
        parser.error("--manifest requires file output")

    if args.source_domains is not None and not (args.bundle or args.modules):
        parser.error("--source-domains requires --bundle or --modules")
    if args.list_source_domains:
        try:
            list_source_domains()
        except (ValueError, OSError) as exc:
            parser.error(str(exc))
        return 0
    if args.selftest:
        return selftest()

    if args.list or not (args.bundle or args.modules):
        list_bundles()
        return 0

    if args.bundle:
        modules = list(BUNDLES[args.bundle]["modules"])  # type: ignore[arg-type]
        name = args.name or args.bundle
    else:
        tokens = args.modules.split(",")
        if any(not re.fullmatch(r"\d{1,2}", m.strip()) for m in tokens):
            parser.error("--modules requires comma-separated one- or two-digit module numbers")
        modules = [m.strip().zfill(2) for m in tokens]
        name = args.name or "custom"

    seen: set[str] = set()
    ordered = [m for m in sorted(modules) if not (m in seen or seen.add(m))]

    try:
        selected_domains = [code.strip() for code in args.source_domains.split(",")] if args.source_domains is not None else None
        text, stats = build(ordered, name, args.budget, selected_domains)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    if args.strict_budget and "over_budget" in stats:
        print(f"error: ~{stats['tokens']:,} estimated tokens exceeds budget {args.budget:,}; no output written", file=sys.stderr)
        return 1
    report = sys.stderr if args.stdout else sys.stdout

    if args.stdout:
        sys.stdout.write(text)
    else:
        destination = args.out / f"simple-toolkit-{name}.md"
        atomic_write(destination, text)
        print(f"wrote {destination}")
        if args.manifest:
            files = module_files()
            payload = {"schema_version": 1, "release": re.search(r"Source release: `([^`]+)`", text)[1], "name": name,
                       "modules": ordered, "statistics": stats,
                       "output_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                       "token_estimate_method": f"ceil(characters/{CHARS_PER_TOKEN}); not a tokenizer",
                       "sources": [{"path": path, "sha256": digest} for path, digest in re.findall(r"^- `(toolkit/[^`]+)`: `([0-9a-f]{64})`$", text, re.MULTILINE)]}
            atomic_write(destination.with_suffix(".json"), json.dumps(payload, sort_keys=True, indent=2) + "\n")

    print(
        f"- modules: {stats['modules']} ({', '.join(ordered)})\n"
        f"- lines / words / characters: {stats['lines']:,} / {stats['words']:,} / {stats['chars']:,}\n"
        f"- estimated tokens: ~{stats['tokens']:,} (at {CHARS_PER_TOKEN} chars/token)\n"
        f"- cross-module links rewired to in-file anchors: {stats['links_rewired']:,}\n"
        f"- references marked as not included: {stats['links_flagged']:,}", file=report
    )
    if "over_budget" in stats:
        print(
            f"WARNING: bundle exceeds the stated budget by ~{stats['over_budget']:,} tokens.\n"
            "         Drop a module or split the work. Content was NOT truncated:\n"
            "         a silently shortened bundle would misrepresent its own coverage.", file=report
        )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        # A downstream reader (for example head) may finish before the bundle.
        with open(os.devnull, "w") as sink:
            os.dup2(sink.fileno(), sys.stdout.fileno())
        sys.exit(0)
