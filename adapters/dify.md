# Dify Adapter

Use this guide to adapt Shawn Nursing Pathway to a Dify application.

## 1 分钟版

1. 把 [`Lite 中文单文件`](../dist/shawn-nursing-pathway-lite.md) 放入 Instructions。
2. 把 [`Full 知识库单文件`](../dist/shawn-nursing-pathway-full.md) 上传到 Knowledge。
3. 关联知识库后直接测试，不需要第一天就搭 Workflow。

## Suggested Setup

- Instructions / system prompt: `universal/system-prompt.md`
- Knowledge base: `universal/knowledge-base.md`, `universal/safety-boundary.md`, and selected `skills/shawn-nursing-pathway/references/`
- Workflow app: implement the routing steps from `universal/workflow.md`
- Answer format: use `universal/output-templates.md`

## Suggested Workflow Nodes

1. Classify user intent:
   - nursing fit
   - volunteer review
   - overseas path comparison
   - school/fee verification
   - provider-claim verification
   - Australia OBA/IQNM screening
   - Japan nurse/caregiving/SSW triage
   - next-step navigation
2. Collect missing profile fields.
3. Retrieve only the relevant knowledge files.
4. Generate the answer with boundary reminders and risk notes.
5. End with 2-3 next actions.

## Retrieval Note

Avoid loading every reference for every question. Nursing fit, country paths, school verification, and safety boundaries should be retrieved according to user intent.

For Australia OBA/IQNM screening, retrieve country paths, official source map, user segmentation, output templates, and safety boundary together.

For Japan triage, retrieve country paths, country scenario cards, official source map, output templates, and safety boundary together.
