# Evidence and Research Operating Standard

Version: 1.0
Status: public, tool-agnostic operating standard
Applies to: open-source research, regulatory intelligence, due diligence, investigations support, market and policy research, entity research, and evidence-backed analytical reporting
Does not authorize: access-control circumvention, collection of non-public data, legal determinations, regulatory filings, account restrictions, employment action, or other consequential decisions

## 1. Purpose

This standard turns a research request into a reviewable evidence package. It governs the full chain from question design through source discovery, capture, analysis, quality assurance, and handoff.

The controlling rule is simple:

> A material statement is a claim. A claim is usable only when a reviewer can identify the source, relocate the cited material, understand what it establishes, see how the subject was matched, and reproduce the analyst's reasoning.

This is a research standard, not a truth machine. Public records can be incomplete, delayed, erroneous, amended, sealed, mistranslated, or removed. Search tools can omit results. Automated extraction can corrupt context. Human review is mandatory at the decision gates defined below.

## 2. Scope and operating boundaries

### 2.1 Permitted inputs

- Lawfully accessible public websites, publications, registers, filings, datasets, APIs, and archives.
- Materials supplied by an authorized user for the defined assignment.
- Licensed sources only where the operator is independently authorized and the output respects the applicable license.
- Public ledger observations for blockchains, separated from third-party address labels.

### 2.2 Prohibited or constrained methods

- Do not defeat authentication, paywalls, rate limits, robots controls, technical safeguards, or access restrictions.
- Do not misrepresent identity, pretext, phish, solicit confidential information, or contact a subject without explicit authorization.
- Do not obtain or redistribute stolen credentials, unlawfully obtained personal data, doxxing collections, or bulk sensitive-person data.
- Do not treat a search snippet, generated summary, knowledge panel, chatbot answer, or unsourced database row as evidence.
- Do not embed watchlist records, customer records, personal identifiers, or bulk personal data in a public output. Link to the official list or describe the method.
- Do not automate a legal, sanctions, reporting, offboarding, hiring, credit, or disciplinary decision. Route consequential action to an authorized human.
- Do not infer absence from one failed query, one inaccessible source, or one spelling.

### 2.3 Data minimization

Collect only attributes needed to answer the approved question. Mask or omit unnecessary personal identifiers from reports. Keep raw captures with restricted access when they contain sensitive data, and publish only aggregate methods, source links, schemas, and synthetic examples.

## 3. Non-negotiable evidence rules

1. **Start with a decision question.** Define the question, subject, period, jurisdiction, and intended use before searching.
2. **Prefer the source of the act.** Use the issuing authority, registry of record, court, legislature, company filing, statistical agency, or ledger before commentary about it.
3. **Resolve the party before attaching the fact.** A name match is not an identity match.
4. **Separate evidence states.** Mark information as observed, officially reported, alleged, adjudicated, estimated, inferred, projected, disputed, or unknown.
5. **Capture provenance at retrieval.** A URL without retrieval time and cited location is not a complete source record.
6. **Preserve time.** Record publication, effective, event, amendment, and retrieval dates separately.
7. **Corroborate according to consequence.** The higher the consequence or ambiguity, the stronger the required source and independence.
8. **Search against the hypothesis.** Run disconfirming, resolution, appeal, correction, and later-outcome searches.
9. **Expose gaps.** Missing, inaccessible, stale, or conflicting evidence is part of the result.
10. **Require human judgment at gates.** Automation may collect, normalize, compare, and draft; an accountable reviewer approves material conclusions and actions.

## 4. Roles and separation of duties

| Role | Minimum responsibility | May not silently do |
|---|---|---|
| Request owner | Defines the decision, scope, permissible sources, deadline, sensitivity, and recipient | Convert an exploratory scan into a consequential decision without review |
| Researcher | Plans queries, gathers sources, captures provenance, resolves entities, and maintains the ledgers | Suppress contradictory evidence or upgrade a lead without support |
| Analyst | Converts evidence into bounded claims, alternatives, confidence, and implications | Treat model output as a source or conceal assumptions |
| Reviewer | Re-performs material samples, challenges identity and inference, checks citations and dates | Approve their own high-consequence conclusion where independence is required |
| Decision owner | Applies law, policy, risk appetite, and authority to the evidence package | Delegate accountable judgment to the research system |
| Records owner | Applies retention, access, legal-hold, privacy, and deletion requirements | Place restricted evidence in a public repository |

One person may hold multiple roles for low-risk work. Record the overlap. High-consequence work should use a second-person review.

## 5. Evidence classes, source tiers, and confidence

### 5.1 Evidence-state vocabulary

Use these terms exactly in working papers and outputs.

| State | Meaning | Permitted formulation |
|---|---|---|
| OBSERVED | Directly visible in a captured primary record or reproducible dataset | “The filing states…”; “The ledger records…” |
| OFFICIALLY REPORTED | An authority reports an event but the record is not itself the adjudication | “The authority announced…” |
| ALLEGED | A complaint, charge, claim, investigation, or sourced accusation not finally adjudicated | “The complaint alleges…” |
| ADJUDICATED | A final judgment, order, plea, conviction, or other recorded resolution, subject to stated appeal status | “The court held…”; “The respondent settled without admitting…” |
| ESTIMATED | Derived from a stated method and inputs | “The estimate is…, using…” |
| INFERRED | Reasoned conclusion from evidence that does not state the conclusion directly | “The evidence supports an inference…” |
| PROJECTED | Forward-looking result conditional on assumptions | “Under the base case…” |
| SPECULATIVE | A hypothesis or pattern-based claim for which direct evidence is not yet sufficient | “Hypothesis for testing: …”; never present as a finding |
| DISPUTED | Credible sources materially conflict or a relevant party contests the proposition | “Sources disagree…” |
| UNKNOWN | Evidence is unavailable, inaccessible, ambiguous, or insufficient | “Not established by the reviewed sources.” |

Never collapse **charged**, **liable**, **convicted**, **settled**, **dismissed**, and **acquitted** into “involved in wrongdoing.” Record procedural posture and later disposition.

### 5.2 Source tiers

| Tier | Definition | Examples | Reliance rule |
|---|---|---|---|
| T1 — authoritative primary | The body legally or operationally responsible for the record or act | Official list, statute, gazette, court docket, regulator order, registry of record, issuer filing, statistical agency, public ledger | May support a claim after identity, currency, scope, and record-status checks |
| T2 — accountable secondary | A source with named ownership/editorial responsibility, transparent methods, and a correction path | Established wire service, peer-reviewed research, recognized investigative consortium, reputable professional body | May corroborate or support context; seek T1 for the underlying act when available |
| T3 — discovery source | An index, aggregator, structured lead source, search engine, crowd contribution, explorer label, or unattributed compilation | Search results, public aggregators, wikis, social posts, community labels | Lead only unless independently corroborated; cite the underlying source, not the discovery layer |
| TX — excluded from evidentiary reliance | No inspectable provenance, fabricated or circular citations, manipulated content, deceptive domain, unlawfully obtained data, or material integrity failure | Generated prose without sources, content farm, impersonation site, scraped mirror with no origin | Do not cite or rely; retain only an exclusion log if relevant |

Tier describes authority for a specific proposition, not prestige in general. A company website is T1 for its own published policy, T2 or T3 for claims about competitors, and not independent corroboration of itself. A regulator press release is T1 for what the regulator announced; the filed order is stronger for the order's terms.

### 5.3 Confidence labels

Confidence applies to a claim, not to a document as a whole.

| Label | Minimum basis | Typical constraint |
|---|---|---|
| HIGH | Correctly resolved subject; controlling T1 record or multiple independent sources including T1; no material unresolved contradiction | Still bounded to the record's date and scope |
| MODERATE | Resolved subject; one credible primary source or convergent independent secondary evidence; material caveat remains | Partial coverage, single-source dependence, or uncertain interpretation |
| LOW | Identity, completeness, independence, translation, or source quality is materially weak | Not a sound basis for consequential action |
| NOT ASSESSABLE | Evidence is too incomplete, conflicting, or unreliable to assess confidence responsibly | Use an `UNRESOLVED` disposition and state the collection or decision gap |

Do not compute confidence from source count alone. Ten copied stories are one information lineage. State the reason after the label.

### Claim dependency and correction propagation

For a material claim, preserve the source lineage and list downstream findings,
calculations, and decisions that depend on it. Corroborating sources are independent
only when their underlying observation is independent; mirrored filings, translated
copies, and syndicated reports remain one lineage. Capture disagreement at the exact
claim level instead of averaging source reputations.

If a source is corrected, withdrawn, or shown to identify a different subject, mark the
claim superseded or unresolved and reassess its dependents. Keep the historical record
and the prior as-of conclusion. Do not silently rewrite an issued artifact; produce a
versioned correction and apply the existing release and distribution gates.

## 6. Research lifecycle and decision gates

The required sequence is:

`intake -> scope -> identity brief -> query plan -> discovery -> source qualification -> capture -> extraction -> claim mapping -> corroboration/challenge -> QA -> human approval -> handoff`

### Gate G0 — authority and scope

Before collection, a human confirms:

- the purpose and intended decision;
- subjects and jurisdictions in scope;
- permitted and prohibited source classes;
- required lookback and as-of date;
- legal, privacy, licensing, and retention constraints;
- materiality and escalation thresholds;
- output audience and deadline.

If authority is unclear, stop. Do not broaden the subject set, collect sensitive data, or contact anyone.

### Gate G1 — research-plan approval

Before high-volume collection, a human confirms that the entity brief, issue tree, source map, query families, and stopping rules fit the question. Low-risk one-off work may combine G0 and G1, but record that choice.

### Gate G2 — identity resolution

Before associating adverse, watchlist, enforcement, litigation, or ownership information with the subject, a human reviews the identity scorecard. Name-only or address-only matches remain `POSSIBLE_MATCH`; they cannot become findings.

### Gate G3 — material-claim review

Before a material claim enters the final output, a human checks the cited location, evidence state, subject match, temporal status, corroboration, counterevidence, and wording.

### Gate G4 — consequential-action boundary

Before filing, freezing, rejecting, escalating externally, notifying a subject, or making a legal or employment decision, an authorized decision owner applies governing policy and law. The research package informs; it does not decide.

### Gate G5 — release and retention

Before distribution, a human confirms audience, classification, redaction, copyright limits, link integrity, quality-control completion, and the appropriate retained record.

## 7. Intake and problem framing

### 7.1 Mandatory research brief

Record:

```yaml
research_id: R-YYYYMMDD-NNN
request_received_at: YYYY-MM-DDThh:mm:ssZ
request_owner: role_or_team
decision_question: one answerable sentence
intended_use: descriptive purpose; no implied authority
subjects:
  - subject_id: SUB-001
    type: person|organization|asset|event|jurisdiction|topic
    supplied_identifiers: []
jurisdictions: []
domains: []
time_scope:
  event_from: YYYY-MM-DD|null
  event_to: YYYY-MM-DD|null
  as_of: YYYY-MM-DDThh:mm:ssZ
lookback_logic: explicit rule
materiality_rule: explicit rule
allowed_sources: public and authorized sources
excluded_sources: []
sensitivity: public|internal|restricted
review_level: self_check|second_person|specialist
deadline: YYYY-MM-DDThh:mm:ssZ
known_constraints: []
out_of_scope: []
```

### 7.2 Convert the request into an issue tree

Break the decision question into mutually understandable sub-questions. For entity work, the default issue tree is:

1. **Identity:** Who or what is the subject?
2. **Legal existence and control:** Where is it registered; who owns, manages, or controls it?
3. **Status:** What licenses, listings, sanctions, restrictions, insolvency states, or public-office roles apply?
4. **Conduct and events:** What relevant acts, allegations, findings, transactions, or changes are recorded?
5. **Exposure and relationships:** What counterparties, jurisdictions, assets, or networks are materially connected?
6. **Time:** What was true at the decision's as-of date, and what changed afterward?
7. **Counterevidence:** What evidence weakens the main hypothesis or resolves prior concerns?
8. **Gaps:** What cannot be established from lawful, available sources?

Every query and claim should map to a sub-question. Remove collection that does not.

### 7.3 Define materiality before searching

Specify thresholds appropriate to the question: monetary value, ownership percentage, office seniority, event severity, recency, geographic relevance, control relationship, or reporting status. Do not redefine materiality after seeing results without recording the change and rationale.

### 7.4 Define stopping rules

Examples:

- All mandatory T1 sources for each in-scope jurisdiction were checked.
- Each material claim has the required evidence and challenge search.
- Pagination or dataset coverage is complete, or the uncollected portion is quantified.
- New queries produce no new material evidence across two distinct query families.
- The deadline or access limit is reached and remaining gaps are explicit.

“No more obvious search results” is not a stopping rule.

## 8. Identity brief and entity resolution

### 8.1 Subject record

Create the identity brief before adverse searching.

```yaml
subject_id: SUB-001
subject_type: person|organization|asset|vessel|aircraft|address|domain
canonical_name: exact supplied or authoritative name
names:
  legal: []
  former: []
  aliases: []
  transliterations: []
  local_script: []
  abbreviations: []
identifiers:
  date_of_birth: []
  place_of_birth: []
  nationality: []
  registration_numbers: []
  tax_or_lei_identifiers: []
  addresses: []
  domains: []
  asset_identifiers: []
roles_and_affiliations: []
known_time_bounds: []
do_not_confuse_with: []
source_ids: []
```

Never expose restricted identifiers in a public deliverable.

### 8.2 Attribute hierarchy

| Strength | Person examples | Organization or asset examples |
|---|---|---|
| Strong unique | Government identifier, verified full date of birth plus nationality, passport fragment where lawfully available | Registration number, LEI, regulator ID, IMO number, aircraft registration, exact blockchain address, canonical domain |
| Strong composite | Full name + full DOB + jurisdiction; name + position + official biography | Legal name + jurisdiction + registered address; name + parent + filing identifier |
| Moderate | Name + age + city; name + employer and period | Name + city + director; trading name + website + address |
| Weak | Name only, initials, photograph only, unsourced alias | Name only, shared address only, common email domain, third-party label |

### 8.3 Resolution outcomes

| Outcome | Rule | Use |
|---|---|---|
| CONFIRMED_MATCH | At least one unique identifier, or a sufficiently strong composite with no material contradiction | Information may be attributed, subject to evidence-state rules |
| PROBABLE_MATCH | Multiple independent moderate attributes align; no unique identifier; no material contradiction | Human review required; phrase conditionally and do not take consequential action |
| POSSIBLE_MATCH | Name or one weak attribute aligns | Lead only; do not attach adverse information |
| CONFLICTING_MATCH | Strong attributes conflict | Treat as not resolved; investigate the conflict |
| EXCLUDED_MATCH | A reliable disqualifying attribute differs | Record exclusion reason to prevent rework |
| INSUFFICIENT_DATA | Too little information to compare | State the gap; do not force a match |

### 8.4 Identity scorecard

For each candidate hit, record attribute, subject value, record value, comparison (`exact`, `compatible`, `unknown`, `conflict`), strength, source, and time relevance. A score may triage review but may not override a strong conflict. Name similarity alone never satisfies G2.

### 8.5 Relationship resolution

Distinguish:

- legal ownership from voting rights, economic interest, and operational control;
- direct from indirect ownership;
- current from former roles;
- entity address from service-provider or registered-agent address;
- address operator from address user in blockchain evidence;
- beneficial owner from nominee, trustee, protector, settlor, director, signatory, and authorized representative;
- allegation about an affiliate from evidence about the subject.

For ownership chains, cite every edge and date. Compute effective ownership by multiplying percentages along each path, then sum only independent paths. Flag circular ownership and unknown percentages; do not fill them with zero.

## 9. Query planning

### 9.1 Query-plan schema

```yaml
query_id: Q-001
subquestion_id: SQ-01
subject_id: SUB-001
source_target: SRC-REGISTRY-ID|domain|site
query_family: exact|variant|identifier|relationship|event|negative|resolution|language
query_text: exact submitted string
language: en
script: Latin
date_filter: null
expected_evidence: what would answer or narrow the subquestion
priority: mandatory|high|supplemental
executed_at: YYYY-MM-DDThh:mm:ssZ|null
result_count_visible: integer|null
results_reviewed: integer
result_ids: []
limitations: []
```

### 9.2 Minimum query families

For each subject, plan as applicable:

1. Exact legal name in quotation marks.
2. Known aliases, former names, abbreviations, spacing, punctuation, and word-order variants.
3. Local-script names and defensible transliterations.
4. Unique identifiers alone and paired with names.
5. Jurisdiction, city, address, employer, parent, officer, vessel, product, or domain qualifiers.
6. Relevant event vocabulary: enforcement, sanction, charge, conviction, settlement, fraud, bribery, corruption, money laundering, cyber incident, insolvency, license action, and domain-specific equivalents.
7. Primary-source site queries, followed by the site's own search or official API.
8. Relationship queries for owners, officers, subsidiaries, predecessor entities, and counterparties.
9. Negative and resolution queries: dismissed, acquitted, overturned, appealed, corrected, retracted, delisted, revoked, reinstated, exonerated, mistaken identity.
10. Date-bounded and archive queries for the applicable period.

Translate concepts, not only words. Record the translated terms and who or what produced them. Machine translation is a research aid, not independent corroboration.

### 9.3 Query order

Use the following order unless the plan records a reason to depart:

1. Unique identifiers in official sources.
2. Exact name and authoritative variants in official sources.
3. Primary records for the domain and jurisdiction.
4. Reputable secondary sources for discovery, context, and corroboration.
5. Broad web, archive, and specialist discovery sources.
6. Disconfirming, appeal, correction, and later-outcome searches.

This sequence reduces false associations and circular citation.

### 9.4 Search-log completeness

Log unsuccessful queries as well as productive ones. For each search surface, record filters, sort order, visible result count if available, pages reviewed, and access failures. A “no result” statement is limited to the exact names, sources, dates, languages, and methods actually searched.

## 10. Source discovery and qualification

### 10.1 Source-selection test

Before relying on a source, answer:

1. **Authority:** Who owns or issues it, and for which proposition?
2. **Proximity:** Is it the underlying record or commentary about the record?
3. **Identity:** Does it contain attributes sufficient to connect the record to the subject?
4. **Currency:** What is its coverage date, publication date, update cadence, and supersession status?
5. **Method:** Is collection, computation, editorial review, or correction methodology visible?
6. **Independence:** Does it originate independently, or copy another source?
7. **Integrity:** Is the domain authentic, connection secure, document complete, and content internally consistent?
8. **Access:** Was it accessed lawfully and within applicable terms?
9. **Reproducibility:** Can another reviewer retrieve or verify it?
10. **Limitations:** What can it not establish?

### 10.2 Domain authentication

- Reach government and institutional pages from their recognized parent domain, not an advertisement or look-alike result.
- Check scheme, hostname, spelling, certificate warnings, and organizational ownership.
- Prefer permanent document, docket, filing, dataset, or API URLs over session-bound search-result URLs.
- Treat URL shorteners, copied PDFs, mirrors, and document-sharing sites as discovery paths. Locate the issuer's copy.
- When an issuer has migrated domains, record both the historical URL and the current official landing page.

### 10.3 Aggregator fallback chain

An aggregator may reveal an identifier or original citation. Follow this chain:

`aggregator record -> cited dataset or publication -> issuing body -> controlling record -> archived capture`

If the controlling record cannot be retrieved, label the claim `SECONDARY-ONLY`, state the attempted official paths, and lower confidence. Do not convert an aggregator into T1 because it appears comprehensive.

### 10.4 AI-generated and synthetic content exclusion

Content is not evidence merely because it is fluent, structured, or confident.

Exclude from evidentiary reliance when:

- no inspectable source is provided;
- cited sources do not exist, do not support the text, or form a circular chain;
- the named author, publisher, date, or dataset cannot be authenticated;
- the page is mass-generated, has no accountable editorial owner, or recombines other pages without provenance;
- the image, audio, or video lacks a trustworthy origin and the claim depends on authenticity;
- metadata, wording, or chronology materially conflicts with the alleged source.

Generated summaries may assist query generation or translation. Every substantive statement must be re-established from an admissible source. Never cite the model, its memory, or its paraphrase as the underlying evidence.

### 10.5 Exclusion log

```yaml
excluded_source_id: X-001
url: full URL
observed_at: YYYY-MM-DDThh:mm:ssZ
reason_code: fabricated_citation|no_provenance|impersonation|circular|unlawful|manipulated|content_farm|scope_mismatch|superseded
detail: concise factual explanation
related_claim_ids: []
discovery_value_retained: true|false
reviewer: role_or_initials
```

## 11. Capture and provenance

### 11.1 Capture immediately

Do not postpone provenance until drafting. At the time of retrieval, capture:

- source and publisher names;
- full resolved URL and, where relevant, API endpoint and parameters;
- title, record identifier, case number, filing accession, dataset version, list version, or transaction hash;
- author or issuing body;
- publication, event, effective, updated, and retrieval dates separately;
- cited page, paragraph, section, row, field, timestamp, or record key;
- source tier and reason;
- access method and any authentication or license constraint without recording secrets;
- file format, language, and translation method;
- coverage and pagination status;
- checksum for retained files where permitted;
- archive reference where lawful;
- material limitations and supersession status.

### 11.2 Source-record schema

```yaml
source_id: S-0001
registry_id: "02.001"  # if present in the source register
tier: T1|T2|T3|TX
publisher: exact organization
title: exact record or page title
record_type: order|filing|registry|dataset|article|docket|gazette|ledger|other
canonical_url: https://...
resolved_url: https://...
record_identifier: null
jurisdiction: []
language: en
dates:
  event: null
  publication: null
  effective: null
  updated: null
  retrieved: YYYY-MM-DDThh:mm:ssZ
location:
  page: null
  section: null
  paragraph: null
  row_or_field: null
access:
  method: web|api|download|provided_material
  status: complete|partial|metadata_only|inaccessible
  restriction: public|registration|licensed|fee|other
capture:
  file_name: null
  sha256: null
  archive_url: null
  mime_type: null
lineage:
  underlying_source_id: null
  copied_from_source_id: null
limitations: []
```

### 11.3 File naming and immutable originals

Where retention is authorized, use:

`<research_id>_<source_id>_<publisher>_<record-id>_<publication-date>_<retrieval-date>.<ext>`

Keep the retrieved original immutable. Perform OCR, translation, parsing, redaction, and normalization on derivative copies. Record the tool and version, transformation, time, input checksum, and output checksum.

### 11.4 Dynamic and volatile sources

For sanctions lists, market data, dashboards, registries, social posts, live dockets, and public ledgers:

- capture retrieval time with timezone;
- record the list, dataset, block, or page version where available;
- preserve the relevant response or file where lawful;
- record query parameters, filters, pagination, and sort order;
- distinguish current state from state at the event date;
- never represent a historical “clear” search as current.

### 11.5 Archive practice

Prefer issuer archives and official version histories. Use lawful independent web archives only to establish what a public page displayed at a stated time, and label the archive as a secondary capture of the issuer's content. An archive does not prove the truth of the page. Do not archive pages that expose restricted personal data or violate applicable terms.

## 12. Extraction and data normalization

### 12.1 Extract before interpreting

Create structured facts first. Preserve exact values, units, currencies, timezones, names, identifiers, and cited locations. Put interpretation in separate fields.

### 12.2 Extracted-fact schema

```yaml
fact_id: F-0001
subject_id: SUB-001
predicate: controlled_by|registered_at|named_in_order|reported_value|other
object_exact: value as stated
normalized_value: null
unit_or_currency: null
valid_from: null
valid_to: null
evidence_state: OBSERVED|OFFICIALLY_REPORTED|ALLEGED|ADJUDICATED
source_id: S-0001
cited_location: page, paragraph, row, field, or timestamp
extraction_method: manual|parser|ocr|transcription|translation
extractor_version: null
quality_flags: []
```

### 12.3 Normalization rules

- Retain raw and normalized fields.
- Use ISO 8601 dates and explicit timezones.
- Retain original currency and units; record conversion rate, source, and date separately.
- Normalize legal names without deleting punctuation or local-script originals.
- Do not silently convert “approximately,” ranges, percentages, or rounded values to precise numbers.
- Map country and entity identifiers to a documented standard; retain the source label.
- Preserve null as unknown. Never convert missing to zero.
- Deduplicate on stable record identifiers and lineage, not headline similarity alone.
- If OCR or parsing confidence is low, compare against the image or original document.

### 12.4 Completeness controls

For lists, tables, mailboxes, dockets, filings, or paginated APIs, record:

- expected and collected record counts;
- first and last record or date;
- pages or cursor range;
- duplicate count and rule;
- excluded count and reason;
- parsing failures;
- reconciled totals;
- uncollected or inaccessible scope.

Tag derived totals `COMPLETE`, `PARTIAL`, or `UNKNOWN COVERAGE`. Do not calculate a full-population rate from partial coverage without a stated denominator and limitation.

## 13. Claim-evidence ledger

The claim-evidence ledger is the controlling index for the final output. One row represents one testable proposition.

### 13.1 Required fields

| Field | Requirement |
|---|---|
| claim_id | Stable identifier, such as C-001 |
| claim_text | Atomic proposition; no bundled claims |
| materiality | critical, major, supporting, or context |
| evidence_state | controlled vocabulary from section 5.1 |
| subject_id | Resolved subject |
| time_scope | Date or period for which the claim is asserted |
| support_source_ids | Sources that directly support the claim |
| cited_locations | Pinpoint locations for each source |
| source_lineages | Independent origin groups, not raw link count |
| counter_source_ids | Sources that weaken, qualify, or contradict it |
| identity_outcome | Resolution outcome and record reference |
| corroboration_status | controlling-primary, corroborated, single-source, secondary-only, disputed, or unsupported |
| inference | Any reasoning step not stated by the source |
| confidence | HIGH, MODERATE, LOW, or NOT ASSESSABLE, with reason |
| temporal_status | current, historical, superseded, pending, or unknown |
| limitations | Claim-specific boundaries |
| disposition | include, qualify, omit, investigate, or UNRESOLVED |
| reviewer | Human gate result and date |

### 13.2 Example ledger row

```yaml
claim_id: C-001
claim_text: "Entity A was registered in Jurisdiction B on YYYY-MM-DD."
materiality: supporting
evidence_state: OBSERVED
subject_id: SUB-001
time_scope: YYYY-MM-DD
support_source_ids: [S-0001]
cited_locations: ["registry profile: registration date field"]
source_lineages: ["Jurisdiction B registry"]
counter_source_ids: []
identity_outcome: "CONFIRMED_MATCH; exact registration number"
corroboration_status: controlling-primary
inference: null
confidence: "HIGH — registry of record and unique identifier"
temporal_status: historical
limitations: ["Registry records filing, not operational activity"]
disposition: include
reviewer: "reviewed YYYY-MM-DD"
```

### 13.3 Atomic-claim rule

Split “The company was registered in 2019, is owned by Person X, and was fined for fraud” into three claims. Each has a different source, evidence state, identity test, date, and confidence.

### 13.4 Unsupported-claim rule

A material claim with no supporting source is either:

- removed;
- rewritten as a clearly labeled analytical hypothesis with the basis shown; or
- placed in the gap log as a question for further research.

Never add a citation that is merely related. The cited location must entail or directly support the words used.

## 14. Temporal validity and supersession

### 14.1 Required dates

Do not substitute one date for another:

- **event date:** when the underlying event occurred;
- **record date:** when the filing, order, article, or dataset was issued;
- **effective date:** when the rule, status, or action took legal or operational effect;
- **amendment date:** when the record changed;
- **validity interval:** when the fact applied;
- **retrieval date/time:** when the researcher observed it;
- **decision as-of date:** the time boundary for the analysis.

### 14.2 Supersession checks

For every material legal, regulatory, list, license, office-holder, corporate-status, enforcement, or court claim, search for later:

- amendments, corrections, notices, and FAQs;
- appeals, stays, remands, dismissals, settlements, acquittals, and final judgments;
- delistings, license reinstatements, dissolutions, mergers, name changes, and office departures;
- revised datasets, methodology changes, and restatements.

Record the relationship between versions. Do not delete the earlier state if it is relevant to the as-of analysis.

### 14.3 Staleness classification

| Status | Rule |
|---|---|
| CURRENT | Checked against the source's expected update cycle and no superseding record found |
| HISTORICAL-VALID | Accurate for a defined past interval |
| STALE-UNVERIFIED | Older than the expected cycle and not revalidated |
| SUPERSEDED | Replaced, amended, reversed, or made obsolete by a later record |
| PENDING | Proceeding or change remains open |
| UNKNOWN | Date or status cannot be established |

Do not use a universal freshness window. Sanctions and trading data may require same-day checks; audited accounts, census data, and treaty records follow different cycles.

## 15. Corroboration, independence, and conflict resolution

### 15.1 Corroboration standard

| Claim type | Minimum expected support |
|---|---|
| Existence, registration, license, listing, designation, judgment, or filed financial value | Controlling T1 record |
| Serious adverse allegation | Underlying complaint, charge, or named accountable T2 report; resolved identity; later-outcome search |
| High-consequence adverse conclusion | T1 plus independent corroboration where feasible; specialist/human review |
| Quantitative comparison | Primary dataset or filings; calculation trail; methodology and denominator checks |
| Beneficial ownership or control | Registry/filing evidence for each edge; distinguish declaration from verified fact |
| Public-office or PEP status | Official office-holder, election, appointment, gazette, parliament, or government record; dates and role prominence |
| On-chain activity | Ledger/explorer facts; separate any address attribution, which requires independent support |
| Adverse-media-only event | Two independent accountable lineages when no primary record is available, or label single-source and lower confidence |
| Negative finding | Documented coverage across mandatory sources, variants, period, languages, and limitations; never absolute proof of absence |

### 15.2 Independence test

Sources are not independent when they:

- reproduce the same press release, wire story, court summary, or database;
- cite each other in a circle;
- share the same unnamed source;
- are brands under common editorial control for the relevant story;
- use the same underlying vendor or public dataset;
- merely mirror or translate the same record.

Assign a `lineage_id` to each origin. Corroboration requires distinct lineages, not different URLs.

### 15.3 Conflict log

```yaml
conflict_id: K-001
claim_id: C-001
source_a: S-0001
source_b: S-0002
conflict_type: value|identity|date|scope|legal_status|translation|methodology
description: exact disagreement
authority_comparison: which source controls which proposition and why
temporal_explanation: null
resolution: source_a_preferred|source_b_preferred|both_contextual|unresolved
rationale: concise evidence-based explanation
impact_on_output: wording, confidence, or omission
reviewed_by: human reviewer and date
```

### 15.4 Resolution order

1. Confirm the records refer to the same subject, event, period, unit, and legal stage.
2. Check versions, corrections, definitions, and methodology.
3. Prefer the body with authority for the exact proposition.
4. Prefer the more direct, complete, and current record.
5. Preserve credible dissent if it concerns interpretation rather than fact.
6. If still unresolved, report the conflict and its consequence. Do not average incompatible facts or choose silently.

## 16. Negative searches and absence statements

### 16.1 Purpose

A negative search tests whether the apparent absence of a record survives reasonable variants and mandatory sources. It does not prove a universal negative.

### 16.2 Minimum procedure

1. Define the target record and relevant jurisdiction, period, and authority.
2. Search unique identifiers first.
3. Search exact, variant, former, local-script, and transliterated names.
4. Search relevant official lists, registries, dockets, archives, and datasets.
5. Search parent, subsidiary, officer, predecessor, and related-asset paths where relevant.
6. Check removed, archived, dissolved, historical, and delisted records.
7. Record access, pagination, date, filters, and failed queries.
8. Run a broad discovery search for missed official sources.
9. State the result with its boundary.

### 16.3 Approved wording

- “No responsive record was identified in the listed sources using the recorded names and identifiers as of [timestamp].”
- “The review did not establish [proposition]; coverage was limited by [constraint].”
- “No current designation was identified in the authoritative lists checked as of [timestamp]. Re-screening is required for a later decision.”

Do not write “there is no record,” “the subject is clean,” “not sanctioned,” or “no adverse media exists” without an explicitly bounded scope and current authoritative check.

## 17. Quotations, copyright, and faithful paraphrase

### 17.1 Quotation discipline

- Quote only the minimum language needed to establish a proposition.
- Preserve wording, capitalization where material, omissions, and context.
- Use quotation marks and a pinpoint citation.
- Do not splice non-contiguous text into a single quotation.
- Mark supplied emphasis or translation.
- For legal language, prefer the operative record and quote only where exact wording matters.

### 17.2 Copyright discipline

- Link to or cite copyrighted works; do not reproduce full articles, reports, images, tables, or substantial passages unless licensed or clearly permitted.
- Use short quotations and original summaries.
- Do not reconstruct paywalled content from snippets or copies.
- Record license and attribution requirements for open datasets and media.
- Treat public availability as distinct from public-domain status.

### 17.3 Paraphrase test

A paraphrase must preserve who did what, evidence stage, amount, time, jurisdiction, qualification, and uncertainty. Compare the draft against the cited passage. If the paraphrase makes the source more certain, final, broad, or adverse, correct it.

### 17.4 Translation

Retain original text, language, translator or tool, and translated text. Independently review material legal, technical, or adverse passages when consequences are high. A translated duplicate is not independent corroboration.

## 18. Analysis, inference, and uncertainty

### 18.1 Observation–inference firewall

Use this structure for each material conclusion:

1. **Evidence:** what the sources directly establish.
2. **Inference:** the analytical conclusion drawn from those facts.
3. **Alternative:** a credible competing explanation.
4. **Uncertainty:** missing or conflicting information.
5. **Implication:** why the bounded conclusion matters.
6. **Next test:** evidence that would increase or reduce confidence.

### 18.2 Quantitative work

Record:

- source fields and observation period;
- population, sample, and exclusions;
- units, currencies, conversion sources, and base dates;
- formulas, code version, parameters, and assumptions;
- missing-data treatment;
- reconciliation to source totals;
- sensitivity or scenario results;
- rounding only at presentation.

Do not imply precision beyond the inputs. A calculated number can be exact arithmetic on uncertain data; label the uncertainty.

### 18.3 Risk and legal language

Distinguish evidence from decision criteria. Use “indicator,” “record,” “exposure,” “requires review,” or “supports escalation” when the evidence does not itself establish legal guilt, intent, ownership, control, or prohibited status. Reserve legal conclusions for the controlling record or qualified decision owner.

### 18.4 Uncertainty register

| Field | Description |
|---|---|
| uncertainty_id | Stable key |
| affected_claims | Claim IDs |
| type | identity, source, coverage, time, translation, measurement, legal interpretation, or model |
| description | What is not known |
| direction | Could increase, decrease, or unpredictably change the conclusion |
| materiality | Critical, major, supporting, context |
| reducible | Yes/no and how |
| status | Open, accepted, resolved |
| owner | Human or team |

## 19. Quality assurance

### 19.1 First-line researcher checks

- Scope matches G0; no unauthorized expansion.
- Every source record is complete and tiered for the proposition used.
- Every material claim appears in the claim-evidence ledger.
- Every citation opens or has a documented retained capture and pinpoint location.
- Names, dates, amounts, currencies, case numbers, list versions, and identifiers match originals.
- Entity resolution is complete before adverse attribution.
- Allegation, finding, settlement, dismissal, and appeal status are accurate.
- Later-outcome and disconfirming searches were run.
- Duplicate lineages are not counted as corroboration.
- Calculations reconcile; missing values remain missing.
- Partial coverage is visible.
- Quotes and reproductions are minimal and permitted.
- Sensitive data is minimized and correctly classified.
- Conclusions do not exceed evidence.

### 19.2 Independent review sample

For high-consequence or externally distributed work, the reviewer should independently:

1. Re-open every source for critical claims.
2. Re-perform identity resolution for every critical adverse match.
3. Recalculate critical numbers from the source fields.
4. Sample supporting claims using a risk-based plan.
5. Run at least one disconfirming query per major conclusion.
6. Check one excluded hit and one no-result path for search discipline.
7. Verify temporal status and supersession.
8. Review redaction, copyright, and distribution controls.

### 19.3 QA defect taxonomy

| Code | Defect |
|---|---|
| QA-01 | Citation does not support claim |
| QA-02 | Wrong or unresolved subject |
| QA-03 | Material date/status omitted or wrong |
| QA-04 | Secondary source used where primary exists without explanation |
| QA-05 | Circular or non-independent corroboration |
| QA-06 | Extraction, transcription, translation, or unit error |
| QA-07 | Incomplete pagination or denominator |
| QA-08 | Unsupported inference or overstatement |
| QA-09 | Counterevidence or later disposition omitted |
| QA-10 | Access, privacy, license, or retention issue |
| QA-11 | Generated or fabricated source contamination |
| QA-12 | Reproducibility package incomplete |

Critical defects block release. Correct the source record and every downstream claim, table, chart, and conclusion affected.

### 19.4 Release criteria

The package is ready only when:

- all gates required by the review level are signed;
- no critical defect is open;
- all critical and major claims have disposition and confidence;
- unresolved conflicts and gaps are prominent, not buried;
- the executive wording matches the ledger;
- the output is dated and bounded to its as-of time;
- the evidence pack can be re-walked without the original researcher.

## 20. Reproducibility package

### 20.1 Minimum directory manifest

The storage implementation may vary, but preserve these logical components:

```text
research-brief
subject-register
source-register
query-log
capture-manifest
immutable-source-captures-or-approved-references
extracted-facts
claim-evidence-ledger
conflict-log
uncertainty-and-gap-log
calculations-and-code-manifest
qa-review-log
final-output
release-manifest
```

Do not place restricted captures in a public repository. A public methodology package should contain only the standard, empty schemas, official source links, and synthetic examples.

### 20.2 Run manifest

```yaml
research_id: R-YYYYMMDD-NNN
standard_version: "1.0"
started_at: YYYY-MM-DDThh:mm:ssZ
completed_at: YYYY-MM-DDThh:mm:ssZ
as_of: YYYY-MM-DDThh:mm:ssZ
operators: []
tools:
  - name: browser_or_parser
    version: recorded_if_known
    purpose: collection|ocr|translation|analysis|rendering
source_count:
  total: 0
  by_tier: {T1: 0, T2: 0, T3: 0, TX: 0}
query_count: 0
capture_count: 0
claim_count: 0
coverage: complete|partial|unknown
known_gaps: []
quality_review: self_check|second_person|specialist
approvals: []
artifacts:
  - path_or_id: value
    sha256: value_if_permitted
```

### 20.3 Re-run test

A second analyst should be able to:

1. identify the exact question and as-of date;
2. repeat each mandatory query;
3. retrieve or verify each source;
4. reproduce extracted facts and calculations;
5. understand exclusions and conflicts;
6. reach the same bounded claim set, or explain differences caused by later source changes.

Reproducibility does not require identical search-engine rankings. It requires a complete record of planned sources, queries, inputs, transformations, and judgments.

## 21. Output handoff

### 21.1 Required final structure

1. **Decision-relevant answer:** bounded, dated, and direct.
2. **Scope and as-of time:** subjects, jurisdictions, period, source boundary, and exclusions.
3. **Material findings:** one claim per item, evidence state and confidence visible.
4. **Counterevidence and alternatives:** strongest credible challenge.
5. **Gaps and limitations:** inaccessible, stale, partial, or unresolved evidence.
6. **Implications and options:** separate from facts; name the human decision required.
7. **Method:** source tiers, identity method, search coverage, and calculation approach.
8. **Sources:** full citations with retrieval dates and pinpoint references.
9. **Evidence annex:** claim-evidence ledger or a distribution-safe extract.
10. **Approval and version:** reviewer, release date, as-of date, and supersession note.

### 21.2 Handoff statement

Use a statement equivalent to:

> This output reports evidence identified within the stated public-source scope as of the stated time. It is not a universal assertion of absence, a legal conclusion, or an automated decision. Material actions require review under applicable law and policy. The evidence package records source versions, identity resolution, conflicts, limitations, and unresolved gaps.

### 21.3 Action register

| Action ID | Triggering claim/gap | Proposed next step | Decision owner | Due date | Human approval required | Status |
|---|---|---|---|---|---|---|
| A-001 | C-001 | Obtain controlling filing | Named role | YYYY-MM-DD | Yes | Open |

The research system may propose actions. It may not represent an unapproved action as decided or completed.

## 22. Special domain controls

### 22.1 Sanctions and watchlists

- Use the current authoritative list for every relevant jurisdiction at the decision time.
- Record list version, retrieval timestamp, program, list type, match fields, and search method.
- Treat weak aliases, transliteration, ownership/control rules, and sectoral restrictions according to governing law and policy.
- A clear search expires when the list or subject data changes.
- A potential hit requires human sanctions review; the research tool does not block or clear.

### 22.2 Adverse media

- Classify subject role: alleged wrongdoer, convicted/liable party, victim, witness, official, expert, unrelated namesake, or unclear.
- Classify procedural stage and later outcome.
- Prefer the underlying authority or court record.
- Do not equate repetition with corroboration or allegations with facts.
- Record relevance, severity, recency, materiality, and right-party basis separately.

### 22.3 Corporate and beneficial ownership

- A registry is authoritative for what was filed, not necessarily for current economic reality or verification.
- Capture filing date, effective date, status, jurisdiction, entity number, officers, shareholders, controllers, and source document.
- Distinguish legal, beneficial, voting, and de facto control.
- Document each chain edge and unknown layer; do not infer a natural-person owner from a name alone.

### 22.4 Courts and enforcement

- Capture court, case number, parties, document number, date, stage, operative language, and appeal status.
- Distinguish complaint, indictment, administrative allegation, consent order, settlement, judgment, plea, conviction, dismissal, and acquittal.
- Do not treat sealed, vacated, or superseded records as current without explanation.

### 22.5 Public office and PEP research

- Establish the qualifying public function from official appointment, election, parliament, gazette, government, or institutional sources.
- Record role, jurisdiction, seniority, start/end dates, and whether status is current or former.
- Separate the principal from family members and close associates; relationship evidence requires its own sources.
- PEP status is a risk-management category, not proof of wrongdoing.

### 22.6 On-chain evidence

- Transactions, timestamps, amounts, blocks, and contract interactions are ledger observations.
- Explorer, community, or vendor labels are attributions and require separate source records.
- Never infer a natural person's ownership from control of or interaction with an address without additional evidence.
- Keep assets and chains separate; reconcile pagination; identify dust, spam tokens, internal transactions, and bridge behavior.
- A designated address match routes to a human sanctions process.

### 22.7 Statistics and indices

- Record edition, methodology, coverage, revisions, definitions, units, and missing-data treatment.
- Avoid comparing incompatible editions or definitions.
- Use categorical official designations as designations, not weighted opinion scores.
- For composites, publish components, normalization, weights, sensitivity, and limitations.

## 23. Compact operating checklists

### 23.1 Before research

- [ ] Decision question and as-of date are explicit.
- [ ] Authority, privacy, licensing, and retention are approved.
- [ ] Subjects, jurisdictions, period, and out-of-scope items are defined.
- [ ] Identity brief and mandatory-source map are prepared.
- [ ] Query families, languages, materiality, and stopping rules are recorded.
- [ ] Required human gates and review level are assigned.

### 23.2 During research

- [ ] Every query and failed access attempt is logged.
- [ ] Every source is authenticated, tiered, captured, and bounded.
- [ ] Raw facts are separated from normalized values and interpretation.
- [ ] Identity is resolved before adverse attribution.
- [ ] Source lineage and duplicates are tracked.
- [ ] Temporal status, pagination, and dataset completeness are recorded.
- [ ] Disconfirming, correction, appeal, and later-outcome searches are run.
- [ ] AI-generated and unsourced material is excluded from evidence.

### 23.3 Before release

- [ ] Every material sentence maps to an atomic ledger claim.
- [ ] Citations directly support wording and include pinpoint locations.
- [ ] Confidence has a reason; conflicts and gaps are visible.
- [ ] Numbers reconcile and calculations can be reproduced.
- [ ] Quotes are minimal, accurate, and permitted.
- [ ] Personal and restricted data is minimized and correctly handled.
- [ ] Human reviewers completed required gates.
- [ ] Output date, as-of date, version, and supersession warning are present.

## 24. Failure conditions

Stop and return the work to the appropriate human when:

- the request lacks lawful authority or a defined decision purpose;
- source access would require bypassing a control or violating terms;
- a consequential result depends on unresolved identity;
- the only support is generated, anonymous, circular, or unauthenticated;
- a controlling record is inaccessible and the distinction materially affects the decision;
- material sources conflict and the conflict cannot be resolved;
- source coverage is too incomplete to answer the question responsibly;
- sensitive data cannot be handled within the approved environment;
- a reviewer cannot reproduce a critical claim;
- the requested wording would overstate, defame, or convert allegation into fact.

The correct outcome may be `INSUFFICIENT EVIDENCE`, `UNRESOLVED IDENTITY`, `PARTIAL COVERAGE`, or `HUMAN DECISION REQUIRED`. These are valid results, not system failures.

## 25. Maintenance

Review this standard at least annually and after material changes to law, source access, evidence technology, or operating scope. Version all changes. Do not silently change tier definitions, evidence states, match rules, confidence language, or required gates within an active matter.

The companion source register is `02-osint-source-register.md`. It identifies starting points and known limitations; it does not replace current-source verification or the controls in this standard.
