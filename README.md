# codex-vibekit (Light Mode)

Korean version: [`README.ko.md`](README.ko.md)
Documentation policy: `README.md` is the source of truth; keep `README.ko.md` in sync with this file.

`codex-vibekit` is a lightweight CLI that injects an operating scaffold (docs, logs, skills, and rules) into a project root so coding sessions stay structured without heavy process overhead.

## Philosophy

`codex-vibekit` is built on five principles:

1. The system should work for the developer, not the other way around.
2. Keep logs in one place (`logs/work/`), not scattered across files.
3. Use a minimal role model (orchestrator, planner, builder, critic).
4. Ask for human confirmation only at high-impact decision points (for example: API contract, data model, auth, or architecture choices that are hard to undo).
5. Optimize for shipping speed over document ceremony.

## Purpose

This tool exists to make project startup and operation repeatable for AI-assisted coding sessions, especially in Codex.

- Standardize project structure in seconds.
- Keep current status visible through `PROJECT_HUB.md`.
- Ensure daily work history is always captured in `WORKLOG`.
- Provide reusable skill prompts with consistent operating rules.

## Goals

- Fast bootstrap: run one command and start building.
- Safe merge behavior: no overwrite of existing files by default.
- Agent-friendly context: scaffold files that Codex can immediately use.
- Portable workflow: works on new and existing repositories.

## Use Cases

Use `codex-vibekit` when:

- Starting a new vibe-coding project and you want clean operating scaffolding.
- Bringing consistency to an existing project with scattered docs/logs.
- Running Codex sessions where clear operating context (`AGENTS.md`, `PROJECT_HUB.md`) matters.
- You need lightweight process, not a full enterprise framework.

## Roles
| Role | Purpose |
|---|---|
| `orchestrator` | Break down tasks, choose skills, integrate outputs |
| `planner` | Convert requirements into implementable plans |
| `builder` | Implement code/design/contracts |
| `critic` | Review quality, identify risks, suggest fixes |

## Techniques (auxiliary)
| Technique | Used by | Purpose |
|---|---|---|
| `brainstorming` | `orchestrator`, `planner` | Refine ambiguous requirements, explore approaches, prepare design-approval questions |
| `web-motion-polish` | `builder` | Add lightweight motion and micro-interactions to web UI with performance/accessibility gates |
| `korean-humanizer` | any | Rewrite Korean to remove AI/translationese signals while preserving meaning and keeping tone consistent |

## Codex Workflow

`codex-vibekit` is optimized for Codex with an orchestrator-driven model: human gives goals, orchestrator decides execution and requests extra threads only when needed.

### Operating model (human-light, agent-driven)

1. Start with one thread (orchestrator).
2. Orchestrator reads `PROJECT_HUB.md` and latest `logs/work/WORKLOG-*.md`.
3. Orchestrator chooses which skill to use next (`planner`, `builder`, `critic`) and executes.
4. If extra parallel work is needed, orchestrator explicitly asks for a new support thread.
5. Human opens the new thread and passes orchestrator's request as-is.
6. Orchestrator integrates results, resolves conflicts, and updates `PROJECT_HUB.md` and `WORKLOG`.

### Workflow diagram

```mermaid
flowchart TB
  solo["Solo Developer"]
  orch["Orchestrator"]
  planner["Planner"]
  builder["Builder"]
  critic["Critic"]
  gate_b["User Decision (\"Gate B\")"]

  subgraph repo["Shared Repository"]
    hub["PROJECT_HUB.md"]
    contracts["docs/contracts/*"]
    decisions["docs/decisions/ADR-*"]
    design["docs/design/*"]
    specs["docs/specs/*"]
    worklog["logs/work/WORKLOG-*"]
  end

  solo -->|"Idea / Direction"| orch
  orch -->|"When Architecture decision needed"| gate_b
  gate_b -->|"Approve / Redirect"| solo

  orch -->|"Pull: Read latest header"| hub
  orch -->|"Update links + status"| hub
  orch -->|"Log summary"| worklog

  orch -->|"Call skill"| builder
  orch -->|"Call skill"| planner
  orch -->|"Call skill"| critic

  planner -->|"Create: SPEC"| specs
  planner -->|"Recommend doc structure"| design
  planner -->|"Log work"| worklog

  builder -->|"Create: API contracts"| contracts
  builder -->|"Create: ADR (if tradeoff)"| decisions
  builder -->|"Create: UX flows"| design
  builder -->|"Log work"| worklog

  critic -->|"Score + feedback"| worklog
```

### Prompt examples (orchestrator first)

Thread 1 (main):
```text
Act as orchestrator.
Read PROJECT_HUB.md and latest WORKLOG.
From now on, you decide task breakdown and which skill to run.
If additional parallel resources are needed, ask me to open a new thread with a ready-to-send prompt.
Only ask me at high-impact decision points.
```

Minimal daily kickoff (recommended):
```text
Continue in orchestrator mode.
```

The scaffold rules already define the behavior, so the long prompt is for first setup or reset only.

### Support-thread handoff pattern

When orchestrator asks for support, it should output:

```text
Open Thread 2 and send this:
"Act as builder focused on API contract for <feature>.
Create docs/contracts/API-0001-<slug>.md.
Return only contract draft, assumptions, and open risks."
```

Human then opens Thread 2 and sends exactly that prompt.

Back in Thread 1:
```text
Thread 2 is done. Here is the result: <paste summary>.
Please integrate, resolve conflicts, and continue orchestration.
```

### Parallel decision responsibility

- Human does not micro-manage task decomposition.
- Orchestrator decides when to split work into parallel threads.
- Human acts as a router: open requested thread, run requested prompt, return summary.
- Final merge/priority/conflict decisions stay in orchestrator thread unless escalation is needed.

## IDE Notes

- Codex: best-fit workflow. `AGENTS.md` and scaffold docs are directly useful for operational context.
- Cursor/other IDE agents: usually require extra setup (`.cursorrules`, `CLAUDE.md`, or explicit prompt preamble) because they may not automatically follow `AGENTS.md`.
- Practical rule: keep the scaffold as the source of truth, then mirror key rules into each IDE's native config file.
- Global Codex guidance (`~/.codex/AGENTS.md`) is optional. If you use Codex for mixed contexts (work + vibe coding), keep global rules minimal and put workflow-specific rules in project `AGENTS.md`.
- If needed, use `~/.codex/AGENTS.override.md` only temporarily, then remove it.

## Installation

### Recommended: `uv tool`

```bash
uv tool install --from git+https://github.com/roydude/codex-vibekit.git codex-vibekit
```

### Alternative: `pipx`

```bash
pipx install git+https://github.com/roydude/codex-vibekit.git
```

### Alternative: project-local `venv + pip`

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install git+https://github.com/roydude/codex-vibekit.git
```

## Setup Order (Codex App, natural language)

1. Install `codex-vibekit` (any method above).
2. In your project root, run:

```bash
codex-vibekit init .
```

3. Open a new Codex App thread and send this:

```text
Use `$skill-installer`. Discover all skill folders under `skills/` that contain `SKILL.md` (including nested technique folders), install those folders into `$CODEX_HOME/skills`, report discovered skill names and installed absolute paths, and fail fast with exact error if any install fails.
```

4. Start daily work in your main thread with:

```text
Continue in orchestrator mode.
```

## Uninstall

### If installed with `uv tool`

```bash
uv tool uninstall codex-vibekit
```

### If installed with `pipx`

```bash
pipx uninstall codex-vibekit
```

### If installed in a project virtual environment

```bash
python -m pip uninstall codex-vibekit
```

Note: uninstalling the CLI does not remove files already injected into projects.

## Usage

```bash
codex-vibekit check
codex-vibekit init .
codex-vibekit codex-setup
```

## One-Time Codex App Setup

After `init`, run:

```bash
codex-vibekit codex-setup
```

Then open a new Codex thread, paste the printed prompt, and let `$skill-installer` install all skills from your project skill folders.

Daily use after one-time setup:

```text
Continue in orchestrator mode.
```

## What `init` does

- Copies `src/codex_vibekit/assets/scaffold/` into the target directory.
- Never overwrites existing files.
- If a destination file already exists, writes the new one as `*.vibekit-new`.
- Ensures today's `logs/work/WORKLOG-YYYY-MM-DD.md` exists.

### Core scaffold output

- `AGENTS.md`
- `PROJECT_HUB.md`
- `docs/templates/*`
- `docs/decisions/`, `docs/specs/`, `docs/design/`, `docs/contracts/`
- `logs/work/WORKLOG-YYYY-MM-DD.md`
- `skills/orchestrator/SKILL.md`
- `skills/planner/SKILL.md`
- `skills/builder/SKILL.md`
- `skills/critic/SKILL.md`

## Quick Smoke Test (repo checkout)

```bash
mkdir -p /tmp/vibekit-test && cd /tmp/vibekit-test
PYTHONPATH=/path/to/your/clone/src python3 -m codex_vibekit init .
find . -maxdepth 3 -type f | sort
```
