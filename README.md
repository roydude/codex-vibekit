# codex-vibekit (Light Mode)

`codex-vibekit` is a small CLI that injects an operating scaffold (folders/docs/skills) into a vibe-coding project root.

## Install (via uv)

```bash
uv tool install --from git+https://github.com/roydude/codex-vibekit.git
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
python -m venv .venv && source .venv/bin/activate
python -m pip install -e .
mkdir -p /tmp/vibekit-test && cd /tmp/vibekit-test
codex-vibekit init .
find . -maxdepth 3 -type f | sort
```

