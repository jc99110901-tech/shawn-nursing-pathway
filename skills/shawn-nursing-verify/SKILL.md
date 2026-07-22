---
name: shawn-nursing-verify
description: Use whenever a nursing answer depends on current or latest policy, statistics, school or programme status, tuition, admissions, licensing, exams, visa or migration rules, named employers, vacancies, hiring requirements, salaries, or provider claims. Search at answer time, prefer the newest official source for the exact claim, disclose freshness and unresolved gaps, and never substitute stale memory or marketing material for current evidence.
---

# SNP Verify

Verify dynamic claims before they shape a nursing education, career, or overseas-path decision.

## Boundary

- Do not call a source "latest" merely because it is the first official result.
- Do not use a crawl date as the publication or effective date.
- Do not replace an unavailable current official source with an undated secondary summary.
- Do not endorse a school, employer, provider, recruiter, or migration agent.
- Do not treat a verified rule as a guarantee of an individual outcome.

## Required Protocol

1. Define the exact claim, jurisdiction, user category, and target date or intake.
2. Search at answer time.
3. Prefer sources in this order:
   - regulator, ministry, examination authority, immigration authority, or statutory body
   - official school, hospital, employer, programme, pay scale, award, or collective agreement
   - official database, archive, listing, or same-series publication index
   - high-trust secondary material only as labelled context
4. Check the official same-series listing, archive, database, or superseding notices before calling an item latest.
5. Record search date, data/effective period, publication/update date, and freshness status.
6. If the newest official item found is older than the current year, say so explicitly.
7. If current verification fails, state what was searched and the exact unresolved item.
8. Split bundled claims into education, graduation, license/registration, employment, salary, visa, and long-term residence layers.
9. For Australian care-worker training or employer-sponsorship packages, load `../shawn-nursing-pathway/references/australia-aged-care-sponsorship-claims.md`. Separate English, qualification/RTO, skills assessment, employer eligibility, interview/offer, nomination/visa, and later residence. Do not turn practitioner opinion or a screenshot into a fraud finding.

Use `references/freshness-protocol.md` for statuses and output.

## Required Output

When a dynamic fact is used, place this section before analysis:

```markdown
## 信息时效
| 事实 | 检索日期 | 数据／规则适用期 | 发布或更新日期 | 时效状态 |
|---|---|---|---|---|
| ... | YYYY-MM-DD | ... | ... | ... |

- 尚未找到或仍需核验：
```

Then provide:

```markdown
## 核验结论
## 官方依据
## 这项事实能证明什么
## 不能证明什么
## 用户下一步
```

If browsing or official access is unavailable, say `本次未完成当前官方信息核验` and give the official body, likely page or register, and exact question to check. Do not answer the dynamic fact from memory.

## Salary Claims

Preserve the original metric: minimum scale, median, mean, percentile, posted range, base pay, or total cash earnings. State gross/net basis and separate shifts, overtime, bonus, housing, relocation, and allowances.

## Handoffs

Return the verified evidence brief to the calling fit, explorer, planner, career, or job-readiness module. Verification does not make the final decision.
