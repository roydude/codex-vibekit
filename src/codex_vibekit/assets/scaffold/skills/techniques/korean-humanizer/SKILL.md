---
name: korean-humanizer
description: Edit Korean text to remove AI/translationese signals and make it read like a real person wrote it, while preserving meaning and keeping tone/honorific level consistent. Use when the user asks for “휴머나이징”, “번역체 제거”, “AI 티 없애줘”, “사람처럼 말해줘”, or when Korean output is destined for publishing (blog/report/SNS) and currently sounds generic, over-formal, or template-like.
---

# Skill: korean-humanizer (technique)

## Purpose
Detect common “AI-written” patterns in Korean and rewrite into natural, human-sounding Korean without changing the core message.

## Used By
- `orchestrator`, `planner`, `builder`, `critic` (any time Korean output quality matters)

## Required Inputs
- Source text (and any formatting constraints)
- Target genre: blog / internal report / SNS / press release (if unknown, infer from context and say your assumption)
- Target tone + honorific level: `합니다체` / `해요체` / `해라체` (default: preserve the dominant style in the source)
- Hard constraints: keep facts, keep terminology, length limit, must-keep phrases (if any)

## Workflow
1. **Lock tone**: Choose one honorific level and keep it consistent.
2. **1st pass (K-patterns)**: Fix Korean-structure issues first (e.g., 조사 ‘의’, 명사화, 피동, 번역투).
3. **2nd pass (C-patterns)**: Remove generic/marketing filler (e.g., 과장, 모호한 출처, 접속부사 과잉, 군더더기).
4. **Rhythm & voice**: Vary sentence length, add a natural cadence, and (only when appropriate for the genre) add light 1인칭/구어 요소.
5. **Meaning check**: Do a final read to ensure meaning, emphasis, and constraints stayed intact.

## Quick Checklist (fast scan)
- ‘의’가 연쇄로 붙어 딱딱함 → 문장 쪼개기/동사화
- “~할 수 있습니다/것입니다/…으로 보입니다” 반복 → 단정/구체화/필요하면 불확실성 명시
- “다양한/효과적인/혁신적인/핵심적인” 같은 범용 형용사 → 구체적 사실/예시로 대체 (새 사실은 만들지 말기)
- 접속부사(또한/더불어/나아가) 연속 → 삭제/문장 합치기
- 명사화/피동 남용 → 능동 + 동사 중심으로 재구성
- 문단 리듬이 전부 같음 → 짧게/길게 섞어 리듬 만들기

## Output Contract
Return:
1) **Rewritten text** (ready to paste)
2) *(Optional, short)* **Change summary**: 3–7 bullets (what patterns you fixed and where, without a full diff)

## Constraints (do not violate)
- Do **not** invent new facts, numbers, quotes, or sources. If the rewrite needs evidence, ask for it or keep the claim appropriately vague.
- Preserve the author’s intent; avoid “over-polishing” into press-release tone unless that’s the target genre.
- Keep the document’s formatting contract unless asked to redesign structure.

## Reference
For the full pattern catalog (K1–K8, C1–C10) and genre tone guidance, read: `references/patterns.md`.

