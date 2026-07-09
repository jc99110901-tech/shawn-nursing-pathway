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
