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
2026-06-05 — no cross-repo dependency). Design/status: `TREE.md`, `SLICE.md`; enrichment
rubrics: `CALIBRATION.md` (pass-1 metadata), `CALIBRATION2.md` (pass-2 teaching content).
```bash
python3 scripts/build_slice.py                 # catalog → src/data/grammar_slice.json (the render imports this)
python3 scripts/seed_nodes.py                  # catalog → one tag-layer src/content/.../*.md per node (never overwrites)
python3 scripts/qa_grammar_nodes.py scripts/data/grammar_enriched.csv --source grammar_nodes.csv --merges scripts/data/dedup_decisions.json   # catalog QA, must PASS (--merges credits Step-2 dedup-merged high-risk terms)
python3 scripts/list_stubs.py --freq essential # Pass-2 long-tail worklist: un-enriched stubs (noindex:true), prioritized by freq+JLPT. The resume state for Pass-2 (see TREE.md "Resuming Pass-2 long-tail").
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
