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

## Optional: Qwen3-ASR

The standard installer contains neither the Qwen environment nor its models. Selecting Qwen does not download them automatically. Use the bundled base model or optional Whisper models if you do not need Qwen.

- The recognition model and aligner total about **5.93 GB** and download only after you choose **下载模型 (Download model)**.
- The tested isolated environment occupies about **3.5 GB on disk**. This is not its compressed download size. Allow additional room for download caches.
- Model files and environment readiness are checked separately. Existing files stay intact. First loading may take tens of seconds, depending on hardware and caches.

Official sources: [native Transformers instructions](https://huggingface.co/Qwen/Qwen3-ASR-1.7B-hf#usage), [recognition model](https://huggingface.co/Qwen/Qwen3-ASR-1.7B-hf), and [aligner](https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B-hf). VidSage checks pinned revisions and file hashes; downloading an arbitrary model version does not establish readiness.

If you already have a compatible environment, choose Qwen under **设置 → 字幕 → 本地字幕识别 (Settings → Subtitles → Local recognition)**. Select **选择千问环境… (Choose Qwen environment)** and its python.exe, then check or download the model and select **使用此模型 (Use this model)**. Local recognition does not send audio to a cloud service.

<details>
<summary>Preparing your own Windows environment: advanced</summary>

Install Python 3.12 x64 from [Python's official site](https://www.python.org/downloads/windows/). Create a separate environment so that ComfyUI and other applications remain unchanged. These commands download dependencies only when you run them:

```powershell
$taskQwenEnvironment = Join-Path $env:LOCALAPPDATA 'VidSage\QwenRuntime'
py -3.12 -m venv $taskQwenEnvironment
$taskQwenPython = Join-Path $taskQwenEnvironment 'Scripts\python.exe'
# Replace this with the actual lock file in your current VidSage version folder.
$taskQwenRequirements = 'VERSION_FOLDER\resources\app\runtime\host\tools\asr\qwen3-requirements.lock'
& $taskQwenPython -m pip install --require-hashes -r $taskQwenRequirements
```

The lock file uses pinned upstream PyPI/PyTorch files with SHA256 checks. Downloads are large and depend on your connection. Keep the environment after an interruption and inspect the error before continuing; do not remove hash verification or substitute versions.

Select Scripts\python.exe from this environment in VidSage afterward. The pinned combination passed local imports and a short recognition sample; a fresh online installation on other hardware has not been verified. The tested GPU environment needs a compatible NVIDIA GPU and driver. Qwen performance and compatibility on other hardware remain unverified.

</details>

## AI analysis and captions

Local caption generation needs no AI account. For analysis, questions, and translation, configure your own API, connect ChatGPT, or select a supported local service in AI settings. Cloud providers set their own fees and usage limits.

Cloud audio transcription is not available in this version. ChatGPT sign-in is used for text analysis, questions, and translation.

If caption generation fails, note the model, the step that failed, and your computer configuration, then follow the [feedback guide](FEEDBACK.en.md).

Technical sources: [Whisper](https://github.com/openai/whisper), [faster-whisper](https://github.com/SYSTRAN/faster-whisper), [CTranslate2](https://opennmt.net/CTranslate2/hardware_support.html).
