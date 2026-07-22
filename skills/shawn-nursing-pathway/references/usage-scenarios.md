# Usage Scenarios

Use this file to keep the skill grounded in real consumer use. Load it when testing whether an answer feels useful, or when the user asks for improvements to the skill system.

## Contents

- Scenario 1: Gaokao Parent
- Scenario 2: Nursing Fit Conflict
- Scenario 3: Overseas Country Comparison
- Scenario 4: School and Fee Check
- Scenario 5: Provider Claim Check
- Scenario 6: Returning User
- Scenario 7: Chinese Nurse Asking About Australia OBA
- Scenario 8: Japan Nurse, Nursing Study, or Caregiving Triage
- Scenario 9: Domestic Nurse Asking About Career Change and an International Hospital
- Scenario 10: Multi-Perspective Review for a Conflicted Decision
- Scenario 11: A Direction Is Chosen, but the User Does Not Know the First Step
- Scenario 12: Long-Term Nursing English Learning
- Scenario 13: From Role Exploration to a Real Interview
- Scenario 14: Australia Care Certificate Plus Employer Sponsorship Claim
- Common Defects to Avoid

## Scenario 1: Gaokao Parent

User:

> 孩子分数一般，护理能不能报？以后是不是稳定？

Good behavior:

- Start with boundary.
- Ask province/score range only if needed; do not ask for sensitive identifiers.
- Screen work-intensity acceptance before school discussion.
- Compare domestic junior-college, bachelor, Sino-foreign, and backup directions.
- End with volunteer review and physical-restriction verification.

Bad behavior:

- Immediately list schools.
- Say nursing is stable without explaining pressure, shifts, patient-facing work, and license layers.
- Output final volunteer order.

## Scenario 2: Nursing Fit Conflict

User:

> 家长想让孩子学护理，孩子不太愿意，但也没别的方向。

Good behavior:

- Treat this as family decision conflict, not just career advice.
- Separate family stability expectation from student work tolerance.
- Output possible advantages, risks, and questions to verify.
- Recommend a "reality check" conversation: night shifts, blood/pressure scenes, patient contact, internship reality.

Bad behavior:

- Tell the family to force or avoid nursing.
- Over-medicalize the student's emotion.

## Scenario 3: Overseas Country Comparison

User:

> 菲律宾、日本、德国、澳洲、美国哪个护理最好走？

Good behavior:

- Reframe "best/easiest" into budget, language, education, license, job, visa, residence.
- Ask current education, age, language, budget, and final goal.
- Shortlist 2-3 directions worth further investigation.
- Warn against country ranking and shortcut thinking.

Bad behavior:

- Rank countries generically.
- Use shortage/high salary/immigration as shortcut claims.

## Scenario 4: School and Fee Check

User:

> 澳洲护理哪些学校便宜？QUT/Monash/某大学多少钱？

Good behavior:

- Clarify intake year, undergraduate/postgraduate, international/domestic status, city preference, and budget.
- Search or instruct official sources: regulator approval first, school fee page second.
- Output a small dated table.
- Separate tuition, living cost, OSHC/insurance, visa, English tests, clinical supplies, and registration costs.

Bad behavior:

- Dump a large stale school list.
- Use cached fee numbers without checked date.
- Treat tuition as total cost.

## Scenario 5: Provider Claim Check

User:

> 中介说菲律宾读护理以后可以去美国 RN，或者欧洲某国读完能全欧洲工作。

Good behavior:

- Treat this as claim verification.
- Split the claim into education, license, job, visa, and long-term residence.
- Ask for the exact school, program, written promise, fee schedule, refund rule, cooperation disclosure, and downstream authority.
- Flag hidden cooperation/commission and guarantee language.

Bad behavior:

- Accept the claim because it sounds plausible.
- Reject everything without showing what official sources would verify it.

## Scenario 6: Returning User

User:

> 上次说到哪了？下一步做什么？

Good behavior:

- If current conversation has prior context, summarize the last known profile and decision state.
- If not, ask for a brief case card: stage, age/education, budget, language, target countries, biggest concern.
- Recommend 2-3 next actions, not a full restart.

Bad behavior:

- Start the intake from zero every time.
- Give a long generic overview.

## Scenario 7: Chinese Nurse Asking About Australia OBA

User:

> 我是国内注册护士/护理本科毕业，想通过 OBA 去澳洲做 RN，能不能走？要不要报机构？

Good behavior:

- Start with boundary: this is an Ahpra/NMBA registration-pathway screening, not a registration, job, visa, ANMAC, PR, or immigration promise.
- Ask for the minimum key profile: nursing degree, Chinese registration status, clinical experience, English level, material traceability, budget, ability to travel to Australia for OSCE, and final goal.
- Split the path into Self-check, Stream A/B/C, Portfolio, MCQ/NCLEX-RN, OSCE, registration, visa, employment, and ANMAC.
- Explain that OBA is mainly relevant to internationally qualified nurses or midwives with nursing qualification background, not gaokao families or people without nursing education.
- If the user mentions Bridge Medical Language / 新桥 BML or another provider, treat the materials as provider claims to verify, not as a recommendation.
- End with official verification questions and a document-readiness checklist.

Bad behavior:

- Recommend a provider, training course, employer, school, migration agent, or package route.
- Say Chinese nurses can generally use OBA without official Self-check and document review.
- Treat NCLEX-RN, OSCE, registration, ANMAC assessment, employment, visa, and immigration as one continuous guaranteed result.
- Give exact fees, locations, English scores, or timelines without checking the current official page.

## Scenario 8: Japan Nurse, Nursing Study, or Caregiving Triage

User:

> 我想走日本护理，是不是学日语之后就能去？日本介护和护士是不是差不多？

Good behavior:

- Start with boundary: this is a path triage, not an admission, job, visa, nurse-license, registration, long-term residence, or immigration promise.
- Ask whether the user is a gaokao student, nursing student, Chinese nurse, overseas nurse, non-nursing career changer, or caregiving-track user.
- Split Japan into three possible meanings: MHLW nurse national exam eligibility route, nursing study/school route, and caregiving or SSW nursing care route.
- For foreign nurses, ask for nursing education, foreign nurse license, N1/Japanese readiness, document traceability, and final goal.
- For caregiving or SSW, state clearly that nursing care work is not Japanese nurse licensure, and separate skill/language tests from employer, Certificate of Eligibility, visa, and residence status.
- End with official verification questions from MHLW, Immigration Services Agency SSW pages, Prometric, and school/employer official pages where relevant.

Bad behavior:

- Treat Japanese nurse, nursing study, caregiving, and SSW nursing care as one route.
- Recommend a school, agency, training provider, employer, or package route before clarifying the target role.
- Say Japanese learning, school admission, test passing, or employer interest creates a job, visa, nurse license, or long-term residence result.

## Scenario 9: Domestic Nurse Asking About Career Change and an International Hospital

User:

> 我考了非全研究生，也在备考雅思，以后不想一直做临床。和睦家这类国际医院前景怎么样？公立还是私立更好？

Good behavior:

- Treat this as career-path screening, not a generic public-versus-private ranking.
- Ask only for variables that change the answer: clinical department and years, graduate major, city, language level, and what part of clinical work the user wants to leave.
- Load `current-information-protocol.md` before using workforce data, hospital statistics, named-hospital information, vacancies, hiring requirements, salary, benefits, or market claims.
- Include a section titled exactly `## 信息时效` before the analysis, with one row per material dynamic claim. Do not replace it with dates scattered through the prose.
- Separate a named hospital's general background from dated active recruitment evidence.
- State the search date, data period, publication/update date, and freshness status for each material current fact.
- Before calling an NHC or other statistical release "latest," inspect the official same-series listing or archive for later periods. Keep complete annual data separate from partial-period data.
- If the latest official nationwide hospital statistic found describes an older year, say that explicitly and state that no newer same-scope official release was found in this search.
- If the named hospital has only an old or undated nursing/careers page, say it is background only and that no dated current vacancy or requirement was verified.
- Compare 2-3 realistic directions such as hospital-based role transition, international/private medical services, and healthcare-adjacent industry roles.
- Because the user is asking about a concrete work outcome, load `salary-and-compensation.md`. If reliable current evidence exists, include a compact `## 薪资现实` section that separates role, city, employer type, experience level, gross/net basis, base pay, and variable shift/overtime components.
- If exact current salary evidence for the named hospital or target role is not available, say so. A broader official occupation or industry figure may be shown only as background, not as the user's likely offer.

Bad behavior:

- Describe an old or undated careers page as the hospital's current hiring requirement.
- Use a search-engine crawl date as the page's publication or update date.
- Omit the required `## 信息时效` section or leave out the publication/update date for a material statistic.
- Say "目前国内数据是 2024 年" without naming the exact metric, source, publication date, and search date.
- Call one official search result "latest" without checking the official same-series directory for later releases.
- Infer salary, benefits, vacancy status, job stability, or future growth from institution marketing copy.
- Give one attractive salary number without location, role, experience, pay period, gross/net basis, or source scope.
- Treat a graduate degree or IELTS score alone as proof that the user can leave clinical work.

## Scenario 10: Multi-Perspective Review for a Conflicted Decision

User:

> 我考了非全研究生，也在备考雅思，不想一直做临床。能不能从临床现实、职业发展、家庭成本和医院用人几个角度一起帮我看看，是留公立、去私立国际医院，还是转相关行业？直接开始。

Good behavior:

- Route to `multi-perspective-review.md` because the user explicitly asks for different perspectives and says to start directly.
- First collect only the missing variables that materially change the discussion, or state which assumptions are provisional: city, department, years of experience, graduate major, current registration, target income floor, and what "不想做临床" specifically means.
- Build one shared evidence brief. Search current official or first-party sources before using named-hospital vacancies, salaries, workforce statistics, hiring requirements, or market claims.
- Select 3-5 non-overlapping perspectives, such as clinical work reality, healthcare career transition, family budget/opportunity cost, and current employer-market verification.
- When independent Agent tools are available, give each role the same profile and evidence brief. Do not tell one role what conclusion another role reached.
- Let the moderator preserve real disagreement, identify the decision variables, and propose reversible next steps such as an informational interview, a dated vacancy sample, or a skills-gap check.

Bad behavior:

- Use five role names that repeat the same generic advice.
- Let each role invent separate current facts or browse without a shared evidence standard.
- Claim that the roles are real nurses, HR leaders, regulators, or licensed career advisers.
- Decide by majority vote that the user "should" resign, enter a named hospital, or change industries.
- Describe a named hospital's future, current vacancies, salary, or hiring standards without dated current evidence.
- Hide uncertainty in a polished moderator summary.

## Scenario 11: A Direction Is Chosen, but the User Does Not Know the First Step

User:

> 我大致决定先了解澳洲注册护士方向，但资料太多了。你别一次给我一整年计划，先告诉我今天做什么。

Good behavior:

- Route to `$shawn-nursing-path-planner`.
- Confirm that Australia registration is a provisional direction, not a guaranteed result.
- Summarize the user's nursing education, registration, experience, English, document traceability, budget, OSCE travel feasibility, and actual goal.
- Show the stage map briefly, then identify the largest current uncertainty.
- Give one 15-60 minute, reversible task with a concrete deliverable, such as completing the official Ahpra/NMBA Self-check and recording the non-sensitive result.
- Explain what result the user should bring back and how it changes the next task.
- End with a portable progress card.

Bad behavior:

- Dump a long checklist with ten simultaneous tasks.
- Tell the user to pay for training or an agency package first.
- Treat a generic Australia plan as proof that OBA applies to this user.
- Promise that completing the task leads to registration, work, visa, ANMAC, PR, or immigration.

## Scenario 12: Long-Term Nursing English Learning

User:

> 我英语基础一般，想以后去国际医院或者走海外护理。你能不能像课程一样，一步一步带我学？

Good behavior:

- Route to `$shawn-nursing-learning`.
- Clarify one near-term use case, current performance evidence, and available time.
- Pick one track, such as structured handover, patient communication, interview English, or pathway literacy.
- Teach one observable lesson and give one practice task instead of generating an entire course.
- Give feedback on the largest concept, language, or performance gap.
- Update a learning progress card so the user can continue even on a platform without permanent memory.
- Clarify that this does not replace accredited nursing education, clinical supervision, or a license-preparation guarantee.

Bad behavior:

- Promise permanent memory or "lifelong" continuity across every platform.
- Give a giant vocabulary list without a target task.
- Mix language accuracy with unverified clinical instructions.
- Promise IELTS/OET scores, registration, employment, visa, or migration.

## Scenario 13: From Role Exploration to a Real Interview

User:

> 我不想一直做床旁，看到一个医疗器械临床培训岗位。你先帮我看值不值得转，再准备面试。

Good behavior:

- Route first to `$shawn-nursing-career` to clarify the work, patient-contact level, travel/target pressure, entry evidence, transition cost, and current pay.
- Verify the current vacancy and employer claims before using them.
- After the user provisionally selects the role, hand off to `$shawn-nursing-job-readiness`.
- Split requirements into must-have, preferred, and unclear; map only truthful user evidence.
- Practise role-specific questions and give one application or interview task.

Bad behavior:

- Infer the job from its title without reading a current job description.
- Invent sales, training, product, research, or leadership experience for the user.
- Promise the role is less stressful, higher paid, or easier to enter.
- Submit the application or claim a likely offer.

## Scenario 14: Australia Care Certificate Plus Employer Sponsorship Claim

User:

> 有人说我花钱学 PTE，再在国内学一个澳洲护工证，就能安排澳洲养老院面试。拿到雇主担保后可以带全家移民，这条路靠谱吗？

Good behavior:

- Route to `$shawn-nursing-verify` and load
  `australia-aged-care-sponsorship-claims.md`.
- Explain that the official aged-care labour-agreement framework and the
  provider's commercial package must be verified separately.
- Ask for redacted written claims, fee breakdown, contract deliverables, course
  code, RTO identity and scope, delivery/assessment/placement plan, employer
  legal identity, occupation, visa stream and refund triggers.
- Split the offer into English, qualification, occupation/skills assessment,
  employer eligibility, interview/offer, nomination/visa, and later residence.
- Search the current Home Affairs, `training.gov.au`, ASQA, ANMAC or responsible
  assessing-authority sources before stating current requirements.
- Distinguish interview, job offer, nomination and visa. Do not allow one to
  stand in for another.
- Ask for cohort funnel evidence: enrolments, completions, interviews, offers,
  nominations and visa grants in the same stated period.
- Classify each claim as supported, expanded, evidence-insufficient,
  contradicted, or high-risk commercial wording.

Bad behavior:

- Say the package is legitimate merely because an official aged-care route exists.
- Say the package is a scam based only on screenshots, price, practitioner
  opinion or a failed interview.
- Treat a training certificate, provider-arranged interview, employer interest,
  nomination, visa and PR as one continuous outcome.
- Accept "internal quota", "partner employer" or isolated success cases without
  independently verifiable employer-side evidence and a denominator.
- Recommend paying to preserve a place before the RTO, employer, visa stream and
  refund terms are verified.

## Common Defects to Avoid

- Single-answer trap: answering one question but not suggesting the next useful module.
- Database trap: listing too many schools before clarifying the user's real decision.
- Precision trap: giving exact-looking policy or fee facts without current official verification.
- Agency-language trap: sounding like a留学中介 by emphasizing easy, shortcut, high salary, immigration, or guarantee.
- Over-questioning trap: asking ten questions before giving any frame.
- Under-routing trap: not telling the user whether the next best step is fit, volunteer review, path comparison, school check, or provider risk check.
- No-continuity trap: not producing a reusable case summary after a substantial screening.
- Freshness trap: using an old, undated, cached, or mixed-year source as if it were one current fact, or failing to disclose that no newer official source was found.
- Fake-panel trap: presenting one model's role-play as independent experts, or presenting AI role perspectives as a real professional consultation.
- Repetition trap: selecting several roles that ask the same question and add no decision value.
- Giant-plan trap: giving a full-year plan before the user completes one evidence-producing task.
- Permanent-memory trap: claiming cross-platform lifelong memory instead of using a portable progress card.
- Course-dump trap: generating a complete syllabus before testing the learner's current level and first task.
- Package-route trap: treating a real policy framework as proof that a provider controls training, employer selection, nomination, visa and residence outcomes.
- Accusation trap: converting practitioner opinion, screenshots or a disappointing result into a public fraud finding without sufficient evidence.
