# Getting started with VidSage

[简体中文](GETTING_STARTED.zh-CN.md) · [Privacy](PRIVACY.md)

VidSage combines video, subtitles, AI analysis, and notes. The app currently uses a Simplified Chinese interface; this guide includes the Chinese names of controls.

## Install

VidSage supports **Windows 11 x64**. Choose a version on the [official releases page](https://github.com/Elviszhuoyu/VidSage-Releases/releases) and download its Setup.exe installer. You only need this EXE to use the app. The source archives are for developers who need them.

The installer includes the player, local caption libraries, and the base model. No development tools are needed. Allow at least 6 GB for installation and extraction.

1. Double-click the downloaded Setup EXE.
2. Choose a program folder, read the license, and complete the installation. The default folder is ready to use; a dedicated folder on another drive is optional.
3. Launch VidSage and follow or skip the setup guide.

The current preview installer is unsigned. Windows may show “Unknown publisher” or “Windows protected your PC.” After confirming that the file came from the official release page above, you may choose **More info → Run anyway** if offered. If malware is reported, the option is unavailable, or the source is unclear, stop and report the message. Do not disable system protection.

### Optional: verify the checksum

To check that the download matches the release, run this in PowerShell, replacing the path with the downloaded file:

```powershell
Get-FileHash -LiteralPath "full path to the installer" -Algorithm SHA256
```

The full result should match the installer entry in SHA256SUMS.txt on that version's release page. If it differs, stop and check the download source.

A checksum verifies the downloaded file. It does not replace a digital signature or security checks.

## First use

Follow the setup guide at the top right, or skip it. Reopen it through **关于 → 上手指引 (About → Getting started)**.

1. Open a local video or supported web address. Local playback needs no AI account.
2. Use existing subtitles or import a subtitle file. If there are none, select base in the caption task panel and start generation.
3. For analysis, questions, or translation, configure your API, connect ChatGPT, or choose a supported local service under **AI 服务 (AI services)**. Cloud services may charge separately. VidSage asks for permission before sending content and remembers that permission for the selected service.
4. Open **AI 学习 (AI Learning)** to analyze the subtitles or ask questions. Select a timestamp to return to the video and save useful content as notes.

Whole-video questions can continue a discussion of the current report and recent answers. Video explanations retain subtitle references; concept explanations and hypothetical examples have separate labels. The AI report is not video evidence. Report and conversation context are sent with the question to your selected service; see [Privacy](PRIVACY.md).

Optional Bilibili sign-in provides access to media and subtitles your account may view. YouTube currently supports public videos.

Local caption generation needs no additional AI account. Larger models download only when you select them. See [system requirements and models](HARDWARE.en.md).

## Settings

| Category | Options |
|---|---|
| AI 服务 (AI services) | APIs, authorization, services, models, and connection checks |
| 媒体账号 (Media accounts) | Platform sign-in and sessions |
| 字幕 (Subtitles) | Display, translation, and local models |
| 播放器 (Player) | Playback, appearance, icons, and local records |
| 存储 (Storage) | Model and cache locations, disk usage, and cache cleanup |

Default model and cache locations are ready to use. To change them, open **设置 → 存储 (Settings → Storage)** and select a new location. VidSage copies and verifies files before switching; the originals remain. Cache cleanup shows the proposed files first and excludes subtitles, notes, and account data.

**关于 → 支持作者 (About → Support the author)** offers optional donations, which do not affect features.

## Private playback

Select the hat-and-glasses icon beside the left playlist heading. The app switches to graphite gray and displays **无痕播放 (Private playback)** with an exit control beside the product name. Your ordinary queue stays intact, while the private session starts with an empty temporary queue. Open local media or online links and use subtitles, analysis, questions, and temporary notes.

The previous picture remains visible while the next window prepares. A soft transition runs when it is ready, and reverses on exit. Reduced-motion settings use a short fade. Transition pictures stay in memory and are not saved as screenshot files.

Exiting clears session data and restores the ordinary queue. This version does not export private subtitles or results. Platform and ChatGPT sign-in are separate, and cloud processing requires consent for this session. See [Privacy](PRIVACY.md) for storage and cleanup boundaries.

## Update or uninstall

Opening **关于 (About)** checks for updates; you can also check beside the version. Choose to download the full installer, then confirm closing and installing after verification. Finish active tasks or unsaved settings first. The first upgrade from 0.1.78 or 0.1.80 still requires downloading and running the new Setup from the official releases page.

Uninstall through **Windows Settings → Apps → Installed apps → VidSage**. Updates and uninstall preserve captions, notes, models, account data, and diagnostic records by default, so you can reuse them after reinstalling.

## Report a problem

Use **关于 → 报告问题 (About → Report a problem)**, review the contents, and export a diagnostic ZIP. If VidSage will not open, use **VidSage 反馈与诊断 (VidSage Feedback and Diagnostics)** in the Start menu.

The ZIP stays on your computer until you choose to share it. Check text and images for accounts, keys, private paths, and other sensitive information first. Follow the [feedback guide](FEEDBACK.en.md).

Captions and AI results can be wrong, especially names and numbers. Check them against the video.
