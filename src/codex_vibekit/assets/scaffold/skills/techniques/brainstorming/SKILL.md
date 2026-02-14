---
name: brainstorming
description: Refine ambiguous feature requests into 2-3 viable options with tradeoffs and a recommended direction for orchestrator/planner. Trigger when requirements or architectural approach are unclear; do not trigger for straightforward bug fixes, refactors, or tasks already covered by approved design docs.
---

# Skill: brainstorming (technique)

## Purpose
Refine ambiguous requests into concrete options with clear tradeoffs, then return a recommended path for orchestrator/planner.

## Used By
- `orchestrator`
- `planner`

## Call Conditions
Use this technique when:
- A new feature request is ambiguous
- Two or more implementation approaches are viable
- Architecture-level tradeoffs must be compared before continuing
- Non-functional priorities are unclear (performance, security, cost, reliability)

Skip this technique when:
- Task is already clear (bug fix, focused refactor, copy/doc update)
- Approved design docs already define direction

## Required Inputs
- Current user goal and constraints
- `PROJECT_HUB.md` and latest `logs/work/WORKLOG-*.md`
- Relevant spec/contract/design docs (if they exist)

## Output Contract
Create a design note at:
- `docs/plans/YYYY-MM-DD-<topic>-design.md`

Design note must include:
1. Problem framing (what is unclear)
2. Options (2-3 approaches max)
3. Tradeoff matrix (speed, complexity, risk, reversibility)
4. Recommended option and why
5. Questions requiring human confirmation (if any)

Then return to orchestrator/planner with:
- created file path
- recommendation summary (3-6 lines)
- unresolved risks/questions

## Coordination Rule
- If the next step is planning breakdown, hand off to `planner` (not `writing-plans`)
- If user confirmation is required, stop and escalate through orchestrator

## Constraints
- Keep analysis bounded and decision-oriented
- Do not expand scope beyond the current feature/topic
- Prefer reversible options when information is limited

## Output Block (when decisions are involved)
- Decision Needed (Yes/No):
- Risk (if any):
- Next Action:
- Docs Created/Updated:
