# ON-RAILS.md — the "start here" route ordering for the grammar map

The grammar map's job is to kill *"what do I study next?"*. This doc is the locked
design for how a goal becomes an **ordered, banded path** with a clear first step —
the stateless layer that the future account/state overlay writes onto unchanged.

Companion docs: durable IA in `TREE.md`; vertical-slice validation in `SLICE.md`;
Pass-2 teaching content in `CALIBRATION2.md`. This doc owns *ordering & goals*.

---

## 0. The model we're building on (settled)

- **One body of content, three reading postures.** *Dictionary* (lookup — what Google
  sees), *book* (browse a path anonymously), *library card* (account = own your place).
  The app is not a second product; it is the same tree plus a state layer.
- **The account adds exactly one primitive:** a `done / not-done` bit per node per user.
  Everything else — "what's next", "% complete", "level", "intellectual debt" — is a
  **projection** of that one bit over the graph we already have. Scope of the app is
  therefore tiny; this site is the anonymous app by construction.
- **Hard rule:** the account gates *state*, never *content*. Every node and every goal
  route renders fully, server-side, without auth — which is exactly what the crawler
  needs. The library card lets you *mark* the book; it can never be required to *read* it.
- **The graph is a shallow forest, not a deep tree.** Measured: of 1,458 nodes, only 263
  (18%) ever act as a prerequisite; the median "unlocker" unlocks exactly **1** node;
  `te-form` alone unlocks 71. So a narrow mandatory **trunk** (Foundations) plus a wide,
  largely-parallel **forest**. Ordering inside the forest is therefore by **frequency**,
  not by walking dependency edges that mostly don't exist. *Don't invent edges to fill a
  feature — that's the recurring trap.*

---

## 1. Goals = predicates → ordered banded paths

A **goal** is a coherent, search-shaped subset of the catalog (one goal = one predicate
= one query = one SEO/GEO landing page at `/learn/japanese/grammar/path/[id]`). The
discipline: **if two goals return the same node set, they are one goal with two names.**
Lifestyle labels that don't select distinct *grammar* ("Dating", "Raise a family") are
rejected — they collapse onto `casual-spoken`.

Each goal is rendered as an **ordered path**, chunked into **bands**. The path covers the
goal's full membership; the bands are the numbered backbone; the **first band's first few
nodes are the hero "start here" rail**.

### 1.1 Where order & membership live (canonical)

- **Membership + order are computed build-side in `build_slice.py`** and baked into
  `src/data/grammar_slice.json` as a per-goal ordered, banded node list. `order` is a
  property of the **(goal × node)** pair, not the node (て-form sits at different
  positions in different goals). The sort *logic* lives once in Python; the *result*
  ships as data. Both the web render and the future app read the same field.
- **`goals.ts` holds presentational metadata only** (label, h1, title, description, lede,
  intent, accent, tint). It no longer carries membership `match` predicates — those moved
  build-side, killing the TS/Python duplication.

### 1.2 Sort key (within a band)

`freq (essential→common→uncommon→rare) → jlpt (N5→N1) → family (FAMILY_ORDER) → canonical`.
Frequency first because, in a shallow forest, frequency *is* the "what next" answer.

---

## 2. Band axis — goal-type-specific (adapted to real data)

The band axis is whatever the learner actually reasons in for that goal. The lock said
"register goals band on a curated family→label map"; the catalog showed a **better axis
exists per goal**, so we use it. Intent (semantic, goal-appropriate bands; freq sorts
within) is unchanged.

| Goal | Band axis | Bands (in order) | Foundations |
|------|-----------|------------------|-------------|
| `jlpt-n5…n1` | **JLPT level (cumulative)** | Foundations, then N5, N4, … up to target | **Band 0, numbered** |
| `keigo` (40) | **`keigo` field** | 丁寧語 Polite → 尊敬語 Respectful → 謙譲語 Humble | compact spine |
| `casual-spoken` (948) | **`freq`** | Spoken essentials → Core conversational → Less common → Rare/advanced | compact spine |
| `read-novels` (139) | **curated stages** (hand-authored, kept) | the 4 `route_stages` | compact spine |

- **JLPT goals are cumulative** (`jlpt_rank <= target`). Selecting N3 lights N5→N4→N3 as
  one path — exactly how learners think ("get me to N3" = everything up to N3).
- **`keigo`** has its own sub-tags (sonkeigo/kenjougo/teineigo) — a cleaner, self-labeling
  axis than `family`. Pedagogical order: polite → respectful → humble.
- **`casual-spoken`** has only generic families across 948 nodes; `freq` is the honest
  axis and directly encodes "start here" (essentials first).
- **`read-novels`** keeps its hand-curated `route_stages` (literary ordering a sort key
  can't know); remaining literary members render family-grouped below the path.

---

## 3. The Foundations trunk

The mandatory spine every goal shares. Two presentations, by goal type:

- **JLPT goals → Foundations is Band 0, numbered.** The trunk *is* the content; a beginner
  picking N5 should start at は・が・を. "Start here" lands on the first Foundations node.
- **Register goals → Foundations is a compact "assumed spine"** shown above the path
  ("the shared spine — start here if you're new"), **not numbered into the path**. The
  goal's distinctive content leads the page (good for the keigo learner; good for SEO,
  since unique content sits high instead of under identical boilerplate on every page).

This split is also the cleanest demo of *why* the account matters: statelessly a register
goal only *says* "assumes Foundations"; with an account, "start here" reads your done-bits
and advances your frontier automatically.

---

## 4. Presentation

- **(b) only: grouped stations-in-stages, styled to read as a line.** No plotted metro
  geometry anywhere — a literal node-link diagram does not scale to 1,458 nodes. A
  connecting rail down each band + station dots on the cards gives the subway *feeling*;
  the grouped-card substrate scales and is what already exists.
- **Numbered at the band level, never per-node.** Hero = a short "start here / next few"
  rail (first content band, ~6 nodes). The full ordered, banded path sits below.
- **No locks.** Nothing is gated. Upcoming/not-yet-reached steps render **dimmed/quiet**,
  never with a padlock. Skipping is *intellectual debt* (a future gentle amber nudge),
  never a wall.

---

## 5. Deferred (parked, not adopted)

- Stats / points / streak / "Skills you're building" / achievements / target date — pure
  app state-over-time projections. Would also need per-node skill-dimension tagging we
  don't have.
- **"Unlocks / what becomes possible" panel** — render **nowhere** for now. The data only
  supports it on ~12–20 trunk hubs (te-form unlocks 71; median unlocker = 1); revisit as
  a hub-node-only badge later. Do **not** author fake edges to populate it.
- Per-node prerequisite *locking* — needs progress state ⇒ app, and contradicts §4.

---

## 6. Data shape emitted into `grammar_slice.json`

```jsonc
"goals": [
  {
    "id": "jlpt-n3",
    "band_axis": "jlpt",          // jlpt | keigo | freq | curated
    "foundations_mode": "band0",  // band0 | spine
    "member_count": 740,
    "written_count": 312,
    "bands": [
      { "index": 0, "key": "foundations", "label": "Foundations — the shared spine",
        "nodes": [ /* slim node + order */ ] },
      { "index": 1, "key": "N5", "label": "JLPT N5", "nodes": [ ... ] },
      { "index": 2, "key": "N4", "label": "JLPT N4", "nodes": [ ... ] },
      { "index": 3, "key": "N3", "label": "JLPT N3", "nodes": [ ... ] }
    ],
    "rest_members": []            // members not on the path (read-novels only)
  }
]
```

Each node carries a global `order` (1..N within the goal) — the canonical sequence the
account's "what's next" reads against the done-bits. Slim fields as elsewhere
(`slug, canonical, reading, meaning, freq, jlpt, family, register, keigo, written`).

The existing `foundations`, `branch`, `anchors` keys stay (the hub still consumes them);
`goals` is additive.

---

## 7. Session handoff — begin P1 (Search + IA restructure)

_Written 2026-06-30 at the end of a critique+P0 session. Read this section first to resume._
_Full findings + the ranked worklist live in **`CRITIQUE.md`** (repo root). This section is
the just-enough operating cursor to start P1._

### 7.1 Where we are
A four-persona critique of `/learn/japanese/grammar` (beginner, intermediate, expert,
frontend/IA) produced `CRITIQUE.md`. **All of P0 is shipped** (see the "Shipped" log there).
Net changes this session touched only:
- `src/pages/learn/japanese/grammar/index.astro` (the hub/map)
- `src/pages/learn/japanese/grammar/[slug].astro` (node template — provenance render)
- `CRITIQUE.md`, `ON-RAILS.md` (docs)

P0 shipped, briefly: reading-dedup on cards; removed the inline "Read novels" section
(route members fell into the family catalog, tagged `data-route`); **Frequency chips +
Family `<select>` filters** (the headline fix — data was on every card, unused); deleted
the duplicate "Or follow a goal route" row; copy rewrites (killed "Not a list — a map",
"light a route", em dashes); **provenance** on node pages (DBJG/DIJG/DAJG citation +
confidence caveat + JSON-LD `citation`); **dim → hide** (filtering now shrinks the page,
verified 48,662px → 3,809px on N5+Common); inlined the 4-stat hero row; breadcrumb +
CollectionPage/BreadcrumbList JSON-LD on the hub.

### 7.2 The current filter architecture in `index.astro` (what P1 extends)
The `<script>` at the bottom is vanilla, no framework. State + flow:
```
let preset="all";       // mutually-exclusive: all | foundations | goal:jlpt-n5..n1 | goal:read-novels | goal:casual-spoken | goal:keigo
let writtenOnly=false;  // toggle, ANDs
let freq=null;          // essential|common|uncommon|rare, ANDs   (data-freq chips)
let familyFilter="";    // family string, ANDs                    (#family-select change)
matchesPreset(c)  // per-card predicate for `preset`; JLPT goals are CUMULATIVE (rank<=target)
apply()           // ok = matchesPreset && freq && family && writtenOnly;
                  //   toggles `.dim` (== display:none); `filtering` flag hides empty .stage/.family;
                  //   showRail(); writes #filter-meta count
```
Click handler on `#filter` branches on `data-toggle="written"` / `data-freq` / `data-preset`.
Every card (anchors, Foundations, catalog) carries: `data-slug data-written data-route
data-freq data-jlpt data-fam data-reg data-keigo` (+ `data-found` on spine cards). Inside
each card, text is in `.jp` (canonical), `.reading`, `.meaning` (gloss). **The filters are
already combinable** (preset × freq × family × written all AND) — P1 builds on that, it
doesn't need to rewrite it.

### 7.3 P1 task list (priority order), with approach + anchors
_Status: **P1 complete** — items 1–5 all shipped 2026-07-01 (see CRITIQUE.md "Shipped — P1 batch 1/2/3"). Next: P2 content._

1. **✅ DONE — Client-side search box** (intermediate's #1 gap; no `<input>` exists today).
   - Add an `<input type="search" id="grammar-search">` into the `.filter` bar (top row).
   - Add `let query="";` state; a `matchesQuery(c)` that tests a lowercased haystack.
   - **Recommended:** emit a `data-search` attr at build on each card = lowercased
     `${canonical} ${reading} ${gloss} ${slug}` (robust vs. reading DOM text; note: no
     romaji data exists, so search covers JP + kana reading + English gloss + slug only).
   - AND it into `apply()` alongside the existing predicates; debounce input (~120ms).
2. **✅ DONE — "N3 only" (exclusive) mode** beside the cumulative JLPT chips (intermediate asked).
   Cheapest: a small "only this level" toggle that switches `matchesPreset`'s JLPT branch
   from `rank<=t` to `rank===t` (and stops OR-ing `data-found`).
3. **✅ DONE — Confusable-comparison surface** (both intermediate & expert). Built
   `/learn/japanese/grammar/compare/[set]` driven by `src/lib/compareSets.ts` (first set:
   the four conditionals). Aggregates each member's `equivalents[0]` + `keySentence` +
   `contrasts[]` into an at-a-glance row + a pairwise-difference grid; `FAQPage` JSON-LD.
   Linked in from each member node and the hub "Conditionals" family header. To add a set:
   append to `COMPARE_SETS` (id, family, copy, member slugs) — every member must carry a
   `contrasts[]` entry for each other member so the pairwise grid is complete.
4. **✅ DONE — Tame the *unfiltered* catalog.** Each family is now a native `<details>`,
   collapsed on load: unfiltered mobile scroll-height dropped ~180k px → ~11.7k px, with
   all 1,309 catalog cards still in the DOM (crawlable, openable without JS — not a content
   gate). `apply()` auto-opens families that contain matches while filtering and re-collapses
   them to the tidy default when browsing; an "Expand all families" button in the catalog
   head makes the full render opt-in. First screen is now hero + filter + Foundations.
5. **✅ DONE — Split navigation from refinement.** Added a goal-*destination* grid up top
   (after the hero, before the filter): 8 cards → `/path/[goal]`, split "By exam level"
   (5 JLPT, compact) and "By what you want to read or say" (3 register routes, with the
   goal's `intent` line). Each card shows the destination's own honest path total
   (foundations trunk + bands + rest_members), accent-striped/coloured per goal. The
   filter bar keeps its goal chips as *in-place refinement* — nav (go to the curated route)
   and refinement (light members in context) are now distinct affordances. Guardrails held:
   read-novels chip still lights its 22 `data-route` members, JLPT stays cumulative (N4=369)
   vs exact (241), families still collapse. Mobile: JLPT 2-up, routes 1-up, no overflow.

### 7.4 Deferred from P0 (fold into P1 where noted)
- **✅ DONE — pills → 8px radius** (DESIGN.md): all `.chip` + `.family-select` + `.route-links a`
  + the new `.search-input` moved 999px → 8px in one visual pass (2026-07-01).
- **Drop the monospace slug badge** from cards: it's dev-metadata leak, BUT it's currently
  the only disambiguator for near-duplicate cards (`tatte` vs `tatte-2`). Remove it *only*
  after giving sense-split cards human labels (e.g. 「たって ① even if」).

### 7.5 Verification pattern that worked
`npm run build` (Cloudflare adapter → output under `dist/client/...`; the hub is
`dist/client/learn/japanese/grammar/index.html`; scripts inline+minified, so grep tokens
not identifier names). Then `npm run dev` + Playwright MCP `browser_evaluate` to assert
behavior — e.g. count `.card:not(.dim)` and read `document.body.scrollHeight` before/after
clicking chips. **Clean up after:** `pkill -f "astro dev"`, and delete any
`.playwright-mcp/page-*.yml` / `console-*.log` and stray root `*.png` screenshots so
`git status` stays scoped.

### 7.6 Guardrails (don't regress)
- Filters stay **AND-combinable**; JLPT stays cumulative *unless* the new "only" toggle is on.
- The `read-novels` chip must keep lighting its members — they're catalog cards tagged
  `data-route="1"` (no longer a standalone section). Don't reintroduce that section.
- Everything renders server-side without JS/auth (§0 hard rule): search/filter are
  *progressive enhancement* over a fully-rendered catalog, never a gate on content.
- Light mode only, mobile-first, SVG icons only, no emojis (project rules).
