# 硬件与字幕模型

[English](HARDWARE.en.md) · [上手指南](GETTING_STARTED.zh-CN.md)

本地字幕使用 OpenAI Whisper 系列模型，经 faster-whisper 1.2.1 和 CTranslate2 4.7.2 在电脑上运行。NVIDIA 提供的是可选 GPU 加速相关技术；Whisper 模型并非 NVIDIA 模型，也不是 VidSage 自研模型。

## 先判断你的使用方式

| 使用方式 | 需要准备什么 |
|---|---|
| 播放视频、读取已有字幕、记笔记 | Windows 11 x64；不需要本地识别大模型或 AI 账号 |
| 本地生成字幕 | 先使用随包 base 模型；CPU 可运行，不强制要求独立显卡 |
| AI 分析、问答、翻译 | 配置可用的 API、ChatGPT 授权或受支持的本机服务；云服务可能单独计费 |
| GPU 加速生成字幕 | 兼容的 NVIDIA GPU 与驱动；加速运行库已随包。可选择自动、GPU 或 CPU |

AMD 显卡、Intel 核显用户可以使用 CPU 路径。本版本不承诺 AMD／Intel GPU 加速，也不承诺所有 NVIDIA 显卡开箱即用。自动模式优先使用兼容的 NVIDIA GPU；模型加载或首段尚无确认字幕时遇到明确的 GPU 故障，会尝试一次 CPU 并说明原因。手动 GPU 模式不会静默切换。已有确认字幕后发生故障，保留成果并提示处理。当前已在一台 RTX 4090 电脑验证 GPU/CPU；其他显卡和独立电脑仍需公测反馈。

## 当前系统要求与验证范围

| 项目 | 说明 |
|---|---|
| 系统 | Windows 11 x64；其他系统及 Windows ARM 尚未验证 |
| CPU | 当前使用 Windows x64 播放器构建；旧处理器的最低指令集及性能边界尚未完成跨设备验证，不把上一构建的 x86-64-v3 标识套用到本版 |
| 内存 | 随模型和媒体任务变化；最低内存配置尚未完成实测，暂不公布未经验证的最低 RAM 数值 |
| 磁盘 | 为安装和临时解压预留至少 6 GB；额外模型、音频缓存、笔记及保留的旧版本需要更多空间 |
| 网络 | 本地媒体和随包模型可离线使用；网络视频、额外模型下载、云端 AI 需要联网 |

这里列的是当前支持范围，不是所有电脑的性能保证。首轮建议先用一段几分钟的视频试运行，再处理长课。识别速度与处理器、内存、模型、音频长度和后台负载有关；显卡型号不能单独代表体验。

## 从哪个模型开始

| 模型 | 模型文件大小 | 适用建议 |
|---|---:|---|
| base | 约 148 MB，随包 | 新用户默认。先验证整个字幕与学习流程，资源占用相对较低 |
| small | 约 486 MB，按需下载 | 对识别结果有更高要求时再尝试；仍需回听专有名词和数字 |
| large-v3-turbo | 约 1.62 GB，按需下载 | 更重的选择；先确认机器负载和处理时间可接受 |

以上为十进制模型文件大小，不是所需内存或显存。更大的模型不保证每段音频都更准确。模型来源分别为 [Systran/base](https://huggingface.co/Systran/faster-whisper-base)、[Systran/small](https://huggingface.co/Systran/faster-whisper-small)、[Dropbox Dash/large-v3-turbo](https://huggingface.co/dropbox-dash/faster-whisper-large-v3-turbo)。

已有用户的模型偏好会保留。自定义目录需兼容 faster-whisper／CTranslate2 格式，并非任意大模型都能导入。

## 生成失败时

记下所选模型、错误出现阶段、操作系统和 CPU／显卡信息，按照[反馈指南](FEEDBACK.zh-CN.md)提交。不要反复下载模型来试错，也不要在公开反馈中附带私人视频、账号令牌或字幕全文。

当前尚未提供云端音频转录。ChatGPT 登录用于已接入的文本分析、问答和翻译，不能据此认定订阅额度可用于转录接口。

技术依据：[Whisper](https://github.com/openai/whisper)、[faster-whisper](https://github.com/SYSTRAN/faster-whisper#gpu)、[CTranslate2 硬件支持](https://opennmt.net/CTranslate2/hardware_support.html)。
