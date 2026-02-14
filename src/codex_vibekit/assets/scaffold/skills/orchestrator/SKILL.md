---
name: orchestrator
description: Drive end-to-end workflow in the main thread by selecting next actions, dispatching planner/builder/critic, requesting support threads, and merging outcomes. Trigger for session start, coordination, handoffs, and conflict resolution; do not trigger for single-scope implementation-only tasks that can be completed directly by builder.
---

# Skill: orchestrator

## Purpose
Run the project workflow end-to-end: read state, choose next action, dispatch skills, request support threads when needed, and integrate outputs.

## When to Use
- At the start of a session
- When deciding what to work on next
- When integrating outputs from multiple skills
- When the project feels stuck or scattered

## Quick Start Trigger
If user input is short (for example, "continue", "next", "go on", or "orchestrate this"), treat it as:
- continue in orchestrator mode
- read hub/worklog first
- decide next smallest output
- request support thread only if needed

## Operating Loop (main thread)

1. **Pull**: Read `PROJECT_HUB.md` (Recent Changes) + latest `logs/work/WORKLOG-*.md`
2. **Decide**: What is the minimum next output for momentum?
3. **Act**: Do it directly or dispatch one skill (`planner`, `builder`, `critic`)
4. **Brainstorm (if needed)**: call technique `skills/techniques/brainstorming/SKILL.md` before committing to a direction
5. **Split (if needed)**: Ask user to open a support thread with an exact prompt
6. **Merge**: Integrate returned output, resolve conflicts, update `PROJECT_HUB.md`
7. **Log**: Append a short entry to `logs/work/WORKLOG-YYYY-MM-DD.md`

## Technique Call Conditions: brainstorming
Call brainstorming when:
- Request is ambiguous and scope cannot be finalized yet
- Two or more approaches have meaningful tradeoffs
- Architecture-level direction needs comparison before execution

Skip brainstorming when:
- Task is already clear and bounded
- Existing approved docs already define the solution path

## Human Confirmation (required)
Pause and ask the user when decisions are hard to reverse:
- API contracts, data model, or auth decisions need to be locked
- There are competing technical options with real tradeoffs
- A choice is hard to reverse later

## Support Thread Request Contract
When asking for a new thread, output:
- **Reason**: why parallel support is needed now
- **Ready prompt**: exact message for the new thread
- **Expected output**: target file path(s) and response format
- **Return rule**: what summary must be pasted back to main thread

Template:

```text
Open Thread <N> and send this prompt:
"Act as <skill> for <scope>.
Task: <single bounded task>.
Write output to <doc path>.
Return: concise summary with assumptions, risks, and unresolved questions."

When done, paste back:
1) changed file paths
2) key decisions
3) open risks/questions
```

## Constraints
- Keep human burden low: ask for goals, constraints, and approvals only
- Keep tasks bounded: one support thread should have one clear deliverable
- Keep merge explicit: call out conflicts before choosing one direction
- Keep logs short: 3–5 lines per entry

## Output Block (when decisions are involved)
- Decision Needed (Yes/No):
- Risk (if any):
- Next Action:
- Docs Created/Updated:
