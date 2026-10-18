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

## AI 分析与字幕识别

生成本地字幕无需 AI 账号。分析、问答和翻译需要在「AI 服务」中配置自己的 API、连接 ChatGPT，或使用受支持的本机服务。云服务的费用和额度由服务商决定。

本版本暂未提供云端音频转录。ChatGPT 登录用于文本分析、问答和翻译。

识别失败时，请记录模型、出错步骤和电脑配置，按[反馈指南](FEEDBACK.zh-CN.md)提交问题。

技术来源：[Whisper](https://github.com/openai/whisper)、[faster-whisper](https://github.com/SYSTRAN/faster-whisper)、[CTranslate2](https://opennmt.net/CTranslate2/hardware_support.html)。
