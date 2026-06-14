# GRAMMAR — Grammar Index Ingestion & Catalog

Working doc + cross-session handoff for building a structured catalog of Japanese
grammar points from the *Dictionary of Japanese Grammar* index. Kept lean: status,
systems, rules, known problems, next steps — not an action log.

Related: `JENGOLANG.md` (same repo — content plan + full pipeline mechanics). The
ingestion **scripts live in the JengoApp repo** (`scripts/`, output in
`scripts/ocr_output/`); the vocab analog is `JengoApp/docs/VOCABLISTS.md`. This
doc owns the **ingestion** side and points at JENGOLANG.md for deep detail.

## Goal & motivation

Produce a clean, structured list of every grammar point in the DBJG/DIJG/DAJG
series so we can write grammar-guide content (jengolang.com), ordered by
frequency/usefulness with JLPT level as metadata. The source is the romaji
**"Japanese Index"** of the *Dictionary of Advanced Japanese Grammar* (DAJG),
which indexes all three volumes.

Why a bespoke pipeline (not the vocab one): the index is **romaji**, so there is
**no JMdict to validate against** — the entire validate/fix/reconcile-by-dictionary
half of the vocab flow does not apply. QA here is purely structural.

## Current status  (2026-05-30)

- Pipeline built and run. Output of record: **`scripts/ocr_output/grammar_reconciled.csv`**.
- Scans ingested: **v1** (standalone index, 21pg, clean), **v2** (full DAJG book
  pp.414-424, landscape 2-up spreads, low quality), **v3** (clean standalone
  index, 21pg). v1 is the trusted primary.
- Reconciled v1 + v3 + v2 → **blank refs 238 → 62**, QA-flagged **5% (89/1502)**.
- Remaining manual work: 62 blank refs, 23 ambiguous (`grammar_fill_review.csv`),
  19 low-confidence v2 A-page fills (filter `ref_source=v2, volume=A`).
- Not yet started: ordering/structuring the catalog into content (see JENGOLANG.md).

## System (scripts in the JengoApp repo, `scripts/`)

```
ocr_grammar_pdf.py    [v1|v2|v3]            → {stem}_raw.json   (Google Vision DOCUMENT_TEXT_DETECTION, 3x render)
clean_grammar_ocr.py  --stem {stem}         → {stem}_clean.csv  (bbox parser, auto column-count)
reconcile_grammar.py  --secondary A B …     → grammar_reconciled.csv (+ fill_review, diff_only_in_*)
qa_grammar.py         --stem {stem}         → {stem}_qa.csv     (structural flags)
```

Scan config (PDF path + page range) lives in `ocr_grammar_pdf.py:SCANS`. Override
with `--pdf` / `--pages START END`. OCR refuses to overwrite an existing
`{stem}_raw.json` (delete to re-run). 1 Vision call per page.

**Output schema** (`*_clean.csv`): `term, gloss, volume, page, type, xref_target,
section, src_page`. After reconcile add `ref_source` (v1 / v3 / v2 / blank).

- `volume`: **A** = entry is in *this* book (DAJG), with a `page`; **B** = DBJG,
  **I** = DIJG (no page). Numeric ref → A; letter ref → B/I. `HOME_VOLUME` constant.
- `type`: `main` | `sub` (leading `–`) | `xref` (`→`, target in `xref_target`).
- `gloss`: captures `<see-also>`, `"english"`, and `[grammar label]`.

## Known problems

- **Faint single-letter B/I refs are dropped by OCR** — the lone letter sits past
  the leader dots at the far right. The dominant `missing_ref` cause. Different
  scans drop *different* letters, which is the whole reason reconciliation works.
  62 survive all three scans (genuinely manual).
- **Low-quality scans invent page-A numbers** — v2 mis-read many B/I cross-volume
  refs as `A <page>` and spuriously page-tagged ~1100 rows. Mitigated by trusting
  the cleanest scan first and segregating fills by `ref_source`.
- **Superscript homographs** (`ne²`) OCR inconsistently as `2`/`'`; a leading
  displaced digit is stripped from the term.
- **Dropped closing `>`/`"`** merges ≤2 neighbouring entries (capped); flagged
  `merged_suspect` / `unbalanced`.
- v2's page 424 right half is the book's **References** — prose that yields junk
  rows (filtered by header keywords; residue lands in `diff_only_in_v2`, ignored).

## Ingestion & handling rules (learned)

1. **No dictionary validation.** QA only flags structure (`missing_ref`,
   `unbalanced`, `merged_suspect`, `empty/short_term`, `bad_page/volume`,
   `xref_no_target`, `duplicate`). Never auto-"correct" a romaji term.
2. **Reconcile is additive, never destructive.** The primary scan is always
   trusted; secondaries only fill rows with no reference. A v1 ref is never
   overwritten.
3. **Order secondaries best-scan-first.** `--secondary grammar_v3 grammar_v2`:
   the clean scan wins, the noisy one only fills what the clean one missed (and
   thereby corrects the noisy scan's bad A-page guesses).
4. **Fill only on confidence.** Accept a fill when the term maps to a single
   plausible secondary ref, or a clear gloss match disambiguates senses; else →
   `fill_review.csv`. "Plausible" = B/I, or A with page 1..900.
5. **`ref_source` is the trust signal.** v1/v3 = reliable; v2 A-page = verify
   against the book before trusting.
6. **Column layout is auto-detected by aspect** — portrait = one book page (2
   columns); landscape = a 2-page spread (4 columns on even width-fractions, book
   gutter dead-centre). Override with `--columns`.
7. **Be dash-tolerant.** Poor scans render refs as `B -` and leader dots as
   dashes; reference/leader parsing strips trailing `.-–—` junk.
8. **Cap wrap-merges at 2 lines.** Prevents a single dropped delimiter from
   chaining a column-wide runaway merge.
9. **A new scan = a new `grammar_vN`.** Add it to `SCANS`, OCR, clean, then
   `reconcile_grammar.py --secondary grammar_vN grammar_v3 grammar_v2`. Reusable.

## Enrichment: catalog → skill-tree nodes  (current stage)

The reconciled catalog (romaji term + gloss + ref) is being turned into structured
**grammar nodes** for the skill tree. The product/IA design lives in **`TREE.md`**;
this section owns the data mechanics. Scripts in `JengoApp/scripts/`.

```
prep_grammar_nodes.py    grammar_reconciled.csv  →  grammar_nodes.csv   (DONE)
enrich_grammar_nodes.py  grammar_nodes.csv       →  grammar_enriched.csv (+ _review.csv)
```

- **`prep_grammar_nodes.py`** collapses 1,469 non-xref rows into **1,090 candidate
  nodes** (groups identical terms; keeps semantically-distinct terms separate per
  TREE.md #3), folds 33 xrefs as aliases, and **auto-flags risk**: `collision` (64 —
  a romaji string with >1 sense, the false-confidence trap), `garble` (20 — OCR-fused
  rows), `missing_only` (53 — not blockers; AI supplies the meaning). ~1,006 are clean.
- **Node record schema** (the enrichment target — see `enrich_grammar_nodes.py`
  `SCHEMA`/`OUT_FIELDS`): `slug, canonical, reading, meaning, senses[], register{set},
  keigo, freq, jlpt, family, candidate_prereqs, fold_into_parent, confidence,
  review_reason`. `slug` = stable kebab node id / URL; `candidate_prereqs` are
  prerequisite-node slugs (`*`-prefixed for non-catalog foundations). See TREE.md #16.
- **Collision guard** (TREE.md #14): enumerate every sense of a romaji term; disambiguate
  by gloss / volume (B/I/A) / superscript; flag if ambiguous even with a default guess.
- **Execution:** enrichment is run **by Claude in-session (this chat), not the API** —
  the `.env` Anthropic key has no credits, and an in-session hand-pass (full review,
  asks on ambiguity) is the chosen path. `enrich_grammar_nodes.py` (Batch API + caching
  + structured outputs) is built and validated up to the billing wall, **parked as a
  fallback** if credits are added. Next session: hand-enrich all 1,090, high-risk first.

## Next steps

1. **Enrich all 1,090 nodes** in-session (high-risk 84 first; see TREE.md "Next session").
2. External-source reconciliation (TREE.md #15) to catch sense-collisions + fill gaps.
3. Manual-fill the 62 `missing_ref` blanks + review 23 ambiguous / 19 v2 A-page fills
   (only those that block a node; most don't).
4. Build one vertical tree slice (Foundations line + a branch) to validate the model.
