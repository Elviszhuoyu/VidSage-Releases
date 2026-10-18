<p align="center"><img src="docs/assets/release/app-icon.svg" width="64" height="64" alt="VidSage"></p>
<h1 align="center">VidSage 脉络</h1>
<p align="center"><strong>看视频，也理清思路。</strong><br>视频学习播放器，把字幕、笔记与 AI 分析放在视频旁边。</p>
<p align="center"><strong>简体中文</strong> · <a href="README.en.md"><strong>English</strong></a></p>
<p align="center"><img src="docs/assets/release/windows.svg" alt="Windows 11 x64"> <img src="docs/assets/release/languages.svg" alt="中文界面 · English docs"> <img src="docs/assets/release/preview.svg" alt="0.1.80 Public preview"></p>

<p align="center"><a href="docs/GETTING_STARTED.zh-CN.md">开始使用</a> · <a href="docs/HARDWARE.zh-CN.md">硬件与模型</a> · <a href="docs/FEEDBACK.zh-CN.md">反馈问题</a> · <a href="docs/PRIVACY.md">隐私与授权</a></p>

> **0.1.80 首次公开测试包现已提供下载。** 前往 [GitHub Release](https://github.com/Elviszhuoyu/VidSage-Releases/releases/tag/v0.1.80) 获取完整安装包、SHA256 和第三方对应源码材料。首版未签名，请按安装指南核对来源和摘要。下方保留 0.1.77 界面示意图。

## 做这个软件的起点

我最初做它，是因为自己在看金融学和一些专业课程时，经常遇到这样的时刻：视频已经往下讲了，我还在想上一个概念到底是什么意思。

有了 AI，我可以把难懂的部分拆开，换个说法问一遍，再回到视频里核对。但网页、插件、笔记之间来回切换，总会打断思路。我想要一个自己用着舒服的桌面工具，让视频、字幕、提问和笔记待在一起。无论是本地保存的课，还是 B站、YouTube 上支持的视频，都能边看边想，把知识慢慢变成自己的理解。

这就是我做 VidSage 的起点。也希望它能让你的学习过程轻松一点。

![VidSage 首页与轻量上手引导](docs/assets/release/home.png)

## 主要功能

- 使用平台已有字幕、导入字幕，或在本机生成字幕。
- 根据字幕分析、提问，点击时间回到原视频核对。
- 留下笔记与分析资料，之后继续阅读和检索。
- 选择 API、ChatGPT 云授权或受支持的本机服务。媒体账号可跳过，本地播放不依赖 AI 账号。

首次打开时，右上角的上手指引可以帮助你配置服务和字幕，也可以直接跳过。

![四个单行设置分类](docs/assets/release/settings.png)

## 系统要求

当前支持 **Windows 11 x64**，安装和解压至少预留 **6 GB** 空间。安装包已包含本地字幕所需的 base 模型。可以使用 CPU 识别字幕，兼容的 NVIDIA 显卡可提供 GPU 加速。建议先用一段短视频试用。

| 想做的事 | 从这里开始 |
|---|---|
| 看视频、读已有字幕 | 直接打开媒体，无需 AI 账号 |
| 本地生成字幕 | 先用随包 base；small 和 large-v3-turbo 按需下载 |
| AI 分析、问答、翻译 | 配置自己选择的服务，确认费用与内容发送范围 |
| 判断配置是否适合 | 查看[硬件与模型说明](docs/HARDWARE.zh-CN.md)，先试一段短视频 |

最低内存需求和较老处理器的兼容性仍需测试。详细说明见[系统要求与字幕模型](docs/HARDWARE.zh-CN.md)。

## 安装与更新

从本仓库 [0.1.80 Release](https://github.com/Elviszhuoyu/VidSage-Releases/releases/tag/v0.1.80) 获取完整 Setup 并核对 SHA256。首版未签名，Windows 可能显示未知发布者或安全提示；部分设备策略可能阻止运行。请先核对下载来源，遇到不明或恶意软件提示时停止安装，不要关闭系统防护。

普通用户只需下载 EXE 安装包，无需下载源码 ZIP 或安装开发工具。在「关于 → 更新与安装」检查新版本；关闭播放器后，运行新版安装包并选择原目录。更新和卸载默认保留个人资料。

[安装、校验与四步上手 →](docs/GETTING_STARTED.zh-CN.md)

## 隐私与反馈

本地字幕识别在电脑上运行。使用云端分析、问答或翻译时，软件会在授权后向你选择的服务发送字幕和必要上下文。

软件保留有限的本机运行记录，不会自动上传。遇到问题，可以在「关于 → 报告问题」检查并导出诊断包，再自行提交。**GitHub Issues 对所有人公开；图片和图片元数据不会自动脱敏。**

[如何写清问题、检查材料并提交反馈 →](docs/FEEDBACK.zh-CN.md) · [完整隐私说明](docs/PRIVACY.md)

## 支持作者

如果 VidSage 帮到了你，欢迎请作者喝杯咖啡。金额随心，感谢每一份支持；是否打赏不影响任何功能。

<table>
<tr><td align="center"><strong>微信支付 · WeChat Pay</strong></td><td align="center"><strong>支付宝 · Alipay</strong></td></tr>
<tr><td align="center"><img src="docs/assets/release/wechat-qr.png" width="184" alt="微信支付收款码 / WeChat Pay donation QR"></td><td align="center"><img src="docs/assets/release/alipay-qr.png" width="184" alt="支付宝收款码 / Alipay donation QR"></td></tr>
</table>

软件内「关于 → 支持作者」也可以打开收款码。打赏不授予二次开发或再分发许可。

## 使用与授权

**原创代码保留权利，二次开发须事先取得作者书面授权。** 正式发布的官方测试包可免费体验。应用源码和开发历史保持私有；GitHub 平台内权利及第三方许可证另行适用。详见[使用与版权声明](COPYRIGHT.md)。

识别、翻译与分析可能出错，尤其是数字和专有名词。重要内容请回到原视频核对；仅处理你有权访问与使用的内容。
