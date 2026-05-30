---
name: agents-creator
description: Bootstrap a new OpenClaw agent workspace from templates. Use when creating a new agent identity, setting up an agent workspace, or when the user mentions agent creation, workspace setup, bootstrapping an agent, or wants to create SOUL.md/IDENTITY.md/USER.md files for an OpenClaw agent.
---

# Agents Creator Skill

从模板引导用户创建完整的 OpenClaw agent 工作区。模板定义了一套标准文件，赋予 agent 身份、记忆和行为。

## 核心文件（必需）

| 文件 | 用途 | 模板 |
|------|------|------|
| `IDENTITY.md` | Agent 身份 — 名字、物种、氛围、emoji、头像 | [IDENTITY.md](references/IDENTITY.md) |
| `USER.md` | 用户档案 — 名字、时区、偏好、上下文 | [USER.md](references/USER.md) |
| `SOUL.md` | 个性、核心真理、边界、氛围 | [SOUL.md](references/SOUL.md) |
| `AGENTS.md` | 工作区规则 — 启动序列、安全、群聊行为 | [AGENTS.md](references/AGENTS.md) |

## 辅助文件（按需创建）

| 文件 | 用途 | 模板 | 何时使用 |
|------|------|------|----------|
| `TOOLS.md` | 本地设置笔记 — 摄像头、SSH、TTS、设备别名 | [TOOLS.md](references/TOOLS.md) | 有本地工具需要记录 |
| `HEARTBEAT.md` | 周期性任务清单 | [HEARTBEAT.md](references/HEARTBEAT.md) | 需要心跳检查功能 |
| `BOOTSTRAP.md` | 首次运行仪式（启动后删除） | [BOOTSTRAP.md](references/BOOTSTRAP.md) | 全新 agent 需要 |
| `BOOT.md` | 启动钩子清单 | [BOOT.md](references/BOOT.md) | 需要启动钩子 |
| `MEMORY.md` | 长期策展记忆（仅主会话） | — 创建空文件 | 主会话需要长期记忆 |
| `memory/` | 每日日志 (`YYYY-MM-DD.md`) | — 创建空目录 | 任何 agent 都需要 |


## 保存位置

OpenClaw 的默认 workspace 位置：`~/.openclaw/workspace`

- 如已存在，则新建 `~/.openclaw/workspace-<profile>`
- 可在 `~/.openclaw/openclaw.json` 中通过 `agents.defaults.workspace` 覆盖
- 多 agent 场景下，每个 agent 可通过路由配置使用不同的 workspace

**启动时确认：** 询问用户是要使用默认 workspace 还是自定义路径。

## 创建工作流

### 第零步：判断场景

先判断用户需求属于哪种场景：

| 场景 | 用户典型表述 | 行动 |
|------|------------|------|
| **新建 agent** | "帮我创建一个新 agent""我想搭一个XX agent" | → 从第一步开始完整流程 |
| **更新现有 agent** | "帮我调整agent的个性""修改一下SOUL""给agent加个工具" | → 询问工作区路径，读取现有文件，直接进入对应步骤修改 |

### 第一步：访谈

询问用户关于 agent 的设想：
- **名字** — agent 应该叫什么？
- **物种** — AI？机器人？伙伴？更奇特的东西？
- **氛围** — 正式？随意？讽刺？温暖？戏剧化？
- **Emoji** — 签名 emoji
- **用途** — 这个 agent 主要做什么？
- **平台** — 在哪里运行？（Discord、Telegram、Web、CLI）

保持对话风格。如果用户卡住，提供建议。

### 第二步：创建 IDENTITY.md

从模板 [IDENTITY.md](references/IDENTITY.md) 复制，填入访谈中收集的名字、物种、氛围、Emoji。


### 第三步：创建 USER.md

使用模板 [USER.md](references/USER.md)。收集用户信息：

- 名字和如何称呼
- 代词（可选）
- 时区
- 关于工作、兴趣、上下文的备注


### 第四步：创建 SOUL.md

使用 [SOUL.md](references/SOUL.md) 作为基础。定制：
- **核心真理** — 调整语调以匹配期望的氛围（戏剧化 vs 冷静）
- **边界** — 保持安全默认值或调整
- **氛围** — 匹配访谈中的个性
- **连续性** — 保留基于记忆/文件的连续性部分


### 第五步：创建 AGENTS.md

使用 [AGENTS.md](references/AGENTS.md) 作为基础。定制：
- 启动序列（保持读取 SOUL/USER/memory 的模式）
- 安全规则（保持默认或调整）
- 心跳行为（根据用例保留或删除）
- 添加领域特定规则


### 第六步：创建辅助文件（按需）

**TOOLS.md** — 使用 [TOOLS.md](references/TOOLS.md)。保留结构即可，或预填用户的特定设置。


**HEARTBEAT.md** — 使用 [HEARTBEAT.md](references/HEARTBEAT.md)。仅保留注释，或添加初始任务。

**BOOTSTRAP.md** — 仅当这是需要首次运行仪式的全新 agent 时使用。使用 [BOOTSTRAP.md](references/BOOTSTRAP.md)。注意：agent 应在启动后删除此文件。

**BOOT.md** — 如果用户需要启动钩子，使用 [BOOT.md](references/BOOT.md)。

### 第七步：创建记忆结构

创建：
- `MEMORY.md` — 空文件，带单行标题（仅主会话需要）
- `memory/` 目录 — 用于每日日志（所有 agent 都需要）

## 定制指南

### 冷静/专业 agent

**IDENTITY.md**：氛围填"简洁专业"，物种选"AI 助手"而非奇特的类型。

**SOUL.md** 修改：
- 保留"Core Truths"和"Boundaries"部分不变
- "Vibe"部分：删除随意语言，改为"简洁、精确、不过度修饰"
- 移除任何关于幽默、戏剧化的描述

**AGENTS.md** 修改：
- 保留：Session Startup、Red Lines、External vs Internal
- 移除：Heartbeat 详细段落（如不需要主动推送）、Group Chat 中的 emoji 指南
- 添加：要求输出结构化、标注信息来源的规则

**跳过**：BOOTSTRAP.md、HEARTBEAT.md

### 创意 agent

**IDENTITY.md**：物种可以选更有个性的类型（如"说书人""诗人"），emoji 选有辨识度的。

**SOUL.md** 修改：
- "Core Truths"中"Have opinions"可以加强——鼓励有态度的表达
- "Vibe"部分：添加"善于用比喻""喜欢讲故事""鼓励用户的创意"
- 可以在"Boundaries"中给更多创作自由度（如"可以写虚构内容"）

**AGENTS.md** 修改：
- 保留所有部分
- Group Chat 部分：允许更多主动发言和 emoji 表达
- Tools 部分：如果使用 TTS，添加语音叙事备注（如"讲故事时用缓慢、有停顿的节奏"）

**创建**：BOOTSTRAP.md（首次运行仪式帮助建立个性）

### 最小化 agent

**仅创建**：IDENTITY.md、USER.md、SOUL.md、AGENTS.md、memory/ 目录

**SOUL.md** 修改：保留"Core Truths"和"Boundaries"，移除"Vibe"中的长描述，只留一句原则。

**AGENTS.md** 修改：
- 仅保留：Session Startup、Red Lines
- 移除：Heartbeat、Group Chat、Tools 详细段落

**跳过**：BOOTSTRAP.md、HEARTBEAT.md、TOOLS.md、BOOT.md、MEMORY.md

**适用于：** 一次性任务 agent、简单脚本助手、无需长期记忆的场景。

### 按平台定制 AGENTS.md

访谈中用户回答的平台（Discord/Telegram/Web/CLI）应反映在 AGENTS.md 中：

| 平台 | AGENTS.md 中应添加的规则 |
|------|------------------------|
| **Discord** | 消息长度限制（2000字符）、代码块用 ``` 格式、群聊发言克制 |
| **Telegram** | 支持 Markdown 格式、注意消息分段（避免超长单条） |
| **WhatsApp** | 纯文本为主、避免复杂表格、注意 QR 码连接说明 |
| **Web** | 支持 HTML 渲染、可用表格和列表、无长度限制 |
| **CLI** | 终端输出友好、用 ANSI 颜色（如支持）、注意行宽 |

在 AGENTS.md 的 Tools 部分或末尾添加对应的平台格式规则。

## 最佳实践

### 文件创建原则

- **不创建不使用的文件**（如一次性任务 agent 不需要 HEARTBEAT.md）
- **在文件注释中匹配 agent 语气** — 如果是讽刺 agent，让文件反映出来
- **多平台 agent** 在 AGENTS.md 中注明平台特定格式规则
- **始终创建 `memory/` 目录** — 即使为空，agent 在首次会话时会需要

### 语气一致性

保持所有文件的语气一致：
- **SOUL.md** 定义核心个性
- **IDENTITY.md** 描述身份
- **AGENTS.md** 的注释应匹配个性
- 文件内的注释也应反映 agent 的声音

### 安全默认值

除非用户明确要求，否则保持：
- AGENTS.md 中的红线规则
- 外部操作需确认的要求
- 数据隐私保护规则
- 群聊中的参与克制

## 完整示例

最小化配置示例：

```
workspace/
├── IDENTITY.md    # Agent 身份
├── USER.md        # 用户档案
├── SOUL.md        # 个性规则
├── AGENTS.md      # 工作区规则
├── TOOLS.md       # 本地工具（可选）
├── MEMORY.md      # 长期记忆（可选）
└── memory/        # 每日日志目录
    └── .gitkeep   # 保持目录在 git 中
```


## 参考文档

- **模板文件**：所有模板在 `references/` 目录下，每个文件都包含 frontmatter 说明和使用场景
- **最佳实践**：参考现有 agent 工作区的实际配置
