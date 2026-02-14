from __future__ import annotations


def build_codex_setup_prompt() -> str:
    return """One-time Codex App setup request:

Use $skill-installer. Install these skill directories into $CODEX_HOME/skills:
- Discover all skill folders under skills/ that contain SKILL.md
- Include nested technique folders

Requirements:
1) Treat each discovered folder as one install unit.
2) If an installed destination already exists, fail fast with the exact error.
3) Keep existing agents/openai.yaml metadata from source folders as-is.
4) Report discovered skill names and installed absolute paths.
5) After install, remind me to restart Codex.

After setup, return:
- created/updated skill paths
- trigger summary for each skill
- a short "how to start" note for daily use
"""
