[简体中文](./README.md) | **English**

<div align="center">

# First Principles.skill

> *“We say we know each thing only when we think we recognize its first cause.”*  
> — Aristotle, *Metaphysics* I.1

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-0169CC)](https://openai.com/codex)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-CC785C)](https://claude.ai/code)
[![Nuwa](https://img.shields.io/badge/Made%20with-女娲.skill-orange)](https://github.com/alchaincyf/nuwa-skill)
[![Type: Topic Skill](https://img.shields.io/badge/Type-Topic%20Skill-green)](#examples)

<br>

Reduce messy problems back to facts, constraints, assumptions, and experiments.<br>
Useful for cost breakdowns, system redesigns, abstract-question decomposition, and minimum viable experiment design.<br>
Distills 4 core mental models, 8 heuristics, 6 routing modes, classic cases, and modern applications.

[Examples](#examples) · [Installation](#installation) · [What It Distills](#what-it-distills) · [Sources](#sources) · [Acknowledgements](#acknowledgements) · [License](#license)

</div>

## Examples

### Q: How would humans get to Mars?

```text
First Principles  ❯ Do not start from "too expensive," "too hard," or the inherited aerospace playbook.

                    First decompose the mission into unavoidable problems:
                    - how do we move enough mass out of Earth's gravity well?
                    - how do we sustain life support, energy, and radiation protection during transit?
                    - how do we handle entry, descent, and landing on Mars?
                    - can return fuel and supplies be produced in situ on Mars?
                    - which constraints are physical, and which are artifacts of today's wasteful engineering path?

                    Then ask:
                    - does the rocket need to be single-use?
                    - how much mass really has to leave Earth?
                    - which systems need redundancy, and which are just inherited design habits?
                    - what is actually expensive: atoms, or system architecture amplified by one-time hardware and logistics?

                    First principles does not start with the quoted price.
                    It rebuilds the problem as physics, engineering, and supply first.

                    Cost still matters,
                    but it should emerge from the mission architecture,
                    not be treated as the only question from the start.
```

### Q: Why can EV batteries still become much cheaper?

```text
First Principles  ❯ Because first-principles reasoning does not start from the inherited price of a finished battery pack.

                    It would go down to the material layer:
                    - what do the cells actually contain?
                    - what is the raw material cost of nickel, cobalt, lithium, graphite, aluminum?
                    - how much of today's price is chemistry versus manufacturing path?
```

### Q: When will AGI arrive?

```text
First Principles  ❯ Before predicting a year, define what you mean by AGI.

                    Does it mean:
                    - broad human-level task performance
                    - transfer across domains
                    - long-horizon autonomy
                    - acceptable cost and reliability
```

### Q: Our product charges $49 per month, but margins keep shrinking. How should we optimize it?

```text
First Principles  ❯ Do not optimize yet. Decompose it first.

                    Which parts of that $49 are irreducible?
                    Hosting, model cost, payment fees, support, onboarding labor, churn recovery?

                    Which costs are physical and which are artifacts of the current product and team design?
```

### Q: What startup opportunities still exist?

```text
First Principles  ❯ Do not start from "what is hot." Start from "what is still slow, expensive, and painful."

                    Break down:
                    - what job is the user actually trying to get done?
                    - which step in the current path is slowest, most expensive, or most frustrating?
                    - which part seems necessary only because of inherited process?
                    - which capabilities just became cheap enough to redesign because of AI, automation, or new distribution?

                    The best opportunities often do not come from inventing a new desire.
                    They come from serving an old desire through a shorter, cheaper, simpler path.

                    So do not ask "what idea is hottest."
                    Ask "which painful step can now be rewritten for the first time."
```

### Q: What is the meaning of life?

```text
First Principles  ❯ Do not rush toward one grand answer that pretends to fit everyone.

                    At minimum, split the question into:
                    - what makes life worth continued investment?
                    - what sustains responsibility under pain or uncertainty?
                    - what remains meaningful beyond short-term pleasure?

                    Here first principles does not produce a slogan.
                    It forces the question back into lived experience, attention, commitments,
                    and repeated action.
```

---

## Installation

```bash
npx skills add justinhuangai/first-principles-skill
```

After installation, prompts like these should activate it naturally:

```text
From first principles, what is the real AGI bottleneck?
If we redesigned this product from zero, what parts should not exist at all?
Break down this product's cost structure from first principles.
Is this workflow built on the wrong assumptions?
```

---

## What It Distills

### 4 Core Mental Models

| Model | One-line summary | Use |
|------|------|------|
| **Do not accept inherited price as truth** | the industry status quo is not primitive reality | cost, pricing, manufacturing |
| **Decompose to physics or user result** | reason from materials or end outcomes, not packaging | product, technical, workflow design |
| **Separate constraints from path dependence** | many constraints are frozen old decisions | organization, strategy, process |
| **Replace talk with experiment** | when evidence is missing, design the smallest test | uncertainty-heavy decisions |

### 8 Heuristics

1. Rewrite the problem before answering it
2. Find irreducible facts first
3. Translate every conclusion back into assumptions
4. Classify every constraint
5. Delete before optimizing
6. Start from the outcome, not the current system
7. Split large abstract words into smaller questions
8. End with a test, not just a theory

---

## Sources

12 research files, 3435 lines total, all under [references/research/](references/research/):

### Research Layer (12 files, 3435 lines)

| File | Content | Lines |
|------|------|------|
| `references/research/01-first-causes-definitions-and-explanation.md` | first causes, definitions, and explanatory knowledge | 286 |
| `references/research/02-reality-experiment-and-engineering-rebuilds.md` | reality, experiment, and engineering rebuilds | 286 |
| `references/research/03-incentives-path-dependence-and-boundaries.md` | incentives, path dependence, and boundaries | 286 |
| `references/research/04-systems-feedback-and-leverage.md` | systems, feedback loops, and leverage points | 286 |
| `references/research/05-demand-jobs-and-market-creation.md` | demand primitives, JTBD, and market creation | 286 |
| `references/research/06-value-price-unit-economics-and-capture.md` | value, price, unit economics, and value capture | 286 |
| `references/research/07-flow-quality-reliability-and-maturity.md` | flow, quality, reliability, and maturity | 286 |
| `references/research/08-probability-calibration-and-measurement.md` | probability, calibration, and measurement | 287 |
| `references/research/09-optionality-sequencing-and-decision-velocity.md` | optionality, sequencing, and decision velocity | 286 |
| `references/research/10-strategy-positioning-complexity-and-fit.md` | strategy, positioning, complexity, and fit | 286 |
| `references/research/11-governance-learning-and-viability.md` | governance, learning, and viability | 286 |
| `references/research/12-meaning-motivation-and-human-commitment.md` | meaning, motivation, and human commitment | 286 |


### Operational References (13 files, 1672 lines)

| File | Content | Lines |
|------|------|------|
| `references/assumption-audit.md` | assumption-audit workflow | 76 |
| `references/concept-clarification.md` | concept clarification and definition splitting | 66 |
| `references/classic-cases.md` | classic first-principles cases | 115 |
| `references/constraint-decomposition.md` | constraint taxonomy and decomposition | 69 |
| `references/zero-based-redesign.md` | zero-based redesign workflow | 121 |
| `references/experiment-design.md` | minimum viable experiment design | 118 |
| `references/extraction-framework.md` | six-path distillation method, source priority, and QA rules | 151 |
| `references/operations/01-problem-framing-and-reframing.md` | problem framing, reframing, and scope tightening | 155 |
| `references/operations/02-demand-value-and-opportunity.md` | demand, value, and opportunity discovery | 155 |
| `references/operations/03-cost-flow-and-bottlenecks.md` | cost, flow, and bottleneck diagnosis | 155 |
| `references/operations/04-boundaries-incentives-and-governance.md` | boundaries, incentives, and governance design | 155 |
| `references/operations/05-decisions-metrics-and-experiments.md` | decisions, metrics, and experiment design | 155 |
| `references/operations/06-strategy-learning-and-resilience.md` | strategy, learning, and resilience | 181 |

### Core Figures

- **Aristotle / Euclid** — first causes, axioms, primitives, and definition clarity
- **Galileo Galilei / Richard Feynman** — observable reality, explanation, experimentation, and anti-self-deception
- **Elon Musk / Charlie Munger** — engineering cost floors, incentives, constraints, opportunity cost, and path dependence
- **Hayek / Herbert A. Simon / Donella Meadows / Stafford Beer** — distributed knowledge, bounded rationality, feedback loops, system boundaries, and viability
- **Clayton Christensen / Bob Moesta / Peter Drucker** — jobs to be done, opportunity discovery, objectives, and knowledge work
- **John Little / Eliyahu Goldratt / W. Edwards Deming** — queues, throughput, bottlenecks, variation, and quality
- **Ronald Coase / Michael Porter / Richard Rumelt / Jeff Bezos** — transaction costs, competitive position, diagnosis, and high-velocity decision making
- **Elinor Ostrom / Peter Senge / Chris Argyris / Russell Ackoff** — commons governance, learning loops, double-loop learning, and messes
- **Thomas Bayes / Daniel Kahneman / Nassim Nicholas Taleb / Charles Goodhart / John Tukey** — base rates, calibration, optionality, proxy metrics, and anti-vanity measurement
- **Viktor Frankl / Abraham Maslow** — meaning, motivation, commitment, and layered human needs

---

## Acknowledgements

This skill was distilled and assembled with [Nuwa.skill](https://github.com/alchaincyf/nuwa-skill).

---

## Repo Layout

```text
first-principles-skill/
├── README.md
├── README_EN.md
├── SKILL.md                    # routing + execution rules
├── references/                 # 25 files (5023 lines)
│   ├── assumption-audit.md     # primary direct-load mode file
│   ├── concept-clarification.md
│   ├── classic-cases.md
│   ├── constraint-decomposition.md
│   ├── zero-based-redesign.md
│   ├── experiment-design.md
│   ├── extraction-framework.md # six-path distillation + QA rules
│   ├── operations/             # 6 thematic operational pillar files (956 lines)
│   └── research/               # 12 thematic research files (3351 lines)
└── examples/                  # public example library
```

---

## Usage Notes

- Use it to decompose problems, not to skip evidence gathering
- If the output starts sounding vague, rewrite the question before extending the answer
- Stay suspicious of claims like "this is impossible", "this has always been expensive", or "the industry just works this way"
- If there is no minimum viable experiment at the end, the analysis is not finished

---

## Honest Boundaries

- It helps recover ground truth; it does not replace missing evidence
- It helps expose assumptions; it does not magically validate them
- It works best for product, business, strategy, learning, and workflow design
- It should not be treated as legal, medical, or financial authority

---

## License

Released under the [MIT License](LICENSE).
