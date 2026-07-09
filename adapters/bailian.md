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
- Australia OBA/IQNM screening
- Japan nurse/caregiving/SSW triage
- next-step navigation

Then retrieve only the relevant knowledge content and produce a bounded answer.

## Safety Requirement

Keep the safety boundary visible in the agent configuration. The agent must not promise admission, employment, visa, licensure, or immigration.

For Australia OBA/IQNM, do not configure the agent to recommend a training provider. The agent should ask for education, registration status, clinical experience, English, document traceability, OSCE feasibility, and final goal.

For Japan triage, do not configure the agent to recommend a school, employer, or agency before clarifying whether the user means Japanese nurse, nursing study, caregiving, or SSW nursing care.
