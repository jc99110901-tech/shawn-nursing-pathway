# Hub Routing

Use this file when the user enters with a vague question, asks "what should I do next," or returns after a previous nursing/pathway discussion. This skill should feel like a high-frequency front desk, not a one-off expert answer.

## Contents

- Routing-First Pattern
- Mode A: Before-Task Routing
- Mode B: After-Task Navigation
- Multi-Perspective Review Route
- Routing Table
- Dashboard Prompt
- Progress Continuity

## Routing-First Pattern

Use a routing-first front-desk structure:

- Main entry first routes the user's task.
- Specialist modules do the actual diagnosis or review.
- After each module, the entry suggests 2-3 next useful actions.
- User should be able to come back with "下一步" or "继续" and not start from zero.

For Shawn nursing, the main entry is `shawn-nursing-pathway`. Stable high-frequency workflows are now separate child skills. The main entry should route to them when available and perform the same workflow internally when they are not.

On a combined single-skill distribution, load `references/modules/<skill-name>/SKILL.md` when that packaged module file is present. Do not tell the user that a separate child skill was invoked when the runtime only used the combined fallback.

## Mode A: Before-Task Routing

Use this when there is no clear prior module result in the current conversation.

If the user already states a clear task, route directly. Do not show a menu.

If the user is vague, ask one question:

```text
你现在最想解决的是哪一件？
1 看自己／孩子是否适合护理
2 比较国内外学习和执业路径
3 已经选了方向，拆下一步
4 学护理／英语，或准备岗位和面试
5 核验政策、学校、费用、薪资或机构说法
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
| "要不要报护理" / "孩子适不适合护理" | `$shawn-nursing-fit` or `nursing-fit-assessment.md` | Fit screen: advantages, risks, questions to verify |
| "志愿表帮我看看" / "这些学校怎么排" | `volunteer-form-questions.md` | Review checklist only; no final ranking |
| "专科护理还是本科护理" / "中外合作值不值" | `$shawn-nursing-path-explorer` or `pathway-comparison.md` | Compare tradeoffs by budget, score/rank, city, degree, license |
| "菲律宾/宿务/口腔" | `country-paths.md` + `official-source-map.md` | Separate education, license, return-country use, third-country use |
| "日本护理/介护" | `country-paths.md` | Separate nurse, caregiver, SSW, language, visa |
| "德国/英国/澳洲/美国/欧洲" | `country-paths.md` + `official-source-map.md` | Country screening; no job/visa/immigration promise |
| "哪个国家最好走" | `$shawn-nursing-path-explorer` + `consumer-intent-routing.md` | Reframe into budget/language/goal fit; no country ranking |
| "方向定了，第一步做什么" | `$shawn-nursing-path-planner` | Build milestones and give one reversible, evidence-producing task |
| "一步一步学护理" / "练护理英语" | `$shawn-nursing-learning` | One adaptive lesson and one practice task at the user's level |
| "不想一直做临床" / "有哪些岗位" / "公立还是私立" | `$shawn-nursing-career` | Compare role reality, entry gaps, work setting, and current pay evidence |
| "帮我看 JD" / "简历怎么写" / "面试怎么答" | `$shawn-nursing-job-readiness` | Map requirements to evidence; do not invent experience |
| "某学校学费多少" / "哪些学校可选" | `$shawn-nursing-verify` + `institution-search-playbook.md` | Search current official sources; output a small table |
| "这个岗位多少钱" / "以后能拿多少" | `$shawn-nursing-career` + `$shawn-nursing-verify` | Give a scoped salary reality check with current evidence; no personal pay promise |
| "中介说包就业/包移民/保注册" | `$shawn-nursing-verify` + `product-boundary.md` | Split the claim by layer and verify evidence |
| "多视角看看" / "帮我会诊" / "家长和孩子意见不一致" | `multi-perspective-review.md` | Propose or run 3-5 distinct role perspectives; use independent Agents only when actually available, otherwise disclose the single-model fallback |
| "继续/下一步" after a result | `suite-architecture.md` + this file | Restore the progress card and recommend one primary task plus 1-2 alternatives |

## Dashboard Prompt

Only use this when the user is vague or asks to start:

```text
SNP Skill 护理路径工作台：
1 看自己／孩子是否适合护理
2 比较国内外学习和执业路径
3 已经选了方向，拆下一步
4 学护理／英语，或准备岗位和面试
5 核验政策、学校、费用、薪资或机构说法
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

## Progress Continuity

Use the progress card in `suite-architecture.md` when a user wants long-term learning or returns with "继续". Do not claim the platform remembers permanently. If no history or card is available, ask only for the current goal, last completed task, and result.
