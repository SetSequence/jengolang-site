---
name: enrich-batch
description: Run one Pass-2 grammar-enrichment cluster — pick the next stubs, enrich per CALIBRATION2.md, lint, build, and checkpoint. Use when the user wants to enrich grammar nodes, run a Pass-2 batch, or continue the enrichment loop.
disable-model-invocation: true
---

# Enrich a Pass-2 grammar batch

Run **one** thematic enrichment cluster end to end. This is the deliberate,
single-batch entry point for the loop that `PASS.md` describes (the
`context_gate.py` Stop hook drives the same loop automatically until context
fills; this skill lets you fire one batch on demand).

Read `PASS.md` first — it is the slim operating cursor (current frontier,
per-pass loop, gotchas, subagent pattern). Then:

1. **Pick the cluster.** Run:
   ```bash
   python3 scripts/list_stubs.py --freq common
   ```
   Take the next thematic cluster — highest frequency first, lower JLPT first —
   grouped so contrasting/related points cross-link densely. The Essential band
   is drained; `common` is the active band.

2. **Read before writing.** Open each stub file plus its already-enriched sibling
   anchors (so cross-links and contrasts stay consistent). Enrich each node per
   the teaching rubric in `CALIBRATION2.md` (plain-English explanation, formation,
   5–10 furigana examples, exceptions, see-also, CTA). Read-before-Write every file.

3. **Validate the batch.** Run, over exactly the slugs you touched:
   ```bash
   python3 scripts/lint_batch.py <slug…>     # brace balance, dangling slugs, sense-refs
   ```
   Then the Hangul scan (no stray Korean characters in Japanese content), then:
   ```bash
   npm run build
   ```
   The `lint_grammar_node.py` PostToolUse hook lints each file as you save it, but
   still run `lint_batch.py` over the whole batch and the full build before
   checkpointing.

4. **Checkpoint.** Update the Frontier count in `PASS.md` and append a one-line
   entry to `HISTORY.md` describing the batch (count + theme).

Stop after one batch and report what was enriched. If `list_stubs.py` returns no
remaining `common` stubs, say the band is drained instead of inventing work.
