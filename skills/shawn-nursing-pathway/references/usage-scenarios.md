# Usage Scenarios

Use this file to keep the skill grounded in real consumer use. Load it when testing whether an answer feels useful, or when the user asks for improvements to the skill system.

## Contents

- Scenario 1: Gaokao Parent
- Scenario 2: Nursing Fit Conflict
- Scenario 3: Overseas Country Comparison
- Scenario 4: School and Fee Check
- Scenario 5: Provider Claim Check
- Scenario 6: Returning User
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

## Common Defects to Avoid

- Single-answer trap: answering one question but not suggesting the next useful module.
- Database trap: listing too many schools before clarifying the user's real decision.
- Precision trap: giving exact-looking policy or fee facts without current official verification.
- Agency-language trap: sounding like a留学中介 by emphasizing easy, shortcut, high salary, immigration, or guarantee.
- Over-questioning trap: asking ten questions before giving any frame.
- Under-routing trap: not telling the user whether the next best step is fit, volunteer review, path comparison, school check, or provider risk check.
- No-continuity trap: not producing a reusable case summary after a substantial screening.
