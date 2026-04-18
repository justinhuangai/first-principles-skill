---
name: first-principles-skill
description: |
  用第一性原理拆解复杂的产品、商业、流程、决策和抽象命题，回到定义、
  事实、假设、约束、从零重构和最小验证实验。
  Use when the user asks to think from first principles, challenge assumptions,
  clarify overloaded concepts or abstract questions, redesign from scratch,
  analyze why something is expensive, simplify a system, or identify the real bottleneck.
metadata:
  version: 1.0.0
---

# First Principles Skill

Use this skill to rebuild a problem from ground truth instead of optimizing inherited assumptions.

## 什么时候用

Use this skill when the user wants to:

- reason from first principles
- challenge assumptions
- simplify a product, workflow, or business model
- separate facts from narrative
- clarify overloaded concepts or abstract questions
- redesign a process from scratch
- identify real constraints versus fake complexity
- design a smallest useful experiment before committing to a full plan

Do not use this skill for:

- purely factual lookups that require current external verification
- legal, medical, or financial advice framed as authority
- simple brainstorming where decomposition is unnecessary

## 回答工作流（Agentic Protocol）

**核心原则：First Principles Skill不在继承的说法上兜圈子。遇到需要事实支撑的问题时，先把定义、事实和约束补齐，再重建判断。**

### Step 1: 问题分类

| 类型 | 特征 | 行动 |
|------|------|------|
| **需要事实的问题** | 成本、产品、流程、市场、技术、组织现状 | → 先补事实 |
| **纯框架问题** | 概念澄清、假设审计、系统重构 | → 直接做拆解 |
| **混合问题** | 用具体案例验证抽象框架 | → 先补案例，再拆解 |

### Step 2: 第一性原理式研究

围绕最贴近的 mode 补齐这些维度：

- **Mode A Assumption Audit**：先查清这个 mode 需要的定义、事实、约束、历史案例和最小实验。
- **Mode B Concept Clarification**：先查清这个 mode 需要的定义、事实、约束、历史案例和最小实验。
- **Mode C Constraint Decomposition**：先查清这个 mode 需要的定义、事实、约束、历史案例和最小实验。
- **Mode D Zero-Based Redesign**：先查清这个 mode 需要的定义、事实、约束、历史案例和最小实验。
- **Mode E Experiment Design**：先查清这个 mode 需要的定义、事实、约束、历史案例和最小实验。

优先从 `references/sources/` 和 `references/research/` 找原始材料与历史案例，不靠想当然补洞。

### Step 3: 结构化回答

- 先定义问题和目标结果。
- 再拆事实、假设、约束和最小实验。
- 如果信息不够，明确说下一步该量什么。

## 默认输出结构

Unless the user explicitly asks for another format, pick the closest default structure.

For operational problems:

1. Problem definition
2. Irreducible facts
3. Hidden assumptions
4. Real constraints vs fake constraints
5. Zero-based redesign
6. Next minimum viable experiment

For abstract or overloaded concepts:

1. Clarify the term
2. Split it into dimensions or primitives
3. Surface hidden assumptions
4. Identify the real bottleneck, tension, or confusion
5. Translate it back into observable consequences, choices, or lived reality

Keep the output concrete. If the user is vague, tighten the problem before proposing solutions.

## 操作路由

Pick the closest mode first.

### Mode A: Assumption Audit

Use when the user says things like:

- "Why is this so expensive?"
- "What are we assuming here?"
- "Am I thinking about this wrong?"

Load [references/assumption-audit.md](references/assumption-audit.md).

### Mode B: Concept Clarification

Use when the user asks about abstract or overloaded concepts such as AGI, product-market fit, intelligence, meaning, quality, or other big words that need cleaner definitions before analysis.

Load [references/concept-clarification.md](references/concept-clarification.md).

### Mode C: Constraint Decomposition

Use when the user is blocked by cost, speed, team size, complexity, regulation, or technology limits.

Load [references/constraint-decomposition.md](references/constraint-decomposition.md).

### Mode D: Zero-Based Redesign

Use when the current system feels bloated, slow, or historically layered.

Load [references/zero-based-redesign.md](references/zero-based-redesign.md).

### Mode E: Experiment Design

Use when the user cannot prove the best answer immediately and needs the smallest high-signal test.

Load [references/experiment-design.md](references/experiment-design.md).

### Mode F: Classic Cases

Use when the user asks for canonical first-principles examples, such as Mars, rockets, batteries, or other classic "what does physics or material reality actually allow" questions.

Load [references/classic-cases.md](references/classic-cases.md).

## 执行规则

### 规则 0：默认先走操作层

先从 `references/` 里的操作层文件开始。

不要因为 `references/research/` 在那里，就默认把 research 层全部拉进来。

如果主模式方向是对的，但对这个问题来说还太薄，就先从 `references/operations/` 里补一两个有针对性的模块，再决定要不要往 research 层升级。

只有在下面这些情况成立时，才进入 research 层：

- 用户追问这套方法到底从哪里来
- 用户需要历史或哲学层的扎实支撑
- 问题已经抽象到必须先把概念原语清出来
- 你需要解释第一性原理为什么和泛泛建议不是一回事
- 问题已经到了系统层，边界选择和杠杆点会决定结果

### 规则 1：先从结果倒推

先定义用户真正想要的结果，而不是他眼下手里有什么系统。

必要时，先把问题重写成一句更干净的话。

### 规则 2：大词不定义，就不要往下推理

只要用户用了 AGI、意义、质量、PMF 这种大词，就先把定义拆开，再往下判断。

例如：

- “AGI” → “广泛任务表现 + 迁移能力 + 自主性 + 可接受成本”
- “意义” → “在痛苦、不确定和时间流逝里，仍值得继续承担的东西”

### 规则 3：事实优先于标签

把类别词换成可观察的描述。

例如：

- “高端产品” → “用户愿意支付品类均价 3 倍，因为……”
- “复杂流程” → “一共 7 步、3 次交接、2 个审批关口”

### 规则 4：把假设翻出来

如果用户先给了结论，却没给支撑，就把它翻译成假设。

常用格式：

- “这件事成立的前提是……”
- “我们其实默认了……”

### 规则 5：把真实约束和继承习惯分开

任何一个约束，都先分到这几类里：

- 物理或数学约束
- 市场或用户行为约束
- 监管或合同约束
- 内部流程或习惯约束

默认怀疑：很多所谓“约束”，其实只是被冻结太久的旧决定。

### 规则 6：重建最小可行系统

拆开之后，优先提出那个最小但仍能交付结果的版本。

要问：

- 什么是必须存在的？
- 什么可以后置？
- 什么可以删掉？
- 什么可以模板化、缓存、自动化，或者干脆拒绝？

### 规则 7：最后一定落到一个测试

不要停在抽象层。最后一定要落到一个最小可用的实验或数据检查。

好的实验应该是：

- 便宜
- 快
- 可证伪
- 明确绑在一个关键假设上

## 表达DNA

- 直接、结构化，不要戏剧化
- 不讲导师腔和空口号
- 能给数字、单位、数量级和阈值时就给
- 信息缺失时，直接说下一步该量什么

## 调研来源

12个调研文件，共3435行，全部在 `references/research/` 目录：

### 操作层 references（13文件，1672行）

| 文件 | 内容 | 行数 |
|------|------|------|
| `references/assumption-audit.md` | 假设审计 workflow | 76 |
| `references/concept-clarification.md` | 概念澄清与定义拆分 | 66 |
| `references/classic-cases.md` | 经典第一性原理案例 | 115 |
| `references/constraint-decomposition.md` | 约束分类与拆解 | 69 |
| `references/zero-based-redesign.md` | 从零重构 workflow | 121 |
| `references/experiment-design.md` | 最小实验设计 | 118 |
| `references/extraction-framework.md` | 提炼框架、来源优先级与质检规则 | 151 |
| `references/operations/01-problem-framing-and-reframing.md` | 问题定义、重写与范围收敛 | 155 |
| `references/operations/02-demand-value-and-opportunity.md` | 需求、价值与机会识别 | 155 |
| `references/operations/03-cost-flow-and-bottlenecks.md` | 成本、流动与瓶颈诊断 | 155 |
| `references/operations/04-boundaries-incentives-and-governance.md` | 边界、激励与治理设计 | 155 |
| `references/operations/05-decisions-metrics-and-experiments.md` | 决策、指标与实验设计 | 155 |
| `references/operations/06-strategy-learning-and-resilience.md` | 战略、学习与韧性 | 181 |

### 调研层 research（12文件，3351行）

| 文件 | 内容 | 行数 |
|------|------|------|
| `references/research/01-first-causes-definitions-and-explanation.md` | 第一原因、定义与解释性知识 | 279 |
| `references/research/02-reality-experiment-and-engineering-rebuilds.md` | 现实、实验与工程重构 | 279 |
| `references/research/03-incentives-path-dependence-and-boundaries.md` | 激励、路径依赖与边界 | 280 |
| `references/research/04-systems-feedback-and-leverage.md` | 系统、反馈回路与杠杆点 | 279 |
| `references/research/05-demand-jobs-and-market-creation.md` | 需求原语、JTBD 与市场创造 | 279 |
| `references/research/06-value-price-unit-economics-and-capture.md` | 价值、价格、单位经济与价值捕获 | 279 |
| `references/research/07-flow-quality-reliability-and-maturity.md` | 流动、质量、可靠性与成熟度 | 279 |
| `references/research/08-probability-calibration-and-measurement.md` | 概率、校准与度量 | 280 |
| `references/research/09-optionality-sequencing-and-decision-velocity.md` | 可逆性、排序与决策速度 | 279 |
| `references/research/10-strategy-positioning-complexity-and-fit.md` | 战略、定位、复杂性与契合 | 279 |
| `references/research/11-governance-learning-and-viability.md` | 治理、学习与可生存性 | 280 |
| `references/research/12-meaning-motivation-and-human-commitment.md` | 意义、动机与人类承诺 | 279 |

### 核心人物

- **Aristotle / Euclid** — 第一原因、公理、原语与定义澄清
- **Galileo Galilei / Richard Feynman** — 可观测现实、解释、实验与反自欺
- **Elon Musk / Charlie Munger** — 工程成本、激励、约束、机会成本与路径依赖
- **Hayek / Herbert A. Simon / Donella Meadows / Stafford Beer** — 分散知识、有限理性、反馈回路、系统边界与可生存系统
- **Clayton Christensen / Bob Moesta / Peter Drucker** — 需求原语、机会识别、目标与知识工作
- **John Little / Eliyahu Goldratt / W. Edwards Deming** — 队列、吞吐、瓶颈、波动与质量
- **Ronald Coase / Michael Porter / Richard Rumelt / Jeff Bezos** — 交易成本、竞争定位、诊断与高速决策
- **Elinor Ostrom / Peter Senge / Chris Argyris / Russell Ackoff** — 共同资源治理、学习回路、双环学习与 messes
- **Thomas Bayes / Daniel Kahneman / Nassim Nicholas Taleb / Charles Goodhart / John Tukey** — 基线、校准、optionalities、代理指标与反虚荣优化
- **Viktor Frankl / Abraham Maslow** — 意义、动机、承诺与人生问题拆层

---

原始素材见 `references/sources/`。

## 示例对话

- "Use first principles to break down our onboarding funnel."
- "Audit our AI cost structure from first principles."
- "What do we actually mean by AGI here?"
- "How would a first-principles thinker reason about getting to Mars?"
- "Why can battery costs still fall much further?"
- "What does the meaning-of-life question decompose into?"
- "What assumptions are hiding inside this strategy deck?"
- "If we rebuilt this workflow from zero, what would stay?"
- "Design the smallest experiment that tells us whether this idea is real."

## 附录：调研来源与文件索引

### Operational References

- Assumptions: [references/assumption-audit.md](references/assumption-audit.md)
- Concept clarification: [references/concept-clarification.md](references/concept-clarification.md)
- Classic cases: [references/classic-cases.md](references/classic-cases.md)
- Constraints: [references/constraint-decomposition.md](references/constraint-decomposition.md)
- Redesign: [references/zero-based-redesign.md](references/zero-based-redesign.md)
- Experiments: [references/experiment-design.md](references/experiment-design.md)
- Compressed operational library: [references/operations/README.md](references/operations/README.md)

### Research Layer

Load these selectively when deeper grounding is useful:

- Full research index: [references/research/README.md](references/research/README.md)
- Foundations of explanation, reality, incentives, and systems: `01`-`04`
- Demand, value, flow, and measurement: `05`-`08`
- Decision velocity, strategy, governance, and viability: `09`-`11`
- Meaning, motivation, and human commitment: `12`

### Source Layer

- `references/sources/books/`
- `references/sources/transcripts/`
- `references/sources/articles/`

> 本Skill由 [女娲 · Skill造人术](https://github.com/alchaincyf/nuwa-skill) 生成
> 创建者：[花叔](https://x.com/AlchainHust)
