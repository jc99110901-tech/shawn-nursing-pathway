# MaxKB Adapter

Use this guide to adapt Shawn Nursing Pathway to MaxKB-like knowledge-base agents.

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
- school and fee verification
- provider claim review
- Australia OBA/IQNM screening
- output templates

## Caution

Do not treat retrieved school or policy information as permanent. Current operational facts still need official verification.

For Australia OBA/IQNM, current Ahpra/NMBA/ANMAC rules should be treated as operational facts that require official verification.
