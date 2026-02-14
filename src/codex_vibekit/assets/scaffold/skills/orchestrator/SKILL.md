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

