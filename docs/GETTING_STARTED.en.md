# Getting started with VidSage

[简体中文](GETTING_STARTED.zh-CN.md) · [Privacy](PRIVACY.md)

VidSage combines video, subtitles, AI analysis, and notes. The interface supports English and Simplified Chinese. In Settings → Player → Interface language, choose a language or follow the system. Switching does not change subtitle, report or note content.

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
2. Use existing subtitles or import a subtitle file. If there are none, choose a ready model in the caption task panel and start generation. Settings → Subtitles shows model files and runtime readiness separately: downloaded files alone do not mean a model is ready to use.
3. For analysis, questions, or translation, configure your API, connect ChatGPT, or choose a supported local service under **AI 服务 (AI services)**. Cloud services may charge separately. VidSage asks for permission before sending content and remembers that permission for the selected service.
4. Open **AI 学习 (AI Learning)** to analyze the subtitles or ask questions. Select a timestamp to return to the video and save useful content as notes.

Whole-video questions can continue a discussion of the current report and recent answers. Video explanations retain subtitle references; concept explanations and hypothetical examples have separate labels. The AI report is not video evidence. Report and conversation context are sent with the question to your selected service; see [Privacy](PRIVACY.md).

Gemini model availability and free quotas depend on your project. You can select Lite for analysis and Q&A without enabling billing for this local test. Per-cue translation quality varies by model; languages with a different word order may reorder fragments. Keep the original track and review the translation rather than treating generation completion as semantic acceptance.

Optional Bilibili sign-in provides access to media and subtitles your account may view. YouTube currently supports public videos.

Local caption generation needs no additional AI account. Larger models download only when you select them. See [system requirements and models](HARDWARE.en.md).

Long transcripts are processed in sections. Returned-section counts, active source ranges and elapsed time show real progress; reports are saved after checks. Playback remains available while waiting, and cancelling or failing keeps existing reports.

Application icons default to dark, with a light option in Settings → Player. Drag a sidebar divider, or use its left/right arrow keys, to adjust its width.

## Report images and free export

In a report, choose More → Export report image to typeset the existing content locally. This does not call AI or require an image account. Export shows progress and completion feedback; canceling the save dialog lets you try again. Use Markdown export if the report exceeds the image height limit.

For AI illustrations, open Settings → AI services → Images and reuse an existing official API account or add a key. Then choose AI image in the report. Selected text limits the scope; clearing the selection restores the whole report. Gemini image generation requires a paid API tier. The ChatGPT subscription connection and DeepSeek API do not currently generate images here. Models, quotas and charges depend on your provider account.

The report shows task status and lets you cancel waiting. The image window supports wheel zoom, pan, fit, full screen, minimize, copy, save and reveal in folder. More options contains layouts and previous versions. Regeneration keeps older versions; clearing caches keeps finished images. Cancellation or a timeout does not guarantee that the provider stops processing or charging. VidSage does not retry automatically.

## Settings

| Category | Options |
|---|---|
| AI 服务 (AI services) | APIs, authorization, services, models, and connection checks |
| 媒体账号 (Media accounts) | Platform sign-in and sessions |
| 字幕 (Subtitles) | Display, translation, and local models |
| 播放器 (Player) | Interface language, playback, appearance, icons, and local records |
| 存储 (Storage) | Model and cache locations, disk usage, and cache cleanup |

Default model and cache locations are ready to use. To change them, open **设置 → 存储 (Settings → Storage)** and select a new location. VidSage copies and verifies files before switching; the originals remain. Cache cleanup shows the proposed files first and excludes subtitles, notes, and account data.

**关于 → 支持作者 (About → Support the author)** offers optional donations, which do not affect features.

## Everyday controls

To open media from Explorer, choose Open with → VidSage. Set VidSage as your preferred player through Windows Settings → Apps → Default apps; installing VidSage does not change your current default. Files opened while private playback is active go to that private session.

For supported Bilibili media, use the quality control to choose an available quality. The list reflects the current video and account access. Failed changes retain the previous playable quality. Right-click the video and choose Playback statistics to inspect resolution, codecs, frame rate, dropped frames, cache duration and hardware decoding. Copy statistics excludes the media title, file path and playback URL.

In Learn, open Comments to sample the current Bilibili video's public top-level comments. Reading samples does not call a model. Confirm the service and sample before summarizing or asking a question. Citations return to the sampled comments. These views do not represent all viewers or establish facts about the video. Samples and answers last only for the current session.

Open AI services → Usage and costs, or the shortcut in Learn, to review request counts, token usage and cost estimates. Subscription requests, local processing and API requests are distinct. Missing provider usage is shown as unavailable. Estimates default to CNY. Applicable models use official reference rates; you can save your own rate and exchange-rate snapshots. Unknown requests are excluded from the amount, and time-dependent prices appear as a range. Sort models by tokens, requests or estimated cost. Estimates are not the provider's bill. Private-session usage clears on exit.

## Private playback

Select the hat-and-glasses icon beside the left playlist heading. The app switches to graphite gray and displays **无痕播放 (Private playback)** with an exit control beside the product name. Your ordinary queue stays intact, while the private session starts with an empty temporary queue. Open local media or online links and use subtitles, analysis, questions, and temporary notes.

The previous picture remains visible while the next window prepares. A soft transition runs when it is ready, and reverses on exit. Reduced-motion settings use a short fade. Transition pictures stay in memory and are not saved as screenshot files.

Exiting clears session data and restores the ordinary queue. This version does not export private subtitles or results. Platform and ChatGPT sign-in are separate, and cloud processing requires consent for this session. See [Privacy](PRIVACY.md) for storage and cleanup boundaries.

## Update or uninstall

Normal startup checks for updates once. Use the notice at the top or open About to check manually. VidSage verifies reusable local files and downloads the missing content when a compatible content update is available; a full installer remains available as a fallback. You can skip intermediate releases. Download progress shows transferred and reused bytes. After verification, confirm closing, installation and reopening. Finish active tasks or unsaved settings first. If an older version cannot complete an update, download and run the latest available Setup from the official releases page.

Uninstall through **Windows Settings → Apps → Installed apps → VidSage**. Updates preserve your data. Starting with 0.1.91, interactive uninstall offers three independent choices: caches and diagnostics, downloaded models in the default folder, and personal data and sign-ins. All are unchecked by default; deleting personal data requires a second confirmation and cannot be undone. Custom or relocated model/cache folders, development-preview data, and exported files remain untouched. Silent uninstall always preserves user data.

## Report a problem

Use **关于 → 报告问题 (About → Report a problem)**, review the contents, and export a diagnostic ZIP. If VidSage will not open, use **VidSage 反馈与诊断 (VidSage Feedback and Diagnostics)** in the Start menu.

The ZIP stays on your computer until you choose to share it. Check text and images for accounts, keys, private paths, and other sensitive information first. Follow the [feedback guide](FEEDBACK.en.md).

Captions and AI results can be wrong, especially names and numbers. Check them against the video.


The full installer retains the bundled base subtitle model, CPU offline processing and NVIDIA acceleration components. Content reuse reduces later update downloads; it does not reduce the first installer. Changed installation terms require review in the wizard.
