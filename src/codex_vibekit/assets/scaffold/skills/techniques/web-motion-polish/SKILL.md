---
name: web-motion-polish
description: "Add motion, micro-interactions, and dynamic feel to static web UIs (HTML/CSS/JS) while staying lightweight and accessible. Use when a web page feels visually flat or unresponsive and needs: view transitions, hover/press states, subtle animations (CSS/WAAPI), text reveal effects, ambient background motion, and interaction feedback. Works across all web UI styles — dashboards, landing pages, forms, games, terminal-like interfaces, and more."
---

# Skill: web-motion-polish

## Goal

Make the UI feel "alive" with small, intentional motion and feedback — not big graphical animation.

<HARD-GATE>
Before writing any animation code, you MUST:
1. Identify and present exactly 3 moments to enhance.
2. Get user approval on those 3 moments.
3. Present the motion spec (tokens + rules) for approval.

Do NOT implement until both approvals are received. This applies regardless of how simple the UI appears.
</HARD-GATE>

## Quick Workflow

1. **Audit the current UI** — identify flat/unresponsive areas
2. **Pick 3 moments** to enhance (don't boil the ocean):
   - Screen/view transitions (e.g. page load, route change, modal open/close)
   - Interaction states (hover, press, selection, disabled/locked feedback)
   - Content reveal (list population, result display, status update)
3. **Present 3 moments + rationale → get user approval**
4. **Define a motion spec** (tokens + rules):
   - Durations: `--t-fast: 120ms` / `--t-med: 180ms` / `--t-slow: 260ms`
     - 120ms: human threshold for perceived cause-and-effect (instant feedback)
     - 180ms: comfortable for state transitions without feeling sluggish
     - 260ms: enough for eye tracking on spatial movement (enters/exits)
   - Easing: `cubic-bezier(0.2, 0.8, 0.2, 1)` for UI interactions, `ease-out` for reveals
     - This curve starts fast and decelerates naturally, matching physical expectation
   - Animate only `opacity` and `transform` by default (compositor-only properties)
5. **Present motion spec → get user approval**
6. **Implement** with CSS first; use JS only for:
   - Toggling `data-state` attributes/classes
   - Typewriter text reveal (optional)
   - One-shot "shake/flash" feedback (locked/invalid actions)
7. **Run accessibility gates**
8. **Run ship check**

## Polishing Checklist (apply in order)

### Interaction Feedback
- Add distinct styles for `hover`, `active`, `focus-visible`, and "selected/hot"
- For locked/disabled actions: show a brief, readable cue (color shift + micro shake)
- Ensure every interactive element has visible state change within `--t-fast`

### View Transitions
- Implement enter/exit transitions with a single source of truth (e.g. `.is-active` + `.hidden` or `data-view="..."`)
- Ensure focus lands somewhere sensible after view change (first actionable element)
- Stagger sequential items if more than 3 appear at once (30–50ms offset per item)

### Content Reveal
- For new content: animate with fade + slight slide (`translateY(8px)` → `0`)
- For status updates: brief highlight pulse on changed element
- For sequential results: stagger reveal (subtle, not cinematic)

### Ambient Motion (optional)
- Lightweight background effect (gradient shift, subtle parallax, soft pulse)
- Must not reduce text contrast or readability
- Must be disabled entirely under `prefers-reduced-motion`

## Accessibility Gates

These are pass/fail requirements, not suggestions:

- [ ] `prefers-reduced-motion: reduce` disables or short-circuits all animations
- [ ] Every animation completes within 260ms (no infinite loops except opt-in ambient)
- [ ] `:focus-visible` has intentional, visible styling on all interactive elements
- [ ] No content is inaccessible while animation is in progress (no pointer-events: none during transitions unless intentional)
- [ ] Color contrast ratios maintained during all animation states (WCAG AA minimum)

## Ship Check

Verify each item before marking the skill complete:

- [ ] **No layout jank**: zero use of animated `height`, `width`, `top`, `left`, `margin`, `padding` — only `opacity` and `transform`
- [ ] **No forced reflow**: confirm no JS reads layout properties (offsetHeight, getBoundingClientRect) between DOM writes inside animation loops
- [ ] **Performance verified**: Chrome DevTools Performance tab shows 0 Layout Shift events caused by animations
- [ ] **No always-on expensive effects**: `box-shadow`, `filter`, `backdrop-filter` are not animated continuously (static application is fine)
- [ ] **Bundle impact**: no animation library added (CSS + WAAPI only, zero dependencies)
- [ ] **Fallback behavior**: UI is fully functional with all animations disabled

## Implementation Patterns (prefer in this order)

### Pattern A: Motion Tokens (CSS custom properties)

Define once, reuse everywhere:

```css
:root {
  --t-fast: 120ms;
  --t-med: 180ms;
  --t-slow: 260ms;
  --ease-ui: cubic-bezier(0.2, 0.8, 0.2, 1);
  --ease-reveal: ease-out;
}

@media (prefers-reduced-motion: reduce) {
  :root {
    --t-fast: 0ms;
    --t-med: 0ms;
    --t-slow: 0ms;
  }
}
```

### Pattern B: State-driven CSS (no JS animation timelines)

Use attributes/classes as the animation API:

```css
/* View states */
body[data-view="home"] .home-section { opacity: 1; transform: translateY(0); }
body[data-view="home"] .other-section { opacity: 0; transform: translateY(8px); }

/* Interaction states */
.choice.is-hot { transform: scale(1.02); }
.choice.is-locked-flash { animation: shake var(--t-fast) var(--ease-ui); }
.item.is-new { animation: fade-slide-in var(--t-slow) var(--ease-reveal); }
```

### Pattern C: WAAPI for one-shot effects only

Use `element.animate(...)` sparingly for:
- Brief shake on invalid action
- Quick pulse for confirmation feedback

Do NOT build sequenced choreography in JS. If you need sequencing, use CSS `animation-delay` with stagger offsets.

## Output Contract

When executing this skill, return:

1. **3 chosen moments** — what they are and why they were selected
2. **Motion spec** — tokens (durations, easing) and rules summary
3. **Files changed** — list of modified files with brief description of changes
4. **Accessibility report** — reduced-motion behavior, focus handling notes
5. **Ship check results** — all items passed with verification method noted