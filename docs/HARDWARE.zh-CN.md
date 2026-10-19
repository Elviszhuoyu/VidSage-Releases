# 系统要求与字幕模型

[English](HARDWARE.en.md) · [上手指南](GETTING_STARTED.zh-CN.md)

VidSage 当前支持 Windows 11 x64。本地字幕使用 OpenAI Whisper 模型，可通过 CPU 或兼容的 NVIDIA 显卡运行。

## 系统要求

| 项目 | 说明 |
|---|---|
| 操作系统 | Windows 11 x64；暂不支持 Windows ARM、macOS 和 Linux |
| 处理器 | 64 位 Intel 或 AMD 处理器；较老型号的兼容性仍需测试 |
| 内存 | 最低需求尚未确定，使用较大模型会占用更多内存 |
| 磁盘空间 | 安装和解压至少预留 6 GB；额外模型、字幕、笔记和保留的旧版本另占空间 |
| 网络连接 | 本地视频播放和随包模型生成字幕可离线使用；网络视频、模型下载和云端 AI 需要联网 |

公测版还未覆盖不同配置的电脑。建议先用几分钟的视频试用，再处理长课程。

## 字幕识别与显卡

安装包已包含 base 模型和 NVIDIA 加速运行库。没有独立显卡，或使用 AMD、Intel 显卡时，可以选择 CPU 生成字幕。当前 GPU 加速仅支持兼容的 NVIDIA 显卡，仍需要电脑上安装相应驱动。

在字幕设置中可以选择：

- **自动**：优先使用 NVIDIA GPU。如果加载模型或刚开始识别时遇到可恢复的 GPU 错误，软件会提示原因并尝试 CPU。
- **GPU**：仅使用显卡，失败时显示错误，由你决定是否改用 CPU。
- **CPU**：使用处理器识别，不依赖显卡加速。

识别过程中已保存的字幕会保留。CPU 和 GPU 路径已在测试电脑上运行通过，其他配置的兼容性仍在收集反馈。

## 模型选择

| 模型 | 下载大小 | 使用建议 |
|---|---:|---|
| base | 约 148 MB，已随包提供 | 首次使用建议从它开始，占用资源较少 |
| small | 约 486 MB，按需下载 | base 的效果不理想时，可以用同一段视频对比识别结果 |
| large-v3-turbo | 约 1.62 GB，按需下载 | 占用资源更多，建议先试短视频，观察识别效果和耗时 |

表中是模型文件大小，运行时还需要内存或显存。模型越大并不意味着每段录音都识别得更准；专有名词和数字仍需核对。软件会记住所选模型；自定义模型需要使用兼容 faster-whisper / CTranslate2 的格式。

模型来源：[base](https://huggingface.co/Systran/faster-whisper-base)、[small](https://huggingface.co/Systran/faster-whisper-small)、[large-v3-turbo](https://huggingface.co/dropbox-dash/faster-whisper-large-v3-turbo)。

## 可选：Qwen3-ASR 千问

标准安装包不包含千问运行环境、识别模型或对齐器，也不会在选择模型时自动下载它们。不需要千问时可以继续使用随包 base 或可选 Whisper 模型。

- 模型与对齐器文件合计约 **5.93 GB**，只在你点击「下载模型」后准备。
- 已测试的独立运行环境约占 **3.5 GB 磁盘**；这不是压缩下载大小。准备过程中还需为下载缓存预留空间。
- 模型文件齐全与运行环境就绪分别检查；已有文件保留。首次加载可能需要几十秒，耗时取决于设备和缓存。

官方来源：[Qwen 原生 Transformers 使用说明](https://huggingface.co/Qwen/Qwen3-ASR-1.7B-hf#usage)、[识别模型](https://huggingface.co/Qwen/Qwen3-ASR-1.7B-hf)、[时间对齐模型](https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B-hf)。VidSage 使用固定模型修订和文件校验；手动下载任意版本不等于本机已就绪。

已有兼容环境时，在「设置 → 字幕 → 本地字幕识别」选择千问，再点「选择千问环境…」，选中该环境的 python.exe。配置完成后再检查或下载模型，最后选择「使用此模型」。本机识别不发送音频到云端。

<details>
<summary>需要自行准备环境时：Windows 高级操作</summary>

先从 [Python 官方网站](https://www.python.org/downloads/windows/)安装 Python 3.12 x64。使用独立虚拟环境，避免修改 ComfyUI 或其他软件的 Python。下面命令只在你自行执行时下载依赖：

```powershell
$taskQwenEnvironment = Join-Path $env:LOCALAPPDATA 'VidSage\QwenRuntime'
py -3.12 -m venv $taskQwenEnvironment
$taskQwenPython = Join-Path $taskQwenEnvironment 'Scripts\python.exe'
# 将此处替换为当前 VidSage 版本目录中的实际锁定文件路径
$taskQwenRequirements = '程序版本目录\resources\app\runtime\host\tools\asr\qwen3-requirements.lock'
& $taskQwenPython -m pip install --require-hashes -r $taskQwenRequirements
```

依赖从锁定的 PyPI/PyTorch 上游地址获取，并核对 SHA256。下载量较大，速度取决于网络；失败后保留已有环境，检查错误后再继续。不要取消校验或随意替换依赖版本。

完成后，在软件中选择上述 Scripts\python.exe。随包锁定版本组合已通过本机依赖导入和短样本识别；其他设备上的全新联网准备尚未验收。当前已测 GPU 环境需要兼容 NVIDIA 显卡及驱动；其他硬件上的千问性能与兼容性尚未确认。

</details>

## AI 分析与字幕识别

生成本地字幕无需 AI 账号。分析、问答和翻译需要在「AI 服务」中配置自己的 API、连接 ChatGPT，或使用受支持的本机服务。云服务的费用和额度由服务商决定。

本版本暂未提供云端音频转录。ChatGPT 登录用于文本分析、问答和翻译。

识别失败时，请记录模型、出错步骤和电脑配置，按[反馈指南](FEEDBACK.zh-CN.md)提交问题。

技术来源：[Whisper](https://github.com/openai/whisper)、[faster-whisper](https://github.com/SYSTRAN/faster-whisper)、[CTranslate2](https://opennmt.net/CTranslate2/hardware_support.html)。
