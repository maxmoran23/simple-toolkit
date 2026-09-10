# Unified Output Templates and Professional Design Standard

This is the single controlling source for deliverable structure, visual design,
interaction, export, source presentation, and render QA. Use it for Markdown, Word, PDF,
Excel, PowerPoint, HTML dashboards, email, and short-form updates. Do not maintain a
second template standard in a domain module; add domain-specific content to the universal
structures here.

Pair this file with [`00-operating-system.md`](00-operating-system.md) and
[`09-quality-assurance.md`](09-quality-assurance.md). Use
[`06-data-quality-governance.md`](06-data-quality-governance.md) when the deliverable is
driven by structured data.

## 1. Output selection

Choose the artifact from the decision, audience, data, and maintenance pattern.

| Need | Primary artifact | Add when useful | Avoid |
|---|---|---|---|
| One decision, little data | one-page decision memo | appendix or evidence table | dashboard |
| Formal narrative and review trail | Word report | locked PDF distribution copy | spreadsheet as the only narrative |
| Fixed, externally shared record | PDF report | accessible source workbook | PDF as working model |
| Row-level tracking or calculation | Excel workbook | short memo or dashboard | long narrative in cells |
| Executive discussion | PowerPoint deck | appendix workbook/report | text-heavy slide transcript |
| Repeated metric exploration | HTML dashboard | exportable detail table and method note | novelty-first interactive site |
| Urgent development | flash alert/email | linked brief or tracker | long report before escalation |
| Recurring operational status | dashboard plus digest | issue/action register | disconnected weekly files |
| Controlled procedure | SOP/policy document | RACI and control matrix | slide deck as authority |
| Large evidence package | indexed folder/manifest | executive report | embedding every raw file in the report |

Use one analytical source of truth and render multiple faces from it. A Word report, PDF,
dashboard, and slide deck may differ in density, but their findings, totals, labels,
ratings, dates, and source IDs must reconcile.

## 2. Deliverable contract

Before rendering, define:

```yaml
deliverable_id: DEL-<stable-id>
title: <decision-oriented title>
purpose: <what decision/action it supports>
audience: []
owner: <role>
classification: <approved label>
as_of: <ISO-8601 timestamp and timezone>
period: <start/end or point in time>
status: draft|reviewed|approved|superseded
version: <semantic or controlled version>
source_data_version: <identifier>
method_version: <identifier>
formats: []
sections: []
required_reviews: []
distribution: []
retention: <approved rule or reference>
```

The deliverable must state its as-of date, period, scope, source version, and status. A
reader should not have to infer whether it is a live view, a point-in-time snapshot, a
draft, or an approved record.

## 3. Universal narrative anatomy

Every substantive artifact uses this order unless the format-specific template changes
it for a stated reason:

1. **Document control:** title, status, version, classification, owner, date, period.
2. **Bottom line:** decision, conclusion, or status in one to three sentences.
3. **Decision or action required:** who must decide/do what, by when.
4. **Key findings:** three to seven material findings with severity and confidence.
5. **Scope and coverage:** included/excluded population, sources, period, reconciliation.
6. **Analysis:** organized by decision question, not collection order.
7. **Counterevidence and alternatives:** facts that weaken or change the conclusion.
8. **Risk and implications:** actual/potential impact and affected scope.
9. **Recommendations or options:** owner, due date, dependency, priority, evidence of
   completion.
10. **Method and limitations:** method version, assumptions, gaps, fallback use.
11. **Sources and evidence index:** exact traceable references.
12. **Appendices:** detailed data, calculations, glossary, change log, technical material.

The executive summary is not a background section. It carries the conclusion,
supporting evidence, material uncertainty, and requested decision.

## 4. Writing standard

- Lead with the answer. Do not open with generic context.
- Use active voice and specific actors.
- Put numbers before adjectives: `42 of 810 records (5.2%)`, not `many records`.
- Separate observed, reported/alleged, inferred, and projected content.
- Cite every material fact and calculation near the claim.
- State the benchmark or criteria before describing a gap.
- Give confidence with a reason, not as a decorative label.
- Treat proposals, approvals, executions, and verifications as different states.
- Explain `no findings` through coverage and test results; never imply omniscience.
- Use sentence case for headings. Avoid all-caps body text.
- Expand acronyms once when the audience may not share them; do not over-explain domain
  terms to specialist readers.
- Remove filler, marketing claims, redundant conclusions, and assistant-centric language.

### Finding card

```text
[SEVERITY] Finding headline — the condition and consequence in one sentence

Criteria: [required state or benchmark]
Condition: [observed fact with evidence pointer]
Impact: [quantified or bounded consequence]
Confidence: [rating — reason]
Counterevidence/limitation: [material caveat]
Action: [verb + object + owner + due date]
Evidence: [source IDs and exact spans]
```

## 5. Institutional visual system

The default is restrained, printable, and familiar to bank, regulator, audit, legal, and
professional-services readers. Visual design serves hierarchy and decision-making.

### 5.1 Design principles

1. Light theme first; dark theme only when the audience or operating environment requires
   it.
2. One restrained accent family; semantic colors only for meaning.
3. Flat surfaces and clean rules; no decorative glass, glow, liquid animation, or neon.
4. Real charts with labeled axes, units, time periods, and sources.
5. Tables for precision, charts for patterns, prose for judgment.
6. Dense enough for professional review, with deliberate whitespace and alignment.
7. Accessible contrast, keyboard behavior, alt text, and non-color status cues.
8. Consistent document control, evidence, source, and export surfaces.
9. Print and PDF behavior are first-class, not afterthoughts.
10. Branding is configurable and secondary to traceability.

### 5.2 Color tokens

| Token | Hex | Use |
|---|---|---|
| Ink | `#172033` | primary text and titles |
| Navy | `#173A5E` | primary headings, table headers, navigation |
| Blue | `#2E668F` | links, selected state, primary accent |
| Teal | `#3E7773` | secondary series or informational accent |
| Slate | `#5D6878` | secondary text |
| Rule | `#CBD2DA` | borders and dividers |
| Panel | `#F3F5F7` | section background and table zebra |
| Canvas | `#FFFFFF` | primary surface |
| Critical | `#B42318` | critical only; pair with text/icon/pattern |
| High | `#B54708` | high/amber warning |
| Medium | `#806000` | medium/caution |
| Low/positive | `#28734D` | low-risk, positive, or complete when labeled |
| Neutral | `#667085` | not rated, pending, or contextual |

Do not use red/green alone. Add labels, shapes, line styles, or icons. Reserve bright
colors for small, meaningful signals. A page should remain legible in grayscale.

### 5.3 Typography

| Surface | Preferred fonts | Rules |
|---|---|---|
| Office documents | Aptos, Arial, Calibri, or approved corporate sans serif | 10–11 pt body; 15–20 pt title; 12–14 pt section heading |
| Formal long report | approved sans serif or restrained serif for body | use one body family and one heading family at most |
| Dashboard | system UI, Arial, or approved web font with local fallback | 14–16 px body; 12 px minimum supporting text |
| Tables/data | same family; tabular numerals when available | right-align quantities; consistent decimals |
| Code/IDs | Consolas, Menlo, or system monospace | use sparingly for identifiers and snippets |

Do not use novelty display fonts. Do not shrink text to fit excessive content; edit or
move detail to an appendix.

### 5.4 Spacing and layout

- Use a 4-point or 8-point spacing grid.
- Keep primary content width readable: roughly 70–90 characters for prose.
- Align titles, section headings, tables, and charts to a common left edge.
- Use 1-inch/25 mm page margins unless an approved template differs.
- Use thin `0.5–1 pt` rules; avoid boxed layouts around every paragraph.
- Use square or lightly rounded corners (`0–4 px` default, `6 px` maximum).
- Use shadows only to distinguish an overlay or floating menu, not every card.
- Keep executive pages to one primary message and a small number of visual objects.
- Repeat table headers across pages; never split a row where it becomes unreadable.

### 5.5 Prohibited visual patterns

- animated gradient blobs, parallax, confetti, or decorative motion;
- glassmorphism, glowing borders, neon-on-black palettes, or gaming-style panels;
- cartoon people, generic AI robot art, decorative stock illustrations, or emojis as
  analytical icons;
- 3-D charts, exploded pies, speedometer gauges, ornamental radar charts, and faux
  scientific precision;
- trophy, achievement, streak, or gamification modules in governance reporting;
- giant metric cards without denominator, period, source, or decision relevance;
- unlabelled red/amber/green traffic lights;
- automatic animations that delay comprehension or interfere with printing;
- a dashboard when a table or one-page memo answers the question more clearly.

## 6. Tables

### 6.1 Universal table rules

- Use a descriptive title and a note stating population, period, unit, and source.
- Put dimensions on the left and measures on the right.
- Left-align text; right-align numbers; align decimals.
- Include units in headers, not repeated in every cell.
- Use ISO `YYYY-MM-DD` in working tables unless the audience requires another display.
- Show missing as `Not available`, `Not applicable`, or `Not collected`; do not blur
  these into blank or zero.
- Show totals for additive measures and a denominator for every rate; when a total would
  mislead, state why it is omitted instead of omitting it silently.
- Freeze and repeat headers; enable filters for row-level workbooks/dashboards.
- Use restrained zebra shading or thin row rules, not full cell borders everywhere.
- Put notes and caveats below the table, keyed to superscript or note ID.
- Protect identifiers from spreadsheet auto-conversion.

### 6.2 Standard finding table

| ID | Severity | Finding | Evidence | Impact | Confidence | Owner | Due | Status |
|---|---|---|---|---|---|---|---|---|

### 6.3 Standard action table

| Action ID | Action | Rationale/source | Owner | Approver | Due | Dependency | Status | Completion evidence |
|---|---|---|---|---|---|---|---|---|

### 6.4 Standard source table

| Source ID | Publisher/system | Document/record | Published/event date | Retrieved | Version | Evidence span | Tier | Link/record ID |
|---|---|---|---|---|---|---|---|---|

## 7. Charts and quantitative visuals

### 7.1 Select by question

| Question | Preferred visual | Notes |
|---|---|---|
| Change over time | line or column chart | show time grain, gaps, and comparison period |
| Compare categories | sorted horizontal bar | zero baseline; direct labels where possible |
| Composition | stacked bar or 100% stacked bar | use pie/donut only for 2–5 stable categories |
| Distribution | histogram, box plot, ECDF | show sample size and bin/method choices |
| Relationship | scatter plot | show units, correlation method, and outliers |
| Movement from A to B | waterfall | reconcile starting value, drivers, ending value |
| Risk by likelihood/impact | matrix/heat map | show criteria and counts; do not imply precision beyond scale |
| Process or ownership | flow, tree, or network | label edge meaning and evidence/confidence |
| Geography | map only when spatial pattern matters | provide accessible table and normalize for population where relevant |
| Plan and dependencies | milestone/Gantt | show owner, status, dependencies, and critical path |

### 7.2 Chart contract

Every chart must include:

- a conclusion-oriented title;
- defined population, metric, unit, and period;
- source and refresh/as-of note;
- visible axes and baselines appropriate to the claim;
- legend or direct labels;
- treatment of missing, suppressed, revised, and estimated values;
- denominator and sample size for rates;
- accessible description or data table;
- no more precision than the data supports.

Annotate material events and methodology changes. Distinguish actual, estimated, target,
and forecast series by line style as well as color.

### 7.3 Color sequence

Default categorical sequence:

`#173A5E`, `#3E7773`, `#7A6F9B`, `#9A6A3A`, `#6B7C45`, `#7B5A68`

Use a single-hue sequential scale for magnitude and a balanced diverging scale centered
on the defined benchmark for variance. Do not use a rainbow scale.

## 8. Source, evidence, and methodology surfaces

Every formal output includes:

- **as-of banner:** time zone, data cut, publication status;
- **scope note:** included and excluded populations;
- **method note:** approach, version, assumptions, thresholds, transformations;
- **coverage panel:** expected, processed, excluded, failed, and duplicate totals;
- **source register:** source IDs and direct traceable references;
- **finding-to-evidence links:** evidence IDs at the statement or row level;
- **limitations:** material gaps and decision effect;
- **change log:** for maintained outputs;
- **approval record:** where the artifact is controlled.

For public web outputs, source links should open the exact official document when
possible. For internal outputs, use stable record IDs and approved deep links; do not
expose restricted locations in a broadly distributed file.

## 9. File naming and package structure

Use stable, sortable names:

```text
<topic>-<artifact>-<period-or-asof>-v<major.minor>-<status>.<ext>
```

Examples:

```text
regulatory-change-tracker-2026-q3-v1.0-reviewed.xlsx
entity-risk-assessment-entity-0042-2026-08-13-v2.1-draft.docx
control-testing-summary-2026-h1-v1.0-approved.pdf
```

Do not put confidential names in filenames when a stable approved identifier works.

For a multi-file delivery:

```text
00-readme-and-manifest
01-executive-deliverable
02-supporting-workbook
03-evidence-index
04-source-materials-or-links
05-qa-and-approval
```

Use an inventory with file hash, version, classification, owner, and purpose.

## 10. Template: executive one-pager

```text
TITLE — decision or status as of [date]
Status | Owner | Classification | Version

BOTTOM LINE
[Two or three sentences: conclusion, evidence, uncertainty.]

DECISION / ACTION REQUIRED
[Decision, accountable role, deadline.]

KEY FINDINGS
1. [Severity] [finding] — [evidence ID] — confidence [rating/reason]
2. ...

EXPOSURE / METRICS
[Up to six governed measures with period, denominator, and source.]

OPTIONS AND RECOMMENDATION
| Option | Benefit | Risk | Cost/timing | Recommendation |

NEXT ACTIONS
| Action | Owner | Due | Dependency | Status |

SCOPE, METHOD, AND LIMITATIONS
[Population reconciliation; method version; material gaps.]

SOURCES
[Direct references or source IDs.]
```

## 11. Template: decision memo

```text
TO:
FROM:
DATE / AS OF:
SUBJECT:
CLASSIFICATION / STATUS / VERSION:

DECISION REQUESTED
[One sentence.]

RECOMMENDATION
[Direct recommendation and conditions.]

RATIONALE
1. [evidence-led reason]
2. [evidence-led reason]
3. [evidence-led reason]

BACKGROUND
[Only context required to assess the decision.]

ANALYSIS
[Organized by decision criterion.]

COUNTEREVIDENCE AND UNCERTAINTY
[What could change the recommendation.]

OPTIONS
| Option | Benefit | Risk | Preconditions | Cost/timing |

IMPLEMENTATION
| Action | Owner | Due | Dependency | Approval | Evidence of completion |

METHOD / SOURCES / LIMITATIONS
```

## 12. Template: analytical or research report

Recommended sections:

1. Cover and document control.
2. Executive summary and decision implications.
3. Scope, priority questions, and coverage reconciliation.
4. Method, source hierarchy, search strategy, and evidence standard.
5. Findings by decision question.
6. Chronology, network, quantitative, or comparative analysis as applicable.
7. Counteranalysis and alternative explanations.
8. Risk assessment and scenarios, clearly labeled.
9. Recommendations, owners, and due dates.
10. Limitations and open questions.
11. Sources and claim-evidence index.
12. Appendices: data dictionary, calculations, search log, change log.

For research, each major finding carries a confidence reason and at least one primary
source; the fallback chains in module `02` section 6 define where a primary record
should exist, and when none does, say so explicitly and lower confidence. Source count
is not corroboration when many articles repeat one underlying report.

## 13. Template: investigation or case report

```text
CASE CONTROL
Case ID | Type | Status | Owner | Reviewer | Period | As of | Classification

PROPOSED DISPOSITION
[Proposed, not approved, unless approval record follows.]

EXECUTIVE CASE SUMMARY
[Trigger, scope, observed activity, typology relevance, conclusion, uncertainty.]

SCOPE AND COMPLETENESS
| Population | Expected | Processed | Excluded | Failed | Duplicate | Reconciled? |

SUBJECTS AND IDENTITY RESOLUTION
| Subject ID | Identity outcome | Decisive attributes | Conflicts/gaps | Confidence |

CHRONOLOGY
| Time | Event | Observed fact | Value | Evidence | Relevance |

ANALYSIS
- transaction/activity analysis
- relationships and ownership
- external intelligence and screening
- typologies considered
- alternative explanations and counterevidence

FINDINGS AND DECISION CRITERIA
| ID | Criteria | Condition | Evidence | Impact | Severity | Confidence |

RECOMMENDATION AND HUMAN GATE
[Options, proposed action, authorized decision-maker.]

EVIDENCE INDEX / METHOD / LIMITATIONS / REVIEW RECORD
```

## 14. Template: entity or product risk assessment

```text
COVER AND DOCUMENT CONTROL
Entity/product ID | Assessment type | Method version | As of | Owner | Status

EXECUTIVE ASSESSMENT
Overall rating | Confidence | Override/floor | Recommendation | Next review

PROFILE AND CLASSIFICATION
Identity | Ownership/control | Business/activity model | Geography | Products | Lifecycle

RISK DOMAIN MATRIX
| Domain | Inherent score | Control effectiveness | Residual score | Evidence | Rationale | Confidence |

MATERIAL FINDINGS
[Finding cards.]

CONTROL AND CONDITION MATRIX
| Risk | Control/condition | Owner | Test/evidence | Status | Due |

SCORING AND SENSITIVITY
[Weights, missing treatment, raw result, floors/overrides, sensitivity.]

DECISION / CONDITIONS / ACTIONS
[Authorized decision record or proposed decision.]

SOURCES / LIMITATIONS / CHANGE HISTORY
```

## 15. Template: regulatory alert and obligation register

### Alert

```text
[SEVERITY] [Authority/instrument] — [decision-relevant change]
Published | Effective | Comment/transition deadline | As of | Confidence

BOTTOM LINE
[What changed, who is affected, and why it matters.]

STATUS AND AUTHORITY
[Proposed/final/effective/stayed/etc.; binding status; legal basis.]

IMPACT
| Product/process | Change | Current coverage | Gap | Owner |

IMMEDIATE ACTIONS
| Action | Owner | Due | Approval/dependency |

SOURCE
[Official direct source and exact provisions.]

LIMITATIONS / INTERPRETIVE QUESTIONS
```

### Obligation register columns

`Obligation ID`, jurisdiction, authority, instrument, status, citation, regulated actor,
modal verb, action, object, condition/trigger, deadline/frequency, exceptions, evidence,
policy, procedure, control, system/data, owner, gap, action, due date, confidence, source
version, last reviewed.

## 16. Template: control matrix and testing workpaper

### Control matrix columns

`Control ID`, risk ID, objective, complete control activity, owner, frequency, nature,
execution, population, inputs, criteria/threshold, evidence, exception/escalation,
dependencies, key status, design rating, operating rating, last tested, issue ID.

### Testing workbook tabs

1. `Read Me`: purpose, version, owner, definitions, instructions, limitations.
2. `Test Plan`: control, population, period, source, reconciliation, method, sample basis.
3. `Population`: immutable imported population with source row IDs.
4. `Selections`: selected items and reproducible selection metadata.
5. `Test Results`: procedure-level results and evidence pointers.
6. `Exceptions`: issue classification, impact, owner, response, due date.
7. `Summary`: counts, rates, confidence limits where applicable, conclusion.
8. `Change Log`: version, date, author/reviewer, description.

Keep raw population and formula cells protected. Use formulas or controlled calculations,
not typed summary totals.

## 17. Template: issue and remediation tracker

Required columns:

`Issue ID`, title, source, criteria, condition, root cause, impact, affected population,
severity, confidence, containment, remediation action, owner, approver, original due,
current due, milestones, dependencies, status, extension/risk acceptance, validation
procedure, closure evidence, validated by/date, last updated.

The executive view should show:

- total open by severity and age;
- overdue and due in 30/60/90 days;
- movement since prior period;
- recurring root causes and affected controls;
- extensions, risk acceptances, and blockers;
- closed items pending validation;
- source and data-quality caveats.

## 18. Template: mailbox or communications output

### Executive digest

```text
MAILBOX / CORPUS / PERIOD / AS OF
Coverage: expected | processed | excluded | failed | duplicate | reconciled

BOTTOM LINE
[What materially changed and what requires attention.]

URGENT / ESCALATED
| Thread/item | Issue | Why urgent | Owner | Deadline | Evidence |

DECISIONS AND COMMITMENTS
| Decision/commitment | Decision-maker/owner | Date | Scope | Evidence |

ACTIONS
| Action | Owner | Due | Status | Source message/thread |

OPEN QUESTIONS / REQUESTS
| Question/request | Requester | Respondent | Aging | Next step |

THEMES AND TRENDS
[Counts and narrative with denominators and comparison periods.]

DRAFT RESPONSES PENDING APPROVAL
[Draft ID, target, purpose, reviewer, no automatic send.]

LIMITATIONS / FAILURES / METHOD
```

### Row-level index

Use the canonical schema in module `03`; preserve message/thread/source IDs and evidence
spans. Do not place sensitive message text into a broad executive output when a restricted
evidence link is sufficient.

## 19. Template: policy or standard operating procedure

```text
DOCUMENT CONTROL
Title | ID | Version | Owner | Approver | Effective | Next review | Status | Classification

1. Purpose
2. Scope and applicability
3. Authority and source requirements
4. Definitions and controlled vocabulary
5. Roles, responsibilities, and RACI
6. Policy requirements
7. Procedure with numbered steps and decision points
8. Controls, evidence, and recordkeeping
9. Exceptions and risk acceptance
10. Escalation and incident handling
11. Training and competency
12. Monitoring, testing, and management information
13. Retention, privacy, and access
14. Related documents
15. Revision history
Appendices: forms, schemas, flow, control mapping
```

Write testable requirements. Replace `periodically`, `appropriate`, and `timely` with
defined triggers, criteria, or ownership unless the governing authority intentionally
uses discretion and the policy explains it.

## 20. Template: committee reporting pack

### Recommended page/slide sequence

1. Title, meeting, period, status, and decision rights.
2. Decisions and approvals requested.
3. Executive scorecard with definitions and source cut.
4. Material changes since prior meeting.
5. Critical/high issues and incidents.
6. Portfolio or risk-domain view.
7. Controls, testing, model, and data-quality performance.
8. Regulatory and external developments.
9. Remediation, overdue actions, and blockers.
10. Forward calendar and emerging risks.
11. Decisions taken and action log.
12. Appendix: methodology, metric definitions, detail tables, sources.

Every metric shows definition, numerator, denominator, period, target/threshold, trend,
owner, source, and data-quality status. Do not use a green scorecard to conceal overdue
high-severity actions.

## 21. Template: email and short-form communication

### Executive email

```text
Subject: [specific topic] — [decision/action] by [date]

[Name/team],

Bottom line: [one or two sentences].

What changed
- [finding with source/reference]

Action required
- [action] — owner: [role] — due: [date]

Key evidence / attachment
- [link or controlled attachment]

Limitations or open question
- [material caveat]

[Sender/signature per approved convention]
```

### Automated or recurring digest

May omit the greeting, but must include source cut, coverage, failures, and a reply route.
Use HTML only when rendering has been tested across the target clients; always include a
plain-text alternative when the system supports it.

### Short-form channel update

```text
[SOURCE / TOPIC] | [date/time/timezone] | [status]
Bottom line: [single most important conclusion].
Findings: [up to three concise, sourced items].
Action: [owner + due date, or none].
Coverage/quality: [population and material limitation].
Details: [controlled link].
```

Keep the top-level update short; place detail in a linked report or thread. Do not use
emoji severity markers.

## 22. Word document standard

### 22.1 Document setup

- Use a real document-generation library or approved authoring tool; do not hand-edit
  Office Open XML.
- Apply named styles for Title, Subtitle, Heading 1–3, Body, Caption, Quote, Table Header,
  Table Body, and Source Note.
- Use standard page size for the audience, 1-inch/25 mm margins, and restrained header/
  footer distance.
- Put classification, short title, version, and date in the header/footer according to
  policy; use automatic page fields.
- Generate a real table of contents for documents longer than five pages.
- Use section breaks intentionally for landscape exhibits; return to portrait after.
- Add captions and cross-references for tables, figures, and appendices.
- Preserve heading hierarchy for navigation and accessibility.

### 22.2 Title page

```text
[DOCUMENT TITLE]
[Decision, subject, or period]

Status: [Draft/Reviewed/Approved]
Classification: [approved label]
Version: [x.y]
As of: [date/time/timezone]
Owner: [role]
Prepared for: [audience/body]
```

Do not add decorative cover images unless the user provides approved branding and the
image materially supports the document.

### 22.3 Word QA

- Inspect every page after rendering.
- Check table width, repeated headers, row splitting, orphan headings, page breaks,
  footnotes, captions, cross-references, and TOC updates.
- Confirm fonts are embedded or safely substituted.
- Check tracked changes/comments and document metadata before distribution.
- Confirm hyperlinks and internal bookmarks work.
- Verify content remains readable when printed in grayscale.

## 23. PDF report standard

PDF is the controlled distribution face, not the analytical source model.

### 23.1 Preferred production paths

1. Author in Word or an approved document system and export to tagged PDF.
2. Author in accessible HTML/CSS and render with an approved engine.
3. Generate directly only when the library supports page control, fonts, links, and
   accessibility needed for the audience.

### 23.2 Required PDF features

- selectable text; do not deliver image-only pages without OCR and validation;
- document title, language, authoring metadata as policy permits;
- bookmarks for major sections in reports longer than five pages;
- live source and internal links where classification permits;
- page numbers and stable exhibit labels;
- tagged reading order and alt text when the distribution standard requires it;
- embedded or safely licensed fonts;
- print-safe colors, margins, and page breaks;
- no clipped charts, hidden footnotes, or rasterized small text.

### 23.3 PDF QA

Render pages to images and visually inspect at normal size and 125–150% zoom. Extract
text to confirm it is present and ordered. Check links, bookmarks, page count, metadata,
fonts, signatures, redactions, and file size. A black rectangle placed over text is not a
redaction unless the underlying content is actually removed through an approved method.

## 24. Excel workbook standard

### 24.1 Workbook architecture

Use only the tabs the task needs, in this order:

1. `Read Me` — purpose, owner, version, as-of, source cut, instructions, limitations.
2. `Executive Summary` — decisions, governed KPIs, trend, findings, actions.
3. `Parameters` — controlled assumptions, thresholds, mappings, and version.
4. `Raw Data` — immutable source extract or linked staging area.
5. `Normalized Data` — controlled transformations and stable row IDs.
6. `Analysis` — formulas, pivots, or calculation outputs.
7. Domain tabs — risks, controls, findings, issues, cases, obligations, etc.
8. `Data Quality` — reconciliation, rule results, exceptions, source health.
9. `Sources` — source and extraction metadata.
10. `Change Log` — version history and reviewer.

Do not create empty tabs to appear comprehensive.

### 24.2 Spreadsheet control rules

- Preserve raw data; never overwrite it with cleaned values.
- Use stable row IDs and source IDs.
- Use Excel tables with filters and structured references.
- Freeze panes and repeat print headers.
- Highlight approved input cells with one restrained fill and label them `Input`.
- Lock formula and structure cells in any workbook that leaves the producing team,
  keeping only labeled `Input` regions unlocked; document the password/owner through an
  approved channel, never in the workbook.
- Use data validation lists tied to a controlled vocabulary table.
- Use formulas or governed queries for summaries; do not type totals.
- Separate actual, forecast, assumption, override, and calculated cells by style and
  label, not color alone.
- Avoid volatile functions and hard-coded constants inside formulas.
- Include formula-error, blank-key, duplicate-key, and reconciliation checks.
- State Excel date system, locale, currency, FX source/date, and rounding.
- Do not merge cells inside data ranges.

### 24.3 Standard number formats

| Type | Display | Notes |
|---|---|---|
| Integer | `#,##0;[Red](#,##0);-` | use dash for zero only if defined |
| Decimal | `#,##0.0` or governed precision | avoid false precision |
| Currency | thousands separators, parentheses for negatives, or explicit ISO currency | label currency in header |
| Percentage | `0.0%` | confirm stored as decimal |
| Date | `yyyy-mm-dd` | working data standard |
| Date-time | `yyyy-mm-dd hh:mm` plus timezone field | never silently mix zones |
| Identifier | text | protect leading zeros and long integers |

### 24.4 Formula provenance

For material calculations, provide:

- business definition;
- formula or query logic;
- source fields and filters;
- effective version/date;
- owner and reviewer;
- example recalculation;
- tie-out to the source or external control total.

### 24.5 Excel QA

- Recalculate with the target spreadsheet engine.
- Scan for `#REF!`, `#DIV/0!`, `#VALUE!`, `#N/A`, circular references, hidden errors,
  inconsistent formulas, and hard-coded values in formula regions.
- Verify filters, validation, conditional formatting, named ranges, protection, print
  areas, frozen panes, hidden rows/columns/tabs, external links, macros, and metadata.
- Reconcile summary totals to detailed tabs and source controls.
- Open and visually inspect every sheet at normal size and 125 to 150 percent zoom, and
  in print preview.

## 25. PowerPoint standard

### 25.1 Narrative arc

Build a decision story, not a report cut into slides:

1. Title and decision context.
2. Executive answer: three messages maximum.
3. Evidence and material change.
4. Analysis by decision driver.
5. Risks, alternatives, and uncertainty.
6. Recommendation/options.
7. Actions, owners, and timeline.
8. Appendix with method, definitions, detailed data, and sources.

### 25.2 Slide rules

- Use a message title that states the conclusion, not a topic label.
- One primary analytical message per slide.
- Prefer one chart or structured table plus two to four implications.
- Use a consistent master, grid, footer, page number, source note, and status label.
- Keep body text generally at or above 16–18 pt and chart labels readable at projected
  size; do not rely on a rigid `6x6` rule when a clearer structured exhibit is better.
- Use builds/animation only to control discussion sequence; provide a static printable
  view.
- Do not use stock imagery, decorative icons, or photos merely to fill space.
- Include source IDs and as-of date on every data slide.
- Keep appendices available for challenge and drill-down.

### 25.3 Common slide layouts

| Layout | Use |
|---|---|
| Executive takeaway | three messages plus decision/action |
| Evidence chart | one chart with annotations and implications |
| Issue deep dive | criteria, condition, cause, effect, recommendation |
| Options | consistent comparison across benefit, risk, cost, timing, dependency |
| Roadmap | milestones, owners, dependencies, decision gates |
| Portfolio | governed scorecard plus exceptions and trend |
| Process/control | swim lane with control/evidence points |
| Appendix table | precise data with definitions and source |

### 25.4 PowerPoint QA

Render every slide and inspect alignment, overlap, clipping, font substitution, chart
legibility, contrast, source notes, and appendix links. Confirm slide titles form a
coherent summary when read alone. Check speaker notes, comments, hidden slides, embedded
files, links, metadata, and export to PDF.

## 26. Institutional HTML dashboard standard

The dashboard is an analytical application, not a poster. It should expose governed data,
support decisions, and make evidence and quality visible.

### 26.1 Architecture choices

| Pattern | Use | Control points |
|---|---|---|
| Single-file offline HTML | portable snapshot, restricted workstation, one-time analysis | embedded data, no hidden network calls, source cut, file-size and privacy review |
| Static site with data files | larger snapshot or multiple pages | relative paths, access controls, integrity/version of data files |
| Connected application | maintained operational dashboard | authentication, authorization, API contracts, logging, monitoring, retention |
| BI platform | governed enterprise metrics and distribution | semantic model, row-level security, refresh and certification controls |

Do not claim a single-file snapshot is live. Do not include a CDN dependency when the
file must work offline; bundle approved libraries or use native browser features. Review
licenses and integrity for dependencies.

### 26.2 Page anatomy

1. **Utility header:** title, owner, as-of/refresh, status, classification, help.
2. **Scope and filter bar:** period, population, segment, saved view, reset.
3. **Decision strip:** decisions/actions requested and material alerts.
4. **KPI band:** four to six governed measures with definitions, denominators, trend,
   target, source, and quality status.
5. **Primary analysis:** two to four decision-relevant charts/tables.
6. **Findings/issues:** severity, evidence, owner, due date, status.
7. **Trend and segmentation:** comparisons and drivers.
8. **Data browser:** searchable, sortable, filterable, paginated row-level table when
   permitted.
9. **Method, data quality, and sources:** always accessible, not hidden in code.
10. **Footer:** version, generated time, source cut, contact/owner, export status.

Do not force ten to twenty sections when four answer the decision. Depth comes from
drill-through and precise data, not page length.

### 26.3 Required interactions

Four are mandatory for any interactive dashboard: keyboard-accessible filters with
reset, chart tooltips with exact values, visible loading/empty/partial/stale/error
states, and a source link from each finding. Include the remainder when the data and
environment support them:

- keyboard-accessible filters with active-filter summary and reset;
- sort and search with clear match count;
- drill-through from aggregate to governed detail;
- chart tooltip with exact value, unit, period, and source/definition link;
- saved or shareable view only if sensitive filters are not leaked in URLs;
- print view and accessible data table;
- export of the filtered dataset, current view, and evidence/source index;
- source link or record pointer from each finding;
- data-dictionary and metric-definition panel;
- visible loading, empty, partial, stale, and error states;
- confirmation and authorization for any write action.

Export is a control surface. Each exported file should include filter state, generated
time, data/version ID, row count, classification, and source/method notes.

### 26.4 Corporate light-theme CSS baseline

```css
:root {
  --canvas: #ffffff;
  --panel: #f3f5f7;
  --panel-strong: #e8ecf0;
  --ink: #172033;
  --muted: #5d6878;
  --navy: #173a5e;
  --blue: #2e668f;
  --teal: #3e7773;
  --rule: #cbd2da;
  --critical: #b42318;
  --high: #b54708;
  --medium: #806000;
  --positive: #28734d;
  --radius: 4px;
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --font: Arial, Aptos, system-ui, -apple-system, sans-serif;
}

body {
  margin: 0;
  color: var(--ink);
  background: var(--canvas);
  font: 14px/1.45 var(--font);
}

.panel {
  background: var(--canvas);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  padding: var(--space-4);
}

.section-title {
  color: var(--navy);
  font-size: 18px;
  font-weight: 700;
  border-bottom: 2px solid var(--navy);
  padding-bottom: var(--space-2);
}

@media print {
  .no-print { display: none !important; }
  body { color: #000; background: #fff; font-size: 10pt; }
  .panel { break-inside: avoid; box-shadow: none; }
  a { color: #000; text-decoration: none; }
  a[href]::after { content: " (" attr(href) ")"; font-size: 8pt; }
}
```

Customize through tokens, not scattered one-off styles.

### 26.5 Dashboard data contract

```yaml
dashboard_id: <stable-id>
version: <version>
title: <title>
owner: <role>
as_of: <timestamp>
refresh_status: current|stale|partial|failed
classification: <label>
datasets:
  - dataset_id: <id>
    version: <id>
    source_ids: []
    expected_rows: <number or unknown>
    actual_rows: <number>
    primary_key: []
    period: <start/end>
    fields:
      - name: <machine name>
        label: <display label>
        type: text|integer|number|currency|percent|date|datetime|boolean|category
        unit: <unit or null>
        definition: <text>
        sensitivity: <class>
        allowed_values: []
        null_treatment: <rule>
metrics:
  - metric_id: <id>
    label: <label>
    definition: <business definition>
    formula: <governed logic>
    denominator: <definition>
    owner: <role>
    thresholds: []
    source_fields: []
    version: <version>
```

The same data object should drive visible KPIs, charts, tables, exports, and any embedded
assistant. Do not keep a second, drifting copy of dashboard data.

### 26.6 Empty, stale, partial, and error states

| State | Required display |
|---|---|
| Legitimate zero | `0` with population/period and confirmation that the source loaded |
| No data expected | explanation and scope rule |
| No data received | failure, affected source, last good data, owner, next retry |
| Partial | processed/expected, missing segments, decision impact |
| Stale | last good as-of, staleness threshold, refresh owner |
| Unauthorized | access message without leaking record existence or contents |
| Filtered to none | active filters and reset control |

Never render a blank chart that a user could mistake for zero activity.

Derive the staleness boundary from the declared refresh cadence rather than inventing it
per page: data is `current` while its age is within the cadence, `stale` once age
exceeds the cadence by the manifest's declared multiplier (1.5 is a reasonable
illustrative default), and `failed` when a scheduled refresh did not complete at all.

## 27. Embedded analytical assistant standard

An assistant inside a dashboard should make governed data easier to query; it must not
become an unbounded agent with implicit write authority.

### 27.1 Three-lane design

| Lane | Capability | Required behavior |
|---|---|---|
| Deterministic | counts, sums, averages, rankings, filters, distributions, trends from declared data | execute governed query; show method, filters, nulls, and evidence rows |
| Deterministic insights | declared thresholds, concentration, outliers, freshness, data-quality caveats | rank by governed salience; distinguish rule hits from statistical observations |
| Model-assisted | synthesis, explanation, follow-up, external context where approved | ground in query results; label interpretation; refuse unsupported numbers/actions |

### 27.2 Schema-first configuration

Declare datasets, field types, aliases, units, categories, date fields, entity IDs,
metrics, threshold/watch rules, and glossary. Validate configuration at startup. If a
user term cannot be mapped or two interpretations compete, clarify instead of guessing.

### 27.3 Answer contract

Every answer exposes:

- interpretation of the question;
- filter state and time anchor;
- result and denominator;
- source dataset/version and row/evidence references;
- null/exclusion treatment;
- calculation or reasoning method;
- confidence and any assumption;
- allowed follow-up or export;
- action state (`analysis only`, `draft`, or `approval required`).

### 27.4 Grounding and refusal

- Validate all stated numbers against governed query results.
- Refuse prediction, causation, or external factual claims when the required evidence is
  unavailable; offer a data read or handoff pack.
- Do not invent a field, metric, category, row, or trend.
- Preserve ambiguous and unknown terms in the clarification message.
- Do not let a model bypass row-level access controls.
- Keep live-provider calls opt-in, authenticated, logged, minimized, and covered by
  approved retention/data-use terms.

### 27.5 Handoff pack

When the question exceeds local data, package:

1. title, context, as-of, classification, and data version;
2. question verbatim and relevant prior turns;
3. dataset census, schema, definitions, and quality status;
4. relevant filtered slice with row IDs and stated cap;
5. query results and calculation methods;
6. response contract: cite rows, distinguish fact from interpretation, state assumptions,
   and do not fabricate values;
7. approved external sources or research scope, if any.

Review the pack for sensitive data before copy/download.

### 27.6 Assistant action gate

Read-only analysis is the default. Any proposed write requires:

- explicit function allowlist and least-privilege identity;
- visible target, payload, consequences, and approver;
- confirmation against current state to prevent stale writes;
- idempotency key and duplicate prevention;
- content, recipient, and classification checks;
- success/failure confirmation and audit log;
- rollback/correction or escalation procedure.

## 28. Export and source-link standard

### 28.1 Export menu

Where the environment permits, provide:

- current filtered rows as CSV/XLSX;
- current visual or section as PNG/SVG/PDF;
- full print-ready report as PDF;
- findings/actions as Markdown and structured JSON;
- source/evidence register;
- method/metric dictionary;
- handoff pack for approved analysis.

### 28.2 Export manifest

Every export includes or accompanies:

```yaml
export_id: <stable-id>
created_at: <timestamp/timezone>
created_by: <user/system role>
source_artifact: <dashboard/report id and version>
filters: <complete state>
row_count: <number>
data_version: <id>
method_version: <id>
classification: <label>
content_hash: <where supported>
limitations: []
```

Do not export hidden fields, inaccessible rows, or unfiltered underlying data merely
because the chart displays an aggregate.

### 28.3 Source links

- Link findings to the exact source record or evidence span when permitted.
- Use stable source IDs when direct links could expose sensitive locations.
- Distinguish public URL, internal record, attachment, query result, and calculation.
- Include source publication/event date and retrieval/extraction time.
- Mark broken, superseded, archived, or inaccessible links visibly.

### Verify the exported artifact

Freeze the analytical data version before rendering. For each export, record the
active filters, included population, row count, units, and control totals; reconcile
these to the intended screen or full-population view. Make filtered versus full export
an explicit choice. Hash the completed file for integrity and verify after the final
save, since a check of an earlier draft does not attest the delivered bytes.

Preserve identifier strings and leading zeroes in spreadsheets. Serialize untrusted
text as text, including formula-shaped values; never repair it by changing the raw
evidence. Escape HTML text and attributes, restrict active URL schemes, and keep source
text out of executable script. Check keyboard-only navigation, visible focus, table
headers, non-color status labels, chart alternatives, and print overflow. If a format
cannot be opened or rendered in the available runtime, label that check unverified.

## 29. Format-specific release gates

| Format | Must pass before release |
|---|---|
| Markdown | heading structure, tables, code fences, internal/external links, no placeholders |
| Word | generated TOC/fields, pagination, table/page rendering, comments/metadata, accessibility |
| PDF | page render, selectable text, links/bookmarks, fonts, redactions, metadata |
| Excel | recalculation, formulas/errors, validation/protection, reconciliation, print view |
| PowerPoint | slide render, message-title story, overlap/fonts, sources, notes/hidden content |
| HTML/dashboard | browser/runtime errors, responsive states, keyboard/accessibility, data parity, filters, export, print, source links, offline/network contract |
| Email | recipients, subject, links/attachments, classification, HTML/plain text, mobile/client render, approval |

Perform visual inspection with defined coverage: every page or slide for paginated
formats, every sheet for workbooks, and every top-level view plus each empty, stale, and
error state for dashboards. A successful file-generation call is not evidence that the
artifact is correct.

## 30. Copy-ready renderer prompt

```text
Render the approved analysis using module 07 as the single output standard and module 09
as the release gate.

Audience:
Decision/action supported:
Required format(s):
Classification:
As-of and reporting period:
Brand/theme override, if approved:
Distribution environment and accessibility requirements:

Use one governed analytical source of truth across every format. Lead with the answer,
show the decision/action required, preserve severity and confidence, reconcile all
totals, and link each material finding to evidence. Apply the institutional light design:
white/warm-gray surfaces, navy hierarchy, one muted accent, restrained semantic colors,
flat panels, real charts, precise tables, and strong print behavior. Do not use animated
backgrounds, glassmorphism, neon palettes, cartoon imagery, decorative gauges, emoji
icons, or novelty interactions.

For dashboards, include purposeful filters, drill-through, a governed data browser,
source/method panels, data-freshness and partial/error states, accessible keyboard
behavior, print view, and export of the current authorized filtered view. If an embedded
assistant is requested, bind it to the declared schema and data version, ground every
number, clarify ambiguity, refuse unsupported claims, and keep writes behind approval.

For every format, verify calculations, citations, links, status labels, dates, names,
metadata, and visual rendering. Do not mark the deliverable final if any material gate
fails; return a labeled draft with the defect log instead.
```

## 31. Final output checklist

- Correct artifact for the decision and audience.
- Document control, as-of, period, status, classification, owner, and version present.
- Bottom line and requested action visible without reading the appendix.
- Findings trace to evidence; criteria, severity, confidence, and limitations clear.
- Population, calculations, and multi-format totals reconcile.
- Institutional light design applied consistently; no prohibited patterns.
- Tables, charts, labels, units, denominators, sources, and accessibility meet standard.
- Source links, methodology, coverage, and data-quality states are usable.
- Export contains only authorized filtered content and a manifest.
- Embedded assistant, if any, is schema-bound, grounded, read-only by default, and gated.
- File opens and renders correctly in the target applications and print/PDF path.
- Comments, hidden content, metadata, test data, and temporary artifacts are reviewed.
- Module `09` release gate passed and approval state is correctly represented.
