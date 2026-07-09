# Workbody Adapter

This is a cautious, platform-neutral adaptation guide. It does not claim an official one-click import format.

## If Workbody Supports System Prompts

Copy `universal/system-prompt.md` into the agent's system prompt or role instruction field.

## If Workbody Supports Knowledge Bases

Import:

- `universal/knowledge-base.md`
- `universal/safety-boundary.md`
- selected files from `skills/shawn-nursing-pathway/references/`

Keep source titles visible so the agent can cite which layer it is using: fit, pathway comparison, official source map, school/fee verification, or provider-claim review.

For Australia OBA/IQNM questions, include `country-paths.md`, `official-source-map.md`, `user-segmentation.md`, and `output-templates.md` in retrieval if Workbody supports scoped knowledge files.

For Japan questions, include `country-paths.md`, `country-scenario-cards.md`, `official-source-map.md`, and `output-templates.md` so the agent can split Japanese nurse, nursing study, caregiving, and SSW nursing care.

## If Workbody Supports Workflows

Configure the main workflow from `universal/workflow.md`:

1. front-desk routing
2. profile collection
3. fit/pathway/school/provider module selection
4. risk output
5. next-step navigation

## Do Not Invent Platform Features

If the Workbody workspace does not clearly support a feature, do not describe it as available. Use the generic prompt and knowledge-base approach instead.
