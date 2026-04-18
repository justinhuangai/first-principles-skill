# Zero-Based Redesign

Use this mode when the current system has too much history inside it.

## Goal

Rebuild the smallest system that still delivers the desired result.

## When This Mode Is Usually Right

- the current flow feels bloated, slow, or hard to explain
- many steps exist only because of other bad steps
- the system has accumulated features, approvals, or tools over time
- local optimization is no longer improving total outcome

## Output Pattern

1. Define the result in user terms
2. List the minimum necessary components
3. Identify deletions and postponements
4. Propose the shortest viable path from intent to outcome
5. Name the main risk and the smallest check against it

## Workflow

1. Define the result in user terms
2. Ignore the current implementation temporarily
3. Ask what the minimum necessary components are
4. Remove steps, roles, tools, and features that are not essential
5. Reintroduce only what earns its place

## Core Question Set

- If we started today, would we build it this way?
- What is the shortest path from intent to outcome?
- Which steps exist only to support other bad steps?
- Which features defend complexity rather than create value?

## Deletion Tests

- If we remove this step, what user outcome breaks?
- Is this step preserving value or preserving familiarity?
- Is this feature needed by the user or by the current org chart?
- Are we optimizing around a dependency that should itself be removed?

## Mini Example

System:

- a seven-step approval process for publishing a small product update

Redesign move:

1. define the real result: safe release with clear ownership
2. keep only version control, automated checks, and one accountable approver
3. delete review steps that mainly exist to diffuse responsibility
4. reintroduce only what earns its place after the simple path exists

## Design Bias

Prefer:

- deletion before optimization
- manual proof before automation
- one clear path before many optional branches

## Failure Modes

- rebuilding around the current org chart instead of the user outcome
- preserving legacy exceptions in the first draft of the redesign
- adding optionality before proving a simple core path

## Useful Prompts

- "If we use zero-based redesign here, what is the smallest honest restatement of the problem?"
- "Which part of this situation becomes clearer when we apply zero-based redesign instead of generic advice?"
- "What are we treating as fixed that zero-based redesign would challenge?"
- "Where is the present framing making the problem look simpler or cleaner than it really is?"
- "What does zero-based redesign say the user, team, or system is actually trying to achieve?"
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

- Do not use zero-based redesign as a license for verbosity.
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
