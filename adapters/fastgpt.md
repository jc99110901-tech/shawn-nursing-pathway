# FastGPT Adapter

Use this guide to adapt Shawn Nursing Pathway to FastGPT-like knowledge-base and workflow agents.

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
- 志愿复核
- 海外路径比较
- 学校/费用核验
- 机构话术核验
- 澳洲 OBA/IQNM 初筛
- 日本护士/介护/SSW 分流
- 下一步规划

Then retrieve the matching knowledge chunk only.

## Caution

Do not use a giant always-on knowledge prompt. If all references are injected at once, answers may become too long and less useful.

For Australia OBA/IQNM questions, retrieve only the Australia path, official source map, user segmentation, safety boundary, and OBA output template.

For Japan questions, retrieve only the Japan path, scenario cards, official source map, safety boundary, and Japan triage template.
