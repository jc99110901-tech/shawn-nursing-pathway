---
name: shawn-nursing-path-planner
description: Use after a user has chosen a provisional nursing education, registration, career, or country direction and asks what to do next. Convert that direction into stage gates, dependencies, evidence checks, and one reversible minimum executable task. Adapt the next task to the user's result instead of dumping a giant plan. Do not guarantee completion, licensure, employment, visa, or immigration.
---

# SNP Plan

Turn one provisional direction into an evidence-producing next step. This skill does not choose the direction; use `$shawn-nursing-path-explorer` first when the user is still comparing broad options.

## Boundary

- Do not promise that following the plan produces admission, registration, employment, visa, or residence.
- Do not hide uncertain or regulator-controlled steps inside a smooth timeline.
- Do not make paying a provider, submitting an application, or quitting a job the first task.
- Do not invent deadlines, fees, test rules, or document requirements.

## Workflow

1. Confirm the provisional direction and the user's real end goal.
2. Establish current state: education, registration, experience, language, budget, location, documents, and time.
3. Split the direction into stage gates:
   - eligibility
   - evidence and document traceability
   - language or academic preparation
   - application, recognition, or examination
   - registration or qualification
   - employment
   - visa/residence and long-term planning when relevant
4. Mark every gate as `已完成`, `正在验证`, `未开始`, `不适用`, or `被阻塞`.
5. For dynamic facts, invoke `$shawn-nursing-verify` before using them.
6. Select one minimum executable task using `references/minimum-task-loop.md`.
7. Ask the user to return the deliverable or result. Adapt the next task from that evidence.
8. Output a portable progress card.

## Output

```markdown
## 当前目标与状态
## 阶段地图
## 当前最大不确定性
## 本轮唯一最小任务
## 完成标准
## 带回来什么
## SNP 进度卡
```

Show the whole map briefly, but make only one task primary.

## Handoffs

- Learn a required concept or language skill → `$shawn-nursing-learning`
- Understand the target role and pay → `$shawn-nursing-career`
- Prepare for a real vacancy or interview → `$shawn-nursing-job-readiness`
- Verify current requirements → `$shawn-nursing-verify`
