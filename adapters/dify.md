# Dify Adapter

Use this guide to adapt Shawn Nursing Pathway to a Dify application.

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
   - next-step navigation
2. Collect missing profile fields.
3. Retrieve only the relevant knowledge files.
4. Generate the answer with boundary reminders and risk notes.
5. End with 2-3 next actions.

## Retrieval Note

Avoid loading every reference for every question. Nursing fit, country paths, school verification, and safety boundaries should be retrieved according to user intent.
