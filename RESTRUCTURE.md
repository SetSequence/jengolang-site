# RESTRUCTURE — One Spine, Three Doors

_2026-07-02. Synthesis of two research passes (codebase IA audit + competitive/UX
research) run against the three-mode goal: dictionary lookup, mastery path, custom
goal paths. This doc amends several TREE.md locked decisions and defines the surfaces
claude_design will design. Status: **direction signed off 2026-07-02** (see Decisions
at bottom); design handoff in `DESIGN_HANDOFF.md`; nothing built yet._

Companion docs: `CRITIQUE.md` (the P0–P2 worklist that got us here), `TREE.md`
(original locked IA — amended below, not replaced), `JengoApp/GAMEPLAN.md` §6.2
(the business frame: "a pathway, not a reference"; grammar eventually lives inside
the app as a third surface; per-point drill + save-to-SRS is the funnel).

---

## The verdict in one paragraph

The three modes are real, but they are **three doors, not three systems**. Build one
canonical mastery ordering over the whole catalog (the spine), then give each mode its
own thin surface over that single spine: a search-first lookup surface (dictionary), a
unit-based path surface with a progress overlay (mastery), and goal **lenses** that
highlight/gray sections of the same path without moving anything (custom). The current
hub fails because it tries to be all three doors on one page. The "8 goal paths" fail
because 6 of them are the same list truncated — the data proves the owner's instinct
right.

---

## Evidence (what the research found)

### From the codebase audit
- **The custom paths are an illusion in the data.** The 5 JLPT goals are strict nested
  supersets (N5=75 ⊂ N4=306 ⊂ … ⊂ N1=1,345 — same ordering, different cap).
  `casual-spoken` matches 852/1,458 nodes — not a carve-out. Only **keigo (37)** and
  **read-novels (22 curated + 117 rest)** are genuinely distinct subsets.
- **There is no mastery path today.** The 61-node Foundations line is the only curated
  ordering; everything after is a static sort (freq → JLPT → family). The prereq DAG
  (648 nodes) is nav chrome only — SLICE.md Finding 1 already showed it's too flat to
  order anything.
- **No progress state exists.** No localStorage, no check-offs, nothing. TREE #11
  planned it; it was never built. Green field.
- **Dictionary mode is a filter, not a surface.** Search is a substring filter over
  ~1,377 cards pre-rendered into one DOM. No romaji tolerance (haystack = canonical +
  kana + gloss + slug only). No lookup-first entry point.
- **App-embed readiness is poor.** Every page hard-codes marketing chrome ("Try
  Jengo" nav, AppCTA blocks, Google Fonts link); no embed/headless mode; the hub ships
  the full catalog in one document.
- **Coverage skew:** essential 97% / common 88% written, but rare = 94% stub and
  N1 = 36% stub. The far end of any mastery path is hollow; the entry is solid.
- **Coupling:** `index.astro` is 801 lines, all CSS+JS inline, and the client filter
  predicates duplicate `build_slice.py` membership logic. Any split must first decide
  where membership truth lives (answer: the build, once, baked into per-surface data).

### From the competitive research (full citations in the session transcript)
- **Bunpro** — one grammar-point base, multiple *orderings* (default JLPT spine +
  textbook paths). Paths work because they mirror an artifact the user already owns
  (their textbook); most users stay on the default. Its most-defended feature: example
  sentences scaffolded so each point only uses previously-taught grammar. Its SRS =
  typed cloze + ghost reviews; the two universal complaints are **answer ambiguity**
  and **review avalanche** at N2/N1.
- **MaruMori** — path-first adventure map, *plus* a plain flat JLPT grammar list as a
  parallel reference, because the map alone can't serve lookup. Gamification chrome is
  the top complaint ("cute graphics mostly get in the way after a while"); no way to
  reposition yourself on the path is the second.
- **renshuu** — cleanest split: a searchable Grammar Library (reference) and
  "schedules" (paths) as *different UI objects pointing at the same pages*.
- **imabi / JLPT Sensei** — the two failure poles: depth without progression
  scaffolding caps you at "supplement for enthusiasts"; shallow-but-findable wins
  search anyway. Findability beats depth in SERPs; depth wins trust once found.
- **Duolingo 2022** — forced linear path improved novice retention, enraged
  self-directed adults (our exact target). Their fix: keep the path, add jump-ahead.
  **WaniKani's unskippable levels are its #1 complaint** from the same demographic.
- **Khan Academy** — the strongest model for a website: one canonical structure,
  progress as a **mastery overlay** (per-skill state, per-unit bars), zero locks.
- **Choice overload** is documented for course catalogs specifically: several
  near-identical paths reduce commitment and satisfaction. Products offering both
  always aggressively promote **one default**; alternates exist only for users with an
  external reason (a textbook, an exam date).

---

## Amendments to TREE.md locked decisions

| TREE # | Was | Now |
|---|---|---|
| #5 "everything always visible, never hidden" | One canvas, all 1,458 nodes in the DOM, filters dim/hide | Retired **as a single-page rule**. Crawlability is preserved by real index pages per surface, not one mega-DOM. Within the path surface, "visible but grayed" survives as the lens behavior. |
| #8 "layered tech-tree canvas" | The map is the product | The map metaphor is demoted. The spine is the product; surfaces are a search page, a path page, and node pages. (MaruMori's map needed a flat list beside it anyway; our own CRITIQUE personas found the map crowded.) A visual map can return later as garnish, never as the primary nav. |
| #10 "goals = subway lines" (8 presets) | 8 parallel goal routes | JLPT goals become **milestones on the spine** (they're prefixes of it — render them as markers, not paths). Only goals that genuinely *exclude or reorder* material stay as lenses: **keigo**, **read-novels**, and (future, needs tag work) **spoken-only**. |
| #6 "position = prereq depth" | Already amended by SLICE Finding 1 | Confirmed: curated stage/unit is the axis; prereqs stay nav chrome ("Builds on" chips) and mesh metadata. |
| #11 "progress = localStorage now, app-sync later" | Planned, unbuilt | **Promoted to load-bearing.** The mastery surface is meaningless without it. v1 = localStorage; schema designed for Jengo-account sync from day one (GAMEPLAN §6.2 integration). |

Unchanged: node schema (content.config.ts), per-node URL scheme, noindex/thin-page
posture, Pass-2 enrichment rubric, the node page's section order.

---

## The architecture: one spine, three doors

### 0. The spine (data work, prerequisite for everything)
A single global ordering over all 1,458 nodes: **curated units** extending the
Foundations pattern. Foundations' 9 stages already exist; continue with curated units
through essential → common → uncommon, ending in honest appendix units for
rare/literary/N1 long-tail ("appendix: in progress" — coverage there is 6–64% and the
UI must say so rather than pretend).

- New data: `unit {index, label}` + within-unit `order` per node, produced by
  `build_slice.py` (or a sibling curated-units file it consumes). JLPT milestone
  markers computed from where each level's members are exhausted.
- Membership/ordering truth lives **only** in the build output; surfaces consume baked
  JSON. Kill the JS re-implementation of membership predicates.
- Long-term content rule (aspirational, enforce first in Foundations, then per unit as
  Pass-2 continues): a node's examples prefer grammar from earlier in the spine —
  Bunpro's most-defended feature and cheap to honor going forward even if not
  retrofitted.

### 1. Door one — Lookup (`/learn/japanese/grammar`)
The hub becomes the **dictionary**. Lean, search-first, jisho-shaped:

- One forgiving search box above the fold: accepts romaji (add romaji to the search
  haystack — it's absent today), kana, kanji, English gloss, and common surface forms.
  Instant as-you-type; results are rows (canonical + reading + gloss + JLPT + freq
  badge), not cards — disambiguation happens in the list.
- Below search: compact browse fallbacks — family index, gojuon index (DBJG users
  expect it; cheap), JLPT level indexes. These are links to index pages, not 1,377
  inline cards.
- Prominent but secondary: "Learning from zero? → the Path" and the 2–3 real lenses.
- The search index becomes a small baked JSON + tiny JS, not DOM cards. This is also
  the piece that ports into the app as the in-app grammar lookup.

### 2. Door two — The Path (`/learn/japanese/grammar/path`)
One canonical path surface, Khan-style overlay, zero hard locks:

- Unit-by-unit rendering (units collapse/expand; current unit open), each node a row
  with its learned-state checkbox. Per-unit progress bar; JLPT milestone markers
  inline ("everything above this line ≈ N5").
- **Self-placement:** "I already know this unit/section" bulk-marks — solves both
  Bunpro's missing placement and WaniKani's can't-skip complaint in one gesture.
- Progress in localStorage v1 (`{slug: state}` + revision field, designed to merge
  into a Jengo account later). Soft gating only — everything always clickable.
- Checkpoint slots reserved per unit (future: consolidation drills recycling only
  taught grammar — MaruMori's reading-exercise cadence). Slot now, content later.
- The old `/path/[goal]` JLPT pages remain as SEO landing pages ("N4 grammar
  checklist") but reframe as milestone views of the spine and link into the Path with
  the lens applied — they stop pretending to be separate curricula.

### 3. Door three — Lenses (on the Path, not beside it)
A lens = highlight/gray over the same spine; position and learned-state persist across
lens switches (the "speaking-only user later returns to reading" case falls out for
free — nothing was forked, so nothing is lost).

- v1 lenses: **keigo**, **read-novels**. **JLPT levels are milestones, not lenses.**
- **spoken-only** is desired but blocked on data: `casual-spoken` matches 852 nodes,
  so register tags can't carve it. Needs an exclusion pass (tag written-only/literary
  nodes precisely) before it's honest. Roadmap, not v1.
- Lens = a build-side node-set, same mechanism as today's route tags. No new model.

### 4. The node page (`/[slug]`) — smallest changes
Shape stays. Add: learned-state toggle (syncs with the Path), "next on the path →"
footer nav (the spine gives every node a successor), and a reserved slot for the
inline drill + "save to Jengo SRS" (GAMEPLAN §6.2's funnel — slot now, feature when
the app API exists).

---

## App-embed requirements (design now, so nothing fights it later)

GAMEPLAN §6.2: same content renders on the site and inside the app as a third surface.
Requirements for every new surface:

1. An **embed variant** (layout prop or `?embed`) that strips site nav, footer,
   AppCTA blocks, and ad slots. A "Try Jengo" CTA inside the Jengo app is absurd.
2. Node pages fully standalone — no dependency on hub context. (Already true.)
3. The lookup surface's search index consumable by the app directly (baked JSON, no
   DOM scraping).
4. No page ships the full catalog in one document. Lookup = JSON + rows on demand;
   Path = unit-chunked.
5. Fonts self-hosted or system-stack fallback in embed mode (currently a Google Fonts
   network dependency on every page).
6. Progress schema account-ready from day one: app activity eventually auto-fills the
   map (TREE #11's endgame, the strongest funnel).

## Grammar SRS (roadmap — design the seam, don't build)

- v1 site ships **learned-state only**. A "review today" queue is v2, keyed to
  learned-state timestamps.
- When built, engineer against the two universal complaints from day one: **answer
  ambiguity** (cloze with hint layers / accept alternates, or recognition-first on
  the site with production cloze reserved for the app) and **review avalanche**
  (hard daily cap, no guilt mechanics).
- Long-term the real SRS lives in the app (FSRS-6 already exists there); the site's
  queue should be a thin feeder, not a second scheduler. "Save this grammar point to
  your Jengo deck" > rebuilding Anki in the browser.

---

## Build order (proposed)

1. **Spine data** — curated units over the full catalog + JLPT milestone computation
   in `build_slice.py`. No UI change yet. (This is also a Pass-2 aid: enrich in spine
   order.)
2. **Shared chrome extraction** — pull the duplicated nav/tokens/CSS into a layout +
   components, with the embed variant designed in. Precondition for any split.
3. **claude_design handoff** — the three surfaces (lookup hub, path, node-page
   additions) as a designed system. Return, place in the seam.
4. **Lookup surface** (replaces hub) + baked search JSON with romaji.
5. **Path surface** + localStorage progress + lenses (keigo, read-novels) + milestone
   markers. Old `/path/[goal]` pages reframed as milestone/lens landing pages.
6. Node-page additions (learned toggle, next-on-path, drill slot).
7. Later: spoken-only exclusion tag pass, checkpoint drills, review-today queue,
   app deep-links.

## Decisions (owner sign-off 2026-07-02)

- **Unit granularity/naming — DECIDED.** Two levels: **arcs → units**. The path proper
  is essential + common (163 + 768 = 931 nodes) → **~35 units of 25–30 nodes** grouped
  into **7–8 capability-named arcs**; Foundations (61 nodes / 9 stages) is arc 1
  unchanged. Units carry **number + capability name** ("Unit 14 — Quoting and
  reporting"). Uncommon (419) = a coarser Extension tier (~10 units of ~40); rare (110)
  = 2–3 appendix units, UI honest about stub coverage there. Curation = the Pass-2
  subagent pattern: batches of 2–3 units into `scripts/data/spine_units.csv`
  (`slug, unit_index, unit_label, order`), linted (every non-fold slug assigned exactly
  once, no order gaps), consumed by `build_slice.py`. The spine file also becomes the
  Pass-2 worklist: enrich in spine order.
- **Family catalog — fold into lookup.** No standalone family browse page; family
  indexes live in the lookup surface's browse section.
- **`/compare/[set]` — paused.** Keep only comparisons that are *essential for beginner
  progression* (e.g. the four conditionals と/ば/たら/なら), and link those from their
  spine units so they're part of the path, not orphan pages. No new compare pages
  chasing rogue searches — thin comparison text is dead in the AI-answer era; these
  pages earn their existence pedagogically or not at all.
- CRITIQUE.md P2 leftovers (kana link-out, 5+ examples, ぬ/なり glosses) — unchanged,
  still open, orthogonal.
