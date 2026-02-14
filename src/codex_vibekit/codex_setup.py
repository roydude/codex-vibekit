from __future__ import annotations


def build_codex_setup_prompt() -> str:
    return """One-time Codex App setup request:

Use $skill-creator to register four Codex-native skills from this project:
- orchestrator
- planner
- builder
- critic

Source of truth:
- skills/orchestrator/SKILL.md
- skills/planner/SKILL.md
- skills/builder/SKILL.md
- skills/critic/SKILL.md

Install location:
- $CODEX_HOME/skills/codex-vibekit-orchestrator
- $CODEX_HOME/skills/codex-vibekit-planner
- $CODEX_HOME/skills/codex-vibekit-builder
- $CODEX_HOME/skills/codex-vibekit-critic

Requirements:
1) Keep SKILL.md concise and keep trigger conditions in frontmatter description.
2) If agents/openai.yaml already exists, validate first and preserve it by default.
3) Regenerate agents/openai.yaml only when validation fails or required fields are missing.
4) If agents/openai.yaml is missing, generate it from SKILL.md.
5) When any regeneration happens, show before/after summary of changed interface fields.
6) Validate each skill and report installed paths.
7) Do not copy unrelated files.

After setup, return:
- created/updated skill paths
- trigger summary for each skill
- a short "how to start" note for daily use
"""
