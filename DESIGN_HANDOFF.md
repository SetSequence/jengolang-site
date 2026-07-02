# DESIGN_HANDOFF — Grammar section redesign for claude_design

_2026-07-02. Handoff for the "one spine, three doors" restructure. Decision-of-record:
`RESTRUCTURE.md` (read it first — this doc is the design brief, that doc is the why).
Scope: three surfaces + node-page additions. Return with a designed system; we place it
in the seam._

---

## What this is

jengolang.com's Japanese grammar section: 1,458 grammar-point pages derived from the
Dictionary of Basic/Intermediate/Advanced Japanese Grammar, currently fronted by a
single 801-line hub that tries to be a dictionary, a curriculum, and a goal-picker at
once. It's being split into three thin surfaces over one canonical ordering (the
spine). The same content must eventually render **inside the Jengo app** as an embedded
surface, so every design needs an embed variant with the marketing chrome stripped.

Audience: self-directed adult Japanese learners past kana. Two personas per surface:
the **looker-upper** (knows what they want, came from a search or the app, wants the
answer in seconds — jisho.org behavior) and the **path-walker** (learning front to
back, wants to know where they are, what's next, and what they can skip).

## Hard constraints (project rules — non-negotiable)

- Light mode only. No dark mode.
- Mobile-first. Most path-walkers will be on phones.
- No emojis anywhere. SVG icons only.
- No stock photos or abstract illustrations.
- Warm palette pulled from the Jengo app theme (see existing site pages for tokens) —
  but the grammar section needs an **expanded palette beyond the marketing tokens**.
  Grammar node pages differentiate many element types at once (formation slots, senses,
  example JP vs gloss, restrictions/warnings, contrast blocks, JLPT/freq/register
  badges, learned state, lens graying, stub framing) and the current few accents can't
  carry that. Deliver a **semantic color system**: each role gets a stable, named color
  used consistently across all three surfaces, legible on light backgrounds, and
  distinguishable when several roles co-occur in one component. This is a first-class
  deliverable, not a nice-to-have.
- Japanese text renders furigana via `<ruby>` — components must tolerate tall line
  boxes with ruby annotations.
- No gamification chrome (mascots, streaks, XP). Progress is calm and factual —
  Khan Academy's mastery overlay is the tonal reference, not Duolingo.

## The data available to every surface

Baked at build time from `build_slice.py` (no runtime API):

- Per node: slug, canonical form (kanji), kana reading, romaji, English gloss, JLPT
  level (N5–N1), frequency band (essential/common/uncommon/rare), family, register
  tags, keigo flag, stub flag (`noindex` — teaching content not yet written).
- Spine: every node gets `arc → unit {index, label} → order`. ~48 units in ~10 arcs;
  the path proper is ~35 units (essential+common, 931 nodes); then an Extension tier
  (~10 coarse units, 419 nodes) and 2–3 appendix units (110 rare nodes). Foundations
  (61 nodes, 9 stages) is arc 1.
- JLPT milestones: computed positions on the spine ("everything above this line ≈ N5").
- Lenses: two build-side node-sets — **keigo** (37 nodes) and **read-novels** (22
  curated + 117 extended).
- Learned-state: client-side, localStorage, `{slug: state}` + revision field. States:
  unlearned / learned (self-marked). Design should not preclude a third
  "auto-verified" state later (app sync).

## Surface 1 — Lookup hub (`/learn/japanese/grammar`)

The dictionary door. Replaces the current card-wall hub entirely.

- **One search box above the fold**, instantly filtering as you type. Input is
  forgiving: romaji, kana, kanji, English gloss, surface forms. This is the hero — the
  page should read as "search this" the way jisho.org does.
- **Results are rows, not cards**: canonical form (with ruby) + kana + one-line gloss +
  small JLPT badge + freq indicator. Dense, scannable, disambiguation happens in the
  list. Stub nodes visibly marked (they exist and are findable, but set expectations).
- Empty state (no query): compact **browse indexes** — by family, by gojuon (あ-row
  ordering, DBJG users expect it), by JLPT level. These are links to index pages, not
  inline content.
- Secondary but prominent: a "Learning from zero? → the Path" entry point, and the two
  lenses (keigo, read-novels) as labeled entry points.
- Needs a keyboard-first feel on desktop (focus search on load, arrow-key through
  results) without breaking mobile.
- This surface ports into the app nearly verbatim — keep it chrome-light by nature.

## Surface 2 — The Path (`/learn/japanese/grammar/path`)

The mastery door. Khan-style overlay, zero hard locks — everything always clickable.

- **Arc → unit → node rows.** Units collapse/expand; the user's current unit (first
  with unlearned nodes) opens by default. Node row = canonical + gloss + learned
  checkbox. Per-unit progress bar; per-arc rollup.
- **JLPT milestone markers inline** on the spine ("↑ N5 complete"). Levels are
  milestones, not paths — never render a "N4 path" as a separate object.
- **Self-placement:** "I already know this" bulk-mark at unit and arc level. This is a
  first-run moment worth designing well — an experienced learner should be able to
  place themselves mid-spine in under a minute without a quiz.
- **Lens toggle** (keigo / read-novels): lens-on grays non-members in place — nothing
  hides, nothing reorders, position and progress persist across toggles.
- **Honest tail:** Extension and appendix units render with visible "in progress"
  coverage framing (many nodes there are stubs). Do not pretend completeness.
- Reserved slot per unit for a future **checkpoint drill** (design the affordance,
  it ships empty/hidden for now).
- Progress is client-only in v1: design must read fine at 0% for a fresh visitor and
  not nag about accounts.

## Surface 3 — Node page additions (`/learn/japanese/grammar/[slug]`)

The page shape stays (title, explanation, formation, examples, contrasts, see-also).
Add three things:

1. **Learned toggle** in the header area, synced with the Path.
2. **"Next on the path →"** footer nav (the spine gives every node a successor;
   previous-node link too).
3. A **reserved slot** below examples for a future inline drill + "Save to Jengo SRS"
   CTA — design the container, feature comes when the app API exists.

Progression-essential compare pages (e.g. the four conditionals) get linked from their
spine unit — treat "compare" links as first-class within a unit, not orphan see-alsos.

## Embed variant (applies to all three surfaces)

The Jengo app will render these surfaces in-app. Every layout needs an embed mode:

- No site nav, no footer, no "Try Jengo" CTA/AppCTA blocks, no ad slots.
- System font stack or self-hosted fonts — no Google Fonts network dependency.
- Content column works at app-webview widths; no assumption of a marketing shell.

Design both variants together — the embed version is the same components minus chrome,
not a second design.

## Out of scope for this handoff

- SRS/review-queue UI (roadmap; only the reserved slots above).
- Spoken-only lens (blocked on a data tagging pass).
- Any visual map/tech-tree canvas — explicitly demoted, do not resurrect.
- The marketing landing page, vocab pages, and non-grammar site chrome.

## Deliverables wanted back

1. Designed system for the three surfaces + node additions: layout, component
   inventory, states (learned/unlearned, lens-on grayed, stub, embed), mobile and
   desktop.
2. The shared tokens/components split so the site shell and the embed variant come
   from one source.
3. First-run and self-placement flow for the Path.
4. Anything the spine data model above makes awkward — flag it, the data layer is
   still cheap to change.
