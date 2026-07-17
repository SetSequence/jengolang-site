# PASS — Pass-2 long-tail operating cursor

The **slim "what now" doc.** Read this + `CALIBRATION2.md` (the frozen judgment rubric)
before enriching. Everything here is meant to **evolve after each pass** — update the
§1 Frontier numbers, fold new gotchas into §4, append the batch narrative to
`HISTORY.md`. Durable design lives in `TREE.md`; it is not needed to run a pass.

---

## 1. Frontier (update this every pass)

Keep this section SLIM — current count, position, next work, open decisions. Full batch
narratives are **append-only in `HISTORY.md`** ("PASS.md frontier ledger" section; the
batch 6–119 ledger was archived there 2026-07-02). After a pass: update the numbers
here, write the batch narrative in HISTORY.md.

- **Indexed: 1202 / 1,462** (through batch 120, the unit-39 spine-order pilot; truth =
  working-tree grep `noindex: false`). `list_stubs.py` *is* the resume state — there is no
  cursor file; a node is done iff `noindex:false`. `--enriched` lists finished nodes;
  `foldInto` folds are excluded by default (`--include-folds` to see them).
- **Position:** Foundations 72/72 (+い/な-adjective unit, Arc-1 U4, 2026-07-15) ·
  read-novels 22/22 · **essential band drained** ·
  **common band drained (batch 72)** — any "common stubs" still surfacing in the
  worklist are resolved noindex redirect-hubs by design; skip them. Currently mining
  the **uncommon band**: `python3 scripts/list_stubs.py --freq uncommon` (then `rare`).
- **Worklist order = spine unit order.** `scripts/data/spine_units.csv` landed
  2026-07-10 (SPINE.md §10 — all 1,419 non-fold nodes placed, 9 arcs / 56 units), so
  spine order is now the Pass-2 worklist: enrich unit by unit, `order` within a unit.
  The remaining non-fold stubs all sit in **units 39–56** (Extension → Advanced
  comprehension → Appendix): ~35 across units 39–45, ~20 across 47–52, ~99 in the
  Appendix (53–56). Units *are* the thematic clusters now — no more ad-hoc grouping.
  `list_stubs.py` is not spine-aware; join its output against `spine_units.csv`
  (or add a `--spine` flag) to get the unit-ordered worklist.
- **Open catalog decisions:** near-dup fold pairs `o-suru`(N3)/`o-suru-2`(N4) and
  `yaru`/`yaru-3`/`te-yaru` still need a catalog-level fold decision. `mata-mo` canonical
  in `grammar_enriched.csv` is still the wrong frame notation `又〜も` (node fixed to `又も`
  batch 120; the CSV is hook-guarded as generated — fix pipeline-side). `koto-nano` and
  `no-wa-no-koto-da` remain low-conf fold/dup candidates (enriched conservatively b120,
  held noindex).
- **Throughput (user directives 2026-06-15 / 2026-06-19):** roll multiple thematic
  clusters back-to-back per turn; one consolidated build + one checkpoint
  (PASS + HISTORY) per cluster-group. Context ceiling ≈ **20% per turn** (~60–70 nodes,
  5–6 clusters) — checking it is MY responsibility, at each build+checkpoint boundary,
  not a hook's. Pattern: cluster(s) → build → checkpoint → **yield the turn**; re-check
  the ceiling on the next turn before continuing. A yield between groups is the norm.

## 2. The loop (per batch)

1. **Pick the next spine unit (or 2–3 small adjacent ones) with unfilled stubs.**
   Spine unit order is the worklist (see §1); work a unit's stubs in its `order`. The
   unit is the thematic cluster — its members are the natural `contrasts` targets, and
   that cross-link density is the GEO win.
2. **Get the cluster brief (subagent — see §3).** This hands you the existing sibling
   slugs, valid contrast targets, and homograph warnings up front, so your context stays
   on the judgment work instead of grep round-trips.
3. **Edit each `src/content/japanese/grammar/<slug>.md`.** Preserve the seeded tag-layer
   frontmatter; append the teaching layer per `CALIBRATION2.md`. **Read-before-Write is
   required by the harness** — the Read tool, not `cat` (Write fails otherwise).
4. **Verify every `contrasts`/`prereqs` slug exists** before referencing it (a dangling
   slug fails the build). The brief from §3 lists valid targets; still spot-check.
5. **Flip `noindex:false`** only when the node clears the non-thin gate (CALIBRATION2 §5:
   key sentence per sense + examples threshold + equivalents). Shaky/low-confidence nodes
   fill conservatively and **stay `noindex`**. `foldInto` folds stay `noindex` by design.
6. **Validate:** `python3 scripts/lint_batch.py <slug…>` over the batch (furigana brace
   balance, dangling contrast/prereq slugs, `sense:` ref ↔ `senses[].label`,
   foreign-script scan), then `npm run build` (validates all ~1,458 — schema + dangling
   slugs). Spot-read ~10% against CALIBRATION2 §1–§4.
7. **Record:** update §1 Frontier here (numbers/position only); append the batch
   narrative to `HISTORY.md` under "PASS.md frontier ledger".

## 3. Cluster-prep subagent pattern

**Enrichment stays single-threaded** (cross-linking + calibration consistency need one
hand on the pen). Parallelize the *read-heavy prep and the verify*, not the writing.

- **Before a batch — spawn an `Explore` agent** with the cluster's stub slugs. It returns a
  compact **brief**, no file dumps: for each stub → its seeded frontmatter (canonical,
  reading, freq, jlpt, family, prereqs, confidence); the **already-enriched sibling nodes**
  in the same `family`/theme with their slugs + titles (= valid `contrasts` targets); and
  **homograph warnings** (slugs whose romaji collides — see §4). Prompt it to confirm each
  candidate target file exists. Cost: replaces ~10 grep/read round-trips with one summary.
- **After a batch — spawn an `Explore` (or general) agent** to QA the finished files
  against CALIBRATION2 §1–§4: the furigana/gate/over-fill/under-fill scans (§7) + a
  §1–§4 spot-read. It reports issues; you fix. A second set of eyes, not a parallel pen.
- **Writer-subagent pattern (piloted batch 120, unit 39 — validated for the tail):** an
  Opus writer subagent drafts a whole unit, orchestrated per unit: Explore prep brief →
  writer (gets the brief + CALIBRATION2 + PASS §4 gotchas + 2–3 enriched same-unit
  exemplars, self-lints, conservative-noindex mandate) → orchestrator runs lint + build →
  `content-reviewer` agent audits vs CALIBRATION2 → orchestrator adjudicates findings and
  fixes. Pilot yield: 6 nodes, writer made 3 real slips (a §5 contrasts-on-low-conf
  violation, a notation error, an example contradicting its own nuance) — all caught by
  the gate; main context stayed at briefs + verdicts. **One writer per unit, ≤2 units in
  flight.** The old caution stands for dense essential/common material: this pattern is
  cleared for the uncommon/rare tail (units 39–56), where contrasts are sparse and holds
  are cheap. Orchestrator must re-adjudicate reviewer findings against the seed diff —
  the reviewer can't tell seeded content from writer-invented content.

## 4. Gotchas (the traps that cost real time — fold new ones in here)

- **Homograph slug traps** (grep first if unsure): `ga-2` = subject が · `ga-3` = "but" が ·
  `to-2` = "and/with" と · `to-quotative` = quote と · `to-conditional` = と "natural result" ·
  `souda` = hearsay そうだ · `youda`/`mitai`/`mitaida`/`rashii` = seeming · `reru` =
  potential/passive godan · `rareru` = honorific/spontaneous · `rareru-2` = passive られる ·
  `te-mo-ii` (not `temo-ii`) · `kurai`/`gurai` are a fold pair · `ni`/`ni-2`/`ni-3`/`ni-5` =
  umbrella / destination+location+time / indirect-object / time-point · `o`/`o-2` = を
  object / を path · `ka`/`ka-2` = question+or+embedded / "or" · `iku`/`kuru-2` = ていく/てくる
  aspect (the bare verbs are `kuru`, and 行く has no standalone node).
- **Slug macron convention = `ou`/`uu`** (ō→ou, ū→uu): deshou, darou, youni.
- **`foldInto` = folded form**, not its own indexed page. Document the folded form as a
  `note`/`variants` entry on the **parent**, keep the child a noindex redirect-hub
  (equiv + key sentence + contrast→parent). Don't index it (duplicate-content tax).
- **Furigana** is `漢字{かんじ}` markup → build-time `<ruby>`. Every kanji needs a reading;
  verify the reading. Lint balance before building.
- **Scalar vs array schema fields** (`src/content.config.ts`): `usageSetting` and `nuance`
  are **plain strings** (`usageSetting: "…"`), NOT YAML lists. `equivalents`/`examples`/
  `restrictions`/`notes`/`contrasts`/`formation`/`senses` are arrays. Writing a list under
  `usageSetting`/`nuance` fails the build with "Expected string, received object."
- **`variants[]` item shape** = `form:` (required) + optional `note:`/`reading:`/`register:`
  — NOT `text:`. `restrictions`/`notes` items use `text:`; `variants` does not. A prose aside
  with no alternate surface form belongs in `notes:`, not `variants:`. (Caught in batch 6.)
  **`variants[].register` is an ARRAY** (`["polite-spoken"]`), not a scalar — it mirrors the
  top-level `register` set. A scalar dies at build with "Expected array, received string"
  (caught in batch 101, tsuite-wa).
- **Seed already has `confidence:` — bump it by EDITING that line, never adding a second.**
  A duplicate `confidence:` key (e.g. seed `med` + an appended `high`) is silent until
  `npm run build` dies with "duplicated mapping key". Same applies to any seed key you adjust
  (`noindex`, `register`). Bit this in b70 (nanraka-no) and b71 (buri).
- **Foreign-script intrusions are real.** Hangul slipped into kana examples twice
  (약속→約束, 체조子→調子, batch 13) and Cyrillic into prose once (благодаря, batch 34) —
  the build passes silently. `lint_batch.py` now scans for `[가-힣ᄀ-ᇿ㄰-㆏Ѐ-ӿ]`
  (added 2026-07-02), so running the lint covers this.
- **No stray non-furigana CJK in English strings.** A kanji accidentally typed inside an
  `equivalents`/`distinction`/`note` English sentence (e.g. `specific評価criterion`) passes lint
  and build silently — only a read catches it. Watch the IME when writing English mid-field.
- **No nested double-quotes inside a double-quoted scalar.** `nuance`/`usageSetting`/
  `distinction` are double-quoted YAML strings — an inner `"…"` (e.g. quoting an English nickname
  or title) ends the string early and dies at build with a js-yaml `readBlockMapping` error
  pointing at the line:col. Use single quotes or none for inner quoting. (Caught in b89, tokoro-kara.)
- **Don't manufacture slots.** CALIBRATION2 §1–§2: presence is *earned*. A `restriction`
  that restates the rule, or a `contrast` no learner confuses, is padding — omit it.
  Equally, a real prohibition or confusable sibling is **mandatory**, not optional.

## 5. Validation snippet (pre-build lint)

`python3 scripts/lint_batch.py <slug…>` — the promoted stdlib pass, catches most issues
in seconds before `npm run build`: brace balance (`jp` count of `{` == `}`, no `{}`),
each `slug:` in `contrasts` exists as a file, each `prereqs` entry exists (or is
`*`-anchored), each `sense:` ref matches a `senses[].label`, and foreign-script
intrusions (Hangul/Cyrillic). It does NOT catch stray CJK inside English strings
(e.g. `specific評価criterion`) — only a spot-read does.
