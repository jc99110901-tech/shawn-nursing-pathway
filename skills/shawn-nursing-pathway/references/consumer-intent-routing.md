# Consumer Intent Routing

Use this file when the user asks a broad, emotional, or consumer-facing question. The skill should answer the decision need, not dump a database.

## Contents

- Core Rule
- Common Consumer Questions
- What to Ask Next
- What to Output
- What Not to Do

## Core Rule

Most users are not really asking for "all schools" or "all countries." They are asking one of these:

- Can my child use nursing as a realistic path?
- Is nursing a bad fit for this student?
- Which route matches our budget, language, age, and risk tolerance?
- Is this school, agency, or country claim reliable?
- What should we verify before paying, applying, or filling a volunteer form?

Answer that decision need first. Use school lists, fee data, and official pages only as supporting evidence.

For high-frequency use, treat every user request as one of three jobs:

- decide whether nursing is worth considering
- verify whether a concrete path/school/provider claim is risky
- identify the next official information to check before money, application, or volunteer submission

## Common Consumer Questions

### "高考志愿要不要选护理?"

Route to:

- nursing fit assessment
- domestic junior-college/bachelor comparison
- volunteer review checklist
- physical restriction and school brochure verification

Do not output a final volunteer order.

### "孩子适不适合学护理?"

Route to:

- work intensity tolerance
- night shift and rotation tolerance
- patient-facing pressure
- family expectation versus student's own acceptance
- backup path if nursing is chosen only as a fallback

Do not say the student is definitely suitable or unsuitable.

### "哪个国家护理最好走?"

Route to:

- education, license, job, visa, and long-term residence layers
- budget, language, age, current education, and final goal
- country shortlisting, not country ranking

Do not use "easy," "guaranteed," "shortage," or "high salary" as the main logic.

### "某某学校/项目靠不靠谱?"

Route to:

- official regulator or directory check
- school official program page
- fee page and refund rule
- license/registration relevance
- provider cooperation and commission disclosure

Do not decide only from an agency brochure, ranking, or social post.

### "澳洲/英国/菲律宾/日本/德国/美国学费大概多少?"

Route to:

- ask for target intake, student identity, degree level, and country/city
- search current official course and fee pages if browsing is available
- give a fee range only when source-backed and dated
- separate tuition from living cost, exams, visa, insurance, clinical supplies, credential evaluation, and emergency budget

Do not treat a cached fee number as permanent.

### "菲律宾宿务护理/口腔值得了解吗?"

Route to:

- why Cebu rather than another city
- CHED school/program recognition
- dentistry versus nursing difference
- PRC/local license and foreign-student rules
- China CSCSE or third-country downstream use
- fee schedule, refund, housing, visa, and service-provider disclosure

Do not turn Cebu into a universal answer.

### "欧洲护理能不能走? 波兰/克罗地亚/法国/英国呢?"

Route to:

- EU/EEA recognition layer versus national regulator layer
- target language
- study route versus professional recognition route
- registered nurse versus caregiver/assistant distinction
- visa/residence and employer layer

Do not say one European diploma automatically works across Europe.

## What to Ask Next

Ask only the minimum questions that change the answer:

- Who is deciding: student, parent, nurse, nursing student, or career changer?
- What is the current stage and education level?
- What is the budget and acceptable timeline?
- What language can the user realistically study?
- What is the final goal: domestic employment, overseas study, overseas work, immigration-oriented planning, or family stability?
- Has a school, country, agency, or provider already been named?
- Is the user near a payment, contract, application, or volunteer submission deadline?

## What to Output

Prefer decision-support outputs:

- "This is worth further investigation if..."
- "This is high risk for this profile because..."
- "Before paying or applying, verify these documents..."
- "The next search should check these exact official pages..."
- "This is not enough information for a school/country conclusion yet."

When school or fee facts are needed, produce a source-backed mini table, not an exhaustive list.

End substantial responses with a short "next-step navigation" so the user knows whether to continue with fit, volunteer review, country path, school/fee check, or provider claim check.

## What Not to Do

- Do not create a giant school encyclopedia inside the skill answer.
- Do not rank all schools or countries.
- Do not present cached fee data without a checked date.
- Do not let a user's desire for certainty turn into false precision.
- Do not answer a school-list question before clarifying the user's real decision layer.
