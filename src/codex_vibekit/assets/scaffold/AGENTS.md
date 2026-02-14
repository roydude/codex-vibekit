# AGENTS.md (codex-vibekit Light Mode)

## Start of session
- Read `PROJECT_HUB.md` (Recent Changes at the top)
- Read the latest `logs/work/WORKLOG-*.md`
- Default to `orchestrator` as the control role in the main thread
- Unless user says otherwise, auto-apply orchestrator-driven mode without requiring full repeated prompt text

## Minimal user kickoff (recommended)
- User can start with one short line:
  - `Continue in orchestrator mode.`
- Then proceed using this file's operating rules automatically

## End of session (required)
- Append a short entry to today's `logs/work/WORKLOG-YYYY-MM-DD.md` (3–5 lines)
- If you created or updated docs, add links in `PROJECT_HUB.md`

## Operating model (orchestrator-driven)
- Human gives goal and constraints, not detailed task decomposition
- Orchestrator decides next task and which skill to use
- If parallel work is needed, orchestrator asks human to open a support thread
- Human acts as a router: opens requested thread, runs prompt, returns summary
- Main-thread orchestrator integrates outputs and resolves conflicts

## Human confirmation points (required)
- Ask the user before locking hard-to-reverse choices:
  - API contracts
  - Data model and migration shape
  - Auth and permission model
  - Major architecture direction

## Support thread handoff format
- When requesting a support thread, output:
  - Why support is needed
  - Exact prompt to paste in new thread
  - Expected output format (doc path + concise summary)
  - Merge criteria for returning to main thread

## Naming and location rules
- Specs: `docs/specs/SPEC-####-<slug>.md`
- Decisions: `docs/decisions/ADR-####-<slug>.md`
- Contracts: `docs/contracts/API-####-<slug>.md` (or similar)
- UX notes: `docs/design/UX-####-<slug>.md`
- Work logs: `logs/work/WORKLOG-YYYY-MM-DD.md`
