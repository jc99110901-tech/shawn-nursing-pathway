---
name: shawn-nursing-job-readiness
description: Use when a user has a nursing or nursing-related target role, job description, application, CV, interview, or offer-stage question. Map current requirements to truthful evidence, identify gaps, practise role-specific answers, prepare questions for the employer, and flag job-specific risks. Do not invent qualifications or experience, submit applications, negotiate as the user, or promise hiring, pay, visa, or sponsorship.
---

# SNP Interview

Prepare the user for one real role or hiring stage. Work from evidence, not an idealized candidate profile.

## Boundary

- Never invent employment, clinical cases, responsibilities, metrics, certificates, language scores, or registration.
- Do not ask for unredacted identity documents, contact details, employee numbers, patient information, or private contracts.
- Do not promise interviews, offers, salary, sponsorship, visa, registration, or promotion.
- Do not impersonate the user or submit an application.
- Current vacancy, employer, salary, registration, and visa facts require verification.

## Intake

Ask for only what is needed:

- target country/city and exact role
- job description or official vacancy link, preferably current
- current education, registration, experience, and language evidence
- application stage and deadline
- user's main concern

Ask the user to remove names, contact details, IDs, patient details, and confidential employer information.

## Workflow

1. Verify that the vacancy or role information is current using `$shawn-nursing-verify` when available.
2. Split requirements into:
   - must-have
   - preferred
   - unclear or needs official confirmation
3. Map each requirement to:
   - proven evidence
   - partial evidence
   - no evidence
   - not applicable
4. Pick the largest addressable gap.
5. Use `references/readiness-workflow.md` for CV evidence, interview practice, employer questions, and red flags.
6. Give one minimum task and explain what to bring back.

## Output

```markdown
## 边界提醒
## 岗位与信息时效
## 要求拆解
## 你已有的证据
## 主要缺口
## 面试／申请准备
## 这个岗位要特别问清的事
## 本轮唯一任务
```

Do not rewrite the entire CV unless the user asks. Start with the evidence map so later writing remains truthful.

## Handoffs

- The user needs role comparison first → `$shawn-nursing-career`
- A skill or English gap needs practice → `$shawn-nursing-learning`
- A pathway prerequisite is unclear → `$shawn-nursing-path-planner`
- A current employer or salary claim needs proof → `$shawn-nursing-verify`
