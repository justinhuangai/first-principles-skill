# Experiment Design

Use this mode when a good answer depends on evidence that does not yet exist.

## Goal

Convert uncertainty into the smallest cheap test that changes the decision.

## When This Mode Is Usually Right

- the user wants certainty that does not yet exist
- multiple explanations sound plausible
- the next decision depends on one high-weight assumption
- the team is about to commit major resources without a cheap read

## Output Pattern

1. Critical assumption
2. Evidence that would raise or lower confidence
3. Smallest falsifiable test
4. Success threshold defined in advance
5. Kill / continue / redesign rule

## Workflow

1. Identify the critical assumption
2. Define what evidence would increase or decrease confidence
3. Design the smallest falsifiable test
4. Set a success threshold before running it
5. Describe how the decision changes based on the result

## Good Experiment Properties

- low cost
- fast feedback
- one dominant variable
- measurable outcome
- clear kill / continue rule

## Experiment Ladder

1. desk check or data sanity check
2. manual or concierge test
3. smoke test for demand or behavior
4. small-cohort behavioral test
5. production rollout only after the earlier layers teach something

## Mini Example

Assumption:

- "Users need real-time generation here."

Test:

- replace real-time generation with a batched version for a small cohort
- define success as no significant drop in task completion or retention
- if user experience holds, redesign cost structure around batching

## Failure Modes

- testing too many assumptions at once
- designing a test that mainly produces vanity metrics
- collecting data without a decision threshold

## Boundary

If the problem is still poorly defined, return to assumption audit or concept clarification first. A bad experiment on a bad question is still a bad experiment.

## Useful Prompts

- "If we use experiment design here, what is the smallest honest restatement of the problem?"
- "Which part of this situation becomes clearer when we apply experiment design instead of generic advice?"
- "What are we treating as fixed that experiment design would challenge?"
- "Where is the present framing making the problem look simpler or cleaner than it really is?"
- "What does experiment design say the user, team, or system is actually trying to achieve?"
- "Which part of the answer should stay structural rather than tactical?"
- "What would a stronger operator look at first through this lens?"
- "What would count as a concrete next move, not just a better explanation?"

## Observation Checklist

- Identify the smallest boundary that still contains the mechanism.
- Separate visible symptoms from the structural layer behind them.
- Look for irreducible facts before following any preferred narrative.
- Name the assumptions hiding inside the current explanation.
- Inspect whether the current system is preserving baggage that no longer earns its keep.
- Ask whether the right move is subtraction, redesign, measurement, or sequencing.
- Check whether local improvements are harming the whole system.
- End with a deliverable that can guide a real decision.

## Red Flags

- The answer sounds polished before the problem is stable.
- The team is optimizing inside inherited categories that may be wrong.
- Constraints are being asserted without classification or evidence.
- The user is asking for a conclusion when a decomposition is still missing.
- The system is carrying complexity that nobody would rebuild from zero.
- The discussion has many opinions but no discriminating observation.
- A metric is steering behavior without a clearly named guardrail.

## Misreadings To Avoid

- Do not use experiment design as a license for verbosity.
- Do not confuse this lens with a universal answer to every adjacent problem.
- Do not stop at naming the pattern; push it back into concrete consequences.
- Do not let this lens erase timeline, owner, or decision context.
- Do not assume a cleaner model means the world itself is clean.
- Do not turn a structural diagnosis into a moral story about people.

## Modern Questions This Helps With

- Which part of an AI product is structurally expensive versus temporarily expensive?
- Why does a workflow keep slowing down even after new tooling is added?
- What are we really saying when we use a large word like quality, AGI, or strategy?
- Which parts of a product or service exist only because of historical layering?
- Where should authority, measurement, or ownership actually sit?
- What is the smallest move that would create real information rather than more debate?
