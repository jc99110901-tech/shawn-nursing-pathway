# SNP Skill Modular Architecture

Use this file to route across the SNP Skill suite without making the user learn the product structure first.

## Design Goal

The suite supports this user lifecycle:

```text
护理适配
→ 路径探索
→ 选定方向后的阶段规划
→ 护理知识／职业英语学习
→ 岗位与薪资现实
→ 求职与面试准备
```

Verification can be called at any point.

The main router is `shawn-nursing-pathway`. The focused child skills are:

| Skill | Use it when | Primary output |
|---|---|---|
| `shawn-nursing-fit` | The user asks whether nursing is worth considering or whether they can tolerate the work | Possible advantages, main risks, verification questions |
| `shawn-nursing-path-explorer` | The user has not chosen a direction and needs 2-3 relevant domestic or overseas candidates | Shortlist, tradeoffs, deferred paths, decision variables |
| `shawn-nursing-path-planner` | The user has chosen a provisional direction and asks what to do next | Milestone map, dependencies, one minimum executable task |
| `shawn-nursing-learning` | The user wants to learn nursing knowledge, professional English, or pathway literacy step by step | One lesson, one practice task, feedback check, progress card |
| `shawn-nursing-career` | The user asks about roles, work settings, career transitions, or realistic pay | Role comparison, entry gaps, current salary evidence, trial task |
| `shawn-nursing-job-readiness` | The user has a role or job description and needs application or interview preparation | Requirement map, evidence gaps, interview practice, questions to ask |
| `shawn-nursing-verify` | The answer depends on current policy, school, fee, salary, recruitment, or a provider claim | Freshness table, source trail, verification status, unresolved items |

## Five User-Facing Entrances

Do not show eight skill names to a new user. If their request is vague, show only:

```text
1 看自己／孩子是否适合护理
2 比较国内外学习和执业路径
3 已经选了方向，拆下一步
4 学护理／英语，或准备岗位和面试
5 核验政策、学校、费用、薪资或机构说法
```

Route option 4 again based on the immediate goal:

- learn knowledge or English → `shawn-nursing-learning`
- understand roles, settings, or pay → `shawn-nursing-career`
- prepare for a named role, application, or interview → `shawn-nursing-job-readiness`

Route option 5 to `shawn-nursing-verify`.

## Minimum Executable Task

Once a direction is provisionally chosen, do not end with a giant plan. Give one task that:

- normally takes 15-60 minutes
- has one concrete deliverable
- does not require paying a provider or making an irreversible commitment
- produces evidence that changes the next decision
- names what result the user should bring back

Good examples:

- complete an official regulator self-check and record the result without sharing sensitive identifiers
- compare two current official programme pages in a three-column table
- annotate one real job description into must-have, preferred, and unclear requirements
- record a 60-second English handover and identify three communication gaps
- ask one practising nurse five prepared questions, with consent and without patient information

Bad examples:

- "Improve your English"
- "Research Australia"
- "Apply to several schools"
- "Pay for a package first"
- "Prepare everything"

## Progress Card

Use this card when the user says "继续", changes platforms, or wants a longer learning journey:

```markdown
## SNP 进度卡
- 当前阶段：
- 用户目标：
- 已知画像：
- 暂定方向：
- 已核验事实与日期：
- 当前最大不确定性：
- 已完成的最小任务：
- 任务结果／反馈：
- 下一项最小任务：
- 建议调用模块：
```

Do not include sensitive identifiers. The card is a portable summary, not proof that the platform has permanent memory.

## Continuity Boundary

The suite supports iterative, long-term learning and planning. It does not guarantee:

- permanent memory across platforms or deleted conversations
- that a lesson sequence replaces accredited nursing education
- that completing tasks leads to admission, licensure, employment, visa, or immigration outcomes

When history is unavailable, ask for the latest progress card or collect only the missing state.
