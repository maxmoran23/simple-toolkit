#!/usr/bin/env python3
"""Report exact module words and estimated raw/assembled context, without edits."""
from __future__ import annotations

import argparse
import json

import bundle


def report() -> dict:
    modules = []
    for number, path in bundle.module_files().items():
        text = path.read_text(encoding="utf-8")
        modules.append({"module": number, "file": path.name, "words": len(text.split()),
                        "characters": len(text), "estimated_tokens": bundle.estimate_tokens(text)})
    bundles = []
    for key, spec in bundle.BUNDLES.items():
        _, stats = bundle.build(list(spec["modules"]), key, None)
        bundles.append({"bundle": key, "modules": spec["modules"], **stats})
    return {"schema_version": 1, "method": "ceil(Unicode characters/4), not a tokenizer",
            "modules": modules, "bundles": bundles,
            "total_words": sum(row["words"] for row in modules),
            "raw_module_tokens": sum(row["estimated_tokens"] for row in modules)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit machine-readable counts")
    args = parser.parse_args()
    payload = report()
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print("| Module | Words | Approx. tokens |\n|---|---:|---:|")
        for row in payload["modules"]:
            print(f"| `{row['file']}` | {row['words']:,} | ~{row['estimated_tokens']:,} |")
        print(f"| **All twelve modules** | **{payload['total_words']:,}** | **~{payload['raw_module_tokens']:,}** |")
        print("\nAssembled bundles include navigation, provenance, and transport overhead:")
        for row in payload["bundles"]:
            print(f"{row['bundle']}: ~{round(row['tokens']/1000)}k ({row['tokens']:,} estimated tokens)")
        print(f"\nMethod: {payload['method']}. No files modified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
