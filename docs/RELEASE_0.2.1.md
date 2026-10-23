# VidSage 0.2.1 · 观看、回看与保存

0.2.1 改善播放切换与列表操作，补齐在线封面、报告图片和免费长图导出。

## 下载与安装

普通用户只需下载 **[VidSage-0.2.1-win11-x64-Setup.exe](https://github.com/Elviszhuoyu/VidSage-Releases/releases/download/v0.2.1/VidSage-0.2.1-win11-x64-Setup.exe)**（约952MB）。完整安装包包含播放器、本地字幕运行库和 base 模型，无需开发环境。

Windows 11 x64；处理器需支持 AVX2。安装与临时解压请预留至少6GB。升级保留资料和模型。安装包未签名，Windows可能显示“未知发布者”。

## 新增

- **报告图片**：从报告生成配图，支持排队、取消、失败反馈和手动重新生成。图片可放大、拖动、全屏、另存和打开所在目录，历史版本保留。
- **免费长图导出**：将报告直接导出为 PNG，不调用 AI，也不需要生图额度。
- **图片存储管理**：查看图片占用，分别管理成品和临时文件。

## 优化

- 改善首次打开、快速切换和播放列表操作的响应，媒体加载中仍能取消或重新选择。
- 在线封面和标题按需加载，取消后及时停止；无痕与关闭历史记录时遵循对应缓存策略。
- 生图服务统一在设置中配置，报告内保留简洁操作；补齐保存、等待、成功和失败反馈。
- 优化窄侧栏、中英界面和不同 Windows 缩放下的布局与交互。

## 修复

- 快速选片时旧请求覆盖当前选择，以及部分播放器画面未及时显示的问题。
- 列表移除、撤销、缺失文件恢复和连续播放中的状态不一致。
- 图片窗口全屏与退出切换冲突，以及导出重复触发、取消后状态未恢复等问题。

AI 生图需要受支持的官方 OpenAI 或 Gemini API，按服务商规则计费与配额；ChatGPT 订阅授权和 DeepSeek API 不能直接用于此功能。Gemini 免费层级通常不提供所选生图模型的额度，请在服务商后台确认。免费报告长图不受这些额度限制。

本版本为公开测试版；字幕和 AI 输出可能出错，重要信息请回到原视频核对。

[开始使用](https://github.com/Elviszhuoyu/VidSage-Releases/blob/main/docs/GETTING_STARTED.zh-CN.md) · [反馈问题](https://github.com/Elviszhuoyu/VidSage-Releases/issues)

<details><summary>校验与其他附件</summary>

完整 Setup SHA256：`9cec357ca385a536b3f7b38976df8e9e12916851dad36bd62ca5a4333c3d5d44`

`Content-Setup.exe`、`.vsp` 和内容清单用于软件更新，不能单独作为完整安装包。源码引用与许可索引供有需要的人查阅，普通用户无需下载。

</details>

## English

VidSage 0.2.1 improves media switching, playlists and online covers. It adds report images, image viewing and storage management, plus free PNG report export with no AI call. Image generation requires a supported official OpenAI or Gemini API with the provider's billing and quota; a ChatGPT subscription or DeepSeek API does not supply this capability.

Download the full **Setup.exe** above. Windows 11 x64, AVX2 and at least 6GB free space are required. Updates retain personal data and models. This unsigned public preview can make mistakes; check important information against the source video.
