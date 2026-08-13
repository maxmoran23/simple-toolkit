# Data Quality and Governance

Use this file to establish whether data is defined, controlled, traceable, fit for an intended use, and governed through change. It covers inventories, critical data elements, contracts, profiling, rules, thresholds, lineage, reconciliation, exceptions, incidents, monitoring, testing, evidence, and deployment.

This standard does not repair data automatically, certify a system, or replace accountable owners. It creates inspectable evidence and controlled routing. A high composite score never overrides a critical breach, a failed reconciliation, an unknown population, or a required human decision.

## 1. Operating principles

1. **Fitness is use-specific.** Data can be adequate for one purpose and unacceptable for another. State the intended use, grain, population, and consequence before measuring quality.
2. **Source values are evidence.** Preserve them; place standardization, imputation, and corrections in versioned derived fields.
3. **Criticality drives control depth.** Identify critical data elements and critical transformations before applying generic profiling.
4. **Rules are contracts.** Each rule has an owner, rationale, population, numerator, denominator, exclusions, threshold, effective date, and test evidence.
5. **Reconciliation precedes interpretation.** Unknown or unexplained population loss invalidates downstream percentages.
6. **Hard gates are structural.** A critical breach cannot be averaged away by clean noncritical fields.
7. **Accuracy requires a reference.** Format conformance is validity, not proof that a value is true.
8. **Exceptions expire.** A waiver without an owner, compensating control, and expiry is silent acceptance.
9. **Lineage must be testable.** A diagram without executable or observed evidence is documentation, not assurance.
10. **Change is governed.** Schema, semantics, rules, thresholds, references, mappings, and models are versioned and impact-assessed.
11. **Automation proposes and routes.** Consequential overrides, releases, merges, deletions, and external notifications remain human-gated unless an approved deterministic control explicitly authorizes them.
12. **Evidence is retained.** A conclusion must reproduce from identified inputs, code/rules, parameters, environment, and run manifest.

When a finding includes a confidence judgment, use only `HIGH`, `MODERATE`, `LOW`, or `NOT ASSESSABLE`, always with a basis. Use `UNRESOLVED` for an issue, match, exception, or disposition status. Use `SPECULATIVE` only to label an unverified hypothesis or claim state, never as a confidence tier.

## 2. Outcomes and boundaries

### Questions every governed data product must answer

- What does each record represent, at what grain, and as of when?
- Which source is authoritative for each element and why?
- Which elements and transformations are critical to the stated use?
- What population was expected, received, rejected, transformed, and published?
- Which quality rules apply, how were thresholds set, and what failed?
- What changed relative to contract, baseline, and prior run?
- Which downstream products, decisions, reports, or controls are affected?
- Who owns the data, rule, remediation, exception, and release decision?
- What evidence proves the assessment and supports closure?

### In scope

- structured, semi-structured, and governed unstructured data products;
- batch files, tables, event streams, APIs, extracts, reports, and reference sets;
- source, ingestion, transformation, storage, serving, and consumption layers;
- manual, deterministic, statistical, and model-assisted checks;
- historical backfills, corrections, restatements, and deletions;
- data used by analytics, operations, automation, reporting, and control processes.

### Out of scope unless separately authorized

- editing a source-of-record value;
- selecting an institution's policy thresholds without accountable-owner approval;
- deciding that a legal, regulatory, contractual, or policy exception is acceptable;
- merging ambiguous entities or deleting duplicate records;
- releasing a blocked feed or report;
- asserting that an inaccessible source, unobserved process, or unavailable control worked;
- using sensitive data beyond the approved purpose.

## 3. Governance roles and RACI

### Roles

| Role | Core accountability |
|---|---|
| Data owner | Accountable for meaning, acceptable use, criticality, quality tolerance, and release decisions |
| Data steward | Maintains definitions, catalog, rules, issues, and day-to-day quality coordination |
| Source owner | Owns source capture, source controls, and upstream remediation |
| Data producer | Delivers data under the contract and resolves producer-side defects |
| Platform/custodian | Operates storage, transport, access, backup, and technical controls |
| Transformation owner | Owns mapping, business logic, code, and transformation reconciliation |
| Consumer owner | Defines fitness requirements and confirms downstream impact |
| Rule owner | Owns rule intent, implementation mapping, threshold, and review cadence |
| Reference-data owner | Owns controlled values, effective dating, and update evidence |
| Model/automation owner | Owns model-assisted checks, evaluations, limits, and monitoring |
| Incident owner | Coordinates containment, communication, remediation, validation, and closure |
| Independent reviewer | Challenges design, evidence, results, exceptions, and release disposition |
| Approver | Accepts residual risk or authorizes release within delegated authority |

### Minimum RACI by activity

| Activity | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Define data product and grain | Steward/producer | Data owner | Consumer, transformation owner | Custodian |
| Designate CDEs | Steward | Data owner | Consumer, control owner | Producer |
| Approve contract | Producer/steward | Data owner | Consumer, custodian | Reviewer |
| Implement rule | Producer or transformation owner | Rule owner | Steward, reviewer | Consumer |
| Approve threshold | Rule owner/steward | Data owner | Consumer, reviewer | Producer |
| Investigate defect | Assigned producer/owner | Data owner | Consumer, steward | Incident owner |
| Approve exception | Steward | Authorized risk owner | Consumer, reviewer | Producer |
| Release after breach | Producer | Authorized approver | Owner, reviewer, consumer | Incident owner |
| Close incident | Incident owner | Data owner | Reviewer, affected consumers | Governance forum |
| Change schema or semantics | Producer | Data owner | Consumers, custodian, reviewer | All registered dependents |

Replace role names with the adopting organization's approved structure, but do not leave accountability implicit.

## 4. Data-product inventory

Create one inventory record for every governed input, intermediate product, reference set, and published output.

### Inventory schema

| Field | Required content |
|---|---|
| `data_product_id` | Stable identifier independent of display name |
| `name` / `description` | Plain-language definition |
| `business_purpose` | Approved uses and decisions supported |
| `prohibited_uses` | Known uses the data is not fit or authorized for |
| `owner_role` / `steward_role` | Accountable and operational roles |
| `producer` / `consumers` | Systems, processes, or roles |
| `source_of_record` | Authoritative origin and basis |
| `grain` | What one row/event/object represents |
| `population` | Inclusion, exclusion, and eligibility rules |
| `primary_key` / `candidate_keys` | Uniqueness basis and limitations |
| `time_semantics` | Event, effective, processing, load, report, and timezone rules |
| `delivery` | Batch/stream/API cadence, expected window, and completeness signal |
| `schema_reference` | Versioned schema or contract |
| `classification` | Sensitivity, confidentiality, residency, and handling |
| `retention` | Approved retention and deletion rules |
| `cdes` | Critical data-element identifiers |
| `critical_transformations` | Transformations whose failure materially affects use |
| `quality_tier` | Control depth based on risk and use |
| `lineage_reference` | Design-time and observed lineage |
| `service_expectations` | Freshness, availability, recovery, and support commitments |
| `status` | Proposed, active, restricted, deprecated, retired |
| `effective_from` / `effective_to` | Version validity |
| `last_reviewed` / `next_review` | Governance cadence |

### Inventory completeness controls

- Reconcile catalog entries to deployed tables, feeds, exports, API endpoints, scheduled jobs, and registered reports where that metadata is available.
- Require an owner and lifecycle status for every active product.
- Identify “dark data”: active products with no owner, consumer, contract, lineage, or recent use evidence.
- Identify unregistered dependencies from query logs, orchestration metadata, code references, or consumer attestations when authorized and available.
- Do not infer that absence from a catalog means the product does not exist.
- Record products that could not be inspected as inventory gaps.

## 5. Critical data elements and transformations

### CDE designation test

Designate an element critical when an error could materially affect one or more of:

- external or management reporting;
- legal, regulatory, contractual, or policy obligations;
- eligibility, routing, escalation, approval, or control execution;
- financial, risk, operational, or customer-impacting decisions;
- entity identity, aggregation, matching, or ownership;
- access, privacy, security, retention, or recordkeeping;
- downstream model, rule, or automation behavior;
- a material reconciliation or control total.

Criticality is consequence-based, not popularity-based. A rarely populated override flag can be more critical than a widely used descriptive field.

### CDE register

| Field | Required content |
|---|---|
| `cde_id` / `data_product_id` | Stable element and parent product |
| `business_name` / `technical_name` | Plain and physical names |
| `definition` | Meaning, scope, and exclusions |
| `data_type` / `format` / `unit` | Representation contract |
| `allowed_values_or_reference` | Versioned domain or validation source |
| `source_of_truth` | Authoritative origin and conditions |
| `derivation` | Formula or transformation reference |
| `grain` / `cardinality` | Expected relationship to product grain |
| `null_semantics` | Whether null, blank, zero, unknown, not applicable, and not collected differ |
| `time_semantics` | Effective dating, timezone, cutoff, and precision |
| `criticality_basis` | Consequence and affected uses |
| `quality_dimensions` | Applicable dimensions and rule IDs |
| `hard_gate` | Whether a breach blocks release or use |
| `owner` / `steward` | Accountable roles |
| `consumers` | Registered dependent products/processes |
| `effective_dates` | Definition/version period |

### Critical transformation register

Treat joins, filters, mappings, aggregations, allocations, currency/unit conversions, entity resolution, temporal logic, and suppression/exclusion logic as governed transformations when they can materially change the population or result.

For each critical transformation record:

- input and output grain;
- code/query/configuration version;
- logic in plain language and executable reference;
- join type, keys, expected cardinality, and unmatched treatment;
- filter and exclusion rationale;
- ordering and effective-date rules;
- null and error handling;
- reconciliation controls;
- owner, reviewers, dependencies, and change history.

## 6. Grain, keys, and semantic discipline

Confirm grain before profiling or aggregation. Many apparent data-quality failures are mixed grain, expected one-to-many relationships, partial snapshots, or late-arriving records; many real failures are hidden by assuming grain.

### Grain declaration

Write the grain as a complete sentence:

```text
One record represents <entity/event/state> for <population> at <time basis>,
unique by <key>, excluding <explicit exclusions>.
```

### Key controls

- Test the declared primary or composite key for nulls and duplicates.
- Distinguish a source key, business key, surrogate key, event ID, and version key.
- Document whether identifiers can be reused, corrected, or reassigned.
- Test key uniqueness by effective period where slowly changing records are expected.
- Record key collision and key churn rates.
- Do not use row position, load order, or unstable hashes as a durable key without an explicit limitation.
- Compare record and distinct-entity counts before and after joins.
- Treat many-to-many joins as prohibited unless specifically designed, quantified, and reconciled.

### Null and sentinel semantics

Create a controlled mapping for:

- missing/not supplied;
- unknown;
- not applicable;
- intentionally withheld;
- not yet available;
- parse failure;
- source-system error;
- legacy sentinel;
- valid zero or empty collection.

Do not collapse these states to a single null unless the contract explicitly permits it and consumers accept the information loss.

## 7. Data contracts

A data contract binds producer and consumers to a versioned, testable agreement. Documentation alone is insufficient; contract checks should run at an appropriate enforcement point where capability exists.

### Contract layers

| Layer | Content |
|---|---|
| Structural | Fields, types, nullability, keys, nesting, file/API encoding, partitioning |
| Semantic | Definitions, grain, populations, statuses, units, timezone, effective dating |
| Behavioral | Cadence, freshness, completeness signal, ordering, late-arrival and correction behavior |
| Quality | CDEs, rules, thresholds, hard gates, warning bands, reconciliation requirements |
| Operational | Ownership, support, incident route, recovery, backfill, deprecation |
| Security | Classification, access, encryption, residency, retention, masking |
| Evolution | Versioning, compatibility, notice, migration, rollback, consumer attestation |

### Copy-ready contract template

```yaml
contract_id: <stable id>
version: <semantic or approved version>
status: <draft/approved/deprecated/retired>
effective_from: <ISO date/time>
producer: <role/system>
owner: <accountable role>
consumers: [<registered consumers>]
purpose: <approved use>
prohibited_uses: [<uses>]
grain: <one-record sentence>
population:
  include: [<rules>]
  exclude: [<rules>]
keys:
  primary: [<fields>]
  version: [<fields>]
time:
  event_field: <field or none>
  effective_fields: [<fields>]
  load_field: <field>
  timezone: <IANA timezone/UTC/source-defined>
  cutoff: <rule>
delivery:
  mode: <batch/stream/API/export>
  cadence: <expectation>
  completeness_signal: <signal>
  late_arrival: <policy>
schema:
  fields:
    - name: <technical name>
      definition: <definition>
      type: <type>
      nullable: <true/false>
      null_semantics: <meaning>
      allowed_values_ref: <versioned reference or none>
      unit: <unit or none>
      cde: <true/false>
quality:
  rules: [<rule ids>]
  reconciliation: [<control ids>]
  hard_gates: [<gate ids>]
security:
  classification: <class>
  access: <least-privilege rule>
  retention: <rule>
change:
  compatibility_policy: <policy>
  notice_period: <policy-defined>
  rollback: <method>
approvals:
  producer: <reference>
  owner: <reference>
  consumer: <references>
```

### Compatibility classification

| Change | Default classification | Required treatment |
|---|---|---|
| Add optional field with stable semantics | Potentially backward-compatible | Contract tests and consumer notice |
| Add required field | Breaking | New version, migration, explicit consumer readiness |
| Remove or rename field | Breaking | New version and deprecation path |
| Change type, unit, timezone, definition, grain, or population | Breaking semantic change | Full impact assessment and parallel validation |
| Expand controlled values | Potentially breaking | Consumer accepted-values test |
| Change key or deduplication behavior | Breaking | Reconciliation, backfill, and identity impact review |
| Change late-arrival, correction, or cutoff behavior | Breaking behavioral change | Period-comparison and restatement review |
| Tighten quality rule/threshold | Operationally breaking | Capacity, exception, and downstream readiness review |

Never classify a semantic change as compatible merely because the physical schema is unchanged.

## 8. Lineage

### Required lineage layers

1. **Business lineage:** source concept -> transformation purpose -> consumed metric, decision, control, or report.
2. **Technical lineage:** physical object/field -> job/query/code -> physical object/field.
3. **Operational lineage:** observed run, input versions, execution, row counts, outputs, and status.
4. **Record lineage:** where proportionate, output record/value -> contributing source records and transformation version.

### Lineage edge schema

| Field | Required content |
|---|---|
| `edge_id` | Stable identifier |
| `from_product/field` / `to_product/field` | Source and target |
| `transformation_id/version` | Executable or governed logic reference |
| `relationship` | Copy, map, filter, join, derive, aggregate, allocate, resolve, redact, enrich |
| `grain_change` | Input and output grain |
| `effective_from/to` | Validity period |
| `observed_run` | Runtime evidence, if available |
| `owner` | Responsible role |
| `evidence` | Code, orchestration metadata, query, manifest, or attestation reference |
| `verification_status` | Verified, observed-partial, documented-only, or unknown; use `HIGH`, `MODERATE`, `LOW`, or `NOT ASSESSABLE` only when a separate confidence judgment is required |

### Lineage controls

- Reconcile registered inputs/outputs to observed job metadata where available.
- Flag transformations with no registered owner or consumers.
- Trace every CDE through each critical transformation.
- Record fan-in, fan-out, joins, filters, and aggregations that change counts or grain.
- Perform impact analysis before a contract, rule, mapping, reference, or schema change.
- Verify lineage after deployment; design-time lineage can become stale.
- Treat inaccessible or dynamically generated logic as a lineage gap.

## 9. Profiling and baselines

Profile before setting thresholds and after material changes. Use authorized environments and minimize exposure of sensitive values.

### Compact profile

For each product and relevant segment/time bucket capture:

- row/object count and distinct entity/event count;
- column/field count, names, types, order where contract-relevant, and schema fingerprint;
- primary/candidate-key null and duplicate rates;
- null, blank, sentinel, and parse-failure rates;
- distinct counts, cardinality ratios, and controlled-value coverage;
- min/max timestamps, freshness lag, missing partitions, and future-dated rates;
- numeric min/max, quantiles, zero/negative rates where semantically relevant;
- string lengths, encodings, patterns, and normalization effects;
- referential-integrity and join-coverage rates;
- exact and near-duplicate rates;
- category shares and new/disappeared categories;
- input/output record counts around each critical transformation.

### Baseline governance

- Baselines have an approved population, window, seasonality treatment, and version.
- Exclude known incidents, partial loads, migrations, and backfills only with documented reason.
- Use rates and robust distributions, not counts alone.
- Segment by source, region, product, platform, status, or other relevant dimensions before calling an aggregate stable.
- Keep warning baselines separate from absolute policy limits.
- A breached batch does not silently reset the baseline against which it failed.
- Record expected late arrival and unstable recent partitions.
- Recompute only under controlled change and retain prior baselines for comparison.

## 10. Quality dimensions and measures

Use dimensions consistently. One defect may map to several dimensions, but avoid double counting in scores by defining the aggregation rule.

| Dimension | Question | Typical measures |
|---|---|---|
| Completeness | Is required data present for the eligible population? | Required-field population rate; missing partition/segment rate; attachment or child-record coverage |
| Accuracy | Does the value agree with an authoritative or independently validated reference? | Agreement rate, confirmed error rate, reference coverage |
| Validity | Does the value conform to type, format, domain, range, and calendar rules? | Parse pass rate, accepted-value rate, domain/range violation rate |
| Consistency | Do related values, products, periods, and calculations agree? | Cross-field contradiction rate, cross-source variance, unit/status alignment |
| Uniqueness | Is each record/entity represented according to the declared grain? | Duplicate-key rate, exact/near-duplicate rate, collision rate |
| Timeliness | Is data available and refreshed when needed? | Delivery lag, freshness lag, late-arrival rate, stale-record rate |
| Integrity | Are relationships and transformations structurally intact? | Orphan rate, join coverage, unexpected cardinality expansion, broken sequence rate |
| Conformity | Does delivery match the contract? | Schema, encoding, naming, precision, ordering, and partition conformance |
| Volume/shape | Is population size and distribution plausible relative to expectation? | Count drift, category-share drift, distribution shift, new/disappeared strata |
| Lineage | Can the value and product be traced through governed transformations? | CDE lineage coverage, observed-lineage coverage, unowned edge rate |

### Core formulas

State numerator, denominator, exclusions, and zero-denominator behavior for every metric.

```text
defect_rate = defective eligible records / eligible records tested
pass_rate = records passing the named rule / eligible records tested
completeness_rate = populated eligible values / eligible values required
uniqueness_rate = unique valid keys / eligible records expected unique
referential_coverage = child keys matching parent / eligible child keys
freshness_lag = assessment cutoff - latest complete source/event/load time, as defined
join_multiplier = output rows after join / input rows before join
reconciliation_variance = output control total - expected control total
```

Do not compute `1 - defect_rate` as a general pass rate when some records were not evaluated. Report `not_evaluated_rate` separately.

## 11. Rule taxonomy and rule specification

### Rule types

| Type | What it checks | Example form without production values |
|---|---|---|
| Presence | Required element populated for eligible state | `required_field is not null when eligibility_rule` |
| Type/parse | Strict type and calendar/encoding parse | `parse(value) succeeds` |
| Domain/reference | Value belongs to effective controlled set | `value in reference(version, effective_date)` |
| Range/plausibility | Value within justified bounds | `lower_bound <= value <= upper_bound` |
| Cross-field | Values obey a logical relationship | `state implies required timestamp` |
| Sequence/time | Event/effective dates occur in permitted order | `start <= end <= cutoff` |
| Key/uniqueness | Declared key unique at intended grain | `count by key <= permitted versions` |
| Referential | Child/parent relationship exists and has expected cardinality | `foreign key matches exactly one eligible parent` |
| Reconciliation | Counts or control totals tie through processing | `source = accepted + rejected + quarantined` |
| Freshness | Delivery/load/refresh meets defined clock | `lag <= approved limit` |
| Drift | Volume, sparsity, category, or distribution changed beyond approved band | `current vs baseline under method` |
| Schema/contract | Physical and semantic contract holds | `schema fingerprint compatible with contract version` |
| Duplicate/entity | Exact or candidate duplicate meets a documented rule | `blocking + comparison + review route` |
| Lineage | CDE paths and critical transformations remain mapped | `required lineage edges observed` |
| Privacy/security | Handling and use match approved controls | `classification/access/retention rule holds` |

### Rule specification

```yaml
rule_id: <stable id>
version: <version>
name: <short name>
description: <plain-language failure condition>
dimension: <dimension>
data_product: <id>
fields: [<field ids>]
cde: <true/false>
critical_transformation: <id or none>
population:
  grain: <grain>
  eligibility: <logic>
  exclusions: [<explicit approved exclusions>]
logic:
  executable_reference: <query/code/config reference>
  plain_language: <rule>
  reference_data: <id/version/effective date or none>
measure:
  numerator: <failed units>
  denominator: <eligible tested units>
  not_evaluated: <treatment>
thresholds:
  warning: <approved value/method>
  breach: <approved value/method>
  hard_gate: <true/false>
  comparison: <greater-than/at-least/etc.>
error_posture:
  false_negative_consequence: <impact>
  false_positive_consequence: <impact>
severity: <rule severity and basis>
routing:
  owner: <role>
  reviewer: <role>
  downstream_action: <hold/investigate/warn/report>
evidence:
  test_fixture: <reference>
  validation: <reference>
  last_reviewed: <date>
effective_from: <date/time>
effective_to: <date/time or null>
change_reference: <approval/diff>
```

### Rule implementation controls

- Rule names and versions in output must map to the exact executed logic.
- Compile or parse failures are test failures, not zero defects.
- Record evaluated, failed, passed, excluded, and not-evaluated populations.
- Suppress duplicate symptoms only under a documented precedence rule; retain the causal defect.
- Version external reference data and apply correct effective dates.
- Do not change thresholds inside code without updating the governed specification.
- Emit record-level defect references sufficient for remediation without exposing unnecessary sensitive content.

## 12. Thresholds, error posture, and dispositions

### Threshold design

Thresholds must be owned and justified. Consider:

- intended use and downstream consequence;
- CDE and transformation criticality;
- contractual or policy requirements;
- historical clean-state distribution and seasonality;
- expected late arrival and source correction behavior;
- measurement error and rule precision/recall;
- operational capacity and remediation route;
- false-negative and false-positive consequences;
- sample uncertainty where rules are sampled rather than full-population;
- performance under adverse and boundary cases.

Do not adopt sample numbers, defaults, or industry folklore as policy. Record how each threshold was calibrated, challenged, approved, and scheduled for review.

### Bands

Use distinct bands where appropriate:

- `OK`: within approved operating range;
- `WATCH`: directional deterioration or proximity to breach;
- `BREACH`: approved limit exceeded;
- `NOT_EVALUATED`: rule could not run on the eligible population;
- `NOT_APPLICABLE`: rule does not apply under its eligibility logic.

`NOT_EVALUATED` is not `OK`.

### Hard-gate firing order

1. **Population/reconciliation gate:** unknown population, incomplete critical input, or failed reconciliation -> `HOLD_NOT_RECONCILED`.
2. **Critical-rule gate:** any approved critical rule in breach -> `BLOCK_OR_HOLD`.
3. **Evaluability gate:** material critical population not evaluated -> `HOLD_NOT_EVALUATED`.
4. **Investigation conditions:** warning bands, noncritical breaches, drift, exceptions nearing expiry, or composite below floor -> `INVESTIGATE`.
5. **Pass recommendation:** only when every named gate and required threshold is satisfied -> `PASS_RECOMMENDATION`.

The tool recommends routing; the accountable owner or approved control authorizes release.

### Composite scores

If a composite is useful for ranking and trend:

```text
composite = sum(weight_i * approved_measure_i) / sum(applicable weights)
```

Rules:

- document weights, direction, missing-measure treatment, and version;
- show dimension/CDE components alongside the composite;
- exclude `NOT_APPLICABLE` only under a documented denominator rule;
- never convert `NOT_EVALUATED` to a passing value;
- never allow the composite to override a hard gate;
- do not compare composites across materially different rule or weight versions without restatement.

## 13. Reconciliation and transformation integrity

### Reconciliation chain

Reconcile at each boundary:

```text
source reported population
-> records received
-> accepted + rejected + quarantined
-> transformed outputs + documented exclusions
-> published population
-> consumer-received population
```

### Required controls

| Control | Test |
|---|---|
| File/batch receipt | Expected deliveries vs received, including zero-record declarations |
| Record count | Source vs landed vs accepted/rejected/quarantined |
| Key count | Distinct keys and duplicates across stages |
| Control total | Approved numeric or categorical totals across transformations where meaningful |
| Partition coverage | Expected time/source partitions vs available complete partitions |
| Join integrity | Row and distinct-entity counts before/after join; unmatched and multi-match counts |
| Filter accounting | Every excluded record maps to a named filter and reason |
| Aggregation | Output totals tie to eligible inputs under stated grain |
| Reference join | Match, no-match, multi-match, expired-reference, and future-reference rates |
| Consumer receipt | Published manifest vs consumer acknowledgement where available |
| Historical rewrite | Prior output hash/count vs current, with authorized backfill/restatement record |

### Reconciliation status

- `PASS`: totals tie exactly or within an explicitly approved, explained tolerance.
- `PASS_WITH_EXPLAINED_VARIANCE`: variance is expected, quantified, approved, and evidenced.
- `FAIL`: unexplained variance exceeds zero or the approved tolerance.
- `NOT_TESTABLE`: required source/target total or lineage is unavailable.

Do not force totals to tie by dropping duplicates, nulls, rejects, or late arrivals. Show each bridge component.

### Join explosion controls

- Profile uniqueness of both join sides at the join key before joining.
- Declare expected cardinality: one-to-one, one-to-many, many-to-one, or approved many-to-many.
- Compare row count, distinct primary entity count, and key multiplicity before and after.
- Aggregate the many side to intended grain when required.
- Identify orphaned left keys and unconsumed right keys.
- Trace a sample of records through the join.
- Block release on unexpected many-to-many expansion affecting material measures.

## 14. Schema and semantic drift

### Drift events

Detect and inventory:

- fields added, removed, renamed, reordered where relevant, or retyped;
- nullability or default changes;
- precision, scale, unit, encoding, delimiter, or timezone changes;
- key, grain, population, or effective-date changes;
- new, removed, or redefined controlled values;
- altered nesting, arrays, or cardinality;
- shifted null, sentinel, category, or distribution patterns;
- changed delivery time, partitioning, correction, or late-arrival behavior;
- changed transformation, rule, threshold, reference, or model version.

### Drift response

1. Capture old/new schema and semantic diff.
2. Classify compatibility and affected CDEs/critical transformations.
3. Identify downstream consumers through lineage.
4. Quarantine or shadow-run breaking changes.
5. Notify accountable owners and registered consumers through approved channels.
6. Update contract, mappings, rules, tests, documentation, and training material.
7. Backtest and reconcile old vs new outputs.
8. Obtain approval and record rollback.
9. Deploy under staged monitoring.
10. Close only after consumer acceptance and post-deployment evidence.

No assistant should autonomously accept a breaking change or rewrite a consumer contract.

## 15. Duplicate detection and entity resolution

### Keep three problems separate

1. **Duplicate row:** the same source event/record was delivered or loaded more than once.
2. **Duplicate record:** multiple records represent the same source-level object contrary to declared grain.
3. **Entity resolution:** different records may refer to the same real-world entity.

An exact row deduplication rule cannot solve entity resolution; an entity match does not prove one record should be deleted.

### Normalization

Create derived comparison values with versioned rules for Unicode, case, whitespace, punctuation, transliteration, address structure, phone formats, dates, and identifiers. Preserve source values. Measure how normalization changes collision and uniqueness rates.

### Candidate-generation and comparison pattern

1. Use documented blocking keys or retrieval logic to generate candidates.
2. Compare approved attributes with named algorithms or deterministic rules.
3. Account for missingness, contradictory identifiers, effective dates, and source reliability.
4. Produce attribute-level evidence and an overall confidence or rule outcome.
5. Apply explicit thresholds for match, possible match, and non-match.
6. Route ambiguous or consequential matches to human review.
7. Preserve accepted, rejected, and unresolved candidate links with reviewer evidence.

### Merge and survivorship controls

- Do not auto-merge on name similarity alone.
- Treat a shared identifier with contradictory core attributes as a collision requiring review.
- Define field-level survivorship by source authority, recency, verification, and effective date; do not use “most complete wins” without qualification.
- Preserve provenance for every golden-record value.
- Keep source records and historical links after consolidation.
- Make split/unmerge possible and tested.
- Re-run downstream aggregation and screening/control logic after a merge or split.
- Record who approved the decision and why.

### Entity-resolution measures

Where labeled evidence exists, report precision, recall, false-match rate, missed-match rate, unresolved rate, cluster purity, and performance by relevant strata. Where it does not, report reviewed-sample results and uncertainty; do not call a similarity score “accuracy.”

## 16. Exceptions and waivers

### Exception policy

An exception is a time-bounded, approved departure from a rule or threshold. It does not change the underlying quality result.

Required fields:

```yaml
exception_id: <stable id>
rule_or_contract_id: <id/version>
affected_population: <exact scope>
defect_condition: <observed condition>
business_justification: <why temporary acceptance is requested>
risk_and_impact: <downstream consequence>
root_cause_status: <known/under-investigation>
compensating_controls: [<control, owner, evidence, frequency>]
remediation_plan: <milestones and owner>
requested_by: <role>
approved_by: <authorized role/reference>
effective_from: <date/time>
expires_at: <date/time>
review_cadence: <cadence>
status: <requested/approved/rejected/expired/closed/revoked>
closure_evidence: <reference or null>
```

Controls:

- An exception cannot convert a failed rule result to a pass; reporting shows `BREACH_WITH_APPROVED_EXCEPTION`.
- Scope exceptions narrowly by product, field, population, and time.
- Require a compensating control where risk remains material.
- Prevent automatic renewal; expiry triggers re-review or removal from use.
- Track cumulative and repeated exceptions as a systemic-risk indicator.
- Revoke an exception when assumptions, impact, or compensating controls change.
- Validate remediation independently before closure.

## 17. Data-quality issues and incidents

### Issue vs incident

- A **defect** is a failed record or rule observation.
- An **issue** is a grouped condition requiring ownership and remediation.
- An **incident** is an issue with material actual or potential operational, reporting, legal, regulatory, security, privacy, or external impact requiring coordinated response.

### Issue record

| Field | Required content |
|---|---|
| `issue_id` | Stable identifier |
| `detected_by` / `detected_at` | Rule, reconciliation, review, consumer, or incident source |
| `products/CDEs/rules` | Affected governed objects and versions |
| `population/time_window` | Count, rate, segments, and period |
| `condition/evidence` | What failed and how established |
| `severity/confidence` | Separate assessments and basis |
| `downstream_impact` | Products, reports, decisions, controls, and consumers |
| `containment` | Holds, warnings, alternative source, or use restrictions |
| `owner` | Accountable role |
| `root_cause` | Confirmed cause or investigation state |
| `remediation` | Corrective and preventive actions |
| `status/age` | Controlled lifecycle and elapsed time |
| `validation` | Independent retest evidence |
| `closure` | Approver and closure basis |

### Severity principles

Classify according to actual/potential impact, affected population, CDE criticality, duration, detectability, reversibility, external exposure, and control failure. Do not set universal response times here; the adopting organization must map severity to approved clocks and notification obligations.

### Incident lifecycle

1. Detect and preserve evidence.
2. Triage severity, confidence, scope, and required responders.
3. Contain use or distribution without destroying evidence.
4. Identify affected products, consumers, reports, decisions, and periods through lineage.
5. Notify under approved incident and disclosure procedures.
6. Diagnose root cause; distinguish trigger, contributing factors, and control failures.
7. Correct source or transformation under change control.
8. Backfill, restate, or reprocess only with approval and reconciliation.
9. Validate the fix independently on affected and boundary populations.
10. Obtain consumer confirmation where outputs changed.
11. Close with evidence, residual risk, and preventive actions.
12. Monitor recurrence and overdue actions.

Do not delete failed data to make a dashboard green. Preserve the original run, correction, and impact bridge.

## 18. Control design and evidence

### Control specification

| Field | Required content |
|---|---|
| `control_id/version` | Stable, versioned control |
| `objective` | Risk the control mitigates |
| `type` | Preventive, detective, corrective; manual, automated, hybrid |
| `trigger/frequency` | When and how often it operates |
| `population` | Complete population and exclusions |
| `procedure` | Exact steps, rules, and decision points |
| `evidence` | Inputs, logs, outputs, approvals, and retention |
| `owner/operator/reviewer` | Segregated roles where required |
| `threshold/escalation` | Decision logic and route |
| `failure_mode` | How failure becomes visible and is contained |
| `dependencies` | Sources, references, jobs, models, and access |
| `change/rollback` | Controlled modification and reversal |

### Control evidence package

At minimum retain:

- scope and population manifest;
- source/input identifiers and hashes;
- executed rule/control versions;
- parameters, thresholds, reference versions, and effective dates;
- record-level defects or protected pointers;
- aggregate scorecard and reconciliation;
- exceptions and approvals;
- technical logs and failures;
- reviewer tests and results;
- output/report hash;
- release or hold decision;
- remediation and closure evidence.

Evidence must show that the control operated, not only that it was scheduled or configured.

## 19. Monitoring and dashboards

Dashboards should support action and audit, not decorate the process. Use conventional professional layouts, restrained color, direct labels, and accessible tables. Never rely on color alone.

### Minimum dashboard sections

1. Scope, as-of time, last complete period, contract/rule version, and data freshness.
2. Overall disposition and hard-gate status.
3. CDE and critical-transformation scorecard.
4. Dimension measures with numerator, denominator, rate, threshold, prior period, and baseline.
5. Reconciliation status and unexplained variance.
6. Defect clusters by source, rule, segment, age, and owner.
7. Open issues, incidents, exceptions, and expiring waivers.
8. Schema/semantic drift and recent changes.
9. Not-evaluated population and source/access gaps.
10. Downstream impact and blocked/restricted consumers.

### Metrics

- rule coverage: applicable rules executed / applicable rules;
- CDE coverage: CDEs with current passing tests / governed CDEs;
- evaluated population rate;
- defect count and defect rate by rule/dimension/segment;
- critical-breach count and affected population;
- reconciliation pass rate and absolute variance;
- freshness and delivery adherence;
- issue age, time to detection, time to containment, time to validated closure;
- repeat-defect and recurrence rate;
- exception count, age, concentration, and upcoming expiry;
- schema drift count and unapproved-change count;
- lineage coverage and unowned-product count;
- downstream products restricted by quality state.

### Dashboard controls

- show source, calculation, owner, as-of date, and refresh status for each KPI;
- distinguish zero from missing and not evaluated;
- allow drill-through to protected evidence references, not necessarily raw sensitive rows;
- reconcile visible totals to the run manifest;
- preserve historical values under their original rule/baseline versions;
- annotate incidents, migrations, backfills, and contract changes;
- test filters, exports, links, and role-based access if implemented;
- never claim real-time operation unless the source and refresh evidence support it.

## 20. Testing strategy

### Rule-level tests

- positive fixture: known valid records pass;
- negative fixture: each named defect fires;
- boundary fixture: exact threshold, date, precision, length, and range edges;
- null/sentinel fixture: every missing-state semantic;
- precedence fixture: overlapping rules produce the intended causal outcome;
- reference fixture: active, expired, future, missing, and duplicated reference values;
- determinism fixture: same inputs and versions produce identical results.

### Pipeline tests

- full-population receipt and reconciliation;
- schema and semantic compatibility;
- partition and late-arrival behavior;
- join cardinality and orphan handling;
- rejected/quarantined population accounting;
- idempotent rerun and recovery from checkpoints;
- backfill, restatement, and historical version behavior;
- rollback to prior schema/rule/configuration;
- permissions, masking, and retention enforcement;
- failure injection for unavailable sources, corrupt inputs, stale references, and write failures.

### Outcome validation

Where labels exist, use an independent test set and report confusion matrices, precision, recall, error rates, segment performance, and confidence bounds. For deterministic rules, plant every critical defect class and require observed detection. For model-assisted checks, test prompt/model/version changes, adversarial inputs, nondeterminism, unsupported assertions, and protected-data leakage.

### Sampling

If the population is not fully tested:

- define sampling objective, frame, unit, confidence, tolerable rate, expected rate, and selection method;
- use reproducible random or stratified selection when making population inferences;
- label risk-based additions separately and do not project their defect rate to the population;
- record seed or selection evidence;
- use exact or appropriate confidence bounds;
- account for clustering and finite populations;
- preserve the selection log and all deviations;
- obtain human judgment on the control conclusion.

### Regression pack

Retain a versioned, non-sensitive fixture set covering every rule, critical transformation, known incident pattern, schema version, and prior defect. A change may add fixtures; deleting or weakening one requires explicit approval and rationale.

## 21. Deployment patterns and release gates

### Patterns

| Pattern | Purpose | Quality action |
|---|---|---|
| Observe-only profile | Establish baseline without affecting flow | Report only; no operational gate |
| Shadow rules | Compare proposed rules to current process | Measure differences; human reviews false positives/negatives |
| Batch pre-ingestion gate | Hold a delivered batch before downstream use | Reconcile, test CDEs, route pass/investigate/hold |
| Quarantine lane | Isolate invalid records while retaining full accounting | Downstream use only if policy permits partial populations and impact is explicit |
| In-pipeline test | Stop a transformation or publication on breach | Fail visibly; preserve run and defect evidence |
| Consumer warning | Product remains accessible with documented limitation | Authorized exception, visible caveat, expiry, monitoring |
| Dual-run migration | Old and new logic run in parallel | Reconcile outputs and investigate deltas before cutover |
| Post-publication monitor | Detect drift or delayed defects | Incident/restatement process; never rewrite history silently |

### Promotion sequence

1. Approve concept, owner, intended use, and risk tier.
2. Complete inventory, contract, CDE, lineage, and control design.
3. Implement rules with unit and negative tests.
4. Backtest against historical and adversarial fixtures.
5. Run in shadow and quantify differences.
6. Obtain independent validation and consumer readiness.
7. Approve change, rollback, incident route, and support model.
8. Deploy to limited scope under heightened monitoring.
9. Reconcile results and confirm no unintended population change.
10. Expand only after release gates pass.

### Release gates

- approved contract and ownership;
- complete and reconciled input population;
- current reference data and rule versions;
- all critical rules evaluated;
- no unresolved hard-gate breach;
- exceptions approved, scoped, evidenced, and unexpired;
- regression, integration, and rollback tests pass;
- downstream consumers informed and ready;
- monitoring and incident response active;
- independent QA and accountable-owner sign-off recorded.

## 22. Administrative and security controls

### Access

- least privilege by product, field, environment, and action;
- separate read, transform, approve, and release permissions;
- periodic access review and timely revocation;
- service identities with attributable ownership;
- no shared credentials in code, prompts, logs, or artifacts;
- break-glass access separately approved, time-bounded, and reviewed.

### Configuration

- version schemas, contracts, rules, thresholds, weights, references, mappings, and prompts;
- prohibit unreviewed runtime edits to production configuration;
- validate configuration syntax and semantic compatibility before deployment;
- compare deployed configuration to approved state;
- retain diff, approver, effective date, and rollback reference.

### Logging and observability

Log run ID, scope, source versions, record counts, rule versions, outcomes, failures, duration, and approval state. Avoid logging raw sensitive values where protected references suffice. Monitor missing runs, stale data, repeated fallbacks, unexplained volume changes, rising not-evaluated rates, control bypass attempts, and failed evidence persistence.

### Retention and disposal

Apply approved retention to source receipts, derived records, defects, reports, logs, and evidence packages. A derived copy does not escape the source's restrictions. Suspend disposal under applicable hold. Record authorized deletion or anonymization; do not use deletion to conceal a failed run.

## 23. Run manifest and reproducibility

```json
{
  "run_id": "<id>",
  "assessment_type": "<profile|rule-run|reconciliation|validation|monitoring>",
  "data_product_id": "<id>",
  "contract_version": "<version>",
  "scope": {"population": "<definition>", "period": "<bounds>", "timezone": "<zone>"},
  "source_inputs": [
    {"id": "<source/version>", "hash": "<hash>", "records": 0, "status": "<status>"}
  ],
  "code_query_config": {
    "repository_or_reference": "<reference>",
    "revision": "<revision>",
    "dirty_or_uncommitted": "<true/false/unknown>",
    "rule_catalog_version": "<version>",
    "reference_versions": ["<id/version>"]
  },
  "parameters": {"<name>": "<value>"},
  "environment": {"runtime": "<version>", "platform": "<value>", "dependencies": ["<locked versions>"]},
  "started_at_utc": "<ISO 8601>",
  "completed_at_utc": "<ISO 8601>",
  "record_counts": {"expected": 0, "received": 0, "evaluated": 0, "not_evaluated": 0, "rejected": 0, "quarantined": 0},
  "reconciliation_status": "<PASS|PASS_WITH_EXPLAINED_VARIANCE|FAIL|NOT_TESTABLE>",
  "hard_gate_status": "<PASS|BREACH|NOT_EVALUATED>",
  "disposition": "<PASS_RECOMMENDATION|INVESTIGATE|BLOCK_OR_HOLD|HOLD_NOT_RECONCILED|HOLD_NOT_EVALUATED>",
  "exceptions": ["<ids>"],
  "issues": ["<ids>"],
  "output_hashes": {"<artifact>": "<hash>"},
  "review": {"status": "<state>", "evidence": "<reference>"}
}
```

Reproduction requires the manifest, accessible versioned inputs, executable logic, parameters, locked environment, and a documented command or workflow. If source data cannot be retained, retain an approved immutable reference and enough protected evidence for independent reperformance.

## 24. Output contract

### Data-quality assessment

```markdown
# Data Quality Assessment — <data product> — <as of>

## Disposition
<named disposition, hard-gate basis, approver required>

## Intended Use, Grain, and Population
<purpose, one-record definition, inclusions/exclusions, period, timezone>

## Source and Contract
<source versions, contract version, delivery status, CDEs, critical transformations>

## Reconciliation
<expected/received/evaluated/rejected/quarantined/published bridge and unexplained variance>

## Critical Findings
<rule, CDE, failed/evaluated counts, rate, threshold, segments, evidence, impact, severity, confidence>

## Dimension Scorecard
<numerator, denominator, rate, threshold, baseline, prior period, status>

## Drift and Change
<schema, semantic, distribution, reference, rule, or lineage changes>

## Downstream Impact
<affected consumers, reports, decisions, models, and controls>

## Open Issues, Incidents, and Exceptions
<owners, age, expiry, containment, remediation, evidence>

## Recommended Controls and Remediation
<smallest useful fix, automated tests, owner, validation requirement>

## Methods, Assumptions, and Limitations
<rules, thresholds, not-evaluated population, unavailable evidence>

## Reproducibility and Evidence
<manifest, input/code/reference versions, queries/notebooks/scripts, output hashes>

## Review and Sign-off
<operator, owner, independent reviewer, release decision>
```

### Finding row

| Field | Required content |
|---|---|
| Rule/CDE | Named, versioned rule and critical element |
| Failure | Plain description of what failed |
| Evidence | Counts, rates, segments, dates, and protected record references |
| Denominator | Eligible, evaluated, excluded, and not-evaluated populations |
| Threshold | Approved warning/breach values and comparison logic |
| Impact | Downstream use and consequence |
| Severity/confidence | Separate, with basis |
| Cause | Confirmed cause or clearly labeled hypothesis |
| Remediation | Owner, action, due date, validation requirement |
| Status | Open, contained, remediating, validation, closed |

## 25. Copy-ready operating prompt

```text
You are operating the Data Quality and Governance standard.

OBJECTIVE
Determine whether the stated data product is fit for its explicitly stated use. Build traceable evidence, not a cosmetic score. Do not repair source data, approve exceptions, release blocked data, merge entities, or claim unavailable capabilities.

INPUTS
- Data product and owner: <id/name/roles>
- Intended use and prohibited uses: <uses>
- Grain and population: <one-record definition, inclusions/exclusions>
- Period, cutoff, and timezone: <values>
- Source inputs and versions: <references>
- Contract/schema: <reference/version>
- CDE and critical-transformation register: <references or request to draft>
- Rule catalog and approved thresholds: <references>
- Reference data versions: <references>
- Prior baseline/run: <references>
- Downstream consumers: <list>
- Available tools/data access: <actual capabilities only>
- Output audience/handling: <requirements>

METHOD
1. Inventory the product, source, owner, consumer, grain, population, keys, time semantics, classification, retention, and delivery behavior.
2. Confirm CDEs and critical transformations against consequence. Flag missing designations; do not invent owner approval.
3. Compare the delivered physical and semantic schema to the approved contract. Classify drift and affected consumers.
4. Profile the population: counts, keys, null/sentinel rates, distinct values, timestamps, domains, distributions, join coverage, duplicates, and partitions. Segment by relevant source/time/population dimensions.
5. Reconcile expected -> received -> accepted/rejected/quarantined -> transformed -> published populations. Test key counts, partitions, filters, joins, aggregates, and material control totals.
6. Execute only named, versioned rules. For each rule report eligible, evaluated, passed, failed, excluded, and not-evaluated counts; numerator, denominator, rate, threshold, and evidence.
7. Assess completeness, accuracy where a valid reference exists, validity, consistency, uniqueness, timeliness, integrity, conformity, volume/shape, and lineage.
8. Apply gates in order: population/reconciliation, critical breach, critical evaluability, investigation conditions, then pass recommendation. Never let a composite override a gate.
9. Detect schema, semantic, volume, sparsity, category, distribution, rule, reference, and lineage drift against the governed baseline.
10. Keep duplicate rows, duplicate records, and entity resolution separate. Preserve source values and route ambiguous merges to human review.
11. Identify downstream impact through lineage. Distinguish confirmed cause from hypothesis.
12. Inventory open issues, incidents, and exceptions. An exception does not change a failed rule result and must show owner, compensating control, expiry, and approval.
13. Recommend the smallest material remediation and stable automated tests. Do not hard-code a new policy threshold without owner approval.
14. Create a reproducibility manifest with source hashes/versions, code/query/config revision, rule/reference versions, parameters, environment, counts, status, and output hashes.
15. Apply independent QA under the universal QA standard and state required human gates.

OUTPUT
A. Disposition and named gate basis
B. Intended use, grain, population, scope, period, and timezone
C. Inventory, contract, CDEs, critical transformations, and lineage gaps
D. Source-to-published reconciliation bridge
E. Rule and CDE findings with counts, rates, thresholds, evidence, impact, severity, confidence, and cause status
F. Dimension scorecard and not-evaluated population
G. Schema/semantic/distribution drift and change impact
H. Duplicate/entity-resolution assessment
I. Issues, incidents, exceptions, ownership, aging, and containment
J. Remediation, automated tests, deployment gate, and rollback
K. Assumptions, limitations, gaps, and unavailable checks
L. Reproducibility manifest, evidence index, QA result, and sign-off required

Use PASS_RECOMMENDATION only when every named gate and required threshold is satisfied. If the population cannot be reconciled or a critical rule cannot be evaluated, hold the disposition and explain the affected scope.
```

## 26. Copy-ready operational templates

### Defect-to-issue bridge

```yaml
issue_id: <id>
data_product: <id/version>
rules: [<ids/versions>]
cdes: [<ids>]
first_detected_run: <run id>
affected_period: <bounds>
eligible_records: <count>
evaluated_records: <count>
failed_records: <count>
affected_rate: <rate>
not_evaluated_records: <count>
segments: [<affected segments>]
reconciliation_status: <status>
severity: <tier and basis>
confidence: <HIGH/MODERATE/LOW/NOT ASSESSABLE and basis>
downstream_consumers: [<ids>]
containment: <action/status>
owner_role: <role>
root_cause: <confirmed cause or hypothesis label>
remediation: <plan>
validation_required: <tests>
status: <state>
```

### Change record

```yaml
change_id: <id>
objects_changed: [<schema/contract/rule/threshold/reference/mapping/model ids>]
old_versions: [<versions>]
new_versions: [<versions>]
reason: <reason>
compatibility: <backward-compatible/breaking/unknown>
cdes_affected: [<ids>]
consumers_affected: [<ids>]
data_impact: <population/history/backfill effect>
test_evidence: [<references>]
parallel_run_reconciliation: <reference/status>
rollback: <steps/version>
requested_by: <role>
reviewed_by: <roles>
approved_by: <authority/reference>
effective_at: <date/time>
post_deployment_checks: [<checks>]
status: <proposed/approved/deployed/rolled_back/closed>
```

### Release decision

```yaml
run_id: <id>
disposition_recommended: <value>
reconciliation_gate: <pass/fail/not-testable>
critical_rule_gate: <pass/breach/not-evaluated>
exceptions: [<approved exception ids>]
residual_risk: <statement>
affected_consumers: [<ids>]
owner_decision: <release/hold/restrict/reject/pending>
approver_role: <role>
approval_reference: <reference or null>
decision_at: <date/time or null>
conditions: [<conditions>]
```

## 27. Completion checklist

- [ ] Intended use, prohibited uses, grain, population, period, cutoff, and timezone are explicit.
- [ ] Product, owner, steward, producer, consumers, classification, retention, and lifecycle are inventoried.
- [ ] Keys, null semantics, delivery behavior, and completeness signal are defined.
- [ ] CDEs and critical transformations have consequence-based rationales and owners.
- [ ] A versioned producer-consumer contract exists or its absence is a finding.
- [ ] Business, technical, operational, and proportionate record lineage are assessed.
- [ ] Profiling covers counts, keys, nulls, domains, timestamps, distributions, joins, duplicates, and partitions.
- [ ] Every rule has version, population, logic, numerator, denominator, exclusions, threshold, owner, evidence, and effective date.
- [ ] Accuracy claims use an appropriate reference; validity is not mislabeled accuracy.
- [ ] Expected, received, evaluated, rejected, quarantined, transformed, published, and consumer-received populations reconcile.
- [ ] Join cardinality, filter accounting, and historical rewrites are tested.
- [ ] `NOT_EVALUATED` and `NOT_APPLICABLE` are not reported as pass.
- [ ] Hard gates execute before composite/pass logic.
- [ ] Schema and semantic drift are impact-assessed and governed.
- [ ] Duplicate rows, duplicate records, and entity resolution remain distinct.
- [ ] Ambiguous merge, survivorship, and split decisions are human-reviewed and reversible.
- [ ] Exceptions are approved, scoped, compensated, monitored, and time-bounded.
- [ ] Issues and incidents show population, downstream impact, containment, owner, remediation, and validation.
- [ ] Dashboard values reconcile to the evidence manifest and distinguish zero/missing/not evaluated.
- [ ] Unit, negative, boundary, integration, reconciliation, regression, failure, and rollback tests exist.
- [ ] Deployment, monitoring, incident, consumer-notification, and rollback plans are approved.
- [ ] Source, code, query, configuration, reference, environment, parameter, count, and output provenance are retained.
- [ ] Independent QA and accountable-owner sign-off are complete before release.
