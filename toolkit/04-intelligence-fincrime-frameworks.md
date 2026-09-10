# Intelligence and Financial-Crime Frameworks

Use this module to classify a problem, select the right risk lens, identify relevant
typologies, and convert raw signals into a defensible intelligence product. Pair it with:

- [`00-operating-system.md`](00-operating-system.md) for authority and task lifecycle;
- [`01-evidence-research-standard.md`](01-evidence-research-standard.md) and
  [`02-osint-source-register.md`](02-osint-source-register.md) for external evidence;
- [`05-investigation-control-methods.md`](05-investigation-control-methods.md) for case,
  screening, testing, and decision procedures;
- [`06-data-quality-governance.md`](06-data-quality-governance.md) for structured data;
- [`07-output-templates.md`](07-output-templates.md) and
  [`09-quality-assurance.md`](09-quality-assurance.md) for release.

This is a general analytical reference, not legal advice, an approved surveillance
model, or a replacement for current policy. Confirm jurisdiction-specific requirements
against the issuing authority as of the analysis date.

## 1. Start with the analytical object

Do not begin by choosing a score or searching for adverse facts. First classify what is
being assessed.

| Object | Examples | Primary question | Typical output |
|---|---|---|---|
| Person | customer, principal, director, beneficial owner | Is the identity resolved, and what risk-relevant roles or conduct attach to this person? | identity or screening disposition |
| Legal entity | customer, counterparty, issuer, vendor | What does the entity do, who controls it, where does it operate, and what is its risk? | entity risk assessment |
| Relationship | ownership, control, payment, employment, agency | Is the relationship real, material, current, and risk-relevant? | network or ownership analysis |
| Transaction or event | payment, trade, login, filing, enforcement action | What happened, is it expected, and what response does it require? | alert disposition or event brief |
| Account or wallet | bank account, custody account, blockchain address | Who controls it, how is it used, and what patterns appear? | activity analysis or fund-flow trace |
| Product or service | payments feature, market, token, onboarding channel | What inherent risks, obligations, controls, and residual exposures arise? | product or new-activity risk assessment |
| Control or model | screening rule, monitoring scenario, QA control | Is it designed appropriately and operating effectively? | control assessment or validation workpaper |
| Jurisdiction | country, territory, subnational region | Which risk factors are evidenced, current, and relevant to the use case? | jurisdiction profile |
| Population | mailbox, alert queue, customer book, control inventory | Is coverage complete, and what segments or outliers require attention? | tracker, dashboard, or portfolio review |
| Regulatory development | law, rule, guidance, enforcement, speech | What changed, who is affected, when, and what response is required? | regulatory alert or obligation register |

Record the primary object and any linked objects in the run manifest. Scoring a person
with an entity model, a passive investor with an operator model, or an allegation with a
confirmed-event model creates systematic error.

## 2. Intelligence lifecycle

Use one lifecycle across domains:

1. **Direct:** define the decision, priority intelligence requirements, scope, authority,
   and materiality.
2. **Collect:** acquire the best available evidence through a documented source plan.
3. **Preserve:** retain source identity, time, version, evidence spans, and raw values.
4. **Process:** normalize, deduplicate, translate, resolve identities, and reconcile.
5. **Analyze:** test hypotheses, link entities and events, quantify patterns, and seek
   disconfirming evidence.
6. **Assess:** state severity, confidence, implications, and alternative explanations.
7. **Disseminate:** render for the decision-maker with source and limitation visibility.
8. **Act or escalate:** route recommendations through the authorized human gate.
9. **Learn:** capture outcomes, false positives, missed signals, source failures, and
   framework changes.

An output that skips preservation and processing may look complete while being
impossible to reproduce. An output that skips disconfirming evidence is advocacy, not
analysis.

## 3. Common analytical vocabulary

### 3.1 Claim class

| Class | Meaning | Required treatment |
|---|---|---|
| Observed | Directly shown by admissible evidence | State fact and cite exact support |
| Reported or alleged | Claimed by a named source but not established | Attribute, preserve procedural status, seek corroboration |
| Inferred | Analytical conclusion drawn from observed inputs | State reasoning, alternatives, and confidence |
| Projected | Forward-looking estimate or scenario | State assumptions, horizon, sensitivity, and uncertainty |

### 3.2 Severity

| Tier | Meaning | Default response |
|---|---|---|
| CRITICAL | Active or imminent material harm; confirmed disqualifying fact; or urgent statutory/operational deadline | Immediate authorized escalation; preserve evidence; no automated closure |
| HIGH | Significant evidenced exposure, control failure, or strong adverse signal | Near-term review, containment, or remediation |
| MEDIUM | Genuine issue with moderate impact, uncertainty, or effective mitigation | Track, investigate proportionately, assign review date |
| LOW | Informational, minor, remote, or well-controlled item | Record for context; no action unless pattern changes |

Severity measures consequence and urgency. It is not source credibility, probability,
or confidence. When a tier is arguable, the discriminators are evidence and time:
evidenced exposure with a near-term clock is HIGH, not MEDIUM, while uncertainty alone
without evidenced exposure is MEDIUM, not HIGH. Record the discriminating fact next to
the tier.

### 3.3 Confidence

| Rating | Evidence condition |
|---|---|
| HIGH | Direct observation or multiple independent, consistent, authoritative sources; material identity ambiguity resolved |
| MODERATE | One strong primary source, partial corroboration, or a bounded inference with material caveats |
| LOW | Secondary-only support, unresolved identity or timing, incomplete population, or fragile inference |
| NOT ASSESSABLE | Evidence is insufficient, inaccessible, internally inconsistent, or outside authorized scope; do not force a rating |

Always add a reason: `MODERATE — ownership is documented in one current registry, but
the upstream holding entity could not be independently corroborated.`

Use `speculative` for a hypothesis or scenario that lacks direct evidence, not as a
confidence score. Use `unresolved` for a disposition when the available evidence cannot
support a decision.

### 3.4 Analytical status

Keep status separate from severity and confidence:

`new -> triaged -> investigating -> pending information -> escalated -> decided ->
remediating -> closed -> reopened`

Use `closed` only with a documented decision, owner, date, and evidence. A case is not
closed merely because no new information arrived.

## 4. Typology-analysis method

A typology is a recurring pattern that guides inquiry. It is not proof that a specific
person or transaction is illicit.

For each candidate typology:

1. Define the protected objective and harmful mechanism.
2. Identify observable indicators across customer, account, transaction, device,
   counterparty, geography, communications, and external intelligence.
3. Separate necessary conditions from optional indicators.
4. Identify common legitimate explanations and segment-specific baselines.
5. Specify the evidence required to confirm or refute the pattern.
6. Map indicators to preventive, detective, and corrective controls.
7. Record coverage gaps, thresholds, exclusions, and known blind spots.
8. Test performance using labeled data or structured review; never assume face validity.
9. Define escalation and closure conditions.

Use this record:

```yaml
typology_id: TYP-<domain>-<number>
name: <descriptive name>
harm: <objective or asset at risk>
mechanism: <how the pattern works>
stages: []
indicators:
  customer: []
  transaction: []
  network: []
  communications: []
  external: []
necessary_conditions: []
legitimate_explanations: []
evidence_to_confirm: []
evidence_to_refute: []
covered_controls: []
coverage_gaps: []
escalation_conditions: []
closure_conditions: []
owner: <role>
version: <semantic version>
as_of: <date>
```

## 5. Cross-domain indicator library

Indicators gain meaning through combinations, sequence, and context. A single indicator
rarely supports a conclusion.

| Dimension | Illustrative indicators | Evidence to seek | Frequent benign explanations |
|---|---|---|---|
| Identity | inconsistent name/date/address; reused credentials; synthetic attributes; unexplained aliases | authoritative ID/registry record, prior profile, device history | transcription, transliteration, legal name change, shared household |
| Ownership and control | opaque layers; nominees; rapid ownership change; common controller across entities | registry filings, shareholder records, control rights, director history | investment structure, trust/estate planning, acquisition |
| Geography | high-risk corridor; unusual IP/location; sanctioned or conflict nexus; secrecy jurisdiction | origin/destination, residency, operating footprint, source reliability | travel, cross-border trade, remote work, correspondent routing |
| Product/channel | use inconsistent with stated purpose; rapid adoption of high-velocity feature | product logs, onboarding purpose, peer baseline | seasonal use, business expansion, channel migration |
| Transaction velocity | rapid in/out; pass-through; circular movement; burst after dormancy | complete chronological ledger, balances, counterparties | treasury sweep, settlement cycle, marketplace payout |
| Value and structuring | repeated near-threshold amounts; round-dollar patterns; fragmentation | thresholds, aggregation windows, cash/source records | billing increments, payroll, limits, installment schedules |
| Counterparty | newly created, unrelated, high-risk service, shared with known cases | counterparty profile, ownership, network and case links | marketplace, processor, correspondent, common vendor |
| Device/network | many accounts per device; impossible travel; anonymization; credential change | device fingerprint, IP history, authentication and recovery logs | household/device sharing, VPN, carrier routing, corporate gateway |
| Communications | urgency, secrecy, off-channel direction, evasion language, inconsistent rationale | full thread, attachments, neighboring messages, policies | informal shorthand, legitimate confidentiality, time-sensitive operations |
| External intelligence | enforcement, litigation, designation, regulatory warning, credible adverse reporting | original order/docket/list/filing and current status | name collision, withdrawn action, historical issue with remediation |
| Behavior change | deviation from own history or peer segment | baseline window, seasonality, product changes | life event, acquisition, new contract, corrected data |
| Control response | alerts repeatedly suppressed; overrides; missing evidence; aging backlog | rule/version history, decisions, reviewer and SLA logs | approved tuning, documented risk acceptance, outage recovery |

## 6. Money-laundering and terrorist-financing typologies

### 6.1 Transaction and account patterns

| Typology | Core pattern | Signals to combine | Key false positives | Evidence and response |
|---|---|---|---|---|
| Structuring or smurfing | Value is fragmented to avoid attention, thresholds, or reporting | repeated near-threshold activity; multiple channels/locations; short aggregation window; common beneficiary | cash-intensive business, deposit limits, invoice installments | aggregate across accounts/time; compare declared activity; establish source and purpose |
| Funnel account | Dispersed deposits are concentrated and withdrawn or transferred elsewhere | remote deposits; geographic dispersion; rapid withdrawal; little local activity | national sales network, franchising, collections service | map origin locations and actors; test commercial rationale; review linked accounts |
| Rapid movement or pass-through | Funds enter and leave with little retained balance or economic activity | high turnover; same-day outflow; repeated intermediaries; thin stated purpose | settlement, brokerage, treasury management, payment processing | calculate dwell time and turnover; inspect contract and business model; trace destination |
| Layering through multiple accounts | Funds move across related accounts/entities to obscure origin | circular routes; common control; repeated round amounts; unnecessary intermediaries | cash pooling, intercompany financing, escrow | build ownership/payment network; identify economic purpose at each hop |
| Circular or round-trip activity | Funds or securities return to origin or related party | repeated loops; offsetting entries; minimal economic change | liquidity management, market-making, corrections | reconstruct full loop; quantify fees/losses; test independence of parties |
| Dormant-to-active burst | Inactive account suddenly receives and disperses material value | long dormancy; profile change absent; new device/counterparties | sale, inheritance, funding round, account reactivation | validate source of funds, profile update, device and counterparty links |
| Cash-intensive commingling | Illicit value is mixed with legitimate cash receipts | deposits inconsistent with location/industry; round amounts; cash-to-wire conversion | legitimate high-cash business, events, seasonality | benchmark peers; inspect sales/tax records; reconcile cash to operations |
| Trade-based laundering | Trade price, quantity, quality, routing, or documentation transfers value | invoice mismatch; dual invoicing; unusual route; phantom shipment; third-party payment | commodity volatility, Incoterms, partial shipment, supply disruption | reconcile contract/invoice/shipping/customs/payment; verify parties and goods |
| Shell or front company | Entity with limited substance intermediates ownership or payments | shared address/directors; thin staffing; unclear revenue; unrelated transactions | holding company, SPV, early-stage business, registered-agent address | establish purpose, operations, ownership/control, financial and tax evidence |
| Professional laundering network | Specialized intermediaries move value for multiple unrelated actors | common counterparties/devices; many-to-many flows; fee-like retention | payment processor, marketplace, remittance operator | license/status review; network centrality; customer and transaction sampling |
| Correspondent or nested access | Respondent provides indirect access to undisclosed downstream institutions or customers | payable-through behavior; high-risk corridors; respondent unable to identify originator | ordinary correspondent chain, processor arrangement | map access chain; assess respondent controls; sample originator/beneficiary transparency |
| Informal value transfer | Value settles outside conventional account-to-account paths | reciprocal transfers; family/business networks; cash settlement; corridor concentration | remittance, family support, rotating savings group | understand network role, settlement mechanism, licensing, source and beneficiary |
| Third-party funding | Person or entity not in the stated relationship supplies or receives funds | unrelated payer; repeated refund to new destination; many customers sharing funder | payroll, sponsor, escrow, marketplace, family payment | verify relationship, authority, contractual purpose, beneficial ownership |
| Monetary-instrument cycling | Cashier's checks, prepaid value, stored value, or similar instruments obscure trail | repeated purchase/redemption; multiple issuers; rapid liquidation | travel, payroll, unbanked use, gift programs | obtain instrument chain and purchaser/beneficiary data; aggregate across products |
| Gaming or gambling value cycling | Funds are converted to gaming value and redeemed with limited play | high buy-in/low play; coordinated accounts; repeated withdrawals | legitimate high-value player, bonus strategy | compare play-to-funding; identify linked accounts/payment methods; source wealth review |
| Insurance or investment-product misuse | Premiums/contributions are quickly surrendered, borrowed, or transferred | early surrender; third-party premium; unexplained beneficiary change | changed financial need, estate planning, portfolio rebalancing | trace funder/beneficiary; review advice and product economics |
| Charitable or nonprofit misuse | Funds are diverted, passed through, or sent to high-risk actors/areas | vague programs; weak governance; cash movement; related-party vendors | emergency relief, field operations, cash-based local delivery | verify program, governance, beneficiaries, partners, sanctions and expenditure evidence |
| Terrorist financing | Funds, often small, support designated or violent activity | linked actors; high-risk geography; fundraising language; travel/logistics pattern | diaspora support, legitimate charity, religious donation | apply legal/authorized escalation; preserve links; do not infer intent from religion or nationality |

### 6.2 Fraud and scam typologies

| Typology | Mechanism | Signals | Alternative explanations | Core response |
|---|---|---|---|---|
| Authorized push-payment scam | Victim is manipulated into authorizing transfer | new payee; urgency; impersonation; remote-access evidence; victim contact | genuine urgent purchase or family transfer | rapid hold/recall where authorized; victim verification; beneficiary network review |
| Business-email compromise | Attacker redirects business payment through compromised or spoofed communication | payment-instruction change; lookalike domain; secrecy; new account | legitimate vendor bank change | out-of-band verification; preserve headers/thread; review beneficiary links |
| Account takeover | Unauthorized actor gains access and transacts | credential/device change; impossible travel; MFA reset; rapid cash-out | replacement device, travel, shared corporate access | secure account; authenticate customer; device/network investigation; recover funds where possible |
| Identity theft | Real person's attributes are used without authorization | identity mismatch; credit/application anomalies; victim report | data-entry error, legitimate representative | confirm identity and authority; restrict access; preserve application/device evidence |
| Synthetic identity | Real and fabricated attributes are combined to build a false profile | thin file; reused identifiers; coordinated applications; gradual limit growth | young/new-to-country/thin-file customer | cross-source identity checks; device/address network; avoid demographic proxies |
| Mule account | Account receives and forwards proceeds for others | many unrelated credits; rapid onward transfers; victim-linked origins; recruitment communications | gig/platform seller, collections, remittance | identify recruitment/control; trace funds; assess vulnerability and complicity separately |
| First-party fraud | Applicant or customer intentionally misrepresents identity, income, purpose, or dispute | contradictory evidence; bust-out pattern; coordinated accounts | hardship, dispute confusion, inconsistent third-party data | document intent evidence cautiously; distinguish inability from deception |
| Check fraud | Altered, counterfeit, duplicate, or fraudulently endorsed item is deposited | image anomalies; rapid withdrawal; duplicate serial; payee mismatch | scanning error, legitimate reissue | verify item/issuer/payee; compare images and presentment history; contain funds if authorized |
| Wire/payment fraud | Unauthorized or deceptively induced transfer | instruction anomaly; beneficiary risk; device change; unusual timing/value | legitimate acquisition, closing, treasury movement | verify authority and purpose; attempt recall under approved process; trace beneficiary |
| Romance/investment confidence scam | Relationship or investment story induces repeated payments | escalating transfers; secrecy; platform migration; crypto purchase; recovery scam | legitimate relationship or investment | sensitive victim engagement; trace destinations; preserve communications; avoid blaming language |
| Merchant or refund abuse | False purchases, collusion, or refund routing extracts value | high refund ratio; refund to different instrument; related merchant/customer | returns-heavy segment, operational correction | reconcile sales/shipping/refunds; network links; segment baseline |
| Insider-enabled fraud | Authorized employee or contractor abuses access or overrides | unusual overrides; collusion links; off-hours access; control bypass | operational urgency, coverage role, training gap | preserve access logs; separate investigation authority; limit disclosure; legal/HR gate |

Fraud disposition is dual-sided: a missed fraud and a false decline both harm real
people, so both error rates carry explicit gates rather than only the fraud-miss rate.
Reserve unconditional approval for sessions where every continuity fact holds (known
device, strong authentication, no recent credential or contact change, established
beneficiary); route uncertain cases to step-up authentication, which is a
non-adverse outcome, before any decline. An adverse action needs corroborating
typology evidence, not a single anomalous signal.

## 7. Sanctions, proliferation, and export-control risk

### 7.1 Exposure mechanisms

| Mechanism | What to test | Evidence required |
|---|---|---|
| Direct designation | Exact person/entity/vessel/address appears on an applicable list | current official list record, identifiers, program, effective date |
| Ownership or control | Designated persons own or control an unlisted entity under the applicable regime | complete ownership/control chain, percentages, agreements, applicable rule |
| Sectoral restriction | Activity, debt/equity tenor, goods, or services fall within a targeted restriction | program text, transaction terms, entity classification, dates |
| Geographic restriction | Activity has a prohibited location, origin, destination, government, or territorial nexus | location and routing evidence, program scope, exemptions/licenses |
| Facilitation or evasion | Intermediaries, transshipment, front companies, re-documentation, or payment routing conceal nexus | sequence, counterparties, trade documents, beneficial owners, communications |
| Maritime evasion | Vessel identity manipulation, ship-to-ship transfer, route anomaly, flag/ownership change | IMO identity, AIS history, port calls, ownership/management, cargo records |
| Dual-use/proliferation | Goods, technology, end user, or route creates controlled or proliferation concern | item classification, end-use/end-user, license status, shipping/customs evidence |
| Digital-asset nexus | Listed address, sanctioned service, or attributed actor interacts with funds | official designation details, chain/asset, transaction hashes, attribution basis |

### 7.2 Screening discipline

1. Identify the applicable lists and the exact as-of time.
2. Normalize names and identifiers without destroying originals.
3. Generate candidates using approved fuzzy/transliteration rules.
4. Resolve candidates using independent attributes: birth date, location, nationality,
   registration number, address, role, vessel identifiers, or wallet evidence.
5. Test ownership/control and indirect exposure separately from direct name matching.
6. Document false-positive rationale using mismatching decisive attributes, not a low
   name score alone.
7. Escalate unresolved plausible matches. Never auto-clear a possible true match solely
   because data is missing.
8. Preserve list version, matcher version, threshold, input, candidates, and reviewer.

Do not redistribute list records as sample data. Link to official sources and use
synthetic examples.

## 8. Corruption, bribery, and third-party risk

| Pattern | Indicators | Evidence and questions |
|---|---|---|
| Government-intermediary risk | public-official nexus; high commission; vague services; payment offshore | What service was delivered? Is compensation proportionate? Who owns and controls the intermediary? |
| Procurement manipulation | tailored requirements; single bid; split purchases; rotating winners | Compare bids, specifications, timing, approvals, ownership, and conflicts |
| Gifts, travel, entertainment | repeated high-value benefits; proximity to decision; inaccurate coding | Who received value, for what purpose, under which approval and limit? |
| Charitable or political contribution | contribution requested by official/customer; linked beneficiary | What is the legitimate purpose, governance, ultimate beneficiary, and decision nexus? |
| Facilitation payment or unofficial fee | cash or vague charge to speed routine action | What law/policy applies, who requested it, and was emergency/duress documented? |
| Books-and-records concealment | vague invoices, false descriptions, round amounts, manual override | Do contract, invoice, approval, delivery, ledger, and recipient align? |
| Conflict of interest | employee/official/vendor ownership or family link | Was it disclosed, independently approved, and managed? |
| Third-party concentration | critical activity relies on opaque or weakly controlled intermediary | Is due diligence current, scope clear, subcontracting known, monitoring effective? |

Political exposure is a risk factor, not evidence of wrongdoing. Record the position,
relationship, jurisdiction, dates, source, and risk-relevant authority. Apply enhanced
review proportionately and avoid adverse conclusions based only on status.

## 9. Market and communications surveillance

| Typology | Market behavior | Communications or contextual signals | Key controls against false positives |
|---|---|---|---|
| Insider dealing | trading before material event; profitable deviation; related accounts | access to information, deal codewords, source/contact timing | event window, trading history, role/access map, pre-clearance |
| Front-running | employee/client-aware order precedes customer or house order | knowledge of order, timing, benefit, linked account | latency and routing analysis; role and mandate; market movement |
| Spoofing/layering | non-bona-fide orders create false depth and are canceled | intent language, repeated side-switch, cancel-to-fill pattern | liquidity provision, algorithm design, market conditions |
| Wash trading | common control trades with itself or coordinated parties | ownership/device/communications links; no economic change | market-making, internal crossing, transfer of beneficial ownership |
| Marking close/open | trading influences reference price near benchmark window | benchmark-linked incentive or direction | liquidity, rebalancing, index events, execution mandate |
| Pump-and-dump | promotion precedes coordinated buying and disposal | promotional messages, undisclosed interest, account network | genuine news, broad market movement, independent positions |
| Misuse of confidential information | restricted information is shared or used improperly | channel, recipients, access rights, timing | approved wall-crossing, documented need-to-know, public availability |
| Off-channel or evasive communications | business moves to unapproved channel or uses concealment language | device/channel metadata, deletions, repeated direction to move | outage, approved alternate channel, personal/nonbusiness content boundaries |
| Collusion or bid/quote coordination | competitors coordinate prices, allocation, or participation | repeated contact and patterned outcomes | legitimate syndication, public signals, common market conditions |

Surveillance signals require context. A statistically unusual trade is not proof of
intent; a concerning message is not proof that a trade occurred. Join order, trade,
position, event, access, employee, and communication evidence before concluding.

## 10. Digital-asset entity and activity frameworks

### 10.1 Classify the entity before scoring

| Family | Examples | Central question | Dominant risks |
|---|---|---|---|
| Custodial or centralized service | exchange, broker, custodian, hosted wallet, payment processor | Is the service authorized, controlled, solvent, and transparent for every activity and jurisdiction? | regulatory, sanctions, customer asset, liquidity, governance |
| Issuer or financial product | stablecoin, token issuer, lending/yield product, fund | What rights, reserves, obligations, conflicts, and failure paths exist? | financial, disclosure, legal, redemption, market integrity |
| Protocol-native or decentralized | DeFi protocol, bridge, mixer/privacy tool, DAO, staking protocol | Who controls material functions and front ends; how do governance and code risks allocate accountability? | governance, exploit, sanctions, oracle, concentration |
| Infrastructure | analytics, nodes, software, mining, validators | Does it control customer assets or transactions, and what operational dependencies arise? | technology, concentration, geographic, vendor |
| Traditional entity with exposure | bank, fintech, treasury holder, merchant, service vendor | How material is the exposure and which activities create regulated obligations? | financial, operational, counterparty, disclosure |

Do not apply service-provider licensing tests to an entity that merely holds an asset.
Do not assume a protocol lacks accountable persons merely because its interface is
described as decentralized.

### 10.2 On-chain typologies

| Typology | Transaction pattern | Required context |
|---|---|---|
| Mixer or privacy-service exposure | deposit, denomination pattern, delay, and withdrawal through obfuscation service | service identity/status as of time, direct vs indirect hops, asset/chain, legitimate privacy uses |
| Chain hopping | value crosses assets or networks through bridges/swaps | bridge route, timing, equivalent value, address attribution confidence |
| Peel chain | repeated small transfers peel from a moving balance | ownership hypothesis, transaction sequence, change-address behavior |
| Address hopping | value rapidly moves through newly created or low-history addresses | timing, address reuse, gas funding, common counterparties |
| Nested-service exposure | customer transacts through account at another VASP or broker | hosted vs unhosted status, service relationship, underlying customer visibility |
| Sanctioned-address exposure | direct or indirect flow touches officially attributed address | list version, transaction time, attribution source, ownership and intervening service |
| Ransomware/extortion flow | victim payment consolidates, swaps, bridges, or reaches cash-out service | incident attribution, payment demand, chain trace, service response |
| Scam proceeds aggregation | many victim-linked deposits consolidate and cash out | victim reports, common deposit pattern, communications, off-chain beneficiary |
| Theft or exploit laundering | exploit address disperses through swaps, bridges, services | exploit transaction, ownership attribution, trace continuity, asset-price method |
| DeFi flash-loan/manipulation | borrowed liquidity affects oracle/price or governance before repayment | transaction call trace, protocol mechanics, economic outcome, code/market context |
| NFT wash trading | linked wallets repeatedly trade asset to create volume or price | funding links, beneficial control, fees, marketplace incentives |
| Mining-pool or validator laundering | attributed illicit funds are represented as mining/staking proceeds | pool/validator relationship, reward records, timing, ownership |
| Cross-chain layering | repeated bridges, swaps, and services fragment trail | complete cross-chain mapping, fees/slippage, attribution confidence at each hop |

On-chain observations show transaction mechanics, not necessarily beneficial ownership or
intent. State attribution source, directness, hop count, asset, chain, timestamp, value
method, and confidence. Preserve transaction hashes and do not treat a vendor label as a
confirmed identity without understanding its method and date.

When a vendor export reports indirect exposure without a hop distance, treat distance as
unknown and route to review; never substitute an assumed hop count to reach a
disposition, because remoteness that cannot be shown cannot be relied on. Separate
structural noise from signal with named observations before interpreting flows: dust and
spam deposits below defined value floors, self-transfers between addresses under common
control, and high-frequency same-counterparty churn each distort volume and counterparty
counts if left unlabeled.

### Reproducible ledger scope

For a fund-flow calculation, pin chain/network, asset identifier, block range and
canonical block references, transaction status, base units, decimal conversion,
and valuation timestamp. Do not join assets by ticker alone. Keep failed execution,
internal movement, fees, and duplicate logs in declared separate buckets. Record
whether finality was checked for the chosen network; later reorganizations require
reconciliation and a versioned correction. Unknown finality, valuation, or attribution
remains a limitation, not a zero balance or a verified owner.

### 10.3 Protocol risk domains

Assess at least:

- governance and administrative-key control;
- smart-contract design, audits, exploit history, and upgradeability;
- oracle, bridge, validator, sequencer, or relayer dependencies;
- liquidity, concentration, leverage, collateral, and liquidation behavior;
- token rights, distribution, incentives, and market integrity;
- custody, reserves, segregation, redemption, and bankruptcy treatment;
- sanctions and financial-crime controls at controlled interfaces;
- legal entities, developers, foundations, DAOs, front ends, and geographic nexus;
- operational resilience, incident response, disclosures, and user protection.

## 11. Jurisdiction-risk framework

Jurisdiction risk is use-case dependent. A country can present different risk for cash,
correspondent banking, securities, bribery, data protection, or digital assets.

| Domain | Questions | Source families |
|---|---|---|
| AML/CFT effectiveness | What do recent mutual evaluations and follow-ups show? | FATF-style bodies, national assessments, supervisors |
| Sanctions and conflict | Which applicable measures, conflicts, or occupied territories create exposure? | sanctions authorities, UN, official advisories |
| Corruption and governance | What official enforcement, governance, procurement, and audit evidence exists? | courts, prosecutors, audit offices, procurement portals |
| Financial transparency | Are ownership, corporate, tax, and accounting records accessible and reliable? | registries, tax/customs bodies, statistical offices |
| Predicate crime | Which fraud, trafficking, cyber, tax, organized-crime, or environmental risks are evidenced? | law enforcement, national risk assessments, international bodies |
| Regulatory capacity | Are supervisors independent, resourced, and active? | supervisory reports, assessments, enforcement records |
| Market and capital controls | Are currency, transfer, securities, or banking restrictions material to the activity? | central bank, securities regulator, finance ministry |
| Digital-asset regime | What licensing, prohibition, travel-rule, or supervisory requirements apply? | legislature, financial supervisor, central bank |
| Legal and records reliability | Can rights, judgments, filings, and enforcement be verified? | official gazettes, courts, registries |
| Data and operational risk | Do privacy, localization, cyber, infrastructure, or access constraints affect the process? | data regulator, cyber agency, telecom/statistics authorities |

Score only evidenced factors relevant to the use case. Record source date and review
cadence. Do not convert a composite country index into a conclusion about a person.

Public designations act as categorical raise-only floors that no composite score can
dilute: comprehensive sanctions on the jurisdiction floor the rating at the highest
tier; a FATF call-for-action listing floors it at the highest tier; FATF increased
monitoring and the EU high-risk third-country list each floor it at a high tier. Compute
the floor over the jurisdictions actually designated at the assessment date, cite the
designation instrument, and show the pre-floor score alongside the floored rating.
Exclude a missing dimension from the weighted denominator rather than scoring it as zero
or a midpoint.

## 12. Entity and counterparty risk framework

Use a multi-domain assessment. Tune weights to the stated risk appetite; never hide
weight changes.

| Domain | Core questions | Typical evidence |
|---|---|---|
| Identity and legal existence | Is the entity real, active, and correctly identified? | authoritative registry, license, tax/identifier record |
| Ownership and control | Who ultimately owns, controls, appoints, or benefits? | ownership chain, voting/control rights, filings |
| Business model and purpose | How does value move and how is revenue earned? | contracts, filings, website corroboration, financials |
| Products and channels | Which services, custody, credit, markets, or delivery methods create exposure? | product terms, flow diagrams, operating data |
| Customer/counterparty base | Who uses the service and how is access controlled? | segment data, eligibility, due-diligence framework |
| Geography | Where are customers, operations, assets, payments, and control located? | footprint, transaction data, licenses, counterparties |
| Regulatory standing | Which permissions attach and are they current? | regulator/license registers, orders, filings |
| Sanctions and political exposure | Do direct, ownership/control, geographic, or role-related risks exist? | applicable official lists and authoritative role sources |
| Enforcement and litigation | What is the allegation, procedural posture, outcome, and remediation? | original orders, dockets, judgments, settlements |
| Financial condition | Can obligations be met and assets protected? | audited financials, regulatory reports, attestations |
| Governance and controls | Are accountability, independence, policies, monitoring, and audit credible? | governance records, control evidence, assurance reports |
| Adverse information | What credible reporting affects integrity, conduct, or viability? | primary records and corroborated high-quality reporting |
| Technology and operations | Are critical services resilient and controlled? | architecture, incidents, audits, continuity tests |
| Third-party concentration | Which vendors, banks, custodians, or affiliates are critical? | contracts, concentration data, due diligence |

### Scoring discipline

- Define scales, anchors, weights, missing-data treatment, floors, overrides, and rating
  bands before scoring.
- Score a domain from evidence, not from the desired overall outcome.
- Missing evidence reduces confidence. It is not automatically adverse unless the
  evidence is required and the entity failed to provide it after a documented request.
- A confirmed disqualifying fact may trigger a documented override. Keep the underlying
  weighted score visible.
- Use score floors only for pre-defined confirmed conditions. A floor is a minimum, not
  a substitute for analysis. Typical named floors in published open implementations:
  confirmed political exposure floors the rating at no lower than the middle band;
  a prior regulatory filing on the subject, confirmed adverse media, or an opaque
  shell structure floors it at the high band. Label any adopted floor set as policy
  once approved, and record who approved it.
- Maintain any prohibited list as routing, not scoring: a prohibited attribute routes
  the case out of the scoring path entirely, so there is no score at which it passes.
- Run sensitivity as a defined test, for example moving any single domain by one band
  and any single weight by a tenth of its value; report whether either movement changes
  the final rating, and treat a rating that flips inside that envelope as
  decision-fragile.
- Calibrate against historical reviewed cases and monitor outcomes and overrides.
- Verify monotonicity after any change: raising one risk factor may never lower the
  final rating.

Example calculation:

```text
domain_score = sum(indicator_score x indicator_weight) / sum(applicable_weights)
composite = sum(domain_score x domain_weight) / sum(applicable_domain_weights)
final_rating = apply_predefined_floors_and_overrides(composite)
```

Do not calculate missing indicators as zero. Exclude them from the denominator or apply
an approved conservative treatment, and disclose which method was used.

## 13. Product and new-activity risk framework

Assess a proposed or changed product across the full lifecycle:

| Domain | Questions |
|---|---|
| Customer and eligibility | Who can access it, and what misuse or vulnerability risks arise? |
| Value movement | How does value enter, move, settle, reverse, and exit? |
| Geography and legal entity | Which customers, entities, booking locations, and service locations create nexus? |
| Financial crime | Which AML/CFT, sanctions, fraud, corruption, and evasion typologies are enabled? |
| Market conduct | Could features enable manipulation, conflicts, misuse of information, or unfair outcomes? |
| Data and privacy | Which CDEs, consents, transfers, retention, and automated decisions arise? |
| Technology and cyber | Which identities, keys, vendors, APIs, models, and failure modes are critical? |
| Operations | How are exceptions, disputes, reconciliation, support, and business continuity handled? |
| Third parties | Which outsourced services or embedded partners create dependency or indirect access? |
| Accounting and financial | How are revenue, assets, liabilities, reserves, liquidity, and capital affected? |
| Regulatory permissions | Which current laws, licenses, filings, disclosures, and conditions apply? |
| Controls and monitoring | Which preventive/detective controls, KRIs, testing, and escalation exist at launch? |

Require traceability from risk to control to test to launch condition. A launch-readiness
rating cannot be HIGH when a mandatory control lacks an owner, evidence, or tested
operating procedure.

## 14. Regulatory-intelligence framework

For every development, answer:

1. **Instrument:** law, proposed/final rule, guidance, enforcement, decision, speech,
   consultation, list change, or supervisory communication.
2. **Authority:** issuer, legal basis, jurisdiction, and binding status.
3. **Change:** exact difference from prior state; separate proposal from final rule.
4. **Scope:** affected entities, products, activities, thresholds, and exemptions.
5. **Timeline:** publication, effective, comment, transition, compliance, and review dates.
6. **Obligation:** actor, required/prohibited action, trigger, object, condition, timing,
   evidence, and consequence.
7. **Impact:** policies, procedures, systems, data, controls, contracts, reporting, and
   training affected.
8. **Action:** owner, deliverable, dependency, due date, and approval.
9. **Uncertainty:** interpretive questions, pending guidance, litigation, or conflicts.
10. **Source status:** official text/version and retrieval time.

Obligation record:

```yaml
obligation_id: OBL-<jurisdiction>-<instrument>-<number>
source_citation: <article, section, paragraph, page>
authority: <issuer>
status: proposed|final|effective|stayed|withdrawn|superseded
regulated_actor: <who>
modal: must|must_not|may|should
action: <verb>
object: <what>
trigger_or_condition: <when/if>
deadline_or_frequency: <time requirement>
exceptions: []
evidence_of_compliance: []
affected_controls: []
owner: <role>
confidence: <rating and rationale>
```

## 15. Network and link analysis

Build graphs from evidence, not association by proximity.

### Node types

Person, entity, account, wallet, device, address, domain, email, phone, vessel,
aircraft, document, transaction, case, event, product, jurisdiction, control.

### Edge types

Owns, controls, directs, employed by, transacts with, shares identifier, shares device,
resides at, registered at, communicates with, contracts with, litigates against,
designated by, mentioned in, observed at, derives from.

Every edge requires:

```yaml
edge_id: EDGE-<stable-id>
from_node: <id>
relationship: <controlled vocabulary>
to_node: <id>
valid_from: <date or unknown>
valid_to: <date or open>
claim_class: observed|reported|inferred
evidence_pointers: []
confidence: <rating and reason>
directional: true|false
materiality: <why the link matters>
```

Do not turn co-occurrence into control, contact into collusion, or a shared service
address into common ownership. Visualize inferred edges differently from observed ones.

## 16. Adverse-information framework

Use adverse information to identify and contextualize risk, not to compile accusations.

1. Resolve the subject before attributing the item.
2. Capture publisher, author, date, jurisdiction, headline, direct link, and underlying
   primary record.
3. Classify event type, alleged conduct, procedural status, affected entity/person, and
   date of conduct.
4. Search for corrections, dismissals, appeals, acquittals, settlements, remediation,
   and later outcomes.
5. Separate duplicate syndication from independent corroboration.
6. Assess source credibility and proximity to the evidence.
7. State relevance to the decision, recency, materiality, and nexus.
8. Quote minimally and preserve context.

Procedural status vocabulary:

`rumor -> reported allegation -> complaint/charge -> pending proceeding -> finding or
judgment -> appeal -> final outcome -> remediation/closure`

Never describe a charge as a conviction, a complaint as a finding, a settlement as an
admission unless the instrument says so, or repeated syndication as multiple sources.

## 17. Intelligence-product contracts

| Product | Mandatory elements |
|---|---|
| Flash alert | event, why it matters, severity/confidence, affected scope, immediate actions, direct source, timestamp |
| Daily brief | top findings, change since prior run, watchlist, negative/quiet result, coverage and source health |
| Weekly intelligence report | executive judgment, themes, chronology, domain findings, counterview, actions, source ledger |
| Entity dossier | identity, ownership, business/footprint, risk domains, chronology, network, findings, limitations, recommendation |
| Typology assessment | behavior mapped to typology, indicators present/absent, alternatives, evidence, control coverage, escalation |
| Regulatory tracker | instrument/status, obligations, dates, impact, actions/owners, affected controls, source versions |
| Risk heat map | governed rating method, counts and exposure, trend, outliers, data-quality caveats, drill-through |
| Committee pack | decision requests, portfolio position, material changes, overdue actions, incidents, forward calendar, appendix |

## 18. Copy-ready analytical prompts

### 18.1 Typology mapping

```text
Act as a senior intelligence analyst. Using modules 00, 01, 04, 05, 06, 07, and 09,
map the supplied activity to relevant typologies without presuming misconduct.

Scope:
- subject/population:
- period and timezone:
- source systems and expected totals:
- applicable products/jurisdictions:
- decision to support:

For each candidate typology, state the mechanism, indicators present, indicators absent,
alternative explanations, evidence needed to confirm or refute, severity, confidence,
control coverage, and recommended next step. Cite exact rows/messages/transactions. Build
a chronology and relationship map where relevant. Reconcile the full population and
list exclusions and failures. Do not turn correlation into intent. Render a decision
memo plus a structured typology-evidence matrix and run the module 09 release gate.
```

### 18.2 Entity intelligence assessment

```text
Build an evidence-led entity risk assessment as of [timestamp]. First resolve the legal
entity and classify its business/entity typology. Trace ownership and control to natural
persons or explain the unresolved layer. Assess every applicable domain in section 12,
with direct evidence, counterevidence, severity, confidence, and data gaps. Search for
current licensing, enforcement/litigation status, sanctions/ownership exposure, adverse
information outcomes, financial condition, governance, technology, geography, and key
third parties. Do not score missing public information as adverse by default. Show the
unadjusted score, any predefined floor or override, sensitivity, and the decision impact.
Produce an executive report, evidence ledger, source list, ownership table, chronology,
and action tracker. Require human approval for any onboarding, offboarding, restriction,
or external communication decision.
```

### 18.3 Regulatory change assessment

```text
Monitor [authorities/topics/jurisdictions] for the period [range], using official sources
first. Deduplicate releases, compare new versions to the prior state, and classify each
item as proposed, final, effective, stayed, withdrawn, superseded, enforcement, guidance,
or nonbinding speech. Extract atomic obligations with exact citations and dates. Map each
obligation to affected products, policies, procedures, controls, systems, data, training,
contracts, and reports. Produce: a one-page executive brief, obligation register, action
tracker, source/change log, negative-search record, and coverage reconciliation. Separate
legal text from analytical interpretation. Flag where counsel or policy-owner review is
required.
```

### 18.4 On-chain fund-flow analysis

```text
Analyze the supplied blockchain transactions for [chains/assets/period]. Preserve every
transaction hash and source label. Reconcile starting value, traced value, fees, swaps,
bridges, untraced value, and ending value under a stated valuation method. Identify
services and typologies, but distinguish observed transactions from third-party address
attribution and from inferred ownership or intent. State directness and hop count for
each exposure. Provide a chronological flow table, network diagram specification,
typology matrix, attribution ledger, alternative explanations, limitations, and
escalation recommendations. Do not claim that the analysis identifies a beneficial owner
unless independent off-chain evidence supports it.
```

## 19. Release conditions

Before distributing an intelligence product, confirm:

- the subject, object, jurisdiction, period, and as-of time are explicit;
- the expected population reconciles or the coverage limitation is prominent;
- every material claim is classified and cited to an evidence span;
- identities and duplicate reports have been resolved;
- current status is distinguished from historical status;
- indicators are not presented as proof of intent;
- alternatives and disconfirming evidence were considered;
- severity and confidence are independently reasoned;
- scoring rules, floors, overrides, and missing-data treatment are visible;
- recommendations identify owner, urgency, dependency, and approval;
- no automated conclusion performs a regulated or consequential decision;
- the module `09` gate passes and the output renders under module `07`.
