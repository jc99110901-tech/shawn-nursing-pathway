# Salary and Compensation Reality Check

Use this reference when the user's real question includes "after all this effort, what can I realistically earn?"

## Contents

- Trigger
- Minimum Context
- Source Hierarchy
- Search Workflow
- Required Output
- Interpretation Rules
- Fallback
- Official Starting Points
- Prohibited Claims

## Trigger

Include a compact salary reality check when the user asks about:

- a specific occupation, role, specialty, employer type, hospital department, or work setting
- public versus private hospitals, international hospitals, care institutions, agencies, or non-clinical nursing work
- the employment outcome of a named education, registration, or overseas pathway
- career prospects, return on time and money, whether a difficult path is financially worth it, or what the user can earn after qualification
- a comparison in which income materially changes the decision

Do not force a salary section into a broad nursing-fit question when the user has not reached a concrete job or pathway layer.

## Minimum Context

Before giving a specific number, identify or clearly state the assumed:

- country, region, and city
- occupation and legal role level, such as registered nurse, enrolled nurse, nursing assistant, caregiver, clinical research coordinator, or case manager
- license or registration status
- public, private, international, aged-care, community, agency, or other employer setting
- entry, experienced, specialist, or management level
- full-time, part-time, casual, contract, or agency work
- base schedule, night shifts, weekends, overtime, and material allowances
- currency and pay period

If 2-3 missing variables could change the range substantially, ask only those variables. Otherwise state a cautious assumption and continue.

## Source Hierarchy

Prefer sources in this order:

1. Current statutory pay table, collective agreement, public-sector salary scale, government occupational wage dataset, or regulator-linked remuneration source.
2. Current dated official employer vacancy or employer pay table for the exact role and location.
3. High-trust professional association, union, or large transparent salary survey with methodology, sample, period, and role definition.
4. Multiple dated job postings or recruitment-platform records as a market signal only.
5. Provider, agency, training-school, influencer, forum, or social-media claims as unverified leads only.

An official national or industry average is not automatically a nurse salary. A current employer vacancy is evidence for that vacancy, not the entire market.

## Search Workflow

1. Load `current-information-protocol.md` and search at answer time.
2. Search the responsible labour-statistics agency, public pay scale, collective agreement, or official employer first.
3. Define the exact metric: minimum rate, pay scale, median, mean, percentile range, posted range, or total cash earnings.
4. Check the source archive or same-series listing before calling the figure latest.
5. Record search date, data period, publication/update date, geography, role scope, employment type, and source status.
6. Separate base pay from night, weekend, overtime, bonus, housing, relocation, pension, insurance, and other allowances.
7. Use a second source when the first source is broad, old, employer-specific, or based on a small sample.
8. If converting currencies, show the original currency first and label the conversion as an approximate reference using a dated exchange rate.

## Required Output

Keep this section brief unless the user asks for a detailed compensation comparison:

```markdown
## 薪资现实

| 口径 | 当前可核验水平 | 这代表什么 |
|---|---|---|
| 地区/岗位/经验层级 | 原币金额或薪级范围；税前/税后；时薪/月薪/年薪 | 基本工资、总现金收入或岗位报价 |

- 可能另外增加：夜班、周末、加班、地区或岗位津贴；没有官方依据时不估算。
- 不能直接当成“到手”：税、社保、养老金、工时和个人排班会改变结果。
- 对这个用户的意义：用 1-2 句话说明收入与前期成本、准备年限和工作强度是否匹配。
```

When comparing paths, add one compact column or row for pay only if the role, location, and evidence scope are comparable. Do not rank countries by raw salary alone.

## Interpretation Rules

- Always label gross versus net. If the source uses "average wage" that includes withheld tax or social contributions, explain that it is not take-home pay.
- Label hourly, weekly, monthly, and annual figures. Do not convert between them without stating the work-hour assumption.
- Preserve median, mean, percentile, minimum scale, and posted range as different concepts.
- A public pay scale is a contractual floor or scale, not proof that every employer pays the same amount.
- A salary survey is a population estimate, not a personal offer.
- An active vacancy is a single-employer snapshot, not a market average.
- Overseas gross salary must not be presented as Chinese disposable income. Mention tax and essential living-cost differences when they materially affect the user's decision, but do not turn every answer into a full cost-of-living report.
- Higher pay may reflect night work, overtime, agency instability, scarce specialties, seniority, or high-cost locations. State the tradeoff when the evidence supports it.
- For non-clinical roles, do not use bedside-RN wage data unless the role genuinely shares the same occupation code or pay scale.

## Fallback

If exact current role-level evidence cannot be found:

1. Say which official sources and exact role terms were checked.
2. State: `本次未核验到该城市、该岗位、该经验层级的当前可靠薪资数据。`
3. If useful, provide a broader occupation, industry, or region figure labelled as background only.
4. List the missing evidence: current vacancy, pay scale, collective agreement, employer HR confirmation, or occupational dataset.
5. Do not invent a range by averaging agency claims or social posts.

## Official Starting Points

These are search starting points, not permanent salary facts. Recheck the current release and exact occupational scope at answer time.

- China: National Bureau of Statistics employment and wage releases and methodology, `https://www.stats.gov.cn/zs/tjws/zytjzbqs/dwjyry/`. National or industry averages are usually not nurse-specific; use current official employer postings or applicable public pay documents for a named role where available.
- United States: Bureau of Labor Statistics Occupational Employment and Wage Statistics, `https://www.bls.gov/oes/`.
- Australia: Fair Work Ombudsman pay guides, `https://www.fairwork.gov.au/pay-and-wages/minimum-wages/pay-guides`, plus Australian Bureau of Statistics employee earnings, `https://www.abs.gov.au/statistics/labour/earnings-and-working-conditions/employee-earnings-and-hours-australia/latest-release`.
- United Kingdom: NHS Employers current Agenda for Change pay resources and historical pay library, `https://www.nhsemployers.org/historical-pay-library`. Keep England, Scotland, Wales, Northern Ireland, NHS, and private employers separate.
- Ireland: HSE consolidated pay scales, `https://healthservice.hse.ie/staff/pay/pay-scales/`.
- Germany: Federal Employment Agency Entgeltatlas, `https://web.arbeitsagentur.de/entgeltatlas/`, and the applicable collective agreement or employer scale.
- Japan: MHLW Basic Survey on Wage Structure listing, `https://www.mhlw.go.jp/toukei/list/chinginkouzou_a.html`, and MHLW job tag occupation pages, `https://shigoto.mhlw.go.jp/`.
- Poland: Statistics Poland occupational wage structure releases, `https://stat.gov.pl/en/topics/labour-market/working-employed-wages-and-salaries-cost-of-labour/`.
- Croatia: Croatian Bureau of Statistics employment and earnings releases, `https://podaci.dzs.hr/`.
- Philippines: Philippine Statistics Authority Occupational Wages Survey, `https://psa.gov.ph/statistics/occupational-wages-survey`.
- Singapore: Ministry of Manpower Occupational Wages tables, `https://stats.mom.gov.sg/`.
- Malaysia: Department of Statistics Malaysia salary and wage releases, `https://www.dosm.gov.my/`, and OpenDOSM formal-sector wage data, `https://open.dosm.gov.my/dashboard/formal-sector-wages`.
- France, other EU countries, and named employers: start with the national statistics office, current public-sector pay scale or collective agreement, and dated official employer vacancies. Do not substitute a whole-economy average for the requested nursing role.

## Prohibited Claims

Do not:

- promise a salary, pay rise, bonus, overtime volume, or take-home amount
- call gross salary "到手"
- present an average as what the user will personally earn
- combine base pay, overtime, bonuses, and allowances without labelling them
- convert a foreign annual salary to RMB and imply equivalent purchasing power
- use one old vacancy, agency brochure, influencer post, or anonymous self-report as a current market range
- say a high salary makes registration, employment, visa, or immigration likely
- use "高薪逆袭" or salary alone as the reason to recommend a path
