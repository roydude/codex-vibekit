# codex-vibekit (Light Mode)

`codex-vibekit` is a small CLI that injects an operating scaffold (folders/docs/skills) into a vibe-coding project root.

## Install

### Option A: pipx (recommended, no uv)

```bash
pipx install git+https://github.com/roydude/codex-vibekit.git
```

### Option B: uv (optional)

```bash
uv tool install --from git+https://github.com/roydude/codex-vibekit.git
```

### Option C: venv + pip (project-local)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install git+https://github.com/roydude/codex-vibekit.git
```

## Usage

```bash
codex-vibekit check
codex-vibekit init .
```

### `init` behavior

- Copies `src/codex_vibekit/assets/scaffold/` into the target directory.
- Never overwrites existing files.
- If a destination file exists, writes the new file as `*.vibekit-new` next to it.
- Creates today's work log at `logs/work/WORKLOG-YYYY-MM-DD.md` if missing.

## Local smoke test (repo checkout)

```bash
mkdir -p /tmp/vibekit-test && cd /tmp/vibekit-test
PYTHONPATH=/path/to/your/clone/src python3 -m codex_vibekit init .
find . -maxdepth 3 -type f | sort
```
