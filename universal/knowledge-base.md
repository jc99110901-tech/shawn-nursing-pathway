# SNP Skill Knowledge Base

This file is a platform-neutral knowledge base for AI agents. It should be used with `system-prompt.md`, `workflow.md`, `output-templates.md`, and `safety-boundary.md`.

## Modular Suite

`SNP Skill` is the user-facing main router. Its stable technical package name is `shawn-nursing-pathway`.

Focused modules:

| Public name | Purpose |
|---|---|
| SNP Fit | Nursing-fit and work-reality screening |
| SNP Explore | Domestic and overseas pathway shortlisting |
| SNP Plan | Chosen-path milestones and one minimum next task |
| SNP Learn | Adaptive nursing knowledge and professional English learning |
| SNP Career | Roles, work settings, transitions, and salary reality |
| SNP Interview | Job-description, evidence, application, and interview preparation |
| SNP Verify | Current official information and claim verification |

Platforms without native multi-Skill routing should use the combined Lite or Full distribution and run the same internal modules.

## User Segments

- Gaokao student: deciding whether nursing should appear in volunteer planning.
- Parent or guardian: concerned with stability, cost, city, risk, and long-term path.
- Nursing student: considering graduate study, domestic employment, or overseas preparation.
- Domestic nurse: considering recognition, exams, overseas work, or career transition.
- Non-nursing career changer: considering nursing, caregiving, or healthcare-related routes.
- Provider-claim checker: wants to verify school, agency, cooperation, employment, visa, or migration claims.
- Conflicted decision user: wants several distinct perspectives on a family, study, career, or overseas-pathway tradeoff.
- Chosen-path user: has a provisional direction but needs the next evidence-producing task.
- Learner: wants nursing knowledge, professional English, or pathway literacy one step at a time.
- Career-transition user: wants to compare bedside and non-bedside roles, work settings, and pay.
- Job candidate: has a role, vacancy, application, or interview and needs truthful evidence mapping.

## Multi-Perspective Review

Use 3-5 perspectives only when the user asks for them or confirms the proposed roles:

- nursing clinical reality
- education and degree pathway
- licensing and official-policy verification
- family budget and opportunity cost
- career development and employer evidence
- overseas life and family fit
- student autonomy and family communication
- irreversible-risk review

Every role must own one distinct decision dimension and receive the same evidence brief. If independent Agents are unavailable, disclose that the result is a single-model simulation. The moderator preserves disagreement and identifies decision variables; it does not count votes or make the final decision.

## Information Freshness

Dynamic facts include statistics, policy, fees, programmes, licensing rules, exams, visas, migration rules, named institutions, active jobs, hiring requirements, salaries, and market claims.

Before using them:

1. Search current official sources.
2. Check the same-series official listing or archive before saying "latest".
3. Record search date, effective/data period, publication/update date, and freshness status.
4. Say explicitly when no newer official source or dated active vacancy was found.
5. Do not use a crawl date, undated marketing page, or third-party summary as a current official fact.

## Nursing Fit Dimensions

Screen nursing fit through:

- tolerance for high-intensity hands-on practice
- acceptance of night shifts, rotation, patient contact, and clinical pressure
- ability to face illness, blood, bodily care, grief, conflict, and family pressure
- preference for stable but stressful work
- willingness to learn professional communication and follow strict procedures
- family budget and time tolerance
- overseas life acceptance if an overseas route is involved

Output only possible advantages, main risks, and questions to verify.

## Salary and Compensation Reality

When the user's real concern is what a specific job or completed path pays, include a compact salary reality check.

Required scope:

- country, region, and city
- exact occupation and license level
- public, private, international, aged-care, community, agency, or other setting
- entry, experienced, specialist, or management level
- full-time, part-time, casual, contract, or agency work
- currency, hourly/monthly/annual period, and gross/net basis
- whether the figure is a minimum scale, median, mean, percentile range, active-vacancy range, base pay, or total cash earnings

Prefer current official occupational statistics, public pay scales, collective agreements, and dated official employer vacancies. Separate base pay from night, weekend, overtime, bonuses, and allowances.

An average is not a personal offer. A pay scale is not proof that every employer pays the same. A vacancy is evidence for one vacancy, not the entire market. If exact current evidence cannot be verified, say so and use a broader figure only as labelled background.

## Chosen-Path Planning

After the user selects a provisional direction:

1. map eligibility, evidence, language, application/exam, registration, employment, and visa/residence stages as relevant
2. mark each stage `已完成`, `正在验证`, `未开始`, `不适用`, or `被阻塞`
3. identify the largest current uncertainty
4. give one reversible 15-60 minute task with one deliverable and completion condition
5. update a portable `SNP 进度卡`

The first task should not be payment, resignation, application submission, or another irreversible action. Completing a task can reveal that the route should be paused.

## Adaptive Learning

Learning tracks can include:

- nursing foundations and professional concepts
- clinical communication and nursing English
- English for a named role or interview
- licensing and pathway literacy
- documentation or structured handover practice
- role-transition knowledge

Every lesson has one observable objective, one baseline check, the minimum input, one worked example, one practice task, feedback on the largest gap, and an updated progress card.

This support does not replace accredited nursing education, clinical supervision, or patient-specific medical advice. Do not promise language-test scores, licensure, employment, or migration.

## Career and Job Readiness

Role exploration should compare:

- normal work and patient-contact level
- must-have and preferred entry evidence
- transferable nursing evidence
- gaps and transition cost
- schedule, travel, target, on-call, and accountability reality
- current salary evidence and its metric
- one reversible role experiment

After a target role or current vacancy is selected:

1. verify that the job information is current
2. split requirements into must-have, preferred, and unclear
3. map each item to proven, partial, absent, or not-applicable evidence
4. practise role-specific interview questions
5. prepare questions about scope, supervision, schedule, pay, training, and official sponsorship wording

Never invent experience, metrics, responsibilities, certificates, language scores, or clinical cases.

## Domestic China Pathways

### Junior-College Nursing

Possible fit:

- families prioritizing vocational entry
- lower-score users who still accept clinical work
- users considering later degree upgrading

Risks:

- not an easy low-score shortcut
- degree upgrading, internship, license exam, and employment rules must be checked locally
- school brochure and physical restrictions must be verified

### Bachelor Nursing

Possible fit:

- users who can reach bachelor-level choices
- families wanting a stronger domestic education base
- students considering hospital work, graduate study, or later overseas preparation

Risks:

- bachelor degree does not remove work pressure
- school city, clinical resources, tuition, and admission restrictions matter
- graduation, license exam, and practice registration are separate

### Sino-Foreign or Related Programs

Possible fit:

- higher-budget families
- users wanting English exposure or a bridge to later overseas study

Risks:

- Sino-foreign does not mean guaranteed transfer, foreign license, employment, visa, or immigration
- partner school, degree-award arrangement, fee, exit rules, refund rules, and license relevance must be verified

## Philippines and Cebu

Use Cebu as one investigation direction, not a universal answer.

Check:

- school and program recognition through CHED or official school/regulator sources
- BS Nursing versus Doctor of Dental Medicine difference
- PRC licensure rules and foreign-student implications
- student visa, tuition, refund, housing, clinical practice, and international-student charges
- CSCSE or third-country credential use if the user plans to return to China or move onward
- any agent commission, cooperation, or employment referral relationship

Risk:

- studying in the Philippines does not guarantee US RN, employment, visa, or immigration outcomes.

## Japan Nursing and Caregiving

First split Japan questions into:

- foreign nurse qualification holder wants to become a nurse in Japan
- gaokao student or ordinary family asks about "Japan nursing"
- Japanese caregiving or SSW nursing care

Do not answer "Japan nursing" as one route. Japanese nurse, nursing study, certified care work, caregiving, and SSW nursing care are different directions.

### Japan Nurse Route for Foreign Nurses

Use when a Chinese nurse, overseas nurse, or nursing graduate asks whether they can become a nurse in Japan.

Ask for:

- foreign nursing school, degree, graduation year, transcript, syllabus, clinical practice, and curriculum evidence
- original country or region nurse license status, not only graduation
- current Japanese level and whether MHLW-level document work in Japanese is realistic
- translations, notarisation, name/date consistency, and whether documents can be traced to official sources
- final goal: exam eligibility, Japanese nurse license, employment, visa, long-term planning, or only feasibility screening

Core layers:

- Education: foreign nursing education is reviewed against Japan-side criteria.
- Qualification: foreign nurse license status is a central review point.
- Exam eligibility and license: MHLW recognition is needed before sitting Japan's nurse national examination; exam and later licensing steps are separate.
- Employment and visa: exam eligibility or license progress is not an employer, work contract, Certificate of Eligibility, visa, or residence status.
- Long-term planning: long-term residence requires separate immigration and employment checks.

### Japan Nursing Study for Ordinary Families

Use when a family asks whether a student should study nursing in Japan, use Japan as a lower-cost path, or compare Japan with domestic nursing.

Ask first whether the user means nursing school, Japanese nurse license, caregiving, SSW nursing care, language school, or general study abroad.

Risks:

- school admission or language study is only the education layer
- graduation does not automatically create nurse license, work status, visa, or long-term residence
- if the user has no nursing background, start with fit, language, budget, and work-scene acceptance before discussing schools

### Japan Caregiving or SSW Nursing Care

Use when the user asks about kaigo, caregiving, care worker, nursing-care work, SSW nursing care, or "Japan nursing jobs" that sound like care work.

Key points:

- SSW nursing care is not Japanese nurse licensure.
- Nursing care under SSW involves direct care and related support work, not a nurse-license route.
- Skill and language tests are separate from employer matching, Certificate of Eligibility, status change, visa review, and long-term planning.
- Passing a test does not guarantee residence status, visa, employment, or long-term residence.

Official checks:

- MHLW nurse national exam eligibility recognition system, criteria, FAQ, annual application page, and document list.
- Immigration Services Agency SSW nursing care page.
- Prometric Long-term Care Specified Skilled Worker Evaluation Test page.
- Employer, residence status, Certificate of Eligibility, visa, and long-term residence rules.

## Germany

Separate:

- recognition of an existing nursing qualification
- vocational training route
- assistant or care-related work
- employer/contract route

Key factors:

- German language is central
- recognition authority varies by state and route
- shortage does not remove language, document, recognition, employment, or visa thresholds

## United States RN

Separate:

- nursing education background
- credential evaluation
- state board requirements
- NCLEX
- license
- employer sponsorship
- VisaScreen or healthcare worker certification where relevant
- immigration process

Risk:

- passing an exam does not guarantee job, visa, or immigration.

## Australia

Separate:

- education admission
- NMBA/Ahpra registration pathway
- English-language registration standard
- ANMAC skilled-migration assessment if migration is discussed
- visa and employment

Risk:

- "study and stay" is not a safe claim. Registration, employment, visa, and migration are separate.

### Australia OBA/IQNM for Internationally Qualified Nurses

Use this branch when the user asks about OBA, Ahpra, NMBA, Self-check, Stream A/B/C, Portfolio, MCQ/NCLEX-RN, OSCE, or a Chinese nurse applying for Australian RN registration.

Suitable for discussion:

- internationally qualified nurses or midwives with nursing education and registration background
- Chinese domestic nurses with traceable education, registration, and practice documents
- nursing graduates whose education and registration status need clarification
- applicants with another overseas nursing registration or previous NCLEX-RN history

Not a direct route for:

- gaokao students choosing a major
- users without nursing education
- ordinary first-degree study-abroad users
- users seeking a quick identity or migration shortcut

Core layers:

- Self-check: entry point for IQNMs; identifies assessment stream but does not decide final registration
- Stream A/B/C: official assessment stream; do not pre-assign without official process
- Portfolio: document, qualification, identity, registration, translation, and certification evidence
- MCQ/NCLEX-RN: exam layer for relevant RN candidates
- OSCE: in-person clinical assessment layer in Australia if required
- Registration: Ahpra/NMBA decision layer
- Visa and employment: separate from registration
- ANMAC: skilled migration assessment, separate from Ahpra/NMBA registration

Ask for:

- highest nursing education, school, graduation year, transcript, clinical hours, and internship evidence
- nurse qualification, practice certificate, registration status, regulator, and registration changes
- clinical experience, department, paid work duration, recency, and references
- English test status and clinical communication ability
- document traceability, translations, certifications, name changes, and consistency across records
- budget for assessment, English, exams, documents, travel, accommodation, visa, preparation, and repeat attempts
- ability to travel to Australia for OSCE if required
- final goal: registration, employment, ANMAC, visa, long-term residence, or feasibility screening

Provider handling:

- Bridge Medical Language / 新桥 BML and similar providers may be treated only as provider-claim samples or institution-type information sources.
- Do not recommend, rank, or endorse a training provider, migration agent, employer, school, or package route.

## Europe

For Poland, Croatia, France, Ireland, the UK, Germany, and other European countries:

- Do not treat Europe as one market.
- EU automatic recognition can matter for general care nurses, but it is not job, visa, residence, or immigration proof.
- The UK is outside EU recognition.
- France is language- and authorisation-heavy.
- Ireland uses NMBI recognition and registration layers.
- Poland and Croatia should not be described as shortcuts to the whole EU.

## School, Fee, and Provider-Claim Verification

When a user asks for a school, program, tuition, or provider claim:

1. Define the exact layer: education, fee, license, employment, visa, or residence.
2. Check regulator or official directory first.
3. Check school official program page.
4. Check fee schedule, refund policy, international-student rules, and clinical placement.
5. Check downstream licensing, visa, or credential evaluation authority.
6. Ask for written disclosure of cooperation, commission, employer referral, or agency relationship.

Red flags:

- "guaranteed admission"
- "guaranteed employment"
- "guaranteed visa"
- "guaranteed RN"
- "guaranteed immigration"
- "internal channel"
- "one diploma works everywhere"
- fee only appears in a screenshot or sales brochure

## Official Source Principles

Prefer:

- examination authorities
- education ministries
- professional nursing regulators
- licensing boards
- official school websites
- immigration departments
- official fee schedules

Treat social posts, rankings, agency articles, and third-party summaries as leads only.
