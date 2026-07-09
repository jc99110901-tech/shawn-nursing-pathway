# Generic Agent Adapter

Use this guide for any AI platform that supports custom prompts or knowledge files.

## Minimal Setup

1. Paste `universal/system-prompt.md` into the system prompt.
2. Add `universal/knowledge-base.md` as knowledge.
3. Add `universal/safety-boundary.md` as a permanent safety instruction.
4. Use `universal/workflow.md` as the conversation flow.
5. Use `universal/output-templates.md` for answer formatting.

## Recommended Retrieval Setup

If the platform supports retrieval:

- Split knowledge by module.
- Retrieve only relevant content.
- Keep official-source and safety-boundary material available for school, fee, provider, policy, licensing, visa, and immigration questions.

## Minimal Test Prompts

```text
孩子高考分数一般，护理能不能报？
```

```text
菲律宾宿务护理路径值得了解吗？
```

```text
中介说读完护理包就业包移民，可信吗？
```

```text
澳洲护理学费和学校应该怎么查？
```

## Expected Behavior

The agent should not rush to a final answer. It should clarify user profile, separate education/license/job/visa/immigration layers, flag risks, and provide the next official checks.
