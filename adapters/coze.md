# Coze / Kouzi Adapter

Use this guide to adapt SNP Skill to Coze-like bot builders.

## 1 分钟版

1. 把 [`Lite 中文单文件`](../dist/shawn-nursing-pathway-lite.md) 放入角色设定或系统指令。
2. 平台支持知识库文件时，上传 [`Full 知识库单文件`](../dist/shawn-nursing-pathway-full.md)。
3. 先测试，再决定是否配置工作流。

不要把 GitHub 仓库描述成未经官方确认的一键导入包。

## Suggested Setup

- Bot role or system instruction: use `universal/system-prompt.md`
- Knowledge files: import `universal/knowledge-base.md`, `universal/safety-boundary.md`, and selected `references/` files
- Conversation flow or workflow: follow `universal/workflow.md`
- Response style: use `universal/output-templates.md`

## Suggested Bot Capabilities

Create clear user entry points:

- SNP Fit：护理适配
- SNP Explore：路径探索
- SNP Plan：选定方向后的单步规划
- SNP Learn：护理知识和职业英语学习
- SNP Career：岗位、工作场景和薪资现实
- SNP Interview：JD、申请和面试准备
- SNP Verify：当前事实核验
- 澳洲 OBA/IQNM 初筛
- 日本护士/介护/SSW 分流

## Safety Notes

Do not configure the bot to promise admission, employment, visa, licensure, or immigration. If browsing or official-source checking is unavailable, the bot should output a verification checklist instead of current facts.

For Australia OBA/IQNM, the bot should split Self-check, Stream A/B/C, Portfolio, MCQ/NCLEX-RN, OSCE, Registration, Visa, Employment, and ANMAC instead of recommending a provider.

For Japan, the bot should split MHLW nurse exam eligibility, nursing study, caregiving, and SSW nursing care before mentioning schools, employers, or visa steps.
