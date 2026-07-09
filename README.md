# Shawn Nursing Pathway Skill

中文优先的护理升学与海外护理路径智能体提示词包。  
A Chinese-first Codex skill and universal agent prompt package for nursing education, gaokao nursing fit, and overseas nursing pathway screening.

## 一句话说明

面向中国普通家庭，帮助用户初步判断：高考志愿是否考虑护理、自己或孩子是否适合护理、国内外护理路径如何比较、学校/费用/机构话术如何核验。

English: A Codex skill for nursing education, gaokao nursing fit, and overseas nursing pathway screening.

## 图文案例 / Illustrated Cases

这些案例展示真实用户会如何使用这个 Skill。案例是中文优先，中英文配套。

### 案例 1：高考家长问护理能不能报

![高考家长护理适配案例](assets/case-cards/case-01-gaokao-nursing-fit.svg)

完整案例：[`examples/case-01-gaokao-nursing-fit.md`](examples/case-01-gaokao-nursing-fit.md)

### 案例 2：澳洲登记护士、注册护士和护工有什么区别

![澳洲 EN RN 护工区别案例](assets/case-cards/case-02-australia-en-rn-care-worker.svg)

完整案例：[`examples/case-02-australia-en-rn-care-worker.md`](examples/case-02-australia-en-rn-care-worker.md)

### 案例 3：日本护理和介护有什么区别

![日本护理和介护路径区分案例](assets/case-cards/case-03-japan-nursing-caregiving.svg)

完整案例：[`examples/case-03-japan-nursing-caregiving.md`](examples/case-03-japan-nursing-caregiving.md)

## 适用场景 / Use Cases

- 高考志愿里是否选择护理
- 护理适配度初筛
- 国内专科、本科、中外合作路径比较
- 菲律宾/宿务、日本、德国、美国 RN、澳洲、欧洲等护理路径初筛
- 志愿方案复核
- 学校、费用、机构话术核验

English:

- Whether to choose nursing in gaokao volunteer planning
- First-pass nursing fit assessment
- Domestic junior-college, bachelor, and Sino-foreign nursing pathway comparison
- First-pass screening for Philippines/Cebu, Japan, Germany, US RN, Australia, Europe, and other nursing-related pathways
- Volunteer plan review checklist
- School, tuition, and provider-claim verification

## 免责声明 / Disclaimer

本项目是公开信息整理、路径解释、适配度初筛和风险复核工具。它不做以下事情：

- 不预测录取结果
- 不输出最终志愿排序
- 不承诺录取、就业、签证、执照或移民
- 不代表官方、学校、雇主、机构或内部渠道
- 不替代考试院、学校官网、执照机构、移民部门或专业人士意见

用户应以考试院、学校官网、护理监管机构、执照机构、移民部门等官方最新文件为准。

English: This project is an information-organization and risk-review tool. It does not predict admission, rank final volunteer choices, promise admission, employment, visas, licensure, or immigration outcomes, or represent any official body, school, employer, agency, or internal channel.

## Codex 安装方式 / Install for Codex

将 Codex 原生 Skill 复制到本地 Codex skills 目录：

```bash
cp -R skills/shawn-nursing-pathway ~/.codex/skills/
```

或者将 `skills/shawn-nursing-pathway/` 安装到任何 Codex 支持的 skills 目录中。

安装后请重启 Codex，或开启新会话以刷新技能列表。

## 非 Codex 平台使用 / Use Outside Codex

这个仓库不只服务 Codex。

- Codex 用户使用 `skills/shawn-nursing-pathway/`
- 其他 AI 平台用户使用 `universal/`
- 平台适配说明见 `adapters/`
- 国内 AI 平台可以把本仓库当作“护理路径智能体提示词包”，而不是只当 Codex Skill

不承诺所有平台都能一键导入。不同平台对系统提示词、知识库、工作流、工具调用和检索配置的支持不同。

English:

- Codex users should use `skills/shawn-nursing-pathway/`.
- Other AI platform users can use the files in `universal/`.
- Platform-specific adaptation notes are in `adapters/`.
- Domestic AI platforms can treat this repository as a nursing-pathway agent prompt package.

## 使用示例 / Example Prompts

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

## 文件结构 / Repository Structure

```text
shawn-nursing-pathway/
├── README.md
├── LICENSE
├── .gitignore
├── assets/
│   └── case-cards/
│       └── ...
├── examples/
│   ├── README.md
│   └── case-*.md
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

## 公开安全说明 / Public Safety

本仓库不包含 Shawn 工作台私人文件、私人生活信息、内部服务设计、未确认学校合作关系或商业内部资料。

如果真实部署中存在学校、雇主、机构、代理、佣金、服务费或合作关系，应向用户透明披露。本仓库本身不验证、暗示或代表任何此类关系。

This project does not constitute legal, immigration, education, medical, psychological, career, or financial advice, and it does not provide any admission, employment, visa, license, or immigration guarantee.
