# System requirements and caption models

[简体中文](HARDWARE.zh-CN.md) · [Getting started](GETTING_STARTED.en.md)

VidSage currently supports Windows 11 x64. Local captions use OpenAI Whisper models on the CPU or a compatible NVIDIA GPU.

## System requirements

| Item | Details |
|---|---|
| Operating system | Windows 11 x64; Windows ARM, macOS, and Linux are not currently supported |
| Processor | A 64-bit Intel or AMD processor; compatibility with older models still needs testing |
| Memory | The minimum requirement has not been established. Larger models use more memory |
| Storage | Allow at least 6 GB for installation and extraction, plus space for optional models, captions, notes, and retained versions |
| Connection | Local playback and caption generation with the bundled model work offline. Online videos, model downloads, and cloud AI require internet access |

Testing has covered a limited range of computers. Try a short video before processing a long course.

## Caption generation and GPU support

The installer includes the base model and NVIDIA acceleration libraries. Computers without a dedicated GPU, or with AMD or Intel graphics, can generate captions on the CPU. GPU acceleration currently requires a compatible NVIDIA GPU and an installed driver.

Caption settings offer three options:

- **Auto** prefers NVIDIA GPU processing. If a recoverable GPU error occurs while loading the model or starting recognition, VidSage explains the error and tries the CPU.
- **GPU** uses the GPU only. If it fails, you can choose to switch to CPU.
- **CPU** uses the processor without GPU acceleration.

Saved captions are retained if recognition fails. CPU and GPU processing have worked on the test computer; compatibility with other configurations is still being tested.

## Choose a model

| Model | Download size | Suggested use |
|---|---:|---|
| base | About 148 MB, included | Start here for lower resource use |
| small | About 486 MB, optional | If base performs poorly, compare both models on the same short video |
| large-v3-turbo | About 1.62 GB, optional | Uses more resources. Try a short video to check results and processing time |

These are file sizes. Running a model also requires RAM or VRAM. A larger model may not improve every recording; check names and numbers against the video. VidSage remembers your model selection. Custom models must use a compatible faster-whisper / CTranslate2 format.

Model sources: [base](https://huggingface.co/Systran/faster-whisper-base), [small](https://huggingface.co/Systran/faster-whisper-small), [large-v3-turbo](https://huggingface.co/dropbox-dash/faster-whisper-large-v3-turbo).

## AI analysis and captions

Local caption generation needs no AI account. For analysis, questions, and translation, configure your own API, connect ChatGPT, or select a supported local service in AI settings. Cloud providers set their own fees and usage limits.

Cloud audio transcription is not available in this version. ChatGPT sign-in is used for text analysis, questions, and translation.

If caption generation fails, note the model, the step that failed, and your computer configuration, then follow the [feedback guide](FEEDBACK.en.md).

Technical sources: [Whisper](https://github.com/openai/whisper), [faster-whisper](https://github.com/SYSTRAN/faster-whisper), [CTranslate2](https://opennmt.net/CTranslate2/hardware_support.html).
