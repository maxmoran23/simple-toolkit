# Quality Assurance and Audit Standard

Use this file to determine whether an analysis, dataset-dependent conclusion, document, spreadsheet, presentation, dashboard, code output, model-assisted workflow, or automation is ready for its stated audience and decision.

Quality assurance is evidence-based challenge, not copyediting and not a second summary. Review the question, population, sources, data, logic, calculations, claims, limitations, rendered artifact, controls, and release path. A polished artifact with an unsupported conclusion fails. A technically correct artifact with material missing sections also fails. A workflow that can take external action without appropriate authorization fails even when its draft output is accurate.

## 1. Non-negotiable principles

1. **Review the actual claim.** Test what the artifact asks a reader to believe or do, not only whether the format is complete.
2. **Risk determines depth.** Consequence, audience, reversibility, automation, sensitivity, uncertainty, and external use set the review level.
3. **Evidence outranks fluency.** Every material claim must trace to an appropriate source, calculation, or reproducible artifact.
4. **Independence is explicit.** Record who prepared, reviewed, approved, and released the work; disclose self-review and conflicts.
5. **Data quality is a dependency.** If the underlying population, grain, freshness, or reconciliation is unreliable, the conclusion cannot be more reliable.
6. **Recompute high-impact results.** Inspection without independent reperformance is limited assurance.
7. **Fact, allegation, inference, and projection remain distinct.** Do not let narrative confidence erase evidence type.
8. **Zero issues is a result, not a target.** Reviewers are not measured by pass rate or defect count.
9. **Critical defects are vetoes.** No score, style improvement, or unrelated strength offsets a release-blocking issue.
10. **Unperformed checks remain unperformed.** Label them and explain the impact; never convert missing evidence to pass.
11. **Rendered output is the deliverable.** Inspect the final file or interface in the intended viewer, not only source code or a template.
12. **Automation changes the control burden.** Permission, idempotency, failure behavior, monitoring, and human gates are part of quality.
13. **External actions fail closed.** No send, post, publication, assignment, deletion, merge, approval, or state change occurs merely because QA generated a favorable recommendation.
14. **Evidence survives the run.** Preserve the review plan, frozen artifact, source map, calculations, defects, corrections, sign-off, and release record.

## 2. Applicability and boundaries

### Artifacts covered

- analytical memos, research briefs, investigations, recommendations, and decision papers;
- tabular analyses, extracts, query results, notebooks, models, and calculations;
- dashboards, scorecards, reports, PDFs, documents, presentations, spreadsheets, and HTML artifacts;
- communication drafts and tracker updates;
- deterministic rules, scripts, data pipelines, agent prompts, model-assisted workflows, and automations;
- material revisions, restatements, reruns, and post-release corrections.

### QA does not by itself

- approve business, legal, regulatory, risk, or policy decisions;
- validate inaccessible source systems or controls it could not inspect;
- guarantee future model, source, or automation performance;
- convert a sample observation into certainty about the full population;
- authorize external distribution or a system action;
- replace subject-matter judgment where the decision requires it;
- fix defects unless remediation is separately requested and authorized.

### Standard assessment outcomes

| Outcome | Meaning | Release treatment |
|---|---|---|
| `READY_TO_RELEASE` | Scope is satisfied, key evidence and calculations are verified, no open material defect remains, limitations are clear | Release still requires the designated owner/approver |
| `READY_WITH_DISCLOSED_LIMITATIONS` | Fit for the stated narrow use, with non-material or unavoidable limitations that are visible and accepted | Restrict use/audience as stated; owner approval required |
| `NEEDS_REVISION` | One or more defects materially affect correctness, support, completeness, usability, or control | Do not release as final |
| `NOT_REVIEWABLE` | Required artifact, source, population, method, or evidence is unavailable or unreadable | Do not infer pass; obtain missing material or narrow the claim |

`READY_WITH_DISCLOSED_LIMITATIONS` is not available when a limitation undermines the central question, a hard gate is untested, or a consequential external action lacks an approved control.

## 3. Roles, independence, and accountability

### Roles

| Role | Responsibility |
|---|---|
| Preparer | Produces the artifact and supplies complete source/method evidence |
| Data owner/steward | Confirms data definition, fitness, limitations, and approved use |
| Analytical reviewer | Challenges question, method, calculation, interpretation, and claim support |
| Subject-matter reviewer | Confirms domain standards, definitions, obligations, and practical implications |
| Technical reviewer | Reviews code, queries, pipelines, model/automation design, security, and deployment |
| Artifact reviewer | Checks rendered document, spreadsheet, dashboard, presentation, or communication |
| Independent validator | Performs proportionate reperformance and effective challenge outside the build path |
| Risk/records/legal reviewer | Reviews only where required by content, policy, audience, or action |
| Release owner | Decides whether and how to use or distribute the approved artifact |
| Action approver | Separately authorizes any external or state-changing action |

### Independence rules

- The preparer may self-check but may not represent self-check as independent validation.
- Higher-risk work requires a reviewer who did not design the decisive method, rule, model, or calculation.
- Record organizational, financial, authorship, or outcome conflicts that could impair challenge.
- A reviewer must have the source access and competence required for the assertions signed.
- When full independence is impractical, disclose the limitation, add compensating review, and narrow the conclusion.
- Reviewers sign only the domains actually reviewed.
- The release owner cannot waive a required specialist or technical review without documented authority and residual-risk acceptance.

## 4. Risk tiering and review depth

### Risk factors

Assess:

- consequence if wrong, incomplete, stale, or misunderstood;
- external, executive, legal, regulatory, contractual, financial, or public audience;
- whether the output drives an approval, restriction, escalation, filing, payment, customer-impacting decision, or control action;
- sensitivity, confidentiality, privilege, security, and privacy;
- reversibility and time to detect/correct;
- complexity of data, joins, models, assumptions, or transformations;
- novelty of method, source, model, prompt, code, or output format;
- degree of automation and permission to create side effects;
- source quality, conflict, coverage, freshness, and fallback use;
- sample size, uncertainty, model error, or subjective judgment;
- material change since prior validation.

### Review tiers

| Tier | Typical condition | Minimum review |
|---|---|---|
| Tier 1 — Limited | Internal, reversible, low-consequence, simple, no external action | Preparer self-check; source and calculation spot-check; rendered review |
| Tier 2 — Standard | Recurring management or operational use; moderate consequence; multiple sources or transformations | Independent analytical review; data-quality checks; recalculation; artifact QA; owner sign-off |
| Tier 3 — Enhanced | High-consequence, external/formal, sensitive, model-assisted, complex, or materially changed | Independent validator and subject/technical specialists; full claim audit; reproducibility; expanded samples; formal release gates |
| Tier 4 — Controlled action | Workflow can communicate externally or change a system, record, entitlement, status, or decision | Tier 3 plus explicit action authorization, least privilege, idempotency/deduplication, dry run, failure/rollback test, monitored release |

If factors conflict, use the higher tier or document why a lower tier remains sufficient.

### Material-change triggers

Reperform review proportionate to impact when any of these change:

- purpose, audience, decision, scope, population, period, or timezone;
- source, field, schema, contract, reference data, or lineage;
- metric definition, denominator, exclusion, weighting, or threshold;
- transformation, join, query, formula, code, dependency, or environment;
- model, prompt, system instruction, tool permission, retrieval method, or fallback;
- visualization, narrative conclusion, recommendation, or release channel;
- data backfill, restatement, incident, or material source correction;
- owner, control, exception, approval, or regulatory/policy basis.

## 5. QA lifecycle

### Phase 0 — intake and freeze

1. Identify the artifact, version, owner, audience, decision, due date, and risk tier.
2. Freeze or hash the exact artifact being reviewed.
3. Inventory all requested sections, claims, metrics, outputs, actions, and attachments.
4. Obtain the source, data, method, code, environment, and prior-version package.
5. Create the review plan, materiality rules, sampling plan, and specialist-review requirements.
6. Record access gaps before testing.

### Phase 1 — establish scope and criteria

1. Restate the question in testable terms.
2. Define population, grain, period, timezone, eligibility, exclusions, metrics, comparators, and intended use.
3. Identify authoritative standards, contracts, policies, procedures, specifications, and acceptance criteria.
4. Map each required deliverable component to a test.
5. Identify hard gates and conditions that make the artifact not reviewable.

### Phase 2 — validate sources and data

1. Build the claim/source inventory.
2. Confirm source identity, authority, date, version, scope, and accessibility.
3. Apply the core controls in [06-data-quality-governance.md](06-data-quality-governance.md): grain, keys, completeness, accuracy where referenceable, validity, consistency, uniqueness, timeliness, integrity, reconciliation, and drift.
4. Trace critical values through lineage and transformations.
5. Identify missing populations, stale periods, fallbacks, and source conflicts.

### Phase 3 — validate method and calculations

1. Confirm the method answers the stated question.
2. Review assumptions, exclusions, causality, comparisons, sampling, uncertainty, and edge cases.
3. Recompute the highest-impact numbers independently.
4. Trace selected records through filters, joins, formulas, aggregations, and outputs.
5. Test reasonableness, counterexamples, and alternative explanations.

### Phase 4 — audit claims and narrative

1. Classify every material claim by evidence type.
2. Verify each citation at the exact location and effective date.
3. Confirm the wording does not exceed the evidence.
4. Separate findings, interpretations, limitations, open questions, and recommendations.
5. Remove or qualify unsupported claims.

### Phase 5 — inspect final artifact

1. Render/open the artifact in the target environment.
2. Test tables, figures, filters, links, exports, formulas, navigation, pagination, accessibility, and placeholders.
3. Reconcile every displayed headline, total, and chart to the approved calculation.
4. Confirm classification, source, as-of, version, caveat, and ownership metadata.

### Phase 6 — assess model and automation controls

1. Inventory models, prompts, tools, permissions, state, and external effects.
2. Test deterministic gates, evaluation evidence, fallback behavior, prompt-injection controls, failure handling, action deduplication, and human approval.
3. Confirm the workflow does only what the approved design permits.

### Phase 7 — defects, remediation, and retest

1. Record issues with evidence, impact, severity, owner, and required fix.
2. Block release where gates fail.
3. Review the actual correction, not a statement that it was corrected.
4. Reperform affected tests and regression checks.
5. Preserve prior artifact and issue history.

### Phase 8 — release decision and evidence package

1. Confirm every gate has pass/fail/not-tested status.
2. State the assessment outcome and unresolved limitations.
3. Obtain domain-specific sign-offs and release-owner approval.
4. Preserve the evidence package and released artifact hash.
5. Monitor post-release incidents, corrections, and performance where required.

## 6. Review plan and artifact inventory

### Review-plan schema

```yaml
review_id: <stable id>
artifact:
  name: <name>
  type: <memo/report/spreadsheet/dashboard/code/model/automation/etc.>
  version: <version>
  hash: <hash>
  preparer: <role>
purpose: <question/decision/action>
audience: <audience>
intended_use: <use>
prohibited_use: <use>
risk_tier: <1/2/3/4>
materiality:
  quantitative: <rules>
  qualitative: <rules>
hard_gates: [<gate ids>]
scope:
  population: <definition>
  period: <bounds>
  timezone: <zone>
  inclusions: [<rules>]
  exclusions: [<rules>]
required_sections: [<sections>]
headline_claims: [<claim ids>]
headline_metrics: [<metric ids>]
sources_expected: [<source ids>]
data_inputs: [<data product/version>]
methods: [<method/code/query/model refs>]
specialist_reviews: [<domain/role>]
sampling_plan: <reference or full-population>
due_at: <date/time>
status: <planned/in_progress/remediation/complete>
```

### Artifact inventory

Inventory:

- files, tabs, sheets, pages, slides, views, routes, and attachments;
- hidden sheets/rows/columns, appendices, notes, comments, and metadata;
- data connections, macros/scripts, external links, embedded files, and remote assets;
- queries, notebooks, code, parameters, models, prompts, configuration, and environment;
- output channels and intended viewers;
- requested and required sections;
- claims, metrics, recommendations, decisions, and proposed actions;
- prior versions, approved template, and change history.

An unreviewed appendix, hidden sheet, embedded object, or export function remains part of the deliverable if a recipient can access it.

## 7. Source and claim audit

### Source hierarchy

| Tier | Source type | Treatment |
|---|---|---|
| `T1 AUTHORITATIVE PRIMARY` | Original authoritative record, official filing/order, source-system record, signed document, direct measurement, or executable output | Preferred for material facts after identity, authenticity, version, scope, and effective-date checks |
| `T2 ACCOUNTABLE SECONDARY` | Named, method-transparent analysis or reporting about primary material with an accountable correction path | Use for corroboration and context; seek the underlying T1 record when available |
| `T3 DISCOVERY` | Aggregator, search result, community contribution, third-party label, social post, or unattributed compilation | Lead generation only; cannot alone support a material finding |
| `TX EXCLUDED` | Fabricated, unauthenticated, circular, unlawfully obtained, deceptively presented, or without inspectable provenance | Do not rely on or cite as evidence; record the exclusion when material |

This is the canonical tier vocabulary defined in modules `00` and `01`. An internal
system is not automatically T1 or accurate merely because it is internal. Establish
authority, completeness, lineage, and control status for the proposition at issue.

### Claim classes

| Class | Meaning | Required wording |
|---|---|---|
| `OBSERVED` | Directly established in a primary source or verified calculation | State plainly with precise citation |
| `REPORTED` | Attributed statement from a traceable source, not independently established | Name who reported it and preserve attribution |
| `ALLEGED` | Unproven accusation or contested claim | Use explicit allegation language and status |
| `INFERRED` | Reasoned conclusion from observed inputs | State inference and reasoning; do not present as source text |
| `ESTIMATED` | Quantified value derived from incomplete observation or method | State method, range/uncertainty, and assumptions |
| `PROJECTED` | Forward-looking scenario or forecast | State assumptions, scenario, horizon, and uncertainty |
| `SPECULATIVE` | An unverified hypothesis or pattern-based possibility that lacks enough evidence for a finding | Label explicitly as a hypothesis, state what would verify it, and do not use it as a confidence tier |
| `RECOMMENDED` | Proposed action based on evidence and judgment | Separate recommendation from finding and name decision owner |

### Claim ledger

```yaml
claim_id: <id>
artifact_location: <page/section/cell/chart/slide/line>
claim_text: <exact or normalized claim>
claim_class: <OBSERVED/REPORTED/ALLEGED/INFERRED/ESTIMATED/PROJECTED/SPECULATIVE/RECOMMENDED>
materiality: <material/non-material and basis>
sources:
  - source_id: <id>
    exact_location: <page/paragraph/table/cell/query row>
    source_version_date: <value>
    support: <supports/partially supports/contradicts/context only>
calculation_id: <id or null>
assumptions: [<ids>]
limitations: [<ids>]
confidence: <HIGH/MODERATE/LOW/NOT ASSESSABLE and basis>
verification: <VERIFIED/PARTIAL/UNSUPPORTED/CONTRADICTED/UNAVAILABLE>
reviewer: <role>
reviewed_at: <date/time>
```

### Claim-audit tests

- The source exists, opens, and is the cited version.
- The citation points to the exact supporting location, not a home page or nearby discussion.
- The source covers the same entity, definition, population, geography, period, currency/unit, and status.
- The claim preserves qualifications and does not omit contradictory context.
- Numbers match source precision and sign.
- A secondary source is not cited as if it were the primary record.
- A search excerpt, summary, model output, or quoted passage is traced to the underlying source.
- The source date and effective date are appropriate to the “as of” claim.
- Archived or snapshotted evidence is retained where links may change and policy permits.
- Copyright, confidentiality, privacy, privilege, and licensing restrictions are respected.
- Every material claim has support; decorative or duplicative citations do not substitute for coverage.
- Contradictory sources are disclosed and assessed, not silently selected away.

### Confidence

| Rating | Typical basis |
|---|---|
| `HIGH` | Direct primary evidence or independently reproduced result; low ambiguity; material conflicts resolved |
| `MODERATE` | Single primary source, partial corroboration, or a supported inference with material caveats |
| `LOW` | Secondary-only, incomplete coverage, substantial assumption, weak relationship, or model-derived result without strong validation |
| `NOT ASSESSABLE` | Source conflict or missing evidence prevents a confidence assessment; use `UNRESOLVED` for the claim's verification or disposition status |

Always pair the rating with a reason. Confidence does not replace error bounds or source status.

## 8. Analytical and methodological review

### Question alignment

- The stated question matches the reader's decision.
- The analysis does not answer a narrower, easier adjacent question without disclosure.
- Outcome, exposure, population, horizon, and comparison are explicit.
- Descriptive, diagnostic, predictive, causal, and prescriptive questions are not conflated.
- Recommendations stay within the evidence and authority of the analysis.

### Population and eligibility

- Inclusion, exclusion, eligibility, survivorship, and observation windows are explicit.
- Missing, deleted, failed, inactive, closed, censored, or not-yet-observed populations are assessed.
- Cohorts are defined before the outcome when making comparative or causal claims.
- The same population definition is used across compared periods/segments or differences are disclosed.
- Partial periods are compared with equivalent elapsed periods or clearly labeled.
- Small and empty segments are handled explicitly.
- Selection mechanisms and coverage gaps are evaluated for bias.

### Metric definitions

For every headline metric record:

- name and plain-language definition;
- numerator and denominator;
- unit, currency, scaling, precision, and sign convention;
- population, grain, filters, and exclusions;
- event/effective/load/report time and timezone;
- aggregation and weighting;
- treatment of nulls, duplicates, late arrivals, reversals, and revisions;
- comparison baseline and restatement policy;
- source fields and transformation/query/formula;
- owner and version.

### Comparison validity

- Windows have equal or explicitly adjusted duration.
- Denominators and eligibility are stable.
- Currency, units, inflation, seasonality, business-day calendars, and cutoffs align where relevant.
- Cohorts have comparable exposure/opportunity.
- Changes in source coverage, product mix, definitions, policies, or processes are separated from underlying performance.
- Aggregate and segment-level patterns are checked for reversal or masking.
- A benchmark is independent and comparable, not selected after observing the result.

### Causality

Do not use “caused,” “drove,” “resulted in,” “impact,” or equivalent causal language solely from correlation, sequence, or stakeholder belief. A causal claim requires an appropriate design and assumptions: randomized evidence, credible quasi-experimental identification, or another defensible causal method. Otherwise use association language and discuss alternatives.

Review:

- treatment/exposure definition and timing;
- pre-treatment comparability;
- confounding and selection;
- parallel-trend or identification assumptions where applicable;
- interference, spillovers, attrition, and measurement changes;
- robustness, placebo, sensitivity, and heterogeneous effects;
- multiple comparisons and researcher degrees of freedom;
- difference between statistical and practical significance.

### Forecast, scenario, and estimate review

- Separate scenario assumptions from observed inputs.
- State horizon, base date, model/version, and update cadence.
- Show base, adverse/upside, or sensitivity cases only when analytically justified.
- Avoid false precision; use ranges where input or model uncertainty warrants.
- Backtest against out-of-sample periods where possible.
- Report calibration, error distribution, and segment performance, not only average error.
- Do not describe a scenario as likelihood unless probability was estimated and validated.
- Make clear that a projection is not a commitment, reserve, or observed fact.

### Qualitative analysis

- Coding framework, inclusion rules, unit of analysis, and reviewer instructions are explicit.
- Quotations and themes trace to source locations.
- Negative cases and contradictory evidence are retained.
- Inter-reviewer agreement or adjudication is used where classification materially affects the conclusion.
- Frequency of mention is not treated as prevalence without a valid sampling frame.
- Model-assisted coding is validated against human-reviewed examples and does not invent quotes.

## 9. Data selection and quality dependency

Apply [06-data-quality-governance.md](06-data-quality-governance.md) in proportion to risk. At minimum confirm:

- source authority and current version;
- intended grain and primary/candidate keys;
- complete period/partition/segment coverage;
- “as of” time and freshness;
- null, sentinel, and not-evaluated treatment;
- exact and near-duplicate handling;
- filter logic and exclusion accounting;
- join coverage, cardinality, and row/entity counts before and after;
- reference-data version and effective dating;
- schema/semantic drift and recent backfills;
- source-to-output reconciliation;
- CDE and critical-transformation defects;
- approved exceptions and downstream impact.

### Data-quality dependency outcome

| Status | Meaning for analysis |
|---|---|
| `FIT_FOR_STATED_USE` | Relevant controls pass for this use and period |
| `FIT_WITH_LIMITATIONS` | Specific limitations are quantified and do not overturn the narrow conclusion |
| `NOT_FIT` | Defect can materially change the conclusion or decision |
| `NOT ASSESSABLE` | Access, population, grain, or evidence is insufficient |

An analysis cannot be `READY_TO_RELEASE` when a material data dependency is `NOT_FIT` or `NOT ASSESSABLE`.

## 10. Calculation, query, and code review

### Independent recomputation

Prioritize:

1. headline numbers and recommendation drivers;
2. material reconciliations and regulatory/contractual figures;
3. rates with complex denominators;
4. weighted averages, allocations, and multi-stage calculations;
5. surprising movements, exact round values, zeros, and 100% results;
6. boundary dates, new segments, empty categories, and null-heavy populations;
7. calculations changed since the prior version.

Independence means a separate calculation path where practical, not merely rereading the same formula.

### Formula checks

- Numerator and denominator match the definition.
- Denominator is non-zero and excludes only documented populations.
- Percent, percentage-point, basis-point, ratio, index, and absolute changes are not confused.
- Weighted averages use underlying weights; avoid average-of-averages errors.
- Totals and mutually exclusive shares reconcile.
- Sign, unit, currency, precision, and rounding are consistent.
- Period-over-period and year-over-year bases align.
- Missing values are not silently converted to zero.
- Outliers are not removed without a documented rule and impact comparison.
- Rounding occurs at presentation, not prematurely in intermediate calculations.
- Confidence intervals and p-values use the correct design and assumptions.

### Query checks

- Source tables/files and versions are correct.
- `WHERE` filters match eligibility and do not drop nulls unintentionally.
- Join type and cardinality are intentional; row and distinct-entity counts are checked before/after.
- Aggregation grain matches the metric.
- `COUNT(*)`, `COUNT(field)`, and `COUNT(DISTINCT field)` are used intentionally.
- Window partitions/order are correct and deterministic.
- Effective-date and timezone logic handle boundaries.
- Late-arriving and restated records are treated consistently.
- Deduplication ordering has a stable tie-breaker.
- Unions align fields and do not double count overlapping populations.
- Reference joins use the correct effective version.

### Code and notebook checks

- Environment and dependencies are locked or recorded.
- Random seeds and nondeterministic operations are controlled where reproducibility is claimed.
- Functions, parameters, and defaults match the documented method.
- Errors fail visibly; broad exception handling does not convert failure to empty success.
- Temporary, debug, placeholder, and commented-out logic is absent from released code.
- Inputs are validated; output schema is asserted.
- Tests cover positive, negative, boundary, regression, and failure paths.
- Sensitive values do not appear in logs or fixtures.
- Notebook cells run in a clean environment from top to bottom without hidden state.
- Generated reports derive numbers from computation rather than hand-typed copies.

### Spreadsheet calculation checks

- Formula cells are formulas where expected, not pasted values.
- Relative/absolute references, ranges, named ranges, and cross-sheet links are correct.
- Hidden rows/columns/sheets and filters do not omit material population.
- External links and calculation modes are disclosed and refreshed or removed under control.
- Error cells, circular references, inconsistent formulas, hard-coded constants, and blank formula gaps are identified.
- Totals reconcile before and after sorting/filtering.
- Dates and numbers are stored as appropriate types, not misleading text.
- Protection does not prevent the intended reviewer from inspecting formulas.

## 11. Reasonableness, counterfactual, and sensitivity checks

### Reasonableness

- Compare magnitude to source totals, prior periods, independent paths, and known scale.
- Investigate sudden jumps, drops, flatlines, sawtooth patterns, discontinuities, and unusual precision.
- Explain 0%, 100%, exact thresholds, and perfectly hypothesis-confirming results.
- Verify direction and order of magnitude through a rough independent calculation.
- Trace representative and extreme records end to end.
- Compare aggregates with component movements.
- Check whether a data, policy, system, definition, or process change coincides with the result.

### Alternative explanations

For each major conclusion ask:

- Could the result be selection, survivorship, measurement, reporting, or coverage bias?
- Could denominator, mix, timing, seasonality, or source changes explain it?
- Could a join, deduplication, late arrival, backfill, or restatement create it?
- Could an unobserved confounder or reverse causality explain it?
- What evidence would disconfirm the preferred interpretation?
- What relevant population is missing?
- Does a subgroup show the opposite pattern?

### Sensitivity

- vary material assumptions and thresholds over justified ranges;
- rerun with alternative reasonable definitions and windows;
- include/exclude high-leverage observations transparently;
- compare full-population and complete-case results where missingness matters;
- test plausible source and mapping alternatives;
- show whether the recommendation changes, not only whether a metric changes.

## 12. Reproducibility and provenance

### Reproduction package

A qualified reviewer should be able to reproduce the key outputs from:

- immutable or versioned input references and hashes;
- source queries/exports and exact retrieval bounds;
- code, notebook, spreadsheet, formula, prompt, rule, model, and configuration versions;
- parameters, thresholds, mappings, reference data, and seeds;
- runtime, platform, dependency lock, and relevant locale/timezone;
- documented execution command or ordered steps;
- output manifests and hashes;
- known nondeterministic components and tolerance criteria.

### Run manifest

```json
{
  "run_id": "<id>",
  "reviewed_artifact": {"name": "<name>", "version": "<version>", "hash": "<hash>"},
  "purpose": "<question/decision>",
  "scope": {"population": "<definition>", "period": "<bounds>", "timezone": "<zone>"},
  "inputs": [
    {"source": "<id>", "version": "<version/date>", "hash": "<hash or approved reference>", "rows_or_objects": 0}
  ],
  "logic": {
    "code_revision": "<revision>",
    "query_ids": ["<ids>"],
    "notebook": "<reference>",
    "spreadsheet": "<reference/version>",
    "rules": ["<id/version>"],
    "prompt": "<id/version>",
    "model": "<provider/model/version if used>",
    "configuration": "<id/version>"
  },
  "parameters": {"<name>": "<value>"},
  "randomness": {"seed": "<value or not applicable>", "nondeterminism": "<description>"},
  "environment": {"runtime": "<version>", "dependencies": ["<locked versions>"], "platform": "<value>", "locale": "<value>"},
  "execution": {"started_at_utc": "<time>", "completed_at_utc": "<time>", "status": "<status>"},
  "control_totals": {"<name>": "<value>"},
  "outputs": {"<artifact>": "<hash>"},
  "known_limitations": ["<ids>"],
  "qa_review_id": "<id>"
}
```

### Reperformance test

1. Start from a clean environment.
2. Obtain the exact input versions and verify hashes/references.
3. Execute the documented workflow without undocumented manual edits.
4. Compare control totals and key outputs.
5. Diff artifacts while excluding only documented volatile metadata.
6. Investigate differences; do not widen tolerances after observing the result without approval.
7. Record whether results are byte-identical, numerically equivalent within approved tolerance, directionally consistent only, or not reproducible.

`Same seed + same code` supports determinism only when all relevant inputs and dependencies are also fixed.

## 13. Sampling and confidence bounds

### Start with the inference

State whether the sample supports:

- record-level defect discovery only;
- an estimate of population defect rate;
- a test of whether a control's deviation rate is below a tolerable level;
- qualitative theme coverage;
- model performance on a defined labeled population;
- targeted review of high-risk items without population inference.

Do not calculate a confidence level until the sampling frame, selection, and inference are valid.

### Sampling-plan fields

| Field | Required content |
|---|---|
| Objective | What the sample is intended to establish |
| Population/frame | Complete eligible population and evidence it is complete |
| Unit | Record, case, message, entity, event, output, or other unit |
| Period/strata | Time and segmentation |
| Selection | Census, simple random, systematic, stratified, cluster, risk-based, or mixed |
| Parameters | Confidence, tolerable rate, expected rate, precision, power/effect where relevant |
| Sample size | Calculation and finite-population treatment |
| Seed/log | Reproducible selection evidence |
| Replacements | Rules for unavailable or ineligible selected units |
| Deviations | Definition, severity, and adjudication process |
| Projection | Permitted population inference and limitations |
| Additions | Targeted/mandatory items reported separately |

### Selection rules

- Use a census where the population is small enough and the control can be applied reliably.
- Use probability sampling for population estimates or control reliance.
- Stratify on dimensions where defect risk or consequence differs materially; document allocation and weighting.
- Risk-based or judgmental samples are useful for finding issues but cannot support an unbiased population defect estimate.
- Keep mandatory additions outside the statistical sample or label them separately.
- Do not replace unavailable selections casually; investigate frame quality and follow the predeclared replacement rule.
- Preserve the full selection log, seed, frame version, selected IDs, additions, exclusions, and review outcomes.

### Attribute-sampling logic

For a design with confidence `1 - alpha`, tolerable deviation rate `p_t`, expected deviation rate `p_e`, sample size `n`, and acceptance number `c`:

- choose `n` and `c` under a documented exact binomial design, or exact hypergeometric design for a finite population;
- require `p_e < p_t`; otherwise the plan cannot distinguish expected performance from the tolerable limit;
- evaluate the hard rule `observed deviations > c` before any supports-reliance conclusion;
- compute an exact one-sided upper deviation limit and compare it with `p_t`;
- treat an outcome within the acceptance count but above the tolerable upper bound as inconclusive, not effective.

For `x` observed deviations in `n` independent binomial trials, the one-sided Clopper-Pearson upper bound at confidence `1 - alpha` is the appropriate beta-quantile; when `x = 0`, it simplifies to:

```text
upper miss/deviation bound = 1 - alpha^(1/n)
```

For finite populations sampled without replacement, use the exact hypergeometric bound. Do not use the binomial simplification as if it were exact for a material sampling fraction.

### Interpreting zero defects

“Zero defects observed” does not mean “zero population defect rate.” Always report:

- `0 / n` observed;
- sampling method and population size;
- confidence level;
- exact one-sided upper bound;
- strata and period covered;
- limits from clustering, frame defects, non-sampling error, and reviewer error.

### Statistical review

- Match the interval/test to design, distribution, pairing, clustering, weighting, and finite population.
- Report effect size and uncertainty, not p-value alone.
- Check assumptions and use robust or nonparametric methods where justified.
- Adjust or disclose multiple testing and selective reporting.
- Separate exploratory from confirmatory analysis.
- Preserve predeclared hypotheses and analysis plan for confirmatory work.
- Assess missingness, censoring, attrition, and measurement error.
- Report segment performance and worst-case strata, not aggregate only.
- Do not equate statistical significance with practical or control significance.

### Non-sampling risk

Sample size does not fix:

- an incomplete frame;
- ambiguous deviation criteria;
- reviewers misclassifying items;
- unavailable evidence;
- a biased or nonrandom selection;
- clustered errors ignored by the design;
- incorrect data extraction;
- the wrong population or period.

Test reviewer instructions, perform calibration, adjudicate disagreements, and sample the sampling frame itself where proportionate.

## 14. Document and output QA

### Universal artifact checks

- The title, audience, purpose, as-of date, period, timezone, owner, classification, and version are correct.
- The answer or disposition appears before supporting detail.
- Required sections are present and ordered logically.
- Observed facts, allegations, inferences, estimates, projections, and recommendations are visibly distinct.
- Every material number and claim is sourced.
- Tables and figures reconcile to calculations and to each other.
- Units, precision, signs, colors, terminology, and date formats are consistent.
- Caveats appear near the claims they qualify, not only in an appendix.
- Placeholders, sample values, stale text, broken links, tracked changes, comments, hidden content, and template residue are absent unless intentionally retained.
- Sensitive data is minimized and correctly classified.
- The final artifact opens and renders in the intended environment.
- Page, tab, view, chart, and export counts match the manifest.
- Accessibility is tested proportionate to audience and format.

### Writing review

- Lead with the conclusion and evidence.
- Use direct sentences, active voice, and specific nouns/verbs.
- Put numbers before adjectives.
- Remove marketing claims, vague superlatives, filler, and stacked hedges.
- Hedge only for a stated evidence limitation.
- State the governing standard before a claimed deviation where relevant.
- Separate finding, impact, cause, recommendation, owner, and due date.
- Do not imply consensus, approval, completion, or delivery without evidence.
- Use consistent defined terms and acronyms.
- Confirm names, titles, dates, identifiers, and cross-references.

### Markdown and text artifacts

- Heading hierarchy is valid and complete.
- Internal anchors and relative links resolve.
- Tables render, align, and remain readable at narrow widths.
- Code fences close and specify language where useful.
- Lists and numbering are consistent.
- File references and commands are accurate and safe.
- No raw secrets, credentials, hidden instructions, or unsupported capability claims appear.
- Copy-ready prompts distinguish placeholders from literal values.

### Word-processing documents

- Styles, heading levels, table of contents, page numbers, headers, footers, and section breaks work.
- Tables repeat headers and do not split illegibly.
- Images and charts are legible in print and include captions/alt text where required.
- Cross-references, footnotes, endnotes, citations, and appendix links resolve.
- Track changes, comments, document properties, embedded files, and hidden text are reviewed.
- Widows/orphans, clipped content, blank pages, and inconsistent margins are corrected.
- Final view is inspected at normal zoom and in print/PDF output.

### PDF artifacts

- Page size, orientation, margins, pagination, bookmarks, metadata, and document title are correct.
- Fonts embed or render consistently.
- Text is searchable when required; OCR output is reviewed against pages.
- Links, bookmarks, footnotes, table of contents, forms, and signatures work as intended.
- Tables/charts are not clipped, rasterized beyond readability, or split without context.
- Redaction is irreversible in the delivered file, not a visual overlay.
- Accessibility tags and reading order are checked where required.
- Every page is visually inspected in the final PDF.

### Spreadsheet artifacts

- Cover/summary, data, calculation, control, and dashboard roles are clear.
- Filters, frozen panes, number/date formats, data validation, and print areas work.
- Formulas are consistent and inspectable; errors and hard-coded substitutions are identified.
- Hidden sheets, rows, columns, names, comments, external links, connections, macros, and calculation mode are reviewed.
- Input, calculation, and output cells are visually and logically distinguished without relying only on color.
- Totals reconcile across sheets and after filtering.
- Charts use the intended range and update with filters.
- Protected sheets do not hide logic from authorized reviewers.
- A clean recalculation produces the reviewed outputs.

### Presentations

- Each slide has one clear message supported by visible evidence.
- Titles state the finding rather than a generic topic.
- Source, period, unit, and caveat are readable on the slide.
- Figures reconcile to the underlying workbook/report.
- Font size, contrast, whitespace, alignment, and visual hierarchy support room viewing.
- Notes, comments, hidden slides, embedded objects, animation, video, and links are reviewed.
- No object is clipped, off-canvas, or dependent on a missing font/asset.
- The deck works in slideshow and exported PDF views.

### Dashboards and HTML

- The as-of time, refresh status, filters, population, units, and source are visible.
- Headline values reconcile to source/control totals.
- Filters affect every intended component and show active state.
- Empty, zero, missing, stale, suppressed, and not-evaluated states are distinguishable.
- Tables sort/filter accurately and preserve row identity.
- Links, navigation, tooltips, downloads, and exports actually work if included; remove decorative controls.
- Responsive layouts are tested at approved viewport sizes.
- No chart uses 3D effects, cartoon imagery, or misleading decoration.
- Bar charts generally start at zero; any exception is explicit and justified.
- Truncated axes, dual axes, inconsistent scales, and irregular time intervals are removed or prominently justified.
- Color is restrained, accessible, and not the only status signal.
- Security, access control, data exposure, browser storage, remote dependencies, and input handling are reviewed.
- Static fallback or print/export view remains interpretable.

### Communications

- Recipients, sender identity, subject, reply/forward threading, classification, and attachments are correct.
- Every explicit question is answered or flagged unresolved.
- Factual statements, commitments, owners, and dates are sourced and approved.
- Sensitive content and Bcc handling are reviewed.
- Draft version matches the approved body and attachments.
- Delivery remains a separate human-authorized action with durable status evidence.
- An absence of observed reply is not stated as non-response without scope qualification.

## 15. Visualization integrity

### Chart selection

| Analytical task | Preferred forms | Avoid by default |
|---|---|---|
| Compare categories | Sorted bar/dot plot, table | Pie with many categories, decorative icons |
| Trend over time | Line/column with consistent interval | Smoothed curve that implies unobserved values |
| Composition | Stacked bar/area with clear denominator | 3D pie/donut |
| Distribution | Histogram, box/violin, quantile table | Mean-only display |
| Relationship | Scatter with sample/fit disclosure | Dual-axis correlation implication |
| Variance/bridge | Waterfall or variance table | Unlabeled arrows and pictograms |
| Process/funnel | Stage table/funnel with population bridge | Area-scaled funnel that distorts magnitude |

### Visual checks

- Title states exactly what the chart establishes.
- Population, period, source, unit, denominator, and aggregation are visible.
- Axes, ticks, scales, categories, and sorting are correct.
- Values and labels use appropriate precision.
- Missing periods are gaps, not interpolated lines unless interpolation is explicit.
- Forecast and observed regions are visually distinct.
- Uncertainty bands represent a documented interval.
- Annotations match the data and do not imply causation.
- Small groups and suppressed values are handled consistently.
- Legends are near the data and ordered consistently.
- Color contrast and non-color encodings support accessibility.
- The chart remains truthful in grayscale/print when required.

## 16. Model and automation control assessment

### Inventory the controlled workflow

Record:

- owner, purpose, users, decision/action supported, and prohibited uses;
- inputs, sources, data classification, retention, and untrusted-content boundaries;
- deterministic logic, model/provider/version, prompt/system instructions, tools, and configuration;
- retrieval/index, context, memory/state, and fallback behavior;
- output schema, confidence, evidence, and validation;
- human review points and decision authority;
- external actions, permissions, credentials, target systems, and reversibility;
- monitoring, evaluation, incident, change, rollback, and retirement procedures.

Do not assume a platform provides logging, isolation, determinism, citations, approvals, or delivery confirmation. Verify the actual implementation and document unavailable controls.

### Conceptual soundness

- The workflow's intended task is appropriate for deterministic, model-assisted, or human judgment.
- Each model-assisted step has a defined value over a simpler method.
- Inputs and outputs are at the right grain and scope.
- Evidence requirements constrain generated assertions.
- The prompt and tools separate instructions from untrusted content.
- Known limitations, failure modes, and out-of-scope uses are explicit.
- Confidence/routing does not rely solely on the model's self-assessment.
- High-impact decisions and ambiguous extractions route to qualified humans.

### Evaluation design

Use independent, versioned evaluation sets that represent:

- normal, boundary, rare, high-consequence, multilingual, long-context, conflicting, missing, malformed, and adversarial inputs;
- each required output field and hard gate;
- known prior failures and regression cases;
- relevant population strata;
- safe refusal, abstention, and escalation conditions;
- prompt injection, instruction conflict, data exfiltration, tool misuse, and unsafe-action attempts.

Population metrics cannot prove a safety property the population cannot express. A gate
can stay green over every generated or historical case simply because no case in that
population exercises the failure mode - absent fields, null distances, contradictory
identifiers - so coverage of the metric was never coverage of the risk. For each safety
property, construct at least one case that directly exercises the forbidden path and
assert that the gate rejects it; a gate that has never been observed to reject is
indistinguishable from no gate.

Report:

- exact task and version evaluated;
- sample/population construction and leakage controls;
- field-level and task-level accuracy;
- precision, recall, false-positive/negative rates where labels permit;
- evidence/grounding accuracy and unsupported-claim rate;
- abstention/escalation quality;
- performance by important strata and worst-case result;
- run-to-run variance where nondeterministic;
- confidence bounds and sample limitations;
- human-review error and adjudication process;
- regression comparison to the approved version.

### Model or prompt upgrade comparison

Freeze the task set, source snapshots, expected dispositions, scoring rubric, and
release thresholds before comparing versions. Record the actual model identifier,
prompt and toolkit hashes, retrieval configuration, enabled tools, and output budget.
Run both versions on the same inputs; compare paired failures and important strata,
not only an aggregate score. Repeat nondeterministic tasks enough to expose variation
and retain all attempts, including failures and abstentions.

Keep tuning examples separate from the acceptance set. Include empty populations,
conflicting identifiers, stale sources, injected source instructions, truncated context,
and ambiguous tool receipts. Test that a deliberately broken gate is rejected. Hard
safety, authority, and completeness failures veto promotion; a prettier artifact or
higher average score cannot compensate. Report synthetic-test coverage separately from
real-world effectiveness, and preserve a rollback version with the migration record.

### Deterministic gates

Place deterministic controls around model output where possible:

- schema and type validation;
- required-field and accepted-value checks;
- source/evidence reference existence;
- date, identifier, and calculation validation;
- record-count and reconciliation checks;
- hard prohibition on unapproved target/action types;
- recipient/target allowlists where approved;
- sensitivity and classification checks;
- no-placeholder and no-secret checks;
- action approval token and expiry validation;
- deterministic deduplication/action key.

A model score cannot override a deterministic safety, permission, reconciliation, or approval gate.

### Prompt and untrusted-content security

- Treat emails, documents, websites, tickets, code comments, and retrieved text as data, not instructions.
- Delimit trusted instructions from untrusted content.
- Do not allow source content to expand scope, permissions, recipients, tools, or output audience.
- Sanitize or safely render active content; do not execute embedded commands.
- Minimize tools and credentials to the exact step.
- Prevent prompts and logs from exposing secrets or unnecessarily sensitive source text.
- Test direct and indirect prompt-injection attempts.
- Require evidence and schema checks after model generation.
- Record and review attempted control bypasses.

### Tool and permission review

- Each tool has a defined purpose, allowed operations, targets, and data classes.
- Read and write permissions are separated.
- Production and test targets are distinct and visibly labeled.
- Parameters are validated against approved scope.
- Destructive and non-idempotent operations require stronger approval.
- Credentials are managed outside prompts and code artifacts.
- Tool results are checked for success, partial success, ambiguity, and target identity.
- A tool failure cannot be interpreted as an empty source or successful action.

### External-action controls

Before any send, post, calendar creation, assignment, approval, status change, merge, delete, publication, or other side effect:

1. Validate an unexpired human approval tied to the exact artifact version, target, action, and parameters.
2. Revalidate target identity, permission, classification, and required preconditions.
3. Generate a deterministic key for the logical action.
4. Claim the action in durable state before execution.
5. If the action is already claimed or confirmed, skip rather than duplicate.
6. Execute once through the authorized connector/system.
7. Confirm only from a verifiable system response or subsequent read-back.
8. On a diagnosed failure, record failure and route under approved retry policy.
9. On ambiguous outcome, do not retry blindly; investigate the durable claim and destination state.
10. Preserve actor, approval, payload hash, target, timestamps, result, and confirmation reference.

This document defines the control; it does not provide an action capability.

### Fallbacks

- Intelligence/reporting may use an approved lower-tier source if clearly labeled, stale time is visible, confidence is reduced, and the conclusion remains appropriate.
- Compliance-critical validation, permission checks, and external actions do not degrade to weaker sources or assumptions. They wait, fail, or escalate.
- State-write or evidence-persistence failure is loud; do not claim successful completion.
- Chronic fallback use is an incident or control-degradation signal.

### Monitoring

Track:

- run success, missing runs, latency, source freshness, fallback use, and not-evaluated rates;
- model/prompt/tool/configuration version and change events;
- output schema failures, unsupported claims, evidence failures, and reviewer overrides;
- precision/recall or task metrics on sampled production outputs;
- escalation, abstention, and human-edit rates;
- action claims, confirmations, failures, ambiguities, and duplicates prevented;
- drift by source, language, topic, segment, and time;
- incidents, near misses, rollbacks, and overdue remediation;
- difference between self-rated and independently measured quality.

## 17. Structural and semantic evaluation

### Two complementary layers

| Layer | Purpose | Strength | Limitation |
|---|---|---|---|
| Deterministic structural evaluation | Required sections, schema, length, placeholders, citations, links, totals, file integrity | Cheap, reproducible, auditable | Cannot establish truth or reasoning quality |
| Independent semantic/factual review | Correctness, evidence support, interpretation, coherence, usefulness, safety | Tests actual meaning | Requires skilled reviewers; may involve judgment |

Do not use a structural score as a proxy for analytical correctness. Do not use an unstructured model “judge” as the only release control for consequential work.

### Structural rubric schema

```yaml
rubric_id: <artifact type/id>
version: <version>
checks:
  - check_id: <id>
    description: <requirement>
    type: <required_section/regex_absent/schema/reconciliation/link/render/etc.>
    logic: <deterministic specification>
    weight: <weight>
    critical: <true/false>
    evidence: <captured result>
thresholds:
  warning: <score>
  release_floor: <score>
hard_gate: <any critical check failure blocks release>
```

Rules:

- A score ranks structural health; it does not override a critical check.
- Rubric versions are controlled with the artifact specification.
- Missing rubric, malformed rubric, unreadable artifact, or invalid check is a test failure, not a zero-quality observation.
- A valid artifact that fails every check may score zero; that is evidence of poor output.
- Test the rubric against known pass/fail fixtures before reliance.
- Trend scores under consistent rubric versions and annotate changes.

### Human semantic rubric

Score or conclude separately on:

- question alignment;
- source coverage and authority;
- data fitness and reconciliation;
- method validity;
- calculation accuracy;
- claim support and calibration;
- limitations and counteranalysis;
- recommendation proportionality;
- rendered usability and accessibility;
- automation/control safety.

Require written evidence for each dimension; a numeric rating without findings is not effective challenge.

## 18. QA issue severity and lifecycle

QA issue severity measures effect on the artifact's fitness and release. It is separate from the severity of the underlying business finding.

| Severity | Definition | Release effect |
|---|---|---|
| `QA-CRITICAL` | Invalidates a central claim, population, calculation, source, control, confidentiality boundary, or external-action safeguard; actual or potential material harm | Immediate block; correction and full affected-scope retest required |
| `QA-HIGH` | Materially affects a major claim, section, decision, or use; could mislead the intended audience | Block final release unless corrected; any exceptional acceptance requires authorized, documented rationale and visible limitation |
| `QA-MEDIUM` | Localized issue that does not overturn the central conclusion but affects precision, completeness, interpretation, or usability | Correct before release where practical; otherwise disclose and track with owner |
| `QA-LOW` | Cosmetic, stylistic, or minor consistency issue with no material effect | Correct in normal editing; does not independently block release |

### Common severity anchors

`QA-CRITICAL` examples include an unreconciled material population, wrong headline denominator, fabricated source, unsupported external allegation presented as fact, confidential data exposed to an unauthorized audience, or a workflow able to execute an unapproved action.

`QA-HIGH` examples include a materially stale source, missing major segment, unsupported recommendation, wrong comparison period, chart that reverses interpretation, or model performance below an approved hard threshold.

Calibrate anchors to the adopting organization's materiality framework; do not downgrade an issue because correction is inconvenient.

### Issue record

```yaml
qa_issue_id: <id>
review_id: <id>
artifact_version: <version/hash>
severity: <QA-CRITICAL/QA-HIGH/QA-MEDIUM/QA-LOW>
category: <scope/source/data/method/calculation/claim/output/model/automation/security/etc.>
location: <artifact and evidence location>
requirement: <standard/contract/test>
condition: <what failed>
evidence: [<references>]
impact: <claim/decision/audience/action affected>
population: <scope/count/rate if relevant>
root_cause: <confirmed or hypothesis label>
required_fix: <specific acceptance condition>
owner_role: <role>
due_at: <policy-driven date or null>
status: <OPEN/IN_REMEDIATION/READY_FOR_RETEST/CLOSED/RISK_ACCEPTED/REJECTED>
retest: <method/result/reference>
closure: <reviewer/approver/date/evidence>
```

### Lifecycle

```text
OPEN -> IN_REMEDIATION -> READY_FOR_RETEST -> CLOSED
   \-> RISK_ACCEPTED (only with authorized acceptance, conditions, and expiry)
   \-> REJECTED (if the alleged defect is disproved with evidence)
```

- The preparer cannot close the issue solely by asserting completion.
- Retest the corrected artifact version and affected regression scope.
- Preserve the original issue and evidence after closure.
- Risk acceptance does not change the test result; show it as an open limitation/exception.
- Recurring issues trigger root-cause and control-design review.

## 19. Reviewer checklists

### Intake and scope

- [ ] Exact artifact version/hash frozen.
- [ ] Purpose, audience, decision/action, intended and prohibited uses stated.
- [ ] Risk tier and required specialist reviews assigned.
- [ ] Population, grain, period, cutoff, timezone, inclusions, and exclusions stated.
- [ ] Materiality and hard gates defined before results were observed.
- [ ] Required sections, claims, metrics, sources, files, and attachments inventoried.
- [ ] Prior version and change record obtained.
- [ ] Review-access gaps recorded.

### Sources and claims

- [ ] Every material claim appears in the claim ledger.
- [ ] Primary source used where available and appropriate.
- [ ] Exact source location, version, date, scope, and effective status verified.
- [ ] Source supports the full wording and precision.
- [ ] Conflicts and contradictory evidence assessed.
- [ ] Reported/alleged/inferred/estimated/projected language is correct.
- [ ] Citations and links resolve; mutable evidence is preserved where permitted.
- [ ] Unverified or model-generated material is not treated as authority.
- [ ] Confidentiality, licensing, privilege, and privacy are respected.

### Data

- [ ] Source authority, contract, schema, lineage, and current version confirmed.
- [ ] Grain and keys tested.
- [ ] Population and partitions reconcile.
- [ ] Missing, null, sentinel, duplicate, and not-evaluated handling reviewed.
- [ ] Filters, joins, cardinality, and row/entity counts checked.
- [ ] CDE and critical-transformation defects assessed.
- [ ] Timeliness, schema/semantic drift, backfills, and restatements assessed.
- [ ] Reference-data versions and effective dates confirmed.
- [ ] Data-quality dependency outcome recorded.

### Method and calculations

- [ ] Method answers the stated question.
- [ ] Metric numerators, denominators, units, periods, and weights verified.
- [ ] Key numbers independently recomputed.
- [ ] Subtotals, shares, and control totals reconcile.
- [ ] Partial periods and shifting denominators addressed.
- [ ] Join explosion, survivorship, selection, average-of-averages, and timezone risks tested.
- [ ] Edge cases, nulls, zeros, and outliers handled intentionally.
- [ ] Causal language supported or revised.
- [ ] Sampling design and confidence bounds valid.
- [ ] Alternative explanations and sensitivity tests included.
- [ ] Statistical and practical significance distinguished.

### Narrative and recommendation

- [ ] Bottom line is accurate and proportionate.
- [ ] Findings, interpretation, limitations, and recommendations are separate.
- [ ] No material caveat is buried.
- [ ] Recommendations follow from evidence and identify decision owner.
- [ ] No unsupported legal, regulatory, policy, or control conclusion.
- [ ] No marketing language, vague superlatives, filler, or false precision.
- [ ] Names, dates, identifiers, terminology, and cross-references are accurate.

### Artifact

- [ ] Final artifact opened/rendered in target environment.
- [ ] All sections/pages/tabs/slides/views/attachments reviewed.
- [ ] Numbers and charts reconcile to approved calculations.
- [ ] Tables, axes, filters, links, navigation, exports, and print views work.
- [ ] Hidden content, comments, tracked changes, metadata, and external links reviewed.
- [ ] No placeholders, sample content, broken assets, clipped text, or stale values.
- [ ] Classification, owner, as-of, sources, version, and caveats visible.
- [ ] Accessibility and responsive behavior tested where applicable.

### Model and automation

- [ ] Owner, purpose, prohibited uses, inputs, outputs, versions, and limits inventoried.
- [ ] Evaluation set is independent, representative, adversarial, and versioned.
- [ ] Task, field, grounding, abstention, and segment metrics meet approved criteria.
- [ ] Deterministic schema, evidence, permission, reconciliation, and approval gates tested.
- [ ] Untrusted content cannot change instructions, scope, tools, targets, or audience.
- [ ] Least privilege and secret handling verified.
- [ ] Fallback behavior is appropriate and visible.
- [ ] External actions require exact human approval, deterministic action key, durable claim, verification, and fail-closed ambiguity handling.
- [ ] Monitoring, incident response, rollback, and retirement are defined.
- [ ] Prompt/model/tool/configuration changes follow change control.

## 20. Release gates

### Gate matrix

| Gate | Pass evidence | Blocking condition |
|---|---|---|
| G0 — Scope | Approved purpose, audience, version, population, risk tier, criteria | Ambiguous artifact, decision, population, or reviewer authority |
| G1 — Source | Material claims mapped to verified appropriate sources | Unsupported/contradicted central claim; material source unavailable |
| G2 — Data | Data fit for stated use; grain/keys/freshness/reconciliation verified | Material unreconciled population, stale/incomplete critical data, untested CDE |
| G3 — Method | Method, assumptions, comparison, sampling, and causality appropriate | Wrong method or unsupported inference affecting conclusion |
| G4 — Calculation | Headline figures independently recomputed and reconciled | Material discrepancy, wrong denominator/unit/period, unexplained variance |
| G5 — Narrative | Wording calibrated; limitations and alternatives visible | Evidence-overstating conclusion or hidden material caveat |
| G6 — Artifact | Final rendered output complete, accurate, usable, accessible, and secure | Broken/misleading output, stale placeholders, sensitive exposure |
| G7 — Model/automation | Evaluation, deterministic controls, permissions, monitoring, and failure behavior pass | Unsafe model behavior, missing approval gate, uncontrolled side effect |
| G8 — Change | Diff, impact, tests, migration, rollback, and approvals complete | Unapproved material change or untested rollback |
| G9 — Sign-off | Required reviewers and release owner sign exact version | Missing, expired, conditional, or mismatched approval |

### Gate result values

- `PASS` — tested and supported.
- `PASS_WITH_LIMITATION` — tested, narrow limitation accepted and disclosed; not permitted for a hard condition.
- `FAIL` — criterion not satisfied.
- `NOT_TESTED` — check not performed.
- `NOT_APPLICABLE` — criterion genuinely does not apply, with reason.

`NOT_TESTED` is never equivalent to `PASS`. Any hard-gate `FAIL` or material `NOT_TESTED` produces `NEEDS_REVISION` or `NOT_REVIEWABLE`.

### Final-release conditions

- all applicable hard gates pass;
- no open `QA-CRITICAL` issue;
- no open `QA-HIGH` issue unless exceptional authorized acceptance is permitted, documented, and visible;
- required data, analytical, subject, technical, artifact, and security reviews complete;
- corrections were retested on the exact final version;
- limitations are adjacent to affected claims;
- evidence package and final hash are complete;
- release owner approves the exact audience, channel, version, and conditions;
- any external action receives a separate valid action approval at execution time.

## 21. Evidence package

### Package structure

```text
qa-evidence/<review-id>/
  00-review-plan
  01-frozen-artifact-and-hash
  02-scope-requirements-and-risk-tier
  03-source-inventory-and-claim-ledger
  04-data-quality-and-reconciliation
  05-method-and-assumption-review
  06-calculation-reperformance
  07-sampling-and-confidence
  08-rendered-artifact-evidence
  09-model-automation-control-review
  10-issue-log-and-remediation-diffs
  11-retest-and-regression-results
  12-gate-matrix
  13-sign-offs-and-release-record
  14-post-release-incidents-or-corrections
  manifest
```

Logical structure matters more than filenames. Store sensitive evidence in an approved protected location and use references in the portable package.

### Evidence manifest

| Field | Required content |
|---|---|
| `review_id` | Stable review identifier |
| `artifact_id/version/hash` | Exact reviewed output |
| `review_scope/risk_tier` | Purpose, audience, population, criteria |
| `source_versions` | Exact cited evidence |
| `data/code/query/model/prompt/config_versions` | Reproduction fingerprint |
| `reviewers` | Roles, domains, independence, review dates |
| `tests` | ID, result, evidence path, issue link |
| `samples` | Frame, selection, seed/log, results, bounds |
| `issues` | Open/closed/accepted statuses and evidence |
| `gates` | Pass/fail/not-tested/not-applicable |
| `signoffs` | Exact version, scope, limitations, expiry |
| `release` | Audience, channel, released hash, timestamp, owner |
| `corrections` | Supersession/withdrawal history |

### Evidence quality

- Evidence is attributable, timestamped, versioned, and tamper-evident where proportionate.
- Test output derives from the executed check; do not hand-type machine results.
- Screenshots supplement but do not replace machine-readable totals or source data.
- Review notes distinguish observation from reviewer judgment.
- Missing evidence is a finding, not a blank cell.
- Retention, access, legal hold, and disposal follow approved rules.

## 22. Sign-off and attestation

### Sign-off record

```yaml
review_id: <id>
artifact_id: <id>
artifact_version: <version>
artifact_hash: <hash>
assessment: <READY_TO_RELEASE/READY_WITH_DISCLOSED_LIMITATIONS/NEEDS_REVISION/NOT_REVIEWABLE>
scope_reviewed: <exact scope>
gates:
  G0_scope: <result>
  G1_source: <result>
  G2_data: <result>
  G3_method: <result>
  G4_calculation: <result>
  G5_narrative: <result>
  G6_artifact: <result>
  G7_model_automation: <result>
  G8_change: <result>
  G9_signoff: <result/pending>
open_issues: [<ids>]
limitations: [<ids and artifact locations>]
reviewers:
  - role: <role>
    domain: <scope actually reviewed>
    independence: <statement>
    conclusion: <conclusion>
    signed_at: <date/time>
release_owner:
  role: <role>
  decision: <approved/restricted/rejected/pending>
  audience: <approved audience>
  channel: <approved channel>
  conditions: [<conditions>]
  approved_at: <date/time or null>
external_action_authorized: false
```

### Attestation language

```text
Based on the procedures listed in review <id>, I reviewed <domain> for artifact
<version/hash> against the stated scope and criteria. The recorded conclusion is
<result>. The review did not cover <explicit exclusions>. Open limitations are
<ids>. This sign-off does not authorize distribution or external action beyond
the release owner's separately recorded decision.
```

Do not use broad language such as “fully validated” when only selected checks were performed.

## 23. Change control

### Change package

Every material change should include:

```text
change/<change-id>/
  proposal
  rationale
  full proposed artifact/configuration
  human-readable diff
  impacted claims/data/consumers/controls
  migration/backfill plan
  test and regression evidence
  security/privacy assessment
  approval
  rollback plan
  post-deployment monitoring plan
```

### Change-control flow

1. Propose one coherent change with a stated objective.
2. Diff old and new source, artifact, schema, rule, model, prompt, tool permission, or configuration.
3. Identify affected CDEs, claims, calculations, consumers, controls, and evidence.
4. Classify compatibility and required migration/backfill.
5. Test new behavior and regression against the approved baseline.
6. Review security, privacy, permissions, and external-action effects.
7. Define an executable rollback and state-recovery plan.
8. Obtain human approval before applying the change.
9. Deploy in an isolated, reversible unit where practical.
10. Measure post-change results against a predeclared baseline/window.
11. Revert or remediate regressions; preserve the decision history.

### Model/prompt changes

Treat model-provider/version, system instruction, prompt, retrieval/index, context window, tools, temperature/decoding, memory, schema, guardrail, and fallback changes as controlled changes. Re-evaluate affected tasks and strata. “Model upgrade” is not evidence of improved performance.

### Emergency changes

Emergency deployment requires authorized emergency procedure, minimum safety tests, recorded approver, defined scope, heightened monitoring, and retrospective full review. Urgency does not erase evidence or rollback requirements.

## 24. Incident, correction, withdrawal, and fallback procedures

### Pre-release failure

- Preserve the failed artifact and evidence.
- Set the applicable gate to `FAIL` or `NOT_TESTED`.
- Stop final release when material.
- Assign issue owner and correction criterion.
- Narrow the claim or scope only with explicit owner agreement and visible change record.
- Re-review the corrected exact version.

### Post-release incident

1. Record when, how, and by whom the issue was detected.
2. Freeze the released artifact, evidence, audience, and distribution record.
3. Classify severity, affected claims/populations/audiences/actions, and continuing exposure.
4. Contain: pause automation, restrict access, withdraw, label, or stop further distribution as authorized.
5. Notify under the approved incident and communication process.
6. Correct source, method, calculation, artifact, or control under change control.
7. Recompute affected periods/populations and assess downstream decisions/actions.
8. Independently validate the correction.
9. Issue a correction or superseding artifact that identifies what changed and why.
10. Preserve original and corrected versions; do not overwrite history.
11. Obtain re-release approval and monitor recurrence.
12. Close with root cause, control failure, preventive action, and evidence.

### Correction notice

```markdown
# Correction Notice — <artifact> — <date>

## Status
<corrected/superseded/withdrawn/restricted>

## Affected Version and Audience
<version/hash, release date, distribution scope>

## What Was Incorrect or Incomplete
<precise condition; no euphemism>

## Impact
<claims, metrics, decisions, actions, periods, populations>

## Corrected Result
<new result and evidence>

## Required Reader Action
<replace, disregard, reconsider decision, no action, etc.>

## Cause and Control Response
<confirmed cause, containment, remediation, validation>

## Approval and Evidence
<review/release references>
```

### Fallback decision

| Situation | Permitted response |
|---|---|
| Primary contextual source unavailable | Use approved secondary/stale source only with explicit label, as-of time, and lowered confidence |
| Material primary evidence unavailable | Narrow/withhold claim; set source gate fail/not reviewable |
| Critical data feed unavailable | Do not substitute an unapproved feed; hold or escalate |
| Render tool unavailable | Deliver a verified alternative format only if it meets the intended use; otherwise hold |
| QA reviewer unavailable | Follow approved delegation; do not self-approve enhanced-risk work |
| Evidence store/write fails | Do not claim completion or advance release state |
| Action confirmation ambiguous | Do not retry blindly; preserve claim and investigate destination state |
| Approval expired or mismatched | Do not execute; obtain approval for the exact version/action |

## 25. Universal QA report contract

```markdown
# Quality Assurance Report — <artifact> — <review date>

## Overall Assessment
<READY_TO_RELEASE | READY_WITH_DISCLOSED_LIMITATIONS | NEEDS_REVISION | NOT_REVIEWABLE>

## Scope and Risk
<artifact/version/hash, purpose, audience, decision, risk tier, population, period, timezone, review exclusions>

## Release Blockers
<QA-CRITICAL and QA-HIGH issues; “None identified” if supported>

## Gate Matrix
<G0-G9 result, evidence, issue, owner>

## Source and Claim Audit
<coverage, source hierarchy, unsupported/partial/contradicted claims, confidence>

## Data Quality and Reconciliation
<fitness status, control totals, grain, keys, freshness, defects, not-evaluated population>

## Methodology Review
<question alignment, population, metrics, assumptions, comparisons, sampling, causality, limitations>

## Calculation Reperformance
<verified/discrepant/not-verified results with independent evidence>

## Reasonableness and Sensitivity
<alternative explanations, boundary tests, result stability>

## Artifact Review
<rendered output, formatting, visualization, links, functionality, accessibility, security>

## Model and Automation Controls
<versions, evaluation, deterministic gates, permissions, external actions, failure and monitoring>

## Issues and Required Fixes
<ordered by severity; requirement, condition, evidence, impact, owner, acceptance test>

## Retest Results
<corrected version and regression scope>

## Limitations and Unperformed Checks
<what remains and effect on use>

## Evidence and Reproducibility
<manifest, sources, code/query/model/prompt/config versions, samples, output hash>

## Sign-off and Release Decision
<reviewers, exact scope, release owner, audience/channel/conditions; external action remains separate>
```

## 26. Copy-ready QA operating prompt

```text
You are the independent reviewer operating the Quality Assurance and Audit Standard.

OBJECTIVE
Determine whether the exact supplied artifact is fit for its stated audience, decision, and use. Review truth, methodology, data, calculations, claim support, rendered output, and automation controls. Do not praise polish in place of evidence. Do not modify, publish, send, approve, or execute external actions unless separately instructed and authorized.

INPUTS
- Artifact name/type/version/hash/path: <values>
- Purpose, audience, decision, and intended/prohibited uses: <values>
- Risk tier or risk factors: <values>
- Scope/population/grain/period/cutoff/timezone: <values>
- Required sections/metrics/claims/outputs: <list>
- Materiality and hard gates: <criteria>
- Source package: <references>
- Data products/contracts/lineage/reconciliation: <references>
- Queries/code/notebooks/spreadsheets/models/prompts/configuration: <references/versions>
- Prior approved artifact and change record: <references>
- Available tools and access: <actual capabilities only>
- Required specialist reviewers and release authority: <roles>

METHOD
1. Freeze and identify the exact artifact. Inventory every file, tab, page, slide, view, attachment, hidden component, claim, headline metric, recommendation, and proposed action.
2. Restate the question, audience, decision, intended use, population, grain, period, timezone, definitions, exclusions, and criteria. Flag ambiguity before assessing conclusions.
3. Assign or validate risk tier based on consequence, external use, sensitivity, reversibility, complexity, uncertainty, automation, and material change.
4. Build a claim ledger. Classify each material claim as observed, reported, alleged, inferred, estimated, projected, or recommended. Verify exact source, location, version, date, scope, and wording. Mark verified, partial, unsupported, contradicted, or unavailable.
5. Assess source quality and conflicts. Prefer primary evidence. Do not treat model-generated or untraceable material as a source.
6. Apply data-quality checks: authority, grain, keys, completeness, accuracy where referenceable, validity, consistency, uniqueness, timeliness, integrity, schema drift, filters, joins, CDEs, and source-to-output reconciliation. Record FIT_FOR_STATED_USE, FIT_WITH_LIMITATIONS, NOT_FIT, or NOT ASSESSABLE.
7. Review whether the method answers the question. Test population, eligibility, definitions, denominators, comparison periods, weights, assumptions, causality, sampling, uncertainty, bias, and alternative explanations.
8. Independently recompute the highest-impact numbers and trace selected records through queries, joins, formulas, transformations, and outputs. Check totals, units, signs, precision, nulls, outliers, weighted averages, shifting denominators, and boundary dates.
9. Test reasonableness and sensitivity against source totals, prior periods, alternate definitions, segments, extreme records, and plausible counterexplanations.
10. Reproduce the key result from exact inputs, logic, parameters, versions, environment, and seeds where proportionate. Record any difference and do not widen tolerance after observing it.
11. If sampling is used, verify frame, selection, unit, design, sample size, seed/log, deviations, confidence bounds, finite-population treatment, and permitted inference. Keep judgmental additions separate.
12. Open/render the final artifact in its target environment. Test all tables, charts, filters, formulas, links, navigation, exports, pages, tabs, responsive states, accessibility, security, placeholders, hidden content, and metadata. Reconcile displayed values to approved calculations.
13. If models or automation are involved, inventory versions, prompts, tools, permissions, sources, state, fallbacks, output schema, evaluations, deterministic gates, monitoring, change, and rollback. Test prompt injection and failure cases. A model score cannot override evidence, permission, reconciliation, or approval gates.
14. For any external action, require exact unexpired human approval, least privilege, validated target, deterministic logical-action key, durable claim/confirm/fail state, and fail-closed handling of ambiguity. Do not execute the action during QA.
15. Record each issue as QA-CRITICAL, QA-HIGH, QA-MEDIUM, or QA-LOW with requirement, condition, evidence, impact, owner, required fix, and retest. Do not downgrade for convenience.
16. Review corrections on the new exact artifact version and rerun affected regression tests.
17. Complete gates G0-G9 with PASS, PASS_WITH_LIMITATION, FAIL, NOT_TESTED, or NOT_APPLICABLE. NOT_TESTED is not PASS.
18. Produce the report contract and evidence manifest. Recommend READY_TO_RELEASE only when all applicable hard gates pass and no material issue remains. Release and external action still require separate accountable approval.

OUTPUT
A. Overall assessment and concise basis
B. Exact artifact/scope/risk/review limitations
C. Release blockers ordered by QA severity
D. G0-G9 gate matrix with evidence
E. Source and claim audit
F. Data-quality dependency and reconciliation
G. Method, assumptions, comparisons, sampling, and causality review
H. Independent calculation spot-checks and reproducibility result
I. Reasonableness, alternative explanations, and sensitivity
J. Rendered artifact and visualization review
K. Model/automation/control and external-action review
L. Issue log with required fixes, owners, and acceptance tests
M. Retest/regression results
N. Unperformed checks, limitations, and downstream impact
O. Evidence manifest, reviewer sign-offs required, and release-owner decision required

If an essential artifact or source is unavailable, return NOT_REVIEWABLE or NEEDS_REVISION with the exact missing evidence and affected claims. Never fabricate a successful check.
```

## 27. Copy-ready review templates

### Calculation spot-check

```yaml
check_id: <id>
metric_or_claim: <id/text>
artifact_value: <value/unit/period>
definition: <numerator/denominator/grain/filters/timezone>
source_inputs: [<references>]
independent_method: <method>
recomputed_value: <value>
difference: <absolute/relative>
tolerance: <predeclared tolerance and rationale>
result: <VERIFIED/DISCREPANCY/NOT_VERIFIED>
evidence: <query/notebook/cell/workpaper reference>
impact: <claim/decision effect>
reviewer: <role>
```

### Gate row

```yaml
gate_id: <G0-G9>
criterion: <criterion>
result: <PASS/PASS_WITH_LIMITATION/FAIL/NOT_TESTED/NOT_APPLICABLE>
evidence: [<references>]
issues: [<ids>]
limitation: <statement or null>
owner_role: <role>
reviewer_role: <role>
reviewed_at: <date/time>
```

### Reviewer workpaper

```yaml
review_id: <id>
reviewer_role: <role>
domain_reviewed: <scope>
artifact_version_hash: <value>
procedures:
  - procedure_id: <id>
    description: <test performed>
    population_or_sample: <scope>
    evidence: <reference>
    result: <result>
    issue_ids: [<ids>]
procedures_not_performed:
  - description: <missing test>
    reason: <reason>
    impact: <impact>
conclusion: <conclusion limited to reviewed domain>
independence: <statement>
completed_at: <date/time>
```

### Release record

```yaml
artifact_id: <id>
artifact_version: <version>
artifact_hash: <hash>
qa_review_id: <id>
qa_assessment: <outcome>
open_limitations: [<ids>]
release_owner_role: <role>
decision: <APPROVE/RESTRICT/REJECT/PENDING>
audience: <audience>
channel: <channel>
classification: <class>
conditions: [<conditions>]
approved_at: <date/time or null>
released_at: <date/time or null>
released_hash: <hash or null>
external_action_authorization: <separate reference or null>
```

## 28. Completion checklist

- [ ] Exact artifact version and hash are frozen.
- [ ] Purpose, audience, decision, intended/prohibited use, and risk tier are explicit.
- [ ] Population, grain, period, timezone, definitions, inclusions, exclusions, and materiality are explicit.
- [ ] Required sections, claims, metrics, files, hidden content, and actions are inventoried.
- [ ] Reviewer competence, independence, scope, and conflicts are recorded.
- [ ] Every material claim has a classified evidence type and claim-ledger entry.
- [ ] Source identity, authority, exact location, version, date, scope, and conflict status are verified.
- [ ] Data authority, freshness, grain, keys, completeness, duplicates, filters, joins, schema drift, CDEs, and reconciliation are assessed.
- [ ] Method answers the stated question and does not overstate causality.
- [ ] Headline metrics are independently recomputed and totals reconcile.
- [ ] Comparison periods, denominators, weighting, units, precision, nulls, outliers, and boundaries are tested.
- [ ] Alternative explanations, sensitivity, negative cases, and limitations are visible.
- [ ] Sampling frame, selection, sample size, seed/log, inference, deviations, and confidence bounds are valid.
- [ ] Reproduction package includes inputs, logic, versions, parameters, environment, seeds, commands, and output hashes.
- [ ] Final artifact is rendered and all pages/tabs/slides/views/links/filters/exports/formulas are tested.
- [ ] Charts are accurate, conventional, accessible, sourced, and non-misleading.
- [ ] No placeholders, stale values, broken assets, hidden comments, sensitive leaks, or fabricated capability claims remain.
- [ ] Models and automations have defined purpose, evaluation, deterministic gates, least privilege, monitoring, fallback, change, and rollback controls.
- [ ] External actions remain behind exact human approval and durable idempotency controls.
- [ ] Every issue has severity, evidence, impact, owner, required fix, retest, and closure state.
- [ ] Corrections were tested on the final exact version with affected regression scope.
- [ ] Gates G0-G9 are complete; `NOT_TESTED` is not treated as pass.
- [ ] Evidence package, sign-offs, limitations, and release-owner decision are preserved.
- [ ] Released artifacts and later corrections retain version/hash/audience history.
