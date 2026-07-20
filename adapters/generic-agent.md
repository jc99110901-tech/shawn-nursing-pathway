# Generic Agent Adapter

Use this guide for any AI platform that supports custom prompts or knowledge files.

## 30 秒版

只上传 [`Lite 中文单文件`](../dist/shawn-nursing-pathway-lite.md)，然后发送：

```text
请按文件中的规则回答。先判断我的问题属于哪个模块，不替我做最终决定。
```

需要完整国家路径和核验资料时，再换成 [`Full 知识库单文件`](../dist/shawn-nursing-pathway-full.md)。

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

```text
我是国内注册护士，想通过澳洲 OBA 去做 RN，第一步该核实什么？
```

```text
日本护理和介护是不是一回事？国内护士想去日本做护士第一步看什么？
```

## Expected Behavior

The agent should not rush to a final answer. It should clarify user profile, separate education/license/job/visa/immigration layers, flag risks, and provide the next official checks.

For Australia OBA/IQNM questions, it should additionally separate Self-check, Stream A/B/C, Portfolio, MCQ/NCLEX-RN, OSCE, Registration, Visa, Employment, and ANMAC.

For Japan questions, it should separate Japanese nurse, nursing study, caregiving, and SSW nursing care, then verify MHLW, Immigration Services Agency, Prometric, school, employer, and visa layers as relevant.
