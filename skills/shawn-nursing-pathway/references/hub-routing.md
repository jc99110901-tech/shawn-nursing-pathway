# Hub Routing

Use this file when the user enters with a vague question, asks "what should I do next," or returns after a previous nursing/pathway discussion. This skill should feel like a high-frequency front desk, not a one-off expert answer.

## Contents

- Routing-First Pattern
- Mode A: Before-Task Routing
- Mode B: After-Task Navigation
- Multi-Perspective Review Route
- Routing Table
- Dashboard Prompt
- Split-Later Candidates

## Routing-First Pattern

Use a routing-first front-desk structure:

- Main entry first routes the user's task.
- Specialist modules do the actual diagnosis or review.
- After each module, the entry suggests 2-3 next useful actions.
- User should be able to come back with "下一步" or "继续" and not start from zero.

For Shawn nursing, the main entry is `shawn-nursing-pathway`. It can route internally through reference files now. If usage becomes frequent, the high-frequency modules can later become separate skills.

## Mode A: Before-Task Routing

Use this when there is no clear prior module result in the current conversation.

If the user already states a clear task, route directly. Do not show a menu.

If the user is vague, ask one question:

```text
你现在最想解决的是哪一件？
1 护理适配：孩子/自己到底适不适合护理
2 志愿复核：已有学校或专业方案，想查风险
3 海外路径：比较菲律宾、日本、德国、英国、澳洲、美国、欧洲等方向
4 学校/费用核验：查某个学校、项目、学费或官方依据
5 机构话术核验：判断中介/学校/合作方说法是否靠谱
6 多视角会诊：从临床、升学、成本、政策或职业等不同角度看同一问题
7 下一步规划：已经聊过一轮，想知道下一步做什么
```

Then route based on the answer. Do not ask a second broad question.

## Mode B: After-Task Navigation

Use this after any substantial answer, especially if the user seems to need continued use.

Extract the current module result and recommend 2-3 next actions:

```text
根据刚才的结论，下一步最值得做的是：

- 护理适配继续问：因为现在最大不确定性是孩子能不能接受真实工作强度。
- 学校/费用核验：因为如果要比较国家，预算必须先落到官方学费和生活费。
- 机构话术核验：因为你提到的承诺里可能混了录取、就业、签证和注册。
```

Do not recommend every module. Pick the next few that reduce uncertainty most.

## Multi-Perspective Review Route

Route to `multi-perspective-review.md` when the user says things such as:

- "从不同角度帮我看看"
- "帮我会诊一下"
- "家长和孩子意见不一样"
- "我在两条路之间拿不定主意"
- "让临床、政策和职业发展几个视角讨论一下"

Do not use this route for a single current fact, fee, policy clause, or school lookup. Verify that fact directly first.

If the user has not named the desired perspectives, propose 3-5 relevant role perspectives and wait for confirmation. If the user says "直接开始" or names the roles, execute without another confirmation.

If the user did not ask for a multi-perspective review but the skill detects a family conflict or competing values, offer this route and wait for consent. Do not launch it automatically.

## Routing Table

| User signal | Route to module/reference | What the module should do |
|---|---|---|
| "要不要报护理" / "孩子适不适合护理" | `nursing-fit-assessment.md` | Fit screen: advantages, risks, questions to verify |
| "志愿表帮我看看" / "这些学校怎么排" | `volunteer-form-questions.md` | Review checklist only; no final ranking |
| "专科护理还是本科护理" / "中外合作值不值" | `pathway-comparison.md` | Compare tradeoffs by budget, score/rank, city, degree, license |
| "菲律宾/宿务/口腔" | `country-paths.md` + `official-source-map.md` | Separate education, license, return-country use, third-country use |
| "日本护理/介护" | `country-paths.md` | Separate nurse, caregiver, SSW, language, visa |
| "德国/英国/澳洲/美国/欧洲" | `country-paths.md` + `official-source-map.md` | Country screening; no job/visa/immigration promise |
| "哪个国家最好走" | `consumer-intent-routing.md` + `pathway-comparison.md` | Reframe into budget/language/goal fit; no country ranking |
| "某学校学费多少" / "哪些学校可选" | `institution-search-playbook.md` + `institution-source-index.md` | Search or specify current official sources; output a small table |
| "这个岗位多少钱" / "以后能拿多少" / "公立还是私立收入高" | `salary-and-compensation.md` + `current-information-protocol.md` | Give a scoped salary reality check with current evidence; no personal pay or take-home promise |
| "中介说包就业/包移民/保注册" | `product-boundary.md` + `institution-search-playbook.md` | Provider-claim risk review and disclosure checklist |
| "多视角看看" / "帮我会诊" / "家长和孩子意见不一致" | `multi-perspective-review.md` | Propose or run 3-5 distinct role perspectives; use independent Agents only when actually available, otherwise disclose the single-model fallback |
| "继续/下一步" after a result | This file, Mode B | 2-3 next-step recommendations |

## Dashboard Prompt

Only use this when the user is vague or asks to start:

```text
Shawn 护理路径工作台：
1 护理适配
2 志愿复核
3 海外路径
4 学校/费用核验
5 机构话术核验
6 多视角会诊
7 下一步规划
```

Do not show this dashboard when the user's request is already specific.

## Route Selection Rule

Keep all supported countries available, but do not show every route in ordinary answers.

Default path selection:

- If the user is a gaokao family, start with domestic nursing options plus at most one overseas direction.
- If the user mentions Cebu, Philippines, dentistry, or English-language low-cost study, include Philippines/Cebu.
- If the user mentions Japan, caregiving, age constraints, or Japanese learning, include Japan.
- If the user mentions Germany, UK, US RN, Australia, Europe, Poland, Croatia, France, or Ireland, route to the matching country section.
- If the user asks "哪个国家最好走", reframe into budget, language, education, license, job, visa, and long-term residence layers; shortlist 2-3 directions instead of ranking all countries.

## Split-Later Candidates

If this becomes a multi-skill collection, split only stable high-frequency modules:

- `shawn-nursing-fit`: nursing fit and family work-intensity screen
- `shawn-nursing-volunteer-review`: gaokao volunteer and domestic nursing plan review
- `shawn-nursing-overseas-screen`: country pathway screening
- `shawn-nursing-school-check`: school, fee, and official-source verification
- `shawn-nursing-salary-check`: role-level pay, compensation scope, and effort-return reality check
- `shawn-nursing-provider-risk`: agency, cooperation, employment, and promise-risk review
- `shawn-nursing-case-card`: summarize current user profile, risk state, and next actions for future continuation

Do not split too early. A split is worth it only when the module has a clear trigger, distinct workflow, and repeated user demand.
