# Rigi-All 简体中文汉化

Blender 绑定插件 [Rigi-All](https://github.com/hisprofile/rigi-all) 的简体中
文汉化版本，修正了原汉化包中的大量机翻错误。

## 来源声明

| 角色 | 来源 |
|---|---|
| **原插件** | [hisanimations/rigi-all](https://github.com/hisprofile/rigi-all)（GPL-3.0） |
| **汉化基底** | [荣枯CG](https://www.rong.cool) — Rigi-All 1.6.0 汉化版 |
| **修正** | DSH |

本项目遵循 GPL-3.0 协议，原插件作者与协议信息均完整保留。

## 这个版本做了什么

在荣枯汉化版基础上，修正了 **584 条**明显错误的机翻词条：

| 原文 | 原译（错误） | 修正后 |
|---|---|---|
| `Arms` | 武器 | **手臂** |
| `Make Arms` | 制造武器 | **生成双臂** |
| `Fuse Armatures` | 保险丝骨架 | **合并骨架** |
| `Make Spine` | 让脊椎 | **生成脊柱** |
| `Go Back` | 回去 | **返回** |
| `Make Right Fingers` | 做正确的手指 | **生成右手手指** |
| `isLeft` | 是左派 | **是否左侧** |
| `Remove Custom Property` | 移除海关财产 | **移除自定义属性** |
| `Property Name:` | 物业名称： | **属性名：** |
| `Widget` | 控件 | **控制形状** |

完整修正列表见 [`rongcool_i18n.py`](rongcool_i18n.py)。

## 安装

### 方式一：从 Blender 扩展安装（推荐）

1. 下载本仓库为 ZIP（Code → Download ZIP）
2. 解压后把 `rigi-all-cn` 文件夹重命名为 `rigi_all`
3. 压缩成 `rigi_all.zip`（注意：ZIP 内需直接是 `rigi_all/` 目录）
4. Blender → `编辑 → 偏好设置 → 获取扩展 → 右上角下拉 → 从磁盘安装`
5. 选择 ZIP 安装并启用

### 方式二：手动复制

把本仓库所有文件复制到：

```
%APPDATA%\Blender Foundation\Blender\<版本>\extensions\user_default\rigi_all\
```

然后在 `偏好设置 → 扩展` 中启用。

## 前提条件

- **必须启用 Rigify**（Rigi-All 依赖 Rigify 的功能）
- Blender 版本：**4.2+**（实测 5.3 可用）
- 界面语言需设为**简体中文**（`编辑 → 偏好设置 → 界面 → 翻译 → 语言`）

## 使用

安装启用后，在 3D 视口按 `N` 打开侧栏，找到 **Rigi-All** 页签。

### 快速上手

1. 新建或选中一个骨架（`Shift+A → 骨架`）
2. 物体模式下点 **初始化骨架**
3. 姿态模式下选中骨骼，依次点 **生成脊柱 / 生成双腿 / 生成双臂**
4. 最后点 **生成附加骨（最后一步！）**
5. 切回物体模式 → Rigify 面板 → **生成骨架**

### 按钮选中要求

| 按钮 | 需要选中 |
|---|---|
| 生成脊柱 | ≥ 2 根骨骼，骨盆须为骨链根 |
| 生成手臂 | 3 根骨骼（肩/上臂/前臂） |
| 生成腿部 | 4 根骨骼（胯/大腿/小腿/脚） |
| 生成手指 | 一整条手指骨链 |

## 已知问题

- `__init__.py` 中的 `bl_info` 已被汉化包改为
  `Rigi-All-里吉-奥尔-荣枯汉化`，所以插件列表中显示的是中文名
- 翻译使用 Blender 官方 `bpy.app.translations` 机制，
  **不修改插件任何核心逻辑**

## 更新说明

- 本仓库基于 **Rigi-All 1.6.0**
- 官方发布新版本时，本仓库不会自动同步；需要手动合并汉化

## 协议

GPL-3.0-or-later，详见 [LICENSE](LICENSE)。
