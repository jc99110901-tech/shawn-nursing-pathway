# Bailian Agent Adapter

Use this guide to adapt Shawn Nursing Pathway to Bailian-style agent applications.

This file is intentionally cautious. It does not claim an official import package or one-click setup.

## 1 分钟版

1. 新建百炼智能体应用。
2. 把 [`Lite 中文单文件`](../dist/shawn-nursing-pathway-lite.md) 放入 Prompt。
3. 需要完整资料时，把 [`Full 知识库单文件`](../dist/shawn-nursing-pathway-full.md) 上传为知识库文档。

先完成这 3 步即可测试，不需要先画工作流。

## Suggested Setup

- System instruction: `universal/system-prompt.md`
- Knowledge base: `universal/knowledge-base.md`, `universal/safety-boundary.md`, and relevant `references/`
- Workflow or orchestration: `universal/workflow.md`
- Response format: `universal/output-templates.md`

## Suggested Agent Behavior

The agent should first classify the user's intent:

- nursing fit
- volunteer plan review
- overseas pathway screening
- school or fee verification
- provider claim verification
- Australia OBA/IQNM screening
- Japan nurse/caregiving/SSW triage
- next-step navigation

Then retrieve only the relevant knowledge content and produce a bounded answer.

## Safety Requirement

Keep the safety boundary visible in the agent configuration. The agent must not promise admission, employment, visa, licensure, or immigration.

For Australia OBA/IQNM, do not configure the agent to recommend a training provider. The agent should ask for education, registration status, clinical experience, English, document traceability, OSCE feasibility, and final goal.

For Japan triage, do not configure the agent to recommend a school, employer, or agency before clarifying whether the user means Japanese nurse, nursing study, caregiving, or SSW nursing care.

百炼当前官方文档支持智能体、工作流和知识库；多视角模式可在平台明确支持智能体群组时再做进阶配置。

官方说明：[应用类型介绍](https://help.aliyun.com/zh/model-studio/application-introduction)、[知识库](https://help.aliyun.com/zh/model-studio/rag-knowledge-base)
