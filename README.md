# Simple Toolkit

A compact, agent-ready system library for audit-defensible institutional analysis.
It consolidates research, OSINT, communications review, financial-crime intelligence,
data quality, automation, quality assurance, and professional reporting into a small
set of large, reusable Markdown modules.

Current release: `v1.3.1` — 2026-09-10.

The package is designed for constrained work environments where a user can attach a
limited number of reference files to an approved assistant. It is not a monitoring
service, a screening system, a legal opinion, or an authorization to take action.

## Focused Markdown attachment suites

For one clearly scoped review, use the companion [Markdown Analyst Toolkit](https://github.com/maxmoran23/markdown-analyst-toolkit). Its 30 topic suites each contain ten working attachments plus a README and build record. Each suite supplies a detailed method, fictional worked example, fixed report and workbook templates, and a complete offline dashboard with light and dark themes. The [offline suite finder](https://github.com/maxmoran23/markdown-analyst-toolkit/releases/download/v1.2.0/suite-finder.html) helps select a topic and copy the attachment prompt for the current stage. Nine process suites now cover detailed monitoring, tuning, validation, investigations, network flows, alert quality and lookbacks, with complete example records and calculation checks inside the Markdown. See the [process map](https://github.com/maxmoran23/markdown-analyst-toolkit/blob/main/docs/PROCESS-MAP.md) and [measured method depth](https://github.com/maxmoran23/markdown-analyst-toolkit/blob/main/docs/PROCESS-DEPTH.md).

Download one suite, attach its numbered files, and provide permitted inputs. The workflow needs no terminal, connector or agent builder; actual file creation is checked in the current session. Start with [the suite catalog](https://github.com/maxmoran23/markdown-analyst-toolkit#choose-the-decision-you-need-to-support) or [the plain-English guide](https://github.com/maxmoran23/markdown-analyst-toolkit/blob/main/docs/START-HERE.md).

## Why this repository exists

Large prompt libraries become difficult to operate when a single project requires
methods, domain references, output rules, quality controls, and deployment guidance
from many different folders. Simple Toolkit replaces that search problem with one
router and twelve numbered modules. Each module is broad enough to support a full
process, not just a one-off prompt.

The design goals are:

1. **Portable:** Markdown-first, assistant-agnostic, and usable without a runtime.
2. **Navigable:** fourteen Markdown files in total, with stable numbered names.
3. **Comprehensive:** supports end-to-end projects, recurring operations, and review.
4. **Evidence-led:** material claims remain traceable to source evidence.
5. **Human-governed:** consequential decisions and external writes require approval.
6. **Institution-ready:** outputs use restrained, professional, audit-friendly design.
7. **Public-safe:** no employer-specific methods, private data, credentials, or real
   customer records are included.

## Repository map

| File | Purpose | Load when |
|---|---|---|
| [`AGENTS.md`](AGENTS.md) | Machine-readable router and non-negotiable operating rules | Always for repository-aware agents |
| [`00-operating-system.md`](toolkit/00-operating-system.md) | Master task lifecycle, authority boundaries, evidence labels, severity, confidence, and handoff contract | Every substantial task |
| [`01-evidence-research-standard.md`](toolkit/01-evidence-research-standard.md) | Research planning, provenance, corroboration, claim ledgers, temporal validity, and reproducibility | Any research or synthesis task |
| [`02-osint-source-register.md`](toolkit/02-osint-source-register.md) | Tiered global register of official and high-value public sources, with selection and fallback rules | OSINT, regulatory, entity, jurisdiction, or intelligence work |
| [`03-mailbox-communications.md`](toolkit/03-mailbox-communications.md) | Complete mailbox and communications ingestion, threading, extraction, reconciliation, drafting, and refresh logic | Mailboxes, shared inboxes, chats, or escalation intake |
| [`04-intelligence-fincrime-frameworks.md`](toolkit/04-intelligence-fincrime-frameworks.md) | Typologies, risk lenses, indicators, intelligence frameworks, and domain decision trees | Financial-crime, fraud, sanctions, surveillance, crypto, or regulatory intelligence |
| [`05-investigation-control-methods.md`](toolkit/05-investigation-control-methods.md) | Investigation, screening, assessment, control design/testing, issue management, and decision documentation | Cases, reviews, controls, testing, or governance work |
| [`06-data-quality-governance.md`](toolkit/06-data-quality-governance.md) | Data contracts, CDEs, profiling, lineage, reconciliation, quality rules, incidents, and ownership | Data-heavy analysis or maintained trackers |
| [`07-output-templates.md`](toolkit/07-output-templates.md) | Unified content structures and corporate design rules for memos, reports, Word, PDF, Excel, slides, dashboards, and communications | Any file or polished report output |
| [`08-automation-orchestration.md`](toolkit/08-automation-orchestration.md) | State, idempotency, checkpoints, retries, fallbacks, recurring runs, observability, and gated self-repair | Repeatable or autonomous workflows |
| [`09-quality-assurance.md`](toolkit/09-quality-assurance.md) | Review procedures, release gates, sampling, evidence packages, issue severity, and sign-off | Before anything is distributed or operationalized |
| [`10-use-case-recipes.md`](toolkit/10-use-case-recipes.md) | End-to-end recipes and exact module bundles for common institutional projects | When choosing how to assemble the system |
| [`11-deployment-security-maintenance.md`](toolkit/11-deployment-security-maintenance.md) | Workstation setup, permissions, privacy, prompt-injection defense, versioning, maintenance, and source provenance | Installation, integration, administration, or updates |

## Fast start

1. Download or clone the repository into an approved location.
2. Give the assistant [`AGENTS.md`](AGENTS.md) as repository instructions when the
   environment supports it.
3. Load [`00-operating-system.md`](toolkit/00-operating-system.md) plus the modules in
   the relevant bundle below.
4. State the task, scope, approved sources, deliverable, deadline, and actions the
   assistant may or may not take.
5. Require the assistant to run the release gate in
   [`09-quality-assurance.md`](toolkit/09-quality-assurance.md) before delivery.

If the environment supports a project knowledge base, load all fourteen Markdown files.
If attachment capacity is limited, use the smallest bundle that covers the work. Check
the [context budget](#context-budget) first: the full package is roughly 190,000 tokens
and several bundles exceed what a constrained assistant will accept.

## Recommended module bundles

| Bundle | Modules | Approx. context | Fits |
|---|---|---|---|
| `core` | `00`, `07`, `09` | ~46k tokens | Provided materials; no external research or structured population |
| `reporting` | `00`, `06`, `07`, `09` | ~62k tokens | Memo, workbook, deck, dashboard, or maintained tracker |
| `controls` | `00`, `05`, `06`, `07`, `09` | ~73k tokens | Controls, testing, CDEs, lineage, issues, model/data review |
| `operation` | `00`, `06`, `08`, `09`, `11` | ~78k tokens | Recurring tracker or monitored workflow; add the domain modules the task needs |
| `mailbox` | `00`, `03`, `06`, `07`, `09` | ~76k tokens | Inbox, shared mailbox, chat, ticket, or intake corpus |
| `research` | `00`, `01`, `02`, `07`, `09` | ~99k tokens | Public-source research, regulatory scans, background intelligence |
| `entity` | `00`, `01`, `02`, `04`, `05`, `07`, `09` | ~123k tokens | Entity, sanctions/PEP, adverse information, typology, case review |
| `investigation` | `00`, `01`, `02`, `04`, `05`, `06`, `07`, `09` | ~139k tokens | Case work that also depends on structured transaction or record data |
| `full` | `00`–`11` | ~190k tokens | Project knowledge base or complex cross-domain operation |

This table is the same registry used by [`10-use-case-recipes.md`](toolkit/10-use-case-recipes.md)
and by `bundle.py`. Validation fails if the three disagree.

Module numbers are identifiers, not execution order. The controlling order is:

`authority and scope -> evidence -> domain method -> data controls -> output -> QA -> action`

## Context budget

The package is large enough that a bundle can exceed what a constrained assistant
will accept. An assistant that silently truncates attached context does not warn
the user, so a half-loaded bundle can produce confident output while the rules
that would have blocked it were never read. Check the size before loading.

| Module | Words | Approx. tokens |
|---|---:|---:|
| `00-operating-system.md` | 6,870 | ~11,889 |
| `01-evidence-research-standard.md` | 7,447 | ~13,442 |
| `02-osint-source-register.md` | 21,650 | ~39,124 |
| `03-mailbox-communications.md` | 8,203 | ~14,749 |
| `04-intelligence-fincrime-frameworks.md` | 6,896 | ~12,955 |
| `05-investigation-control-methods.md` | 6,260 | ~11,528 |
| `06-data-quality-governance.md` | 8,242 | ~15,524 |
| `07-output-templates.md` | 7,037 | ~12,372 |
| `08-automation-orchestration.md` | 5,586 | ~10,716 |
| `09-quality-assurance.md` | 11,285 | ~21,284 |
| `10-use-case-recipes.md` | 4,604 | ~8,694 |
| `11-deployment-security-maintenance.md` | 8,779 | ~17,003 |
| **All twelve modules** | **102,859** | **~189,280** |

Token figures are coarse estimates at four characters per token, published for
attachment sizing only. They are not a tokenizer result and must not be cited as
a measured value. Word counts are exact and checked by `validate.py`.

Practical consequences:

- `02-osint-source-register.md` is roughly a fifth of the package. Load it only
  when the task actually needs source discovery, and prefer the workflow source
  packs in its section 9 over the full registry.
- If a bundle does not fit, narrow the task or divide it into reconciled stages.
  Keep the operating contract and QA controls with each substantive stage.
- When the assistant accepts few attachments, build one file instead.

## Building a single-file bundle

Constrained environments often allow only a small number of attachments and no
repository access. `bundle.py` assembles any bundle into one Markdown file:

```bash
python3 bundle.py --list                        # bundles and their sizes
python3 bundle.py --bundle mailbox              # write build/simple-toolkit-mailbox.md
python3 bundle.py --modules 00,04,07,09 --name adhoc
python3 bundle.py --bundle research --budget 60000 --strict-budget
python3 bundle.py --bundle core --manifest       # Markdown plus provenance sidecar
python3 context_report.py                       # measured words and size estimates
```

The assembler preserves section destinations and code examples, rewrites cross-module links to in-file anchors, and explicitly
marks every reference to a module that was not included, so a bundle cannot
imply guidance it does not carry. Output is deterministic and written to the
ignored `build/` directory; it is never committed. The tool is a convenience
for transport only — the modules remain directly usable without it, and it adds
no analytical rule that is not already in the toolkit.

`--budget` warns; `--strict-budget` rejects an oversized bundle before creating output.
Both use an estimate, so reserve space for task inputs and the answer. `--stdout`
emits only the Markdown, suitable for piping. `--manifest` writes source and output
SHA-256 hashes, module selection, and size metadata alongside the attachment. These
prove file integrity and provenance, not that an assistant read or followed the content.
Custom selections report missing operating or QA modules explicitly.

Use `python3 context_report.py --json` for machine-readable size data. The module
budget measures raw files; the bundle tables and `--list` include assembly overhead.
Section anchors are added only where a link needs them to limit transport cost.

### Focus the source register

Keep the complete analytical methods and load only the source-domain tables relevant
to the task. Domain codes come from module `02`'s numbered taxonomy; `01` below means
sanctions sources and `16` means digital-asset sources, not module numbers.

```bash
python3 bundle.py --list-source-domains
python3 bundle.py --bundle research --source-domains 01,16 --name research-focused --manifest
python3 context_report.py --source-domains 01,16 --json
```

`--source-domains` retains all register guidance outside section `8` and complete tables
for the selected domains. It automatically adds domains targeted by explicit section
links in the included guidance, repeating until those dependencies resolve. The bundle
and its manifest identify requested, added, included, and omitted domains plus exact
source-row counts. Whole-file source hashes identify the original inputs; the output
hash identifies the assembled extract. Without this option, all domain tables remain.
Unknown, empty, duplicate, or absent-module selections fail before writing output.

The retained taxonomy and workflow packs can mention sources outside the selected
tables. These references do not mean those entries were loaded: add every domain the
actual task needs. Domain selection does not infer jurisdiction coverage, refresh any
source, or establish a complete investigation. Explicit section dependencies are
resolved; source IDs mentioned in prose do not trigger automatic expansion. Combine
with `--budget` and `--strict-budget` to size the actual focused assembly before writing.

## Copy-ready task brief

```text
Use Simple Toolkit for this assignment.

Objective:
Decision or audience:
In scope:
Out of scope:
Inputs and approved sources:
Time period and as-of date:
Required coverage or population:
Deliverable and file type:
Materiality or severity threshold:
Actions you may take:
Actions requiring approval:
Deadline:

Before analysis, return a short preflight that states:
1. the interpreted objective and decision;
2. the population, source, and time boundaries;
3. any blocking gaps or assumptions;
4. the planned evidence and reconciliation controls;
5. the proposed output and release gate.

Do not treat absence of evidence as evidence of absence. Do not invent facts,
citations, records, system access, or completed actions. Label observed, reported,
inferred, and projected content distinctly. Preserve evidence pointers. Require human
approval before consequential external writes or regulated decisions.
```

## Operating model

Simple Toolkit separates five things that assistants often blur:

| Layer | Question | Controlling modules |
|---|---|---|
| Authority | What may the assistant access, decide, or change? | `00`, `11` |
| Evidence | What supports each claim, and how current is it? | `01`, `02`, `03` |
| Method | Which analytical or domain framework applies? | `04`, `05`, `06` |
| Delivery | What artifact should be produced and how should it look? | `07`, `10` |
| Assurance | How is completeness, accuracy, and release readiness demonstrated? | `08`, `09` |

The assistant may draft, classify, reconcile, calculate, and recommend within the
approved scope. It must not imply that a draft is an approved decision, that a public
source is current without checking its date, or that a message/list/system was reviewed
when access was incomplete.

## Professional output standard

The default visual language is a restrained institutional light theme: white and warm
gray surfaces, navy hierarchy, one muted blue or teal accent, limited semantic red and
amber, compact tables, real charts, clear source notes, and strong print behavior.

The package intentionally rejects novelty-first dashboard conventions such as animated
backgrounds, glassmorphism, cartoon illustrations, decorative gauges, excessive rounded
cards, neon palettes, achievement badges, and interactions with no analytical purpose.
Interactive outputs should still include useful filtering, drill-through, source links,
data-freshness indicators, accessible keyboard behavior, and export functions when the
environment permits them.

## Safety and limitations

- Public sources can be incomplete, stale, mistranslated, or wrong. Verify high-impact
  findings against the issuing body or original record.
- A source register is a discovery and collection aid; it is not a substitute for an
  approved screening utility, licensed database, legal advice, or a formal records
  system.
- No automated output should directly clear a sanctions or screening hit, file a
  regulatory report, close an investigation, change a customer relationship, send an
  external communication, or modify a controlled system without authorized review.
- Do not place confidential data into an assistant or connector unless the environment,
  purpose, retention, and access path are approved for that data class.
- Links and regulatory regimes change. Apply the maintenance checks in module `11`.

## Provenance

This repository is a clean-room consolidation and expansion of reusable public methods
from the `analyst-toolkit` and `Claude-Agent-Fleet` projects. The source repositories
remain separate and unchanged. Module `11` records the source snapshot and maps the
major source directories to their consolidated destination.

## Validation

The repository carries a pure-standard-library validation gate:

```bash
python3 validate.py
python3 bundle.py --selftest
python3 linkcheck.py --selftest
python3 -m unittest discover -s tests -v
```

It enforces the fourteen-file Markdown inventory, internal-link resolution, HTTPS-only
external links, OSINT registry IDs, domain coverage, nine-cell row completeness, and
workflow-pack ID resolution, balanced code fences, canonical confidence terminology,
fence-aware duplicate-heading detection, agreement between the bundle registry in
`bundle.py` and both published bundle tables, agreement between the published context
budget and the files on disk, release-record consistency, and public-repository
hygiene. GitHub Actions runs the same gate on every push and pull request. The offline regression suite includes real local HTTP responses, redirect controls,
malformed input, fragment resolution, code preservation, and budget rejection. A separate
on-demand reporter, `linkcheck.py`, probes register URLs and reports reachability only,
recording anti-bot denials as an access outcome rather than source retirement; it is
deliberately kept out of continuous integration. External sites can move or block
automated clients, so live source status remains a controlled maintenance task under
module `11`, not a claim made solely from an HTTP status check.

## License

MIT. See [`LICENSE`](LICENSE). Upstream notices are preserved in [`NOTICE`](NOTICE).
