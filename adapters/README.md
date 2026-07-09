# Platform Adapters

These files explain how to adapt Shawn Nursing Pathway to non-Codex AI platforms.

This repository does not promise one-click import for any platform. Each platform has different support for system prompts, knowledge bases, workflow nodes, tools, and retrieval settings.

Recommended mapping:

- System prompt: `universal/system-prompt.md`
- Knowledge base: `universal/knowledge-base.md` plus selected files from `skills/shawn-nursing-pathway/references/`
- Workflow or orchestration: `universal/workflow.md`
- Output format: `universal/output-templates.md`
- Safety boundary: `universal/safety-boundary.md`

If a platform supports file-based knowledge import, import the universal files first. Then add the detailed `references/` files only if the platform can keep retrieval scoped and source-aware.

For Australia OBA/IQNM questions, make sure the platform can retrieve:

- `universal/knowledge-base.md`
- `universal/output-templates.md`
- `skills/shawn-nursing-pathway/references/country-paths.md`
- `skills/shawn-nursing-pathway/references/official-source-map.md`
- `skills/shawn-nursing-pathway/references/user-segmentation.md`

The agent should treat OBA as a registration-path screening topic, not as a study-abroad shortcut or agency recommendation.

For Japan questions, make sure the platform can retrieve:

- `universal/knowledge-base.md`
- `universal/output-templates.md`
- `skills/shawn-nursing-pathway/references/country-paths.md`
- `skills/shawn-nursing-pathway/references/country-scenario-cards.md`
- `skills/shawn-nursing-pathway/references/official-source-map.md`

The agent should split Japanese nurse, nursing study, caregiving, and SSW nursing care before giving path advice.
