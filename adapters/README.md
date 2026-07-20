# 国内外 AI 平台适配

GitHub 仓库是唯一公开发行源。平台适配器只解释“怎样读取同一份仓库内容”，不另外维护一套业务逻辑。

## 先选最低门槛

| 平台 | 最低门槛方式 | 能否保持自动更新 |
|---|---|---|
| Codex | 安装 `skills/shawn-nursing-pathway/` | 本地需重新拉取或更新仓库 |
| WorkBuddy / 腾讯云智能体开发平台 | 上传 `dist/shawn-nursing-pathway-workbuddy.zip` | 自定义 Skill 需按新版本重新上传 |
| 豆包手机端 | 普通对话上传或粘贴 Lite 文件 | 否 |
| 千问手机端 | 普通对话上传或粘贴 Lite 文件 | 否 |
| 扣子 / Coze | Lite 作为角色指令，Full 作为知识库 | 取决于平台是否支持 URL 重抓取 |
| 百炼 | Lite 作为 Prompt，Full 作为知识库 | 文件上传模式需重新导入 |
| Dify | Lite 作为 Instructions，Full 作为 Knowledge | 文件上传模式需重新导入 |
| FastGPT | Lite 作为系统提示词，Full 作为知识库 | 文件上传模式需重新导入 |
| MaxKB | Lite 作为角色设定，Full 作为知识库 | Web 文档可手动同步；文件需重新导入 |
| 其他 AI 平台 | 上传或粘贴 Lite 文件 | 取决于平台 |

## 三个固定发行文件

- [`Lite 中文单文件`](../dist/shawn-nursing-pathway-lite.md)：手机聊天、系统提示词和第一次试用。
- [`Full 知识库单文件`](../dist/shawn-nursing-pathway-full.md)：需要完整 references 的知识库平台。
- [`WorkBuddy Skill ZIP`](../dist/shawn-nursing-pathway-workbuddy.zip)：支持原生 Skill ZIP 的腾讯云智能体开发平台。

固定 Raw URL：

```text
https://raw.githubusercontent.com/jc99110901-tech/shawn-nursing-pathway/main/dist/shawn-nursing-pathway-lite.md
https://raw.githubusercontent.com/jc99110901-tech/shawn-nursing-pathway/main/dist/shawn-nursing-pathway-full.md
https://raw.githubusercontent.com/jc99110901-tech/shawn-nursing-pathway/main/dist/shawn-nursing-pathway-workbuddy.zip
```

## 自动更新的真实边界

- 平台在每次运行时读取 Raw URL，或知识库支持重新抓取 URL，才能取得 GitHub 当前版本。
- 用户下载再上传的文件是快照，不会因为 GitHub 更新而自动变化。
- 不要声称任何平台支持未经官方确认的一键导入或后台自动同步。
- 可读取 [`../dist/manifest.json`](../dist/manifest.json) 比较版本和 SHA-256。

## 高级组合

只有需要精细配置时，才使用：

- System prompt：`universal/system-prompt.md`
- Knowledge base：`universal/knowledge-base.md` 和选定 references
- Workflow：`universal/workflow.md`
- Output format：`universal/output-templates.md`
- Safety：`universal/safety-boundary.md`

普通用户不需要先理解这些文件。
