# CLAUDE.md

@JENGOLANG.md

## Project
jengolang.com — Astro static site, deploys to Cloudflare Pages automatically on push to main.
The Jengo app (backend) is a separate repo at `/Users/cadenshelley/Documents/JengoApp/`.

## Commands
```bash
npm run dev     # dev server at localhost:4321
npm run build   # production build → dist/
npm run preview # preview production build locally
```

## Grammar skill tree
The grammar skill-tree build lives in this repo under `scripts/` (moved out of JengoApp
2026-06-05 — no cross-repo dependency). **Doing a Pass-2 enrichment pass? Read `PASS.md`
first** (the slim operating cursor: current frontier, per-pass loop, gotchas, subagent
pattern). Durable design: `TREE.md`; vertical-slice IA: `SLICE.md`; dated build log +
Pass-1 handoff archived in `HISTORY.md`. Enrichment rubrics: `CALIBRATION.md` (pass-1
metadata), `CALIBRATION2.md` (pass-2 teaching content).
```bash
python3 scripts/build_slice.py                 # catalog → src/data/grammar_slice.json (the render imports this)
python3 scripts/seed_nodes.py                  # catalog → one tag-layer src/content/.../*.md per node (never overwrites)
python3 scripts/qa_grammar_nodes.py scripts/data/grammar_enriched.csv --source grammar_nodes.csv --merges scripts/data/dedup_decisions.json   # catalog QA, must PASS (--merges credits Step-2 dedup-merged high-risk terms)
python3 scripts/list_stubs.py --freq common    # Pass-2 long-tail worklist: un-enriched stubs (noindex:true), prioritized by freq+JLPT; excludes foldInto folds (--include-folds to see them). The resume state for Pass-2 (see PASS.md). Essential band is drained → next band is `common`.
python3 scripts/lint_batch.py <slug…>          # pre-build lint over a batch: furigana brace balance, dangling contrast/prereq slugs, sense-ref↔senses[].label (run before `npm run build`)
```
- Catalog: `scripts/data/grammar_enriched.csv` (the seed/tag layer, 1,458 nodes post-dedup).
- Node pages: `src/content/japanese/grammar/*.md` (Astro Content Collection, schema in `src/content.config.ts`). All 1,458 materialized (tag layer); teaching layer is Pass-2 (`CALIBRATION2.md`).

## Rules
- No emojis. SVG icons only.
- Light mode only (Jengo app has no dark mode yet).
- Mobile-first.
- No stock photos. Screenshots of the actual Jengo app UI do the visual work.
- No comments in code unless the why is non-obvious.
- Impeccable is installed globally — run /impeccable teach before building any page.
