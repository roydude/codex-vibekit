---
name: planner
description: Convert ambiguous goals into scoped specs with MVP boundaries, non-goals, task breakdown, and acceptance criteria. Trigger when requirements/scope are unclear or need formalization; do not trigger for already-approved clear tasks that should move directly to implementation.
---

# Skill: planner

## Purpose
Turn an idea into an actionable plan: what to build, why, what's out of scope, and what tasks to execute. Combines product spec writing with documentation structure.

## When to Use
- New feature or new project kickoff
- Scope definition and prioritization
- Converting ambiguous ideas into clear requirements
- When docs are scattered and need a structure recommendation

## Required Inputs
- Orchestrator task statement (scope, output path, constraints)
- User idea and constraints (time, platform, must-have / must-not)
- `PROJECT_HUB.md` (North Star, current status)
- Existing specs/design/contracts (if any)

## Technique Call Conditions: brainstorming
Call brainstorming (`skills/techniques/brainstorming/SKILL.md`) when:
- Multiple implementation approaches are plausible and user confirmation is needed
- Non-functional priorities are unclear or conflicting

Skip brainstorming when:
- Task is implementation-clear (bug fix/refactor/doc update)
- Existing approved design docs already settle key choices

## Technique Call Conditions: korean-humanizer
Call korean-humanizer (`skills/techniques/korean-humanizer/SKILL.md`) when:
- You are about to deliver Korean text to the user and it reads like translationese or template prose
- The user explicitly asks for “사람처럼”, “자연스럽게”, “AI 티 빼줘”, or “휴머나이징”

## Output Contract
Create or update a spec doc: `docs/specs/SPEC-####-<slug>.md`

Spec must include:
1. Problem & Value (why are we building this)
2. Target users & key scenarios (3–5)
3. Non-goals (explicit — what we're NOT building)
4. MVP scope (keep it tight)
5. Task breakdown with acceptance criteria
6. Open questions (≤ 5, mark assumptions clearly)

Also recommend which docs are needed next and where they should live:
- ADR: `docs/decisions/ADR-####-<slug>.md`
- API/Schema: `docs/contracts/`
- UX notes: `docs/design/`

Return to orchestrator with:
- changed file path(s)
- 3–7 line summary
- assumptions and open questions

## Constraints
- Avoid over-engineering; MVP should be buildable in days, not weeks
- If requirements are underspecified, ask ≤ 5 questions or mark assumptions
- Don't lock architecture in detail — escalate to orchestrator for human confirmation
- Treat this as a bounded assignment from orchestrator, not a full-project rewrite

## Quality Bar
- MVP scope is small and testable
- Non-goals reduce ambiguity
- Tasks are actionable (each has an acceptance criterion)
- Dependencies and risks are stated

## Output Block (when decisions are involved)
- Decision Needed (Yes/No):
- Risk (if any):
- Next Action:
- Docs Created/Updated:
