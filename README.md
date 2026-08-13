# Simple Toolkit

A compact, agent-ready system library for audit-defensible institutional analysis.
It consolidates research, OSINT, communications review, financial-crime intelligence,
data quality, automation, quality assurance, and professional reporting into a small
set of large, reusable Markdown modules.

Current release: `v1.0.0` — 2026-08-13.

The package is designed for constrained work environments where a user can attach a
limited number of reference files to an approved assistant. It is not a monitoring
service, a screening system, a legal opinion, or an authorization to take action.

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
If attachment capacity is limited, use the smallest bundle that covers the work.

## Recommended module bundles

| Work type | Load these modules |
|---|---|
| Research or regulatory scan | `00`, `01`, `02`, `07`, `09` |
| Entity or counterparty assessment | `00`, `01`, `02`, `04`, `05`, `07`, `09` |
| Mailbox or escalation-intake review | `00`, `03`, `06`, `07`, `09` |
| Investigation or case review | `00`, `01`, `02`, `04`, `05`, `06`, `07`, `09` |
| Controls, testing, or issue remediation | `00`, `05`, `06`, `07`, `09` |
| Dashboard, report, workbook, or presentation | `00`, `06`, `07`, `09` |
| Recurring monitored workflow | `00`, relevant domain modules, `06`, `08`, `09`, `11` |
| Full institutional agent context | `AGENTS.md` plus all numbered modules |

Module numbers are identifiers, not execution order. The controlling order is:

`authority and scope -> evidence -> domain method -> data controls -> output -> QA -> action`

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
```

It enforces the fourteen-file Markdown inventory, internal-link resolution, HTTPS-only
external links, OSINT registry IDs and domain coverage, balanced code fences, canonical
confidence terminology, and public-repository hygiene. GitHub Actions runs the same gate
on every push and pull request. External sites can move or block automated clients, so
live source status remains a controlled maintenance task under module `11`, not a claim
made solely from an HTTP status check.

## License

MIT. See [`LICENSE`](LICENSE). Upstream notices are preserved in [`NOTICE`](NOTICE).
