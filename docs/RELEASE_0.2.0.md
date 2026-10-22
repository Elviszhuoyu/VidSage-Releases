# VidSage 0.2.0 · 视频学习与日常内容整理

VidSage 是把视频、字幕、AI分析、问答和笔记放在一起的Windows播放器。0.2.0让长视频分析更有反馈，补齐用量统计、字幕模型选择和播放细节；课程之外，也可整理生活、娱乐、汽车、美食、数码、穿搭和宠物等带解说内容。

## 下载与安装

普通用户只需下载 **[VidSage-0.2.0-win11-x64-Setup.exe](https://github.com/Elviszhuoyu/VidSage-Releases/releases/download/v0.2.0/VidSage-0.2.0-win11-x64-Setup.exe)**（约952MB）。这是完整安装包，包含播放器、本地字幕运行库和base模型，无需开发环境。

Windows 11 x64；处理器需支持AVX2。安装和临时解压建议预留至少6GB。首次安装或从0.1.96及更早版本升级，均使用这个完整Setup；升级保留资料和模型。安装包未签名。

## 新增

- **用量与费用看板**：按任务和模型查看请求、Token及API费用估算，默认人民币；提供柱状、热力和趋势视图。ChatGPT订阅用量单独记录。
- **公开评论总结与追问**：查看当前B站视频的有限顶层评论样本，确认后分析；结论带评论编号，评论观点与视频事实分开。
- **播放与界面**：支持中英界面切换、Windows打开方式登记、在线清晰度选择和右键播放统计。
- **兼容内容更新**：校验并复用本机已有程序文件，减少后续重复下载；完整离线与GPU组件继续保留。

## 优化

- 长字幕分段最多两路并行，减少重复输入与整片重写；显示真实已用时间、处理范围、已返回段数和接收状态。
- 本机112分钟课程样本由约7分34秒降到约4分24秒，输入Token较旧记录少约17%；实际耗时和用量随视频、模式及服务变化。
- 字幕模型按“可使用、未下载、缺少运行环境”展示；模型文件和运行环境分别说明，减少新手误选。
- 热力图适应侧栏宽度，趋势改为无常驻圆点的平滑曲线；费用说明更简洁，应用默认使用深色图标。

## 修复

- 长字幕输出截断、流式响应完成判定，以及超时和取消状态混淆。
- 左右侧栏限位反向不灵、部分拖动区域被视频遮挡，以及缩放指针残留。
- 平台字幕语言误选、自动字幕来源标识，以及部分分析出现多余分段结束叙述。
- 更新交接与重开反馈，并补齐许可、来源说明和卸载保留资料提示。

当前为公开测试版；识别、翻译与AI结果可能出错，请回看原视频核对。

[开始使用](https://github.com/Elviszhuoyu/VidSage-Releases/blob/main/docs/GETTING_STARTED.zh-CN.md) · [完整功能](https://github.com/Elviszhuoyu/VidSage-Releases/blob/main/docs/FEATURES.zh-CN.md) · [反馈问题](https://github.com/Elviszhuoyu/VidSage-Releases/issues)

<details><summary>校验值与其他附件</summary>

完整Setup SHA256：`eefd69d4b9ca5e8bbf19f616e3b217d9595cedb75b39a203256db3ceaacc2a3e`

`Content-Setup.exe`、`.vsp`和内容清单用于软件更新，不能单独作为完整安装包。第三方源码和许可索引供有需要的人查阅，普通用户无需下载。

</details>

## English

VidSage 0.2.0 brings video, captions, AI analysis, questions and notes into one Windows player. Use the full **Setup.exe** above for installation and the first upgrade from 0.1.96 or earlier.

- Added per-model usage and cost estimates, CNY by default, with activity charts; subscription usage stays separate from API costs.
- Added bounded public Bilibili comment summaries and follow-up questions with sample citations.
- Added Chinese/English UI, Windows file associations, available online quality choices and playback statistics.
- Compatible content updates verify and reuse installed files. Offline and GPU components remain included.
- Long transcripts use up to two cloud sections in flight, less repeated input and visible processing status. One local 112-minute sample improved from about 7m34s to 4m24s with about 17% fewer input tokens; results vary.
- Model readiness, charts, dark icons, sidebar dragging, caption selection and interrupted-generation recovery are clearer and more reliable.

Windows 11 x64 with AVX2; reserve at least 6GB. Unsigned public preview. Captions, translations and AI results may be wrong; check important points in the original video.
