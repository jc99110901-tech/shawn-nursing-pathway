# Institution Search Playbook

Use this file when the user asks for current schools, programmes, tuition, intake, application pages, a named hospital or employer, active recruitment, hiring requirements, or whether a named institution/provider claim is reliable.

## Contents

- Search Policy
- When to Search
- Search Workflow
- Minimum Output Table
- Verification Questions
- Red Flags

## Search Policy

- Do not try to store every school and fee inside the skill.
- Use the skill to define what should be searched, which sources count, how to structure the result, and what risks to flag.
- If internet access is available, check current official sources before giving school or fee facts.
- If internet access is not available, give the user a verification checklist and exact source types to check.
- Always separate current search result from general pathway explanation.
- Load `current-information-protocol.md` and apply its date and disclosure rules.
- Do not treat an old or undated institution page as proof of a current programme, vacancy, salary, benefit, or hiring requirement.

## When to Search

Search current sources when the user asks:

- "哪些学校可以读护理?"
- "某国家护理学费多少?"
- "某某大学护理靠谱吗?"
- "这个项目能不能拿执照?"
- "这个中介说包就业/包移民/直通注册，可信吗?"
- "帮我列几个适合我预算的学校."
- "我要准备申请/交定金/签合同/填志愿了."
- "某家医院现在招不招护士，要求是什么?"
- "某家国际医院或私立医院现在的发展和岗位前景怎么样?"

If the user is only asking whether a broad direction is worth了解, first do pathway screening and ask for profile. Do not jump straight to school lists.

## Search Workflow

1. Define the decision layer:
   - education admission
   - graduation or credential
   - license or registration
   - employment
   - visa
   - long-term residence or immigration
2. Define the exact target:
   - country, city, intake year, degree level, student identity, language, budget, and final goal
   - for jobs: employer, location, role, department, employment type, and target application period
3. Define the freshness target:
   - requested year or intake
   - exact metric, policy, fee, programme, vacancy, or hiring condition
   - what would count as a dated current official source
4. Search official directory or regulator:
   - nursing board, education ministry, professional regulator, approved-program database, school registry, or exam authority
5. Search institution official page:
   - program page, admissions page, fee schedule, refund policy, international-student page, clinical placement page
   - for jobs: current career portal, dated job posting, location, role status, and closing/application information
6. Search downstream authority:
   - license board, visa page, credential evaluator, professional body, or immigration authority
7. Inspect the official listing, archive, database, or notice index, then search the same official domain for a later release, superseding notice, newer fee schedule, or newer posting. If this comparison cannot be completed, do not call the result "latest."
8. Record source quality and freshness:
   - official regulator
   - school official
   - government
   - employer official and dated active posting
   - official but undated background page
   - third-party lead only
   - agency claim
9. Output only what helps the decision. Keep extra raw links out unless the user asks for a deeper table.

## Minimum Output Table

Use a compact table like this:

| 项目/学校/岗位 | 官方依据及日期 | 时效状态 | 费用/时长/岗位状态 | 对用户的意义 | 还必须核实 |
|---|---|---|---|---|---|
| ... | regulator/school/employer URL | 当前官方/较早/未标日期/未找到 | amount, duration, active status, or "未公开" | why it may fit/not fit | license, visa, refund, vacancy, etc. |

For fee searches, include:

- checked date
- intake year
- domestic/international status
- fee unit: annual, semester, course, application, exam, or recognition fee
- whether it is indicative, confirmed, estimated, or not public

For named hospitals or job searches, include:

- search date
- posting or update date
- location and department
- whether the posting is active, closed, archived, undated, or unclear
- whether requirements come from the exact vacancy or only a general careers page
- which salary, benefit, shift, language, experience, and license facts remain unverified

## Verification Questions

Ask the school/provider for:

- official program name and credential
- current tuition and all compulsory non-tuition fees
- refund and withdrawal policy
- international-student requirements
- clinical placement arrangement
- language requirement
- license or registration relevance
- whether the program is approved by the relevant regulator
- whether any partner, agent, employer, commission, or referral relationship exists
- what happens if visa, language, placement, license, or recognition fails

## Red Flags

Warn the user if:

- the provider refuses to show official school/regulator pages
- the fee only appears in a screenshot or sales brochure
- the claim says "one diploma works in all countries"
- the pathway merges study, license, job, visa, and immigration into one promise
- a "scholarship" is used to pressure immediate payment
- the school page exists but the exact program, intake, or fee cannot be verified
- the plan depends on hidden cooperation, commission, or employer promise
- an old or undated careers page is described as a current vacancy
- a search-engine crawl date is used as if it were the official publication date
- the newest official data found is from an older period but the answer says "目前" without disclosure
