# Coze / Kouzi Adapter

Use this guide to adapt Shawn Nursing Pathway to Coze-like bot builders.

## Suggested Setup

- Bot role or system instruction: use `universal/system-prompt.md`
- Knowledge files: import `universal/knowledge-base.md`, `universal/safety-boundary.md`, and selected `references/` files
- Conversation flow or workflow: follow `universal/workflow.md`
- Response style: use `universal/output-templates.md`

## Suggested Bot Capabilities

Create clear user entry points:

- 护理适配
- 志愿复核
- 海外路径
- 学校/费用核验
- 机构话术核验
- 下一步规划
- 澳洲 OBA/IQNM 初筛

## Safety Notes

Do not configure the bot to promise admission, employment, visa, licensure, or immigration. If browsing or official-source checking is unavailable, the bot should output a verification checklist instead of current facts.

For Australia OBA/IQNM, the bot should split Self-check, Stream A/B/C, Portfolio, MCQ/NCLEX-RN, OSCE, Registration, Visa, Employment, and ANMAC instead of recommending a provider.
