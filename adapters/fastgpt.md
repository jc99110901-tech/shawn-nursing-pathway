# FastGPT Adapter

Use this guide to adapt SNP Skill to FastGPT-like knowledge-base and workflow agents.

## 1 分钟版

1. 把 [`Lite 中文单文件`](../dist/shawn-nursing-pathway-lite.md) 放入系统提示词。
2. 把 [`Full 知识库单文件`](../dist/shawn-nursing-pathway-full.md) 作为 Markdown 文档上传知识库。
3. 把知识库关联到对话应用并测试。

FastGPT 官方文档确认知识库可上传 Markdown 等本地文件。

官方说明：[快速上手](https://doc.fastgpt.io/zh-CN/guide/getting-started/quick-start)

## Suggested Setup

- System prompt: `universal/system-prompt.md`
- Knowledge base files:
  - `universal/knowledge-base.md`
  - `universal/safety-boundary.md`
  - selected files from `skills/shawn-nursing-pathway/references/`
- Workflow logic: `universal/workflow.md`
- Output examples: `universal/output-templates.md`

## Suggested Routing

Create a first node that classifies the user request into one of:

- 护理适配
- 路径探索
- 选定方向后的单步规划
- 护理知识和职业英语学习
- 岗位、工作场景和薪资现实
- JD、申请和面试准备
- 当前事实核验
- 澳洲 OBA/IQNM 初筛
- 日本护士/介护/SSW 分流

Then retrieve the matching knowledge chunk only.

## Caution

Do not use a giant always-on knowledge prompt. If all references are injected at once, answers may become too long and less useful.

For Australia OBA/IQNM questions, retrieve only the Australia path, official source map, user segmentation, safety boundary, and OBA output template.

For Japan questions, retrieve only the Japan path, scenario cards, official source map, safety boundary, and Japan triage template.
