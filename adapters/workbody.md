# WorkBuddy / 腾讯云智能体开发平台适配

用户有时会把 WorkBuddy 写成 Workbody。本文件指腾讯 WorkBuddy 和腾讯云智能体开发平台。

## 1 分钟版

下载：

[`shawn-nursing-pathway-workbuddy.zip`](../dist/shawn-nursing-pathway-workbuddy.zip)

然后在腾讯云智能体开发平台：

1. 打开“资源中心 > Skills > 自定义 Skills”。
2. 选择新建并上传 ZIP。
3. 如版本号未自动识别，填写仓库 [`release.json`](../release.json) 中的版本号。
4. 等待平台完成格式校验和安全审核。

腾讯云当前官方规范要求 ZIP 小于 10 MB，且 ZIP 根目录包含 `SKILL.md`。本仓库的 WorkBuddy ZIP 按该结构生成。

官方说明：[新建 Skills](https://cloud.tencent.com/document/product/1759/129562)

## 更新

GitHub 是最新版来源，但 WorkBuddy 自定义 Skill 不应被描述为会自动追踪 GitHub。

仓库发布新版本后：

1. 重新下载同一个固定 ZIP 链接。
2. 在 Skill 详情中按更高版本号更新。
3. 重新等待安全审核。

## 没有 Skills 入口时

不同账号、套餐或部署版本可能显示不同功能。看不到自定义 Skills 时，使用：

- [`Lite 中文单文件`](../dist/shawn-nursing-pathway-lite.md) 作为专家规则。
- [`Full 知识库单文件`](../dist/shawn-nursing-pathway-full.md) 作为知识资料。

不要编造当前工作区不存在的导入按钮。
