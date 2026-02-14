---
name: builder
description: Execute implementation and design work for assigned scope, including code, contracts, and technical decisions tied to the spec. Trigger when concrete build tasks are ready; do not trigger for high-level workflow coordination (orchestrator) or pure requirement shaping (planner).
---

# Skill: builder

## Purpose
Design and implement the product. This skill covers UX design, frontend, backend, and technical decisions — the full build cycle for a solo developer.

## When to Use
- After a spec or plan exists (even a rough one)
- When implementing features end to end
- When API contracts or data models need to be defined
- When UX flows need to be designed alongside implementation

## Required Inputs
- Orchestrator task statement (scope, boundaries, expected outputs)
- `docs/specs/*` (what to build)
- `PROJECT_HUB.md` (current status)
- Existing contracts/decisions (if any)

## Technique Call Conditions: web-motion-polish
Call web-motion-polish (`skills/techniques/web-motion-polish/SKILL.md`) when:
- Building or polishing a web UI that feels static or unresponsive
- You need intentional transitions/micro-interactions while keeping performance and accessibility

Skip web-motion-polish when:
- Task is backend-only, contracts-only, or non-UI work
- Existing approved design constraints explicitly prohibit motion changes

Important:
- web-motion-polish has a hard gate: propose exactly 3 moments and a motion spec, then get user approval before implementation.

## Output Contract
Depending on the task, produce one or more of:

### UX & Design (when needed)
- Core user flows (keep it practical, not decorative)
- Screen list with purpose, primary actions, required data
- State design: empty, loading, error, no-access
- Write into `docs/design/UX-####-<slug>.md` or inline in the spec

### Frontend
- Route map / component breakdown
- State strategy (local/global)
- UI states (loading/error/empty)
- Accessibility basics (keyboard/focus)

### Backend
- Data model (entities, relationships)
- API endpoints: method, path, request/response, error codes
- Auth model (roles/scopes) if applicable
- Write contracts to `docs/contracts/API-####-<slug>.md`

### Technical Decisions
- When facing competing options: compare 2–3, recommend one
- If significant, create `docs/decisions/ADR-####-<slug>.md`
- If the tradeoff is hard to reverse, ask for human confirmation through orchestrator

Return to orchestrator with:
- changed file path(s)
- what was implemented/designed
- assumptions, risks, unresolved dependencies

## Constraints
- Build for the spec, not for hypothetical future needs
- Contract-first: define the API before implementing
- If a UX choice impacts the API significantly, flag it
- Don't silently change contracts — propose changes explicitly
- Keep output bounded to assigned scope; do not branch into unrelated tasks

## Quality Bar
- Code/contracts are consistent with the spec
- Error handling is explicit
- UX flows have no dead-ends
- Accessibility is not ignored
- Tests are feasible and scoped

## Output Block (when decisions are involved)
- Decision Needed (Yes/No):
- Risk (if any):
- Next Action:
- Docs Created/Updated:
