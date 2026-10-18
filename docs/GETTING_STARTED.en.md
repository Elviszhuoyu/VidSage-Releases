# Getting started with VidSage

The application currently uses a Simplified Chinese interface. This English documentation explains the Chinese controls; an English UI is planned for a later version.

[中文](GETTING_STARTED.zh-CN.md) · [Privacy and authorization](PRIVACY.md)

VidSage brings video, subtitles, analysis, and notes into one workspace. Open a video first, then connect the services you need.

## Install, update, or uninstall

The current candidate is **0.1.77 for Windows 11 x64**. Public distribution has not been cleared. When available, obtain installers from the project's announced GitHub Releases channel and check the version's SHA256. The current candidate is unsigned; publisher identity has not been verified by Windows.

The complete installer includes the player, self-contained core, local subtitle runtime, and a small base model. Node.js and the .NET SDK are not required. Allow at least 4 GB for installation and extraction; optional larger models need additional space.

Run Setup and choose an installation directory. The home screen starts with both side panels collapsed. If AI is not configured, a small invitation offers a guided setup. You can skip it.

To update, close VidSage and run the newer complete Setup in the same installation directory. Personal data is stored separately, and earlier program versions are retained. Setup asks you to close an active instance instead of stopping it forcibly. **关于 → 更新与安装 (About → Updates and installation)** provides a version-check entry; it remains unconfigured until a public release channel is selected. Automatic downloads, live patching, and silent installation are not available yet.

Uninstall through **Windows Settings → Apps → Installed apps → VidSage**. Uninstalling preserves personal data, models, account data, and diagnostic records by default. Development-preview data is not automatically migrated into an installed copy.

## Verify the installer and understand Windows prompts

The first public preview will be **unsigned**. We are not purchasing a signing certificate for this preview. Its SHA256 checksum lets you check that your download matches the published file; it does not verify the publisher or prove that software is safe.

1. Download Setup and its checksum from the official [GitHub Releases](https://github.com/Elviszhuoyu/VidSage-Releases/releases) page.
2. In PowerShell, run `Get-FileHash -LiteralPath "full path to the installer" -Algorithm SHA256`.
3. Compare the entire value with the checksum for that exact version. If they differ, do not run the file.
4. Windows may show “Unknown publisher” or “Windows protected your PC.” After verifying the official source and checksum, you may use **More info → Run anyway** if your device allows it. If that option is unavailable, malware is reported, or you are unsure, stop and report the message. Do not disable Windows security protections.

No public installer is available yet. A checksum for an older internal candidate must not be used for a newer download.

## Four short steps

1. **Connect AI.** Choose an API provider or ChatGPT subscription authorization. API access needs your own endpoint, key, and model. ChatGPT sign-in opens the official browser authorization flow and connects to a cloud service; it does not install a local GPT model. Playback and local subtitle generation need no AI account.
2. **Connect media accounts when needed.** Bilibili sign-in can access media and subtitles available to that account. It is optional. YouTube currently supports public videos.
3. **Prepare subtitles.** Use existing subtitles or import a local file. For videos without subtitles, select the bundled base model and start a local caption task. Larger models download only after you choose them. Choose “使用此模型” to set the default. A successful model check or preparation, or starting a caption task, also remembers the selection.
4. **Start learning.** Open a local video or supported URL, obtain subtitles, and open **AI 学习 (AI Learning)**. Analysis, questions, and translation use your selected service. VidSage asks before sending content to a service and remembers that authorization for the service.

You can move back, continue, or skip. Reopen the guide from **关于 → 上手指引 (About → Getting started)**. The guide does not start downloads, transcription, or paid inference automatically.

## Work with the video

Select a subtitle or result timestamp to return to the source. Ask questions about the available subtitles and save useful material as notes. When a playing video has no available subtitles, a small tip may suggest local generation. It closes automatically or manually; hovering or keyboard focus pauses its countdown. Its action opens the caption task without starting transcription.

Recognition, translation, and AI output can be inaccurate. Check names, numbers, and important claims against the original video and other reliable sources. Use appropriate professional advice for consequential decisions.

Settings have four categories: **AI 服务 (AI services)**, **媒体账号 (Media accounts)**, **字幕 (Subtitles)**, and **播放器 (Player)**. Subtitle settings include local models and storage. **关于 → 支持作者 (About → Support the author)** offers optional WeChat Pay and Alipay support; the amount is voluntary and does not affect features.

## Report a problem

Use **关于 → 报告问题 (About → Report a problem)**. Describe what happened, add the time and optional images, review the contents, and export a ZIP locally. If the player cannot open, use the independent diagnostic entry in the Start menu. There is currently no automatic upload endpoint; exporting does not send the report to the author.

A random installation identifier helps relate reports you choose to share. It reads no hardware serial numbers, can be reset, and survives updates in the same data directory. Resetting it does not remove data or change reports already shared. Check text, images, and image metadata before sharing. See the [privacy statement](PRIVACY.md).

See [hardware and models](HARDWARE.en.md) and the [feedback guide](FEEDBACK.en.md).
