# Getting started with VidSage

[简体中文](GETTING_STARTED.zh-CN.md) · [Privacy](PRIVACY.md)

VidSage combines video, subtitles, AI analysis, and notes. The app currently uses a Simplified Chinese interface; this guide includes the Chinese names of controls.

## Install

The current preview is **0.1.80 for Windows 11 x64**. Download `VidSage-0.1.80-win11-x64-Setup.exe` from the [official release page](https://github.com/Elviszhuoyu/VidSage-Releases/releases/tag/v0.1.80). You only need this EXE to use the app. The source archives are for developers who need them.

The installer includes the player, local caption libraries, and the base model. No development tools are needed. Allow at least 6 GB for installation and extraction.

This first release is unsigned. Windows may show “Unknown publisher” or “Windows protected your PC.” Check the download source and checksum before installing:

1. Run this in PowerShell, replacing the path with the downloaded file:

   ```powershell
   Get-FileHash -LiteralPath "full path to the installer" -Algorithm SHA256
   ```

2. Compare the full result with the SHA256 below. If it differs, stop and check the download source.
3. Once verified, you may choose **More info → Run anyway** if Windows offers it. If malware is reported, the option is unavailable, or the source is unclear, stop and report the message. Do not disable system protection.
4. Run the installer, choose a folder, and follow the prompts.

SHA256 for the 0.1.80 installer:

`aa9d787103af26e4771dc499dbea0e17b485e61a8911440e64a5fc5e55b2a549`

A checksum checks that the file matches the release. It does not replace a digital signature or security checks. Use the matching release page for other versions.

## First use

Follow the setup guide at the top right, or skip it. Reopen it through **关于 → 上手指引 (About → Getting started)**.

1. Open a local video or supported web address. Local playback needs no AI account.
2. Use existing subtitles or import a subtitle file. If there are none, select base in the caption task panel and start generation.
3. For analysis, questions, or translation, configure your API, connect ChatGPT, or choose a supported local service under **AI 服务 (AI services)**. Cloud services may charge separately. VidSage asks for permission before sending content and remembers that permission for the selected service.
4. Open **AI 学习 (AI Learning)** to analyze the subtitles or ask questions. Select a timestamp to return to the video and save useful content as notes.

Optional Bilibili sign-in provides access to media and subtitles your account may view. YouTube currently supports public videos.

Local caption generation needs no additional AI account. Larger models download only when you select them. See [system requirements and models](HARDWARE.en.md).

## Settings

| Category | Options |
|---|---|
| AI 服务 (AI services) | APIs, authorization, services, models, and connection checks |
| 媒体账号 (Media accounts) | Platform sign-in and sessions |
| 字幕 (Subtitles) | Display, translation, local models, and storage |
| 播放器 (Player) | Playback, appearance, icons, and local records |

**关于 → 支持作者 (About → Support the author)** offers optional donations, which do not affect features.

## Update or uninstall

Use **关于 → 更新与安装 (About → Updates and installation)** to check for updates and open the download page. Close VidSage, then run the new installer in the same installation folder. The app does not download or install updates automatically.

Uninstall through **Windows Settings → Apps → Installed apps → VidSage**. Updates and uninstall preserve captions, notes, models, account data, and diagnostic records by default, so you can reuse them after reinstalling.

## Report a problem

Use **关于 → 报告问题 (About → Report a problem)**, review the contents, and export a diagnostic ZIP. If VidSage will not open, use **VidSage 反馈与诊断 (VidSage Feedback and Diagnostics)** in the Start menu.

The ZIP stays on your computer until you choose to share it. Check text and images for accounts, keys, private paths, and other sensitive information first. Follow the [feedback guide](FEEDBACK.en.md).

Captions and AI results can be wrong, especially names and numbers. Check them against the video.
