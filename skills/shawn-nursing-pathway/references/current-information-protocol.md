# Current Information Protocol

Use this reference whenever an answer depends on facts that may change. This includes statistics, policies, admissions, tuition and fees, programmes, licensing or registration, exams, visas, migration rules, named schools or hospitals, active job openings, hiring requirements, salaries, institutional scale, and career-market claims.

## Contents

- Freshness Gate
- Date Fields
- Search Sequence
- Source Status
- Named Institution and Recruitment Rules
- Salary and Compensation Rules
- Required User-Facing Disclosure
- Prohibited Freshness Claims

## Freshness Gate

Before using a time-sensitive fact:

1. Search at answer time. Do not rely on model memory, an earlier conversation, or a cached number.
2. Find the newest official source for the exact claim, not merely the newest page mentioning the topic.
3. Define the comparison scope before searching: full-year annual report, monthly or partial-period series, current intake, current policy version, active vacancy, or another exact series.
4. Inspect the official same-series listing, archive, database, or superseding notices and compare later entries before calling a source "latest."
5. Check each metric separately. Different facts from the same country may have different latest data years.
6. Record the search date, data or effective period, publication or update date, source owner, and source status.
7. If the newest official information is older than the current year, state that lag clearly.
8. If no current official source is found, say so. Do not fill the gap by presenting an older, undated, cached, or third-party source as current.

"Latest" means the newest verifiable official publication within a defined same-scope series. It does not mean that the data period must equal the current year. A newer partial-period release does not replace the latest full-year annual report; report both only when both scopes help the decision.

## Date Fields

Keep these dates separate:

- **Search date**: when the source was checked.
- **Data period or effective period**: the year, intake, cycle, or policy period the fact describes.
- **Publication or update date**: when the source owner published or officially updated it.
- **Page crawl date**: a search engine or tool metadata field. Never treat this as the publication or update date.

When a source does not show a publication or update date, label it "official page, date not shown." Do not describe it as a newly issued or current requirement without another dated official source.

## Search Sequence

1. Search the exact topic on the responsible government, regulator, exam authority, licensing board, or institution domain.
2. Open the dated document, linked PDF, fee schedule, notice, database record, or active job posting.
3. Open the official same-series listing, archive, database, or notice index. Compare all later-dated or later-period entries that could supersede the candidate source.
4. Keep full-year, partial-period, national, local, programme-specific, and vacancy-specific scopes separate.
5. Search the same official domain for a later year, superseding notice, replacement document, newer fee schedule, or newer posting.
6. For overseas routes, check both the regulator and the relevant government source when the claim crosses registration, employment, visa, or migration layers.
7. Use high-trust secondary reporting only as a lead. If it cannot be confirmed officially, label it as secondary and do not make it operational advice.

If the official listing or archive cannot be inspected, do not use the unqualified word "latest." Use the status "officially verified, latest not confirmed."

If browsing is unavailable, say:

> 本次无法联网核验最新官方资料，因此下面只解释通用路径，不把具体数字、费用、政策或招聘要求写成当前事实。

## Source Status

Assign one of these statuses to every material time-sensitive source:

- **Latest official confirmed**: a dated official source shown to be the newest entry in the defined same-scope official series.
- **Current official**: a dated official source applicable to the user's requested period, without claiming it is the newest in the series.
- **Officially verified, latest not confirmed**: a dated official source was checked, but the official series listing or later entries were not fully compared.
- **Latest official found, older period**: the newest official source found, but its data or effective period is older than the current year or requested intake.
- **Official but undated**: an official page exists, but its publication or update date is not shown.
- **Secondary only**: no official confirmation found; a high-trust secondary source is available only as a lead.
- **Not found**: no sufficiently reliable source was found for the exact claim.

Do not collapse these statuses into the word "current."

## Named Institution and Recruitment Rules

For a named hospital, school, employer, or provider:

- Separate general institution background from active programme or recruitment evidence.
- Treat an active official posting with a posting/update date, location, role, and application status as current recruitment evidence.
- Treat an old or undated nursing-team, careers, brand, or promotional page only as background.
- Do not infer that an old vacancy is still open because the page remains accessible.
- Do not infer current salary, benefits, staffing scale, hiring threshold, or career path from an undated marketing page.
- If no dated active posting is found, say: "官网存在相关介绍页，但本次未核验到带日期的当前招聘岗位或要求。"

## Salary and Compensation Rules

When the user asks what a specific role or completed pathway pays, also load `salary-and-compensation.md`.

- Define country/city, occupation and legal role level, employer setting, experience level, employment type, currency, pay period, and gross/net basis.
- Name the metric: statutory minimum, pay scale, median, mean, percentile range, posted range, base pay, or total cash earnings.
- Prefer current official occupational statistics, public pay scales, collective agreements, or dated official employer vacancies.
- Separate base pay from shift, weekend, overtime, bonus, housing, relocation, pension, and other allowances.
- Treat an official broad industry average as background unless it matches the requested occupation.
- Treat a vacancy as evidence for that vacancy, not the entire market.
- Treat a salary survey as a population estimate, not a personal offer.
- If converting currencies, show the original currency first and state the dated exchange-rate assumption.
- Never label gross pay as take-home pay or imply equal purchasing power after RMB conversion.
- If exact current evidence is not found, state the gap and do not invent a range from provider or social-media claims.

## Required User-Facing Disclosure

When time-sensitive facts materially affect the answer, include:

```markdown
## 信息时效
| 事实 | 检索日期 | 数据/规则适用期 | 发布或更新日期 | 时效状态 |
|---|---|---|---|---|
| ... | YYYY-MM-DD | ... | YYYY-MM-DD / 官网未标日期 | 最新官方已确认 / 当前官方 / 官方已核验但未确认最新 / 最新官方但数据期较早 / 官方但未标日期 / 仅有二手来源 / 未找到 |

- 尚未找到或仍需核验：
```

This exact section is mandatory when material time-sensitive facts are used. Put it before the analysis that relies on those facts. Do not replace it with dates scattered through the answer.

Use wording below the table when needed:

> 截至 [检索日期]，本次检索到的最新官方全国数据对应 [数据年度]，发布于 [发布日期]。本次未找到更新年度的同口径官方数据。

For mixed-year evidence, report each metric separately rather than saying that all domestic or overseas information is from one year.

## Prohibited Freshness Claims

Do not:

- call a source "latest" without comparing dates
- call a source "latest" after checking only one direct result without inspecting the official same-series listing, archive, database, or later notices
- use "目前" or "当前" for an old or undated fact
- use a search-engine crawl date as the source publication date
- present an evergreen institution page as an active vacancy or current programme
- hide the fact that the newest official data found is older than the current year
- imply that no newer source exists when only one search result was checked
- replace missing official evidence with confident wording from an agency, marketing page, social post, or cached snippet
