# MaxKB Adapter

Use this guide to adapt SNP Skill to MaxKB-like knowledge-base agents.

## 1 分钟版

1. 把 [`Lite 中文单文件`](../dist/shawn-nursing-pathway-lite.md) 放入应用角色设定。
2. 创建通用型知识库并上传 [`Full 知识库单文件`](../dist/shawn-nursing-pathway-full.md)。
3. 关联知识库后直接测试。

MaxKB 官方文档确认通用型知识库支持 Markdown 文件；Web 站点知识库支持 URL 文档和手动同步。使用 Raw URL 前先在自己的部署中测试抓取结果。

官方说明：[知识库](https://maxkb.cn/docs/v2/user_manual/dataset/dataset/)、[文档同步](https://maxkb.cn/docs/v2/user_manual/dataset/doclist/)

## Suggested Setup

- Use `universal/system-prompt.md` as the main role instruction.
- Add `universal/knowledge-base.md` and `universal/safety-boundary.md` to the knowledge base.
- Add selected files from `skills/shawn-nursing-pathway/references/` if the workspace can keep retrieval accurate.
- Use `universal/output-templates.md` as response-format guidance.

## Suggested Knowledge Tags

If the platform supports tags or categories, group content as:

- safety boundary
- user segmentation
- nursing fit
- domestic pathway
- country pathway
- chosen-path planning
- adaptive nursing and English learning
- career and salary reality
- job and interview readiness
- school and fee verification
- provider claim review
- Australia OBA/IQNM screening
- Japan nurse/caregiving/SSW triage
- output templates

## Caution

Do not treat retrieved school or policy information as permanent. Current operational facts still need official verification.

For Australia OBA/IQNM, current Ahpra/NMBA/ANMAC rules should be treated as operational facts that require official verification.

For Japan triage, current MHLW, SSW, Prometric, employer, Certificate of Eligibility, status of residence, and visa rules should be treated as operational facts that require official verification.
