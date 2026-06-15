# PASS — Pass-2 long-tail operating cursor

The **slim "what now" doc.** Read this + `CALIBRATION2.md` (the frozen judgment rubric)
before enriching. Everything here is meant to **evolve after each pass** — update the
Frontier line, fold new gotchas into §4, append a one-liner to `HISTORY.md`. Durable
design lives in `TREE.md`; it is not needed to run a pass.

---

## 1. Frontier (update this every pass)

- **Indexed: 192 nodes.** Done: Foundations 60/60 · Read-novels branch 22/22 · essential
  band **fully drained** · **common batch 1** (interrogatives/indefinites/degree, 10 indexed).
- **Next batch = `--freq common` batch 2.** Run `python3 scripts/list_stubs.py --freq
  common`. **727** common stubs remain (then `uncommon`, then `rare`).
- There is **no cursor file** — `list_stubs.py` *is* the resume state (a node is done iff
  `noindex:false`). `--enriched` lists finished nodes. `foldInto` nodes are excluded by
  default (folded forms aren't pending work; `--include-folds` to see them).

## 2. The loop (per batch)

1. **Pick a thematic cluster of ~15–25 stubs.** Fill order is LOCKED: highest `freq` first,
   low JLPT first within a band (SEO weight). Group by *theme* so the `contrasts` slot
   cross-links densely — that density is the GEO win, and it's why we cluster rather than
   go alphabetically.
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
6. **Validate:** pre-build stdlib lint over the batch (furigana brace balance `{`==`}` and
   no empty `{}`, dangling contrast/prereq slugs, every `sense:` ref matches a
   `senses[].label`), then `npm run build` (validates all ~1,458 — schema + dangling
   slugs). Spot-read ~10% against CALIBRATION2 §1–§4.
7. **Record:** update §1 Frontier here; append a one-line entry to `HISTORY.md`.

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
- **Not recommended (yet):** subagents drafting whole clusters. The contrast web fragments
  across isolated agents and calibration drifts; a mandatory single-threaded review+merge
  gate eats most of the supposed throughput win. Revisit only if prep+verify offload isn't
  enough and the review gate is shown to hold quality.

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
- **Don't manufacture slots.** CALIBRATION2 §1–§2: presence is *earned*. A `restriction`
  that restates the rule, or a `contrast` no learner confuses, is padding — omit it.
  Equally, a real prohibition or confusable sibling is **mandatory**, not optional.

## 5. Validation snippet (pre-build lint)

A stdlib-only pass over the batch catches most issues in seconds before `npm run build`:
brace balance (`jp` count of `{` == `}`, no `{}`), each `slug:` in `contrasts` exists as a
file, each `prereqs` entry exists (or is `*`-anchored), each `sense:` ref matches a
`senses[].label`. (See the inline scripts used in recent batches; promote to
`scripts/lint_batch.py` if it recurs.)
