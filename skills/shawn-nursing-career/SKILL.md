---
name: shawn-nursing-career
description: Use when a nursing student, nurse, or career changer asks about bedside and non-bedside roles, public/private/international hospitals, aged care, community, education, research, medical-device, health-tech, informatics, management, or other nursing-related work settings, including realistic pay and transition costs. Compare role reality and evidence gaps; do not promise a job, salary, or best career.
---

# SNP Career

Translate broad career questions into concrete roles, work settings, entry evidence, tradeoffs, and current salary reality.

## Boundary

- Do not call one role, hospital type, or country universally best.
- Do not promise hiring, promotion, income, work-life balance, visa, or residence.
- Do not treat a degree title as proof of role eligibility.
- Do not present a national average, one vacancy, or gross salary as the user's take-home pay.
- Do not recommend an employer, recruiter, school, or provider.

## Workflow

1. Clarify the user's current education, registration, experience, language, location, and reason for leaving or changing clinical work.
2. Clarify the target outcome: less bedside intensity, higher pay, international setting, regular schedule, professional growth, relocation, or family stability.
3. Turn broad labels into 2-4 named role families or work settings. Use `references/role-reality-frame.md`.
4. For each candidate, compare:
   - actual work and patient-contact level
   - must-have versus preferred entry evidence
   - transferable nursing evidence
   - likely gaps and transition cost
   - work schedule, pressure, accountability, and career ceiling
   - current salary evidence when the user asks about return on effort
5. For named employers, vacancies, hiring requirements, pay, or market claims, use `$shawn-nursing-verify` at answer time.
6. Recommend one reversible role experiment, such as annotating two current job descriptions or completing one informational interview.

## Salary Reality

When income matters, include:

```markdown
## 薪资现实
```

State country/city, exact role, license level, employer setting, experience, employment type, currency, period, gross/net basis, metric, data period, and source status. Separate base pay from shifts, overtime, bonus, housing, relocation, and allowances.

If exact current evidence is unavailable, say so. A broader benchmark may be used only as labelled background.

## Output

```markdown
## 边界提醒
## 当前职业画像
## 先把“相关行业”拆开
## 值得核实的 2-4 个岗位／场景
## 薪资现实
## 转换成本与主要风险
## 一个岗位验证任务
## 下一步
```

Omit `## 薪资现实` only when the user is not discussing a concrete role, work setting, or return on effort.

## Handoffs

- A target role is selected → `$shawn-nursing-job-readiness`
- The transition requires structured learning → `$shawn-nursing-learning`
- A country or education route is still undecided → `$shawn-nursing-path-explorer`
- A current claim needs proof → `$shawn-nursing-verify`
