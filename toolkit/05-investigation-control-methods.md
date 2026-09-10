# Investigation, Assessment, and Control Methods

Use this module to turn a signal into a documented disposition, risk assessment,
control conclusion, remediation plan, or governance decision. It defines method; it does
not authorize access, filing, customer action, employee action, or external communication.

Pair it with:

- [`00-operating-system.md`](00-operating-system.md) for authority and lifecycle;
- [`01-evidence-research-standard.md`](01-evidence-research-standard.md) and
  [`02-osint-source-register.md`](02-osint-source-register.md) for evidence;
- [`03-mailbox-communications.md`](03-mailbox-communications.md) for communication
  populations;
- [`04-intelligence-fincrime-frameworks.md`](04-intelligence-fincrime-frameworks.md) for
  typologies and risk lenses;
- [`06-data-quality-governance.md`](06-data-quality-governance.md) for data controls;
- [`07-output-templates.md`](07-output-templates.md) and
  [`09-quality-assurance.md`](09-quality-assurance.md) for release.

## 1. Decision rights and human gates

Assistants may organize evidence, calculate approved metrics, apply documented rules,
draft dispositions, identify gaps, compare alternatives, and recommend escalation. The
accountable role must approve any decision that can affect a person, customer,
transaction, market access, regulatory filing, employment matter, legal position, or
controlled record.

| Stage | Assistant may | Human or approved deterministic control must |
|---|---|---|
| Intake | validate fields, assign stable IDs, identify missing data | approve scope and access |
| Triage | apply documented priority rules, propose severity | decide urgent containment or statutory escalation |
| Investigation | organize, reconcile, calculate, research, test hypotheses | authorize sensitive collection and interviews |
| Decision support | draft rationale and alternatives | make regulated or consequential decision |
| Communication | prepare draft and distribution list | approve content, recipients, classification, and send |
| Closure | assemble evidence and test closure conditions | approve disposition, risk acceptance, or closure |
| Refresh | compare deltas and reopen candidates | approve changed decision where required |

Do not allow a model-generated confidence score to substitute for reviewer judgment.

## 2. Universal case lifecycle

### 2.1 Stages

1. **Receive:** capture signal, source, time, reporter, object, and original content.
2. **Validate:** confirm legibility, identity, required fields, duplicate/version status,
   and whether the item is in scope.
3. **Prioritize:** apply urgency, potential impact, legal/policy deadline, vulnerability,
   and evidence-preservation factors.
4. **Plan:** state hypotheses, evidence needed, search paths, approvals, and completion
   criteria before collecting broadly.
5. **Collect:** obtain authorized internal and external evidence with lineage.
6. **Reconcile:** prove population and numerical completeness; log inaccessible items.
7. **Analyze:** build chronology, relationships, baselines, calculations, and competing
   explanations.
8. **Conclude:** compare facts to criteria; state disposition, severity, confidence,
   rationale, residual uncertainty, and recommendation.
9. **Review:** scale review to severity: CRITICAL and HIGH items get independent review
   by someone outside the producing line before release, MEDIUM gets supervisory review,
   and LOW may release under the standing sample-based QA in module `09`.
10. **Act:** execute only authorized and approved actions with confirmation logging.
11. **Close:** verify all conditions, preserve the evidence package, set retention and
    review date.
12. **Learn:** capture outcome, false-positive/miss drivers, control gaps, and taxonomy
    or rule changes.

### 2.2 Case manifest

```yaml
case_id: CASE-<stable-id>
case_type: <controlled value>
source_record_ids: []
created_at: <ISO-8601>
as_of: <ISO-8601>
subject_ids: []
alert_or_issue_ids: []
decision_supported: <one sentence>
scope:
  included: []
  excluded: []
  period_start: <date>
  period_end: <date>
expected_populations: []
priority:
  severity: <tier>
  confidence: <rating>
  deadline: <timestamp or null>
  rationale: <text>
authority:
  owner: <role>
  reviewers: []
  restricted_material: []
hypotheses: []
evidence_requests: []
findings: []
decision:
  proposed: <value>
  approved: <value or null>
  approver: <role or null>
  decided_at: <timestamp or null>
actions: []
status: <controlled value>
```

## 3. Intake and triage

### 3.1 Minimum intake fields

| Field | Purpose |
|---|---|
| Source and source record ID | preserves origin and prevents silent duplication |
| Received and event timestamps | establishes SLA, sequence, and legal/policy time |
| Subject identifiers | supports correct identity and joins |
| Trigger or allegation | states why the item exists without adopting it as fact |
| Amount/exposure and currency/unit | supports materiality and reconciliation |
| Product, account, channel, jurisdiction | establishes applicable context |
| Evidence pointers | permits direct review of the triggering material |
| Prior/related records | prevents fragmented investigation |
| Immediate-risk flags | supports urgent preservation or escalation |
| Reporter/source restrictions | protects confidentiality and need-to-know |

### 3.2 Triage dimensions

Assess each independently:

- **potential impact:** financial, customer, legal, regulatory, market, operational,
  reputational, or safety;
- **immediacy:** active, ongoing, imminent, historic, or unknown;
- **evidence strength:** direct, corroborated, single source, ambiguous, or unavailable;
- **scope:** one event, related cluster, systemic population, or unknown;
- **control state:** contained, monitored, bypassed, failed, or unknown;
- **deadline:** statutory, contractual, policy, operational, or none;
- **vulnerability:** potential victim harm or exploitation requiring specialist handling;
- **preservation risk:** evidence or funds may disappear without prompt authorized action.

Route deterministically from these dimensions to a section 3.3 outcome: an active or
imminent immediacy flag, preservation risk, or vulnerability flag routes to `urgent
escalation`; systemic scope or a failed or bypassed control state routes to `systemic
review`; a statutory or contractual deadline pins the queue and the clock; among the
remainder, unavailable evidence becomes an `information request` and the rest a
`standard investigation`. Document every override with the overriding fact.

### 3.3 Triage outcome

Every intake ends in one of these mutually exclusive states:

`duplicate/superseded`, `out of scope with referral`, `information request`, `standard
investigation`, `urgent escalation`, `systemic review`, or `closed under an approved
rule with evidence`.

Do not use `no issue` as a shortcut when required data is missing.

## 4. Investigation planning

### 4.1 Convert the trigger into testable questions

Bad question: `Is this suspicious?`

Better questions:

- Did the subject perform the activity attributed to it?
- Does the activity fit the declared purpose, historical behavior, and peer segment?
- Which parties beneficially owned, controlled, initiated, approved, received, or
  benefited from the activity?
- Does the full sequence support a known typology, and which required elements are
  absent?
- Which legitimate explanations remain plausible, and what evidence distinguishes them?
- Did a control operate as designed? If not, was the failure isolated or systemic?
- What decision is required, by whom, under which criteria, by what date?

### 4.2 Hypothesis matrix

| Hypothesis ID | Proposition | Supporting evidence expected | Refuting evidence expected | Test | Result | Confidence |
|---|---|---|---|---|---|---|
| H1 | triggering explanation | | | | | |
| H2 | credible benign alternative | | | | | |
| H3 | data/control error | | | | | |
| H4 | broader linked activity | | | | | |

Include at least one credible alternative and one data-quality hypothesis. Update the
matrix as evidence changes; do not rewrite history by deleting rejected hypotheses.

### 4.3 Evidence plan

For each question, record:

```yaml
question_id: Q-01
question: <testable question>
criteria: <rule, policy, baseline, or threshold>
evidence_needed: []
preferred_sources: []
fallback_sources: []
authorization_or_owner: <role>
collection_status: requested|received|partial|unavailable
completion_test: <falsifiable stop condition, such as controlling record plus one
  independent source agree on the decisive attribute or the divergence is documented>
```

Collect proportionately. Do not expand into unrelated personal or commercial activity
merely because data is technically accessible.

## 5. Identity resolution and disambiguation

Identity must be resolved before adverse information, list records, transactions, or
relationships are attributed.

### 5.1 Preserve and normalize

Keep both raw and normalized values for:

- names, aliases, former names, transliterations, scripts, honorifics, and suffixes;
- dates of birth/incorporation and partial dates;
- addresses and historic locations;
- government, tax, company, license, vessel, aircraft, account, wallet, domain, email,
  phone, and device identifiers;
- nationality, residency, jurisdiction, occupation, roles, and employer/entity links.

Normalization generates candidates; it does not establish identity.

### 5.2 Attribute classes

| Class | Examples | Weight in resolution |
|---|---|---|
| Decisive unique | exact government/company identifier, IMO number, verified account ownership | sufficient if authentic, current, and uncontradicted; test those three before relying |
| Strong | full birth date plus geography; legal name plus registered address/directors | high, but test conflicts |
| Supporting | nationality, occupation, approximate age, related entities | corroborative only |
| Weak | name alone, common address, shared service provider, generic job title | candidate generation only |
| Contradictory | incompatible birth date, jurisdiction, identity number, chronology | may rule out if reliable and not explainable |

### 5.3 Resolution outcomes

`confirmed same`, `probable same`, `possible/unresolved`, `probable different`,
`confirmed different`.

Every outcome states matched attributes, mismatches, missing attributes, source quality,
and the decisive reason. Do not clear a candidate because one non-decisive field differs.

## 6. Screening disposition

This method applies to sanctions, politically exposed persons, adverse information, and
other official or approved lists. The applicable rules and decision rights differ; keep
each list type and regime explicit.

### 6.1 Required record

| Field | Requirement |
|---|---|
| Screened subject and identifiers | raw input plus normalized form |
| List/source | issuing body, list name, version/effective time, retrieval time |
| Candidate record | exact official record ID and attributes |
| Matching method | exact/fuzzy/transliteration rules and version |
| Attribute comparison | matched, mismatched, missing, and unreliable attributes |
| Ownership/control analysis | separate from name matching where applicable |
| Applicable regime and nexus | documented by authorized policy/legal source |
| Proposed disposition | true match, false positive, unresolved, or out-of-scope |
| Rationale and evidence | decisive facts and direct pointers |
| Reviewer/approval | role, decision, date, override reason |

### 6.2 Candidate decision logic

1. Confirm the input subject.
2. Confirm the official candidate record and current status.
3. Compare decisive identifiers before name similarity.
4. Explain transliteration, aliases, date ranges, and geographic changes.
5. Investigate ownership/control, indirect exposure, and applicable program separately.
6. Treat missing decisive data as unresolved, not as a mismatch.
7. Document the exact reason for a false positive.
8. Route possible true matches, meaning any candidate not cleared by a named cause under
   section 6.5, through the human escalation defined by section 1 decision rights; do
   not notify or act externally unless authorized.

### 6.3 PEP analysis

Record the public function, jurisdiction, seniority, dates, family/close-associate basis,
source, and current/former status. Assess risk-relevant authority, corruption context,
products, geography, source of wealth/funds, and control response. PEP status alone does
not establish wrongdoing and should not be presented as adverse conduct.

Materiality is the product of three factors: function tier (head-of-state and
national-executive level at the top, then senior officials, then junior or advisory
functions), status decay (a former senior function loses weight with time but never
reaches zero, while junior functions can time out under policy), and jurisdiction weight.
Family members and close associates derive materiality from the principal, reduced but
not dismissed while the principal remains material. Any credible adverse indicator
suspends decay. State the three factors separately; a single blended label hides the
reason for the rating.

### 6.4 Adverse information

Confirm subject identity, original event, procedural status, date, outcome, and relevance.
Group syndicated articles into one underlying event. Search for corrections and later
developments. Distinguish allegations, charges, findings, settlements, appeals, and
remediation.

Assess relevance as the combination of event severity (terrorist financing and sanctions
evasion at the top of the scale, then laundering, fraud and corruption, tax, regulatory,
civil), subject role (perpetrator above alleged, association, victim, passing mention),
recency, and source reliability. An old event of modest severity can close as stale and
immaterial under a defined horizon; a severe event never ages out on time alone. Record
which axis drove the disposition.

### 6.5 Named disposition causes and non-clearable conditions

A clearance is auditable only when it rests on a named, provable cause that a true match
could not exhibit, never on a low match score alone. Map resolution outcomes
(section 5.3) onto dispositions (section 6.1): `confirmed different` supports a false
positive, `confirmed same` supports a true match, and every intermediate outcome is
`unresolved` and stays with a human.

Canonical clear causes, drawn from published open screening implementations and stated
here as method, not calibrated policy:

| List type | Named cause | Guard that keeps it safe |
|---|---|---|
| Sanctions | generic-token-only match: every aligned name token is common vocabulary | valid only when the list entry also carries a distinctive token the subject did not match; an entry whose own name is entirely generic is never cleared by name |
| Sanctions | entity-type incompatibility: candidate and subject are different kinds of party | the type must come from the official record, not inference from the name |
| Sanctions | named discriminator: an official identifier contradicts the candidate | unavailable when the name match is near-exact; an exact full-name match is never cleared by a single conflicting field |
| PEP | identifier-proof wrong party | requires at least two independent contradicting fields; one conflicting field never clears |
| PEP | out-of-scope status: former holder of a junior function beyond the policy horizon | unavailable for any current or senior-tier function and for any corroborated identifier |
| Adverse media | wrong entity, non-adverse content, peripheral role (victim, witness, mention), or stale immaterial event | an uncorroborated common-name match routes to review, never to clearance |
| On-chain exposure | benign source category, broken intermediary, de minimis value share, or attenuated distance | absent hop distance routes to review; never substitute an assumed hop count to reach a disposition |

Conditions under which automated or analyst clearance is unreachable regardless of score:

- any match to a currently designated party or a current senior public function;
- any candidate with a corroborated identifier: corroborated identity goes to a human by rule;
- missing decisive data: unresolved is a routing state, not a clearance;
- an opaque or unreconciled layer anywhere in the relevant ownership graph;
- a same-entity conclusion without at least one shared strong identifier;
- an alert on which a defined typology pattern has fired (section 9.5);
- a case carrying an open `QA-CRITICAL` defect (section 15.2).

These constraints are deliberately asymmetric. They spend review effort to make a missed
true match structurally hard, because the two error costs are not symmetric.

## 7. Customer or entity file review

### 7.1 Review domains

| Domain | Required test |
|---|---|
| Identity | required identifiers present, valid, current, and internally consistent |
| Legal existence/status | authoritative registration and current status confirmed |
| Ownership/control | complete chain, calculation, control rights, and UBO rationale |
| Purpose/nature | documented, plausible, and consistent with products/activity |
| Geography | residence, incorporation, operations, counterparties, and funds flow captured |
| Expected activity | value, volume, frequency, counterparties, channels, and seasonality defined |
| Risk factors | approved factor set applied with evidence and rationale |
| Screening | current list/version, subjects screened, candidates/dispositions complete |
| Enhanced diligence | triggers, evidence, approvals, source of wealth/funds where required |
| Ongoing monitoring | review date, triggers, changed facts, and activity variance addressed |
| Documents/consents | required documents, expiry, certification, and permissions captured |
| Decision/governance | rating, conditions, approver, date, next review, and exceptions logged |

### 7.2 File completeness reconciliation

```text
required_items = valid_current + valid_with_documented_exception + missing_or_invalid
subjects_to_screen = successfully_screened + failed_or_pending
ownership_interests = identified_percent + unexplained_percent
```

Do not declare the file complete when any required total is unknown.

## 8. Beneficial ownership and control

### 8.1 Build the chain

1. Resolve the subject legal entity.
2. Identify every direct owner and percentage/class of interest.
3. Follow each legal-person owner upward until natural persons, public/regulated
   exemptions, or a documented unresolved layer.
4. Capture indirect economic ownership and separate voting/control rights.
5. Test nominees, trusts, partnerships, foundations, veto/appointment rights, informal
   control, and acting-in-concert indicators.
6. Reconcile each ownership layer to the expected total or explain the remainder.
7. Apply the current policy/regulatory threshold and aggregation rule; record its source.
8. Screen required persons and entities under the relevant workflow.

### 8.2 Indirect ownership

For a simple chain:

```text
indirect_interest = product(ownership_percentages_along_path)
aggregate_interest(person) = sum(indirect_interest_across_independent_paths)
```

Do not multiply control rights as if they were economic ownership. Record control as a
separate relationship. Prevent double counting when paths converge.

### 8.3 Ownership table

| Layer | Owner ID | Owned entity ID | Direct % | Indirect % to subject | Voting/control rights | Source | As of | Confidence |
|---|---|---|---:|---:|---|---|---|---|

### 8.4 Thresholds and aggregation discipline

- Apply the jurisdiction's identification threshold for beneficial ownership. The widely
  used public reference point is 25 percent of ownership interests (for example the
  [FinCEN customer due diligence rule](https://www.fincen.gov/resources/statutes-and-regulations/cdd-final-rule)),
  with control-based identification as a separate prong that no percentage satisfies.
  Check current exceptions and relief for the institution, customer, and account event;
  this reference threshold does not establish that every opening requires fresh collection.
- For sanctions exposure, apply the blocking rule of the relevant authority. Under the
  published OFAC 50 Percent Rule the interests of sanctioned owners aggregate: two
  blocked persons holding 30 and 25 percent in aggregate meet that ownership test
  even though neither alone reaches 50. Apply blocking through blocked intermediaries
  as described in [OFAC FAQ 401](https://ofac.treasury.gov/faqs/401): in its 50%-then-50%
  chain, the downstream entity is blocked despite a 25% multiplied economic interest.
  The economic path-product formula above is therefore not a sanctions algorithm.
- Treat a result just under a threshold as a review case, not a clean pass, and define
  the near-threshold band in policy before calculating.
- Control qualifies on substance: sole or decisive authority, or voting power at or
  above the applicable fraction. An ordinary non-sole directorship does not by itself
  establish control, and control routes to review rather than to a percentage.
- Circular and cross-holding structures make simple path products undercount. Resolve
  them as a converging series or equivalent method, cap any computed interest at 100
  percent, and route non-converging or capped results to review.
- Truncated evidence blocks clearance: when the ownership graph was cut off by data or
  computation limits, the unexamined part cannot support a below-threshold conclusion.

### 8.5 Threshold provenance and precision

Preserve the applicable regime, effective date, ownership class, threshold, aggregation
rule, control prong, and source of each percentage with the graph version. Compare
unrounded calculated interests against the threshold; round only for display. If
reported percentages are rounded or the filing is incomplete, show the uncertainty
interval and route any interval crossing the threshold for review. Do not substitute
an ownership-identification threshold for a sanctions blocking test or a control test.
The examples above illustrate different questions; obtain the current applicable rule
and qualified interpretation before an institutional decision.

## 9. Transaction and activity analysis

### 9.1 Preserve the ledger

Minimum fields:

`transaction_id`, source system, event/posted timestamps and timezone, account/wallet,
direction, amount, currency/asset, base-currency value and valuation method, balance,
originator, beneficiary, counterparties, channel, location, status/reversal, reference,
related transaction, and raw source pointer.

Never discard reversals, failures, fees, or corrections merely because they complicate
the story.

### 9.2 Core calculations

- count and value by direction, period, product, channel, geography, and counterparty;
- net and gross flow;
- opening + credits - debits +/- adjustments = closing balance;
- velocity, dwell time, turnover, burstiness, and dormant-period activation;
- unique and repeat counterparties;
- concentration and many-to-one/one-to-many patterns;
- near-threshold and multi-window aggregation;
- own-history and peer-baseline deviation;
- linked-account/device/address activity;
- funnel, circular, pass-through, and chain/sequence analysis;
- direct and indirect exposure with hop/path definitions.

State whether values use event time or posting time and how time zones, FX, token prices,
missing values, duplicates, and reversals were treated.

### 9.3 Chronology

| Time | Event ID | Actor/object | Observed event | Amount/unit | Evidence | Analytical relevance |
|---|---|---|---|---:|---|---|

Keep analytical interpretation out of the observed-event column.

### 9.4 Fund-flow reconciliation

```text
starting_value + inbound_value - outbound_value - fees +/- valuation_effect
  = ending_or_untraced_value
```

When asset conversions or incomplete paths prevent exact reconciliation, state the
valuation convention, residual, and uncertainty. Do not report percentage traced without
a numerator, denominator, and boundary.

### 9.5 Alert auto-close discipline

A fired typology pattern is the signal that an alert cannot be closed without analyst
review; auto-close is reachable only when no typology has fired. Named auto-close
causes, stated as method rather than calibrated policy:

- **Within profile:** every measured ratio sits inside the documented expected-activity
  band and no rule fired above the minor-severity floor.
- **Documented context:** each fired non-typology rule is explained by the recorded
  business type, gated on total throughput rather than transaction count, because
  count-based gating invites structuring just below the counter.
- **Below pattern threshold:** an indicator is present but the defined pattern minimum
  was not met, for example two near-threshold deposits where the structuring pattern
  requires three; record the shortfall so repetition stays visible.

The band between auto-close and mandatory escalation is deliberately not auto-closed.
That band is the analyst workload, and removing it removes the control.

## 10. Investigation finding and disposition

### 10.1 Five-element finding

1. **Criteria:** what should have occurred.
2. **Condition:** what the evidence shows.
3. **Cause:** confirmed reason or labeled hypothesis.
4. **Effect:** actual or potential consequence.
5. **Recommendation:** proportionate corrective or investigative action.

Add evidence, severity, confidence, owner, due date, and status.

### 10.2 Disposition logic

| Disposition | Minimum basis |
|---|---|
| No issue identified | complete required evidence; trigger explained; no contradictory material fact; reviewer agrees |
| Explained but monitor | plausible supported explanation; residual signal remains; monitoring condition/date defined |
| Information required | specific decision-critical evidence missing; owner/request/deadline recorded |
| Escalate for specialist/management review | material risk, ambiguity, policy/legal judgment, or authority exceeds investigator |
| Control/data issue | trigger or inability to conclude results from system/data/control defect; issue opened and affected population assessed |
| Related case/duplicate | same underlying event/subject; canonical record and evidence linkage established |
| Regulatory filing decision support | facts and analysis assembled under applicable procedure; authorized decision-maker decides |

### 10.3 Decision memo

```text
Decision requested:
Recommended disposition:
Bottom line:
Scope and completeness:
Criteria:
Key observed facts:
Material allegations/inferences:
Typologies considered:
Alternative explanations and counterevidence:
Risk and control implications:
Severity and rationale:
Confidence and rationale:
Options considered:
Recommended actions, owners, and dates:
Human approvals required:
Sources and evidence index:
Limitations:
```

## 11. Suspicious-activity decision support

This section supports internal analysis only. Filing thresholds, deadlines, narrative
requirements, confidentiality rules, and decision authority must come from current
jurisdiction-specific law and approved policy.

### 11.1 Analysis record

- who or what is involved, with resolved identifiers;
- what occurred, in chronological and quantitative terms;
- when and where it occurred;
- how value or instructions moved;
- why the activity may be unusual or relevant to a typology;
- which information supports and contradicts the concern;
- what investigation was performed and what remained unavailable;
- prior related activity or reports under approved access;
- possible victims, ongoing risk, preservation needs, and authorized escalation;
- decision criteria, decision-maker, decision time, and supporting evidence.

### 11.2 Narrative discipline

Use concise chronology, active voice, exact dates/amounts, full subject identifiers as
permitted, and specific counterparties. Explain why the pattern matters. Do not paste raw
alert text, list every irrelevant transaction, make unsupported legal conclusions, or
state inferred intent as fact. A filing narrative must be reviewed under the controlled
filing process.

## 12. Control design

### 12.1 From risk to control

```text
risk statement -> cause/event/impact -> control objective -> control activity
-> owner/frequency/evidence -> test procedure -> issue/remediation -> residual risk
```

Risk statement format:

`Because [cause], [event] may occur, resulting in [impact].`

Control objective format:

`Ensure that [risk-reducing outcome] occurs within [time/quality boundary].`

Control activity format:

`[Role/system] [performs action] [frequency/trigger] using [input], documents [evidence],
and escalates [exception] to [role] within [SLA].`

Avoid controls that say only `review`, `monitor`, or `ensure` without actor, object,
criteria, frequency, evidence, and exception path.

### 12.2 Control attributes

| Attribute | Values or questions |
|---|---|
| Nature | preventive, detective, corrective |
| Execution | manual, automated, IT-dependent manual, hybrid |
| Frequency | event-driven, continuous, daily, weekly, monthly, quarterly, annual |
| Level | entity, process, transaction, system, model, data, third party |
| Key status | would failure create material risk without timely compensating control? |
| Precision | can the control detect/prevent the defined error at the materiality stated in the control objective? An objective with no stated materiality is a design gap |
| Evidence | what immutable record demonstrates performance and review? |
| Exception | how is failure identified, owned, escalated, corrected, and closed? |
| Dependency | data, model, access, configuration, vendor, upstream/downstream control |

### 12.3 Control matrix schema

```yaml
control_id: CTRL-<domain>-<number>
risk_ids: []
objective: <text>
activity: <complete who/what/when/how/evidence statement>
owner: <role>
frequency: <value>
nature: preventive|detective|corrective
execution: manual|automated|it_dependent_manual|hybrid
population: <what is covered>
inputs: []
criteria_or_thresholds: []
evidence: []
exceptions_and_escalation: <text>
dependencies: []
key_control: true|false
design_rating: <value>
operating_rating: <value>
last_tested: <date>
issues: []
```

## 13. Control testing

### 13.1 Test design effectiveness

Determine whether the control, if performed as documented by a competent person with
reliable inputs, would prevent or detect the defined risk at the required precision and
time.

Test:

- risk-to-control alignment;
- complete population and scope;
- owner competence and segregation;
- frequency/timeliness;
- threshold/criteria precision;
- evidence and audit trail;
- dependencies and change management;
- exception, escalation, and correction path;
- known bypasses and compensating controls.

### 13.2 Test operating effectiveness

Use one or more methods:

| Method | What it establishes | Limitation |
|---|---|---|
| Inquiry | understanding of process and responsibility | never sufficient alone |
| Observation | control was performed at a point in time | may alter behavior; limited period |
| Inspection | evidence exists for selected instances | evidence may not prove quality |
| Reperformance | tester independently executes control/calculation | may require controlled access and expertise |
| Data analysis | full-population or targeted testing | depends on extract completeness and rule validity |

### 13.3 Workpaper structure

```text
WORKPAPER ID / CONTROL ID / VERSION
Objective and risk addressed
Control description and owner
Period, population, source, and reconciliation
Design-effectiveness assessment
Test method and sampling rationale
Procedures performed
Results by item with evidence pointers
Exceptions and management response
Projection or population impact, if valid
Compensating controls
Conclusion: effective / effective with improvement / ineffective / unable to conclude
Prepared by / reviewed by / dates
```

### 13.4 Sampling

Define population, sampling unit, period, source, completeness, expected deviation,
tolerable deviation, confidence, and selection method before selecting items.

- Use random or systematic sampling when inference to a population is intended.
- Use targeted/judgmental samples for risk discovery, not for unbiased population claims.
- Stratify when size, severity, geography, channel, or control performer changes risk.
- Test every item in a critical or rare high-risk stratum instead of sampling it.
- Record seed or selected IDs for reproducibility.
- Evaluate both count and nature of exceptions.

If zero exceptions appear in `n` independent items, do not claim the deviation rate is
zero. For formal conclusions use the exact method in module `09`: a binomial or
hypergeometric design whose zero-defect one-sided bound is `1 - alpha^(1/n)`, replacing
table interpolation and normal approximations. The rule-of-three approximation `3/n` is
acceptable only for quick internal sizing, never for a reliance conclusion.

### 13.5 Exception classification

| Class | Description | Treatment |
|---|---|---|
| Documentation | control may have occurred but required evidence is insufficient | assess whether evidence is integral; cannot assume performance |
| Execution | control step omitted, late, or incorrect | determine frequency, cause, population, and impact |
| Design | control cannot address risk at required precision | redesign; broader population exposure likely |
| Data/system | input, logic, access, interface, or configuration is defective | contain; assess affected period/population; open data/technology issue |
| Governance | ownership, review, escalation, or change control failed | management action and accountability required |

## 14. Issue and remediation management

### 14.1 Issue record

| Field | Requirement |
|---|---|
| Issue ID/title | stable and specific |
| Source | case, audit, test, incident, regulator, self-identification |
| Criteria/condition | required state and observed gap |
| Root cause | method and supported result; hypothesis labeled |
| Impact and population | actual/potential, period, products, records, customers, jurisdictions |
| Severity | approved framework with rationale |
| Immediate containment | action, owner, completion evidence |
| Remediation plan | milestones that address root cause, not symptoms |
| Owner/approver | accountable roles |
| Due dates | regulatory/management and milestone dates |
| Dependencies | technology, data, vendor, policy, training, funding |
| Validation | independent closure test and evidence |
| Status/history | immutable change trail, extensions, risk acceptance |

### 14.2 Root-cause methods

Use evidence-led five-whys, causal tree, process walk-through, data lineage, control
dependency mapping, and change chronology. Avoid `human error` as a root cause unless the
systemic reasons the error was possible and undetected are addressed.

### 14.3 Closure gate

An issue closes only when:

- approved actions are complete and evidenced;
- root cause is addressed;
- affected population has been corrected or risk accepted by authorized role;
- updated control is implemented for the required period;
- independent validation tests design and operating effectiveness;
- residual risk is within appetite or formally accepted;
- documentation, training, monitoring, and ownership are current;
- no contradictory open evidence remains.

## 15. Independent QA and case review

Review the work, not just the final paragraph.

### 15.1 Review dimensions

| Dimension | Core question |
|---|---|
| Scope/completeness | Did the analyst review the right population and reconcile it? |
| Identity | Are subjects and candidates correctly resolved? |
| Evidence | Can every material fact be traced to reliable support? |
| Method | Was the correct framework applied consistently and at the right version? |
| Analysis | Were chronology, amounts, relationships, baselines, alternatives, and gaps addressed? |
| Decision | Does the conclusion follow from criteria and evidence? |
| Writing | Are fact, allegation, inference, and projection distinct? |
| Actions | Are recommendations proportionate, authorized, owned, and time-bound? |
| Record | Does the case retain source, calculations, approvals, and changes? |

### 15.2 Error types

- **`QA-CRITICAL`:** wrong subject, missed plausible true match, unauthorized action,
  material evidence omitted, incorrect regulated decision, or unreconciled material
  population;
- **`QA-HIGH`:** unsupported conclusion, key procedure not performed, material
  calculation or typology error, or missing required approval;
- **`QA-MEDIUM`:** localized evidence, calculation, citation, or documentation defect
  that affects precision or completeness without overturning the central decision;
- **`QA-LOW`:** cosmetic or minor consistency defect with no material effect; and
- **coaching note:** improvement opportunity with no control or decision impact; this
  is not a QA issue severity.

Module `09` controls the universal QA taxonomy and release effects. Do not average away
a `QA-CRITICAL` defect with many correctly completed checklist fields.

### 15.3 Named QA checks

Review against named checks, not a general impression. The core set:

- wrong subject resolved; cleared with unreviewed scope; contradictory disposition,
  where the narrative supports one outcome and the decision records another;
- missed plausible true match; missed escalation trigger; unauthorized external action;
- unsupported material fact; population not reconciled; calculation not reproducible;
- required approval absent; broken evidence pointer; incomplete retention; SLA breach
  beyond the defined material multiple.

Score-only QA gates are unsafe. In the published open reference implementation this list
derives from, files planted with critical deficiencies still scored 74 to 79 of 100,
inside any plausible pass threshold, because many correct checklist fields average away
one fatal defect. A critical finding must make the pass state unreachable
(section 15.2), whatever the score says.

## 16. Model and rules governance

For a scoring model, matcher, threshold, scenario, or automated classifier, document:

- intended use, decision role, users, and prohibited uses;
- data sources, lineage, representativeness, missingness, and protected characteristics;
- features/indicators, transformations, logic, parameters, and version;
- training/tuning and validation populations with leakage controls;
- performance by relevant segment, not only aggregate;
- false-positive and false-negative cost, with safety gates;
- calibration, stability, drift, overrides, and challenger comparison;
- explainability and evidence retained per outcome;
- change approval, deployment, rollback, access, monitoring, and retirement;
- human review and appeal/exception paths.

Prompt-only reasoning aids are not validated models merely because they contain scores.
If a score influences decisions, it requires governance proportionate to impact.

For detection thresholds, tune from a labeled review population using above-the-line
productivity and below-the-line leakage, and recommend the highest threshold whose
detection rate still meets the required recall floor. Tuning may trade alert volume
against analyst capacity; it may never trade away required detection, so a candidate
threshold below the floor is not an option at any volume saving. Keep a small tolerance
band around the incumbent threshold to avoid churn from immaterial differences.

## 17. Policy-gap and obligation-to-control analysis

Build explicit traceability:

```text
source provision -> atomic obligation -> policy statement -> procedure step
-> control -> system/data requirement -> evidence -> test -> issue/action
```

For each obligation classify coverage as:

`covered`, `partially covered`, `not covered`, `conflicting`, `not applicable with
rationale`, or `unable to determine`.

Do not mark an obligation covered because a policy mentions the topic. Confirm actor,
action, scope, trigger, timing, exception, evidence, and enforcement align.

Gap record:

| Field | Requirement |
|---|---|
| Gap ID | stable identifier |
| Obligation/citation | exact provision and current status |
| Existing coverage | policy/procedure/control evidence |
| Gap | precise missing or inconsistent element |
| Impact | affected entities/products/processes and deadline |
| Recommendation | change required |
| Owner/dependency/due date | implementation accountability |
| Validation | how closure will be tested |

## 18. Regulatory-exam or review response pack

1. Parse the request into atomic questions, periods, entities, formats, and deadlines.
2. Assign owner, reviewer, source system, and privilege/confidentiality handling.
3. Maintain a request tracker and immutable version history.
4. Retrieve responsive materials through authorized channels.
5. Reconcile populations and explain exclusions.
6. Draft a response that answers the question directly and distinguishes current state,
   historical state, and planned remediation.
7. Link every statement to production evidence.
8. Run legal/policy/management review as required.
9. Validate filenames, indexes, cross-references, redactions, and delivery package.
10. Log exact submission, time, recipient, and confirmation.

Never create missing historical evidence. Describe the gap and current remediation.

## 19. New-product approval and post-implementation review

### 19.1 Approval pack

- product/process/data flow and legal-entity map;
- target users, eligibility, geographies, channels, and expected volumes;
- risk assessment across module `04` domains;
- obligation and license analysis with counsel/policy-owner gates;
- risk-to-control-to-test traceability;
- data contracts, lineage, reconciliation, privacy, retention, and access;
- third-party diligence and exit/continuity plan;
- operational readiness, procedures, training, support, disputes, and incidents;
- technology/security testing and rollback;
- monitoring, KRIs, alert handling, governance, and launch conditions;
- residual risks, exceptions, accountable acceptance, and decision record.

### 19.2 Launch condition

| Condition | Owner | Evidence | Status | Due | Blocking? | Approver |
|---|---|---|---|---|---|---|

No blocking condition may be represented as complete without evidence. Do not downgrade
a blocker merely to meet a launch date.

### 19.3 Post-implementation review

Compare actual vs approved assumptions: users, volumes, geographies, loss, alerts,
complaints, exceptions, control performance, data quality, incidents, vendors, and
regulatory changes. Identify emergent typologies and unanticipated manual work. Reassess
residual risk and decide continue, condition, remediate, restrict, or retire through the
authorized governance body.

## 20. Copy-ready operating prompts

### 20.1 Full investigation

```text
Use modules 00, 01, 04, 05, 06, 07, and 09. Build a complete decision-support case for
[trigger] covering [population/subject], [period/timezone], and [systems/sources]. Begin
with a manifest, scope reconciliation, testable questions, and a hypothesis matrix that
includes benign and data-quality explanations. Preserve raw values and source pointers;
resolve identities; build a chronology, fund-flow/relationship analysis, and typology
matrix. Separate observed, reported, inferred, and projected content. Quantify all
material totals and residuals. Produce a proposed disposition, alternatives, severity,
confidence, evidence index, limitations, and action tracker. Do not make or execute the
regulated decision. Run the release gate before handoff.
```

### 20.2 Control test

```text
Test [control ID] for [period]. Before selecting items, document the risk, objective,
control activity, population, source, completeness reconciliation, test method, sampling
basis, tolerable criteria, and evidence expected. Evaluate design first. Then test
operating effectiveness through inquiry plus inspection, observation, reperformance, or
full-population analysis as appropriate. Record item-level results and evidence pointers.
Classify exceptions by nature and severity, assess affected population and compensating
controls, and state whether the control is effective, effective with improvement,
ineffective, or unable to conclude. Produce a workpaper, exception log, remediation
tracker, and independent-review checklist. Do not project a judgmental sample to the
population.
```

### 20.3 Policy gap analysis

```text
Compare [current policy/procedure/control set] to [authoritative requirement set] as of
[date]. Extract atomic obligations with exact citations and status. Map each obligation
to policy, procedure, control, system/data requirement, evidence, and test. Classify
coverage using the controlled values in section 17. For every gap, state the precise
missing element, affected scope, deadline, severity, confidence, proposed action, owner,
dependency, and closure test. Separate legal text from interpretation and route legal
questions to the authorized reviewer. Reconcile all obligations and run the release gate.
```

## 21. Minimum release checklist

- Correct object, subject, jurisdiction, regime, policy version, period, and time zone.
- Stable case, source, evidence, finding, control, issue, and action identifiers.
- Population reconciled; inaccessible, excluded, duplicate, and failed items visible.
- Identity resolution precedes attribution and disposition.
- Complete chronology and quantitative reconciliation where activity is involved.
- Criteria stated before condition; cause labeled if inferred.
- Alternative explanations and counterevidence tested.
- Severity and confidence independently reasoned.
- Proposed decision is distinct from approved and executed action.
- Human gates, confidentiality, and need-to-know restrictions applied.
- Evidence package supports independent reperformance.
- Output meets module `07`; review and release meet module `09`.
