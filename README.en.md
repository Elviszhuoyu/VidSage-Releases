# VidSage

The application currently uses a Simplified Chinese interface. This English documentation explains the Chinese controls; an English UI is planned for a later version.

**Watch, understand, and return to the source.**

Keep subtitles, notes, and AI analysis beside the video, with timestamps connecting ideas to the original scene.

[中文](README.md) · [Getting started](docs/GETTING_STARTED.en.md) · [Privacy](docs/PRIVACY.md)

## Why I built VidSage

I started working on it while studying finance and other subjects through video courses. Often, the video had moved on while I was still trying to understand the previous idea.

AI helped me break difficult concepts into smaller pieces, ask for another explanation, and check it against the video. But switching between web pages, extensions, and notes kept interrupting my thinking. I wanted a desktop tool I would enjoy using, with the video, subtitles, questions, and notes together. It should work for a course saved on my computer as well as supported videos on Bilibili and YouTube.

That is where VidSage began. I hope it makes learning a little easier for you, too.

![VidSage home and optional setup guide](docs/assets/release/home.png)

## Downloads and testing

Windows 11 x64 · Screenshots show **0.1.77**.

**Public testing is being prepared; no public installer is available yet.** Local installation, upgrade, and uninstall checks have passed. Third-party redistribution review and other release checks remain unfinished. When ready, installers and SHA256 checksums will appear in this repository’s [Releases](https://github.com/Elviszhuoyu/VidSage-Releases/releases).

This repository hosts the product overview, guides, and future downloads. Application source code and development history remain private.

## A workspace for understanding video

- Use existing subtitles, import a file, or generate captions locally with the bundled small model.
- Analyze and ask questions about subtitles, then return to the source through timestamps.
- Save your notes and analysis as material you can revisit and search.
- Choose API access, ChatGPT cloud authorization, or a supported local service. Media-account sign-in is optional; local playback needs no AI account.

The home screen starts clear. A small optional guide introduces services and subtitles in four steps. Settings use four concise categories: AI services, Media accounts, Subtitles, and Player.

![Compact settings navigation](docs/assets/release/settings.png)

## Install and use

The complete installer includes the player, core, local caption runtime, and base model. No development environment is required. When public distribution is ready, installers and checksums will be published through the announced GitHub Releases channel.

Open a local video or supported Bilibili / YouTube URL, obtain subtitles, then explore AI Learning, questions, and notes. The [getting-started guide](docs/GETTING_STARTED.en.md) covers setup and the full workflow.

Updates use a complete Setup after the player is closed. Standard Windows uninstall is available; updates and uninstall preserve personal data by default. About includes a version-check entry, but the public channel is not enabled yet.

## Privacy and feedback

Local caption generation stays on your computer. Authorized cloud analysis, questions, and translation send subtitles and necessary context to the selected provider. ChatGPT sign-in connects to a cloud service, not a local model.

Runtime logs stay local. There is no automatic diagnostic upload endpoint. Review and export a ZIP through **关于 → 报告问题 (About → Report a problem)**, then decide whether to share it. Images and their metadata are not automatically redacted. A random installation identifier relates reports you voluntarily share and reads no hardware serial numbers. See the [privacy statement](docs/PRIVACY.md).

Optional support is available through WeChat Pay and Alipay in **关于 → 支持作者 (About → Support the author)**. The amount is voluntary and does not affect features.

## Use and permissions

**Rights in original code are reserved; further development requires the author’s prior written permission.** Officially released test builds may be evaluated free of charge. GitHub platform rights and third-party licenses apply separately. Donations do not grant development or redistribution rights. See the [use and copyright notice](COPYRIGHT.md).
