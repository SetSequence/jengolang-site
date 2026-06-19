# PASS — Pass-2 long-tail operating cursor

The **slim "what now" doc.** Read this + `CALIBRATION2.md` (the frozen judgment rubric)
before enriching. Everything here is meant to **evolve after each pass** — update the
Frontier line, fold new gotchas into §4, append a one-liner to `HISTORY.md`. Durable
design lives in `TREE.md`; it is not needed to run a pass.

---

## 1. Frontier (update this every pass)

- **Indexed: 406 nodes.** Done: Foundations 60/60 · Read-novels branch 22/22 · essential
  band **fully drained** · common batches 1–5 (adverbial family, largely drained) · **batch
  6** (appearance/evidentiality modality, 8 + 1 redirect) · **batch 7** (necessity/obligation,
  9) · **batch 8** (はず/わけ/べき expectation-logic, 13) · **batch 9** (こと decision/outcome/
  experience, 11) · **batch 10** (keigo verbs + こそあど 連体詞, 18: いらっしゃる/なさる・いたす・
  さしあげる・くださる・お〜になる↔お〜する・お〜ください・ございます/でございます・なさい; こそあど
  こういう↔そういう↔このような・どのような・こうした↔こういった) · **batch 11** (benefactive
  て-grid + connectives, 14): ていただく↔てくださる・てくれない↔ていただけませんか・てもらいたい↔
  てほしい・てやる(2-sense); それで/それでは/それでも/それなら; だけど→けれど→だが · **batch 12**
  (aspect/phase + causative/passive/potential/perception, 29 = 26 indexed + 3 noindex redirects):
  始める↔出す↔終わる・続ける; ておく↔てある; ているところ↔たところ↔るところだ (ところ trio) ↔たばかり;
  ていく↔てくる (2-sense mirror); ていた; なくなる; ちゃう/ちまう/とく → parents; せる↔させる↔させられる・
  させてください; れる↔られる(passive/potential/honorific 3-way ら-shape); られない; 見える↔見られる↔
  が見られる・聞こえる (perception: natural-sense vs opportunity-potential). · **batch 13** (quotation/
  report + nominalizers, 15): ということ↔ということだ(2-sense)・と聞いた・と言ってもいい; the **reported-belief
  trio** と言われている (general saying) ↔ とされている (established/rule) ↔ と考えられている (reasoned/
  expert) mutually contrasted; って(2-sense quotative/topic); nominalizers の(2-sense pronoun/
  nominalizer)・の-2(sentence-final explanatory)・のこと・のは〜だ cleft・もの(↔こと)・さ(degree)・連用形名詞
  用法 — anchored to enriched という/と/こと/のだ/そうだ/らしい. · **batch 14** (conditionals, 12):
  なかったら (negative たら); the **negative-copula "unless" family** でないと (と-base, 'or-else' warning) ↔
  でなければ (ば-base, neutral) ↔ でなくては (ては-base, 'must be', → でなくてはいけない) ↔ でなかったら (たら-
  base) — each pinned to its conditional base + mutually differentiated; のなら (explanatory なら); できれば
  (set 'if possible', ↔ ばいい); でよければ (humble offer); がなければ (negative ば of ある, 'without', ↔
  でなければ identity-vs-existence); ばいい (suggestion, ↔ たらどう & ば〜のに); ば〜ほど (proportional); ば〜のに
  (counterfactual regret, ↔ のに). Anchored to enriched ば/たら/なら/と-conditional/なければ-obligation/ほど/のに.
  Dense webs: ところ-phase timeline, 五段/一段 causative-passive grid, られる homograph disambiguation,
  見える/見られる confusion, reported-belief saying/rule/reasoning trio, negative-conditional と/ば/ては/たら
  base grid. · **batch 15** (だけ/ばかり limitation + 以外/ほか exclusion, 15 indexed + 5 noindex
  redirects): bakari (2-sense only/nothing-but ↔ approximate-amount, anchor)・dake-da・dake-de↔dake-demo↔
  dake-wa・dake-shika(↔shika)・sore-dake・te-bakari-iru・bakari-de(↔dake-de positive/negative);
  the **"not only but also" canonical pair** だけでなく ↔ ばかりでなく (everyday vs literary, mutually
  contrasted) with 4 numbered near-dups (dake-de-wa-naku-2, bakari-de-wa-naku/-2/-4) collapsed to
  **noindex redirect-hubs** → their canonical; igai (以外)↔hoka(ほか)↔hoka-ni-mo, **以外/意外 same-reading
  trap** igai↔igai-to disambiguated; igai-wa → igai redirect. · **batch 16** (person/address suffixes,
  7): honorific ちゃん↔君↔様 (laddered against enriched san) + plural たち↔ら↔方(sonkeigo, elevates)↔
  ども(humbles/derogates) — politeness-direction grid. Fixed kun's truncated seed title ("for pee"→full).
  **Trap caught (×2, batch 13):** Hangul slipped into kana examples — 약束→約束 (rarenai), 체조子→調子
  (no-2) — both fixed pre-build; a post-batch Hangul scan (가-힣 + Jamo) is now mandatory QA.
  modality する/なる oppositions, keigo & こそあど register ladders, benefactive viewpoint mirrors,
  connective result/concession/condition axes.
- **Next batch = `--freq common`.** Run `python3 scripts/list_stubs.py --freq common`. **516**
  common stubs remain (incl. the 5 batch-15 redirect-hubs below; skip those) (then `uncommon`, then `rare`). Modality + keigo + こそあど + benefactives +
  basic connectives + aspect/causative/passive + quotation/nominalizers + conditionals + だけ/ばかり
  limitation + 以外/ほか exclusion + person/address suffixes largely mined; remaining good families:
  **degree/extent adverbials** (donnani/doushitemo/dou-ka/goto-ni/gimi/darake/buri-ni), the
  **〜化/〜くする/〜にする change-of-state set** (ka-suru/ku-suru/ni-suru), or the **〜がる/〜たがる
  emotion-display pair** (garu/tagaru). **Heads-up:** batch-15's 5 redirect-hubs
  (dake-de-wa-naku-2, bakari-de-wa-naku, bakari-de-wa-naku-2, bakari-de-wa-naku-4, igai-wa) stay
  `noindex:true` by design and will **reappear in the worklist** — they're resolved redirects to a
  canonical, not pending work (same as batch-12's chau/chimau/toku). Skip them. Note: two unresolved
  near-dup stub pairs still need a catalog-level fold decision — `o-suru`(N3)/`o-suru-2`(N4) and
  `yaru`/`yaru-3`/`te-yaru`.
  **Process (user directive 2026-06-15, throughput revised 2026-06-19):** roll multiple clusters
  back-to-back per turn, then ONE consolidated build; checkpoint PASS + HISTORY once per turn, not
  per cluster. **Context can safely run to ~20% (1/5) per turn — that is the target ceiling.**
  Reference point: ~40+ nodes (4 clusters) lands context at only ~13%, so ~20% is roughly 60–70
  nodes / 5–6 clusters in a turn. Don't stop at one ~15-node batch. A consolidated build + checkpoint
  per cluster-group is fine (batch 12 then 13 each got their own build in one turn); the cap is the
  20% context line, not a node count.
  **Watch:** `variants[]` schema is `form:` (+ optional `note:`/`reading:`/`register:`), NOT
  `text:` — using `text:` fails the build (caught batch 6). A pure prose aside with no
  alternate form belongs in `notes:`, not `variants:`.
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
- **Scalar vs array schema fields** (`src/content.config.ts`): `usageSetting` and `nuance`
  are **plain strings** (`usageSetting: "…"`), NOT YAML lists. `equivalents`/`examples`/
  `restrictions`/`notes`/`contrasts`/`formation`/`senses` are arrays. Writing a list under
  `usageSetting`/`nuance` fails the build with "Expected string, received object."
- **`variants[]` item shape** = `form:` (required) + optional `note:`/`reading:`/`register:`
  — NOT `text:`. `restrictions`/`notes` items use `text:`; `variants` does not. A prose aside
  with no alternate surface form belongs in `notes:`, not `variants:`. (Caught in batch 6.)
- **Don't manufacture slots.** CALIBRATION2 §1–§2: presence is *earned*. A `restriction`
  that restates the rule, or a `contrast` no learner confuses, is padding — omit it.
  Equally, a real prohibition or confusable sibling is **mandatory**, not optional.

## 5. Validation snippet (pre-build lint)

A stdlib-only pass over the batch catches most issues in seconds before `npm run build`:
brace balance (`jp` count of `{` == `}`, no `{}`), each `slug:` in `contrasts` exists as a
file, each `prereqs` entry exists (or is `*`-anchored), each `sense:` ref matches a
`senses[].label`. (See the inline scripts used in recent batches; promote to
`scripts/lint_batch.py` if it recurs.)
