# Official-Source Register for OSINT and Institutional Research

Version: 1.0
Registry review date: 2026-08-13
Scope: public research starting points; no list or personal data is redistributed
Companion control standard: `01-evidence-research-standard.md`

## 1. What this register does

This register maps common intelligence questions to authoritative public sources and defensible fallbacks. It is a navigation layer, not a data feed, screening service, legal opinion, or guarantee of coverage. Retrieve the current record directly from the issuer, record the version and time, resolve the subject, and preserve the evidence trail.

The register deliberately links to source pages rather than embedding sanctioned-person, watchlist, customer, officer, complainant, victim, or other personal data. Public redistribution of this file is safe only while that boundary is preserved.

Official websites change. A working link does not establish that the underlying record is current, complete, applicable, or authentic. At use time, confirm the publisher from its parent domain, check for a successor service, and capture the exact record relied on.

## 2. Numbered taxonomy

| Code | Domain | Typical question |
|---|---|---|
| 01 | Sanctions, restrictions, and debarment | Is a person, entity, vessel, aircraft, address, or firm subject to an official restriction? |
| 02 | AML/CFT/CPF standards and country assessment | What standard, jurisdiction status, evaluation, advisory, or supervisory expectation applies? |
| 03 | Public office and PEP evidence | Does an official record establish a qualifying public function and its dates? |
| 04 | Corporate identity, ownership, and beneficial ownership | Does the entity exist; what was filed about officers, shareholders, parents, or controllers? |
| 05 | Securities, markets, and licensed participants | Is an issuer or intermediary registered; what did it file; what actions or warnings exist? |
| 06 | Prudential, banking, insurance, and payments | Is a financial institution authorized or supervised; what sector data apply? |
| 07 | Enforcement, courts, insolvency, and legal proceedings | What proceeding, order, judgment, disposition, or insolvency record exists? |
| 08 | Procurement, public spending, and exclusions | Who won public work; what was paid; is a supplier excluded? |
| 09 | Tax, customs, trade, and export controls | What tariff, customs, tax-transparency, trade-flow, or export-control record applies? |
| 10 | Corruption, bribery, and public integrity | What official or methodologically accountable evidence measures or records integrity risk? |
| 11 | Fraud, cyber, and technical threat intelligence | What official alert, vulnerability, complaint trend, or cybercrime record exists? |
| 12 | Law enforcement, wanted persons, and security designations | What public notice, wanted record, or terrorist designation has an authority issued? |
| 13 | International organizations and development evidence | What treaty, multilateral document, development record, or global program source applies? |
| 14 | Statistical, economic, fiscal, and market data | What official series supports the quantitative statement? |
| 15 | Legislation, regulation, gazettes, and parliamentary records | What controlling law, rule, official notice, or legislative history applies? |
| 16 | Digital assets and public-ledger research | What does the ledger show, and what official virtual-asset registration or rule applies? |
| 17 | ESG, environment, labor, and human rights | What authoritative disclosure, treaty, enforcement, or indicator supports the claim? |
| 18 | Adverse media, archives, and content verification | Where can a lead be corroborated, dated, authenticated, corrected, or archived? |
| 19 | Open data, geospatial, maritime, and aviation | What official dataset establishes location, asset registration, movement context, or boundaries? |

## 3. Credibility tiers

| Tier | Meaning | Reliance |
|---|---|---|
| T1 | Issuer or registry of record for the exact proposition: government, court, legislature, regulator, international body, official statistics producer, filer, or public ledger | May support a claim after identity, scope, temporal, and record-status checks |
| T2 | Accountable secondary or quasi-official source with transparent ownership, methods, and corrections | Corroboration and context; seek the underlying T1 record where one should exist |
| T3 | Discovery source, public aggregator, community contribution, or third-party label | Lead only; do not make a finding from it alone |
| TX | Excluded: fabricated, unauthenticated, circular, unlawfully obtained, deceptively presented, or without inspectable provenance | Do not rely or cite as evidence |

Tier is proposition-specific. A court database is T1 for the docket it maintains. A regulator press release is T1 for what the regulator announced, while the filed order controls the order's terms. A block explorer is a convenient interface to T1 ledger facts but its proprietary address label is T3.

## 4. Field and cadence keys

Every registry row contains these fields:

- **J/C:** jurisdiction or geographic coverage.
- **D:** domain code from the taxonomy.
- **Use:** the proposition the source can establish or the task it supports.
- **Freq:** `EV` event-driven, `C` continuous, `D` daily, `W` weekly, `M` monthly, `Q` quarterly, `A` annual, `P` periodic/irregular, `H` historical/static.
- **Access:** `WEB` browse, `SEARCH` query form, `DL` downloadable data/document, `API` machine interface, `REG` account required, `FEE` official fee, `BULK` bulk data.
- **Limits:** the main reason not to overstate the source.

Access labels describe the public interface at registry review, not a promise of availability. Observe terms, rate limits, license conditions, and data-protection law.

## 5. Source-selection rules

1. Select by proposition and jurisdiction, not familiarity.
2. Start with the controlling T1 record; use T2/T3 to discover identifiers and context.
3. For sanctions, restrictions, licenses, and office-holders, re-check the authoritative source at the decision time.
4. For cross-border entities, search the registry of incorporation plus regulators, exchanges, and parent jurisdictions.
5. For an adverse event, retrieve the docket, order, filing, or authority notice before relying on news.
6. For ownership, cite every relationship edge; registry data usually establishes what was filed, not verified beneficial reality.
7. For statistics, capture series code, edition/vintage, units, seasonal treatment, methodology, and revisions.
8. For public-ledger work, separate observable transactions from third-party attribution.
9. If a source requires registration or payment, record the limitation; do not substitute an unauthenticated mirror.
10. If no official public record exists, state that constraint and lower confidence. Do not invent coverage.

## 6. Standard fallback chains

| Question | Preferred chain |
|---|---|
| Sanctions/watchlist | Current issuing authority list -> governing legal instrument/gazette -> authority change notice -> accountable aggregator for discovery only |
| Company/owner | Incorporation registry -> filed document -> securities/regulatory filing -> LEI relationship data -> reputable aggregator/leak for leads only |
| Enforcement/court | Filed order/judgment/docket -> authority case page -> official press release -> accountable reporting -> broad web lead |
| PEP/public office | Appointment/election/gazette/parliament record -> official biography/roster -> official disclosure -> accountable secondary chronology |
| Licensed firm | Regulator's live register -> license decision/order -> official warnings -> company claim |
| Quantitative series | Producing agency API/download -> methodology/revision page -> recognized multilateral mirror -> secondary chart |
| Adverse media | Underlying authority/court record -> independent accountable reporting -> investigative consortium -> index/search lead |
| Historical page | Issuer archive/version history -> official gazette/library capture -> lawful independent web archive -> secondary quotation with limitation |
| Blockchain | Node/ledger data -> recognized explorer for reproduction -> issuer/regulator designation -> independent attribution; community labels last |

## 7. Exclusions and archive practice

Exclude AI-generated answers, search snippets, knowledge panels, content farms, unattributed list copies, deceptive look-alike domains, source-less “background check” pages, bulk doxxing files, and mirrors whose origin cannot be authenticated. Do not treat a commercial screening match as the controlling record; trace it to the issuer.

For each relied-on source, preserve the canonical URL, record ID, title, issuer, publication/effective/update dates, retrieval timestamp, pinpoint location, access method, file hash where permitted, and coverage status. Prefer issuer archives. An independent web archive proves only what a page displayed at a time, not that the page was true. Do not publicly archive restricted or unnecessarily sensitive personal data.

## 8. Registry

### 8.1 Sanctions, restrictions, and debarment

| ID | Tier | J/C | D | Official source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 01.001 | T1 | Global/UN | 01 | [UN Security Council Consolidated List](https://main.un.org/securitycouncil/en/content/un-sc-consolidated-list) | UN designations and identifiers | EV | WEB,DL | Measures differ by regime; national implementation still controls locally |
| 01.002 | T1 | Global/UN | 01 | [UN sanctions committees](https://main.un.org/securitycouncil/en/sanctions/information) | Regime pages, narrative summaries, exemptions, and delisting | EV | WEB | Search the applicable committee, not only the consolidated name row |
| 01.003 | T1 | United States | 01 | [OFAC Sanctions List Service](https://ofac.treasury.gov/sanctions-list-service) | SDN and non-SDN lists, downloads, search, and change files | EV | SEARCH,DL | Search score is not a disposition; ownership/control rules extend beyond named parties |
| 01.004 | T1 | United States | 01 | [OFAC sanctions programs and country information](https://ofac.treasury.gov/sanctions-programs-and-country-information) | Program scope, legal authorities, guidance, and general licenses | EV | WEB,DL | Programs are not all comprehensive country embargoes; read operative authorities |
| 01.005 | T1 | United States | 01 | [US Consolidated Screening List](https://www.trade.gov/consolidated-screening-list) | Consolidated export and trade-screening lists across US agencies | EV | SEARCH,API,DL | Convenience view; underlying agency list and legal authority control |
| 01.006 | T1 | United States | 01 | [BIS Entity List, 15 CFR Part 744 Supplement 4](https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-744/appendix-Supplement%20No.%204%20to%20Part%20744) | Export-license restrictions for listed entities | EV | WEB | Restrictions are entry- and item-specific; check EAR and footnotes |
| 01.007 | T1 | United States | 01 | [BIS Denied Persons List](https://www.bis.gov/licensing/end-user-guidance/denied-persons-list-dpl) | Export-privilege denial orders | EV | WEB,DL | Check order scope, effective period, aliases, and reinstatement |
| 01.008 | T1 | United States | 01 | [BIS Unverified List](https://www.bis.gov/licensing/end-user-guidance/unverified-list) | Parties whose bona fides BIS could not verify | EV | WEB,DL | Not the Entity List; legal effect and diligence response differ |
| 01.009 | T1 | United States | 01 | [BIS Military End User List](https://www.bis.gov/licensing/end-user-guidance/military-end-user-list) | Listed military end users under EAR controls | EV | WEB,DL | List is not exhaustive; rule may cover unlisted end users |
| 01.010 | T1 | European Union | 01 | [EU sanctions overview and consolidated-list resources](https://finance.ec.europa.eu/eu-and-world/sanctions-restrictive-measures/overview-sanctions-and-related-resources_en) | EU financial-sanctions list and official resource links | EV | WEB,DL | EU Official Journal legal acts control if data and law conflict |
| 01.011 | T1 | European Union | 01 | [EU Sanctions Map](https://www.sanctionsmap.eu/) | Regime, measure, and legal-act discovery | EV | WEB | Navigation aid; verify operative act in EUR-Lex/Official Journal |
| 01.012 | T1 | United Kingdom | 01 | [UK Sanctions List](https://www.gov.uk/government/publications/the-uk-sanctions-list) | UK designations under sanctions regulations | EV | WEB,DL | Check current UK implementation guidance and designation details |
| 01.013 | T1 | United Kingdom | 01 | [OFSI financial sanctions guidance](https://www.gov.uk/government/collections/financial-sanctions-regime-specific-consolidated-lists-and-releases) | Regime notices, guidance, and updates | EV | WEB | Guidance does not replace legislation or the current UK Sanctions List |
| 01.014 | T1 | Canada | 01 | [Canadian autonomous sanctions consolidated list](https://www.international.gc.ca/world-monde/international_relations-relations_internationales/sanctions/consolidated-consolide.aspx?lang=eng) | Names listed under Canadian autonomous sanctions regulations | EV | WEB | Administrative aid; regulations control and UN measures may require separate review |
| 01.015 | T1 | Australia | 01 | [DFAT Consolidated List](https://www.dfat.gov.au/international-relations/security/sanctions/consolidated-list) | Australian targeted financial sanctions | EV | WEB,DL | Autonomous and UN regimes have separate legal bases and permits |
| 01.016 | T1 | New Zealand | 01 | [New Zealand sanctions register](https://www.mfat.govt.nz/en/countries-and-regions/europe/ukraine/russian-invasion-of-ukraine/sanctions) | New Zealand Russia sanctions and designations | EV | WEB,DL | Coverage is regime-specific; check UN implementation separately |
| 01.017 | T1 | Switzerland | 01 | [SECO sanctions and measures](https://www.seco.admin.ch/seco/en/home/Aussenwirtschaftspolitik_Wirtschaftliche_Zusammenarbeit/Wirtschaftsbeziehungen/exportkontrollen-und-sanktionen/sanktionen-embargos.html) | Swiss sanctions regimes and SECO list/search links | EV | WEB,SEARCH | Ordinance and annex for the regime control; multilingual source |
| 01.018 | T1 | Japan | 01 | [Ministry of Finance economic-sanctions target lists](https://www.mof.go.jp/policy/international_policy/gaitame_kawase/gaitame/economic_sanctions/list.html) | Asset-freeze and payment-restriction target lists | EV | WEB,DL | Japanese source; public notices and governing law contain the controlling detail |
| 01.019 | T1 | Singapore | 01 | [MAS targeted financial sanctions](https://www.mas.gov.sg/regulation/anti-money-laundering/targeted-financial-sanctions) | UN-based TFS notices and financial-sector obligations | EV | WEB | Sector notices and Singapore regulations must be read together |
| 01.020 | T1 | South Africa | 01 | [FIC targeted financial sanctions](https://www.fic.gov.za/compliance/targeted-financial-sanctions/) | South African TFS search and guidance | EV | WEB,SEARCH | Search coverage and domestic legal effect require current confirmation |
| 01.021 | T1 | India | 01 | [Ministry of Home Affairs security-list portal](https://www.mha.gov.in/en/safer-india) | Official links to banned organizations and individual terrorists under UAPA | EV | WEB | Not a consolidated financial-sanctions list; open the linked legal notification |
| 01.022 | T1 | France | 01 | [French Treasury national asset-freeze register](https://gels-avoirs.dgtresor.gouv.fr/) | French and applicable EU/UN asset-freeze targets | EV | SEARCH,DL | Verify legal basis and effective scope for each entry |
| 01.023 | T1 | Global/MDB | 01 | [World Bank Listing of Ineligible Firms and Individuals](https://www.worldbank.org/en/projects-operations/procurement/debarred-firms) | World Bank debarments and cross-debarment status | EV | SEARCH,DL | Ineligibility scope and dates vary; not a criminal finding |
| 01.024 | T1 | Asia/MDB | 01 | [Asian Development Bank sanctions list](https://www.adb.org/who-we-are/integrity/sanctions) | ADB debarred and cross-debarred parties | EV | WEB,DL | Confirm period, conditional release, and cross-debarment basis |
| 01.025 | T1 | Africa/MDB | 01 | [African Development Bank sanctions list](https://www.afdb.org/en/projects-operations/debarment-and-sanctions-procedures) | AfDB debarment decisions and list links | EV | WEB | Page and decisions may differ in public detail |
| 01.026 | T1 | Americas/MDB | 01 | [Inter-American Development Bank sanctioned firms and individuals](https://www.iadb.org/en/transparency/sanctioned-firms-and-individuals) | IDB Group sanctions | EV | SEARCH | Administrative sanctions; check duration and institution coverage |
| 01.027 | T1 | Europe/MDB | 01 | [EBRD ineligible entities](https://www.ebrd.com/home/who-we-are/strategies-governance-compliance/ebrd-sanctions-system/ineligible-entities.html) | EBRD enforcement and cross-debarment | EV | WEB | Check decision source, duration, and conditional terms |
| 01.028 | T1 | Global/UN procurement | 01 | [UNGM vendor-sanctions API documentation](https://developer.ungm.org/Article/SearchVendorSanctions) | UN supplier ineligibility and sanctions records across participating agencies | EV | API,REG | Retrieval requires authorization; agency-specific results and sanction types can differ |
| 01.029 | T1 | Global/law enforcement | 01 | [INTERPOL Red Notices](https://www.interpol.int/en/How-we-work/Notices/Red-Notices/View-Red-Notices) | Public extracts of notices seeking location/provisional arrest | EV | SEARCH | Public subset only; a Red Notice is not an international arrest warrant or guilt finding |
| 01.030 | T1 | Global/travel security | 01 | [UN Security Council travel-ban and assets-freeze regime pages](https://main.un.org/securitycouncil/en/sanctions/information) | Measure-specific scope for designated subjects | EV | WEB | Measures and exemptions vary by committee; use regime detail |

### 8.2 AML/CFT/CPF standards and country assessment

| ID | Tier | J/C | D | Official source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 02.001 | T1 | Global | 02 | [FATF Recommendations](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html) | International AML/CFT/CPF standards and interpretive notes | P | WEB,DL | Standards require jurisdiction-specific implementation analysis |
| 02.002 | T1 | Global | 02 | [FATF high-risk and monitored jurisdictions](https://www.fatf-gafi.org/en/topics/high-risk-and-other-monitored-jurisdictions.html) | Current FATF call-for-action and increased-monitoring statements | P | WEB | Check plenary date and exact statement; labels change |
| 02.003 | T1 | Global | 02 | [FATF mutual evaluations](https://www.fatf-gafi.org/en/publications/Mutualevaluations.html) | Country evaluations and follow-up reports | P | SEARCH,DL | Ratings reflect an assessment date and may predate reforms |
| 02.004 | T1 | Asia-Pacific | 02 | [Asia/Pacific Group mutual evaluations](https://apgml.org/mutual-evaluations/) | APG member assessments and follow-up | P | WEB,DL | Country and round dates differ |
| 02.005 | T1 | Caribbean | 02 | [Caribbean Financial Action Task Force](https://cfatf-gafic.org/) | CFATF member mutual-evaluation and follow-up publications | P | WEB,DL | Reports are published through member/news pages; confirm latest version against FATF's evaluation index |
| 02.006 | T1 | Eurasia | 02 | [Eurasian Group mutual-evaluation reports](https://eurasiangroup.org/en/mutual-evaluation-reports) | EAG mutual evaluations and follow-up | P | WEB,DL | Multilingual; confirm latest follow-up report |
| 02.007 | T1 | Eastern/Southern Africa | 02 | [ESAAMLG mutual evaluations](https://www.esaamlg.org/index.php/Mutual_Evaluations/readmore_me) | Regional AML/CFT assessments | P | WEB,DL | Interface may not expose all historical versions consistently |
| 02.008 | T1 | Central Africa | 02 | [GABAC](https://spgabac.org/) | Regional AML/CFT standards, evaluations, and statements | P | WEB | Primarily French; locate exact evaluation and date |
| 02.009 | T1 | Latin America | 02 | [GAFILAT mutual-evaluation library](https://biblioteca.gafilat.org/?cat=13) | Mutual evaluations and follow-up for member states | P | WEB,DL | Primarily Spanish; check assessment round and updates |
| 02.010 | T1 | West Africa | 02 | [GIABA mutual evaluation reports](https://www.giaba.org/mutual-evaluation/) | West African AML/CFT evaluations | P | WEB,DL | Publication lag and site navigation can limit discovery |
| 02.011 | T1 | Middle East/North Africa | 02 | [MENAFATF second-round evaluation reports](https://www.menafatf.org/mutual-evaluations-follow/evaluation-reports-2) | Regional assessments and follow-up | P | WEB,DL | Arabic/English versions may differ in release timing |
| 02.012 | T1 | Europe | 02 | [MONEYVAL country reports](https://www.coe.int/en/web/moneyval/jurisdictions) | Council of Europe AML/CFT evaluations | P | WEB,DL | Applies to MONEYVAL jurisdictions, not all Europe |
| 02.013 | T1 | Global/FIUs | 02 | [Egmont Group member FIUs](https://egmontgroup.org/members-by-region/) | Confirm national FIU membership and official links | P | WEB | Membership does not describe each FIU's powers or public data |
| 02.014 | T1 | United States | 02 | [FinCEN guidance and advisories](https://www.fincen.gov/resources/advisoriesbulletinsfact-sheets) | AML advisories, notices, fact sheets, and typologies | EV | WEB,DL | Advisory is not a designation; check cited legal obligations |
| 02.015 | T1 | United States | 02 | [FFIEC BSA/AML Examination Manual](https://bsaaml.ffiec.gov/manual) | US examination procedures and control expectations | P | WEB | Not a substitute for statutes, regulations, or agency-specific action |
| 02.016 | T1 | United States | 02 | [FinCEN regulations, 31 CFR Chapter X](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X) | Current federal BSA implementing regulations | C | WEB | Check effective dates, applicability, and rulemaking history |
| 02.017 | T1 | European Union | 02 | [European Commission high-risk third countries](https://finance.ec.europa.eu/financial-crime/high-risk-third-countries-and-international-context-content-anti-money-laundering-and-countering_en) | EU AML high-risk-country framework and current acts | EV | WEB | Delegated regulation and effective date control |
| 02.018 | T1 | European Union | 02 | [EBA AML/CFT resources](https://www.eba.europa.eu/regulation-and-policy/anti-money-laundering-and-countering-financing-terrorism) | EU supervisory guidelines, opinions, and risk factors | EV | WEB,DL | Determine whether an instrument is binding, final, or consultative |
| 02.019 | T1 | United Kingdom | 02 | [FCA Financial Crime Guide](https://www.handbook.fca.org.uk/handbook/FCG/) | FCA examples and expectations for financial-crime systems | P | WEB | Guide is non-Handbook guidance; applicable rules may sit elsewhere |
| 02.020 | T2 | United Kingdom | 02 | [JMLSG guidance](https://www.jmlsg.org.uk/guidance/current-guidance/) | Industry guidance approved by HM Treasury | P | WEB,DL | Not law; sectoral parts and approval status matter |
| 02.021 | T1 | Australia | 02 | [AUSTRAC guidance](https://www.austrac.gov.au/business/how-comply-and-report-guidance-and-resources) | Australian AML/CTF compliance and reporting guidance | EV | WEB | Check current Act, Rules, and commencement dates |
| 02.022 | T1 | Canada | 02 | [FINTRAC compliance guidance](https://fintrac-canafe.canada.ca/guidance-directives/guidance-directives-eng) | Canadian AML obligations, indicators, and guidance | EV | WEB | Entity type and effective-date distinctions are material |
| 02.023 | T1 | Singapore | 02 | [MAS AML/CFT supervision](https://www.mas.gov.sg/regulation/anti-money-laundering) | MAS notices, guidelines, and sector materials | EV | WEB | Notice applies by regulated sector; guidelines explain but do not replace it |
| 02.024 | T1 | Hong Kong | 02 | [HKMA AML/CFT](https://www.hkma.gov.hk/eng/key-functions/banking/anti-money-laundering-and-counter-financing-of-terrorism/) | Supervisory guidance for authorized institutions | EV | WEB | Banking-sector scope; other sectors have different supervisors |
| 02.025 | T1 | Global | 02 | [UNODC money-laundering resources](https://www.unodc.org/unodc/en/money-laundering/overview.html) | UN conventions, model materials, and global program context | P | WEB | Not a current country compliance rating |

### 8.3 Public office and PEP evidence

No single free global PEP list is authoritative. Establish the public function from the appointing, electoral, parliamentary, gazette, judicial, military, state-enterprise, or intergovernmental source; then record dates, prominence, jurisdiction, and relationship evidence. PEP status is not adverse conduct.

| ID | Tier | J/C | D | Official source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 03.001 | T1 | United States | 03 | [Biographical Directory of the US Congress](https://bioguide.congress.gov/) | Congressional service and biographical history | C | SEARCH | Historical biographies may omit current external roles |
| 03.002 | T1 | United States | 03 | [US House directory](https://www.house.gov/representatives) | Current representatives and official sites | EV | WEB | Membership changes require date-specific capture |
| 03.003 | T1 | United States | 03 | [US Senate senators](https://www.senate.gov/senators/index.htm) | Current senators, classes, states, and contacts | EV | WEB | Current roster, not full employment or relationship history |
| 03.004 | T1 | United States | 03 | [Office of Government Ethics individual disclosures](https://oge.gov/web/OGE.nsf/Officials%20Individual%20Disclosures%20Search%20Collection) | Federal executive financial-disclosure search and request access | EV | WEB,REG | OGE holds only covered filers; use the employing agency where required and observe statutory use limits |
| 03.005 | T1 | United States | 03 | [House Clerk financial disclosure reports](https://disclosures-clerk.house.gov/FinancialDisclosure) | House member and candidate disclosures | A | SEARCH,DL | Self-reported, period-specific, and subject to statutory ranges |
| 03.006 | T1 | United States | 03 | [Senate electronic financial disclosures](https://efdsearch.senate.gov/) | Senate disclosures and transaction reports | EV | SEARCH | Terms acknowledgment; self-reported and date-bounded |
| 03.007 | T1 | United Kingdom | 03 | [UK Parliament members](https://members.parliament.uk/) | Current and former members, roles, interests links | EV | SEARCH | Registers of interests are separate records with their own dates |
| 03.008 | T1 | United Kingdom | 03 | [UK ministers](https://www.gov.uk/government/ministers) | Current ministerial appointments and portfolios | EV | WEB | Capture appointment and departure dates; page is current-state oriented |
| 03.009 | T1 | European Union | 03 | [EU Who is Who](https://op.europa.eu/en/web/who-is-who) | EU institution organizational posts and office-holders | C | SEARCH | Institutional directory; determine whether the function qualifies under policy |
| 03.010 | T1 | European Union | 03 | [European Parliament MEPs](https://www.europarl.europa.eu/meps/en/home) | Current and historical MEP profiles and roles | EV | SEARCH | Declared interests and assistants are separate records |
| 03.011 | T1 | Canada | 03 | [Parliament of Canada members](https://www.ourcommons.ca/MEMBERS/en) | Current and historical House members | EV | SEARCH | Senate and provincial offices require separate sources |
| 03.012 | T1 | Australia | 03 | [Parliament of Australia senators and members](https://www.aph.gov.au/Senators_and_Members/Parliamentarian_Search_Results) | Federal parliamentary service and roles | EV | SEARCH | State and territory offices require separate sources |
| 03.013 | T1 | India | 03 | [Lok Sabha members](https://sansad.in/ls/members) | Current lower-house membership and profiles | EV | SEARCH | Upper house and subnational office must be checked separately |
| 03.014 | T1 | South Africa | 03 | [Parliament of South Africa members](https://www.parliament.gov.za/group-details) | Parliamentary membership and party grouping | EV | WEB | Historical continuity and outside interests may require archived records |
| 03.015 | T1 | Brazil | 03 | [Chamber of Deputies member data](https://www.camara.leg.br/deputados/quem-sao) | Federal deputy identities, terms, and profiles | EV | SEARCH,API | Senate, executive, state, and municipal offices are separate |
| 03.016 | T1 | Global | 03 | [IPU Parline](https://data.ipu.org/) | National parliament structures and member data supplied through IPU | P | SEARCH | Coverage and update lag vary by parliament; verify with national source |

### 8.4 Corporate identity, ownership, and beneficial ownership

| ID | Tier | J/C | D | Official source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 04.001 | T1 | Global | 04 | [GLEIF LEI Search](https://search.gleif.org/) | Legal-entity identifiers and reported direct/ultimate parent relationships | D | SEARCH,API,BULK | LEI coverage is not universal; relationship exceptions and lapsed records matter |
| 04.002 | T1 | United Kingdom | 04 | [Companies House](https://find-and-update.company-information.service.gov.uk/) | Company status, officers, filings, charges, and PSC declarations | C | SEARCH,API,DL | Registry publishes filed information and warns it may not be verified |
| 04.003 | T1 | European Union/EEA | 04 | [EU e-Justice business registers search](https://e-justice.europa.eu/topics/registers-business-insolvency-land/business-registers-search-company-eu/general-information-find-company_en) | BRIS search across connected national registers | C | SEARCH | Detail, fees, and document availability depend on national registry |
| 04.004 | T1 | United States/public issuers | 04 | [SEC EDGAR company filings](https://www.sec.gov/edgar/search/) | Issuer identity, ownership filings, exhibits, financials, and events | C | SEARCH,API,DL | Covers SEC filers, not all US companies; filer statements may later be amended |
| 04.005 | T1 | United States/Delaware | 04 | [Delaware Division of Corporations entity search](https://icis.corp.delaware.gov/Ecorp/EntitySearch/NameSearch.aspx) | Formation status and file number | C | SEARCH,FEE | Free details are limited; beneficial owners generally not public |
| 04.006 | T1 | United States/New York | 04 | [New York Corporation and Business Entity Database](https://apps.dos.ny.gov/publicInquiry/) | State entity status and filing data | C | SEARCH | Filing data does not establish beneficial ownership |
| 04.007 | T1 | United States/California | 04 | [California bizfile online](https://bizfileonline.sos.ca.gov/search/business) | California entity search and filings | C | SEARCH | Registered-agent address may be a service-provider address |
| 04.008 | T1 | United States/Florida | 04 | [Florida Sunbiz entity search](https://search.sunbiz.org/Inquiry/CorporationSearch/ByName) | Entity, officer/authorized-person, and filing records | C | SEARCH | Roles are filed labels, not proof of beneficial ownership |
| 04.009 | T1 | United States/Texas | 04 | [Texas taxable entity search](https://mycpa.cpa.state.tx.us/coa/) | Entity status, taxpayer number, and registered-agent information | C | SEARCH | Secretary of State documents may require a separate paid service |
| 04.010 | T1 | United States/Nevada | 04 | [Nevada business entity search](https://esos.nv.gov/EntitySearch/OnlineEntitySearch) | Entity status, officers, and filings | C | SEARCH | Filed officer data does not resolve economic control |
| 04.011 | T1 | Canada/federal | 04 | [Corporations Canada search](https://ised-isde.canada.ca/cc/lgcy/fdrlCrpSrch.html?locale=en_CA) | Federal corporation status, directors, and filings | C | SEARCH | Provincial and territorial companies require their own registries |
| 04.012 | T1 | Australia | 04 | [ASIC registers](https://asic.gov.au/online-services/search-asic-s-registers/) | Companies, organizations, persons, and professional registers | C | SEARCH,FEE | Detailed extracts may require payment; filed data can lag |
| 04.013 | T1 | Australia | 04 | [Australian Business Register ABN Lookup](https://abr.business.gov.au/Search) | ABN, entity name, status, type, and business-name links | C | SEARCH,WEB | ABN registration is not the same as company ownership or licensing |
| 04.014 | T1 | New Zealand | 04 | [New Zealand Companies Register](https://companies-register.companiesoffice.govt.nz/) | Company status, directors, shareholders, and filings | C | SEARCH | Shareholder record may not identify ultimate beneficial owner |
| 04.015 | T1 | Singapore | 04 | [ACRA Bizfile](https://www.bizfile.gov.sg/) | Singapore business registration and official extracts | C | SEARCH,REG,FEE | Some data and documents require purchase or login |
| 04.016 | T1 | Hong Kong | 04 | [Companies Registry e-Search Services](https://www.icris.cr.gov.hk/csci/) | Company particulars and filed documents | C | SEARCH,REG,FEE | Search and document fees; current index may not expose beneficial ownership |
| 04.017 | T1 | Japan | 04 | [Corporate Number Publication Site](https://www.houjin-bangou.nta.go.jp/en/) | Corporate number, name, and registered address | C | SEARCH,DL | Does not provide ownership or full corporate filings |
| 04.018 | T1 | South Korea/public filers | 04 | [DART corporate disclosure](https://englishdart.fss.or.kr/) | Corporate filings, ownership, financials, and events | C | SEARCH,API | Primarily covered filers; translations and filing scope vary |
| 04.019 | T1 | India | 04 | [Ministry of Corporate Affairs company/LLP master data](https://www.mca.gov.in/content/mca/global/en/mca/master-data/MDS.html) | Registration, status, directors, charges, and filings | C | SEARCH,REG,FEE | Portal access and paid documents vary; filing is not verification |
| 04.020 | T1 | South Africa | 04 | [CIPC enterprise search](https://bizportal.gov.za/) | Company registration and official service access | C | SEARCH,REG | Detailed records may require authentication and fees |
| 04.021 | T1 | Brazil | 04 | [Federal Revenue CNPJ consultation](https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/Cnpjreva_Solicitacao.asp) | Federal taxpayer registration, status, name, and activities | C | SEARCH | Ownership/control evidence requires additional corporate records |
| 04.022 | T1 | Chile | 04 | [Registro de Empresas y Sociedades](https://www.registrodeempresasysociedades.cl/) | Electronic company constitution and records | C | SEARCH | Not all entities or historical formations use the simplified registry |
| 04.023 | T1 | Germany | 04 | [German Register Portal](https://www.handelsregister.de/rp_web/welcome.xhtml) | Commercial, cooperative, partnership, and association register records | C | SEARCH,FEE | Documents are in German; historic/current extracts differ |
| 04.024 | T1 | France | 04 | [INPI DATA national business register](https://data.inpi.fr/) | RNE company identity, officers, filings, and documents | C | SEARCH,REG | Personal fields and documents may be access-limited; filed data can change |
| 04.025 | T1 | Netherlands | 04 | [KVK Business Register](https://www.kvk.nl/en/ordering-products/kvk-business-register-extract/) | Dutch company identity and official extracts | C | SEARCH,FEE | Detailed extracts cost money; UBO register access is restricted |
| 04.026 | T1 | Denmark | 04 | [Virk Central Business Register](https://datacvr.virk.dk/) | CVR entities, participants, status, and filings | C | SEARCH | Danish interface; role labels require interpretation |
| 04.027 | T1 | Norway | 04 | [Brønnøysund Register Centre entity search](https://w2.brreg.no/enhet/sok/) | Norwegian registered entities and roles | C | SEARCH,API | Registered roles do not necessarily establish beneficial ownership |
| 04.028 | T1 | Sweden | 04 | [Bolagsverket business-register services](https://bolagsverket.se/en/sjalvservice/foretagsinformation.2047.html) | Swedish company information and official documents | C | SEARCH,FEE | English access and free detail are limited |
| 04.029 | T1 | Finland | 04 | [PRH Virre Information Service](https://virre.prh.fi/novus/home?userLang=en) | Finnish Trade Register search and extracts | C | SEARCH,FEE | Some extracts and filings require payment |
| 04.030 | T1 | Ireland | 04 | [Companies Registration Office CORE](https://core.cro.ie/) | Irish company search, status, and filings | C | SEARCH,REG,FEE | Document images may require purchase; beneficial ownership is separate/restricted |
| 04.031 | T1 | Belgium | 04 | [Crossroads Bank for Enterprises Public Search](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=en) | Enterprise number, status, activities, and establishments | C | SEARCH | Does not establish ultimate ownership |
| 04.032 | T1 | Austria | 04 | [Austrian Business Register via JustizOnline](https://justizonline.gv.at/jop/web/firmenbuchabfrage) | Firmenbuch records and official extracts | C | SEARCH,FEE | German interface; paid extracts and identity constraints |
| 04.033 | T1 | Switzerland | 04 | [Zefix central business-name index](https://www.zefix.admin.ch/) | Swiss registered entities and cantonal-register links | C | SEARCH | Cantonal extract controls; ownership coverage limited |
| 04.034 | T1 | Italy | 04 | [Italian Business Register](https://italianbusinessregister.it/) | Company identity, filings, officers, and official reports | C | SEARCH,REG,FEE | Detailed documents cost money; English data can be limited |
| 04.035 | T1 | Spain | 04 | [Colegio de Registradores mercantile registry](https://www.registradores.org/registroVirtual/init.do) | Spanish commercial-registry notes and certificates | C | SEARCH,REG,FEE | Paid registry access; search identifiers and regional records matter |
| 04.036 | T1 | Portugal | 04 | [Justice company publications](https://publicacoes.mj.pt/Pesquisa.aspx) | Company acts and official publications | C | SEARCH | Does not replace a certified commercial-registry extract |
| 04.037 | T1 | Estonia | 04 | [e-Business Register](https://ariregister.rik.ee/eng) | Entity, representative, ownership, annual-report, and status data | C | SEARCH,API | Some documents or data require authentication/payment |
| 04.038 | T1 | Latvia | 04 | [Register of Enterprises information portal](https://info.ur.gov.lv/) | Latvian legal entities, officers, and status | C | SEARCH | Detail and historical data may require authorized services |
| 04.039 | T1 | Lithuania | 04 | [Register of Legal Entities search](https://www.registrucentras.lt/jar/p_en/) | Lithuanian entity search and register information | C | SEARCH,FEE | Public search detail limited; official extracts may be paid |
| 04.040 | T1 | Poland | 04 | [National Court Register search](https://wyszukiwarka-krs.ms.gov.pl/) | KRS company status, representation, and filings | C | SEARCH | Polish records; beneficial ownership uses a separate register |
| 04.041 | T1 | Czechia | 04 | [Public Register and Collection of Documents](https://or.justice.cz/ias/ui/rejstrik) | Czech entities, officers, filings, and document collection | C | SEARCH | Primarily Czech; filed roles need temporal review |
| 04.042 | T1 | Romania | 04 | [National Trade Register Office portal](https://portal.onrc.ro/) | Romanian company search and official services | C | SEARCH,REG,FEE | Free detail limited; some services require payment |
| 04.043 | T1 | Greece | 04 | [GEMI business-publicity search](https://publicity.businessportal.gr/) | Greek company identity, status, and published acts | C | SEARCH | Greek-language filings and varying historical coverage |
| 04.044 | T1 | Cyprus | 04 | [Registrar of Companies search](https://efiling.drcor.mcit.gov.cy/DrcorPublic/SearchForm.aspx?sc=0) | Cyprus entity status and official searches | C | SEARCH,REG,FEE | Full records and certificates may require fee/account |
| 04.045 | T1 | Malta | 04 | [Malta Business Registry](https://register.mbr.mt/app/query/search_for_company) | Company status, officers, shareholders, and filings | C | SEARCH,REG,FEE | Detailed documents and some fields require registration/payment |
| 04.046 | T1 | Luxembourg | 04 | [Luxembourg Business Registers](https://www.lbr.lu/) | Trade and companies register filings and extracts | C | SEARCH,REG,FEE | Beneficial-owner register access is legally restricted |
| 04.047 | T1 | Iceland | 04 | [Iceland company register](https://www.skatturinn.is/fyrirtaekjaskra/) | Registered entities and basic business information | C | SEARCH | Icelandic interface; detailed ownership may be unavailable |
| 04.048 | T1 | Kenya | 04 | [Business Registration Service](https://brs.go.ke/) | Kenyan company registration and official search services | C | SEARCH,REG,FEE | Account/payment and data completeness constraints |
| 04.049 | T1 | Nigeria | 04 | [Corporate Affairs Commission public search](https://search.cac.gov.ng/) | Nigerian entity name, registration number, and status | C | SEARCH,REG | Detailed filings and beneficial ownership access may require login |
| 04.050 | T1 | Israel | 04 | [Corporations Authority services](https://www.gov.il/en/departments/topics/corporations_authority/govil-landing-page) | Company and partnership registry services | C | SEARCH,FEE | English detail limited; official extract may require payment |

### 8.5 Securities, markets, and licensed participants

| ID | Tier | J/C | D | Official source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 05.001 | T1 | United States | 05 | [SEC EDGAR](https://www.sec.gov/edgar/search/) | Issuer filings, ownership reports, exhibits, and current reports | C | SEARCH,API,DL | Filing is issuer-submitted and may be amended; not every entity files |
| 05.002 | T1 | United States | 05 | [SEC Investment Adviser Public Disclosure](https://adviserinfo.sec.gov/) | Registered adviser and exempt-reporting-adviser forms and disclosures | C | SEARCH | Registration is not endorsement; state and federal status differ |
| 05.003 | T1 | United States | 05 | [FINRA BrokerCheck](https://brokercheck.finra.org/) | Broker and brokerage registration, employment, and disclosure history | C | SEARCH | Disclosure may be alleged, pending, disputed, or expunged; read status |
| 05.004 | T1 | United States | 05 | [FINRA disciplinary actions](https://www.finra.org/rules-guidance/oversight-enforcement/finra-disciplinary-actions-online) | FINRA decisions, orders, and monthly action summaries | M/EV | SEARCH,DL | SRO action scope and appeal status matter |
| 05.005 | T1 | United States | 05 | [NFA BASIC](https://www.nfa.futures.org/basicnet/) | Derivatives registration, membership, principals, and actions | C | SEARCH | Commodity/futures scope; not a general financial-license register |
| 05.006 | T1 | United States | 05 | [CFTC intermediaries registration](https://www.cftc.gov/IndustryOversight/Intermediaries/index.htm) | Intermediary categories, registration links, and regulatory status | C | WEB,SEARCH | NFA performs much registration; verify category and current status |
| 05.007 | T1 | Canada | 05 | [CSA National Registration Search](https://info.securities-administrators.ca/nrsmobile/nrssearch.aspx) | Registration of firms and individuals across Canadian securities regulators | C | SEARCH | Registration categories and terms/conditions determine permitted activity |
| 05.008 | T1 | Canada | 05 | [SEDAR+](https://www.sedarplus.ca/) | Canadian public-company, fund, and securities filings | C | SEARCH,REG,DL | Filer-submitted; document type and jurisdictional coverage vary |
| 05.009 | T1 | United Kingdom | 05 | [FCA Financial Services Register](https://register.fca.org.uk/s/) | Authorized firms, individuals, permissions, and status | C | SEARCH | Clone warnings and appointed-representative relationships require separate review |
| 05.010 | T1 | European Union | 05 | [ESMA registers and data](https://www.esma.europa.eu/publications-and-data/databases-and-registers) | EU securities participants, prospectuses, ratings, benchmarks, and MiCA data | C | SEARCH,DL | Each register has distinct scope and competent authority |
| 05.011 | T1 | France | 05 | [AMF GECO database](https://geco.amf-france.org/Bio/Recherche_Societe.aspx) | Authorized investment products and management companies | C | SEARCH | French market scope; consult ACPR for banking/insurance permissions |
| 05.012 | T1 | Germany | 05 | [BaFin company database](https://portal.mvp.bafin.de/database/InstInfo/) | Authorized financial-services institutions and branches | C | SEARCH | Permissions and passporting scope require detail review |
| 05.013 | T1 | Italy | 05 | [CONSOB investment-firm and asset-management registers](https://www.consob.it/web/consob-and-its-activities/asset-management-companies) | Italian investment firms, asset managers, and linked official registers | C | SEARCH,DL | Register coverage varies; Bank of Italy supervises other categories |
| 05.014 | T1 | Spain | 05 | [CNMV official registers](https://www.cnmv.es/portal/consultas/busqueda.aspx) | Spanish securities entities, issuers, products, and filings | C | SEARCH | Spanish-language records; authorization scope must be read |
| 05.015 | T1 | Netherlands | 05 | [AFM registers](https://www.afm.nl/en/sector/registers) | Dutch licensed firms, prospectuses, and warning lists | C | SEARCH | DNB covers prudential/banking categories; passporting may apply |
| 05.016 | T1 | Switzerland | 05 | [FINMA authorized institutions and persons](https://www.finma.ch/en/finma-public/authorised-institutions-individuals-and-products/) | Swiss financial authorizations and product lists | C | SEARCH | Cantonal, self-regulatory, and foreign permissions may differ |
| 05.017 | T1 | Australia | 05 | [ASIC professional registers](https://connectonline.asic.gov.au/) | Australian financial-services and credit licenses and representatives | C | SEARCH | License conditions and representative relationships require the extract |
| 05.018 | T1 | New Zealand | 05 | [Financial Service Providers Register](https://fsp-register.companiesoffice.govt.nz/) | Registered financial service providers and dispute-resolution status | C | SEARCH | Registration alone is not licensing or endorsement |
| 05.019 | T1 | Singapore | 05 | [MAS Financial Institutions Directory](https://eservices.mas.gov.sg/fid/institution) | MAS-regulated institutions, activities, and license types | C | SEARCH | Read institution-specific activity and exemption fields |
| 05.020 | T1 | Hong Kong | 05 | [SFC public register of licensed persons and institutions](https://apps.sfc.hk/publicregWeb/searchByName) | Securities/futures licenses and regulated activities | C | SEARCH | License type, conditions, and representative status matter |
| 05.021 | T1 | Japan | 05 | [FSA lists of licensed financial institutions](https://www.fsa.go.jp/en/regulated/licensed/index.html) | Banks, securities firms, insurers, funds, and crypto operators | C | WEB,DL | Lists are category-specific and sometimes Japanese-only |
| 05.022 | T1 | India | 05 | [SEBI intermediaries portal](https://siportal.sebi.gov.in/intermediary/) | Registered securities intermediaries | C | SEARCH | Registration category and current suspension/action status require review |
| 05.023 | T1 | United Arab Emirates/federal | 05 | [SCA licensed companies](https://www.sca.gov.ae/en/open-data/licensed-companies.aspx) | Federal securities and investment licensees | C | SEARCH,DL | DIFC and ADGM entities use separate regulators |
| 05.024 | T1 | Saudi Arabia | 05 | [Capital Market Authority authorized persons](https://cma.org.sa/en/Market/AuthorisedPersons/Pages/default.aspx) | Capital-market institutions and permissions | C | SEARCH | Authorization category and disciplinary status are separate fields |
| 05.025 | T1 | South Africa | 05 | [FSCA regulated entities and persons](https://www2.fsca.co.za/Regulated%20Entities/Pages/List-Regulated-Entities-Persons.aspx) | South African financial-sector licenses and entity status | C | SEARCH,DL | Search across applicable license category and former names |
| 05.026 | T1 | Brazil | 05 | [CVM regulated participant search](https://sistemas.cvm.gov.br/) | Public companies, funds, auditors, and market participants | C | SEARCH | Multiple systems; filings and enforcement require separate searches |
| 05.027 | T1 | Mexico | 05 | [CNBV supervised-entity information](https://www.gob.mx/cnbv/es/acciones-y-programas/informacion-relevante-cnbv) | Authorized and supervised financial entities and sector data | C | WEB,DL | Spanish interface; entity type determines data source |
| 05.028 | T1 | Global | 05 | [IOSCO investor alerts portal](https://www.iosco.org/i-scan/) | Warnings reported by securities regulators across jurisdictions | EV | SEARCH | Aggregates member alerts; retrieve the issuing regulator's original notice |

### 8.6 Prudential, banking, insurance, and payments

| ID | Tier | J/C | D | Official source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 06.001 | T1 | United States | 06 | [FDIC BankFind Suite](https://banks.data.fdic.gov/bankfind-suite/bankfind) | Insured-bank identity, history, branches, financials, and failures | Q/C | SEARCH,API,DL | Does not cover every nonbank or credit union |
| 06.002 | T1 | United States | 06 | [FFIEC National Information Center](https://www.ffiec.gov/npw) | Bank holding companies, regulated institutions, hierarchy, and financial data | Q/C | SEARCH,DL | Reporting structure and effective dates require care |
| 06.003 | T1 | United States | 06 | [OCC Financial Institution Search](https://www.occ.gov/topics/charters-and-licensing/financial-institution-lists/index-financial-institution-lists.html) | National banks, federal savings associations, and OCC-chartered institutions | C | WEB,DL | OCC scope excludes state-chartered banks and many nonbanks |
| 06.004 | T1 | United States | 06 | [NCUA Research a Credit Union](https://mapping.ncua.gov/) | Federally insured credit-union identity, status, and financials | Q/C | SEARCH | Credit-union scope; historical mergers and liquidations need review |
| 06.005 | T1 | United States | 06 | [Federal Reserve National Information Center](https://www.ffiec.gov/npw) | Supervised institution structures and regulatory data | Q/C | SEARCH | Shared FFIEC interface; identify the responsible regulator |
| 06.006 | T1 | European Union | 06 | [EBA registers and other lists of institutions](https://www.eba.europa.eu/risk-and-data-analysis/data/registers-and-other-list-institutions) | EU/EEA credit, payment, e-money, and related institution registers | C | SEARCH,DL | National competent-authority records may be more current |
| 06.007 | T1 | Euro area | 06 | [ECB list of supervised banks](https://www.bankingsupervision.europa.eu/banking/list/html/index.en.html) | Significant institutions and supervisory status | C | WEB,DL | Scope reflects Single Supervisory Mechanism classification |
| 06.008 | T1 | Euro area | 06 | [ECB Register of Institutions and Affiliates Data](https://www.ecb.europa.eu/stats/financial_corporations/list_of_financial_institutions/html/index.en.html) | Monetary financial institutions, investment funds, insurers, and payment statistics lists | M/C | SEARCH,DL | Category definitions and reporting periods differ |
| 06.009 | T1 | United Kingdom | 06 | [Bank of England Prudential Regulation](https://www.bankofengland.co.uk/prudential-regulation) | PRA policy, supervision, waivers, and regulated-sector materials | EV | WEB | Use FCA Register for firm-level current permissions |
| 06.010 | T1 | Canada | 06 | [OSFI supervision and “who we regulate” resources](https://www.osfi-bsif.gc.ca/en/supervision) | Federally regulated banks, insurers, trust/loan companies, and pensions | C | WEB,DL | Institution list is delivered through Open Government; provincial and securities entities are outside scope |
| 06.011 | T1 | Australia | 06 | [APRA register of authorized institutions](https://www.apra.gov.au/register-of-authorised-deposit-taking-institutions) | Authorized deposit-taking institutions and prudential status | C | WEB,DL | Separate registers cover insurers and superannuation entities |
| 06.012 | T1 | New Zealand | 06 | [Reserve Bank registers](https://www.rbnz.govt.nz/regulation-and-supervision/cross-sector-oversight/registers-of-licensed-and-registered-entities) | Registered banks, insurers, NBDTs, and other regulated entities | C | WEB | Category-specific conditions and legislative changes matter |
| 06.013 | T1 | Singapore | 06 | [MAS Financial Institutions Directory](https://eservices.mas.gov.sg/fid/institution) | Banks, insurers, payment institutions, capital-markets firms, and activities | C | SEARCH | Verify exact license/regulated activity and status |
| 06.014 | T1 | Hong Kong | 06 | [HKMA Register of Authorized Institutions](https://vpr.hkma.gov.hk/eng/regulatory-resources/registers/register-of-ais-and-lros/) | Banks, restricted-license banks, deposit-taking companies, and local offices | C | SEARCH | Securities permissions and insurers use other regulators |
| 06.015 | T1 | India | 06 | [RBI regulated entities and bank lists](https://www.rbi.org.in/Scripts/BankLinks.aspx) | Commercial, cooperative, foreign, and specialized-bank links | C | WEB | Multiple lists; confirm license and cancellation notices |
| 06.016 | T1 | Ireland | 06 | [Central Bank of Ireland registers](https://registers.centralbank.ie/) | Authorized banks, insurers, funds, intermediaries, and payment firms | C | SEARCH | Register category and passport status determine scope |
| 06.017 | T1 | United Arab Emirates | 06 | [Central Bank UAE register](https://www.centralbank.ae/en/licensing/) | Licensed banks, insurers, exchange houses, payment and finance companies | C | WEB,DL | Free-zone regulators and some virtual-asset firms are separate |
| 06.018 | T1 | Saudi Arabia | 06 | [Saudi Central Bank licensed entities](https://sama.gov.sa/en-US/Supervision/LicenseEntities/Pages/default.aspx) | Banks, insurers, finance, payment, and exchange licensees | C | WEB | License category and branch status require confirmation |
| 06.019 | T1 | South Africa | 06 | [South African Reserve Bank registered banks](https://www.resbank.co.za/en/home/what-we-do/Prudentialregulation/sa-registered-banks-and-representative-offices) | Registered banks, mutual banks, and representative offices | C | WEB,DL | Nonbank financial services use FSCA sources |
| 06.020 | T1 | Brazil | 06 | [Banco Central do Brasil supervised institutions](https://www.bcb.gov.br/estabilidadefinanceira/encontreinstituicao) | Authorized financial and payment institutions | C | SEARCH | Authorization status, conglomerate, and operating brand can differ |
| 06.021 | T1 | Mexico | 06 | [CNBV supervised entities](https://www.gob.mx/cnbv/acciones-y-programas/entidades-supervisadas-130846) | Banks, brokerages, funds, and other supervised sectors | C | WEB,DL | Spanish lists may be separated by sector and update date |
| 06.022 | T1 | Global | 06 | [BIS central bank websites](https://www.bis.org/cbanks.htm) | Official central-bank and monetary-authority directory | P | WEB | Directory points to authorities; it is not a license register |
| 06.023 | T1 | Global | 06 | [IMF Financial Soundness Indicators](https://data.imf.org/fsi) | Cross-country banking soundness series | Q | API,DL | Country definitions, reporting institutions, and gaps vary |
| 06.024 | T1 | Global | 06 | [World Bank Global Financial Development Database](https://www.worldbank.org/en/publication/gfdr/data/global-financial-development-database) | Financial-system depth, access, efficiency, and stability indicators | A | DL | Cross-country comparability and lag require methodology review |
| 06.025 | T1 | Global/insurance | 06 | [IAIS member directory](https://www.iais.org/about-the-iais/iais-members/) | Official insurance-supervisor and member-jurisdiction links | P | WEB | Membership is not firm-level authorization data |

### 8.7 Enforcement, courts, insolvency, and legal proceedings

| ID | Tier | J/C | D | Official source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 07.001 | T1 | United States | 07 | [Department of Justice news](https://www.justice.gov/news) | Charging, plea, conviction, settlement, and policy announcements | EV | SEARCH | Announcement is not the docket; retain exact procedural language |
| 07.002 | T1 | United States | 07 | [DOJ Fraud Section cases](https://www.justice.gov/criminal-fraud/related-enforcement-actions) | Corporate resolutions and related enforcement actions | EV | WEB,DL | Scope is Fraud Section; retrieve agreements and court records |
| 07.003 | T1 | United States | 07 | [SEC enforcement actions](https://www.sec.gov/enforcement-litigation/litigation-releases) | Civil complaints, orders, judgments, and litigation releases | EV | SEARCH,DL | Allegations, settlements, and adjudicated findings must be distinguished |
| 07.004 | T1 | United States | 07 | [CFTC enforcement actions](https://www.cftc.gov/LawRegulation/EnforcementActions/index.htm) | Commodity and derivatives enforcement records | EV | SEARCH,DL | Orders and complaints have different evidentiary status |
| 07.005 | T1 | United States | 07 | [FinCEN enforcement actions](https://www.fincen.gov/news-room/enforcement-actions) | BSA civil money penalties and related documents | EV | WEB,DL | Scope is FinCEN authority; parallel proceedings may exist |
| 07.006 | T1 | United States | 07 | [OFAC civil penalties and enforcement](https://ofac.treasury.gov/civil-penalties-and-enforcement-information) | Sanctions enforcement notices and settlements | EV | WEB,DL | Settlement terms, base penalty, and admissions vary |
| 07.007 | T1 | United States | 07 | [FTC legal library](https://www.ftc.gov/legal-library) | Complaints, orders, decisions, rules, and court filings | EV | SEARCH,DL | Administrative and federal-court stages differ |
| 07.008 | T1 | United States | 07 | [CFPB enforcement actions](https://www.consumerfinance.gov/enforcement/actions/) | Consumer-finance complaints, consent orders, and judgments | EV | SEARCH,DL | Check status, vacatur, termination, and parallel actions |
| 07.009 | T1 | United States | 07 | [OCC enforcement actions](https://www.occ.gov/topics/supervision-and-examination/enforcement-actions/index-enforcement-actions.html) | Formal actions against national banks, institutions, and institution-affiliated parties | EV | SEARCH | Search scope and termination status require review |
| 07.010 | T1 | United States | 07 | [FDIC orders and decisions](https://orders.fdic.gov/s/) | FDIC enforcement orders, notices, and adjudicated decisions | EV | SEARCH | Order may be terminated or superseded; capture status |
| 07.011 | T1 | United States | 07 | [Federal Reserve enforcement resources](https://www.federalreserve.gov/supervisionreg/topics/enforcement.htm) | Board enforcement-action search, releases, and supervisory policy | EV | SEARCH,DL | Responsible agency and action status vary; use the linked order |
| 07.012 | T1 | United States/federal courts | 07 | [PACER](https://pacer.uscourts.gov/) | Federal dockets and filed documents of record | C | SEARCH,REG,FEE | Fees, seals, redactions, and coverage constraints apply |
| 07.013 | T2 | United States/federal and state | 07 | [CourtListener/RECAP](https://www.courtlistener.com/) | Searchable opinions and contributed PACER docket documents | C | SEARCH,API | Not the court system; docket coverage is incomplete and contributed |
| 07.014 | T1 | United States | 07 | [US Supreme Court opinions](https://www.supremecourt.gov/opinions/opinions.aspx) | Slip opinions, orders, and bound-volume links | EV | WEB,DL | Slip opinions can be revised; check final bound text and mandate |
| 07.015 | T1 | United States | 07 | [US Tax Court DAWSON](https://dawson.ustaxcourt.gov/) | Tax Court dockets, filings, orders, and opinions | C | SEARCH | Sealed/redacted records and document access limits apply |
| 07.016 | T1 | United Kingdom | 07 | [Find Case Law](https://caselaw.nationalarchives.gov.uk/) | Official judgments from UK courts and tribunals | C | SEARCH,DL | Coverage is not comprehensive for all historical or lower-court matters |
| 07.017 | T1 | United Kingdom | 07 | [FCA enforcement notices](https://www.fca.org.uk/news/search-results?category=final-notices) | Final, decision, and supervisory notices and enforcement outcomes | EV | SEARCH | Search the notices database and distinguish notice stage |
| 07.018 | T1 | United Kingdom | 07 | [Serious Fraud Office cases](https://www.sfo.gov.uk/our-cases/) | SFO investigations, prosecutions, and case outcomes | EV | WEB | Investigation announcement is not a finding; check court disposition |
| 07.019 | T1 | European Union | 07 | [CURIA case-law search](https://curia.europa.eu/juris/recherche.jsf?language=en) | Court of Justice and General Court cases, opinions, and judgments | C | SEARCH,DL | Language/version and procedural stage require review |
| 07.020 | T1 | European Union | 07 | [European Commission competition cases](https://competition-cases.ec.europa.eu/search) | Antitrust, merger, cartel, and state-aid case records | C | SEARCH | Decision, summary, press release, and appeal may differ |
| 07.021 | T1 | Council of Europe | 07 | [HUDOC](https://hudoc.echr.coe.int/) | European Court of Human Rights judgments and decisions | C | SEARCH | Chamber/Grand Chamber status and execution are separate |
| 07.022 | T1 | Global | 07 | [International Court of Justice cases](https://www.icj-cij.org/cases) | ICJ contentious cases, advisory opinions, orders, and pleadings | C | SEARCH,DL | State-party jurisdiction; interim and final stages differ |
| 07.023 | T1 | Global | 07 | [International Criminal Court cases](https://www.icc-cpi.int/cases) | ICC situations, cases, warrants, decisions, and judgments | C | SEARCH | Public records may be redacted; warrant is not conviction |
| 07.024 | T1 | Canada | 07 | [Supreme Court of Canada decisions](https://decisions.scc-csc.ca/scc-csc/en/nav.do?iframe=true&pedisable=false&site_preference=normal) | Supreme Court decisions and case information | C | SEARCH | Lower-court record must be sourced separately |
| 07.025 | T2 | Canada | 07 | [CanLII](https://www.canlii.org/) | Broad Canadian case law and legislation search | C | SEARCH,API | Non-government legal-information institute; verify court record for critical reliance |
| 07.026 | T1 | Australia | 07 | [Federal Court judgments](https://www.fedcourt.gov.au/digital-law-library/judgments) | Federal Court and Federal Circuit and Family Court decisions | C | SEARCH | Other courts and tribunal records require jurisdiction-specific sources |
| 07.027 | T1 | New Zealand | 07 | [Ministry of Justice judicial decisions](https://www.justice.govt.nz/courts/decisions/) | Published New Zealand court decisions | C | SEARCH | Publication is selective and subject to suppression orders |
| 07.028 | T1 | Hong Kong | 07 | [Hong Kong Judiciary judgments](https://legalref.judiciary.hk/lrs/common/ju/judgment.jsp) | Court judgments and reasons | C | SEARCH | Search coverage, reporting restrictions, and appeal stage matter |
| 07.029 | T1 | Singapore | 07 | [Singapore Courts judgments](https://www.elitigation.sg/gd/) | Supreme Court and State Courts written judgments | C | SEARCH | Not every matter yields a published judgment |
| 07.030 | T1 | India | 07 | [eCourts Services](https://services.ecourts.gov.in/ecourtindia_v6/) | Case status, orders, judgments, and court calendars | C | SEARCH | Coverage and digitization vary across courts and states |
| 07.031 | T2 | South Africa | 07 | [SAFLII](https://www.saflii.org/) | Searchable South African judgments and legal materials | C | SEARCH | Independent legal-information institute; publication coverage is incomplete |
| 07.032 | T1 | Brazil | 07 | [Supreme Federal Court case-law portal](https://portal.stf.jus.br/jurisprudencia/) | STF decisions, dockets, and jurisprudence | C | SEARCH | Portuguese records; lower federal and state courts are separate |
| 07.033 | T1 | Americas | 07 | [Inter-American Court jurisprudence](https://www.corteidh.or.cr/casos_sentencias.cfm?lang=en) | Judgments, orders, and advisory opinions | C | WEB,DL | Applies to the Court's jurisdiction; compliance status is separate |
| 07.034 | T1 | United Kingdom/insolvency | 07 | [The Gazette insolvency notices](https://www.thegazette.co.uk/insolvency) | Statutory insolvency, winding-up, and appointment notices | C | SEARCH,DL | Notice is not a full case file; later notices may change status |
| 07.035 | T1 | European Union | 07 | [EU e-Justice bankruptcy and insolvency-register search](https://e-justice.europa.eu/topics/registers-business-insolvency-land/bankruptcy-insolvency-registers-search-insolvent-debtors-eu_en) | Cross-border access to connected national insolvency registers | C | SEARCH | Member-state coverage, access, and legal effect vary |

### 8.8 Procurement, public spending, and exclusions

| ID | Tier | J/C | D | Official source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 08.001 | T1 | United States | 08 | [SAM.gov entity and exclusion search](https://sam.gov/search/) | Federal registrations, exclusions, contract opportunities, and assistance listings | C | SEARCH,API | Entity registration is not qualification; exclusion scope/date matter |
| 08.002 | T1 | United States | 08 | [USAspending.gov](https://www.usaspending.gov/) | Federal contract, grant, loan, and recipient spending data | D | SEARCH,API,DL | Reporting corrections, subaward gaps, and obligation/outlay distinctions |
| 08.003 | T1 | United States | 08 | [Federal Procurement Data System reports](https://www.fpds.gov/) | Historical federal contract-action detail and reports | D | SEARCH,REG | Functions are migrating to SAM.gov; modifications create duplicates if mishandled |
| 08.004 | T1 | Global/MDB | 08 | [World Bank projects and operations](https://projects.worldbank.org/) | Project, financing, procurement, and award context | C | SEARCH,API | Award and disbursement fields may update after the event |
| 08.005 | T1 | Global/MDB | 08 | [World Bank debarred firms](https://www.worldbank.org/en/projects-operations/procurement/debarred-firms) | Supplier ineligibility and cross-debarment | EV | SEARCH,DL | Administrative sanction; confirm dates and release conditions |
| 08.006 | T1 | Asia/MDB | 08 | [ADB procurement notices](https://www.adb.org/work-with-us/business-opportunities) | Project opportunities, procurement plans, awards, and consultant notices | C | SEARCH | Project-level publication completeness varies |
| 08.007 | T1 | Africa/MDB | 08 | [AfDB procurement notices](https://www.afdb.org/en/projects-and-operations/procurement) | Project procurement opportunities and awards | C | SEARCH | Search interface and historic coverage vary |
| 08.008 | T1 | Americas/MDB | 08 | [IDB project procurement](https://www.iadb.org/en/how-we-can-work-together/procurement) | Procurement policies, notices, and awards | C | SEARCH | Borrower-executed procurement data can be decentralized |
| 08.009 | T1 | Europe/MDB | 08 | [EBRD ECEPP](https://ecepp.ebrd.com/) | EBRD client e-procurement notices and contract data | C | SEARCH,REG | Coverage is limited to participating projects/processes |
| 08.010 | T1 | Global/UN | 08 | [UN Global Marketplace](https://www.ungm.org/Public/Notice) | UN procurement notices, awards, and vendor information | C | SEARCH,REG | Participating-agency coverage and award detail vary |
| 08.011 | T1 | European Union | 08 | [Tenders Electronic Daily](https://ted.europa.eu/) | EU public-procurement notices and contract awards | D | SEARCH,API,DL | Notice corrections, lots, and framework call-offs require deduplication |
| 08.012 | T1 | European Union | 08 | [EU Financial Transparency System funding recipients](https://commission.europa.eu/about/service-standards-and-principles/transparency/funding-recipients_en) | Recipients of funds managed directly by the European Commission | A | SEARCH,DL | Does not cover all shared-management EU spending |
| 08.013 | T1 | United Kingdom | 08 | [Contracts Finder](https://www.contractsfinder.service.gov.uk/Search) | England and UK-wide lower-threshold opportunities and awards | C | SEARCH,API | Coverage thresholds and devolved systems vary |
| 08.014 | T1 | United Kingdom | 08 | [Find a Tender](https://www.find-tender.service.gov.uk/Search) | Higher-value UK procurement notices and awards | C | SEARCH,API | Corrections and lot-level structure require careful linkage |
| 08.015 | T1 | Canada | 08 | [CanadaBuys](https://canadabuys.canada.ca/en/tender-opportunities) | Federal procurement opportunities, awards, and supplier information | C | SEARCH | Provincial/municipal procurement sits elsewhere |
| 08.016 | T1 | Australia | 08 | [AusTender](https://www.tenders.gov.au/) | Australian Government opportunities, contracts, and standing offers | C | SEARCH,DL | Amendments and parent/child contracts affect totals |
| 08.017 | T1 | New Zealand | 08 | [Government Electronic Tenders Service](https://www.gets.govt.nz/) | New Zealand public-sector opportunities and award notices | C | SEARCH,REG | Some documents require registration; local-government coverage varies |
| 08.018 | T1 | Singapore | 08 | [GeBIZ](https://www.gebiz.gov.sg/) | Singapore public opportunities and awards | C | SEARCH | Detailed documents and supplier functions may require registration |
| 08.019 | T1 | India | 08 | [Central Public Procurement Portal](https://eprocure.gov.in/eprocure/app) | Central-government tenders and award information | C | SEARCH | Agency and state portals may contain additional records |
| 08.020 | T1 | South Africa | 08 | [eTender Publication Portal](https://www.etenders.gov.za/) | Public tenders and awards across participating bodies | C | SEARCH | Publication completeness and historic availability require validation |
| 08.021 | T1 | Brazil | 08 | [National Public Procurement Portal](https://pncp.gov.br/app/editais) | Procurement plans, notices, contracts, and suppliers | C | SEARCH,API | Federal entities implemented at different times; record amendments |
| 08.022 | T1 | Mexico | 08 | [Compranet](https://upcp-compranet.hacienda.gob.mx/) | Federal procurement procedures and contract information | C | SEARCH | Platform transitions and decentralized records can limit continuity |

### 8.9 Tax, customs, trade, and export controls

| ID | Tier | J/C | D | Official source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 09.001 | T1 | Global/OECD | 09 | [Global Forum peer reviews](https://www.oecd.org/tax/transparency/documents/exchange-of-information-on-request-ratings.htm) | Tax-transparency and exchange-of-information ratings | P | WEB,DL | Rating is assessment-date specific and not a tax-haven list |
| 09.002 | T1 | Global/OECD | 09 | [Common Reporting Standard resources](https://www.oecd.org/tax/automatic-exchange/common-reporting-standard/) | CRS standard, participating jurisdictions, and exchange framework | P | WEB,DL | Domestic implementation, reservations, and effective dates vary |
| 09.003 | T1 | Global/OECD | 09 | [BEPS actions](https://www.oecd.org/tax/beps/beps-actions/) | International tax standards, peer reviews, and implementation reports | P | WEB,DL | Not all outputs are legally binding; jurisdiction adoption varies |
| 09.004 | T1 | European Union | 09 | [EU list of non-cooperative jurisdictions for tax purposes](https://www.consilium.europa.eu/en/policies/eu-list-of-non-cooperative-jurisdictions/) | Current EU tax list and conclusions | P | WEB,DL | Political list with defined criteria; distinguish Annex I and II |
| 09.005 | T1 | European Union | 09 | [TARIC consultation](https://ec.europa.eu/taxation_customs/dds2/taric/taric_consultation.jsp?Lang=en) | EU tariff, restriction, quota, and measure lookup | D | SEARCH | Classification and origin are fact-specific; legal acts control |
| 09.006 | T1 | United States | 09 | [CBP CROSS rulings](https://rulings.cbp.gov/) | Customs classification, origin, and valuation rulings | C | SEARCH | Rulings are fact-specific and may be revoked or modified |
| 09.007 | T1 | United States | 09 | [USITC Harmonized Tariff Schedule](https://hts.usitc.gov/) | Current US tariff classifications and rates | P | SEARCH,DL | Classification depends on product facts; chapters and notes control |
| 09.008 | T1 | United States | 09 | [US Census International Trade Data](https://www.census.gov/foreign-trade/data/index.html) | Official US import/export statistics | M | API,DL | Revisions, suppression, valuation basis, and partner definitions |
| 09.009 | T1 | United States | 09 | [Export Administration Regulations](https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C) | Current EAR licensing and control provisions | C | WEB | Supplement lists, classification, end use, end user, and general orders interact |
| 09.010 | T1 | United States | 09 | [BIS Commerce Control List](https://www.bis.gov/regulations/ear/commerce-control-list) | ECCNs and export-control reasons | P | WEB,DL | Classification requires technical facts and full EAR analysis |
| 09.011 | T1 | United Kingdom | 09 | [UK Trade Tariff](https://www.trade-tariff.service.gov.uk/) | Commodity codes, duties, VAT, quotas, and measures | D | SEARCH | Origin, customs procedure, and date affect treatment |
| 09.012 | T1 | Canada | 09 | [Canada Customs Tariff](https://www.cbsa-asfc.gc.ca/trade-commerce/tariff-tarif/menu-eng.html) | Canadian tariff classification and rates | A/P | WEB,DL | Administrative guidance does not replace Customs Tariff law |
| 09.013 | T1 | Australia | 09 | [Australian Border Force tariff classification](https://www.abf.gov.au/importing-exporting-and-manufacturing/tariff-classification) | Tariff schedules, concessions, and classification guidance | P | WEB,DL | Product facts and concession orders determine final treatment |
| 09.014 | T1 | Global/WTO | 09 | [WTO Tariff Analysis Online](https://tao.wto.org/) | Bound and applied tariff data reported by members | A/P | SEARCH,DL | Reporting years and nomenclature versions differ |
| 09.015 | T1 | Global/UN | 09 | [UN Comtrade](https://comtradeplus.un.org/) | Official merchandise and services trade statistics | M/A | SEARCH,API,DL | Reporter data, revisions, mirror flows, and classification changes |
| 09.016 | T1 | Global/ITC | 09 | [ITC Trade Map](https://www.trademap.org/) | Trade flows, tariffs, and market indicators | M/A | SEARCH,REG | Derived from national/UN data; licensing and aggregation constraints |
| 09.017 | T1 | Global/World Bank | 09 | [World Integrated Trade Solution](https://wits.worldbank.org/) | Trade, tariff, and non-tariff data across partner datasets | A/P | SEARCH,DL | Harmonization and source-vintage differences require review |
| 09.018 | T1 | Global/WCO | 09 | [World Customs Organization tools and instruments](https://www.wcoomd.org/en/topics/nomenclature/instrument-and-tools.aspx) | Harmonized System nomenclature and customs standards | P | WEB | Full commercial products may be licensed; national tariff controls |
| 09.019 | T1 | Global/UNCTAD | 09 | [TRAINS Online](https://trainsonline.unctad.org/) | Tariffs, non-tariff measures, and trade-control classifications | A/P | SEARCH | Country coverage and reporting vintage vary |
| 09.020 | T1 | United States | 09 | [OFAC sanctions programs](https://ofac.treasury.gov/sanctions-programs-and-country-information) | Trade/payment restrictions imposed through US sanctions | EV | WEB | Sanctions analysis is separate from customs classification and export licensing |

### 8.10 Corruption, bribery, and public integrity

| ID | Tier | J/C | D | Official source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 10.001 | T2 | Global | 10 | [Transparency International Corruption Perceptions Index](https://www.transparency.org/en/cpi) | Perceived public-sector corruption scores and methodology | A | WEB,DL | Perception-based composite; not proof of corruption by a person or entity |
| 10.002 | T1 | Global/World Bank | 10 | [Worldwide Governance Indicators](https://www.worldbank.org/en/publication/worldwide-governance-indicators) | Control of corruption, rule of law, and governance estimates | A | DL | Composite estimates carry uncertainty intervals and source dependence |
| 10.003 | T1 | Global/World Bank | 10 | [Enterprise Surveys](https://www.enterprisesurveys.org/) | Firm-level reported business constraints, bribery incidence, and governance indicators | P | SEARCH,DL | Survey years, samples, and questions vary by economy |
| 10.004 | T1 | Global/UN | 10 | [UNODC corruption resources](https://www.unodc.org/unodc/en/corruption/index.html) | UNCAC materials, country reviews, tools, and corruption data links | P | WEB,DL | Review publication and data coverage are uneven |
| 10.005 | T1 | Global/OECD | 10 | [OECD Anti-Bribery Convention country monitoring](https://www.oecd.org/corruption/anti-bribery/country-monitoring-of-the-oecd-anti-bribery-convention.htm) | Peer-review reports on foreign-bribery enforcement and implementation | P | WEB,DL | Applies to Convention parties; reports reflect review dates |
| 10.006 | T1 | Europe | 10 | [GRECO country evaluations](https://www.coe.int/en/web/greco/evaluations) | Council of Europe anti-corruption evaluation and compliance reports | P | WEB,DL | Evaluation rounds cover defined themes and dates |
| 10.007 | T1 | United States | 10 | [DOJ FCPA enforcement](https://www.justice.gov/criminal-fraud/foreign-corrupt-practices-act) | Criminal FCPA cases, opinions, policy, and guidance | EV | WEB,DL | Retrieve charging and resolution documents; corporate and individual stages differ |
| 10.008 | T1 | United States | 10 | [SEC FCPA enforcement actions](https://www.sec.gov/enforcement-litigation/foreign-corrupt-practices-act) | Civil FCPA cases and issuer-accounting-control actions | EV | WEB,DL | Allegation, settlement, and adjudication are distinct |
| 10.009 | T1 | United Kingdom | 10 | [Serious Fraud Office cases](https://www.sfo.gov.uk/our-cases/) | Bribery and serious-fraud investigations, prosecutions, and resolutions | EV | WEB | Investigation is not a finding; retrieve court or agreement record |
| 10.010 | T1 | United Kingdom | 10 | [Bribery Act guidance](https://www.gov.uk/government/publications/bribery-act-2010-guidance) | Government guidance on adequate procedures and statutory offenses | P | WEB,DL | Guidance is not case-specific legal advice |
| 10.011 | T1 | European Union | 10 | [OLAF investigations and reports](https://anti-fraud.ec.europa.eu/investigations_en) | EU budget fraud and misconduct investigation framework and case summaries | EV/A | WEB,DL | Recommendations are not judicial findings; confidentiality limits detail |
| 10.012 | T1 | European Union | 10 | [European Public Prosecutor's Office](https://www.eppo.europa.eu/index_en) | EPPO investigations, charges, judgments, news, and annual statistics | EV | SEARCH | Press stage and national court disposition require distinction |
| 10.013 | T1 | Global/World Bank | 10 | [World Bank Integrity Vice Presidency](https://www.worldbank.org/en/about/unit/integrity-vice-presidency) | Investigation, sanctions-system, and integrity-compliance resources | EV/A | WEB,DL | Institutional administrative process, not a criminal court |
| 10.014 | T2 | Global | 10 | [Basel AML Index](https://index.baselgovernance.org/) | Composite jurisdiction ML/TF risk including corruption dimensions | A | WEB,REG,DL | Composite methodology and missing data; not an entity-risk score |
| 10.015 | T2 | Global | 10 | [U4 Anti-Corruption Resource Centre](https://www.u4.no/) | Sourced research on corruption risks, sectors, and interventions | P | SEARCH,DL | Research source, not an issuing authority or live enforcement register |

### 8.11 Fraud, cyber, and technical threat intelligence

| ID | Tier | J/C | D | Official source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 11.001 | T1 | United States/global relevance | 11 | [CISA Cybersecurity Advisories](https://www.cisa.gov/news-events/cybersecurity-advisories) | Joint advisories, malware analysis, mitigations, and threat reporting | EV | SEARCH,DL | Advisory scope and indicators age quickly; confirm affected versions |
| 11.002 | T1 | United States/global relevance | 11 | [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | Vulnerabilities with evidence of exploitation and federal remediation dates | EV | WEB,DL | Catalog is not all vulnerabilities or a general severity ranking |
| 11.003 | T1 | United States | 11 | [NIST National Vulnerability Database](https://nvd.nist.gov/) | CVE enrichment, CVSS, CPEs, references, and change history | C | SEARCH,API,DL | Enrichment can lag; vendor advisory and CVE record should be checked |
| 11.004 | T1 | United States | 11 | [FBI Internet Crime Complaint Center](https://www.ic3.gov/) | Public alerts and annual cyber-enabled-crime complaint statistics | EV/A | WEB,DL | Complaint counts are reported losses, not adjudicated cases or full incidence |
| 11.005 | T1 | United States | 11 | [FTC Consumer Sentinel data](https://public.tableau.com/app/profile/federal.trade.commission/viz/ConsumerSentinelNetworkDataBook/ReportsbyCategory) | Reported fraud, identity-theft, and consumer-complaint trends | Q/A | WEB,DL | Self-reported complaints; public dashboard is aggregated and may be revised |
| 11.006 | T1 | United States | 11 | [FTC scams and alerts](https://consumer.ftc.gov/consumer-alerts) | Current consumer-fraud patterns and prevention notices | EV | SEARCH | Guidance and reports do not establish a named party's liability |
| 11.007 | T1 | United States | 11 | [SEC Investor Alerts and Bulletins](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins) | Investment-fraud warnings and emerging schemes | EV | SEARCH | Alert may describe a typology rather than a legal action |
| 11.008 | T1 | United States | 11 | [FINRA Investor Insights](https://www.finra.org/investors/insights) | Broker/investment scam and market-abuse warnings | EV | SEARCH | Educational warnings are not findings against an entity; filter to the relevant alert |
| 11.009 | T1 | United Kingdom/global relevance | 11 | [National Cyber Security Centre advisories](https://www.ncsc.gov.uk/section/keep-up-to-date/threat-reports) | UK threat reports, alerts, and mitigation guidance | EV | SEARCH,DL | Applicability depends on affected product, sector, and date |
| 11.010 | T1 | United Kingdom | 11 | [Action Fraud](https://www.actionfraud.police.uk/) | UK fraud reporting, alerts, and public guidance | EV | WEB | A report to Action Fraud is not a finding or necessarily public |
| 11.011 | T1 | European Union | 11 | [ENISA cyber-threat publications](https://www.enisa.europa.eu/topics/cyber-threats?tab=publications) | EU cyber-threat trends, incidents, actors, and sectors | A/P | WEB,DL | Analytical synthesis; not a live incident or attribution register |
| 11.012 | T1 | European Union institutions | 11 | [CERT-EU publications](https://cert.europa.eu/publications) | Threat advisories and reports for EU bodies with broader relevance | EV | WEB,DL | Audience and evidence disclosure may be limited |
| 11.013 | T1 | Australia | 11 | [Australian Signals Directorate cyber advisories](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories) | ACSC alerts, advisories, and mitigation guidance | EV | SEARCH | Confirm product versions and whether exploitation is observed |
| 11.014 | T1 | Canada | 11 | [Canadian Centre for Cyber Security alerts](https://www.cyber.gc.ca/en/alerts-advisories) | Canadian cyber alerts, advisories, and guidance | EV | SEARCH | Alert scope and affected sectors vary |
| 11.015 | T1 | Singapore | 11 | [Cyber Security Agency advisories](https://www.csa.gov.sg/alerts-and-advisories/) | Singapore cyber alerts, vulnerabilities, and recommended actions | EV | SEARCH | Technical details may rely on upstream vendor/CVE sources |
| 11.016 | T2 | Hong Kong | 11 | [Hong Kong Computer Emergency Response Team](https://www.hkcert.org/) | Vulnerability, malware, phishing, and incident advisories | EV | SEARCH | Coordination centre, not a court or attribution authority |
| 11.017 | T2 | Global | 11 | [MITRE CVE](https://www.cve.org/) | Canonical public vulnerability identifiers and CNA references | C | SEARCH,API,DL | CVE assignment does not establish exploitability, severity, or exploitation |
| 11.018 | T1 | Global/law enforcement | 11 | [INTERPOL cybercrime](https://www.interpol.int/en/Crimes/Cybercrime) | International law-enforcement operations and cybercrime assessments | EV | WEB | Public summaries omit operational detail; notices are not adjudications |
| 11.019 | T3 | Global/digital assets | 11 | [Chainabuse](https://www.chainabuse.com/) | Community-reported cryptocurrency scam and abuse leads | C | SEARCH | User reports are unverified leads; never establish ownership or wrongdoing alone |
| 11.020 | T1 | Global/vendor-specific | 11 | [Vendor security advisory directory via CISA](https://www.cisa.gov/news-events/cybersecurity-advisories) | Discovery of primary vendor and government technical notices | EV | WEB | Follow references to the vendor's signed advisory and affected-version record |

### 8.12 Law enforcement, wanted persons, and security designations

| ID | Tier | J/C | D | Official source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 12.001 | T1 | Global | 12 | [INTERPOL public notices](https://www.interpol.int/en/How-we-work/Notices/View-Red-Notices) | Public Red Notice and diffusion extracts | EV | SEARCH | Public subset; notice is not an arrest warrant, conviction, or proof of guilt |
| 12.002 | T1 | European Union | 12 | [Europe's Most Wanted](https://eumostwanted.eu/) | Public fugitives submitted by EU member-state teams | EV | SEARCH | Verify issuing national authority and current wanted status |
| 12.003 | T1 | United States | 12 | [FBI Most Wanted](https://www.fbi.gov/wanted) | Federal wanted persons, missing persons, and seeking-information notices | EV | SEARCH | Allegations and charges are not convictions; notice may be withdrawn |
| 12.004 | T1 | United States | 12 | [US Marshals 15 Most Wanted](https://www.usmarshals.gov/what-we-do/fugitive-investigations/15-most-wanted-fugitive) | Priority federal fugitive notices | EV | WEB | Limited priority subset; check capture/status date |
| 12.005 | T1 | United States | 12 | [DEA fugitives](https://www.dea.gov/fugitives) | Public DEA fugitive notices | EV | SEARCH | Charge/warrant stage only; identity and current status require confirmation |
| 12.006 | T1 | United Kingdom | 12 | [National Crime Agency most wanted](https://www.nationalcrimeagency.gov.uk/most-wanted) | UK priority fugitive appeals | EV | WEB | Selected public cases only; allegation and conviction status vary |
| 12.007 | T1 | Canada | 12 | [RCMP wanted persons](https://www.rcmp-grc.gc.ca/en/wanted) | National and regional wanted-person notices | EV | WEB | Public subset and jurisdiction-specific status |
| 12.008 | T1 | Australia/New South Wales | 12 | [New South Wales Police most wanted](https://www.police.nsw.gov.au/can_you_help_us/wanted) | State police wanted-person notices and public appeals | EV | WEB | Jurisdiction-specific public subset; not a comprehensive national warrant database |
| 12.009 | T1 | New Zealand | 12 | [New Zealand Police wanted persons](https://www.police.govt.nz/wanted) | Public wanted and missing-person notices | EV | SEARCH | Public subset; verify current status and subject identity |
| 12.010 | T1 | United States | 12 | [State Department Foreign Terrorist Organizations](https://www.state.gov/foreign-terrorist-organizations/) | Current FTO designations and legal framework | EV | WEB | Distinct from OFAC designations and other terrorism authorities |
| 12.011 | T1 | United Kingdom | 12 | [Proscribed terrorist groups](https://www.gov.uk/government/publications/proscribed-terror-groups-or-organisations--2) | Organizations proscribed under UK terrorism law | EV | WEB,DL | Names, aliases, territorial scope, and deproscription history matter |
| 12.012 | T1 | European Union | 12 | [EU terrorist list legal framework](https://www.consilium.europa.eu/en/policies/fight-against-terrorism/sanctions-against-terrorism/) | EU autonomous terrorism sanctions and current legal-act links | EV | WEB | Use the current Council act/Official Journal for controlling names and measures |
| 12.013 | T1 | Global/UN | 12 | [UN Counter-Terrorism Committee](https://www.un.org/securitycouncil/ctc/) | Country assessment, resolutions, and counterterrorism implementation context | P | WEB,DL | Not a wanted-person database or standalone designation list |
| 12.014 | T1 | Global/UN | 12 | [UN 1267/1989/2253 ISIL and Al-Qaida Committee](https://main.un.org/securitycouncil/en/sanctions/1267) | Regime list, narrative summaries, exemptions, and updates | EV | WEB,DL | Regime-specific; national implementation remains necessary |
| 12.015 | T2 | Global | 12 | [Global Organized Crime Index](https://ocindex.net/) | Country criminality and resilience indicators | P | WEB,DL | Expert-derived composite; not evidence about a named subject |

### 8.13 International organizations and development evidence

| ID | Tier | J/C | D | Official source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 13.001 | T1 | Global/UN | 13 | [UN Official Document System](https://documents.un.org/) | Resolutions, reports, meeting records, and official UN documents | C | SEARCH,DL | Symbol, organ, version, and language must be captured |
| 13.002 | T1 | Global/UN | 13 | [UN Treaty Collection](https://treaties.un.org/) | Treaty text, parties, signatures, ratifications, reservations, and status | C | SEARCH,DL | Domestic implementation and legal effect require separate analysis |
| 13.003 | T1 | Global/World Bank | 13 | [World Bank Documents & Reports](https://documents.worldbank.org/) | Project documents, research, evaluations, and country reports | C | SEARCH,API,DL | Document type and authoring unit affect authority for a proposition |
| 13.004 | T1 | Global/World Bank | 13 | [World Bank Projects & Operations](https://projects.worldbank.org/) | Project objectives, financing, status, procurement, and results | C | SEARCH,API | Status and amounts update; distinguish commitment from disbursement |
| 13.005 | T1 | Global/IMF | 13 | [IMF country information](https://www.imf.org/en/Countries) | Article IV reports, programs, staff reports, and country data | P | SEARCH,DL | Staff views, Executive Board decisions, and member data differ |
| 13.006 | T1 | Global/OECD | 13 | [OECD publications and data](https://www.oecd.org/en/publications.html) | Standards, peer reviews, policy research, and official datasets | C | SEARCH,DL | Membership/coverage and legal force vary by instrument |
| 13.007 | T1 | Global/WTO | 13 | [WTO Documents Online](https://docs.wto.org/) | Agreements, disputes, notifications, trade-policy reviews, and committee records | C | SEARCH,DL | Member notification is self-reported; document status matters |
| 13.008 | T1 | Global/WHO | 13 | [WHO Global Health Observatory](https://www.who.int/data/gho) | Health indicators, estimates, and country profiles | P | SEARCH,API,DL | Modelled versus reported values and revisions must be distinguished |
| 13.009 | T1 | Global/ILO | 13 | [ILO NORMLEX](https://normlex.ilo.org/) | Labor conventions, ratifications, comments, cases, and national law links | C | SEARCH | Supervisory comments have distinct legal and procedural status |
| 13.010 | T1 | Global/UNHCR | 13 | [Refworld](https://www.refworld.org/) | Refugee law, country information, policy, and jurisprudence | C | SEARCH,DL | Repository includes mixed source tiers; tier the underlying publisher |
| 13.011 | T1 | Global/UNCTAD | 13 | [UNCTAD Data Hub](https://unctadstat.unctad.org/) | Trade, investment, shipping, digital economy, and development indicators | A/P | SEARCH,DL | Series definitions, estimations, and revisions vary |
| 13.012 | T1 | Global/UNODC | 13 | [UNODC Data Portal](https://dataunodc.un.org/) | Crime, drugs, trafficking, homicide, and justice indicators | A/P | SEARCH,DL | National reporting gaps and definitional differences are material |
| 13.013 | T1 | Global/WIPO | 13 | [WIPO Global Brand Database](https://branddb.wipo.int/) | Trademark records from international and participating national collections | C | SEARCH | Coverage and legal status depend on the office of record |
| 13.014 | T1 | Global/FAO | 13 | [FAOSTAT](https://www.fao.org/faostat/en/) | Agriculture, food, land, emissions, and commodity statistics | A/P | SEARCH,API,DL | National reporting and estimation methods vary |
| 13.015 | T1 | Global/UNESCO | 13 | [UNESCO Institute for Statistics](https://uis.unesco.org/) | Education, science, culture, and communication statistics | A/P | SEARCH,API,DL | Country coverage and time lags vary |

### 8.14 Statistical, economic, fiscal, and market data

| ID | Tier | J/C | D | Official source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 14.001 | T1 | United States | 14 | [Federal Reserve Economic Data](https://fred.stlouisfed.org/) | Large catalog of official economic series and vintages | D/M/Q | SEARCH,API,DL | FRED often republishes other agencies; cite original producer for controlling definitions |
| 14.002 | T1 | United States | 14 | [Bureau of Economic Analysis](https://www.bea.gov/data) | GDP, income, trade in value added, industries, and regional accounts | M/Q/A | API,DL | Revisions, chain-dollar bases, and seasonal adjustment matter |
| 14.003 | T1 | United States | 14 | [Bureau of Labor Statistics](https://www.bls.gov/data/) | Employment, prices, productivity, wages, and occupational data | M/Q/A | SEARCH,API,DL | Survey, seasonal adjustment, and revision status must be recorded |
| 14.004 | T1 | United States | 14 | [Census data](https://data.census.gov/) | Population, business, housing, and economic survey data | P/A | SEARCH,API,DL | Estimate, margin of error, geography, and vintage are inseparable |
| 14.005 | T1 | United States | 14 | [Energy Information Administration](https://www.eia.gov/opendata/) | Energy production, consumption, prices, reserves, and forecasts | D/W/M/A | API,DL | Forecasts must be separated from observed series |
| 14.006 | T1 | United States | 14 | [FiscalData](https://fiscaldata.treasury.gov/) | Federal debt, revenue, spending, securities, and fiscal datasets | D/M | API,DL | Cash, accrual, obligation, and debt concepts differ |
| 14.007 | T1 | European Union | 14 | [Eurostat Data Browser](https://ec.europa.eu/eurostat/databrowser/) | Harmonized EU economic, social, trade, and regional data | M/Q/A | SEARCH,API,DL | Breaks in series, flags, and national-method differences require review |
| 14.008 | T1 | Euro area | 14 | [ECB Data Portal](https://data.ecb.europa.eu/) | Monetary, banking, markets, payments, and supervisory statistics | D/M/Q | SEARCH,API,DL | Frequency, seasonal adjustment, and aggregation differ by series |
| 14.009 | T1 | United Kingdom | 14 | [Office for National Statistics](https://www.ons.gov.uk/) | UK economy, labor, prices, population, business, and census data | M/Q/A | SEARCH,API,DL | Release vintage and revisions must be captured |
| 14.010 | T1 | United Kingdom | 14 | [Bank of England database](https://www.bankofengland.co.uk/boeapps/database/) | Monetary, banking, yield, exchange-rate, and financial series | D/M/Q | SEARCH,DL | Series transformations and discontinued codes require care |
| 14.011 | T1 | Canada | 14 | [Statistics Canada data](https://www.statcan.gc.ca/en/start) | Canadian economic, social, census, and business statistics | M/Q/A | SEARCH,API,DL | Table vector, geography, adjustment, and revision matter |
| 14.012 | T1 | Canada | 14 | [Bank of Canada Valet API](https://www.bankofcanada.ca/valet/docs) | Exchange rates, interest rates, and financial indicators | D | API,DL | Holiday gaps and series definitions require handling |
| 14.013 | T1 | Australia | 14 | [Australian Bureau of Statistics](https://www.abs.gov.au/statistics) | Population, labor, economy, prices, business, and census data | M/Q/A | SEARCH,API,DL | Original, seasonally adjusted, and trend series differ |
| 14.014 | T1 | Australia | 14 | [Reserve Bank of Australia statistics](https://www.rba.gov.au/statistics/) | Interest rates, exchange rates, credit, money, and financial markets | D/M | WEB,DL | Series breaks and methodological notes must be retained |
| 14.015 | T1 | New Zealand | 14 | [Stats NZ Infoshare](https://infoshare.stats.govt.nz/) | Official economic, population, labor, and trade series | M/Q/A | SEARCH,DL | Classification and seasonal treatment vary |
| 14.016 | T1 | Singapore | 14 | [SingStat](https://www.singstat.gov.sg/find-data) | Population, economy, labor, trade, and sector data | M/Q/A | SEARCH,API,DL | Definitions and preliminary/final status matter |
| 14.017 | T1 | Hong Kong | 14 | [Census and Statistics Department](https://www.censtatd.gov.hk/en/) | Hong Kong economic, labor, trade, population, and price data | M/Q/A | SEARCH,API,DL | Series revisions and geographic scope require capture |
| 14.018 | T1 | Japan | 14 | [e-Stat](https://www.e-stat.go.jp/en) | Japanese government statistics across agencies | M/Q/A | SEARCH,API,DL | Translation, survey, and ministry-source details vary |
| 14.019 | T1 | India | 14 | [RBI Database on Indian Economy](https://data.rbi.org.in/) | Monetary, banking, external-sector, and macroeconomic series | D/M/Q | SEARCH,DL | Provisional/revised data and units must be checked |
| 14.020 | T1 | Brazil | 14 | [IBGE SIDRA](https://sidra.ibge.gov.br/home/pimpfbr/brasil) | Brazilian census, economy, agriculture, prices, and industry tables | M/Q/A | SEARCH,API,DL | Portuguese table metadata; seasonal and regional definitions vary |
| 14.021 | T1 | South Africa | 14 | [Statistics South Africa](https://www.statssa.gov.za/) | National economic, population, labor, and social statistics | M/Q/A | SEARCH,DL | Survey limitations, revisions, and geographic changes matter |
| 14.022 | T1 | Global/World Bank | 14 | [World Bank DataBank](https://databank.worldbank.org/) | Development, debt, demographic, governance, and economic indicators | A/P | SEARCH,API,DL | Source, methodology, estimates, and country coverage vary by indicator |
| 14.023 | T1 | Global/IMF | 14 | [IMF Data](https://www.imf.org/en/Data) | Macroeconomic, balance-of-payments, fiscal, financial, and trade series | M/Q/A | SEARCH,API,DL | Country reporting, estimates, and database vintages differ |
| 14.024 | T1 | Global/BIS | 14 | [BIS Data Portal](https://data.bis.org/) | Banking, credit, debt securities, derivatives, property, and exchange-rate data | D/Q | SEARCH,API,DL | Reporting populations and breaks in series require review |
| 14.025 | T1 | Global/OECD | 14 | [OECD Data Explorer](https://data-explorer.oecd.org/) | Harmonized economic, tax, labor, education, and policy indicators | M/Q/A | SEARCH,API,DL | Member/partner coverage and methodology vary by dataset |

### 8.15 Legislation, regulation, gazettes, and parliamentary records

| ID | Tier | J/C | D | Official source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 15.001 | T1 | United States | 15 | [Congress.gov](https://www.congress.gov/) | Bills, laws, resolutions, nominations, treaties, members, and legislative actions | C | SEARCH,API,DL | A bill is not law; track chamber, version, action, and enactment |
| 15.002 | T1 | United States | 15 | [GovInfo](https://www.govinfo.gov/) | Authenticated statutes, Congressional Record, CFR editions, bills, reports, and official publications | C | SEARCH,API,DL | Collection, edition, package, and granule identifiers matter |
| 15.003 | T1 | United States | 15 | [Electronic Code of Federal Regulations](https://www.ecfr.gov/) | Current editorial compilation of federal regulations | D | SEARCH,API | eCFR is authoritative but unofficial; Federal Register and CFR edition establish legal publication history |
| 15.004 | T1 | United States | 15 | [Federal Register](https://www.federalregister.gov/) | Proposed/final rules, notices, orders, and presidential documents | D | SEARCH,API,DL | Web edition is unofficial; linked PDF and printed edition control; effective dates vary |
| 15.005 | T1 | European Union | 15 | [EUR-Lex](https://eur-lex.europa.eu/) | EU treaties, legislation, Official Journal, preparatory documents, and case-law links | D | SEARCH,DL | Consolidated texts may not be legally authentic; check applicability and corrigenda |
| 15.006 | T1 | European Union | 15 | [Official Journal of the European Union](https://eur-lex.europa.eu/oj/direct-access.html) | Official publication of EU legal acts and notices | D | SEARCH,DL | Language versions, corrigenda, entry into force, and direct effect require review |
| 15.007 | T1 | European Union | 15 | [European Parliament Legislative Observatory](https://oeil.secure.europarl.europa.eu/oeil/home/home.do) | Procedure files, documents, institutions, and legislative stage | C | SEARCH | Procedure status is not the final legal text |
| 15.008 | T1 | United Kingdom | 15 | [legislation.gov.uk](https://www.legislation.gov.uk/) | UK primary and secondary legislation and revision status | C | SEARCH,API,DL | Some revised texts have outstanding effects; inspect update status |
| 15.009 | T1 | United Kingdom | 15 | [The Gazette](https://www.thegazette.co.uk/) | Official statutory notices including insolvency, appointments, and honors | D | SEARCH,API,DL | Notice establishes publication, not necessarily underlying fact's final status |
| 15.010 | T1 | United Kingdom | 15 | [UK Parliament bills](https://bills.parliament.uk/) | Bill text, amendments, stages, and publications | C | SEARCH,DL | Proposed text can change; use enacted legislation for current law |
| 15.011 | T1 | Canada | 15 | [Justice Laws Website](https://laws-lois.justice.gc.ca/eng/) | Consolidated federal acts and regulations | C | SEARCH,DL | Official consolidation status and amendment-in-force dates require review |
| 15.012 | T1 | Canada | 15 | [Canada Gazette](https://gazette.gc.ca/) | Official notices, proposed regulations, regulations, and appointments | W/EV | SEARCH,DL | Part I proposals and Part II regulations have different legal status |
| 15.013 | T1 | Australia | 15 | [Federal Register of Legislation](https://www.legislation.gov.au/) | Acts, instruments, compilations, explanatory statements, and gazettes | C | SEARCH,DL | Compilation date and in-force status must be checked |
| 15.014 | T1 | New Zealand | 15 | [New Zealand Legislation](https://www.legislation.govt.nz/) | Acts, bills, legislative instruments, and historical versions | C | SEARCH,DL | Version and commencement provisions determine current effect |
| 15.015 | T1 | Singapore | 15 | [Singapore Statutes Online](https://sso.agc.gov.sg/) | Current and historical acts, subsidiary legislation, and bills | C | SEARCH,DL | Check effective date and revised-edition notes |
| 15.016 | T1 | Hong Kong | 15 | [Hong Kong e-Legislation](https://www.elegislation.gov.hk/) | Authenticated ordinances, subsidiary legislation, and historical versions | C | SEARCH,DL | Language and version dates matter; gazette notices may sit separately |
| 15.017 | T1 | India | 15 | [eGazette of India](https://egazette.nic.in/) | Central government gazette notifications, rules, appointments, and notices | D | SEARCH,DL | OCR/search quality and issue/part identification can constrain retrieval |
| 15.018 | T1 | Japan | 15 | [e-Gov Law Search](https://elaws.e-gov.go.jp/?elaws_search_in_english=1) | Japanese constitution, acts, cabinet orders, and regulations | C | SEARCH | English translations may be unofficial or delayed; Japanese text controls |
| 15.019 | T1 | South Africa | 15 | [Government Gazettes](https://www.gov.za/documents/notices) | National notices, regulations, proclamations, and gazettes | D | SEARCH,DL | Gazette number, date, and later amendment/repeal require capture |
| 15.020 | T1 | Brazil | 15 | [Planalto legislation](https://www4.planalto.gov.br/legislacao) | Federal constitution, codes, laws, decrees, and provisional measures | C | SEARCH | Official Diary is required for publication chronology and some notices |
| 15.021 | T1 | Brazil | 15 | [Diário Oficial da União](https://www.in.gov.br/consulta) | Federal official notices, appointments, regulations, and acts | D | SEARCH,DL | Portuguese search, sections, and corrigenda require care |
| 15.022 | T1 | Mexico | 15 | [Diario Oficial de la Federación](https://www.dof.gob.mx/) | Federal laws, regulations, decrees, standards, and official notices | D | SEARCH,DL | Publication and effective dates may differ; Spanish text controls |
| 15.023 | T1 | Global | 15 | [UN Treaty Collection](https://treaties.un.org/) | Multilateral treaty text and participation status | C | SEARCH,DL | Treaty participation does not itself establish domestic implementation |

### 8.16 Digital assets and public-ledger research

Public-ledger facts and address attribution are different evidence classes. Transactions, blocks, contract calls, and balances can be reproduced from the ledger. Explorer name tags, scam reports, clustering, and claims that an address belongs to a service or person are attributions and require separate corroboration.

| ID | Tier | J/C | D | Official source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 16.001 | T1 | Bitcoin network | 16 | [Bitcoin Core RPC documentation](https://developer.bitcoin.org/reference/rpc/) | Reproduce block, transaction, UTXO, and node observations from a validating node | C | API | No central issuer; node completeness, chain tip, and reorg state must be recorded |
| 16.002 | T1 | Ethereum network | 16 | [Ethereum JSON-RPC documentation](https://ethereum.org/developers/docs/apis/json-rpc/) | Query blocks, receipts, logs, transactions, and contract state | C | API | Archive history and trace methods depend on node/provider configuration |
| 16.003 | T1 | Solana network | 16 | [Solana RPC methods](https://solana.com/docs/rpc) | Query slots, signatures, transactions, accounts, and token data | C | API | Commitment level, archival coverage, and parsed formats matter |
| 16.004 | T1 | Tron network | 16 | [TRON FullNode API documentation](https://developers.tron.network/reference/full-node-api-overview) | Query blocks, transactions, contracts, and TRC token activity | C | API | Provider retention, confirmation state, and token-decimal handling matter |
| 16.005 | T2 | Ethereum/EVM | 16 | [Etherscan](https://etherscan.io/) | Convenient reproduction of transactions, logs, tokens, contracts, and verified source code | C | SEARCH,API | Ledger fields are reproducible; proprietary name tags are T3 and pagination can truncate |
| 16.006 | T2 | Bitcoin | 16 | [mempool.space](https://mempool.space/) | Bitcoin blocks, transactions, fees, and UTXO inspection | C | SEARCH,API | Explorer interface is not the ledger; mempool state is volatile |
| 16.007 | T2 | Multiple chains | 16 | [Blockchair](https://blockchair.com/) | Multi-chain transaction and address discovery | C | SEARCH,API | Derived analytics and labels need independent verification |
| 16.008 | T1 | United States | 16 | [OFAC Sanctions List Service](https://ofac.treasury.gov/sanctions-list-service) | Official digital-currency addresses included in sanctions records | EV | SEARCH,DL | Address listing scope and network must be exact; ownership rules extend beyond addresses |
| 16.009 | T1 | United States | 16 | [FinCEN convertible virtual currency guidance](https://www.fincen.gov/resources/statutes-regulations/guidance) | BSA classification and guidance for virtual-currency activity | EV | SEARCH,DL | Locate the exact guidance and later rule; facts determine regulatory category |
| 16.010 | T1 | United States | 16 | [SEC crypto assets and cyber enforcement](https://www.sec.gov/enforcement-litigation/cybersecurity-and-cryptocurrency) | SEC cases, investor materials, and crypto-related enforcement | EV | WEB,DL | Complaint or settlement is not necessarily an adjudicated legal conclusion |
| 16.011 | T1 | United States | 16 | [CFTC digital assets](https://www.cftc.gov/digitalassets/index.htm) | Derivatives regulator guidance, customer advisories, and cases | EV | WEB | Spot-market and commodity jurisdiction questions are fact-specific |
| 16.012 | T1 | United States/New York | 16 | [NYDFS virtual-currency businesses](https://www.dfs.ny.gov/virtual_currency_businesses) | BitLicensees, trust companies, conditional licenses, and virtual-currency guidance | C | WEB | Authorization type and permitted activities differ |
| 16.013 | T1 | Global | 16 | [FATF virtual-assets resources](https://www.fatf-gafi.org/en/topics/virtual-assets.html) | FATF standards, targeted updates, and implementation analysis | P | WEB,DL | International standard; national implementation controls |
| 16.014 | T1 | European Union | 16 | [ESMA MiCA register](https://www.esma.europa.eu/publications-and-data/databases-and-registers) | Crypto-asset white papers, authorized providers, and non-compliant entities | C | SEARCH,DL | Register build-out and national transitional periods affect coverage |
| 16.015 | T1 | European Union | 16 | [EUR-Lex Markets in Crypto-assets Regulation](https://eur-lex.europa.eu/eli/reg/2023/1114/oj) | Controlling MiCA text and application dates | H/P | WEB,DL | Delegated acts, technical standards, and transition provisions also apply |
| 16.016 | T1 | United Kingdom | 16 | [FCA cryptoasset register](https://register.fca.org.uk/s/search?predefined=CA) | UK AML-registered cryptoasset firms | C | SEARCH | AML registration is not product approval or full prudential authorization |
| 16.017 | T1 | Australia | 16 | [AUSTRAC digital currency exchange register](https://www.austrac.gov.au/business/industry-specific-guidance/digital-currency-exchange-providers) | Registration framework and public DCE-register access | C | WEB,SEARCH | Registration is not endorsement and may not cover offshore activity |
| 16.018 | T1 | Canada | 16 | [FINTRAC Money Services Business Registry](https://fintrac-canafe.canada.ca/msb-esm/reg-eng) | Registered domestic and foreign MSBs including virtual-currency activity | C | SEARCH | Registration is not licensing or endorsement; activity scope is self-reported |
| 16.019 | T1 | Japan | 16 | [FSA crypto-asset exchange service providers](https://www.fsa.go.jp/en/regulated/licensed/index.html) | Registered Japanese crypto exchanges and relevant lists | C | WEB,DL | Category-specific lists may be Japanese-only; confirm current action status |
| 16.020 | T1 | Hong Kong | 16 | [SFC virtual asset trading platform lists](https://www.sfc.hk/en/Welcome-to-the-Fintech-Contact-Point/Virtual-assets/Virtual-asset-trading-platforms-operators) | Licensed, applicant, closing, and deemed-license VATP information | C | WEB | Applicant/deemed status is not full licensing; capture category and date |
| 16.021 | T1 | Singapore | 16 | [MAS Financial Institutions Directory](https://eservices.mas.gov.sg/fid/institution) | Licensed payment institutions and digital-payment-token activities | C | SEARCH | Exempt, standard, and major payment-institution status differ |
| 16.022 | T1 | Dubai | 16 | [VARA public register](https://www.vara.ae/en/licenses-and-register/public-register/) | Licensed virtual-asset service providers and activities | C | SEARCH | Emirate/free-zone scope and license stage matter |
| 16.023 | T1 | Abu Dhabi Global Market | 16 | [FSRA public register](https://www.adgm.com/public-registers/fsra) | Authorized persons and regulated activities including virtual assets | C | SEARCH | ADGM scope only; permission conditions must be read |
| 16.024 | T1 | Global/securities regulators | 16 | [IOSCO crypto and digital-assets publications](https://www.iosco.org/publications/?subsection=public_reports) | International securities-regulatory policy and consultation materials | P | SEARCH,DL | Recommendations are not national law or firm-level authorization |

### 8.17 ESG, environment, labor, and human rights

| ID | Tier | J/C | D | Official source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 17.001 | T1 | Global/UN | 17 | [OHCHR treaty body database](https://tbinternet.ohchr.org/) | Ratification, reporting, concluding observations, and treaty-body documents | C | SEARCH,DL | Treaty-body findings have specific mandates and are not criminal judgments |
| 17.002 | T1 | Global/UN | 17 | [UN Guiding Principles on Business and Human Rights](https://www.ohchr.org/sites/default/files/documents/publications/guidingprinciplesbusinesshr_en.pdf) | Authoritative UN framework for state duty, corporate responsibility, and remedy | H | DL | Principles are not a company-rating system or standalone binding treaty |
| 17.003 | T1 | Global/ILO | 17 | [ILO NORMLEX](https://normlex.ilo.org/) | Labor standards, ratifications, supervisory observations, and cases | C | SEARCH | Comments and cases require procedural-status interpretation |
| 17.004 | T1 | Global/ILO | 17 | [ILOSTAT](https://ilostat.ilo.org/data/) | Labor-force, wages, occupational safety, informality, and child-labor data | A/P | SEARCH,API,DL | Estimates, definitions, and national coverage vary |
| 17.005 | T1 | United States/global | 17 | [US Department of Labor child labor and forced labor reports](https://www.dol.gov/agencies/ilab/reports/child-labor/list-of-goods) | Goods and countries linked to child/forced labor evidence | P | WEB,DL | Country/good-level finding is not proof about every company or shipment |
| 17.006 | T1 | United States/global | 17 | [State Department Trafficking in Persons Report](https://www.state.gov/trafficking-in-persons-report/) | Country anti-trafficking assessment and tier placement | A | WEB,DL | Country-level assessment; not an entity or individual finding |
| 17.007 | T1 | United States | 17 | [CBP UFLPA Entity List](https://www.dhs.gov/uflpa-entity-list) | Entities and facilities named under forced-labor import enforcement | EV | WEB | List categories and rebuttable-presumption scope must be read exactly |
| 17.008 | T1 | United States | 17 | [EPA ECHO](https://echo.epa.gov/) | Facility permits, inspections, compliance, violations, and enforcement | C | SEARCH,API,DL | Integrated data can lag and includes alleged/non-final violations |
| 17.009 | T1 | United States | 17 | [EPA cases and settlements](https://www.epa.gov/enforcement/cases-and-settlements) | Environmental case documents, settlements, and outcomes | EV | SEARCH | Agency summary should be tied to filed order or settlement |
| 17.010 | T1 | European Union | 17 | [European Industrial Emissions Portal](https://industry.eea.europa.eu/) | Facility emissions, pollutant releases, transfers, and regulatory context | A | SEARCH,DL | Operator-reported data, thresholds, and reporting years vary |
| 17.011 | T1 | European Union | 17 | [Corporate Sustainability Reporting Directive](https://eur-lex.europa.eu/eli/dir/2022/2464/oj) | Controlling EU sustainability-reporting directive | H/P | WEB,DL | National transposition, scope, phase-in, and later amendments matter |
| 17.012 | T1 | European Union | 17 | [Sustainable Finance Disclosure Regulation](https://eur-lex.europa.eu/eli/reg/2019/2088/oj) | EU financial-product/entity sustainability-disclosure rules | H/P | WEB,DL | Delegated rules and interpretations determine detailed obligations |
| 17.013 | T1 | United Kingdom | 17 | [Modern slavery statement registry](https://modern-slavery-statement-registry.service.gov.uk/) | Organization-submitted modern slavery statements | C | SEARCH | Submission is self-reported; absence and content do not alone prove noncompliance |
| 17.014 | T1 | Australia | 17 | [Modern Slavery Statements Register](https://modernslaveryregister.gov.au/landing) | Published entity statements under Australian law | C | SEARCH,DL | Self-reported statements; entity relationships and reporting periods matter |
| 17.015 | T1 | Global/OECD | 17 | [OECD National Contact Point cases](https://mneguidelines.oecd.org/database/) | Specific instances under OECD responsible-business-conduct guidelines | EV | SEARCH | NCP process is non-judicial; acceptance is not a finding of breach |
| 17.016 | T1 | Global/IFC | 17 | [IFC Performance Standards](https://www.ifc.org/en/insights-reports/2012/ifc-performance-standards) | Environmental and social risk-management standards for IFC contexts | P | WEB,DL | Applicability depends on financing agreement and project context |
| 17.017 | T1 | Global/World Bank | 17 | [World Bank ESG Data](https://esgdata.worldbank.org/) | Sovereign environmental, social, and governance indicators | A/P | SEARCH,DL | Country-level indicators do not rate a company and may lag |
| 17.018 | T2 | Global | 17 | [UN Global Compact participant search](https://unglobalcompact.org/what-is-gc/participants) | Participant status and public communications on progress | C | SEARCH | Voluntary/self-reported participation; not certification or performance proof |
| 17.019 | T1 | Global/UN | 17 | [UN Human Rights Council Universal Periodic Review](https://www.ohchr.org/en/hr-bodies/upr/upr-main) | State human-rights review documents and recommendations | P | SEARCH,DL | State-level peer review; recommendations and acceptance status differ |
| 17.020 | T1 | European Union | 17 | [European Environment Agency data](https://www.eea.europa.eu/en/datahub) | European environment, climate, pollution, and biodiversity datasets | P | SEARCH,API,DL | National data harmonization, modelled values, and reporting lag vary |

### 8.18 Adverse media, archives, and content verification

This domain is primarily a discovery and corroboration layer. For conduct, retrieve the underlying regulator, court, filing, police, procurement, or gazette record from domains 01, 05, 07, 08, 10, 11, or 12. Respect copyright: cite and summarize; do not reproduce full articles or paywalled text.

| ID | Tier | J/C | D | Source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 18.001 | T2 | Global | 18 | [Reuters](https://www.reuters.com/) | Timely accountable reporting and discovery of underlying records | C | SEARCH | Paywall/access can vary; follow citations and independently resolve identity |
| 18.002 | T2 | Global | 18 | [Associated Press](https://apnews.com/) | Accountable international and national reporting | C | SEARCH | Reporting is secondary to the underlying record; syndicated copies are one lineage |
| 18.003 | T2 | Global | 18 | [BBC News](https://www.bbc.com/news) | International reporting, explainers, and archives | C | SEARCH | Not authoritative for legal status; retrieve source documents |
| 18.004 | T2 | Global | 18 | [International Consortium of Investigative Journalists](https://www.icij.org/investigations/) | Sourced cross-border investigations and dataset leads | P | SEARCH | Leaked/compiled material requires identity, legality, and primary-record corroboration |
| 18.005 | T2 | Global | 18 | [OCCRP investigations](https://www.occrp.org/en/investigations) | Organized-crime and corruption investigations with document leads | C | SEARCH | Treat allegations and leaked records according to provenance and legal status |
| 18.006 | T2 | Global | 18 | [Bellingcat](https://www.bellingcat.com/) | Transparent open-source investigations and verification methods | P | SEARCH | Method quality is article-specific; reproduce critical geolocation/chronology steps |
| 18.007 | T2 | Global | 18 | [GDELT Project](https://www.gdeltproject.org/) | Large-scale news discovery, event indexing, and trend scans | C | API,DL | Machine-coded and duplicate-prone; not evidence of an event by itself |
| 18.008 | T3 | Global | 18 | [Google Fact Check Explorer](https://toolbox.google.com/factcheck/explorer) | Discovery of published fact checks and claim variants | C | SEARCH | Index is not the verifier; tier and inspect the underlying fact-check organization |
| 18.009 | T2 | Global | 18 | [International Fact-Checking Network signatories](https://ifcncodeofprinciples.poynter.org/signatories) | Identify organizations assessed against IFCN transparency principles | P | SEARCH | Signatory status does not make each article correct or primary evidence |
| 18.010 | T2 | Global/web history | 18 | [Internet Archive Wayback Machine](https://web.archive.org/) | Historical captures of public web pages | C | SEARCH,API | Capture may be incomplete; archive proves display, not truth; terms/privacy apply |
| 18.011 | T2 | Legal/academic web | 18 | [Perma.cc](https://perma.cc/) | Durable captures created by participating institutions and users | C | SEARCH | Capture creator and underlying page authority must be established |
| 18.012 | T1 | Scholarly metadata | 18 | [Crossref Metadata Search](https://search.crossref.org/) | DOI, publisher, title, author, correction, and relation metadata | C | SEARCH,API | Metadata can be depositor-supplied or incomplete; read the work itself |
| 18.013 | T1 | Biomedical literature | 18 | [PubMed](https://pubmed.ncbi.nlm.nih.gov/) | Curated biomedical citations, abstracts, publication types, and corrections | C | SEARCH,API | Indexing is not quality endorsement; abstracts are not full evidence |
| 18.014 | T1 | Biomedical literature | 18 | [Europe PMC](https://europepmc.org/) | Biomedical citations, grants, full-text links, and retraction/correction metadata | C | SEARCH,API | Repository mixes versions; check publisher record and retraction status |
| 18.015 | T2 | Scholarly integrity | 18 | [Retraction Watch Database](https://retractionwatch.com/retraction-watch-database-user-guide/) | Discovery of retractions, expressions of concern, and corrections | C | SEARCH | Retrieve publisher notice and DOI record as controlling evidence |
| 18.016 | T2 | Media authenticity | 18 | [Content Credentials Verify](https://contentcredentials.org/verify) | Inspect C2PA provenance assertions in supported media | C | WEB | Missing credentials do not prove manipulation; credentials do not prove depicted claim |
| 18.017 | T1 | United States/government web | 18 | [US Government Web Archive](https://www.loc.gov/web-archives/) | Curated historical captures of government and public-policy sites | P | SEARCH | Collection is selective and capture frequency varies |
| 18.018 | T1 | United Kingdom/government web | 18 | [UK Government Web Archive](https://www.nationalarchives.gov.uk/webarchive/) | Historical UK central-government websites and social records | P | SEARCH | Interactive content and databases may not be captured fully |

### 8.19 Open data, geospatial, maritime, and aviation

| ID | Tier | J/C | D | Source | Use | Freq | Access | Limits |
|---|---|---|---|---|---|---|---|---|
| 19.001 | T1 | United States | 19 | [Data.gov](https://data.gov/) | Discovery of US federal, state, and local open datasets | C | SEARCH,API,DL | Catalog entry is not the data producer; cite the publishing agency/dataset |
| 19.002 | T1 | European Union | 19 | [data.europa.eu](https://data.europa.eu/) | EU institution and member-state open-data catalog | C | SEARCH,API,DL | Dataset authority, license, update cycle, and national coverage vary |
| 19.003 | T1 | United Kingdom | 19 | [data.gov.uk](https://www.data.gov.uk/) | UK central and local government open-data catalog | C | SEARCH,API,DL | Catalog metadata may point to stale or externally hosted data |
| 19.004 | T1 | Canada | 19 | [Open Government Portal](https://open.canada.ca/en/open-data) | Canadian federal datasets, maps, and information resources | C | SEARCH,API,DL | Departmental update and licensing details vary |
| 19.005 | T1 | Australia | 19 | [data.gov.au](https://data.gov.au/) | Australian government open-data catalog | C | SEARCH,API,DL | Publisher, jurisdiction, format, and freshness vary |
| 19.006 | T1 | New Zealand | 19 | [data.govt.nz](https://www.data.govt.nz/) | New Zealand public-data catalog and guidance | C | SEARCH,API,DL | Catalog may link to agency-hosted data with separate terms |
| 19.007 | T1 | Singapore | 19 | [data.gov.sg](https://data.gov.sg/) | Singapore government datasets and APIs | C | SEARCH,API,DL | API limits, geographic granularity, and revisions vary |
| 19.008 | T1 | Hong Kong | 19 | [DATA.GOV.HK](https://data.gov.hk/en/) | Hong Kong public datasets and APIs | C | SEARCH,API,DL | Departmental licensing, encoding, and cadence vary |
| 19.009 | T1 | India | 19 | [Open Government Data Platform India](https://www.data.gov.in/) | Indian ministry datasets, catalogs, and APIs | C | SEARCH,API,DL | Publisher, update cadence, and state-level coverage vary |
| 19.010 | T1 | Global/World Bank | 19 | [World Bank Data Catalog](https://datacatalog.worldbank.org/search) | Development datasets, microdata references, geospatial data, and metadata | C | SEARCH,API,DL | Dataset-specific licenses and access restrictions apply |
| 19.011 | T1 | Global/humanitarian | 19 | [Humanitarian Data Exchange](https://data.humdata.org/) | Crisis, population, infrastructure, administrative-boundary, and needs datasets | C | SEARCH,API,DL | Mixed publishers and sensitivity tiers; qualify each underlying dataset |
| 19.012 | T3 | Global | 19 | [OpenStreetMap](https://www.openstreetmap.org/) | Community geographic features and basemap context | C | SEARCH,API,DL | User-contributed, uneven coverage, and not authoritative for legal boundaries |
| 19.013 | T1 | United States/global | 19 | [USGS EarthExplorer](https://earthexplorer.usgs.gov/) | Satellite, aerial, elevation, land, and historical imagery discovery | P | SEARCH,REG,DL | Resolution, cloud cover, license, processing level, and acquisition time matter |
| 19.014 | T1 | Global | 19 | [NASA Earthdata Search](https://search.earthdata.nasa.gov/) | Earth-observation products, imagery, climate, atmosphere, and ocean data | C | SEARCH,REG,API,DL | Product algorithms, processing level, latency, and uncertainty vary |
| 19.015 | T1 | European Union/global | 19 | [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/) | Sentinel imagery and Copernicus Earth-observation products | C | SEARCH,REG,API,DL | Processing level, revisit timing, cloud cover, and terms require review |
| 19.016 | T1 | United States/global | 19 | [NOAA data access](https://www.noaa.gov/information-technology/open-data-dissemination) | Weather, climate, ocean, fisheries, and environmental datasets | C | API,DL | Product-specific quality flags, stations, models, and revisions matter |
| 19.017 | T1 | Global/maritime | 19 | [IMO GISIS](https://gisis.imo.org/Public/Default.aspx) | Ship/company particulars, casualties, security, port facilities, and IMO datasets | C | SEARCH,REG | Modules and public fields vary; identity and ownership may be historical |
| 19.018 | T1 | Global/maritime | 19 | [Equasis](https://www.equasis.org/) | Ship identity, flag, class, management, inspection, and safety data from public authorities | C | SEARCH,REG | Account required; sources and update dates differ by field |
| 19.019 | T1 | United States/maritime | 19 | [US Coast Guard Port State Information Exchange](https://cgmix.uscg.mil/PSIX/) | Vessel particulars, inspections, deficiencies, and detentions | C | SEARCH | USCG coverage; absence does not establish global compliance |
| 19.020 | T1 | United States/aviation | 19 | [FAA Aircraft Registry](https://registry.faa.gov/aircraftinquiry/) | US civil aircraft registration, N-number, owner, and status | C | SEARCH,DL | Registered owner may be trustee or lessor; operators and beneficial owners differ |
| 19.021 | T1 | Global/trade geography | 19 | [UN/LOCODE](https://unece.org/trade/cefact/unlocode-code-list-country-and-territory) | Standard location codes for ports, terminals, and trade locations | P | SEARCH,DL | Code does not prove facility operation, ownership, or current status |
| 19.022 | T1 | United States/geospatial | 19 | [National Map](https://www.usgs.gov/programs/national-geospatial-program/national-map) | Authoritative US elevation, hydrography, boundaries, structures, and map data | P | SEARCH,API,DL | Dataset dates, scales, and boundary authority vary |
| 19.023 | T1 | European Union/geospatial | 19 | [INSPIRE Geoportal](https://inspire-geoportal.ec.europa.eu/) | Discovery of member-state spatial datasets and services | C | SEARCH,API | Member-state publisher and dataset metadata control quality |
| 19.024 | T2 | Global/geospatial | 19 | [Natural Earth](https://www.naturalearthdata.com/) | Public-domain generalized cultural and physical map layers | P | DL | Designed for small-scale cartography, not legal boundaries or precise location |
| 19.025 | T3 | Global/geographic names | 19 | [GeoNames](https://www.geonames.org/) | Geographic-name, alternate-name, and coordinate discovery | C | SEARCH,API,DL | Community-maintained; verify legal names and coordinates with national authority |

## 9. Workflow source packs

Use these packs as minimum starting points. Add the subject's jurisdictions, sector, legal form, and time-specific sources.

| Workflow | Mandatory starting set | Required challenge/fallback |
|---|---|---|
| Current sanctions screen | 01.001 plus relevant national sources in 01; legal instrument and exact retrieval time | Program scope, ownership/control rules, aliases/transliteration, delisting/change check; aggregator only for discovery |
| Cross-border company profile | Registry of incorporation in 04, 04.001, applicable sources in 05/06, filed documents | Former names, parents/subsidiaries, dissolution/insolvency, missing ownership layers, registry-verification limitation |
| Beneficial-ownership chain | National registry/filing for every edge, securities ownership filings, LEI relationships | Voting/control rights, nominees/trusts, effective dates, circular paths, unknown percentages; leaks only as leads |
| PEP assessment | Relevant 03 sources plus national gazette/appointment source in 15 | Role prominence, start/end dates, former status, separate evidence for family/associate relationship |
| Adverse media review | Relevant authority/court sources in 07/10/11/12, then 18.001–18.007 | Wrong-party, victim/witness role, later resolution, correction/retraction, source-lineage independence |
| Jurisdiction-risk profile | 02.002–02.012, 10.001–10.005, relevant 14 series | Edition/date, missing data, hard designations separate from composite indicators, methodology sensitivity |
| Regulatory-intelligence monitor | Issuing regulator in 02/05/06, controlling law/gazette in 15 | Proposal versus final, publication/effective/compliance dates, correction, litigation, supersession |
| Enforcement history | Authority action source in 07, court docket/judgment, participant register in 05/06 | Allegation versus resolution, appeal/stay/termination, related but distinct entities, current license status |
| Procurement integrity | Award sources in 08 plus debarments in 01 and registries in 04 | Amendments, lots, subcontractors, common identifiers, procurement challenge/cancellation, one-lineage duplicates |
| Trade-control review | 01, 09.005–09.013, current legal text in 15 | Classification, origin, destination/end use/end user, licenses/exceptions, effective date; specialist decision |
| Cyber threat brief | 11.001–11.003 and affected vendor advisory | CVE/CPE/version accuracy, exploitation evidence, patch status, attribution confidence, stale indicators |
| Public-ledger investigation | 16.001–16.007, sanctions source 16.008, relevant license source 16.012–16.023 | Complete pagination, chain/asset separation, reorg/confirmation state, spam/dust, attribution firewall |
| ESG/human-rights review | Applicable 17 sources plus issuer filings and enforcement sources | Self-reporting, scope/period, value-chain boundary, country-to-entity inference, grievance or outcome evidence |
| Geospatial or asset verification | Relevant 19 source plus registry/filing and time-specific imagery | Capture time, coordinate system, resolution, legal-boundary limits, registered owner versus operator/control |

## 10. Registry maintenance controls

### 10.1 Review cadence

| Source class | Minimum registry review | Use-time validation |
|---|---|---|
| Sanctions, restrictions, terrorist lists, export lists | Monthly and after known issuer change | Mandatory immediately before the decision |
| Licenses and regulated-firm registers | Quarterly | Mandatory for current-status claims |
| Laws, regulations, gazettes, court/enforcement sources | Quarterly link review | Mandatory for effective date, status, appeal, and supersession |
| Corporate registries | Semiannual link/access review | Mandatory for current identity/status/ownership claims |
| Statistical APIs and datasets | Annual schema/method review | Capture series vintage and latest revision |
| News, archives, open-data, and geospatial catalogs | Annual | Validate underlying publisher, license, and capture date |
| Blockchain explorers and APIs | Quarterly interface review | Record node/explorer, chain tip, parameters, and completeness |

### 10.2 Change log schema

```yaml
change_id: CHG-YYYYMMDD-NNN
registry_id: "01.001"
checked_at: YYYY-MM-DDThh:mm:ssZ
checker: role_or_initials
status: active|moved|restricted|retired|replaced|temporarily_unavailable
old_url: null
new_url: null
access_change: null
scope_change: null
tier_change: null
replacement_registry_id: null
evidence: official migration or issuer notice URL
notes: concise reason
```

Never silently repoint an entry to a third-party mirror. Preserve the old URL in the change log, identify the official successor, and review any change to scope, fields, cadence, terms, or legal effect.

### 10.3 Link and content checks

For each maintenance cycle:

1. Resolve the URL from the listed parent domain.
2. Record HTTP/access outcome without treating anti-bot denial as source retirement.
3. Confirm page title, publisher, purpose, and successor notice.
4. Check whether search, download, API, registration, fee, or license terms changed.
5. Check data fields, coverage, format, update cadence, and version history.
6. Re-test one representative retrieval without collecting unnecessary personal data.
7. Update limitations before adding coverage claims.
8. Independently review changes to Tier 1 sanctions, legal, court, or licensing sources.

## 11. Researcher handoff checklist

- [ ] The decision question, subject, jurisdictions, period, and as-of timestamp are fixed.
- [ ] Each proposition was mapped to a registry domain and controlling jurisdiction.
- [ ] Mandatory T1 sources were searched before aggregators.
- [ ] Exact records, not search-result pages or snippets, were captured.
- [ ] Names, identifiers, aliases, languages, and temporal variants were tested.
- [ ] Identity was resolved before adverse information was attached.
- [ ] Source tier, lineage, access, cadence, and limitations were recorded.
- [ ] List/dataset/filing version and retrieval timestamp were captured.
- [ ] Later outcomes, appeals, corrections, amendments, and delistings were searched.
- [ ] Negative results are bounded to the documented sources and queries.
- [ ] Quotes are minimal and copyright/licensing conditions are respected.
- [ ] No sanctioned-person, customer, victim, complainant, or bulk personal data is embedded in a public artifact.
- [ ] Material findings passed the human gates in `01-evidence-research-standard.md`.

## 12. Known limitations

- This is a broad official-source baseline, not an exhaustive list of every national, state, provincial, municipal, tribal, sectoral, or court registry.
- Some official services require an account, fee, local identifier, local language, CAPTCHA, accepted terms, or in-jurisdiction access.
- Registry records may be declarative rather than verified; public beneficial-ownership access is restricted in many jurisdictions.
- Courts differ sharply in publication, sealing, redaction, docket access, and historical digitization.
- Sanctions and license status can change at any time. A cached or archived copy is not a current screen.
- Official statistics are revised and may not be comparable across definitions, vintages, or countries.
- Media and investigative sources are secondary even when highly reputable; underlying records should carry the finding.
- Public-ledger visibility does not by itself establish real-world identity, intent, beneficial ownership, or illegality.
- A missing result can reflect spelling, language, coverage, access, indexing, or timing. It is not proof of absence.

Maintain the register as a controlled index. The value is not the number of links; it is the disciplined path from the right source to a dated, identity-resolved, reproducible claim.
