# End-to-End Use-Case Recipes

This module tells a user or agent which files to load and how to assemble them into a
complete project. It is the operational index for Simple Toolkit. Detailed rules remain
in the linked modules; do not duplicate or weaken them here.

## 1. Choose the smallest complete bundle

Start with the decision and the population, not the desired file type.

```text
Does the task use a communication corpus?
  Yes -> include 03.

Does it require external or multi-source evidence?
  Yes -> include 01; include 02 for source discovery.

Does it concern financial crime, fraud, sanctions, surveillance, digital assets,
regulatory intelligence, or entity/jurisdiction risk?
  Yes -> include 04.

Does it require a case disposition, screening decision support, risk assessment,
control/test, issue, policy gap, exam response, or new-product governance?
  Yes -> include 05.

Does it use structured data, trackers, metrics, joins, or reconciliation?
  Yes -> include 06.

Does it create a polished deliverable?
  Yes -> include 07.

Is it recurring, stateful, scheduled, multi-agent, or capable of writes?
  Yes -> include 08 and 11.

Will anyone rely on or distribute the result?
  Yes -> include 09.

Every substantial task -> include 00.
```

## 2. Standard bundles

| Bundle | Key | Modules | Approx. context | Fits |
|---|---|---|---|---|
| Core analysis | `core` | `00`, `07`, `09` | ~44k | provided materials, no external research or structured population |
| Reporting and dashboards | `reporting` | `00`, `06`, `07`, `09` | ~59k | memo, workbook, deck, dashboard, or maintained tracker |
| Data and controls | `controls` | `00`, `05`, `06`, `07`, `09` | ~68k | controls, testing, CDEs, lineage, issues, model/data review |
| Maintained operation | `operation` | `00`, `06`, `08`, `09`, `11` | ~72k | recurring tracker or monitored workflow; add the domain modules the task needs |
| Mailbox intelligence | `mailbox` | `00`, `03`, `06`, `07`, `09` | ~74k | inbox, shared mailbox, chat, ticket, or intake corpus |
| Research and OSINT | `research` | `00`, `01`, `02`, `07`, `09` | ~92k | public-source research, regulatory scans, background intelligence |
| Entity and financial-crime | `entity` | `00`, `01`, `02`, `04`, `05`, `07`, `09` | ~113k | entity, sanctions/PEP, adverse information, typology, case review |
| Investigation and case review | `investigation` | `00`, `01`, `02`, `04`, `05`, `06`, `07`, `09` | ~128k | case work that also depends on structured transaction or record data |
| Full system | `full` | `00`–`11` | ~176k | project knowledge base or complex cross-domain operation |

This is the controlling bundle registry. The [repository README](../README.md) table and
`bundle.py` restate it; validation fails if any of the three disagree. The key column is
the argument to `python3 bundle.py --bundle <key>`, which assembles the bundle into one
attachable file. Load `AGENTS.md` as repository instructions alongside any bundle when the
environment supports it.

Approximate context figures are coarse estimates at four characters per token, for
attachment sizing only. Check them before loading: an assistant that truncates attached
context does not announce it, and a partially loaded bundle can produce confident output
under rules it never read. If a bundle does not fit, drop a domain module and state the
reduced coverage in the output.

Module `09` is not optional merely because the output is internal. Its gate should scale
to impact and urgency, and it is never the module to drop for size.

## 3. Universal project brief

Complete this once, then use the selected recipe.

```yaml
project_id: <stable-id>
objective: <concrete outcome>
decision_supported: <who decides what>
requester_and_audience: []
accountable_owner: <role>
scope:
  objects: []
  populations: []
  systems_or_sources: []
  period: <start/end>
  as_of: <timestamp/timezone>
  included: []
  excluded: []
authority:
  read: []
  write: []
  human_approval: []
expected_control_totals: []
materiality_and_thresholds: []
deliverables: []
required_reviews: []
deadline: <timestamp>
retention_and_classification: <rule/label>
```

No recipe authorizes access or action. The brief must state both.

## 4. Universal execution sequence

1. Load modules and resolve instruction conflicts.
2. Return a preflight: objective, decision, scope, access, gaps, plan, output, gates.
3. Create stable IDs and run manifest.
4. Inventory inputs and expected populations.
5. Acquire/preserve evidence and raw data.
6. Normalize, deduplicate, resolve identities, and reconcile.
7. Apply the domain method and test alternatives.
8. Draft findings, severity, confidence, recommendation, and actions.
9. Render the selected artifact from one source of truth.
10. Run data, content, visual, privacy, and action release gates.
11. Obtain required approval; execute only the authorized action.
12. Record outcome, state, evidence, and lessons for refresh.

## 5. Full mailbox or shared-inbox review

| Element | Recipe |
|---|---|
| Objective | Create a complete, deduplicated, thread-aware index and decision/action view of a mailbox or approved folder set |
| Load | `00`, `03`, `06`, `07`, `09`; add `08` and `11` if recurring |
| Minimum inputs | mailbox/folders, access authority, period, expected count or control report, inclusion/exclusion rules, time zone, issue taxonomy, owners/SLAs, output |
| Core steps | manifest; folder and paging inventory; immutable message/attachment capture; canonical ID; thread reconstruction; quoted/signature removal without deleting raw text; duplicate/version logic; entity/issue/action/decision/deadline extraction with evidence spans; reconciliation; review queue; digest/tracker |
| Outputs | corpus manifest, message/thread index, issue/action/decision registers, attachment inventory, exception/failure log, executive digest, coverage and QA report |
| Gates | Canonical reconciliation from module `00`: `items received or identified = processed + duplicates + excluded by rule + unparsed + inaccessible + deferred`, with mutually exclusive terminal buckets; every processed item has one disposition; uncertain extraction remains reviewable; external drafts not sent without approval |

Use module `03`'s canonical schemas. Do not summarize only the inbox landing page or a
search result and call it a mailbox review.

## 6. Escalation-intake inbox to operational tracker

| Element | Recipe |
|---|---|
| Objective | Convert inbound escalation threads into a controlled case/action tracker without losing source context |
| Load | `00`, `03`, `05`, `06`, `07`, `09`; add `08`, `11` for maintained operation |
| Minimum inputs | intake address/folders, intake fields, routing/severity rules, teams, SLAs, case system, duplicate/related-case policy, approval/write authority |
| Core steps | ingest and reconcile; identify original escalation vs replies/forwards; resolve case/thread identity; extract subject, issue, event, requested decision, urgency, owner, deadlines, commitments, attachments; map to existing cases; flag missing intake data; propose routing; generate draft acknowledgments/requests; sync only after gate |
| Outputs | intake register, canonical case map, SLA/aging dashboard, missing-information queue, proposed routing, draft responses, reconciliation/exception report |
| Gates | prevent duplicate cases; preserve reporter confidentiality; no automated disposition or send; every sync uses idempotency key and confirmation |

## 7. Entity or counterparty risk assessment

| Element | Recipe |
|---|---|
| Objective | Support an onboarding, periodic review, exposure, partnership, or monitoring decision with a complete evidence-led assessment |
| Load | `00`, `01`, `02`, `04`, `05`, `06` if structured data, `07`, `09` |
| Minimum inputs | resolved subject identifiers, decision, jurisdiction/product scope, as-of date, approved risk methodology, internal profile/activity, source-of-funds/wealth requirements, prior decisions |
| Core steps | resolve entity; classify business/entity typology; trace ownership/control; inventory product/geographic/activity exposure; screen required subjects; research regulatory standing/enforcement/adverse information; analyze financial/governance/technology/third-party risk; score with visible weights/missing treatment/floors/overrides; sensitivity; conditions/actions |
| Outputs | executive assessment, domain scorecard, ownership table/diagram, chronology, screening and evidence ledger, conditions/action tracker, source/limitation appendix |
| Gates | missing public information not automatically adverse; allegations retain status; human decides onboarding/restriction/offboarding; all scores and overrides trace to evidence |

## 8. Corporate registry and beneficial-ownership investigation

| Element | Recipe |
|---|---|
| Objective | Establish legal existence, ownership, control, and relevant connected parties across jurisdictions |
| Load | `00`, `01`, `02`, `04`, `05`, `06`, `07`, `09` |
| Minimum inputs | legal names, identifiers, known jurisdictions, as-of date, ownership/control threshold and aggregation rule, purpose of analysis |
| Core steps | search official registries; preserve filings and dates; resolve similarly named entities; build layer-by-layer graph; calculate indirect ownership along independent paths; separate economic interest from control; reconcile each layer; identify unresolved/nominee/trust structures; screen required nodes; search historical directors/owners and status changes |
| Outputs | ownership/control register, network diagram specification, source ledger, calculation table, unresolved-evidence requests, risk implications |
| Gates | do not infer ownership from co-location; prevent double counting; distinguish registered, beneficial, and controlling parties; apply current jurisdiction-specific rules through authorized policy/legal review |

## 9. Sanctions, PEP, or watchlist review

| Element | Recipe |
|---|---|
| Objective | Produce a traceable candidate disposition and indirect-exposure analysis under applicable policy |
| Load | `00`, `01`, `02`, `04`, `05`, `06`, `07`, `09` |
| Minimum inputs | subject identifiers, applicable lists/regimes, list version/time, matcher version/threshold, ownership/control data, policy and escalation route |
| Core steps | confirm input subject; obtain current official list; generate candidates; compare decisive and supporting attributes; test transliteration/aliases; resolve conflicts/missing data; analyze ownership/control and nexus separately; document proposed disposition and rationale; independent review |
| Outputs | subject/candidate comparison matrix, list/source manifest, ownership exposure table, proposed disposition, unresolved queue, reviewer record |
| Gates | no auto-clear of plausible true match; no action based solely on name score; missing decisive attributes produce unresolved state; authorized reviewer decides and acts |

## 10. Adverse-information or reputational-risk review

| Element | Recipe |
|---|---|
| Objective | Identify material, correctly attributed adverse events and their current procedural status |
| Load | `00`, `01`, `02`, `04`, `05`, `07`, `09` |
| Minimum inputs | subject identifiers, languages/jurisdictions, event taxonomy, period, decision/materiality, approved media/source access |
| Core steps | identity-led query matrix; search official records and quality reporting; capture direct links/dates; cluster syndication into underlying events; retrieve primary records; classify allegations/proceedings/outcomes; search corrections/appeals/remediation; relevance/recency/materiality; counterevidence; negative-search log |
| Outputs | event register, source clusters, chronology, finding cards, search/coverage log, decision implications |
| Gates | no headline-only conclusion; no duplication as corroboration; no charge-as-conviction or settlement-as-admission error; privacy and defamation-sensitive review |

## 11. Transaction alert triage and investigation

| Element | Recipe |
|---|---|
| Objective | Explain a trigger in full activity context and propose a documented disposition |
| Load | `00`, `04`, `05`, `06`, `07`, `09`; add `01`, `02` for external enrichment |
| Minimum inputs | alert/rule/version, subject profile, complete relevant transaction population, account/product, peer/baseline, prior alerts/cases, period/time zone, policy criteria |
| Core steps | validate trigger; reconcile ledger; handle reversals/duplicates/FX/time; build chronology; calculate velocity/concentration/aggregation/dwell time; map counterparties/network; compare expected/own-history/peer; test typologies and alternatives; identify data/control defect; propose disposition and next actions |
| Outputs | case memo, transaction table, chronology, fund-flow reconciliation, typology matrix, evidence index, proposed disposition, information requests |
| Gates | trigger is not conclusion; incomplete activity cannot support no-issue closure; human decides regulated disposition; data defect routes to affected-population assessment |

## 12. Investigation and filing-decision support pack

| Element | Recipe |
|---|---|
| Objective | Assemble complete facts, analysis, and narrative support for an authorized filing or escalation decision |
| Load | `00`, `01`, `02`, `04`, `05`, `06`, `07`, `09` |
| Minimum inputs | case scope, subject/account identifiers, transactions/events, prior related records under approved access, applicable criteria/deadline, decision-maker |
| Core steps | case plan/hypotheses; identity resolution; full ledger and chronology; internal/external evidence; typology and alternatives; amounts/parties/date range; decision criteria; draft narrative; independent QA; decision record |
| Outputs | decision memo, narrative draft, subject and activity schedules, evidence index, related-case map, approval/filing checklist |
| Gates | assistant does not make/file decision; confidentiality rules applied; exact jurisdiction-specific requirements sourced from current authority/policy; final submission separately confirmed |

## 13. Fraud-event response and fund recovery support

| Element | Recipe |
|---|---|
| Objective | Rapidly establish event, preserve evidence, support containment/recovery, identify network, and document victim-sensitive next steps |
| Load | `00`, `03` if communications, `04`, `05`, `06`, `07`, `08` for coordinated operation, `09`, `11` |
| Minimum inputs | event/report, accounts/transactions, authentication/device data, communications, timing, payment rails, response authority, recovery contacts/process |
| Core steps | urgent triage; preserve data; authenticate reporter/subject; establish unauthorized vs deceptively authorized; trace funds; identify beneficiary/device/account network; distinguish victim, mule, and organizer evidence; propose containment/recall under approved procedure; log actions and outcomes; systemic/control assessment |
| Outputs | incident chronology, fund-flow/network, action log, recovery tracker, case referrals, customer communication drafts, control-gap report |
| Gates | urgent writes require explicit authority and current-state confirmation; sensitive victim handling; no accusation beyond evidence; legal/law-enforcement referral gate |

## 14. Trade or communications surveillance case

| Element | Recipe |
|---|---|
| Objective | Join market/order/trade/access/communication evidence to assess a conduct hypothesis |
| Load | `00`, `03`, `04`, `05`, `06`, `07`, `09` |
| Minimum inputs | alert/scenario, orders/trades/positions, market/reference data, employee/client/account links, access/restricted-list events, relevant communications, time synchronization |
| Core steps | validate clocks and identifiers; reconstruct order/trade/event timeline; benchmark market behavior; resolve beneficial control; extract communication evidence in thread context; test manipulation/conduct typology and legitimate execution explanations; quantify benefit/impact; propose disposition |
| Outputs | integrated chronology, trade/order exhibits, communication excerpts with source spans, relationship map, typology matrix, decision memo |
| Gates | unusual statistics do not prove intent; concerning language does not prove activity; protect unrelated/private communications; specialized reviewer makes conduct decision |

## 15. Regulatory-intelligence monitor and obligation tracker

| Element | Recipe |
|---|---|
| Objective | Detect material regulatory changes and translate them into owned obligations and implementation actions |
| Load | `00`, `01`, `02`, `04`, `05`, `06`, `07`, `08` if recurring, `09`, `11` |
| Minimum inputs | authorities, jurisdictions, topics, products, prior source state, scan cadence, materiality, policy/control inventories, owners |
| Core steps | source registry; scheduled/delta collection; version/hash comparison; deduplicate releases; classify instrument/status; extract atomic obligations; exact citations/dates; impact and gap mapping; assign owners; quality/reviewer gate; persist source/action state |
| Outputs | flash alerts, weekly brief, obligation register, policy/control gap map, action tracker, source-health/coverage report, change log |
| Gates | proposal vs final vs effective clear; speeches/nonbinding material labeled; no legal conclusion without authorized review; source failures visible; no duplicate alerts across reruns |

## 16. Policy gap and remediation program

| Element | Recipe |
|---|---|
| Objective | Demonstrate how authoritative requirements map to policy, procedures, controls, systems, evidence, tests, and remediation |
| Load | `00`, `01`, `02`, `05`, `06`, `07`, `09`; add `08`, `11` for maintained tracker |
| Minimum inputs | current requirements, policies/procedures, control inventory, systems/data, prior gaps, owners, deadlines, approval model |
| Core steps | extract atomic obligations; map complete requirement attributes; classify coverage; validate actual implementation/evidence; write precise gaps; severity/impact; root cause; remediation milestones; closure tests; governed change log |
| Outputs | traceability matrix, gap report, remediation plan/tracker, executive one-pager, validation/closure workpapers |
| Gates | mention of topic is not coverage; current authoritative text and document versions; legal interpretation gate; closure requires evidence and independent validation |

## 17. Control inventory, risk-control matrix, and testing program

| Element | Recipe |
|---|---|
| Objective | Build a complete control universe, map it to risk/obligations, and operate a defensible testing plan |
| Load | `00`, `05`, `06`, `07`, `09` |
| Minimum inputs | processes/risks/obligations, control sources, owners, systems, evidence, testing history, issues, population reports |
| Core steps | inventory/dedupe controls; rewrite complete activity; map risk/objective/obligation; classify nature/execution/frequency/key status; dependency and coverage analysis; design assessment; risk-based testing plan; population reconciliation; sampling/full-population tests; issue and remediation linkage |
| Outputs | control matrix, coverage/gap view, test plan, testing workpapers, exceptions/issues, committee summary |
| Gates | no invented controls/evidence; inquiry alone insufficient; critical defects not averaged away; sample claims match selection design; formulas/totals reconcile |

## 18. Data-quality assessment or sentinel

| Element | Recipe |
|---|---|
| Objective | Determine whether a dataset/process is fit for a defined decision and maintain controlled detection of degradation |
| Load | `00`, `06`, `07`, `09`; add `05` for control implications and `08`, `11` for recurring monitoring |
| Minimum inputs | data product/use case, sources, expected totals, schema/contracts, CDEs, lineage, owners, thresholds, historical baselines, incident process |
| Core steps | inventory/profile; key and control-total reconciliation; CDE rules across completeness/accuracy/validity/consistency/timeliness/uniqueness; cross-source tie-outs; segmentation; lineage/control mapping; defect sampling; root cause; impact/affected population; issue actions; recurring delta checks |
| Outputs | data-quality report, rule catalog/results, exception table, lineage, source-health dashboard, incident/remediation tracker, fit-for-use conclusion |
| Gates | quality is decision-specific; passing averages cannot hide critical-field failure; thresholds versioned; failures trace to records; output does not imply source truth where no reference exists |

## 19. Model, rule, threshold, or matcher review

| Element | Recipe |
|---|---|
| Objective | Assess conceptual soundness, data, implementation, performance, stability, governance, and decision risk |
| Load | `00`, `05`, `06`, `07`, `09`; add `04` for domain typologies and `11` for deployment |
| Minimum inputs | intended use, model/rule code or specification, data lineage, versions, tuning/validation data, thresholds, outcomes, overrides, monitoring, governance |
| Core steps | scope/prohibited use; conceptual review; data quality/leakage; independent implementation/reperformance; performance by segment; false-negative safety; calibration/stability/drift; threshold sensitivity; overrides; documentation/change/access/rollback; findings and remediation |
| Outputs | validation report, test notebook/workpaper, metric and segment tables, limitations, findings/issues, monitoring and change conditions |
| Gates | no accuracy claim without sample/population and uncertainty; no synthetic-only evidence presented as production performance; high-impact use requires independent validation and human governance |

## 20. New product or activity approval

| Element | Recipe |
|---|---|
| Objective | Decide whether a product/change is ready, under which conditions, and how post-launch risk is monitored |
| Load | `00`, `01`, `02`, `04`, `05`, `06`, `07`, `09`; add `08`, `11` for operationalization |
| Minimum inputs | product/process/data flows, legal entities, users/geographies, expected volumes, third parties, regulatory analysis, risks/controls/tests, launch plan |
| Core steps | classify activity; end-to-end flow; obligations/permissions; risk domains; typology threat model; risk-control-test traceability; data/privacy/security/operations/vendor readiness; residual risk; blocking conditions; approval record; post-launch metrics/review |
| Outputs | risk assessment, control/condition matrix, decision memo, launch checklist, monitoring plan, post-implementation review template |
| Gates | unresolved mandatory control remains blocker; planned control not represented as operating; legal/policy approval current; rollback/incident path tested; human governance body decides |

## 21. Third-party, vendor, correspondent, or embedded-partner review

| Element | Recipe |
|---|---|
| Objective | Assess direct and indirect access, ownership, services, control reliance, concentration, and exit risk |
| Load | `00`, `01`, `02`, `04`, `05`, `06`, `07`, `09` |
| Minimum inputs | entity/ownership, services and data/funds flow, subcontractors/downstream access, contracts/SLAs, control evidence, incidents, financial/regulatory standing, concentration/exit plan |
| Core steps | identity/ownership; service and access mapping; regulatory/financial-crime/cyber/data/business-continuity risk; downstream/nested relationships; control and assurance evidence; concentration and substitutability; contractual controls; issues/conditions; ongoing monitoring |
| Outputs | due-diligence assessment, service/data flow, critical-dependency register, control/evidence matrix, conditions/action plan, monitoring schedule |
| Gates | assurance report not treated as universal coverage; period/scope/subservice carve-outs analyzed; self-reported claims unverified; procurement/contract/relationship decision human-approved |

## 22. Digital-asset protocol, token, VASP, or fund-flow review

| Element | Recipe |
|---|---|
| Objective | Assess entity/protocol risk or trace on-chain activity with off-chain attribution discipline |
| Load | `00`, `01`, `02`, `04`, `05`, `06`, `07`, `09` |
| Minimum inputs | entity/protocol classification, chains/assets, addresses/transactions, as-of, attribution sources, governance/legal entities, product and jurisdiction scope |
| Core steps | classify service/exposure; legal entity/control map; licensing/regulatory status; governance/admin keys/dependencies; financial/reserve/liquidity risks; sanctions/typology analysis; transaction trace with hashes/hops/bridges/swaps/fees/valuation; independent attribution; alternatives and limitations |
| Outputs | risk report or trace report, on/off-chain network, transaction and attribution ledger, reconciliation, typology matrix, controls/actions |
| Gates | transaction does not prove owner/intent; vendor label confidence visible; direct vs indirect exposure and time stated; relevant current regulation verified; consequential decision human-approved |

## 23. Committee, management, or board reporting pack

| Element | Recipe |
|---|---|
| Objective | Provide a reconciled decision-centric view of performance, risk, incidents, issues, controls, and forward actions |
| Load | `00`, relevant domain modules, `06`, `07`, `09`; add `08`, `11` for recurring pack |
| Minimum inputs | prior pack/decisions, governed KPI definitions, source cuts, issues/incidents, testing, regulatory developments, actions, meeting decisions |
| Core steps | inventory questions/decisions; lock data cut; refresh metrics from governed sources; reconcile and variance analysis; material changes; exception and overdue review; source/data-quality state; write message titles; action/decision log; render slides plus appendices; review |
| Outputs | executive deck/PDF, source workbook, action and decision log, metric dictionary, QA/approval record |
| Gates | every KPI has numerator/denominator/period/source/owner; totals agree across formats; prior actions accounted for; no cosmetic green status over material overdue issue; meeting outcomes captured after approval |

## 24. Professional dashboard or maintained tracker

| Element | Recipe |
|---|---|
| Objective | Create a bank-friendly, interactive, source-linked view that supports governed exploration and export |
| Load | `00`, `06`, `07`, `09`; add domain modules and `08`, `11` for connected operation |
| Minimum inputs | decision questions, users/access, metrics/data contracts, source/refresh, drill-through fields, export needs, deployment environment, branding/accessibility |
| Core steps | define data/metric contract; reconcile source; sketch decision hierarchy; build restrained light theme; implement filters/KPIs/charts/findings/detail/method/source/data-quality states; export manifest; optional schema-bound assistant; browser and print QA |
| Outputs | dashboard, governed data/export, metric dictionary, source register, user guide, QA report, deployment/rollback record |
| Gates | no unsupported live claim; no hidden network/write behavior; access enforced at data layer; all numbers match source; responsive/accessibility/export/source links tested; no novelty-first visuals |

## 25. Regulatory examination or formal information response

| Element | Recipe |
|---|---|
| Objective | Track, assemble, review, and deliver a complete response package with version and evidence control |
| Load | `00`, `01`, `02`, `05`, `06`, `07`, `08` if large/recurring, `09`, `11` |
| Minimum inputs | request letter/questions, due dates, entities/periods, delivery specifications, owners/reviewers, privilege/confidentiality rules, source systems |
| Core steps | atomize requests; assign owner/reviewer; source/evidence manifest; collect and reconcile responsive population; exceptions; draft direct responses; verify current/historical/planned state; redaction and legal review; file/index/hash QA; approved delivery; confirmation log |
| Outputs | request tracker, response narrative, indexed production, source/evidence manifest, gap/exception log, review/approval record, submission confirmation |
| Gates | never create historical evidence; privilege/redaction handled by authorized reviewers; exact requested format/scope; duplicate/omitted file checks; external submission separately approved and confirmed |

## 26. Recurring intelligence or operations agent

| Element | Recipe |
|---|---|
| Objective | Run a controlled delta-based workflow repeatedly without duplicate actions or silent degradation |
| Load | `00`, relevant domain modules, `06`, `07`, `08`, `09`, `11` |
| Minimum inputs | schedule/trigger, source registry, state authority, last-good checkpoint, output destinations, budgets, SLAs, owners, fallback and approval rules |
| Core steps | acquire lock; load state; verify source health; collect delta with overlap; normalize/dedupe; reconcile; analyze; compare prior; produce an immutable draft and exact action preview; validate and self-check; obtain specific human approval; persist the approval reference; claim the approved deterministic action key in the outbox; publish once; verify and confirm the destination receipt; confirm the outbox action; persist authoritative state; health report; release lock |
| Outputs | current report/tracker, delta log, source-health and coverage metrics, outbox/action receipts, state/checkpoint, exception/incident log |
| Gates | idempotency and canonical IDs; state advances only after confirmed outcome; fallbacks visible; no fallback for compliance-critical decisions/writes; proposed self-repair gated; deadman/liveness monitor independent |

## 27. Team-to-bundle map

| Team/function | Start with | Common recipes |
|---|---|---|
| Sanctions and screening | entity/financial-crime bundle | 7–10 |
| Transaction monitoring | entity/financial-crime plus data | 11–12, 17–19 |
| Fraud operations | financial-crime plus communications/data | 6, 11, 13 |
| Trade and communications surveillance | communications plus financial-crime/data | 14, 19 |
| Investigations and filing governance | full case bundle | 11–12, 23, 25 |
| KYC/CDD and onboarding | entity/financial-crime plus data | 7–9, 21 |
| Adverse-information screening | research/OSINT plus entity methods | 7, 10 |
| Third-party/correspondent/ABC | entity/financial-crime plus controls | 7, 21 |
| Digital assets/blockchain | research plus financial-crime/case/data | 22 |
| Financial-crime risk assessment | financial-crime plus controls/data | 7, 17, 23 |
| Controls/testing/internal assurance | data and controls | 16–19, 23 |
| Model risk/governance | data and controls plus domain module | 19, 23 |
| Data governance | data and controls | 18, 24, 26 |
| New product/activity governance | full cross-domain | 20, 23 |
| Regulatory affairs/exam management | research plus controls/operations | 15–16, 25–26 |

## 28. Thin-prompt patterns

### 28.1 One-time complete project

```text
Use the [recipe number/name] recipe and its required modules. My project brief is below.
Do the full lifecycle from preflight through a release-gated deliverable. Do not stop at
a summary or list of ideas. Reconcile the entire accessible population, preserve source
evidence, apply the specified domain method, test counterevidence, render the requested
artifact under module 07, and run module 09. Do not execute any action outside the exact
authority in the brief.

[paste completed universal project brief]
```

### 28.2 Build a repeatable workflow specification

```text
Use the [recipe] with modules 00, the relevant domain files, 06, 08, 09, and 11. Design an
implementation-neutral workflow that can be run manually first and automated later.
Include job manifest, schemas, deterministic IDs, state/checkpoints, reconciliation,
fallbacks, idempotency/outbox, human gates, source/output contracts, monitoring, incident
handling, security/privacy, acceptance tests, rollout, rollback, and maintenance. Label
which components are prompt-only, which require connectors/code, and which remain human
decisions. Do not claim an integration has been built unless it is implemented and
tested.
```

### 28.3 Refresh an existing artifact

```text
Refresh [artifact ID/version] through [as-of timestamp] using the same governed method
unless an approved change is documented. Load prior state and source manifest; collect an
overlapping delta; detect late revisions/deletions; deduplicate; reconcile; compare every
finding, metric, issue, action, source, and limitation to the prior version. Produce a
change log that distinguishes new, changed, resolved, reopened, unchanged, and unavailable
items. Run the same release tests plus regression checks. Do not overwrite the prior
approved artifact; issue a new version and mark supersession only after approval.
```

## 29. Project acceptance criteria

Every recipe inherits these conditions:

- the decision and accountable role are explicit;
- scope, period, as-of, authority, classification, and expected populations are fixed;
- raw inputs and source lineage are preserved within policy;
- processed, excluded, failed, and duplicate totals reconcile;
- identities and versions are resolved before attribution;
- material claims link to evidence and retain claim status;
- the domain framework is named/versioned and applied consistently;
- alternatives and data/control-error explanations are tested;
- recommendations are proportionate, owned, dated, and gated;
- multi-format outputs share one analytical source of truth;
- privacy, security, prompt-injection, and external-action controls apply;
- module `09` release gate passes;
- approved actions are distinct from proposals and are confirmed after execution;
- recurring work persists state, outcomes, and lessons without duplicate effects.
