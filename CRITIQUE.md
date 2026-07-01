# Grammar Map — Multi-Perspective Critique & Fix Plan

_Generated 2026-06-30 from a four-persona review of `/learn/japanese/grammar` (live site + source). Personas: absolute beginner, upper-beginner→intermediate (the target user), near-fluent expert, and a frontend/IA design critic (run through the `impeccable` + `avoid-ai-writing` skills)._

**Primary target file:** `src/pages/learn/japanese/grammar/index.astro` (the map; hero, filter JS, catalog all live here). Secondary: `src/pages/learn/japanese/grammar/[slug].astro` (node template), `src/pages/learn/japanese/grammar/path/[goal].astro` (goal routes), `scripts/data/grammar_enriched.csv` + `scripts/build_slice.py` (catalog/Foundations ordering).

> Line anchors below are from the review snapshot and may drift as the file changes — confirm before editing.

---

## Decisions (chosen 2026-06-30)

- **Build focus:** P0 UI quick wins **and** the Search + IA restructure workstream.
- **Beginner scope:** _Add the missing rungs._ Build `verb-classes`, polite `ます`, and sequenced plain past/negative as Foundations nodes; add a kana link-out (Tofugu). The map becomes a true from-zero on-ramp rather than silently assuming kana + conjugation.
- **This file is the worklist.** Check items off as they ship.

---

## Shipped (2026-07-01 — P1 batch 1)

- **Client-side search box** (P1.1). A `type="search"` input with an SVG magnifier at the top of the sticky filter bar. Build bakes a `data-search` haystack onto every card (`canonical + reading + gloss + slug`, lowercased — no romaji data exists), so the client filters a string, not live DOM. Debounced 120ms, ANDs with every other filter. Verified: たら → 25 lit (page 48,709px → 3,084px), English "conditional" → 6, clear restores 1,377.
- **"Only this level" toggle** (P1.2). A toggle beside the JLPT chips that switches `matchesPreset`'s JLPT branch from cumulative (`rank ≤ target`, OR-ing Foundations) to exact (`rank === target`). Hidden until a JLPT preset is active; auto-resets when leaving JLPT. Verified: N3 cumulative → 685 (N3/N4/N5/Foundations), N3 exact → 316 (N3 only), N3-exact + "なら" search → 3.
- **Pills → 8px radius** (deferred P0 §7.4). All `.chip`, `.family-select`, `.route-links a`, and the new `.search-input` moved from `999px` to `8px` per DESIGN.md ("no pill/fully-rounded buttons") in one visual pass.
- **Confusable-comparison surface** (P1.3). New `/learn/japanese/grammar/compare/[set]` page + `src/lib/compareSets.ts` config (first set: the four conditionals と・ば・たら・なら). The page *aggregates* data already on the nodes — each member's `equivalents[0]`, `keySentence`, and `contrasts[]` — into an "at a glance" 4-card row + a 6-card pairwise-difference grid; no new grammar prose authored. Emits `FAQPage` JSON-LD (one Q&A per pairwise difference — the GEO shape for "difference between X and Y") + `BreadcrumbList`. Linked *in* from each member node (below "Easily confused with") and from the hub's "Conditionals" family header. Verified live: 4 members, all 6 pairs populated, 11 ruby, both inbound links resolve.

## Shipped (2026-07-01 — P1 batch 3)

- **Split navigation from refinement** (P1.5 — the last P1 item; **P1 complete**). Added a goal-*destination* grid at the top of the hub (after the hero, before the filter bar): 8 cards linking to the curated `/path/[goal]` routes, in two groups — "By exam level" (5 compact JLPT cards) and "By what you want to read or say" (3 register-route cards carrying the goal's `intent` line). Each card shows the destination page's *own* path total (foundations trunk + goal bands + `rest_members`, so N5=135 … N1=1,405, read-novels=139, casual=852, keigo=36) and is accent-striped + accent-labelled per goal (`goals.ts` colours). The lede now leads with "Pick a goal." Crucially this is *navigation* (go to the ordered route); the filter bar keeps its goal chips as *in-place refinement* (light members in context) — two distinct affordances instead of one overloaded chip row. Verified: all 8 hrefs resolve 200; guardrails intact (read-novels lights 22 `data-route` members, JLPT cumulative N4=369 vs exact 241, exact toggle hides on "All", families re-collapse); mobile 390px = JLPT 2-up / routes 1-up / no horizontal overflow.

## Shipped (2026-07-01 — P1 batch 2)

- **Tame the unfiltered catalog** (P1.4). Each of the 16 family groups is now a native `<details>`, collapsed on load. Unfiltered mobile (390px) scroll-height dropped **~180k px → 11.7k px**, while all 1,309 catalog cards stay in the DOM — crawlable and openable without JS, so it's an accordion, not a content gate (§7.6). `apply()` was split: `.stage`s keep the old empty-hide; families now auto-`open` when they contain a match while filtering and re-collapse to the tidy default when browsing returns to "All". An "Expand all families" button in the catalog head makes the full ~180k-px render opt-in (label toggles to "Collapse all families"). Chevron rotates on open. Verified: load = 0 open / 11.7k px; search たら = 6 families open, 10 hidden-empty, 25 lit, 5.5k px; N5 = 11 open / 144 lit; clear → 0 open / re-collapsed; expand-all → 16 open / 181.8k px.

## Shipped (2026-06-30)

- **Hide redundant kana readings on cards** — when the reading equals the displayed form (くれる / くれる, だ, は), the reading span is dropped. Genuine differences (前に/まえに, は/わ) still show. `index.astro` `sameReading()` helper, guards all three card types.
- **Removed the inline "Read novels" section** from the map. Featuring one (complex, literary) goal route right after beginner Foundations was an IA mistake; read-novels now lives in the family catalog with everything else and stays reachable via its chip (`data-route` tags moved onto catalog cards) and `/path/read-novels`.
- **Frequency + Family filtering** (the headline finding). New "Frequency" chips (Essential / Common / Uncommon / Rare) and a "Family" `<select>` (16 families), both ANDing with the route/level preset and the written toggle. Verified live: Common → 701 lit; Family=conditional → 48 lit and **surfaces 〜と/たら/〜ば/なら from Foundations** (fixes the "Conditionals bucket omits the four" complaint); Family+Common → 20 lit.
- **Deleted the duplicate "Or follow a goal route" link row** — the second near-identical pill row the owner flagged. Goal routes stay reachable via the filter chips + the start-here rail's "Full route →" links (still crawlable in HTML) + `/path/[goal]` pages.
- **Copy rewrites** (avoid-ai-writing). Killed "Not a list — a map," "light a route/level/goal," and the em dashes across the hero lede, filter label ("Filter the map"), section subtitles, catalog blurb, and the "About this map" note. Plainer, more direct voice; removed the designer-arguing-with-the-reader dim rationalization.
- **Provenance on node pages** (`[slug].astro`). A "Sources" footer citing the DBJG/DIJG/DAJG volumes each point derives from (data was in `sources.volumes` all along, rendered nowhere), a low/medium-confidence caveat, and the dictionary titles fed into the Article JSON-LD `citation`. The expert's #1 authority win.
- **dim → hide.** Filtering now removes non-matching cards (`display:none`) instead of dimming them, so the page collapses to the lit set (verified 48,662px → 3,809px on N5+Common). Directly addresses the mobile-wall complaint.
- **Hub polish.** Inlined the 4-stat hero-metric row (impeccable-banned template) to one muted line; added a visible breadcrumb and CollectionPage + BreadcrumbList JSON-LD so the internal-linking hub is marked up like the `/path` pages.

---

## The headline finding (all four personas)

**Frequency bands are dead data.** Every card emits `data-freq` (essential / common / uncommon / rare) and renders a freq badge; the lede even promises filtering "by family" — but `matchesPreset` (index.astro:~508–525) has no `freq` or `family` predicate. Cheapest high-value fix on the board, and the false "filter by family" promise in the lede (index.astro:~302) is a broken affordance until fixed.

---

## Cross-cutting themes (2+ personas agreed)

1. **One job offered four times — chaos is structural.** (beginner + frontend) Four parallel routes to the same goals: filter chips (dim-in-place, ~320–326) → "Or follow a goal route" links (navigate, ~362–370) → hidden "start here" rail (~333–360) → the real `/path/[goal]` pages. Chips and link row are near-identical pills ~40px apart with different behaviors. The clean experience already exists (the `/path` pages); the hub is four vague teasers for it.
2. **Metaphor-register copy the owner + brand docs dislike.** (beginner + frontend) "Not a list — a map" is an AI-ism ("not X — it's Y" + em dash) and fights PRODUCT.md's direct voice. Whole page runs on _map / route / light / spine / trunk / rail_; "light a route" is invented jargon. Em dashes in nearly every section head.
3. **No search; lookup is a dominant use case.** (intermediate + frontend) Zero `<input>`. Filtering _dims_ (opacity .26, ~256) instead of _hides_, so the DOM is always ~1,377 cards. Mobile page is **182,339px (~216 screens)** tall.
4. **Stub honesty good globally, empty where it matters.** (intermediate + expert) 1,195/1,458 framing is honest; N3/common zone ~95% written. But 94% of "rare" and ~47% of N1 are stubs, and read-novels is 59/139 written — _below_ average. Route-level truth isn't surfaced.
5. **Written nodes are good but thin on examples.** (intermediate + expert) Contrast cards (たら→と/ば/なら; のに→けど/から) are the most-praised feature. But ~3 examples/node vs the 5–10 the spec requires.

---

## Persona-specific findings

### Absolute beginner — content gaps, not just UI
- **Verb classes (godan/ichidan/irregular) never taught** — no node exists. Can't derive ます/ない/て/た without it. "Single biggest hole."
- **Polite ます-present and sequenced plain past/negative are missing as taught skills** — only the abstract 連用形 stem exists.
- **No kana on-ramp / no Tofugu link-out**, despite the JENGOLANG plan calling for it; early examples furigana-annotate only kanji, leaving kana unreadable to a true beginner.
- **"Forms you build on" leads with raw 連用形 / 使役形 / 意向形** — intermediate forms as the first content block, before anything is explained.
- Order itself is fine: leading だ/です/は matches Genki + Tae Kim. The missing conjugation rungs are the problem, not the sequence.
- か is buried 11th in a 13-particle wall instead of an early "ask a question" beat.

### Intermediate (target user)
- **"Conditionals (43)" family bucket omits と/たら/ば/なら** — they're sequestered in Foundations, so the section labeled "Conditionals" shows only compound forms. Label promises what it doesn't contain.
- **JLPT chips are cumulative-only** — N3 also lights N5+N4+Foundations; no "N3 only," no combinable filters.
- Filters mutually exclusive (`preset` is a single string) — can't ask "N3 + common + conditionals."
- Near-duplicate cards disambiguated only by a cryptic monospace slug badge (`tatte-2`) — reads as a data dupe, not an intentional sense-split.
- Genuine strengths: stub honesty, ~95% N3/common coverage, best-in-class contrast cards.

### Near-fluent expert
- **Provenance is invisible.** Every content file carries `sources.volumes` (B/I/A = Dictionary of Basic/Intermediate/Advanced Japanese Grammar) + `confidence`; rendered on zero pages. ~10-line template change, biggest authority win.
- **Mis-glosses:** `nu.md` gives ぬ as negative-only (omits 完了 perfective ぬ); `nari.md` surfaces modern temporal なり, not classical 断定/伝聞 copula.
- **"Read novels" over-claims "classical"** — missing the 文語 spine (べし / む / けり / き / 完了 つ・ぬ・たり / らむ / けむ / まじ); band 2 is really formal-written modern + kanbun fossils.
- One-directional confusable: `noni.md` should contrast くせに. `family: particle` mislabels suffixes (ぶり = 接尾語).

### Frontend / IA
- **Drop the 4-stat hero-metric row** (~305–310) — impeccable absolute-ban template + PRODUCT.md anti-reference. Inline as one muted sentence if kept.
- **Pills → 8px radius** (~164, ~200) per DESIGN.md ("no pill/fully-rounded buttons").
- **Card-everything** violates DESIGN.md ("alternate bg/brand-tint for rhythm") + impeccable ("cards are the lazy answer"). Differentiate Foundations from the catalog with background rhythm.
- **Drop the monospace slug badge** from user-facing cards (~414, ~476) — dev metadata leaking to users.
- **Hub lacks breadcrumb + JSON-LD** (head ends ~104, canonical-only) while the `/path` pages have ItemList/BreadcrumbList — the strongest hub page is the least marked-up.
- Plain-voice copy rewrites supplied for hero, all section subtitles, catalog blurb, and the "About this map" note (kill em dashes + metaphor verbs).

---

## Prioritized fix list (the worklist)

### P0 — quick wins (hours; index.astro / [slug].astro)
- [x] Add **freq-band + family filtering** — done; ANDs with preset + written toggle.
- [x] **Delete the "Or follow a goal route" link row** — done.
- [x] **Rewrite hero + section subtitles** — done (hero, filter label, subtitles, catalog blurb, note).
- [x] **Render provenance** on `[slug].astro` — "Compiled with reference to A Dictionary of Basic/Intermediate/Advanced Japanese Grammar" footer + low/med confidence caveat + JSON-LD `citation`. Done.
- [x] **Switch catalog filter dim → hide** — done; verified N5+Common shrinks the page 48,662px → 3,809px (~8%), full restore on clear.
- [x] Inline the 4-stat hero-metric row → one muted `.statline`; add breadcrumb + CollectionPage/BreadcrumbList JSON-LD to the hub head. Done.
- [ ] **Deferred:** pills → 8px (DESIGN.md) — do all chips + the new family `<select>` together in one visual pass. Drop the monospace slug badge — deferred until sense-split cards get human labels (P1), since the slug is currently the *only* disambiguator for near-duplicate cards (tatte / tatte-2).

### P1 — Search + IA restructure (days)
- [x] **Client-side search box** over canonical / reading / gloss in the sticky filter bar. Done 2026-07-01 (`data-search` haystack + debounced input).
- [x] **Combinable filters + "N3 only"** — filters were already AND-combinable (P0); added the "Only this level" exact-JLPT toggle. Done 2026-07-01.
- [x] **Confusable-comparison surface** — `/grammar/compare/conditionals` (と・ば・たら・なら side by side), linked from each member node + the hub Conditionals family header. Done 2026-07-01.
- [~] **Fix the Conditionals bucket** — partially addressed: the "Conditionals" family header links to the compare page (which holds all four base forms) and search surfaces them. Still open after the P1.4/P1.5 reshuffle: the four base forms are not *inline* in the family grid (they live in Foundations, deliberately excluded from the catalog via `spineSlugs`). Remaining fix if desired: a pinned "also in Foundations →" row at the top of the collapsed Conditionals `<details>`. Low priority — reachable via Foundations, compare page, and search.
- [x] **Tame mobile** — collapsed each family behind a native `<details>` (content stays in the DOM, not a JS gate); unfiltered 390px page ~180k px → 11.7k px; filters auto-open matching families; "Expand all families" makes the full render opt-in. Done 2026-07-01.
- [x] **Split navigation from refinement** — goal *destination* cards up top (8 → `/path/[goal]`, split exam-level / register-route, honest per-route totals); the filter bar's goal chips stay as in-place refinement. Done 2026-07-01.

### P2 — content (touches grammar_enriched.csv + build_slice.py)
- [x] **Add Foundations nodes** (2026-07-01). Authored `verb-classes` (godan/ichidan/irregular — the classification every formation table referenced but no page taught; now leads the "Forms you build on" anchors row) and `masu-form` (the polite ます/ません/ました/ませんでした paradigm; only the abstract 連用形 stem existed before). Both enriched to the Foundations exemplar standard (5 examples, full furigana, formation tables, contrasts, the ru-verb godan trap 帰る/入る/知る). Catalog 1,458→1,460. `verb-classes` prepended to `ANCHOR_SLUGS`; `masu-form` inserted after `masu-stem` in the "Verb bases & politeness" stage (and lands in the 丁寧語 keigo band). **Sequenced plain past/negative:** no new nodes — `ta-form`/`nai-form` already exist and are well-enriched; the real gap was the missing `verb-classes` prerequisite feeding them, now closed. **か reorder:** pulled from 11th to 6th in "Core case & binding particles" (now right after で — an early "ask a question" beat), ね/よ kept sentence-final. build_slice PASS, lint OK, prod build green, furigana verified (verb-classes 50 ruby / masu-form 35).
- [ ] **Add kana link-out** (Tofugu) on the map + a "this map assumes kana" note.
- [ ] Push written nodes to **5+ examples** (per spec).
- [ ] Fix **ぬ / なり** glosses; populate or relabel the **classical** route; reclassify suffix `family` mislabels.

---

## Source reports
Full per-persona reports (with citations and quotes) are in the chat transcript that generated this file. Research cited by the beginner audit: Genki I&II grammar index (St. Olaf), Tofugu Genki review, Tae Kim's Guide, Coto Academy N5, JLPT Samurai N5.
