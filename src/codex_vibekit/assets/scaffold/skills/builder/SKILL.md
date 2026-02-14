# Skill: builder

## Purpose
Design and implement the product. This skill covers UX design, frontend, backend, and technical decisions — the full build cycle for a solo developer.

## When to Use
- After a spec or plan exists (even a rough one)
- When implementing features end to end
- When API contracts or data models need to be defined
- When UX flows need to be designed alongside implementation

## Required Inputs
- `docs/specs/*` (what to build)
- `PROJECT_HUB.md` (current status)
- Existing contracts/decisions (if any)

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
- If the tradeoff is hard to reverse, trigger Gate B

## Constraints
- Build for the spec, not for hypothetical future needs
- Contract-first: define the API before implementing
- If a UX choice impacts the API significantly, flag it
- Don't silently change contracts — propose changes explicitly

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

