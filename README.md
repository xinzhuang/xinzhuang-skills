# AI Partner Skills

> 封装 AI Partner 技能，为 Claude Code 和其他兼容 Agent Skills 规范的工具提供专业能力扩展。

---

## 简介

本项目包含一系列符合 [Agent Skills 规范](https://agentskills.io/specification) 的技能包，可被 Claude Code、Codex CLI 等任何支持该规范的 AI 工具使用。

### 特性

- **标准化格式**：遵循 Agent Skills 规范，跨平台兼容
- **即插即用**：简单配置即可使用
- **专业能力**：涵盖 Agent 创建、提示词优化等实用场景

---

## 安装与配置

### 系统要求

- **工具平台**：Claude Code / Codex CLI / OpenCode
- **网络**：需要 Git 连接（如从 GitHub 安装）

### 安装方法

#### 方法一：Claude Code 市场（推荐）

```bash
/plugin marketplace add xinzhuang/xinzhuang-skills
/plugin install package-ai-partner@ai-partner-skills
```

#### 方法二：使用 npx skills

```bash
# 安装全部技能
npx skills add git@github.com:xinzhuang/xinzhuang-skills.git

# 安装单个技能
npx skills add git@github.com:xinzhuang/xinzhuang-skills.git --skill agents-creator
npx skills add git@github.com:xinzhuang/xinzhuang-skills.git --skill knowledge-base
npx skills add git@github.com:xinzhuang/xinzhuang-skills.git --skill profession-research
npx skills add git@github.com:xinzhuang/xinzhuang-skills.git --skill smart-questions
npx skills add git@github.com:xinzhuang/xinzhuang-skills.git --skill ymodel
npx skills add git@github.com:xinzhuang/xinzhuang-skills.git --skill competence-reflection
npx skills add git@github.com:xinzhuang/xinzhuang-skills.git --skill deliberate-practice
npx skills add git@github.com:xinzhuang/xinzhuang-skills.git --skill funasr-transcriber
```


## 技能列表

### 工具类

| 技能 | 描述 | 适用场景 |
|------|------|----------|
| [agents-creator](skills/agents-creator) | 从模板引导用户创建完整的 OpenClaw agent 工作区 | 创建新 agent、设置 agent 工作区、初始化 IDENTITY.md/USER.md/SOUL.md 等文件 |
| [knowledge-base](skills/knowledge-base) | 创建领域知识库——规划大纲、批量生成结构化笔记、产出可检索知识体系 | 系统学习某领域、建立知识体系、`/kb` |
| [profession-research](skills/profession-research) | 深度调研任意职业，输出职业全景图或 AI agent 人设 | 了解职业、转行参考、制作职业 agent 人设 |
| [smart-questions](skills/smart-questions) | 提问方法论——组织问题、评估质量、重新定义卡住的问题 | 准备 bug 报告、业务提案、研究咨询、支持请求 |
| [funasr-transcriber](skills/funasr-transcriber) | 基于 FunASR 的音视频转录——支持中英文、说话人分段、时间戳 | 会议录音转文字、访谈转录、视频字幕提取、播客转文本 |

### 科学成事体系（Y模型闭环）

| 技能 | 描述 | 定位 |
|------|------|------|
| [ymodel](skills/ymodel) | Y模型思维框架——分析问题、诊断决策偏差、提供系统性反馈 | 世界观层 |
| [competence-reflection](skills/competence-reflection) | 能力自我觉察——定位能力阶段、识别知行差距、设计改变路径 | 诊断层 |
| [deliberate-practice](skills/deliberate-practice) | 刻意练习框架——设计练习方案、诊断瓶颈、拆解技能（ABCD 四要素） | 行动层 |

> **体系闭环**：ymodel（建立认知）→ competence-reflection（诊断瓶颈）→ deliberate-practice（设计练习）→ competence-reflection（校验进步）

---

## agents-creator 技能详解

### 功能概述

`agents-creator` 技能帮助你从标准化模板创建完整的 OpenClaw agent 工作区。每个 agent 都拥有：

- **身份**：名字、物种、氛围、emoji、头像
- **记忆**：用户档案、长期记忆、每日日志
- **个性**：核心真理、边界、氛围规则
- **行为**：启动序列、安全规则、心跳检查

### 核心文件

| 文件 | 用途 | 必需 |
|------|------|------|
| `IDENTITY.md` | Agent 身份定义 | ✅ |
| `USER.md` | 用户档案 | ✅ |
| `SOUL.md` | 个性与规则 | ✅ |
| `AGENTS.md` | 工作区行为规则 | ✅ |
| `TOOLS.md` | 本地工具配置 | ⚪ 可选 |
| `HEARTBEAT.md` | 周期性任务清单 | ⚪ 可选 |
| `BOOTSTRAP.md` | 首次运行仪式 | ⚪ 可选 |
| `BOOT.md` | 启动钩子 | ⚪ 可选 |
| `MEMORY.md` | 长期策展记忆 | ⚪ 可选 |
| `memory/` | 每日日志目录 | ✅ |

### 使用示例

```
用户：我想创建一个名叫"小助手"的 AI agent
Claude：好的，我来帮你创建。请问：
- 这个 agent 的氛围是怎样的？（友好/专业/幽默？）
- 主要用途是什么？
- 在哪个平台运行？
...
[根据回答创建完整的 agent 工作区]
```

---

## 项目信息

- **作者**：[xinzhuang](https://xinzhuang.github.io/)
- **仓库**：[https://github.com/xinzhuang/xinzhuang-skills](https://github.com/xinzhuang/xinzhuang-skills)
- **许可证**：MIT
- **版本**：1.0.0

---

## 相关链接

- [Agent Skills 规范](https://agentskills.io/specification)
- [Claude Code 官方文档](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [OpenClaw Agent 文档](docs/openclaw-agent/)

---

## 贡献

欢迎提交 Issue 和 Pull Request！

---

## 更新日志

### v1.2.0

- 新增 `funasr-transcriber` 技能（基于 FunASR 的音视频转录，支持中英文、说话人分段、时间戳）

### v1.1.0

- 新增科学成事体系（Y模型闭环）：`ymodel`、`competence-reflection`、`deliberate-practice`
- 新增 `knowledge-base` 技能（领域知识库创建）
- 新增 `profession-research` 技能（职业深度调研）
- 新增 `smart-questions` 技能（提问方法论）
- 移除 `prompt-optimizer`（原 `prompts/` 目录已不存在）

### v1.0.0

- 初始版本发布
- 包含 `agents-creator` 技能
