Below are the **Light Mode MD files** to place under `assets/scaffold/` for **4 reusable Skills** (no separate Thread Charter needed in Light Mode — the orchestrator SKILL.md covers the operating loop).

Use these exact paths:

* `skills/orchestrator/SKILL.md`
* `skills/planner/SKILL.md`
* `skills/builder/SKILL.md`
* `skills/critic/SKILL.md`

---

## assets/scaffold/skills/orchestrator/SKILL.md

```markdown
# Skill: orchestrator

## Purpose
Run the project workflow: read the current state, decide what to do next, call the right skills, and keep the work log updated.

## When to Use
- At the start of a session
- When deciding what to work on next
- When integrating outputs from multiple skills
- When the project feels stuck or scattered

## Operating Loop (One Cycle)

1. **Pull**: Read `PROJECT_HUB.md` (Recent Changes) + latest `logs/work/WORKLOG-*.md`
2. **Decide**: What stage are we in? What's the minimum next output?
   - Stages: **Specify → Plan → Build → Review**
3. **Act**: Call 1–2 skills (prefer fewer), or do the work directly if it's small
4. **Log**: Append to today's `logs/work/WORKLOG-YYYY-MM-DD.md`
   - If new docs were created, add links to `PROJECT_HUB.md`

## Gate B — Architecture / Contract Check
Pause and ask the user when:
- API contracts, data model, or auth decisions need to be locked
- There are competing technical options with real tradeoffs
- A choice is hard to reverse later

(Gate A for scope and Gate C for release can be triggered manually by the user when needed.)

## Constraints
- Prefer doing over planning. If the next step is obvious, just do it.
- Don't over-call skills. 1–2 per cycle is the sweet spot.
- Don't skip logging — but keep logs short (3–5 lines per entry).
- If something is outside your scope, call the appropriate skill instead of guessing.

## Output Block (when decisions are involved)
- Decision Needed (Yes/No):
- Risk (if any):
- Next Action:
- Docs Created/Updated:
```

---

## assets/scaffold/skills/planner/SKILL.md

```markdown
# Skill: planner

## Purpose
Turn an idea into an actionable plan: what to build, why, what's out of scope, and what tasks to execute. Combines product spec writing with documentation structure.

## When to Use
- New feature or new project kickoff
- Scope definition and prioritization
- Converting ambiguous ideas into clear requirements
- When docs are scattered and need a structure recommendation

## Required Inputs
- User idea and constraints (time, platform, must-have / must-not)
- `PROJECT_HUB.md` (North Star, current status)
- Existing specs/design/contracts (if any)

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

## Constraints
- Avoid over-engineering; MVP should be buildable in days, not weeks
- If requirements are underspecified, ask ≤ 5 questions or mark assumptions
- Don't decide architecture in detail — flag for builder or Gate B

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
```

---

## assets/scaffold/skills/builder/SKILL.md

```markdown
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
```

---

## assets/scaffold/skills/critic/SKILL.md

```markdown
# Skill: critic

## Purpose
Evaluate the product as the target customer: find usability and trust issues, score quality, and propose concrete improvements.

## When to Use
- After UX or implementation exists (even partially)
- Before shipping or sharing with users
- When something feels off but you can't pinpoint why
- As a sanity check on any major feature

## Required Inputs
- Current UX spec, implementation, or prototype description
- Feature spec (intent and success metrics)
- Any screenshots/flows if available

## Output Contract
Provide:
1. Quick scores (1–10 each):
   - First-5-min clarity (can a new user figure it out?)
   - Friction to complete the core task
   - Trust & safety (errors, permissions, data handling)
   - Visual clarity
2. Feedback:
   - 1 thing that works well
   - Up to 3 critical issues (with "why it hurts" + "what to change")
   - Up to 5 quick wins (smallest effort first)

Record in `logs/work/WORKLOG-YYYY-MM-DD.md`

## Constraints
- Use user language, not engineering jargon
- Be specific and actionable
- Don't propose large scope expansions as "quick wins"
- Quick wins should be achievable in under an hour each

## Quality Bar
- Feedback is actionable and prioritized
- Scores align with rationale
- Critical issues are truly critical
- Quick wins are actually quick

## Output Block (when decisions are involved)
- Decision Needed (Yes/No):
- Risk (if any):
- Next Action:
- Docs Created/Updated:
```