# 1 分钟开始使用

本仓库以 GitHub `main` 分支作为公开发行真源。普通用户不需要理解 Codex Skill 的目录结构，只需要根据使用场景选择一个文件。

## 最简单的选择

| 使用场景 | 使用文件 | 最少操作 |
|---|---|---|
| 豆包、千问或其他普通 AI 对话 | [`shawn-nursing-pathway-lite.md`](dist/shawn-nursing-pathway-lite.md) | 上传文件，发送“请按文件规则回答我的问题” |
| 扣子、Dify、FastGPT、MaxKB、百炼等知识库平台 | [`shawn-nursing-pathway-full.md`](dist/shawn-nursing-pathway-full.md) | 导入一个知识库文件，再把 Lite 文件设为角色提示词 |
| WorkBuddy / 腾讯云智能体开发平台 | [`shawn-nursing-pathway-workbuddy.zip`](dist/shawn-nursing-pathway-workbuddy.zip) | 在自定义 Skills 中上传 ZIP |
| Codex | [`skills/shawn-nursing-pathway/`](skills/shawn-nursing-pathway/) | 复制到 `~/.codex/skills/` |

## 手机聊天版

1. 下载 [`Lite 单文件`](dist/shawn-nursing-pathway-lite.md)。
2. 在支持文件上传的 AI 对话里上传它。
3. 发送：

```text
请把我上传的 Shawn Nursing Pathway 文件作为本次对话规则。先判断我的问题属于哪个模块；缺少关键信息时只问最少的问题，不要替我做最终决定。
```

如果当前 App 不支持上传 Markdown 文件，打开 Lite 文件，复制全文到一段新对话中即可。

## 知识库工作台版

最低配置：

1. 把 Lite 文件放进“系统提示词、角色设定或指令”。
2. 把 Full 文件上传到知识库。
3. 用下面问题测试：

```text
孩子高考分数一般，家长觉得护理稳定，孩子不太愿意。先做护理适配初筛，不要替我们决定。
```

只有在平台明确支持工作流时，才继续配置 `universal/workflow.md`。第一轮使用不需要先搭工作流。

## 最新版固定链接

以下 URL 始终指向 GitHub `main` 分支的当前版本：

```text
https://raw.githubusercontent.com/jc99110901-tech/shawn-nursing-pathway/main/dist/shawn-nursing-pathway-lite.md
https://raw.githubusercontent.com/jc99110901-tech/shawn-nursing-pathway/main/dist/shawn-nursing-pathway-full.md
https://raw.githubusercontent.com/jc99110901-tech/shawn-nursing-pathway/main/dist/shawn-nursing-pathway-workbuddy.zip
https://raw.githubusercontent.com/jc99110901-tech/shawn-nursing-pathway/main/dist/manifest.json
```

## 更新规则

- 能直接引用 URL 并支持重新同步的平台，可以继续使用上述固定 URL。
- 下载后再上传的平台，上传的是一个版本快照；仓库更新后需要重新下载并替换。
- GitHub 无法主动修改用户在第三方平台里已经上传的旧文件。
- `dist/manifest.json` 提供当前版本、发布日期和文件哈希，可用于检查是否需要更新。

## 隐私提醒

不要上传身份证号、准考证号、完整成绩截图、护照号、银行信息、未脱敏合同或私人医疗记录。
