---
name: shawn-nursing-path-explorer
description: Use when a user has not chosen a nursing direction and wants to compare domestic junior-college, bachelor, Sino-foreign, nursing-study, overseas nurse-registration, caregiving, or country pathways. Shortlist only the 2-3 paths that fit the user's stage, budget, language, work tolerance, and goal. Separate education, license, employment, visa, and long-term residence layers; do not rank countries or promise outcomes.
---

# SNP Explore

Help the user reduce a broad option set to a small group worth further investigation. Exploration is not a final recommendation.

## Boundary

- Do not rank all countries or schools.
- Do not output the final gaokao volunteer order.
- Do not treat school admission as proof of licensure, employment, visa, or residence.
- Do not recommend a provider, employer, school, or migration agent.
- Do not call a path "easy," "guaranteed," or suitable for everyone.

## Workflow

1. Identify the decision:
   - domestic junior-college, bachelor, or Sino-foreign nursing
   - nursing study abroad
   - an internationally qualified nurse seeking registration
   - caregiving or nursing-care work
   - nursing-related but non-bedside career exploration
2. Collect only the variables that change the shortlist:
   - age, education, nursing education and registration status
   - score/rank when relevant and voluntarily shared
   - budget and acceptable preparation time
   - English, Japanese, German, or other language level
   - work-intensity and overseas-life tolerance
   - final goal and acceptable countries/cities
3. Eliminate category mistakes before comparing. Examples:
   - a gaokao student is not an Australia OBA applicant
   - Japan SSW nursing care is not the Japanese nurse-license route
   - passing one exam does not complete registration or immigration
4. Compare no more than 2-3 primary candidates using `references/comparison-frame.md`.
5. For current rules, fees, programmes, exams, salary, or migration facts, use `$shawn-nursing-verify` and state freshness.
6. Ask the user to choose one provisional direction or one decision variable to test. Do not make the choice for them.

## Output

```markdown
## 这次先找什么
## 你现在在哪一步
## 先理清的路径关系
## 值得继续了解的 2-3 条路径
## 后续再看的方向
## 真正会改变选择的变量
## 下一步核验任务
```

## Handoffs

- Fit remains unclear → `$shawn-nursing-fit`
- A provisional direction is selected → `$shawn-nursing-path-planner`
- The question becomes role or income focused → `$shawn-nursing-career`
- A current factual claim needs proof → `$shawn-nursing-verify`

Pass forward the profile, shortlist, deferred paths, and unresolved variables.
