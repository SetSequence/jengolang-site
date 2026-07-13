# SPINE.md — building the grammar spine (ordering handoff)

_Handoff for a placement pass. This doc is self-contained: a fresh model should be
able to build the spine from this + the repo, without the conversation that produced it._

**Status: reoriented 2026-07-10.** `scripts/data/spine_units.csv` assigns every one
of the 1,419 non-fold nodes on a readiness-first path. The active task is now local
refinement, not first-pass placement.

**Decision-of-record this implements:** `RESTRUCTURE.md` ("one spine, three doors",
signed off 2026-07-02) → its **Decisions** section (arcs→units granularity) and §0
(the spine). Companion context: `ON-RAILS.md` (goal ordering, now subsumed),
`DESIGN_HANDOFF.md` (the three surfaces that consume the spine), `PASS.md` (the
*enrichment* project — separate from this one; see §1).

---

## 1. The one idea that makes this tractable

**Ordering and enrichment are two different projects.** Do not conflate them.

- **Enrichment (Pass-2, `PASS.md`)** = writing the *teaching layer* inside each node
  (explanation, examples, contrasts). Status ~1,217/1,460 written. A marathon.
- **The spine (this doc)** = deciding the *canonical learning order* of all nodes and
  grouping them into arcs → units. Pure metadata. A curation pass, much faster.

**A node's identity is fixed in its seed frontmatter — enrichment does not discover it.**
Every one of the 1,460 nodes (enriched or stub) already carries `title` (with an English
gloss), `canonical`, `reading`, `register`, `keigo`, `freq`, `jlpt`, `family`, and
`candidate_prereqs`. That is everything you need to *place* a node. Example stub:

```yaml
title: "この上ない — the utmost"
canonical: "この上ない"
reading: "このうえない"
register: ["written-modern", "literary"]
freq: "rare"
jlpt: "N1"
family: "modality"
noindex: true          # ← stub: teaching layer not written. Order it anyway.
```

**Therefore: you can and should order all nodes now, stubs included.** You are never
blocked on enrichment. Ordering never edits node prose — it writes a separate CSV.

Corollary for the tail: fine "3rd vs 4th within a unit" judgment is easiest when the
point is written. The **essential+common band is ~90% enriched**, so its fine ordering
is well-supported today. Stubs cluster in the **uncommon/rare tail**, which by design
only gets *coarse* buckets (see §4) where exact within-unit order barely matters — so
even the stubs don't hold you up.

---

## 2. The artifact

A single new file: **`scripts/data/spine_units.csv`**

```csv
slug,unit_index,unit_label,order
da,1,Copula & the は～だ frame,1
desu,1,Copula & the は～だ frame,2
...
```

- `slug` — matches a `.md` filename in `src/content/japanese/grammar/` and a row in
  the catalog (§3). One row per placed node.
- `unit_index` — integer, globally increasing across the whole spine (1..~48).
- `unit_label` — "capability name" for the unit (see §4). Repeated on every node in the
  unit (denormalized on purpose; keeps the file greppable and diff-friendly).
- `order` — integer position **within the unit**, 1..N, no gaps.

The learner-facing arc and unit names live beside `ARC_RANGES` in
`scripts/build_slice.py`. The CSV keeps stable curation labels; update the display map
when a unit’s capability name changes.

Arc grouping is derived, not a column: units map to arcs by `unit_index` ranges
(define the arc→unit-range table in `build_slice.py`, §7). Keep it a range table, not a
per-row arc column, so re-parenting a unit is a one-line edit.

---

## 3. Data source

`scripts/data/grammar_enriched.csv` — the catalog, **1,460 rows**. Columns:

```
term, slug, canonical, reading, meaning, senses, register, keigo, freq, jlpt,
family, candidate_prereqs, fold_into_parent, confidence, review_reason,
src_risk, src_volumes, src_glosses
```

Use `meaning` + `family` + `freq` + `jlpt` + `candidate_prereqs` to judge placement.
`meaning` (and the node `title`) give you the point's identity without opening the node.

**Distribution (know your shape):**

| freq | count | spine treatment |
|------|------:|-----------------|
| essential | 163 | the path proper — fine units |
| common | 768 | the path proper — fine units |
| uncommon | 419 | Extension tier — coarse units |
| rare | 110 | Appendix — 2–3 units, UI honest about stub coverage |

| JLPT | N5 | N4 | N3 | N2 | N1 | none |
|------|---:|---:|---:|---:|---:|-----:|
| count | 133 | 269 | 340 | 389 | 321 | 8 |

Families (largest first): connective 467, modality 285, adverbial 213, particle 156,
other 110, auxiliary 66, conditional 48, aspect 41, nominalizer 18, quotation 12,
copula 12, honorific 10, form 9, interjection 5, passive 4, causative 3, counter 1.

**Folds:** 41 rows have `fold_into_parent` set. These are noindex redirect-hubs, not
standalone pages (`PASS.md`). **Exclude them from `spine_units.csv`** — they have no
independent position; they live as a `variants`/`note` on their parent. The lint (§6)
must allow unassigned fold rows and flag any *non-fold* slug that's missing.

---

## 4. Structure — arcs → units (granularity is decided)

From `RESTRUCTURE.md` Decisions (do not relitigate):

- **Two levels: arcs → units.** ~48 units in ~7–10 arcs total.
- **Path proper = essential + common (163 + 768 = 931 nodes) → ~35 units of 25–30**,
  grouped into **7–8 capability-named arcs**. Units carry **number + capability name**
  ("Unit 14 — Quoting and reporting").
- **Extension tier = uncommon (419) → ~10 coarser units of ~40.**
- **Appendix = rare (110) → 2–3 units.** The Path UI must visibly frame these as
  "in progress" (coverage there is mostly stubs) — that framing is downstream, but
  keep rare in its own arc so the UI can gate the honesty banner on arc identity.

Foundations is **arc 1, already built — reuse it verbatim** (§5).

The Path also has a non-catalog **Start here** primer before Unit 1. It checks kana
readiness and introduces predicate-final order, dropped pronouns, particles, and the
reference words used in early examples. It is a path prerequisite, not a catalog node.

### Chosen arc skeleton (reoriented 2026-07-10)

The first placement exposed a structural error: concept-first arcs put advanced patterns
in front of basic material from a different family. The path is now **readiness first,
concept second**. A concept may recur at several stages; that is deliberate. It is much
better to teach the everyday part of time/aspect before its formal or literary part than
to force every time expression into one early arc.

The spine uses **9 arcs and 55 units**. The extra units keep a learner from receiving a
50+ node concept dump while preserving a single canonical order.

| arc | units | capability progression |
|---:|---:|---|
| 1. Foundations | 1–10 | sentence frame, core particles, and conjugation |
| 2. Everyday Japanese | 11–20 | requests, negation, て-form, aspect, wants, and basic conditions |
| 3. Building sentences | 21–24 | describing, comparison, time, reasons, and simple contrast |
| 4. Everyday interaction | 25–30 | plans, ability, permission, obligation, advice, and quotes |
| 5. Expanded expression | 31–37 | common patterns that deepen the same everyday capabilities |
| 6. Precision & discourse | 38 | formal framing, nuance, and careful expression |
| 7. Extension | 39–44 | uncommon patterns that extend the core path |
| 8. Advanced comprehension | 45–51 | formal, literary, and high-level reading grammar |
| 9. Appendix — rare and literary grammar | 52–55 | rare, classical, and specialist patterns |

Within each readiness arc, units group related forms (for example, linking ideas or
everyday intention), but **a later arc may never supply an earlier learner's basic
toolkit**. `keigo` and `read-novels` remain lenses; they do not create competing routes.

---

## 5. Foundations = arc 1, already curated (reuse, don't redo)

`scripts/build_slice.py` already defines the Foundations line as **9 pedagogical stages,
61 slugs**, hand-ordered — this IS arc 1. Lift it verbatim into `spine_units.csv` as
units 1–9 (each stage = one unit; keep the stage label as the unit label; `order` = the
slug's index within the stage list). Source of truth, copy exactly:

```
FOUNDATION_STAGES (build_slice.py ~line 55):
1 Copula & the は～だ frame           da, desu, wa-2, no-3, janai, datta
2 Core case & binding particles       ga-2, o, ni-2, ni-3, de, ka, e, to-2, mo, kara-3, made, ne, yo
3 Verb bases & politeness             masu-stem, masu-form, te-form, nai, kudasai
4 て-form uses & aspect               te, te-kudasai, te-iru, te-kara, te-mo-ii, te-wa-ikenai, te-shimau, te-miru
5 Benefactive giving/receiving        ageru, kureru, ageru-2, kureru-2, morau
6 Desire & basic modality             tai, hoshii, darou, deshou, kamoshirenai, hazu
7 The four conditionals               to-conditional, tara, ba, nara
8 Clause connectives & temporal       kara, node, kedo, ga-3, noni, nagara, toki, mae-ni, ato-de
9 Nominalizers & comparison           koto, no-ga-suki, no-hou-ga, yori-no-hou-ga, ichiban
```

(The `ANCHOR_SLUGS` list — verb-classes, masu-stem, te-form, ta-form, nai-form,
ba-conditional, volitional-form, causative-form, counter — are the 9 form anchors.
Their placement is now complete: `counter` is appended to unit 2; `verb-classes`,
`ta-form`, and `nai-form` sit in unit 3; `volitional-form` in unit 6;
`ba-conditional` in unit 7; and `causative-form` starts unit 10. The original
Foundation sequence remains intact as a subsequence.)

**`read-novels`** already has a hand-curated 4-stage literary route in `build_slice.py`
(`BRANCH.route_stages`, ~22 slugs). Its common prerequisites remain where they are
first learned; its rare literary forms sit in the Appendix. The route is a lens over the
spine, not an appendix-only sequence (§8).

---

## 6. Within-unit order & the placement loop

### Sort within a unit
Primary signal is the **readiness arc**, then JLPT and frequency within that arc. This
is the hard guard against an advanced member of a concept family arriving before a
beginner's everyday grammar from a different family:

`readiness arc → jlpt (N5→N1) → freq (essential→common→uncommon→rare) → family → canonical`

`FAMILY_ORDER` (from build_slice.py, keep consistent):
`particle, copula, aspect, conditional, auxiliary, modality, quotation, nominalizer,
causative, passive, honorific, connective, adverbial, counter, form, interjection, other`

`candidate_prereqs` is a **sanity check / tiebreak, not the sort key** — the enriched
prereq DAG is too sparse to order the spine (SLICE.md Finding 1; RESTRUCTURE §"no
mastery path today"). Use it only to catch "this obviously needs that first" inversions.

But the unit is a *pedagogical cluster*, so the human/curation judgment overrides the
mechanical sort when a teaching sequence is clearer. The mechanical sort is the default;
override deliberately.

### The loop (mirror the PASS.md subagent-brief pattern)
1. **Pick a batch of 2–3 adjacent units** (thematic cluster, in spine order).
2. **Spawn an `Explore` agent** for the batch's candidate slugs → returns a compact
   brief: each slug's `meaning`, `family`, `freq`, `jlpt`, `candidate_prereqs`, and
   which siblings are already enriched. (Replaces grep round-trips; keeps you on
   judgment.) Same pattern PASS.md §3 uses for enrichment.
3. **Assign** each slug an `unit_index`, `unit_label`, `order`; append rows to
   `spine_units.csv`.
4. **Lint** (§ below). Fix. Move on.
5. **Checkpoint:** every non-fold slug ends up assigned exactly once by the end.

Work the path proper (arcs 2–7) first — it's the enriched, high-value core and what the
Path UI renders first. Then coarse-bucket the Extension and Appendix tiers.

### Lint (write `scripts/lint_spine.py`, or fold into `lint_batch.py`)
- Every non-fold catalog slug appears in `spine_units.csv` **exactly once**.
- No `order` gaps within a unit (1..N contiguous); no duplicate `(unit_index, order)`.
- `unit_index` values contiguous 1..max; each maps to exactly one `unit_label`.
- Fold rows (`fold_into_parent` set) are **absent** from the CSV (allowed, not flagged).
- Every slug in the CSV resolves to an existing `.md` file.

---

## 7. `build_slice.py` integration (the consumer)

After the CSV exists, wire it in — no UI change in this step, just bake the data:

1. Read `spine_units.csv`; build `arc → units → ordered nodes`.
2. Stamp each node with `spine: {arc_index, arc_label, unit_index, unit_label, order,
   global_order}` where `global_order` is the node's absolute rank across the whole
   spine (the sequence the Path's "next →" and progressive furigana read against).
3. **JLPT milestone markers:** for each level N5..N1, compute the `global_order` at which
   the **essential/common** members at or below that level are exhausted (the max
   `global_order` among nodes with `freq ∈ {essential, common}` and `jlpt <= level`).
   Uncommon/rare N4 forms remain in their honest late extension/appendix homes; they
   must not push an "≈ N4 complete" marker to the end of the path. Emit as
   `slice.jlpt_milestones` with `scope: "essential-common"`.
4. Emit `slice.spine` (the arc/unit tree) alongside the existing `foundations`,
   `branch`, `anchors`, `goals` keys — additive; don't remove the old keys yet (the
   current hub still consumes them until the Door surfaces replace it).
5. Keep the arc→unit-range table as a small constant at the top of `build_slice.py`.

Validate: `python3 scripts/build_slice.py` succeeds, then
`python3 scripts/qa_grammar_nodes.py ...` (existing catalog QA) still PASSes.

---

## 8. Downstream constraints (why the spine data shape matters)

These consume the spine; the ordering must support them. Design-of-record in
`DESIGN_HANDOFF.md` / `RESTRUCTURE.md`:

- **The Path surface** renders arc → unit → node in `order`, with per-unit/per-arc
  progress and the JLPT milestone lines. Needs `global_order` + the arc/unit tree.
- **Progressive furigana / romaji cutoff (the "dictionary-book" model).** The owner's
  target display behavior: a beginner mode shows romaji; the advanced mode gives a kanji
  furigana **the first time it appears in reading order, then not again**. "First time"
  is defined **only by the spine's `global_order`** — walk the spine accumulating a set
  of introduced kanji; a node shows ruby only on kanji not yet seen. This is a v2 render
  layer, but it is *impossible without the spine's global order*, so `global_order` must
  be stable and complete. (v1 is just a display toggle: romaji / furigana / kanji-bare —
  romaji is free, a Hepburn transliteration of the kana `reading`; no content authoring.)
- **Lenses are overlays, orthogonal to arc placement.** `keigo` and `read-novels` are
  highlight-over-the-spine node-sets, **not** separate spine sections. Place each keigo
  or literary node at the position it's actually *learned* (teineigo/ます in Foundations;
  sonkeigo/kenjougo in the Politeness arc; literary points in the Appendix); the lens
  then highlights the full set wherever the nodes landed. Do not pull a lens's members
  out into a dedicated arc *because of the lens* — the arc is about learning order, the
  lens is a view. (A Politeness arc for the honorific/humble block is fine on its own
  pedagogical merit; that's placement, not the lens.)
- **Embed/app parity:** the same baked spine data renders inside the Jengo app later.
  Keep it pure data in `grammar_slice.json`; no UI assumptions in the CSV.

---

## 9. Guardrails — what NOT to do

- **Don't edit node `.md` prose.** Ordering is CSV-only. Reordering is cheap because the
  content never moves.
- **Don't invent prerequisite edges** to justify an order. Frequency orders the forest;
  the DAG is nav chrome (RESTRUCTURE / ON-RAILS §0). No fake edges.
- **Don't wait on enrichment.** Stubs are orderable (§1). Don't reorder "to enrich in
  order" as a blocker — enrichment *follows* the spine, not the reverse.
- **Don't place folds** (§3). Don't split a lens into its own arc (§8).
- **Don't relitigate granularity** (arcs→units, ~48 units, band tiers) — decided in
  RESTRUCTURE. The open thing to confirm is the **arc skeleton** (§4 draft), then place.

---

## 10. Placement frontier

- [x] Reoriented to the 9-arc / 55-unit readiness-first sequence (§4).
- [x] Placed all 1,419 non-fold nodes in `spine_units.csv`; folds remain absent.
- [x] Preserved Foundations and placed every missing form anchor early (§5).
- [x] Added `lint_spine.py`; it checks completeness, folds, file resolution, labels,
  contiguous units, and contiguous within-unit order.
- [x] Baked `spine`, per-node global order, and JLPT milestones into
  `grammar_slice.json` via `build_slice.py`.
- [x] Verified lint, slice build, catalog QA, and the Astro production build.

Future refinements should review a unit's local order or thematic boundary in the CSV,
without weakening the readiness rule.

**Enrichment (PASS.md) and the spine are parallel tracks.** Once the spine exists,
enrichment's worklist reorders to *spine order* (RESTRUCTURE), but neither blocks the
other. This doc owns ordering; PASS.md owns writing.
