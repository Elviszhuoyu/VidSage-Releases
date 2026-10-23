# 隐私说明 / Privacy

适用范围：0.2.1 的播放与 AI 功能（以实际安装包为准） · 更新于 2026-10-23

## 本地资料与云服务

VidSage 默认在本机保存播放记录、字幕、笔记和分析结果。本地字幕识别在电脑上运行，部分可选模型需要先下载。

使用云端分析、问答或翻译时，软件会请求你授权，将字幕和必要的任务上下文发送给所选服务。授权按服务保存，后续使用该服务时不会每次重复询问。请查阅服务商的费用、使用条款和隐私政策。

全片提问还会参考当前同一字幕版本的 AI 报告及最近问答，包括 AI 补充内容；这些上下文随问题发送给所选服务，只用于理解讨论，不作为视频原文证据。当前片段或选段提问不附整篇报告。

ChatGPT 登录连接 OpenAI 云端服务；API 是另一种接入方式，两者的额度和费用分别由服务商决定。VidSage 不读取你的 Codex 登录文件或 ChatGPT 历史对话。

## 报告生图

「导出报告长图」只在本机排版已有报告，不调用 AI，也不向服务商发送内容。你主动保存到外部目录的文件由你自行保管。

AI 生图使用单独配置的官方 OpenAI 或 Gemini API。确认授权后，只发送当前报告或选中文字及排版说明，不附整段字幕、原视频、笔记或账号资料。可复用已有官方 API 密钥；ChatGPT 订阅登录不用于生图。密钥在本机加密保存。

生成的配图与原报告文字在本地排版保存。图片、来源文字和版本信息属于个人资料，清理缓存不会删除；删除原报告时默认保留图片，可另行选择同时删除。取消等待或网络超时不能保证服务端停止处理或不计费，软件不会自动重试或更换服务。

无痕会话内生图需要单独同意，退出后清理本次图片与临时文件；主动复制到剪贴板或另存到外部文件夹的图片会保留，执行前会提示。

## 无痕播放

点击左侧播放列表标题旁的帽子与眼镜图标，进入独立的无痕会话；状态与退出入口显示在产品名右侧。普通播放队列暂停保留；本次使用临时队列，本地媒体、在线解析、字幕、分析、问答和笔记不会加入普通历史或知识库，也不写入 VidSage 诊断记录。

处理过程中可能在专用临时目录写入字幕、缓存和结果，并非全程只使用内存。这些文件不加密，退出会话时清理；异常中断后，应用会在下次启动时清理已结束会话的残留。清理失败会明确提示。不要把这一功能视为磁盘取证不可恢复的保证。

本次字幕和分析结果仅供当前会话使用。AI 图片可主动复制或另存；外部副本不随会话清理。普通资料和原始媒体保留。平台登录单独隔离；ChatGPT 需要在无痕会话内单独登录，云端处理同意也只适用于本次会话。

无痕播放不提供网络匿名，也不能清理操作系统、浏览器、在线平台或外部模型服务保存的记录。使用云端 AI 前仍须确认数据发送和费用；在系统浏览器中打开报告链接时会另行提醒。

切换动画会在内存中短暂合成当前 VidSage 窗口与视频画面，不捕获其他应用，不写入截图文件或诊断记录；过渡结束、窗口移动或失焦后即释放。关闭无痕窗口后，软件先等待进程结束并清理专用临时目录，再提示清理完成。清理过程不应抢回已切换到其他应用的焦点。

## 评论与用量记录

评论采集只请求当前 B站视频的公开顶层样本，不发送你的平台 Cookie，不采集评论账号资料；打开入口或读取样本不会调用模型。确认后发送样本、问题和同一样本内必要的近期讨论给所选模型服务。评论样本与回答只保留在本次会话，重新采集成功后替换。

普通模式在本机记录请求类型、服务与模型、结果状态、耗时及服务返回的 Token 用量，用于汇总与费用估算。账本不保存字幕、评论、问题、Prompt、模型回答、密钥或播放地址。价格是你填写的本地估算配置，不连接服务商账单。无痕用量仅保留在当前会话内存中，退出后清理，不进入普通账本。

## 账号信息

API 密钥和登录令牌使用 Windows 当前用户的加密机制保护。账号标识、邮箱等必要信息保存在本机，用于显示账号和恢复登录。

媒体平台登录使用 VidSage 自己的会话。访问 B站时，本机辅助程序可能需要一个临时 Cookie 文件。该文件以明文保存，正常结束后清理；异常退出时可能残留。

退出服务授权会移除相应令牌，部分注册关联信息可能继续保留。卸载默认保留资料、账号数据、模型和诊断记录。共用电脑时，建议各自使用独立的 Windows 用户账号。

## 诊断与反馈

软件保留有限的本机运行和错误记录，不会自动上传给作者。你可以在「报告问题」中预览并导出 ZIP，再决定是否分享。

诊断包包含你填写的文字和选择的图片。软件的文本过滤无法识别所有私人信息，图片内容与元数据也不会自动脱敏。分享前请自行检查；GitHub Issues 是公开页面。

诊断报告使用随机生成的安装编号，方便关联你主动提交的问题。它不读取硬件序列号、MAC 地址或 Windows 机器标识，也不随更新检查发送。你可以在反馈页重置编号，已经分享的报告不会因此删除或更改。

## 更新检查

正常启动自动检查一次更新；打开「关于」或手动检查时，软件也会访问本项目的公开 GitHub 发布渠道。请求不附带安装编号、诊断、账号、媒体或字幕内容。GitHub 会接收到 IP 地址等正常网络请求信息。

你决定是否下载内容更新或完整安装包，校验完成后另行确认退出并安装。可复用文件只在本机读取和核对，不上传。无痕播放中不提供下载或安装更新。

## 使用提醒

请只处理你有权访问和分享的媒体，遵守平台、模型及服务商的相关条款。字幕和 AI 输出可能出错，重要内容应核对原始来源。

## English

This statement applies to playback and AI features in the 0.2.0 candidate and was updated on 2026-10-21.

### Local data and cloud services

VidSage stores playback history, subtitles, notes, and analysis results locally by default. Local caption generation runs on your computer. Some optional models require an initial download.

Cloud analysis, questions, and translation send subtitles and necessary task context to the service you select, after you grant permission. VidSage remembers that permission for the service. Check the provider's fees, terms, and privacy policy.

Whole-video questions also send the current AI report for the same subtitle version and recent questions and answers, including AI supplements, to the selected service. This context helps follow the discussion and is not video evidence. Current-fragment and selected-subtitle questions do not include the full report.

ChatGPT sign-in connects to OpenAI's cloud service. API access is a separate option with its own limits and fees. VidSage does not read your Codex login files or ChatGPT conversation history.

### Private playback

Select the hat-and-glasses icon beside the left playlist heading to start an isolated private session. Its status and exit control appear beside the product name. The ordinary queue pauses and stays intact. Local and online playback, subtitles, analysis, questions, and notes use a temporary session without entering ordinary history, the ordinary knowledge library, or VidSage diagnostic records.

Subtitles, caches, and results may be written to a dedicated temporary directory during processing; this is not a memory-only mode. These files are not encrypted. They are removed when the session ends. After an interruption, the next startup cleans up ended sessions and reports cleanup failures. This does not guarantee forensic erasure.

Subtitles and results are available only during the session; this version offers neither export nor encrypted storage. Ordinary data and original media stay intact. Platform sign-in is separate. ChatGPT requires a separate sign-in, and cloud-processing consent lasts only for this private session.

Private playback does not provide network anonymity or clear records held by the operating system, browsers, online platforms, or external model services. Cloud processing still requires consent to data transfer and applicable charges. Opening a report link in the system browser prompts a separate notice.

Transition animations briefly composite the current VidSage window and video picture in memory. They do not capture other applications or write screenshot files or diagnostic records. The picture is released when the transition ends, the window moves, or focus is lost. Cleanup completion is reported after the private process ends and its dedicated temporary directory is removed. Cleanup does not reclaim focus from another application.

### Comments and usage records

Comment sampling requests only the current Bilibili video's public top-level samples, without your platform cookies or commenter account details. Opening the view and reading samples do not call a model. After confirmation, the selected service receives the sample, question and necessary recent discussion of the same sample. Samples and answers remain only for this session and are replaced after a successful refresh.

Normal mode keeps a local ledger of request type, service and model, outcome, duration and token usage returned by the provider. It does not store subtitles, comments, questions, prompts, model answers, keys or playback URLs. Prices are local estimates you enter, separate from provider billing. Private usage stays in session memory, clears on exit and never enters the ordinary ledger.

### Account information

API keys and login tokens use the current Windows user's encryption facilities. Necessary account identifiers and email addresses stay locally to display accounts and restore sign-in.

Media sign-in uses VidSage's own sessions. Bilibili access may require a temporary plaintext cookie file for a local helper. Normal cleanup removes it; an unexpected exit may leave it behind.

Signing out removes the relevant tokens, though some registration information may remain. Uninstalling preserves data, accounts, models, and diagnostic records by default. Use separate Windows accounts on shared computers.

### Diagnostics and feedback

VidSage keeps limited local runtime and error records without automatically uploading them to the author. You can preview and export a diagnostic ZIP, then choose whether to share it.

The ZIP includes the text and images you select. Text filtering cannot catch every private detail, and images and their metadata are not automatically redacted. Review them before sharing. GitHub Issues are public.

A randomly generated installation identifier helps relate reports you submit. It does not read hardware serial numbers, MAC addresses, or Windows machine identifiers, and is not sent with update checks. You can reset it in the feedback page; reports already shared remain unchanged.

### Update checks

Normal startup checks the project's public GitHub release channel once. About and the manual check use the same channel. The request does not include installation identifiers, diagnostics, accounts, media, or subtitles. GitHub receives normal network request information, including your IP address.

You choose whether to download a content update or full installer, then separately confirm closing the app and installing it after verification. Reusable files are read and verified locally; they are not uploaded. Downloading and installing updates are unavailable during private playback.

### Use

Only process media you have permission to access and share, and follow the terms of the platforms, models, and services you use. Captions and AI results can be wrong; check important details against the original source.
