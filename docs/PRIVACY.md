# 隐私说明 / Privacy

适用版本：0.1.80 · 更新于 2026-10-19

## 本地资料与云服务

VidSage 默认在本机保存播放记录、字幕、笔记和分析结果。本地字幕识别在电脑上运行，部分可选模型需要先下载。

使用云端分析、问答或翻译时，软件会请求你授权，将字幕和必要的任务上下文发送给所选服务。授权按服务保存，后续使用该服务时不会每次重复询问。请查阅服务商的费用、使用条款和隐私政策。

ChatGPT 登录连接 OpenAI 云端服务；API 是另一种接入方式，两者的额度和费用分别由服务商决定。VidSage 不读取你的 Codex 登录文件或 ChatGPT 历史对话。

## 账号信息

API 密钥和登录令牌使用 Windows 当前用户的加密机制保护。账号标识、邮箱等必要信息保存在本机，用于显示账号和恢复登录。

媒体平台登录使用 VidSage 自己的会话。访问 B站时，本机辅助程序可能需要一个临时 Cookie 文件。该文件以明文保存，正常结束后清理；异常退出时可能残留。

退出服务授权会移除相应令牌，部分注册关联信息可能继续保留。卸载默认保留资料、账号数据、模型和诊断记录。共用电脑时，建议各自使用独立的 Windows 用户账号。

## 诊断与反馈

软件保留有限的本机运行和错误记录，不会自动上传给作者。你可以在「报告问题」中预览并导出 ZIP，再决定是否分享。

诊断包包含你填写的文字和选择的图片。软件的文本过滤无法识别所有私人信息，图片内容与元数据也不会自动脱敏。分享前请自行检查；GitHub Issues 是公开页面。

诊断报告使用随机生成的安装编号，方便关联你主动提交的问题。它不读取硬件序列号、MAC 地址或 Windows 机器标识，也不随更新检查发送。你可以在反馈页重置编号，已经分享的报告不会因此删除或更改。

## 更新检查

点击「关于 → 更新与安装」后，软件会访问本项目的公开 GitHub 发布渠道。请求不附带安装编号、诊断、账号、媒体或字幕内容。GitHub 会接收到 IP 地址等正常网络请求信息。

软件只检查版本并打开下载页，由你下载和运行安装包。

## 使用提醒

请只处理你有权访问和分享的媒体，遵守平台、模型及服务商的相关条款。字幕和 AI 输出可能出错，重要内容应核对原始来源。

## English

This statement applies to version 0.1.80 and was updated on 2026-10-19.

### Local data and cloud services

VidSage stores playback history, subtitles, notes, and analysis results locally by default. Local caption generation runs on your computer. Some optional models require an initial download.

Cloud analysis, questions, and translation send subtitles and necessary task context to the service you select, after you grant permission. VidSage remembers that permission for the service. Check the provider's fees, terms, and privacy policy.

ChatGPT sign-in connects to OpenAI's cloud service. API access is a separate option with its own limits and fees. VidSage does not read your Codex login files or ChatGPT conversation history.

### Account information

API keys and login tokens use the current Windows user's encryption facilities. Necessary account identifiers and email addresses stay locally to display accounts and restore sign-in.

Media sign-in uses VidSage's own sessions. Bilibili access may require a temporary plaintext cookie file for a local helper. Normal cleanup removes it; an unexpected exit may leave it behind.

Signing out removes the relevant tokens, though some registration information may remain. Uninstalling preserves data, accounts, models, and diagnostic records by default. Use separate Windows accounts on shared computers.

### Diagnostics and feedback

VidSage keeps limited local runtime and error records without automatically uploading them to the author. You can preview and export a diagnostic ZIP, then choose whether to share it.

The ZIP includes the text and images you select. Text filtering cannot catch every private detail, and images and their metadata are not automatically redacted. Review them before sharing. GitHub Issues are public.

A randomly generated installation identifier helps relate reports you submit. It does not read hardware serial numbers, MAC addresses, or Windows machine identifiers, and is not sent with update checks. You can reset it in the feedback page; reports already shared remain unchanged.

### Update checks

Selecting **关于 → 更新与安装 (About → Updates and installation)** contacts this project's public GitHub release channel. The request does not include installation identifiers, diagnostics, accounts, media, or subtitles. GitHub receives normal network request information, including your IP address.

VidSage checks the version and opens the download page. You choose whether to download and run the installer.

### Use

Only process media you have permission to access and share, and follow the terms of the platforms, models, and services you use. Captions and AI results can be wrong; check important details against the original source.
