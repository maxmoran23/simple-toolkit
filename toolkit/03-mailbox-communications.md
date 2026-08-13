# Mailbox and Communications Intelligence

Use this file to inventory, normalize, reconcile, analyze, track, and draft from authorized email and internal-communications records. It is an implementation standard, not a promise that an assistant can access a mailbox. Access must be explicitly authorized and supplied through an available connector, API, export, or pasted material.

The governing rule is preservation before interpretation: establish what was in scope, prove what was received, retain the source record, reconstruct relationships, and only then extract issues, actions, deadlines, or proposed responses. A concise summary is useful only after coverage and lineage are visible.

## 1. Operating contract

### Required outcomes

Every run must produce enough evidence to answer:

1. What sources, mailboxes, folders, channels, date ranges, and record types were authorized and requested?
2. What was actually retrieved, what was excluded, and what failed?
3. Which source records are unique messages, duplicates, versions, replies, forwards, quoted copies, or unresolved fragments?
4. What facts, issues, decisions, actions, deadlines, escalations, and response obligations are supported by which exact records?
5. What remains uncertain, incomplete, unreadable, or outside access?
6. What changed since the prior successful run?
7. Which proposed actions require human approval?

### Non-negotiable controls

- Operate only within the explicit scope and permissions recorded in the run manifest.
- Use read-only access for collection whenever the source permits it.
- Never infer that access exists. State `ACCESS_NOT_AVAILABLE` when it does not.
- Never mark a mailbox or period complete merely because a search returned no more rows.
- Preserve source identifiers, headers, timestamps, body text, attachment metadata, and retrieval provenance before transformation.
- Never silently discard corrupt, unsupported, excluded, duplicated, or unparsed material; account for it in a ledger.
- Never merge people, messages, threads, issues, or actions solely because their names or subjects look similar.
- Separate source fact, deterministic normalization, and analytical inference.
- Attach an evidence pointer and confidence to every material extracted item.
- Never send email, post a message, change a record, assign work, or close an issue without a human-authorized action step.
- Treat a proposed response as a draft. A draft is not an approval, delivery confirmation, or completed action.
- Do not place secrets, authentication material, or unnecessary sensitive content in outputs, prompts, logs, or examples.

### Supported operating modes

| Mode | Purpose | Permitted default | Prohibited default |
|---|---|---|---|
| Inventory | Establish source coverage and control totals | Read metadata, enumerate authorized containers, report gaps | Content analysis, writes |
| Archive | Preserve normalized message and attachment records | Read and write to the designated local evidence workspace | Deleting or changing source records |
| Intelligence | Extract issues, actions, decisions, deadlines, and escalation indicators | Read normalized evidence and create trackers | Treating an inference as a source fact |
| Drafting | Prepare proposed replies, forwards, updates, and follow-ups | Create clearly labeled drafts | Sending, scheduling, posting, or altering recipients |
| Refresh | Add new or changed records and reconcile longitudinal state | Idempotent ingestion and versioned updates | Rewriting history without a supersession record |
| Review | Test completeness and accuracy | Sampling, reconciliation, trace-back | Self-approval of external action |

## 2. Roles and human gates

One person may hold several roles, but the role performed at each decision must be logged.

| Role | Accountability |
|---|---|
| Scope owner | Approves sources, populations, exclusions, period, purpose, and acceptable use |
| Access owner | Grants and periodically reviews least-privilege access |
| Records owner | Confirms retention, legal-hold, privilege, and records-management constraints |
| Process owner | Defines issue, escalation, action, and response rules |
| Operator | Runs ingestion and resolves technical failures without changing analytical rules |
| Analyst | Reviews extraction, exceptions, and evidence links |
| Approver | Approves any communication or external state change |
| Quality reviewer | Independently tests coverage, mappings, calculations, and output |

Human approval is mandatory before:

- adding a new mailbox, shared mailbox, channel, folder, person, or date range to scope;
- using content for a purpose not listed in the run manifest;
- retrieving restricted material when a narrower source would suffice;
- changing a retention, redaction, privilege, or exclusion rule;
- resolving an ambiguous person or entity match that affects attribution;
- overriding a hard completeness or evidence gate;
- issuing a substantive escalation, assigning an action, or changing an owner or deadline;
- sending, scheduling, posting, forwarding, or otherwise releasing a communication;
- closing an issue, action, exception, or incident;
- publishing outputs outside the approved audience.

## 3. Scope specification and run manifest

Do not begin extraction until a scope specification exists. If information is missing, record the gap; do not invent it.

### Scope specification

| Field | Required content |
|---|---|
| `purpose` | The decision or operational outcome the review supports |
| `authorized_by` | Role or approval record, not credentials |
| `sources_requested` | Mailboxes, shared mailboxes, folders, archives, channels, exports, or pasted sets |
| `record_types` | Messages, drafts, calendar-linked messages, channel posts, attachments, reactions, edits, or other authorized types |
| `period_start` / `period_end` | Inclusive bounds, source timezone, and normalization timezone |
| `cutoff_at` | Exact time after which later records are outside the run |
| `inclusions` | Participants, domains, subjects, issue categories, or populations explicitly included |
| `exclusions` | Personal, privileged, restricted, automated, newsletter, spam, or other excluded material and the authority for exclusion |
| `content_depth` | Metadata only, body, headers, attachments, embedded messages, or linked content |
| `retention_class` | Approved retention and disposal treatment for derived artifacts |
| `output_audience` | Authorized readers and distribution boundary |
| `prior_run` | Prior successful run identifier and watermark, if incremental |
| `completion_standard` | Required coverage and reconciliation gates |

### Run manifest

Create a machine-readable manifest for every attempt, including failed and partial runs.

```json
{
  "run_id": "<stable run identifier>",
  "mode": "<inventory|archive|intelligence|drafting|refresh|review>",
  "started_at_utc": "<ISO 8601>",
  "completed_at_utc": "<ISO 8601 or null>",
  "status": "<COMPLETE|COMPLETE_WITH_GAPS|PARTIAL|FAILED>",
  "purpose": "<approved purpose>",
  "scope_version": "<version>",
  "authorization_reference": "<approval or policy reference>",
  "requested_sources": ["<source/container>"],
  "retrieved_sources": ["<source/container>"],
  "period": {
    "start": "<ISO 8601>",
    "end": "<ISO 8601>",
    "source_timezone": "<IANA timezone or unknown>",
    "normalization_timezone": "UTC"
  },
  "cutoff_at_utc": "<ISO 8601>",
  "query_or_export_references": ["<traceable reference>"],
  "retrieval_pages": 0,
  "source_records_reported": 0,
  "records_received": 0,
  "records_normalized": 0,
  "records_quarantined": 0,
  "unique_messages": 0,
  "duplicate_instances": 0,
  "message_versions": 0,
  "attachments_declared": 0,
  "attachments_retrieved": 0,
  "attachments_parsed": 0,
  "gaps": ["<gap id>"],
  "prior_run_id": "<id or null>",
  "watermark_in": "<source-specific value or null>",
  "watermark_out": "<source-specific value or null>",
  "tool_and_parser_versions": {"<component>": "<version>"},
  "input_manifest_hash": "<hash over ordered source receipt manifest>",
  "output_manifest_hash": "<hash over ordered output manifest>",
  "review_status": "<NOT_REVIEWED|REVIEWED_WITH_EXCEPTIONS|APPROVED>"
}
```

Hashes support integrity and change detection; they do not prove that the source system returned a complete population.

## 4. Permission, minimization, and information handling

### Least-privilege pattern

1. Define the narrowest containers, fields, period, and purpose that answer the question.
2. Prefer read-only, metadata-first discovery.
3. Expand to body or attachment content only when the approved purpose requires it.
4. Keep credentials in the source platform or approved secret store; never copy them into a prompt or artifact.
5. Restrict derived outputs at least as tightly as their most restricted source.
6. Record access failures as scope gaps. Never route around a permission boundary with another account or unapproved source.
7. Revoke temporary access and document revocation when the run ends, if that was part of the authorization.

### Data minimization rules

- Store a source pointer rather than repeated body text in trackers when the pointer is sufficient.
- Quote only the minimum evidence span required to substantiate an item.
- Redact or tokenize unnecessary sensitive values in summaries, examples, and broad-audience dashboards.
- Keep raw records separate from analyst-facing outputs.
- Do not copy attachment content into a tracker merely because it was available.
- Do not infer or enrich sensitive attributes unless explicitly authorized and necessary.
- Do not use mailbox content to train or tune a model unless separately approved.
- Treat privilege, confidentiality, retention, and legal-hold flags as hard routing constraints, not display labels.

### Handling classes

Assign each source and derived artifact a handling class defined by the adopting organization. At minimum record: classification, allowed audience, retention rule, redaction requirement, external-sharing restriction, and whether automated processing is permitted. Where the classification cannot be established, route the record to restricted review and exclude it from broad outputs.

## 5. Source inventory and coverage map

Build a coverage map before collection.

| Source/container | Owner role | Access path | Expected record types | Expected period | Content depth | Pagination/export method | Control total available | Status |
|---|---|---|---|---|---|---|---|---|
| `<source>` | `<role>` | `<authorized method>` | `<types>` | `<bounds>` | `<metadata/body/attachment>` | `<method>` | `<yes/no and basis>` | `<ready/gap>` |

For email, inventory every in-scope mailbox and relevant container separately: primary folders, user-created folders, shared-mailbox folders, archive stores, sent items, drafts when approved, recoverable/deleted areas when approved and technically exposed, and quarantine or junk areas when relevant. Do not assume a provider's default “all mail” view includes every container.

For internal collaboration records, inventory each authorized workspace, channel, direct-message population, thread/reply type, edit history, reaction record, attachment store, and linked document source. A channel export is not complete if replies or edits are delivered through separate endpoints and were not retrieved.

### Coverage statuses

| Status | Meaning |
|---|---|
| `IN_SCOPE_RETRIEVED` | Requested and received through an authorized method |
| `IN_SCOPE_EMPTY_VERIFIED` | Source reports zero records and the zero was independently checked against the scope and bounds |
| `IN_SCOPE_PARTIAL` | Some records received, with a named gap |
| `IN_SCOPE_UNAVAILABLE` | Access, export, or technical constraint prevented retrieval |
| `OUT_OF_SCOPE_APPROVED` | Explicitly excluded with authority and reason |
| `OUT_OF_SCOPE_UNASSESSED` | Not requested; no completeness claim may include it |

## 6. End-to-end processing pipeline

Run the stages in order. A later stage may not erase an earlier-stage failure.

### Stage 0 — authorize and freeze scope

- Validate the purpose, access, handling, time bounds, containers, and outputs.
- Record the exact query, export, or selection logic.
- Establish the cutoff and baseline control totals.
- Freeze rule, parser, and prompt versions for the run.
- Create an empty gap ledger before ingestion.

### Stage 1 — enumerate containers

- Retrieve the authorized container hierarchy and record source-native identifiers.
- Detect aliases, redirects, nested folders, renamed channels, and archived containers where exposed.
- Record containers the interface cannot enumerate.
- Compare the retrieved container list with the approved coverage map.

### Stage 2 — retrieve completely

- Page until the source explicitly indicates exhaustion; record page tokens or export chunks.
- Preserve the source's stable record ID, transport `Message-ID` where present, conversation/thread IDs, folder or channel location, and retrieval timestamp.
- Capture sent and received records needed to determine response status.
- Use an overlap window for incremental retrieval to catch late-arriving, moved, or edited records.
- Respect rate limits and resume from a recorded checkpoint. Never silently shorten the period.
- If a page or chunk fails, retry only the read operation under the source's documented behavior; otherwise mark the missing interval or token as a gap.
- Record provider-reported totals where available, but do not substitute them for received-record counts.

### Stage 3 — preserve source receipts

For each received object, write or record:

- source system and container;
- source-native record ID and version/change token;
- retrieval batch, page/chunk, and timestamp;
- raw or lossless export location;
- content hash over the received bytes or canonical export;
- header/metadata availability;
- body and attachment availability;
- parse state;
- handling class.

The raw receipt layer is append-only or versioned. Correct a normalization in the derived layer; do not rewrite the received source representation.

### Stage 4 — normalize without losing source values

- Decode transfer and character encodings while retaining the original bytes or source export.
- Store original and normalized subject, addresses, timestamp strings, body variants, filenames, and content types.
- Normalize line endings and Unicode for comparison in a derived field only.
- Convert timestamps to UTC while preserving the source value and source timezone/offset.
- Separate plain text, HTML, rich text, and embedded-message bodies; record conversion method.
- Sanitize active content for viewing. Do not execute macros, scripts, remote images, or embedded objects.
- Quarantine password-protected, encrypted, malformed, or unsupported items without declaring them empty.

### Stage 5 — resolve identity and relationships

- Assign stable message, instance, version, thread, participant, and attachment identifiers under the rules below.
- Link replies, forwards, quoted copies, duplicates, and superseding versions with typed relationships.
- Preserve uncertainty and competing candidate relationships.

### Stage 6 — extract intelligence

- Extract only the approved classes of entity, issue, decision, action, deadline, escalation indicator, and response obligation.
- Bind each item to an exact evidence span and source record.
- Keep deterministic extraction separate from model-assisted classification.
- Route low-confidence or consequential items to review.

### Stage 7 — reconcile and test

- Run control totals and one-to-one accounting across source receipts, normalized records, deduplicated messages, versions, and quarantine.
- Test a risk-based and random sample back to source.
- Confirm no hard gap is hidden by successful downstream processing.

### Stage 8 — render and gate

- Produce the output contract in Section 20.
- Mark partial outputs prominently.
- Prepare drafts, if requested, but do not release them.
- Obtain independent QA under [09-quality-assurance.md](09-quality-assurance.md).

## 7. Record identity and immutable lineage

Do not use `date|from|subject` alone as a message identity; collisions and missing headers make it unsafe.

### Identifier hierarchy

Maintain distinct identifiers for distinct concepts:

| Identifier | Represents | Preferred derivation |
|---|---|---|
| `source_instance_id` | One object in one source/container | Source system + mailbox/workspace + source-native immutable ID |
| `message_id` | The logical message content | Valid transport `Message-ID` plus source domain; otherwise a documented canonical-content fingerprint |
| `message_version_id` | One observed version of a logical message | `message_id` + source version/change token or content hash |
| `thread_id` | A reconstructed conversation | Strongest available relationship graph identifier; never subject alone without a low-confidence flag |
| `attachment_id` | One attachment payload | Content hash when bytes exist; otherwise message version + ordinal + normalized filename |
| `participant_id` | One resolved communication identity | Source directory ID when authorized; otherwise normalized address with explicit alias links |
| `extraction_id` | One issue/action/etc. observation | Type + source span + extraction-rule version |

### Canonical-content fingerprint fallback

When no reliable message identifier exists, compute a versioned fingerprint over an explicitly documented canonical tuple such as normalized sender address, normalized recipient sets, source timestamp including offset, normalized subject, and normalized body hash. Keep the tuple and algorithm version. Treat collisions as review exceptions. Do not pretend the fingerprint is a source identifier.

### Lineage invariant

Every derived record must trace through:

```text
derived item -> evidence span -> message version -> source instance -> retrieval batch -> scope manifest
```

If any link is absent, the item is `UNTRACEABLE` and cannot support a final finding or outbound draft.

## 8. Message, duplicate, version, reply, and forward logic

### Relationship precedence

Use the strongest available evidence in this order:

1. Valid `References` and `In-Reply-To` transport headers.
2. Source-native conversation/thread identifiers, interpreted within that source.
3. Embedded original-message identifiers or complete forwarding headers.
4. Exact quoted-content containment linked to a known message version.
5. Participant, temporal, and normalized-subject similarity as a candidate relationship only.

Do not force a single thread when strong signals conflict. Create a `relationship_conflict` exception with the candidate edges.

### Subject normalization

Maintain both original and normalized subjects. For comparison only:

- trim and collapse whitespace;
- normalize Unicode;
- strip repeated localized reply/forward prefixes using a versioned list;
- preserve bracketed case, ticket, or distribution references unless a documented rule removes them;
- do not remove numbers or named identifiers merely to increase matching.

Subject equivalence is weak evidence. Two messages with the same subject can be unrelated; one thread can change subject.

### Relationship decision table

| Condition | Classification | Treatment |
|---|---|---|
| Same source-native object and same version token/hash | Same instance/version | Idempotent re-retrieval; do not duplicate |
| Different source instances, same reliable transport ID and same body hash | Duplicate instance | Keep both locations; count once as logical message |
| Same reliable transport ID, different body or headers | Version/conflict | Preserve each version; investigate source behavior |
| Same canonical content, identifiers absent or different | Probable duplicate | Link with confidence; do not delete either receipt |
| Valid parent header points to known message | Reply | Add directed parent-child edge |
| Complete forwarding block or embedded message | Forward containing prior record | Link forward wrapper and embedded/quoted record separately |
| Quoted history exactly matches captured message | Quoted duplicate | Replace only in a display view with a pointer; retain raw body |
| Quoted history has no captured source record | Orphan quoted message | Preserve as embedded fragment with derived identity and gap flag |
| Changed subject with strong reference chain | Same thread | Preserve subject change event |
| Same normalized subject without strong linkage | Candidate thread | Keep separate unless corroborated |

### Versions and edits

- Preserve each edit or source version the authorized interface exposes.
- Mark one version `latest_observed`, not “true,” unless the source defines authority.
- Never overwrite a prior version in the evidence layer.
- Create `supersedes`, `edited_from`, or `retracted_by` edges only when supported.
- Record deletion or recall notices as events; do not infer that all recipients' copies were removed.

## 9. Body segmentation, quoted text, signatures, and disclaimers

Preserve the raw body and build a derived segment map.

| Segment type | Examples of evidence | Analytical treatment |
|---|---|---|
| `AUTHOR_TEXT` | New text attributable to the current sender | Eligible for current-message extraction |
| `INLINE_REPLY` | New response interleaved with quoted passages | Extract only attributable new spans; retain adjacency |
| `QUOTED_HISTORY` | Reply markers, indentation, known prior-content match | Link to prior message or preserve orphan fragment |
| `FORWARDED_WRAPPER` | Current sender's text introducing a forwarded item | Analyze as current-message content |
| `FORWARDED_MESSAGE` | Complete embedded headers/body | Treat as separate embedded record where possible |
| `SIGNATURE` | Name, title, contact block, mobile footer | Use cautiously for identity hints; exclude from issue/action extraction by default |
| `DISCLAIMER` | Standard legal, confidentiality, or security footer | Preserve; exclude from substantive extraction unless specifically relevant |
| `AUTOMATED_BANNER` | External-sender warning, security gateway text | Preserve as system-added metadata; do not attribute to sender |
| `UNCLASSIFIED` | Parser cannot assign reliably | Preserve and route to review |

Segmentation rules must be versioned and tested against multilingual replies, top-posting, bottom-posting, inline replies, malformed HTML, and mobile signatures. A parser may label a segment; it may not delete it from the source record.

## 10. Participants, aliases, and attribution

### Participant record

Capture source values separately from resolution:

- display name as written;
- address or platform handle as written;
- normalized address/handle;
- source directory identifier, only when authorized;
- role in the message: from, sender, on-behalf-of, reply-to, to, cc, bcc if available and authorized, channel author, mentioned, or forwarded author;
- participant type: person, group, shared mailbox, system, service account, external, or unknown;
- alias/group membership evidence and effective dates when available;
- resolution status and confidence.

### Attribution rules

- `From`, `Sender`, `Reply-To`, and on-behalf-of fields are not interchangeable.
- A group address does not prove which member read or acted on a message.
- A display name is not a unique person identifier.
- A signature can support an alias hypothesis but cannot override contradictory headers.
- Forwarding a statement does not make the forwarder its author or endorser.
- Mentioning a person does not assign an action unless the language reaches the commitment bar.
- Bcc recipients may be unavailable in received copies; state this limitation.
- Do not infer organizational hierarchy or authority from address order.

Ambiguous identity resolution that changes ownership, attribution, escalation, or response routing requires human review.

## 11. Dates, clocks, and timezones

Store:

- source timestamp string;
- parsed instant, if valid;
- source offset and named timezone, if available;
- normalized UTC timestamp;
- display timezone chosen in the scope manifest;
- timestamp type: sent, received, created, edited, posted, due, mentioned, or retrieved;
- parse confidence and any ambiguity.

Rules:

- Never attach a timezone that the source did not supply without labeling the assumption.
- Preserve daylight-saving offsets as recorded; use an IANA timezone for display conversion when known.
- Do not treat received time as sent time.
- For date-only deadlines, store `precision=date`; do not invent a time of day.
- Resolve relative expressions such as “tomorrow” against the author's message timestamp and timezone only when both are reliable; otherwise keep the original phrase and mark the normalized due date unresolved.
- Distinguish a policy deadline, committed deadline, requested deadline, target date, meeting date, and inferred urgency.
- A later quoted copy does not change the original message's sent date.

## 12. Attachment and linked-content handling

### Attachment manifest fields

For every declared attachment, capture:

- parent message version and attachment ordinal;
- source attachment identifier;
- original and normalized filename;
- source-declared MIME type and detected type, if detection was actually run;
- byte size and content hash, if bytes were retrieved;
- inline/content-ID disposition;
- retrieval status and failure reason;
- encryption/password status;
- parse/OCR status, tool/version, page or sheet count when observed;
- extracted-text location and hash;
- handling class;
- evidence-use status.

### Safety and completeness rules

- Do not execute active content, scripts, macros, links, or embedded objects.
- Do not fetch remote images or linked documents unless explicitly in scope and authorized.
- A filename in the message proves an attachment was declared, not that its content was retrieved or reviewed.
- Treat nested `.eml` or equivalent message objects as embedded message candidates, preserving both wrapper and payload.
- Treat archive files as containers. Inventory members before extraction; prevent path traversal and decompression abuse in the implementation.
- Record password-protected and encrypted files as unreadable, not empty.
- If OCR or format conversion is unavailable, state that. Do not claim attachment analysis from filename alone.
- Verify parser output against the rendered or native file for high-impact evidence.
- Preserve sheet, slide, page, table, cell, paragraph, or object coordinates where the format supports them.

## 13. Intelligence ontology and extraction rules

### Extracted object types

| Type | Definition | Minimum evidence bar |
|---|---|---|
| `ENTITY_MENTION` | A named organization, person, system, process, product, location, document, or other approved entity | Exact mention span plus type; resolution may remain unknown |
| `ISSUE` | A matter requiring investigation, monitoring, decision, remediation, or communication | Specific described condition, not topic similarity alone |
| `DECISION` | A choice explicitly made or approved | Decision language, decision-maker attribution, date, and scope |
| `ACTION` | A concrete task someone committed or was directed to perform | Owner or `owner_unresolved`, actionable verb, source span |
| `DEADLINE` | A date/time governing an action, issue, response, or decision | Exact expression, target object, precision, and normalization basis |
| `ESCALATION_INDICATOR` | Source content that matches a documented escalation rule | Rule ID and evidence; not itself an authorized escalation |
| `RESPONSE_OBLIGATION` | A request or condition that may warrant a response | Requester, requested outcome, status, and evidence |
| `COMMITMENT` | An explicit promise by a participant | Actor, promised result, beneficiary, due date if any |
| `BLOCKER` | A dependency preventing an action or decision | Blocked object, dependency, owner if stated |
| `STATUS_UPDATE` | Evidence that an existing item changed state | Prior state, new observed statement, date, evidence |

### Commitment bar

Create an action or commitment only when the text supports a concrete act by a stated or unresolved owner. Discussion, preference, aspiration, complaint, hypothetical language, and “we should consider” do not meet the bar. Do not operationalize vague language beyond the source. A vague source action remains vague and is routed for clarification.

### Decision rules

- Separate proposed, recommended, approved, rejected, deferred, and implemented states.
- Do not label consensus from silence, attendance, or lack of objection.
- Record the decision scope and conditions; do not generalize beyond them.
- A decision to investigate is not a decision on the underlying issue.
- A later message may supersede a decision only with evidence of changed authority or state.

### Deadline rules

- Link every deadline to the item it governs.
- Preserve whether it is explicit, calculated by a stated rule, or inferred.
- Flag conflicting deadlines; never choose one silently.
- Store due date, timezone, precision, recurrence, source phrase, and calculation method.
- Compute overdue status against the run cutoff, not the current clock after the fact.
- “Urgent” without a date is priority language, not a normalized deadline.

### Escalation rules

Escalation indicators must map to a versioned rule catalog containing rule ID, triggering evidence, severity, required reviewer, destination role, clock, and closure evidence. The system may recommend or queue an escalation. A qualified human approves the escalation and its wording unless an independently approved deterministic workflow explicitly authorizes the action.

### Response-state rules

Classify separately:

- whether a response was requested;
- whether any later sent message is linked as a reply;
- whether the requested matter was substantively addressed;
- whether the thread is resolved;
- whether action remains open.

`NO_LINKED_REPLY_OBSERVED` is not “ignored.” The person may have responded through another channel, in a missing folder, or outside scope. Use `appears_unanswered_within_scope` and state the coverage basis.

## 14. Evidence spans and confidence

### Evidence span contract

Each extraction must include:

```json
{
  "evidence_id": "<stable id>",
  "source_instance_id": "<id>",
  "message_version_id": "<id>",
  "segment_id": "<id>",
  "location": {
    "representation": "<plain|html|attachment-text|table|image-ocr>",
    "start": "<character/cell/page coordinate>",
    "end": "<coordinate>"
  },
  "verbatim_excerpt": "<minimum necessary excerpt>",
  "source_fact_or_inference": "<SOURCE_FACT|NORMALIZED|INFERRED>",
  "extraction_method": "<rule id or model/prompt version>",
  "review_status": "<UNREVIEWED|CONFIRMED|CORRECTED|REJECTED>"
}
```

### Confidence scale

| Confidence | Basis | Permitted use |
|---|---|---|
| `HIGH` | Direct, unambiguous source span; strong identifiers; no material conflict | May support a reviewed finding or draft |
| `MODERATE` | Source supports the item but attribution, normalization, or context has a material caveat | Must show caveat; review before consequential use |
| `LOW` | Weak relationship, incomplete thread, ambiguous language, parser/OCR uncertainty, or single unsupported inference | Lead or review queue only |
| `NOT ASSESSABLE` | Conflicting evidence or missing required context prevents a confidence assessment | Cannot support disposition or external action; set the item or relationship status to `UNRESOLVED` |

Confidence is not severity. A consequential issue may be high severity and low confidence; report both rather than inflating either.

### Conflict handling

Preserve conflicting statements as separate observations. Create a conflict object linking the claims, sources, dates, and possible explanations. Do not “resolve” a conflict by choosing the later message, the more senior sender, or the most fluent wording. Record the reviewer decision and basis if the conflict is adjudicated.

## 15. Canonical data schemas

Use durable, typed records rather than a single prose summary. Implementations may use JSONL, relational tables, or a governed equivalent, but must preserve these concepts.

### Message schema

| Field | Description |
|---|---|
| `source_instance_id` | Unique receipt in a source/container |
| `message_id` / `message_version_id` | Logical message and observed version |
| `source_system` / `source_container_id` | Provenance |
| `transport_message_id` | Verbatim valid header when present |
| `source_conversation_id` | Verbatim source value when present |
| `parent_message_id` | Strongest supported parent, nullable |
| `relationship_confidence` | Confidence and method for parent/thread assignment |
| `subject_original` / `subject_normalized` | Source and comparison forms |
| `sender`, `from`, `reply_to`, `to`, `cc`, `bcc` | Typed participant links with source values |
| `sent_at_source`, `sent_at_utc`, `received_at_utc` | Timestamp forms and precision |
| `body_raw_ref`, `body_plain_ref`, `body_html_ref` | Content locations, not necessarily repeated content |
| `body_hash`, `content_hash` | Integrity/comparison hashes with algorithm version |
| `segment_map` | Author, quote, forward, signature, disclaimer, unknown spans |
| `attachment_count_declared` / `attachment_count_retrieved` | Completeness controls |
| `handling_class` | Information-handling rule |
| `parse_status` / `parse_errors` | Explicit processing state |
| `first_seen_run` / `last_seen_run` | Longitudinal provenance |

### Relationship schema

| Field | Description |
|---|---|
| `edge_id` | Stable relationship observation |
| `from_record` / `to_record` | Linked message, version, fragment, or thread |
| `edge_type` | `reply_to`, `references`, `forward_contains`, `quotes`, `duplicate_of`, `version_of`, `supersedes`, `candidate_thread` |
| `basis` | Header, source conversation ID, content match, or heuristic |
| `confidence` | `HIGH`, `MODERATE`, `LOW`, or `NOT ASSESSABLE` |
| `rule_version` | Relationship logic version |
| `review_status` | Unreviewed, confirmed, corrected, rejected |

### Work-item schema

| Field | Description |
|---|---|
| `item_id` / `item_type` | Stable item and ontology type |
| `canonical_title` | Concise analyst label; never replaces source wording |
| `description` | Supported description |
| `status` | Controlled state appropriate to type |
| `owner_participant_id` | Nullable; never guessed |
| `requested_by` / `decision_by` | Typed participant link where supported |
| `opened_at` / `observed_at` / `due_at` / `closed_at` | Typed dates with precision |
| `due_basis` | Explicit phrase, rule calculation, or inference |
| `severity` / `confidence` | Separate axes |
| `evidence_ids` | All supporting and contradicting spans |
| `related_item_ids` | Dependencies, blockers, duplicates, supersessions |
| `source_thread_ids` | Conversation linkage |
| `review_status` / `reviewer_role` | Human review state |
| `first_seen_run` / `last_changed_run` | Longitudinal state |

### Draft schema

| Field | Description |
|---|---|
| `draft_id` / `draft_version` | Stable proposed communication and version |
| `purpose` | Response, follow-up, escalation, update, clarification, or other approved purpose |
| `basis_item_ids` / `basis_evidence_ids` | Traceable rationale |
| `to`, `cc`, `bcc`, `from` | Proposed recipients/sender; none invented |
| `subject` / `body_plain` / `body_html` | Proposed content |
| `reply_to_message_id` / `references` | Only supplied or source-derived threading values |
| `attachments_proposed` | Explicit references; not automatically attached |
| `sensitivity_review` | Required information-handling check |
| `factual_review` | Reviewer status |
| `recipient_review` | Reviewer status |
| `approver` / `approved_at` | Null until human approval |
| `delivery_status` | `DRAFT_ONLY` until a separately authorized delivery system confirms action |
| `delivery_reference` | Null unless confirmed by the delivery system |

## 16. Reconciliation and control totals

### Source-to-output equation

At the source-instance level:

```text
records_received
= records_normalized
 + records_quarantined_before_normalization
```

At the normalized-instance level:

```text
records_normalized
= unique_logical_message_instances
 + duplicate_instances
 + non_message_objects
```

Do not subtract duplicates from received counts. They remain source instances and must be accounted for.

### Required reconciliations

| Control | Comparison | Failure treatment |
|---|---|---|
| Container coverage | Approved coverage map vs enumerated/retrieved containers | Hard gap if any in-scope container lacks a status |
| Page/chunk continuity | Requested page tokens/chunks vs received sequence | Partial run; name missing interval/token |
| Provider total | Provider-reported count vs received count under identical scope | Investigate mismatch; do not adjust silently |
| Receipt accounting | Received vs normalized + quarantined | Hard processing failure |
| Identity accounting | Normalized instances vs unique + duplicate + non-message | Hard processing failure |
| Attachment accounting | Declared vs retrieved + unavailable + excluded | Hard gap if any attachment is unaccounted |
| Parse accounting | Retrieved vs parsed + unsupported + corrupt + encrypted | Hard gap if any object lacks terminal status |
| Tracker lineage | Extracted items vs items with evidence and review status | Untraceable items blocked from release |
| Thread coverage | Messages vs assigned + deliberately unthreaded/conflicted | Never force assignment to make totals tie |
| Incremental delta | Prior state + additions + versions + removals/events = current state | Stop refresh publication on unexplained delta |

### Control-total report

Report counts by source, mailbox/workspace, folder/channel, record type, day or batch, and terminal status. Include rates as well as counts. Explain differences caused by moved messages, aliases, cross-folder copies, shared-mailbox duplication, edits, deleted records, or overlap-window reingestion.

### Completeness conclusion

Use one of:

- `COMPLETE_WITHIN_STATED_SCOPE` — all in-scope containers and objects reconcile; limitations remain visible.
- `COMPLETE_WITH_DOCUMENTED_EXCLUSIONS` — reconciliation passes after approved exclusions.
- `PARTIAL_WITH_IDENTIFIED_GAPS` — useful output exists, but one or more gaps remain.
- `NOT_RECONCILED` — control totals fail or cannot be obtained; no completeness claim.

“Complete” never means all communications that exist everywhere. It means complete within the exact authorized scope and source capabilities recorded in the manifest.

## 17. Gap, exception, and failure handling

### Gap ledger

| Field | Required content |
|---|---|
| `gap_id` | Stable identifier |
| `stage` | Scope, access, retrieval, parse, relationship, extraction, reconciliation, review, or delivery |
| `source/container/record` | Exact affected population |
| `condition` | What is missing, failed, ambiguous, or excluded |
| `first_observed` / `last_observed` | Timestamps |
| `population_impact` | Known count/rate or `unknown` |
| `downstream_impact` | Which conclusions, trackers, or drafts may be incomplete |
| `severity` | Operational severity under approved criteria |
| `owner_role` | Responsible role, not guessed person |
| `workaround` | Approved fallback, if any |
| `status` / `closure_evidence` | Open state and proof of resolution |

### Failure posture

- Missing authorization: stop that source; do not attempt an alternative identity.
- Missing current delivery: report `NO_CURRENT_SOURCE`; a prior snapshot may be shown only as stale context.
- Partial pagination: preserve the received subset, mark the exact missing continuation, and block completeness claims.
- Schema drift: quarantine affected records until mappings are reviewed.
- Corrupt or unsupported content: preserve receipt and metadata; mark unreadable.
- Encrypted attachment: record presence and route for authorized handling; do not bypass protection.
- Thread ambiguity: leave unthreaded or multi-candidate; do not merge for convenience.
- Low-confidence extraction: route to review; do not include as a confirmed tracker fact.
- Tracker write failure: do not report the tracker as updated.
- External-action uncertainty: do not retry blindly; verify status through durable action state and require approval.

Fallbacks are acceptable for continuity reporting, not for manufacturing evidence. A stale source can support “last known as of,” never a fresh conclusion. A lower-tier source must be labeled and must lower confidence.

## 18. Draft-response logic and release gates

### Determine whether a draft is warranted

A draft candidate requires all of:

1. a supported response obligation, approved proactive communication rule, or human request;
2. an identified communication purpose;
3. sufficient thread context and recipient evidence;
4. traceable facts and open items;
5. no unresolved hard gap likely to change the response materially.

Do not draft merely because a message is old, high priority, sent by a senior participant, or lacks a linked reply.

### Draft construction

Build the draft from a response brief:

| Field | Required content |
|---|---|
| Objective | What the communication should achieve |
| Audience | Proposed recipients and why each is included |
| Source message | Exact message/thread being answered |
| Questions to answer | Each explicit request mapped to a response section |
| Facts available | Supported statements and evidence IDs |
| Facts unavailable | Gaps requiring clarification or omission |
| Commitments proposed | Action, owner, and date; human approval required |
| Attachments | Proposed files and confirmed current versions |
| Sensitivity | Handling, privilege, or disclosure constraints |
| Tone/format | Purpose-driven, not inferred from hierarchy alone |

Draft rules:

- Answer each supported request directly; do not add unsupported assurances.
- Distinguish completed work, current status, planned action, and requested decision.
- Do not invent recipients, titles, approvals, deadlines, attachments, or delivery status.
- Do not quote more source content than necessary.
- Do not expose Bcc recipients or restricted source context.
- Use reply/forward headers only when the source provides the necessary identifiers.
- Include unresolved questions as reviewer notes, not polished factual claims.
- Mark assistant-composed language in the draft ledger for heightened review.
- Generate deterministic draft versions so edits are diffable.

### Release gate

No draft leaves `DRAFT_ONLY` until a human approver confirms:

- recipient and distribution-list accuracy;
- reply/forward context and threading;
- factual accuracy and source support;
- completeness against the requests in the source message;
- commitments, owners, and deadlines;
- tone and authority;
- attachment identity, version, and sensitivity;
- required legal, records, confidentiality, or subject-matter review;
- final body and subject;
- approved sending identity and time.

Delivery, if separately authorized, should use a deterministic action key and durable claim/confirm/fail state so a retry cannot duplicate a send after an ambiguous result. Failure to obtain the action claim is fail-closed. This file does not supply a sending capability.

## 19. Longitudinal refresh and tracker maintenance

### Incremental retrieval

- Begin from the last successful watermark, not the last attempted run.
- Re-read a documented overlap window to catch delayed delivery, folder moves, source corrections, and edits.
- Derive the same identity for the same logical record; a rerun must not create a new item merely because retrieval time changed.
- Track `first_seen`, `last_seen`, `first_effective`, `last_changed`, and `source_deleted_or_unavailable` separately.
- Reconcile the overlap population to the prior run before advancing the watermark.
- Advance a watermark only after retrieval receipts persist and control totals pass.

### State transitions

Use explicit, type-specific states. Example action states:

```text
PROPOSED -> CONFIRMED_OPEN -> IN_PROGRESS -> COMPLETED_PENDING_VERIFICATION -> CLOSED
                         \-> BLOCKED
                         \-> SUPERSEDED
```

Do not infer closure from silence, a later date, or disappearance from the latest extract. Require closure evidence. Preserve every transition with source, actor, timestamp, prior state, new state, and reviewer status.

### Duplicate and supersession logic for tracker items

- Consolidate only when item type, objective, evidence, and lifecycle align.
- Keep multiple observations linked to one canonical item.
- Preserve conflicting owners, dates, and statuses until reviewed.
- Use `duplicate_of` for the same item, `related_to` for connected items, and `supersedes` for an explicit replacement.
- Never erase the superseded item or its history.

### Required trackers

1. Source coverage and gap register.
2. Message/thread index.
3. Participant/alias register.
4. Issue and decision register.
5. Action, commitment, dependency, and deadline tracker.
6. Escalation-indicator review queue.
7. Draft and approval ledger.
8. Exception and incident log.
9. Run history and reconciliation trend.

## 20. Output contract

Every implementation should emit the following logical package, in governed formats appropriate to the environment:

```text
communications-intelligence/
  README-or-run-summary
  run-manifest
  source-coverage
  source-receipt-manifest
  message-index
  thread-index
  participant-register
  attachment-manifest
  issues-decisions-register
  actions-deadlines-register
  escalation-review-queue
  draft-register
  gap-exception-ledger
  reconciliation-report
  qa-report
```

Raw messages and attachment content should remain in the approved evidence store, not automatically copied into a portable summary package.

### Run summary structure

```markdown
# Communications Intelligence Run — <scope> — <cutoff>

## Disposition
<COMPLETE_WITHIN_STATED_SCOPE | COMPLETE_WITH_DOCUMENTED_EXCLUSIONS | PARTIAL_WITH_IDENTIFIED_GAPS | NOT_RECONCILED>

## Scope and Access
<sources, containers, period, timezone, content depth, exclusions, authorization reference>

## Control Totals
<received, normalized, unique, duplicate, version, quarantined, attachment and gap counts>

## What Changed
<new, updated, closed, reopened, superseded, and removed/unavailable observations since prior run>

## Priority Review Queue
<items ordered by rule-based consequence and deadline; every row has evidence and confidence>

## Issues and Decisions
<structured register view>

## Actions, Commitments, and Deadlines
<structured tracker view>

## Appears Unanswered Within Scope
<clearly labeled inference, coverage basis, and confidence>

## Drafts Awaiting Approval
<draft IDs, purposes, evidence basis, approver state; no sent claims>

## Gaps and Exceptions
<population impact and downstream limitation>

## Methods and Versions
<identity, segmentation, extraction, reconciliation, and QA versions>

## Sign-off
<operator, analyst reviewer, quality reviewer, and approval status>
```

## 21. Quality assurance

Apply [09-quality-assurance.md](09-quality-assurance.md) and at minimum test:

### Population and reconciliation tests

- every in-scope container has a terminal coverage status;
- every retrieval page/chunk is accounted for;
- receipt equations tie exactly;
- duplicate counts do not erase source-instance counts;
- every declared attachment has a terminal status;
- incremental watermarks reconcile and do not advance on partial runs.

### Record-level trace tests

Select both random and risk-based samples covering source types, folders/channels, dates, languages, multipart bodies, shared mailboxes, edits, forwards, replies, duplicates, and attachments. Trace source to normalized record, segment map, relationships, extractions, trackers, and rendered output.

### Adversarial parser fixtures

Use synthetic, non-sensitive fixtures for:

- same subject, unrelated threads;
- changed subject, valid reference chain;
- missing or duplicated transport identifiers;
- nested forwards and partial forwarding headers;
- inline replies and repeated quoted history;
- mobile signatures, disclaimers, and security banners;
- timezone boundaries and ambiguous date-only deadlines;
- source duplicates across folders and shared mailboxes;
- edited collaboration posts;
- encrypted, corrupt, oversized, and unsupported attachments;
- two people with the same display name;
- group addresses and on-behalf-of sending;
- apparent unanswered items with an out-of-scope reply;
- conflicting owners, dates, and decisions;
- partial pagination and schema drift.

### Extraction tests

- precision and recall on a reviewed fixture set by object type;
- no action from discussion below the commitment bar;
- no closure without closure evidence;
- no material item without an evidence span;
- source fact, normalization, and inference remain distinct;
- confidence decreases when thread, attachment, or source coverage is incomplete;
- critical rules and human gates cannot be bypassed by a composite score.

### Draft tests

- every explicit question in the source is answered or marked unresolved;
- every factual statement traces to evidence;
- no recipient, commitment, deadline, attachment, or approval is invented;
- thread headers match source evidence;
- all drafts remain `DRAFT_ONLY` before approval;
- a re-run produces a new version or byte-identical draft, not an untracked mutation.

## 22. Deployment patterns

Choose a pattern based on approved capability and risk.

| Pattern | Use | Control posture |
|---|---|---|
| Offline export review | Controlled periodic analysis | Hash and inventory exports; no source writes |
| Read-only connected inventory | Frequent metadata and content indexing | Least privilege, checkpoints, rate-limit handling |
| Shadow intelligence | Compare outputs with current manual process | No operational routing; measure omissions and false positives |
| Human-reviewed tracker | Maintain issues/actions with reviewer confirmation | Proposed changes queued; reviewer approves state transitions |
| Draft-only assistant | Prepare communications for human editing | No send tool or send authorization |
| Approved delivery integration | Deliver only after explicit approval | Durable action state, deterministic dedup key, fail-closed on uncertainty |

Promotion sequence: fixture validation -> historical backtest -> shadow run -> limited pilot -> controlled production -> periodic review. Define rollback, data retention, owner, monitoring, and incident response before each promotion.

## 23. Copy-ready operating prompt

```text
You are operating the Mailbox and Communications Intelligence standard.

OBJECTIVE
Inventory, preserve, normalize, reconcile, analyze, and, only if requested, draft from the authorized communications scope. Coverage and traceability take precedence over summary fluency.

INPUTS
- Purpose: <approved purpose>
- Authorization reference: <reference>
- Sources and containers: <mailboxes/folders/workspaces/channels/exports>
- Period and cutoff: <start/end/cutoff/timezones>
- Content depth: <metadata/body/headers/attachments/edits>
- Inclusions: <rules>
- Exclusions: <rules and authority>
- Prior run, state, and watermark: <references or none>
- Output audience and handling: <audience/classification/retention>
- Available read tools or supplied exports: <actual capabilities only>
- Drafting requested: <yes/no; purpose if yes>

HARD RULES
1. Do not claim access you do not have. Operate only through supplied material or explicitly available authorized tools.
2. Create the scope and run manifest first. Inventory every in-scope container and give it a terminal coverage status.
3. Retrieve through explicit exhaustion, recording pages/chunks, checkpoints, source IDs, hashes, and failures. Never shorten scope silently.
4. Preserve raw/source receipts separately. Normalize in derived fields and retain original values.
5. Keep source instance, logical message, version, thread, participant, attachment, and extracted-item identities distinct.
6. Reconstruct replies and threads using strong headers and source relationship IDs before heuristics. Subject similarity alone is low-confidence candidate evidence.
7. Segment author text, inline replies, quoted history, forwarded material, signatures, disclaimers, banners, and unclassified text. Never delete source content.
8. Account for duplicates and versions; do not erase duplicate source instances.
9. Extract entities, issues, decisions, actions, deadlines, escalation indicators, commitments, blockers, and response obligations only when the source supports them. Every material item requires an evidence span, method, confidence, and review status.
10. Never infer an owner, decision, closure, deadline, or response from silence. Label “appears unanswered within scope” as an inference.
11. Inventory every attachment and record retrieved, parsed, unreadable, encrypted, unsupported, excluded, or missing status. Do not claim analysis from a filename.
12. Reconcile source receipts, normalized records, unique messages, duplicates, versions, quarantine, attachments, and tracker lineage. If totals do not tie, mark the run NOT_RECONCILED.
13. Maintain a gap ledger with population and downstream impact. Stale or fallback data must be labeled and cannot support a fresh conclusion.
14. For refreshes, use the last successful watermark plus an overlap window. Preserve history and explicit supersession.
15. Draft only when a supported response obligation or human request exists. Do not invent recipients, facts, commitments, dates, attachments, approvals, or delivery.
16. Keep every draft DRAFT_ONLY. Do not send, post, schedule, assign, escalate, close, or alter an external system. Present required human gates.
17. Apply independent QA and return the output contract below. Do not hide gaps in prose.

OUTPUT CONTRACT
A. Run disposition and manifest
B. Scope/access and source-coverage matrix
C. Reconciliation and control totals
D. Message/thread/participant/attachment registers
E. Issues, decisions, actions, commitments, blockers, and deadlines
F. Escalation-indicator review queue
G. Appears-unanswered-within-scope queue, clearly labeled as inference
H. Draft register and approval status, if requested
I. Gap, exception, and failure ledger
J. Incremental delta from the prior successful run
K. Methods, versions, assumptions, and limitations
L. QA results and human sign-off required

If required material is unavailable, do not fabricate it. Produce the maximum defensible partial output, name the missing population, lower confidence, and block any conclusion or draft that depends on the gap.
```

## 24. Copy-ready templates

### Source coverage row

```yaml
source_container: <source/container>
scope_status: <status>
authorized_depth: <metadata/body/attachments/etc.>
period_requested: <start/end/timezone>
period_received: <start/end/timezone or none>
provider_total: <count or unavailable>
records_received: <count>
retrieval_complete_signal: <value or unavailable>
pages_or_chunks: <count>
gaps: [<gap ids>]
reconciliation_status: <pass/fail/not-testable>
```

### Extracted item row

```yaml
item_id: <stable id>
type: <issue/decision/action/deadline/escalation_indicator/response_obligation/etc.>
statement: <concise supported statement>
source_fact_or_inference: <SOURCE_FACT/NORMALIZED/INFERRED>
owner: <participant id or unresolved>
status: <controlled state>
due: <ISO value or unresolved>
due_precision: <instant/date/relative/unresolved>
severity: <tier and basis>
confidence: <HIGH/MODERATE/LOW/NOT ASSESSABLE and basis>
evidence_ids: [<ids>]
contradicting_evidence_ids: [<ids>]
review_status: <state>
first_seen_run: <run id>
last_changed_run: <run id>
```

### Draft approval record

```yaml
draft_id: <id>
draft_version: <version>
purpose: <purpose>
basis_items: [<item ids>]
recipient_review: <pending/approved/rejected>
factual_review: <pending/approved/rejected>
sensitivity_review: <pending/approved/rejected/not-required>
attachment_review: <pending/approved/rejected/not-applicable>
final_approver_role: <role>
approval_reference: <null until approved>
delivery_authorized: false
delivery_status: DRAFT_ONLY
```

## 25. Completion checklist

- [ ] Purpose, authorization, audience, handling, period, cutoff, inclusions, and exclusions are explicit.
- [ ] Every in-scope source and container has a terminal coverage status.
- [ ] Pagination/export continuity and retrieval checkpoints are recorded.
- [ ] Raw receipts and hashes exist; normalized values do not overwrite source values.
- [ ] Message, instance, version, thread, participant, attachment, and item IDs follow documented rules.
- [ ] Replies, forwards, quotes, duplicates, versions, signatures, and disclaimers are handled explicitly.
- [ ] Participants and timestamps retain source values and resolution uncertainty.
- [ ] Every declared attachment has a terminal status.
- [ ] Every material extraction has an evidence span, confidence, method, and review status.
- [ ] Conflicts and low-confidence relationships remain visible.
- [ ] All control totals reconcile or the run is marked partial/not reconciled.
- [ ] Incremental changes reconcile to the prior successful run.
- [ ] Tracker transitions preserve history and closure evidence.
- [ ] Drafts contain no invented facts, recipients, commitments, deadlines, or delivery claims.
- [ ] External actions remain behind explicit human approval and durable deduplication controls.
- [ ] Gaps state population and downstream impact.
- [ ] Independent QA and sign-off are recorded.
