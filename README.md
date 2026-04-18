**简体中文** | [English](./README_EN.md)

<div align="center">

# 第一性原理.skill

> *“当我们认为自己认识了一件事物的第一原因时，我们才说自己真正知道了它。”*  
> — 亚里士多德，《形而上学》I.1

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-0169CC)](https://openai.com/codex)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-CC785C)](https://claude.ai/code)
[![Nuwa](https://img.shields.io/badge/Made%20with-女娲.skill-orange)](https://github.com/alchaincyf/nuwa-skill)
[![Type: Topic Skill](https://img.shields.io/badge/Type-Topic%20Skill-green)](#效果示例)

<br>

把复杂问题拆回事实、约束、假设和实验。
适合成本拆解、系统重构、抽象命题澄清、最小验证实验设计。
提炼 4 个核心心智模型、8 条决策启发式、6 个场景路由、经典案例与现代应用。

[看效果](#效果示例) · [安装](#安装) · [蒸馏了什么](#蒸馏了什么) · [调研来源](#调研来源) · [致谢](#致谢) · [许可证](#许可证)

</div>

---

## 效果示例

### 问：人类如何前往火星？

```text
第一性原理 ❯ 先别从“太贵了”“太难了”或者现有航天工业怎么做开始。

            先把任务拆回几个不可回避的问题：
            - 怎样把足够的质量送出地球引力井？
            - 怎样在长途飞行里维持生命支持、能源和辐射防护？
            - 怎样在火星完成进入、下降与着陆？
            - 返程推进剂和补给，能不能在火星原位制造？
            - 哪些约束来自物理，哪些只是今天的工程路径太浪费？

            然后再往下问：
            - 火箭必须一次性使用吗？
            - 有多少质量其实不必都从地球带过去？
            - 哪些系统必须冗余，哪些只是旧设计习惯？
            - 真正昂贵的，是原材料，还是被一次性设计和补给链放大的系统成本？

            第一性原理不是先问“现在报价多少”，
            而是先把这件事重新定义成一个物理、工程和补给问题。

            成本当然重要，
            但它应该从任务架构里被推导出来，
            而不是在一开始就被当成唯一问题。
```

### 问：为什么电动车电池有机会继续大幅降价？

```text
第一性原理 ❯ 因为第一性原理不会先从“汽车行业一直这么贵”开始想。

            它会往下拆到材料层：
            - 电池包里真正值钱的物质是什么？
            - 镍、钴、锂、石墨、铝这些原材料理论成本是多少？
            - 现在的高价里，有多少是制造工艺和供应链结构的问题？

            如果原材料本身没有那么贵，
            那问题就不该被定义成“电动车天生贵”，
            而该被定义成“怎样把制造路径逼近材料极限成本”。

            这就是典型的第一性原理：从分子和材料往上重建，而不是从行业定价往下接受。
```

### 问：AGI 什么时候会到来？

```text
第一性原理 ❯ 先别急着预测年份，先定义你说的 AGI 是什么。

            如果 AGI 指：
            - 能在多数认知任务上接近人类平均水平
            - 能跨任务迁移
            - 能长期自主完成目标
            - 成本可以被社会大规模承受

            那这不是一个单点技术问题，而是能力、可靠性、工具使用、
            记忆、成本和部署边界共同收敛的问题。

            所以更好的问题不是“哪一年”，
            而是：现在离这几个条件分别还差多远，哪个才是真瓶颈？
```

### 问：我们的产品月费 49 美元，利润越来越薄，应该怎么优化？

```text
第一性原理 ❯ 先不要优化，先拆。

            49 美元里有哪些不可压缩成本？
            计算、存储、支付抽成、获客、客服、人工交付，分别占多少？

            哪些是物理成本，哪些是你现在的组织方式制造出来的成本？

            如果把产品从零重做，只保留「让用户得到结果」的最小路径，
            哪三个功能会先被删掉？

            优化一个不该存在的功能，是最高级别的浪费。
```

### 问：现在还有什么创业机会？

```text
第一性原理 ❯ 先别从“什么最火”开始找，而是从“哪里还又慢、又贵、又麻烦”开始拆。

            真正要拆的是：
            - 用户到底想完成什么任务？
            - 现有路径里，哪一步最慢、最贵、最令人厌烦？
            - 哪个环节大家默认必须这样做，其实只是旧路径留下来的习惯？
            - 哪些能力因为 AI、自动化或新分发方式，成本刚刚降到可以重写？

            真正的创业机会，往往不是凭空发明一个新需求，
            而是把一个旧需求用更短、更便宜、更简单的路径满足。

            所以先别问“做什么最火”，
            先问“哪一步最痛，而且现在第一次有条件被重写”。
```

### 问：人生的意义是什么？

```text
第一性原理 ❯ 先不要急着追求一个覆盖所有人的大答案。

            这个问题至少可以拆成几层：
            - 什么让生活值得继续投入？
            - 什么让人在痛苦和不确定里仍然愿意承担责任？
            - 什么东西不是短期快感，而是长期也不轻易崩塌？

            第一性原理在这里不是给你一句漂亮格言，
            而是逼你把“大词”拆回真实经验、注意力分配、
            承诺对象和持续行动。
```

---

## 安装

```bash
npx skills add justinhuangai/first-principles-skill
```

安装后可以直接说：

```text
从第一性原理看，AGI 真正的瓶颈是什么？
如果从零开始设计，这个产品哪些部分根本不该存在？
用第一性原理拆一下这个产品的成本
这个流程是不是建立在错误假设上？
```

---

## 蒸馏了什么

### 4个核心心智模型

| 模型 | 一句话 | 用途 |
|------|--------|------|
| **不接受继承价格** | 行业现状不是原始真相 | 用于成本、定价、制造问题 |
| **拆到物理或结果层** | 不从包装层思考，从材料/用户结果层思考 | 用于技术、产品、流程问题 |
| **区分真约束与路径依赖** | 很多“限制”只是冻结的旧决定 | 用于组织、流程、战略问题 |
| **用实验代替空谈** | 没证据时，不靠气势，靠最小测试 | 用于高不确定性决策 |

### 8条决策启发式

1. **先重写问题** — 说法不对，答案一定偏
2. **先找不可压缩事实** — 没有事实，就只有情绪和叙事
3. **所有结论先还原成假设** — 看清“这只在什么条件下成立”
4. **所有约束先分类** — 物理、经济、行为、组织、监管
5. **先删再优** — 删除不该存在的步骤，比优化旧步骤更值钱
6. **从结果往回拆** — 先定义用户要的结果，不先维护现有系统
7. **把大词拆成小问题** — 意义、AGI、创业机会，都先拆层
8. **最后必须落到一个实验** — 没有下一步动作，就还是抽象讨论

---

## 调研来源

12个调研文件，共3435行，全部在 [references/research/](references/research/) 目录：

### 调研层 research（12文件，3435行）

| 文件 | 内容 | 行数 |
|------|------|------|
| `references/research/01-first-causes-definitions-and-explanation.md` | 第一原因、定义与解释性知识 | 286 |
| `references/research/02-reality-experiment-and-engineering-rebuilds.md` | 现实、实验与工程重构 | 286 |
| `references/research/03-incentives-path-dependence-and-boundaries.md` | 激励、路径依赖与边界 | 286 |
| `references/research/04-systems-feedback-and-leverage.md` | 系统、反馈回路与杠杆点 | 286 |
| `references/research/05-demand-jobs-and-market-creation.md` | 需求原语、JTBD 与市场创造 | 286 |
| `references/research/06-value-price-unit-economics-and-capture.md` | 价值、价格、单位经济与价值捕获 | 286 |
| `references/research/07-flow-quality-reliability-and-maturity.md` | 流动、质量、可靠性与成熟度 | 286 |
| `references/research/08-probability-calibration-and-measurement.md` | 概率、校准与度量 | 287 |
| `references/research/09-optionality-sequencing-and-decision-velocity.md` | 可逆性、排序与决策速度 | 286 |
| `references/research/10-strategy-positioning-complexity-and-fit.md` | 战略、定位、复杂性与契合 | 286 |
| `references/research/11-governance-learning-and-viability.md` | 治理、学习与可生存性 | 286 |
| `references/research/12-meaning-motivation-and-human-commitment.md` | 意义、动机与人类承诺 | 286 |

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

## 致谢

这个 skill 基于 [女娲.skill](https://github.com/alchaincyf/nuwa-skill) 蒸馏与搭建。

---

## 仓库结构

```text
first-principles-skill/
├── README.md
├── README_EN.md
├── SKILL.md                              # 路由 + 执行规则
├── references/                           # 25文件（5023行）
│   ├── assumption-audit.md               # 假设审计（按需加载）
│   ├── concept-clarification.md          # 概念澄清（按需加载）
│   ├── classic-cases.md                  # 经典案例（按需加载）
│   ├── constraint-decomposition.md       # 约束拆解（按需加载）
│   ├── zero-based-redesign.md            # 从零重构（按需加载）
│   ├── experiment-design.md              # 最小实验（按需加载）
│   ├── extraction-framework.md           # 提炼框架与质检规则
│   ├── operations/                       # 6个辅助操作柱状文件（956行）
│   └── research/                         # 12个主题调研文件（3351行）
└── examples/                             # 案例库
```

---

## 使用建议

- 用它拆问题，不用它替你跳过事实收集
- 当输出开始变空泛时，先重写问题，而不是继续写答案
- 对所有“这不可能”“这一直很贵”“行业都这样”的说法保持怀疑
- 如果没有最小验证动作，这次分析还不算完成

---

## 诚实边界

- 它能帮你回到基本事实，不能替你拥有缺失的一手数据
- 它能帮你发现假设，不能保证每个假设都能立即证伪
- 它适合产品、商业、学习、决策，不适合冒充法律、医疗、财务专业意见
- 它提供的是重构问题的框架，不是假装无所不知的结论

---

## 许可证

本项目基于 [MIT License](LICENSE) 开源。
