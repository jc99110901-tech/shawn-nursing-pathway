# Multi-Perspective Review

Execute this module when the user explicitly asks for different viewpoints, a panel-style discussion, a consultation, or a stress test of an earlier answer, and has either named the perspectives or confirmed the proposed perspectives.

This is an internal module of `shawn-nursing-pathway`, not a separate public entry. Do not use it for a simple factual lookup.

## Contents

- Entry Conditions
- Role Selection
- Confirmation Rule
- Shared Evidence Brief
- Independent Agent Execution
- Single-Model Fallback
- Moderator Synthesis
- Safety and Quality Checks

## Entry Conditions

Execute this module when at least one condition is true:

- The user explicitly says "多视角看看", "帮我会诊", "让几个角色讨论", or similar.
- The user asks to stress-test an earlier recommendation.
- The user previously accepted a suggested multi-perspective review.

Offer this module, but do not execute it yet, when the user has not requested it and:

- The user is choosing between paths whose tradeoffs involve different values, such as stability versus autonomy, domestic versus overseas life, or short-term cost versus long-term optionality.
- A parent and student disagree about nursing.

In that case, explain why 3-5 perspectives may help, propose the perspectives, and wait for consent.

Do not use it when:

- The task is one school fee, one policy clause, one application date, or another bounded fact.
- The user only needs the ordinary nursing-fit or pathway-screening workflow.
- The available profile is too thin for the roles to say anything beyond generic advice. Ask the minimum blocking questions first.

## Role Selection

Choose 3-5 perspectives dynamically. Do not automatically use every role.

Candidate perspectives:

| Perspective | Owns this decision dimension |
|---|---|
| 护理临床现实视角 | Direct-care duties, shifts, patient contact, physical/emotional load, and bedside tolerance; exclude employer-market claims |
| 升学与学历路径视角 | Formal study sequence, credential utility, admissions assumptions, and academic alternatives; exclude household cash flow |
| 执照与政策核验视角 | Regulator layers, current official rules, source status, and unresolved official requirements; exclude general downside analysis |
| 家庭预算与机会成本视角 | Household cash flow, total cost, income interruption, time horizon, and loss-bearing capacity; exclude academic value judgments |
| 职业发展与用人视角 | Role families, transferable skills, job-description evidence, and realistic transition steps; exclude bedside tolerance |
| 海外生活与家庭适配视角 | Language, relocation, support network, family obligations, and daily-life tolerance |
| 学生自主与家庭沟通视角 | Student willingness, parent expectations, consent, and conflict that facts alone cannot resolve |
| 风险审查视角 | Provider promises, irreversible commitments, hidden assumptions, worst-case loss, and exit options; use only when these are prominent |

Before choosing a role, answer:

1. What unique question does this role own?
2. Which other role would duplicate it?
3. What important risk would disappear if this role were removed?

Drop any role that cannot pass this test. Use role labels, not celebrity names or impersonations of real professionals.

Potentially overlapping pairs may be used together only when their ownership is stated narrowly:

- 护理临床现实 only evaluates the work itself; 职业发展与用人 only evaluates role transition and employer evidence.
- 升学与学历路径 only evaluates academic structure; 家庭预算与机会成本 only evaluates money, time, and downside capacity.
- 执照与政策核验 only evaluates official rules and source status; 风险审查 only evaluates claims, irreversible action, worst-case loss, and exit options.

## Confirmation Rule

If the user requests a multi-perspective review but does not name roles, or if the skill only detects a conflict and wants to offer this mode:

1. Propose 3-5 relevant role perspectives.
2. Give one sentence explaining what each role will examine.
3. Wait for "开始", "确认", or role changes.

If the user names the roles, confirms the proposed roles, or says "直接开始/不用确认", proceed immediately.

Do not force a confirmation step when the user has already made their preference clear.

## Shared Evidence Brief

The main agent prepares one shared brief before role execution:

```markdown
用户问题：

用户画像：
- 已确认：
- 尚不确定：

共同事实：
| 事实 | 来源主体 | 检索日期 | 数据/规则适用期 | 发布或更新日期 | 时效状态 |
|---|---|---|---|---|---|
| ... | ... | YYYY-MM-DD | ... | YYYY-MM-DD / 官网未标日期 | ... |

- 未核验或未找到的事实：

本轮暂用假设：

产品边界：
- 不做最终决定。
- 不承诺录取、就业、签证、执照或移民。
```

For dynamic facts, load `current-information-protocol.md` and complete the official-source check before the roles reason from them. Every role receives the same brief.

Roles may challenge an assumption or identify a missing fact. They must not silently add uncited current policies, fees, salaries, vacancies, school claims, or market data.

## Independent Agent Execution

When independent Agent tools are available, launch one agent per role in parallel. Do not reveal another role's draft or the intended moderator conclusion.

Use this role prompt:

```text
你负责“{角色名称}”这一项分析视角。你不是现实中的持证专家、官方代表、学校内部人员或雇主。

用户问题：
{question}

共同用户画像与证据简报：
{evidence_brief}

你只负责：
{owned_dimension}

请输出：
1. 核心判断
2. 最强依据
3. 最大风险
4. 什么新信息会改变你的判断
5. 下一项最值得核验的问题

只使用共同证据简报中的动态事实；可以指出事实不足，但不要补造新数据。不要替用户做最终决定，不要承诺结果，不要推荐或背书机构。控制在 150-250 个中文字符。
```

If one role fails, report that role as unavailable or rerun it once. Do not fabricate its response.

## Single-Model Fallback

If independent Agent tools are unavailable, the main agent may use the same role structure, but must state:

> 当前平台未调用独立 Agent；以下为单模型多视角模拟，不代表真实专家会诊。

Do not describe this fallback as independent debate, expert consensus, or a multidisciplinary consultation.

## Moderator Synthesis

After all role responses are available, the main agent acts as moderator. Preserve differences instead of blending every view into one smooth answer.

The moderator uses the same shared evidence brief and must not introduce a new dynamic fact that the roles did not receive. If a new fact becomes necessary, pause synthesis, verify it under `current-information-protocol.md`, update the brief, and make the update visible.

The moderator must output:

- 共识：roles agree because they rely on the same constraint or evidence.
- 真正分歧：which values, assumptions, or time horizons produce different judgments.
- 容易忽略的盲点：a material dimension none of the initial framing handled well.
- 决策关键变量：the 2-4 facts or preferences most likely to change the direction.
- 建议先做的事：2-3 reversible, evidence-producing actions.
- 不建议现在做的事：irreversible or costly action that is premature.

Do not:

- count votes
- rank the roles
- announce a winner
- turn consensus into a final volunteer ranking or career command
- erase an unresolved disagreement

## Safety and Quality Checks

Before sending the answer, verify:

- There are 3-5 roles and each owns a distinct dimension.
- The user can see whether this was independent-agent analysis or a single-model simulation.
- Dynamic facts share one freshness-checked evidence brief.
- Facts, assumptions, and value judgments are labelled separately.
- No role claims to be a real professional or official representative.
- No role promises admission, graduation, employment, salary, visa, licensure, long-term residence, or immigration.
- The moderator gives decision variables and next verification steps, not a final decision.
