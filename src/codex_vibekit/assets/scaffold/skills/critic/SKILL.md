# Skill: critic

## Purpose
Evaluate the product as the target customer: find usability and trust issues, score quality, and propose concrete improvements.

## When to Use
- After UX or implementation exists (even partially)
- Before shipping or sharing with users
- When something feels off but you can't pinpoint why
- As a sanity check on any major feature

## Required Inputs
- Orchestrator review request (what to review and why now)
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

Return to orchestrator with:
- priority-ordered issues
- quick wins
- ship/no-ship recommendation for current scope

## Constraints
- Use user language, not engineering jargon
- Be specific and actionable
- Don't propose large scope expansions as "quick wins"
- Quick wins should be achievable in under an hour each
- Keep review focused on assigned scope, not whole-project re-planning

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
