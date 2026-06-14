# SLICE — Grammar Skill-Tree Vertical Slice (validation)

The deliverable of **TREE.md Step 4b item 3**: one Foundations line + one goal
branch ("Read novels" / literary), fully tagged, built to **validate the IA
model before the tree UI**. This doc owns the slice's *findings*; `TREE.md` owns
the wider IA; `CALIBRATION.md` owns the enrichment rubric.

Status: **DONE (2026-06-03).** Generator + manifest + static render built and
validated (PASS). The IA model holds, with three concrete amendments below.

---

## Artifacts

All grammar skill-tree scripts + the catalog now live **in this repo** under
`scripts/` (moved out of JengoApp 2026-06-05 — no more cross-repo dependency).

| Artifact | Path | What it is |
|---|---|---|
| Generator | `scripts/build_slice.py` | Curates the slice from the catalog, resolves the form-anchors, computes tiers, validates, emits the manifest. Pure stdlib, re-runnable. |
| Catalog | `scripts/data/grammar_enriched.csv` | The enriched node catalog (1,527 rows) — the build input. |
| Manifest | `src/data/grammar_slice.json` | The slice data (anchors + Foundations + branch + validation + findings). Single canonical output, imported by the render. |
| Static render | `src/pages/learn/japanese/grammar/index.astro` | The crawlable layered node-link index (TREE #8). Light-mode, mobile-first, Jengo palette + an indigo accent for the literary line. |

Re-run (from repo root): `python3 scripts/build_slice.py` (rewrites the manifest).

## What the slice contains

- **8 form-anchors** (tier-0): `*te-form`, `*masu-stem`, `*ta-form`, `*nai-form`,
  `*ba-conditional`, `*volitional-form`, `*causative-form`, `*counter` —
  materialized as real nodes (see Finding 2).
- **Foundations line — 60 nodes, 9 curated stages**: copula & the は～だ frame →
  core case/binding particles → verb bases & politeness → て-form uses & aspect →
  benefactive giving/receiving → desire & basic modality → the four conditionals →
  clause connectives & temporal frames → nominalizers & comparison.
- **Read-novels branch — 22-node curated route, 4 stages**, selected by the filter
  `register ⊇ {literary}` (145 members total): written-style copula & classical
  negatives → classical auxiliaries (likeness/obligation/prohibition) → literary
  particles of restriction/emphasis → literary connectives & temporal "as soon as".

## Validation result — PASS

| Check | Result |
|---|---|
| Curated slugs resolve to catalog | **82/82** (0 typos — the hard-error gate works) |
| Dangling prereqs | **0** |
| Foundations-first ordering (no branch node depends on a later one) | **0 violations** |
| Prereqs pointing outside the slice | 11 (expected — they resolve in the full tree) |
| Same-surface clusters needing dedup/sense review | 12 (Finding 3) |

---

## Findings (the point of the exercise)

### 1. Prereq-depth can't lay out the spine — **stage is the axis**
`max prereq tier = 2` across the *entire* slice; 42 of 60 Foundations nodes are
tier-0. The enriched `candidate_prereqs` overwhelmingly point at `*`-form anchors,
not at each other, so the DAG is too flat to order the line by depth.

**Amendment to TREE #6 ("Position = prereq depth"):** depth alone collapses. The
**curated `stage`** (TREE #9, the Foundations line) is the real vertical axis;
prereq depth stays a *secondary* signal — within-stage nuance and the source of
the faint mesh edges between nodes. The manifest carries an explicit `stage`
`{index, label, line}` on every node for exactly this reason.

> Optional future work: a denser inter-node prereq pass would make depth
> meaningful again, but it is **not required** — the curated line is the product.

### 2. The `*`-form anchors are load-bearing and must become real nodes — **DONE (Build step 1, 2026-06-05)**
`*te-form`, `*masu-stem`, etc. are referenced as prereqs **225 times** across the
catalog but were never catalog rows. The slice materialized 8 of them as tier-0
"form" nodes — without them the Foundations line has dangling roots.

**Resolved:** all 8 are now **real catalog rows** (`scripts/data/grammar_enriched.csv`
= 1,527, `family=form`, added via `scripts/promote_form_anchors.py`) with **real
teaching pages** (conjugation explainers) in the new Astro Content Collection
(`src/content/japanese/grammar/{te-form,masu-stem,ta-form,nai-form,ba-conditional,
volitional-form,causative-form,counter}.md`, schema in `src/content.config.ts`).
Every `*<anchor>` prereq was flipped to its bare slug; `build_slice.py` now resolves
the anchors straight from the catalog. QA + build PASS.

### 3. Same-surface dedup is a real, unautomatable pre-ship task — **DONE (Build step 2, 2026-06-11)**
12 surfaces in the slice carry multiple catalog slugs. These mix **true OCR dups**
(て / `te-2`, ので / `na-node`) with **genuine sense-splits** (が subject `ga-2` /
が "but" `ga-3`; を object/path/separation `o`/`o-2`/`o-3`; に dest/IO `ni-2`/`ni-3`).
A meaning-prefix heuristic mis-sorts both directions, so this is **not mechanically
separable** — it needs a human same-surface review pass before the full tree ships.

**Resolved:** all **78 same-surface clusters across the full catalog (175 nodes)**
were adjudicated by hand (not just the slice's 12). Decision per node = keep-distinct
(genuine sense, TREE #3) vs merge (OCR/cross-row dup). **69 dups merged → catalog
1,527 → 1,458 nodes**; the remaining cluster members are kept as distinct senses
(を×4, に×5, られる×3, の×3, etc.). Decisions + provenance frozen in
`scripts/data/dedup_decisions.json` (`merges` / `keep_distinct` / `merged_terms`);
applied by `scripts/apply_dedup.py` (drops merged rows, repoints every prereq /
fold_into_parent ref to the survivor, safety-gates against breaking the curated path);
audit log `scripts/data/dedup_applied.md`. **Slice-author choices honored** where the
slice had already picked a canonical (e.g. benefactive `ageru-2`/`morau` over the
`te-`prefixed dups; `ga-3` kept since the Foundations path uses it). QA-coverage was
taught about merges via a new `--merges` flag (a merged high-risk term counts as
covered when its survivor exists). QA PASS (0 hard), `build_slice` PASS (now 1,458
nodes, same-surface clusters in slice 12→8), `npm run build` PASS.

### 4. The subway-line model works as designed
A pure tag query (`register ⊇ {literary}`) cleanly selects a 145-node line; a
22-node curated route through it is coherent, attaches to Foundations with **zero
ordering violations**, and the "+123 dimmed-but-present" pattern (TREE #5 — never
hidden) renders naturally. **No new data model was needed** — the line is just a
filter preset over the existing tag schema, confirming TREE #10. The register
**set** tag (vs a scalar) is what made this branch selectable; it earns its
complexity.

---

## Verdict for the tree UI

The enriched catalog + tag schema **support the IA**. Before the interactive tree:
1. ~~Promote the form-anchors to real nodes (Finding 2).~~ **DONE (Build step 1, 2026-06-05).**
2. ~~Run the same-surface dedup/sense review (Finding 3).~~ **DONE (Build step 2, 2026-06-11).**
3. Treat `stage` as the layout axis and prereq edges as the faint mesh (Finding 1).
4. Decide the still-open **per-node content schema** (what a node page shows) and
   **render tech** (Astro island: canvas/D3/Sigma/Cytoscape) — see TREE "Still open".
