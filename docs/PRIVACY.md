# 隐私、授权与使用边界 / Privacy, authorization, and use

适用候选：0.1.77（数据流自0.1.75保持一致） · 更新于 2026-10-18。本说明描述当前实现，功能变化时同步更新。

## 中文

VidSage 优先在本机保存播放记录、字幕、笔记和分析结果。本地字幕识别在本机运行；部分可选模型与运行库需要先下载。

ChatGPT 登录连接 OpenAI 的云端服务，并非在电脑上安装本地 GPT。API 与 ChatGPT 授权是不同接入方式，额度、费用及服务条款由对应服务决定。使用云端分析、问答或翻译前，应用请求你确认将字幕原文及必要任务上下文发送至所选服务。授权按服务保存，不会每次重复询问。第三方服务如何处理收到的信息，应查阅其隐私政策。

API 密钥和登录令牌使用 Windows 当前用户的加密机制保护。必要的账号标识、邮箱等信息保存在本机，用于显示账号和恢复授权。应用不读取 Codex 的登录文件或你的 ChatGPT 历史对话。媒体平台登录可选，使用应用自己的会话。B站解析可能向本机工具提供短期明文 Cookie 临时文件，正常结束时清理；异常退出可能留有临时文件。因此不承诺“所有信息从不落盘”或“任何情况下都不会泄露”。

应用自动保留有限的本机运行与错误记录。目前没有作者的诊断上传接收端，也不会自动发送诊断资料。「报告问题」提供预览和本地 ZIP 导出，由你决定是否分享。文本过滤不能识别所有私人内容；你填写的文字和所选图片会随包导出，图片内容及元数据不自动脱敏。

本机安装编号为随机 UUID，不读取主板、硬盘、MAC 地址或 Windows 机器标识，也不复用账号授权标识。它仅用于关联主动分享的报告，不随版本检查发送。可以在报告问题页重置。复制整个资料目录会复制编号；不同资料目录产生不同编号，不能用于准确统计硬件设备数量。重置不会撤回已分享的报告。

版本检查在用户点击后访问配置的公开 GitHub 渠道；渠道未配置时不发请求。请求不附加安装编号、诊断、账号、媒体或字幕。GitHub 会收到普通网络请求信息。当前候选未启用公开更新渠道，也不自动下载或执行安装包。

退出服务授权可移除相应令牌，但必要注册关联信息可能继续保存在本机。卸载默认保留资料、账号数据、模型和诊断记录；卸载不等于擦除数据。共享电脑上请分别使用 Windows 用户账号。

请只处理你有权访问、使用和分享的媒体，不规避平台访问限制。第三方平台、API、模型各自受其条款约束。AI 输出可能错误，不保证字幕完整、分析准确或平台持续可用；重要结论应回看来源。免责声明不取消适用法律规定的权利，也不代替必要的许可和分发审查。

## English

VidSage stores playback history, subtitles, notes, and analysis results locally by default. Local subtitle generation runs on your computer. Some optional models and runtimes require an initial download.

ChatGPT sign-in connects to OpenAI's cloud service; it does not install a local GPT model. ChatGPT authorization and API access are separate methods, with limits, charges, and terms set by the relevant service. Before cloud analysis, questions, or translation, VidSage asks you to authorize sending subtitles and necessary context to the selected service. This permission is remembered for that service. Consult the provider's privacy policy for its handling of submitted content.

API keys and sign-in tokens are protected using the current Windows user's encryption facilities. Necessary account identifiers and email addresses are stored locally to display accounts and restore authorization. VidSage does not read Codex sign-in files or your ChatGPT conversation history. Optional media-platform sign-in uses the app's own session. Bilibili access may provide a local helper with a temporary plaintext cookie file, removed during normal cleanup. Unexpected exits may leave it behind.

VidSage keeps limited local runtime and error records. It currently has no diagnostic upload endpoint and does not automatically send diagnostic data. **Report a problem** lets you review and export a ZIP locally; you decide whether to share it. Text filtering cannot identify all private information. Your text and selected images are included, and image content and metadata are not automatically redacted.

A random UUID identifies a local installation for reports you voluntarily share. It does not read hardware serial numbers, MAC addresses, or Windows machine identifiers, and does not reuse account identifiers. It is not sent with update checks. You can reset it; resetting does not retract previously shared reports. Copying an entire data directory copies the identifier, while separate data directories have different identifiers. It is not an accurate hardware-device counter.

An explicit update check contacts the configured public GitHub channel. No request is made when the channel is unconfigured. Installation identifiers, diagnostics, accounts, media, and subtitles are not attached. GitHub receives ordinary network request information. This candidate has no enabled public update channel and does not automatically download or execute installers.

Signing out can remove the relevant tokens, while necessary registration associations may remain locally. Uninstalling preserves personal data, account data, models, and diagnostic records by default; it does not erase them. Use separate Windows user accounts on shared computers.

Use only media you are entitled to access, process, and share, and respect platform restrictions and third-party terms. AI output can be incorrect; check consequential claims against the source. Availability, subtitle completeness, and model accuracy are not guaranteed. This statement does not remove rights under applicable law or replace licensing and distribution review.
