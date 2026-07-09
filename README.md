# Shawn Nursing Pathway Skill

A Codex skill for nursing education, gaokao nursing fit, and overseas nursing pathway screening.

This repository contains a public, reusable AI-agent skill and prompt package for families and learners who need to understand nursing education choices, nursing fit, domestic nursing pathways, and overseas nursing pathway risks.

## Use Cases

- Whether to choose nursing in gaokao volunteer planning
- First-pass nursing fit assessment
- Domestic junior-college, bachelor, and Sino-foreign nursing pathway comparison
- First-pass screening for Philippines/Cebu, Japan, Germany, US RN, Australia, Europe, and other nursing-related pathways
- Volunteer plan review checklist
- School, tuition, and provider-claim verification

## Disclaimer

This project is an information-organization and risk-review tool. It does not:

- predict admission results
- output final gaokao volunteer rankings
- promise admission, employment, visa approval, licensure, or immigration outcomes
- represent any official body, school, employer, agency, or internal channel
- replace advice from examination authorities, schools, regulators, licensing bodies, immigration authorities, or qualified professionals

Users should verify current facts against the latest official documents from examination authorities, school websites, nursing regulators, licensing boards, immigration departments, and other relevant official sources.

## Install for Codex

Copy the Codex-native skill folder into your Codex skills directory:

```bash
cp -R skills/shawn-nursing-pathway ~/.codex/skills/
```

Or install `skills/shawn-nursing-pathway/` into any Codex-supported skills directory.

After installation, restart Codex or open a new Codex session so the skill list refreshes.

## Use Outside Codex

This repository is not only for Codex.

- Codex users should use `skills/shawn-nursing-pathway/`.
- Other AI platform users can use the files in `universal/` as a general agent prompt package.
- Platform-specific adaptation notes are in `adapters/`.
- Domestic AI platforms can treat this repository as a nursing-pathway agent prompt package, not only as a Codex Skill.

No one-click import is promised. Different platforms support different combinations of system prompts, knowledge bases, workflow nodes, and tools.

## Example Prompts

```text
孩子高考分数一般，护理能不能报？
```

```text
菲律宾宿务护理路径值得了解吗？
```

```text
日本护理和介护有什么区别？
```

```text
中介说包就业包移民可信吗？
```

```text
澳洲护理学校和学费应该怎么查？
```

## Repository Structure

```text
shawn-nursing-pathway/
├── README.md
├── LICENSE
├── .gitignore
├── skills/
│   └── shawn-nursing-pathway/
│       ├── SKILL.md
│       ├── agents/
│       │   └── openai.yaml
│       └── references/
│           └── ...
├── universal/
│   ├── system-prompt.md
│   ├── knowledge-base.md
│   ├── workflow.md
│   ├── output-templates.md
│   └── safety-boundary.md
└── adapters/
    ├── README.md
    ├── workbody.md
    ├── coze.md
    ├── dify.md
    ├── fastgpt.md
    ├── maxkb.md
    ├── bailian.md
    └── generic-agent.md
```

## Public Safety

This repository does not contain private Shawn workspace files, private life information, internal service design, unconfirmed school partnerships, or internal business materials.

If a school, employer, provider, agent, commission, or cooperation relationship exists in a real deployment, it should be disclosed transparently to users. This repository does not itself verify or imply any such relationship.

This project does not constitute legal, immigration, education, medical, psychological, career, or financial advice, and it does not provide any admission, employment, visa, license, or immigration guarantee.
