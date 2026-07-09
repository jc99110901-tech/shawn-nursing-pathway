# Bailian Agent Adapter

Use this guide to adapt Shawn Nursing Pathway to Bailian-style agent applications.

This file is intentionally cautious. It does not claim an official import package or one-click setup.

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
- next-step navigation

Then retrieve only the relevant knowledge content and produce a bounded answer.

## Safety Requirement

Keep the safety boundary visible in the agent configuration. The agent must not promise admission, employment, visa, licensure, or immigration.
