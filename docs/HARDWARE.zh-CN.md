# 硬件与字幕模型

[English](HARDWARE.en.md) · [上手指南](GETTING_STARTED.zh-CN.md)

本地字幕使用 OpenAI Whisper 系列模型，经 faster-whisper 1.2.1 和 CTranslate2 4.7.2 在电脑上运行。NVIDIA 提供的是可选 GPU 加速相关技术；Whisper 模型并非 NVIDIA 模型，也不是 VidSage 自研模型。

## 先判断你的使用方式

| 使用方式 | 需要准备什么 |
|---|---|
| 播放视频、读取已有字幕、记笔记 | Windows 11 x64；不需要本地识别大模型或 AI 账号 |
| 本地生成字幕 | 先使用随包 base 模型；CPU 可运行，不强制要求独立显卡 |
| AI 分析、问答、翻译 | 配置可用的 API、ChatGPT 授权或受支持的本机服务；云服务可能单独计费 |
| GPU 加速生成字幕 | 兼容的 NVIDIA GPU、驱动及运行库；当前候选尚未完成独立 GPU 环境验收 |

AMD 显卡、Intel 核显用户可以使用 CPU 路径。本版本不承诺 AMD／Intel GPU 加速，也不承诺所有 NVIDIA 显卡开箱即用。当前设备选择为自动；GPU 初始化失败时，应用尚无自动重启 CPU 任务的保证。

## 当前系统要求与验证范围

| 项目 | 说明 |
|---|---|
| 系统 | Windows 11 x64；其他系统及 Windows ARM 尚未验证 |
| CPU | 当前播放器要求 CPU 和系统支持 **x86-64-v3**（包括 AVX2、FMA、BMI2 等指令及相应系统支持）。仅有 SSE 4.1 不够；这是随包播放器的限制。尚未覆盖所有旧处理器实测 |
| 内存 | 随模型和媒体任务变化；最低内存配置尚未完成实测，暂不公布未经验证的最低 RAM 数值 |
| 磁盘 | 为安装和临时解压预留至少 4 GB；额外模型、音频缓存、笔记及保留的旧版本需要更多空间 |
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

播放器 CPU 要求依据：[x86-64 psABI](https://gitlab.com/x86-psABIs/x86-64-ABI/-/blob/master/x86-64-ABI/low-level-sys-info.tex).
