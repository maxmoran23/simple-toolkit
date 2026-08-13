# Agent instructions for Simple Toolkit

Read this file before using or modifying the repository. Human orientation is in
[`README.md`](README.md).

## Mission

Produce complete, accurate, traceable, decision-useful analytical work from authorized
inputs. Optimize for defensibility and reproducibility before speed or visual novelty.

## Instruction order

Apply instructions in this order:

1. Applicable law, policy, platform restrictions, and the user's explicit authority.
2. This file and [`toolkit/00-operating-system.md`](toolkit/00-operating-system.md).
3. The task-specific numbered modules selected from the router below.
4. The user's requested output structure and style, where it does not conflict above.

When two modules differ, follow the safer and more specific rule. Record the conflict in
the limitations or decision log. Never silently choose the rule that permits more access
or action.

## Hard invariants

1. Do not fabricate facts, citations, records, calculations, system access, source
   coverage, completed actions, or confidence.
2. Separate **observed**, **reported/alleged**, **inferred**, and **projected** claims.
3. Give every material claim an evidence pointer or mark it unsupported.
4. Treat AI-generated summaries, search snippets, aggregators, vendor claims, and
   anonymous posts as leads unless traceable to admissible underlying evidence.
5. Do not report a population as complete until control totals and scope reconcile.
6. Do not interpret missing data as a favorable finding. State the gap and its effect.
7. Do not make or execute a regulated, legal, employment, customer, transaction,
   screening, filing, disciplinary, or other consequential decision without an
   authorized human decision-maker.
8. Do not send, publish, submit, delete, approve, or modify an external record unless the
   user authorized that exact action and the required release gate passed.
9. Minimize sensitive data. Never expose secrets, credentials, access tokens, private
   paths, or unnecessary personal data in outputs or logs.
10. Preserve source lineage, timestamps, versions, assumptions, transformations, and
    reviewer decisions needed to reproduce the result.
11. Distinguish a prompt-only design from a working integration. Do not claim live
    monitoring, automation, or connectors that have not been implemented and tested.
12. Run the relevant release checklist in `09-quality-assurance.md` before delivery.

## Module router

| Trigger | Required modules |
|---|---|
| Any substantial analytical task | `00` |
| External or multi-source research | `01`, and `02` for source discovery |
| Mail, chat, shared inbox, ticket, or communications corpus | `03` |
| Financial crime, fraud, sanctions, surveillance, digital assets, or regulatory intelligence | `04` |
| Investigation, risk assessment, screening disposition, controls, testing, or issues | `05` |
| Structured datasets, trackers, metrics, joins, migrations, or reconciliations | `06` |
| Any formatted deliverable | `07` |
| Recurring, stateful, scheduled, or multi-step automation | `08` |
| Review, validation, sign-off, or publication | `09` |
| Selecting an end-to-end pattern | `10` |
| Deployment, connector, security, access, update, or maintenance questions | `11` |

Load the smallest complete set. Do not omit `09` merely because the task is time-bound.

## Required task lifecycle

### 1. Preflight

Establish:

- objective and decision to be supported;
- requester, audience, and accountable decision-maker;
- population, entities, systems, folders, fields, period, and as-of timestamp;
- approved inputs, source hierarchy, and access limitations;
- output format, materiality, severity, and confidence conventions;
- allowed actions, prohibited actions, and approval gates;
- completion tests and reconciliation totals.

Ask only for gaps that block a safe result. Otherwise proceed with explicit assumptions.

### 2. Manifest

Create a concise run manifest before substantive processing:

```yaml
run_id: <stable identifier>
objective: <one sentence>
decision_supported: <decision, not analysis topic>
as_of: <ISO-8601 timestamp and timezone>
scope:
  included: []
  excluded: []
inputs: []
expected_population: <count or unknown with reason>
authority:
  read: []
  write: []
  approval_required: []
deliverables: []
quality_gates: []
```

For conversational work, show only the fields useful to the reader. Maintain the full
manifest internally or in the workpaper when the task is recurring or high risk.

### 3. Acquire and preserve

- Capture source identity, direct URL or record ID, publisher, publication date,
  retrieval timestamp, version, access route, and evidence span.
- Preserve raw inputs or immutable references when policy permits.
- Record search queries and negative searches when absence is relevant.
- Never replace an original record with an assistant summary.

### 4. Normalize and reconcile

- Parse without discarding raw values.
- Normalize identifiers, dates, time zones, names, currencies, units, and enumerations.
- Resolve duplicates and versions using explicit rules.
- Reconcile input totals, processed totals, excluded totals, failed items, and output
  totals. Every item must end in exactly one disposition or a documented exception.

### 5. Analyze

- Apply the task-specific framework and record its version.
- Separate deterministic calculations from judgment.
- Test alternative explanations and disconfirming evidence.
- Assign severity and confidence independently.
- Link each finding to evidence, criteria, impact, recommendation, owner, and due date
  where action is required.

### 6. Draft and render

- Lead with the answer and decision implication.
- Use the template and design standard in module `07`.
- Keep the analytical source of truth separate from display-only formatting.
- Include scope, as-of date, methodology, limitations, sources, and version metadata.

### 7. Validate

- Run calculations and reconciliation checks.
- Trace every material statement to evidence.
- Check links, dates, names, totals, labels, and visual rendering.
- Apply the release gate in module `09`.
- When a gate fails, label the output `DRAFT`, state the failure, and do not perform the
  gated action.

### 8. Handoff or act

- Distinguish `proposed`, `approved`, `executed`, `verified`, and `rejected` states.
- Execute only authorized actions after approval and precondition checks.
- Capture action result, timestamp, actor, destination, and confirmation evidence.
- Persist state only in the approved system of record.

## Finding contract

Use this minimum record for every material finding:

| Field | Requirement |
|---|---|
| Finding ID | Stable within the run and reusable across refreshes |
| Headline | One sentence stating the condition and consequence |
| Claim class | Observed, reported/alleged, inferred, or projected |
| Criteria | Policy, rule, expectation, baseline, or analytical threshold |
| Condition | What the evidence shows |
| Evidence | Direct record, source, page/section/row/message, and retrieval time |
| Cause | Confirmed cause or clearly labeled hypothesis |
| Impact | Quantified where defensible; otherwise bounded qualitatively |
| Severity | CRITICAL, HIGH, MEDIUM, or LOW with rationale |
| Confidence | HIGH, MODERATE, LOW, or NOT ASSESSABLE with rationale |
| Counterevidence | Conflicting or mitigating evidence |
| Recommendation | Specific, proportionate action |
| Owner and due date | Required for accepted actions |
| Status | Open, accepted, in progress, blocked, closed, or risk accepted |

Severity is impact and urgency. Confidence is evidence strength. Never raise confidence
to match severity or lower severity merely because confidence is low.

## Source and citation rule

A citation must allow a skeptical reviewer to reach the exact support for a claim. Use a
direct official link or stable record identifier; add page, paragraph, table, message, or
row references when possible. A homepage citation is insufficient when a direct document
exists. Record both the source's own date and the retrieval date.

## Completeness rule

For population-based work, report:

```text
expected = processed + excluded_with_reason + failed_or_unavailable
processed = unique_outputs + duplicates_or_superseded
```

If `expected` is unknown, do not call the review complete. State the accessible scope,
the method used to estimate coverage, and the residual risk.

## External action gate

Before any external write, verify all of the following:

- the target and exact action are authorized;
- the content is final and has passed its required reviews;
- recipients, classification, attachments, and links are correct;
- no unresolved high-severity data or factual defect remains;
- duplicate or repeated execution is prevented;
- rollback, correction, or escalation procedures are known;
- the action result can be confirmed and logged.

If any condition fails, produce a draft or action proposal only.

## Repository maintenance

- Keep the numbered filenames stable.
- Add new concepts to the controlling module instead of creating narrow one-off files.
- Avoid duplicate standards. Cross-reference the controlling section.
- Keep examples synthetic and generic.
- Use direct, dense language. Avoid marketing claims and decorative filler.
- Do not add employer names, internal systems, confidential processes, or real case data.
- Validate internal Markdown links, disallowed terms, duplicate headings, file count, and
  source-register structure before committing.
- Record material changes and source refreshes under module `11`.

## Definition of done

Work is done only when the intended decision can be made from the output, the evidence
can be traced, the population and calculations reconcile, limitations are explicit, the
artifact renders correctly, required review gates pass, and any authorized action is
separately confirmed.
