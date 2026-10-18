# Hardware and caption models

[简体中文](HARDWARE.zh-CN.md) · [Getting started](GETTING_STARTED.en.md)

Local captions use OpenAI Whisper-family models through faster-whisper 1.2.1 and CTranslate2 4.7.2. NVIDIA technology is used for optional GPU acceleration. The Whisper models are not NVIDIA models or models trained by VidSage.

## What you need

| Use | Requirements |
|---|---|
| Play video, read existing subtitles, take notes | Windows 11 x64; no speech model or AI account required |
| Generate local captions | Start with the bundled base model. CPU processing does not require a dedicated GPU |
| Analyze, ask questions, or translate | Configure an API, ChatGPT authorization, or a supported local service. Cloud services may charge separately |
| Accelerate captions with a GPU | Compatible NVIDIA hardware and drivers. Acceleration runtimes are included; choose Auto, GPU, or CPU |

Computers with AMD graphics or Intel integrated graphics can use CPU processing. AMD/Intel GPU acceleration is not promised, and not every NVIDIA setup is ready without configuration. Auto prefers a compatible NVIDIA GPU. A recognized GPU failure during loading or the first computation before confirmed captions triggers one CPU attempt with a visible reason. Manual GPU mode does not silently switch. Later failures preserve confirmed output. GPU and CPU were verified on one RTX 4090 computer; other devices remain part of public testing.

## Current support and validation

| Item | Details |
|---|---|
| OS | Windows 11 x64. Other systems and Windows ARM have not been validated |
| CPU | This release uses a Windows x64 player build. Minimum instruction-set and performance boundaries on older processors remain unverified across devices; the previous build’s x86-64-v3 label is not carried over |
| RAM | Usage varies by model and workload. A minimum RAM specification has not yet been validated |
| Storage | Allow at least 6 GB for installation and temporary extraction, plus space for optional models, audio caches, notes, and retained versions |
| Network | Local media and the bundled model work offline. Online media, optional downloads, and cloud AI require a connection |

These are support boundaries, not a performance guarantee for every computer. Try a short video before processing a long course. Speed depends on the processor, memory, model, audio length, and other running applications.

## Choose a model

| Model | Model files | Suggested use |
|---|---:|---|
| base | About 148 MB, included | Default for new users. Start here to try the full workflow with lower resource demands |
| small | About 486 MB, optional | Try when you need another accuracy option; still check names and numbers |
| large-v3-turbo | About 1.62 GB, optional | A heavier option. First confirm that resource use and processing time suit your machine |

Sizes are decimal file sizes, not RAM or VRAM requirements. A larger model does not guarantee a better result for every recording. Sources: [Systran/base](https://huggingface.co/Systran/faster-whisper-base), [Systran/small](https://huggingface.co/Systran/faster-whisper-small), [Dropbox Dash/large-v3-turbo](https://huggingface.co/dropbox-dash/faster-whisper-large-v3-turbo).

Existing model preferences are preserved. Custom directories must use a compatible faster-whisper/CTranslate2 format.

## If generation fails

Record the model, failure stage, operating system, CPU, and GPU, then follow the [feedback guide](FEEDBACK.en.md). Keep private videos, account tokens, and full transcripts out of public reports.

Cloud audio transcription is not available in this release. ChatGPT sign-in serves the integrated text analysis, questions, and translation features; it does not establish access to transcription APIs through your subscription.

References: [Whisper](https://github.com/openai/whisper), [faster-whisper](https://github.com/SYSTRAN/faster-whisper#gpu), [CTranslate2 hardware support](https://opennmt.net/CTranslate2/hardware_support.html).
