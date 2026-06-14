# TREE — Grammar Skill-Tree Architecture

Design decisions for the jengolang.com grammar **skill tree**: the navigable map
that replaces JENGOLANG.md's flat "leveled-category articles" model as the primary
IA for grammar content. Source catalog: `JengoApp/scripts/ocr_output/grammar_reconciled.csv`
(~1,502 romaji index rows from the DBJG/DIJG/DAJG dictionaries — see `GRAMMAR.md`
for ingestion).

This doc owns the **product/IA model**. `GRAMMAR.md` owns ingestion. `CALIBRATION.md`
owns the enrichment judgment rubric (frozen spec for every enricher/agent).
`JENGOLANG.md` owns the wider site/content/SEO plan (and must be updated to point
grammar at this tree).

## ► CURRENT STATE (top of stack — read this first, 2026-06-14)

All design **LOCKED** (content schema + sense layer + render tech 2026-06-04, app-funnel
2026-06-05); catalog enrichment **complete** (1,458 nodes post-dedup, QA PASS); the full
Content Collection is **materialized + rendered** ([slug].astro template done). **Frontier
= Pass-2 long-tail teaching-content fill.** Done so far: Foundations 60/60 + Read-novels
branch 22/22 + long-tail batches 1–3 (21 + 15 + 14 essential N5/N4) → **138 nodes
indexed**, ~1,320 stubs remain. **Next action = long-tail batch 4** (run
`scripts/list_stubs.py --freq essential`; **48 essential stubs left**, then `--freq
common`). Then **step 4 = tree UI pan/zoom** (extend `index.astro`; render tech locked
below). The dated BUILD log further down is *history* — for "what now," this block + the
next one are enough.

## ► Resuming Pass-2 long-tail (operating procedure)

The judgment rubric is **`CALIBRATION2.md`** (read it before enriching). This is just the
*mechanic* + the gotchas that cost a cold session real time:

1. **Pick the batch.** `python3 scripts/list_stubs.py --freq essential` (then `common`).
   Fill order is LOCKED: highest `freq` first, low JLPT first within a band (SEO weight,
   per JENGOLANG) — **not** tree position. Group ~15–25 into *thematic clusters* so the
   `contrasts` slot cross-links densely (the GEO win).
2. **Edit each file** `src/content/japanese/grammar/<slug>.md`. **Read-before-Write is
   required by the harness** — `cat` via Bash does *not* satisfy it; use the Read tool, or
   Write fails. Preserve the seeded tag-layer frontmatter; append the teaching layer.
3. **Verify every `contrasts`/`prereqs` slug exists before referencing it** — a dangling
   slug fails `npm run build`. Common homograph traps (grep first if unsure):
   `ga-2` = subject が · `ga-3` = "but" が · `to-2` = "and/with" と · `to-quotative` =
   quote と · `souda` = hearsay そうだ · `youda`/`mitai`/`mitaida`/`rashii` = seeming ·
   `reru` = potential/passive れる · `rareru` = honorific · `rareru-2` = passive られる ·
   `te-mo-ii` (not `temo-ii`) · `kurai`/`gurai` are a fold pair.
4. **Flip `noindex: false`** only when the node clears the non-thin gate (CALIBRATION2 §5:
   key sentence per sense + examples threshold + equivalents). Low-confidence/shaky nodes
   fill conservatively and **stay `noindex`** by design.
5. **Validate:** `npm run build` (validates all 1,458 — schema + dangling slugs). For a
   pre-build local lint, a quick stdlib check over the batch for furigana brace balance
   (`{`==`}`, no empty `{}`), dangling contrast slugs, and the noindex flip catches most
   issues in seconds. Then spot-read ~10% against CALIBRATION2 §1–§4.

There is **no progress-cursor file** for Pass-2 — `list_stubs.py` *is* the resume state
(a node is done iff `noindex:false`). `--enriched` lists what's finished.

> **This handoff is meant to evolve.** When a session re-derives something the docs
> should have given it (a query, a gotcha, a disambiguation), fold that back in — and
> prefer **a committed script over prose** (turn "the query I had to write" into
> `scripts/*.py`, like `list_stubs.py`). Keep this CURRENT-STATE block fresh and the
> dated log append-only as history; don't let the log grow to where the frontier is hard
> to find. The goal is that the *next* cold start is faster than this one was.
**BUILD step 1 DONE (2026-06-05):** the 8 form-anchors (SLICE Finding 2) are promoted to
real catalog rows (`grammar_enriched.csv` = 1,527, `family=form`) + real teaching pages in
a bootstrapped Astro Content Collection (`src/content.config.ts` + 8 `.md` files); all
`*<anchor>` prereqs flipped to bare slugs; `build_slice.py` resolves anchors from the
catalog; QA + `npm run build` PASS.
**BUILD step 2 DONE (2026-06-11):** same-surface dedup/sense review (SLICE Finding 3).
All **78 same-surface clusters (175 nodes)** in the full catalog adjudicated by hand —
keep-distinct (genuine sense, #3) vs merge (OCR/cross-row dup). **69 dups merged →
`grammar_enriched.csv` = 1,458**; sense-splits kept (を×4, に×5, られる×3, の×3…).
Decisions frozen in `scripts/data/dedup_decisions.json`, applied by
`scripts/apply_dedup.py` (repoints every prereq/fold ref to the survivor, safety-gated
against the curated path), audit `scripts/data/dedup_applied.md`. `qa_grammar_nodes.py`
gained a `--merges` flag (merged high-risk term = covered). QA + `build_slice` + `npm run
build` all PASS.
**BUILD step 3a DONE (2026-06-13):** Content Collection fully materialized. New seeder
`scripts/seed_nodes.py` writes one **tag-layer** `.md` per catalog node from
`grammar_enriched.csv` (identity + #7 tags + DAG prereqs + `sources.volumes`, `noindex:
true`, empty teaching body) — **1,450 seeded, the 8 hand-enriched anchors skipped** (never
overwrites). All **1,458** files now validate against the Zod schema (`npm run build`
PASS); catalog QA PASS with `--merges scripts/data/dedup_decisions.json` (the post-dedup
invocation — CLAUDE.md updated).
**BUILD step 3b-template DONE (2026-06-13):** node-page template
`src/pages/learn/japanese/grammar/[slug].astro` built (ran `/impeccable teach` —
PRODUCT.md/DESIGN.md already complete). Renders the full 9-slot schema in DBJG order
(Header+badges → Builds-on chips → Meaning → Key sentence(s) → Formation → Variants →
Examples → When-you-can't-use → Easily-confused-with → Notes → soft AppCTA → See-also),
single-column mobile-first, DESIGN.md tokens; build-time furigana parser
(`漢字{かんじ}`→`<ruby>`); single-sense↔multi-sense normalized to one render path; per-slot
visual distinction (green key-sentence hero, clay "can't use" callout, indigo "confused
with" comparison). **Decisions (user-confirmed):** stubs render a real "guide coming"
page (noindex, still navigable); prereqs/related = inline-top "Builds on" + footer "See
also"; ad slots reserved (commented) not rendered (AdSense=Phase 4). `noindex` from
frontmatter; JSON-LD Article only when indexed + has content. **All 1,458 pages prerender
+ validate** (`prerender=true`); build ~78s after fixing an O(n²) (resolve nav labels
once in `getStaticPaths`, not per-page). Tree `index.astro` cards now link to node pages.
**BUILD step 3b-Foundations DONE (2026-06-13):** Pass-2 teaching-content fill for the
**entire Foundations line — all 60 nodes** (58 stubs hand-enriched per CALIBRATION2.md;
the 8 form-anchors were already done). Every Foundations node now clears the non-thin gate
(`keySentence`/`senses` + examples + equivalents) and **flipped `noindex:false`** → the
curated trunk indexes immediately. Slot judgment applied per CALIBRATION2 §1–§3 (presence
earned, not defaulted): multi-sense `senses[]` where real (に destination/existence/time,
で place/means/cause/scope, か question/or/embedded, と and/with, ている ongoing/resulting,
てしまう completion/regret, ほしい thing/action, まで endpoint/even, ない negation/existential);
high-value `restrictions` + cross-linked `contrasts` on the confusion clusters (は/が, the
four conditionals と/たら/ば/なら, あげる/くれる/もらう + てあげる/てくれる/てもらう, から/ので,
けど/が/のに, 前に/あとで, だろう/でしょう/かもしれない/はず). All 1,458 pages build PASS,
0 dangling contrast/prereq slugs, multi-sense + sense-pinned restrictions render verified.
A few Pass-1 `confidence` upgrades med/low→high where the meaning was never actually shaky
(datta, de, hoshii, kara, ga-3, ichiban, to-conditional). **Next: step 3b-goals** = Pass-2
fill of the active goal-route nodes (Read-novels branch + any other launched lines), then
long-tail. **step 4** = tree UI pan/zoom.
**BUILD step 3b-goals DONE (2026-06-14):** Pass-2 teaching-content fill for the
**entire Read-novels goal branch — all 22 nodes** (the literary route from the vertical
slice, `register⊇{literary}`). Every node hand-enriched per CALIBRATION2.md, clears the
non-thin gate (key sentence + examples ≥3 + equivalents), and **flipped `noindex:false`**
→ the goal route indexes. Slot judgment applied per CALIBRATION2 §1–§3: multi-sense
`senses[]` where real (まい neg-conjecture/neg-volition, 故に therefore/because-of); high-
value `restrictions` on the form-restricted classics (だに's fixed set, なり same-subject/
spontaneous, べからず/べく irregular せ-, すら negative-polarity, かのごとく counterfactual);
cross-linked `contrasts` on the confusion clusters (である/だ/です, ず/ぬ/ないで,
ねばならない/なければならない, であろう/だろう, 如し/ようだ, のみ/だけ/ばかり, すら/さえ/も,
だに/すら/さえ, つつ/ながら, as-soon-as なり/や否や/途端に/と同時に, と言えども/とはいえ/ても,
ものを/のに, 故に/から/ために, にあって/において, 折に/際に/とき). A few Pass-1 med→high
confidence upgrades where the meaning was never shaky (mai, to-ie-domo); nari kept med
(homograph family) but indexed with a disambiguating note. All 1,458 pages build PASS,
0 dangling contrast/prereq slugs, 0 furigana brace imbalances. **Next: long-tail Pass-2
fill** (remaining ~1,376 stubs, stay noindex until enriched) + **step 4** = tree UI
pan/zoom.
**BUILD long-tail batch 1 DONE (2026-06-14):** Pass-2 fill of the **21 highest-value
essential N5/N4 stubs** (the first long-tail batch — selected by `freq=essential` + low
JLPT for SEO weight per JENGOLANG, not by tree position; 97 essential stubs remain after
this). Thematically clustered so `contrasts` cross-link densely: limiting particles
(だけ/しか, the canonical 'only' pair), comparison/degree (より multi-sense than/from,
ほど multi-sense degree/neg-comparison, ぐらい), desire/intention (がほしい, つもり,
ようと思う), ability/seeming (ことができる, ようだ multi-sense conjecture/resemblance,
やすい), quotation (と/という/と思う), connectives (だから, しかし, そして), and the
obligation/permission/advice quadrant (なければならない/なくてもいい/たほうがいい, all
cross-linked to the already-done てはいけない/てもいい). Slot judgment per CALIBRATION2
§1–§3: multi-sense `senses[]` only where real (より, ほど, ようだ, という); high-value
`restrictions` on the learner-error classics (しか-needs-negative, ほしい-3rd-person→
ほしがる, たほうがいい-past-form, にとって≠のために benefit, ことができる no double-potential);
contrasts seeded from same-`family`. Confidence upgrades med/low→high where meaning was
never shaky (to-quotative, hodo→med). `しかし` register corrected casual→formal/written.
All flipped `noindex:false` (109 indexed now, was 88). All 1,458 pages build PASS,
0 dangling contrast/prereq slugs, 0 furigana imbalances, rendered furigana + multi-sense
verified. **Next: long-tail batch 2** (the remaining ~76 essential stubs, then common) +
**step 4** = tree UI pan/zoom.
**BUILD long-tail batch 2 DONE (2026-06-14):** Pass-2 fill of **15 essential N4/N5 stubs** —
the **obligation / prohibition / advice web + explanatory のだ + polite invitations** cluster,
chosen to cross-link densely into batch-1's already-indexed てはいけない/てもいい/なくてもいい/
たほうがいい/なければならない. Nodes: the "must" family (なければ conditional base +
なければいけない/なくてはいけない/なくてはならない/ないといけない — all four contrasted as
same-meaning-different-base/register, the canonical learner question), advice
(ないほうがいい/ほうがいい — ほうがいい framed as the **comparison** form のほうがいい+より to
differentiate from batch-1's たほうがいい specific-advice), polite prohibition/request
(てはいけません/ないでください), explanatory のだ/んです/のです (のだ = full canonical page w/
`nuance` + overuse `restriction`; んです/のです indexed as register variants per the
darou/deshou precedent), and the invitation trio ましょう/ましょうか/ませんか (cross-linked).
Slot judgment per CALIBRATION2 §1–§3: `restrictions` only where a real learner-error exists
(ないほうがいい keeps ない-form not past; ほうがいい past-vs-nonpast; のだ overuse); `nuance`
fired on のだ/ましょうか/ませんか (connotation a structured field can't carry); no manufactured
slots. **One Pass-1 tag fix:** `nai-de-kudasai` keigo sonkeigo→teineigo (ないでください is
plain polite, not honorific). All flipped `noindex:false` (**124 indexed now, was 109**;
62 essential stubs remain). All 1,458 pages build PASS, 0 dangling contrast/prereq slugs,
0 furigana brace imbalances (pre-build stdlib lint + `npm run build`). **Next: long-tail
batch 3** (62 essential stubs left → then `--freq common`) + **step 4** = tree UI pan/zoom.
**BUILD long-tail batch 3 DONE (2026-06-14):** Pass-2 fill of **14 essential N5/N4 stubs** —
the **existence / becoming / よう-aspect / purpose** web, chosen for dense internal
cross-linking. Nodes: existence (ある/いる + the 〜がある/〜がいる/〜があります constructions —
core teaching point = the **animate/inanimate** split, fired as a `restriction` on each + the
ある↔いる, がある↔がいる contrasts), becoming/deciding (なる + 〜になる・〜くなる + にする — the
canonical **になる/にする** natural-vs-deliberate contrast pair, `restriction` on くなる-not-になる
for i-adjectives), the よう family (**ように** done as a rich **2-sense** node resemblance/purpose
with the ように-vs-ために purpose `restriction`; ようになる/ようにする the なる/する change-vs-effort
pair; **ようとする** 2-sense attempt/about-to), and purpose (ために verb-purpose + のために
**2-sense** benefit/cause). Multi-sense nodes used `senses[]` with sense-pinned
`restrictions`/`contrasts` (e.g. ように purpose-restriction pinned to the purpose sense).
Slot judgment per CALIBRATION2 §1–§3: `restrictions` only on real learner-errors
(animate/inanimate, くなる, ように/ために); `nuance` on なる (natural-change feel); no
manufactured slots. All flipped `noindex:false` (**138 indexed now, was 124**; 48 essential
stubs remain). All 1,458 pages build PASS, 0 dangling slugs, 0 furigana imbalances, all
sense-refs match a senses[].label (pre-build stdlib lint + `npm run build`). **Next:
long-tail batch 4** (48 essential stubs left → then `--freq common`) + **step 4** = tree UI
pan/zoom.

---

## Locked decisions

| # | Decision | Detail |
|---|----------|--------|
| 1 | **Scope = open-ended** | The DBJG index is a *seed*, not the boundary. Augment with other guides + AI gap-fills + colloquial/literary grammar. No fixed node count. |
| 2 | **Comprehensive catalog, curated path** | Every *real* grammar point gets a node + page (long-tail SEO). The tree's mandatory path routes only through high-value grammar; rare/archaic/niche live on optional, dimmed branches. Two bars: "is it real grammar?" (gets a node) vs "is it on the main path?" (trunk placement). |
| 3 | **Node = distinct teachable pattern** | Not one index row, not one headword. Dedup pure OCR/spelling variants, but KEEP semantically-distinct patterns separate even when they share a keyword (`bakari` / `bakari da` / `bakari ni` / `bakari de naku` = 4 nodes; the 3 OCR'd `~ba~hodo` rows = 1). Est. **~700–900 nodes**. Curation verdict per row = **own-node / fold-into-parent-as-note / merge-dup**. "Stripped to bones" = strip dictionary verbosity + over-segmentation, NOT delete real grammar. |
| 4 | **Backbone = prerequisite DAG** | An edge = "you must understand X before Y makes sense." Category/modality is an *orthogonal tag*, not the edge. |
| 5 | **Goal lens = tags + presets** | Per-node tags + saved goal presets that **highlight/dim**. **Everything always visible, never hidden** — the value is perspective ("huh, that exists — later"). The dictionary failed because you couldn't tell what was *related*, not because unrelated grammar was present. (Also ideal for SEO: all nodes always in the DOM.) |
| 6 | **Position = prereq depth** | A node sits one tier out from its hardest prerequisite. Frequency/usefulness = tiebreaker + visual prominence (size/brightness). JLPT = badge + filter only; it never moves a node. |
| 7 | **Tag schema (two-axis + metadata)** | `register` is a **set** ⊆ {casual-spoken, polite-spoken, written-modern, literary, archaic}; `keigo` ∈ {none, teineigo, sonkeigo, kenjougo}; `freq` ∈ {essential, common, uncommon, rare}; `jlpt` ∈ {N5..N1, none}; `family` ∈ {conditional, causative, passive, aspect, modality, quotation, connective, nominalizer, …}. Core grammar tagged all-registers → always bright. Goal presets are queries over these. |
| 8 | **Base layout = layered tech-tree** | Top-down, tier = prereq depth. Chosen over radial because beginners need an unambiguous "start here, go down." Rendered as a single semantic-zoom canvas; ship a parallel static node-link index for crawlers. |
| 9 | **Core = the "Foundations" line** | Early grammar is a dense interconnected mesh, but the learner doesn't navigate the mesh — they follow a **curated near-linear "Foundations" line laid through it** (mesh edges render faint; the recommended path is bold). Foundations is the mandatory first leg every goal route shares. |
| 10 | **Goals = subway lines (outcome-based)** | Pick an *outcome* ("understand anime", "read novels", "pass N2", "business Japanese") → it lights its route through the graph, Foundations-first then its own branch, everything else dimmed. Lines are just filter presets over the tag schema (no new data model). Each line = an SEO/GEO landing page ("The N2 grammar checklist", "Every grammar point to read Japanese novels"). |
| 11 | **Progress = localStorage now, app-sync later** | v1: self-checkoff stored in-browser; node states locked/available/done; **gating is soft** (visual only — reading never blocked). Structure designed to lift into a Jengo account later (cross-device, app-activity auto-fills the map → strongest funnel). |
| 12 | **Data completion = AI-first, gated** | LLM pass per catalog row → {canonical kana/kanji, plain meaning, register/keigo/freq/jlpt/family tags, candidate prereqs, **confidence**}. High-confidence auto-accepts; low-confidence (obscure romaji, missing gloss, self-referential, QA-flagged) → review queue for user / web / printed book. The gate's flag-rate *is* the "good enough to continue?" metric. |
| 13 | **URLs extend the existing scheme** | Tree hub = `/learn/japanese/grammar`. Node = `/learn/japanese/grammar/[slug]` (slug = romaji pattern, e.g. `te-iru`, `bakari-ni`). Goal line = `/learn/japanese/grammar/path/[goal]` (e.g. `/path/n2`, `/path/anime`). Language-segmented, multi-lang ready. |
| 14 | **Collision guard on enrichment** | The top enrichment risk is *false-confidence sense-collisions* — a romaji string with several grammar senses where AI confidently picks the wrong one. Rule: enumerate every sense for a term; disambiguate by gloss / volume (B/I/A) / superscript-homograph; if still ambiguous, flag (med/low confidence) even with a default guess. Auto-pre-flagged by `prep_grammar_nodes.py` (`collision` risk). |
| 15 | **External-source reconciliation** (PASS 1 DONE 2026-06-02) | Compared the catalog against Bunpro (910) + JLPTsensei (696) + Tae Kim to (a) catch sense-collisions and (b) fill grammar the DBJG series lacks (#1). The catch-net for #14. Results in "Step 4a" below: 85 JLPT-badge fixes applied, 4 collisions flagged, 22 low-conf re-checked, **519 gap candidates** queued for the next enrichment batch. |
| 16 | **Slug = node identity, prereqs = slugs** | Each node gets a stable kebab `slug` at enrichment time (= the #13 URL). Rule: lowercase romaji term; drop homograph markers but disambiguate with a numeric suffix (`aru`/`aru-2`); spaces, `~`, and parenthesised tails → hyphens (`bakari-ni`, `aida-ni`, `de-mo`). `candidate_prereqs` reference the **exact prerequisite node's slug** so the DAG (#4) resolves straight from enrichment output; a foundational prereq that is *not* a catalog node (e.g. te-form, masu-stem) is written with a leading `*` (`*te-form`) to mark a non-catalog anchor rather than a dangling ref. |

---

## App funnel placement (LOCKED 2026-06-05)

**Posture = minimal / protect-content (v1).** Jengo is framed as a **companion
learning tool that pairs with the grammar page — not an advertisement.** On content
pages the funnel *competes* with the other two goals (ad revenue + SEO/GEO trust), so
v1 deliberately under-asks; scale up only **after the content model proves itself**
(traffic + engagement). Rationale: most SEO/GEO traffic is low-commitment drive-by
lookup (interrupting = bounce), Google penalizes intrusive mobile interstitials, and
the page already carries 2 ad slots (density budget).

**Framing/mechanic (LOCKED):** **contextual feature + progress-sync**, never
install-first. The hook = the app's "vocab in real-sentence context" maps exactly onto
a node's example block → *"see 〜ている across 30 real sentences in Jengo,"* not
"download our app." Progress-sync (#11) is the earned, value-forward pitch (*"save your
tree progress — it syncs with your app study"*).

**v1 surfaces (minimal):**
- **Every page:** low-profile header "Open app" link (the floor).
- **Node + goal pages:** **ONE** soft contextual `AppCTA` at end-of-content, copy =
  companion-tool framing tied to that grammar's examples. Placed **above** the final ad
  (page doesn't close on an ad). **Max 1 app-ask per content page**, visually distinct
  from the ad slots.
- **Tree hub:** light progress-sync affordance, value-forward, **not** pushed;
  strengthens after node check-offs. (Depends on account/sync — until it exists, a soft
  "make a free account to save progress" or omit.)
- **Vocab pages:** soft "study these in Jengo" at end + the future "Add to Jengo" deep-link.
- **Destination, phased:** contextual copy → app store / app home now; **true deep-link**
  (open these exact words / this grammar in-app) later, tied to the app backlog — the
  biggest conversion unlock but needs app support.
- **Rejected in v1:** sticky/floating bar, interstitials/modals, a second post-examples
  ask, goal-page hero CTA.

**Saved scale-up plan** (trigger = content model proven). Move minimal → **balanced,
surface-varied:** add the post-examples node CTA, a goal-page hero CTA ("Track this
path in Jengo"), stronger tree progress-sync prominence; A/B a persistent low-profile
bar. **Full-screen interstitials stay rejected at every stage** (mobile SEO penalty).

## Still open

*(none — content schema, render tech, SEO posture, and app-funnel placement all
locked. Next is the build, not more design.)*

---

## Per-node content schema (LOCKED 2026-06-04)

**Storage = Astro Content Collections, one file per node.** Matches JENGOLANG.md's
original `content/japanese/grammar/*.md` plan, Zod-validated, multi-language-ready.
The enriched catalog (`grammar_enriched.csv`, 1,521 nodes) is the **seed**: a
migration script writes one file per node with the tag layer pre-filled; the
**teaching layer is a 2nd enrichment pass** (gated + machine-validated, same
discipline as the first — frozen spec = **CALIBRATION2.md**; Pass-1 metadata spec =
CALIBRATION.md).

**Two layers per file:**
1. **Tag layer (frontmatter, seeded from CSV)** — node identity + the #7 tag schema +
   DAG edges. Already exists per node.
2. **Teaching layer (filled by pass 2)** — the article. Structured arrays so rendering
   is uniform + each field is Zod-validated; one short *optional* prose field for
   genuine nuance, always in the same slot.

### Two governing principles (from the user, 2026-06-04)
- **Consistent slots, judgment-driven presence.** The schema is a **superset of
  optional slots**. Consistency lives in slot *position + colour + format* — when a
  section appears it is always in the same place and styled the same (retrievability
  across 1,521 nodes). *Presence* is a per-principle **judgment call** by the pass-2
  enricher: a point with no confusable sibling shows no Confused-with; one with no
  restriction shows no Can't-use. This is how TREE #3's "judgment over rubric" survives
  contact with a fixed schema — don't ram every principle through every slot.
- **Streamlined, never thin-but-padded.** Each field is exactly what the reader needs
  — no rambling. Different *categories* of information must be **visibly distinct**
  (own colour/icon/format) and each rendered in its best format (table vs cards vs
  chips vs callout), not a uniform wall of text.

### Section order (LOCKED — mirrors the scanned DBJG: Key-Sentence → Formation → Examples → Notes → Related)
1. **Header** — pattern (canonical + reading ruby) + **badges** = category/`family`,
   `register` set, `keigo`, `jlpt`, `freq`. (The "category" field = these tags, *not* a
   body section.) Prereqs / See-also are **nav chrome** (rail + footer from the DAG), not
   body sections.
2. **Meaning** — nearest English equivalent(s) + one clarifying clause; **+ optional
   short prose** nuance field (used only where sentences beat structure).
3. **Key sentence** — ONE hero example, clean **base form** (no variants), furigana.
   Show-don't-tell before any rule. *Effectively mandatory → doubles as the non-thin gate.*
   **Multi-sense nodes get one hero per sense** (DBJG KS①/KS② — see Senses below).
4. **Formation** — attachment/conjugation table + one `usage_setting` line (where/when deployed).
5. **Variants** — same-meaning surface forms (なきゃ/なくちゃ/ねば for なければ): contracted /
   register-shifted / written. **Folded forms, not own nodes** (distinct from TREE #3's
   own-node patterns). Placed before the full example set so examples may use them.
6. **Examples** — the full set, **graded only when the grammar warrants it** (optional
   `level`; never force tiers — that would be ramming the rubric). May use variants.
7. **When you can't use it** — restrictions / negative space. Promoted to its **own slot**
   (the thing dictionaries do worst), not buried in notes.
8. **Easily confused with** — sibling disambiguation (= `contrasts`). DBJG's "Related
   Expressions"; the capstone that **links out** to sibling nodes (GEO win).
9. **Notes** — strictly residual. If a fact fits Variants/Can't-use/Confused-with it goes
   *there*; Notes is the last resort, never a dumping ground.

```ts
// src/content/config.ts  (sketch)
const register = z.enum(['casual-spoken','polite-spoken','written-modern','literary','archaic']);
const ex = z.object({ jp: z.string(), en: z.string(), note: z.string().optional(),  // jp = 漢字{かんじ} markup
                      level: z.enum(['intro','core','advanced']).optional() });
// a sense = the sense-DEFINING slots; node-level slots that can scope to one sense carry `sense`.
const sense = z.object({ label: z.string(), equivalents: z.array(z.string()).default([]),
                         keySentence: ex.optional(), examples: z.array(ex).default([]) });
schema: z.object({
  // — tag layer (seeded from grammar_enriched.csv); renders as Header badges (slot 1) —
  title: z.string(),                 // display heading, e.g. "〜ている — Ongoing Actions & States"
  canonical: z.string(), reading: z.string(),
  register: z.array(register), keigo: z.enum(['none','teineigo','sonkeigo','kenjougo']),
  freq: z.enum(['essential','common','uncommon','rare']),
  jlpt: z.enum(['N5','N4','N3','N2','N1','none']),
  family: z.string(),
  prereqs: z.array(z.string()).default([]),   // slugs, may be *-anchors — NAV chrome, not a body slot
  related: z.array(z.string()).default([]),   // see-also slugs — NAV chrome
  foldInto: z.string().optional(), confidence: z.enum(['high','med','low']),
  stage: z.object({ line: z.string(), index: z.number(), label: z.string() }).optional(),
  sources: z.object({ volumes: z.string().optional(), external: z.string().optional() }).optional(),
  // — teaching layer (pass 2; every field below is an OPTIONAL slot, present by judgment) —
  nuance:      z.string().optional(),                                   // 2 Meaning — short optional prose
  // SENSE-DEFINING slots: flat for single-sense; OR senses[] when multi (renderer normalizes — see below).
  equivalents: z.array(z.string()).default([]),                         // 2 Meaning — "≈ -ing / is in a state of"
  keySentence: ex.optional(),                                           // 3 hero, base form (de-facto required)
  examples:    z.array(ex).default([]),                                 // 6 full set, graded only when warranted
  senses:      z.array(sense).optional(),                               // present ONLY for multi-sense (≥2). overrides the 3 flat fields above.
  // SHARED scaffolding (node-level; each item may pin to a sense via `sense: label`) —
  formation:   z.array(z.object({ attaches_to: z.string(), form: z.string(), example: z.string().optional(),
                                  sense: z.string().optional() })).default([]),                                       // 4
  usageSetting: z.string().optional(),                                  // 4 where/when deployed
  variants:    z.array(z.object({ form: z.string(), reading: z.string().optional(),
                                  register: z.array(register).optional(), note: z.string().optional() })).default([]), // 5
  restrictions: z.array(z.object({ text: z.string(), sense: z.string().optional() })).default([]),                    // 7
  contrasts:   z.array(z.object({ slug: z.string(), label: z.string(), distinction: z.string(),
                                  sense: z.string().optional() })).default([]),                                        // 8
  notes:       z.array(z.object({ text: z.string(), sense: z.string().optional() })).default([]),                     // 9 residual only
  noindex:     z.boolean().default(true),                               // tiered fill — see below
})
```

**Senses (multi-meaning nodes) — carry DBJG's per-sense key sentence.**
- **Sense ≠ variant** (different *meaning*, same *form* — vs variant = same meaning,
  different form). Don't fold senses into Variants or into one flat example list.
- **Node-vs-sense boundary** (consistent with #3): *different form/particle/formation →
  separate nodes* (ばかり/ばかりだ/ばかりに already 4); *identical form + formation,
  meaning splits by context → one node, multiple senses* (ている = ongoing / resulting state).
- **Storage = lean, render = uniform.** Single-sense nodes use the flat `equivalents`/
  `keySentence`/`examples`. Multi-sense nodes put those in **`senses[]`** (each =
  label + equivalents + key sentence + its own examples). The render layer normalizes
  `senses ?? [{equivalents, keySentence, examples}]` → **one render path**, so the slot
  position/styling is identical whether a node has 1 sense or 3. Multi-sense ⇒ one hero
  per sense up top (KS①/KS②), examples grouped by sense.
- **Sense-scoped scaffolding:** `formation`/`restrictions`/`contrasts`/`notes` stay
  node-level but each item may carry `sense: <label>` to pin it to one sense (DBJG's
  "Note 2 applies to ②"); absent `sense` = applies to all.
- The pass-2 enricher's first judgment per node is **"how many senses?"** — array
  length encodes it; the non-thin gate requires a key sentence **per sense**.

- **Furigana**: any `jp` written as `漢字{かんじ}` markup → build-time parser →
  `<ruby>漢字<rt>かんじ</rt></ruby>` (crawlable per the SEO strategy).
- **Visual distinction per slot** (light-mode, Jengo palette): Meaning = clean lead;
  Formation = table/mono; Key-sentence + Examples = JP-large furigana cards (the visual
  heart), EN muted; Variants = compact chips/row; Can't-use = bordered callout (clay/amber
  accent, *not* alarm red); Confused-with = paired/two-column comparison (indigo accent);
  Notes = subdued callout. Same category ⇒ same treatment on every node.
- **Contrasts** seed from same-`family` clustering, curated in pass 2.

**Tiered fill / SEO posture (LOCKED — "noindex long-tail").** Don't ship ~1,400 thin
pages (Google doorway/thin-content penalty risks the *good* pages too). Rule:
- **`noindex: true` by default.** A build step flips it `false` only when the page
  clears the not-thin bar — `explanation` present **and** `examples.length >= 4`.
- **Fill order:** curated path first (Foundations ~60 + active goal routes) → those
  index immediately. Long-tail nodes stay **visible + crawlable in the tree map**
  (every node always in the DOM, #5) but their solo page is `noindex` until enriched.
- This keeps #2 (comprehensive catalog) + #5 (never hidden) intact without the thin-content tax.

## Render tech (LOCKED 2026-06-04)

**Astro-native: build-time positioned HTML+SVG + one small vanilla island. No D3 /
Cytoscape / Sigma.** Finding #1 (SLICE.md) is the deciding fact — **layout positions
are deterministic from the curated `stage`**, not from a graph layout engine, so the
auto-layout/perf value of those libs is mostly wasted at our ~1,521 static nodes.

- **Build time:** `stage.index → y`, within-stage order `→ x`; edges = one SVG layer.
  The static DOM **doubles as the crawlable SEO index** — collapses decision #8's
  "parallel static node-link index" into a *single* artifact (no dual maintenance).
- **Island (~5kb vanilla):** panzoom (~3kb, e.g. anvaka/panzoom or hand-rolled
  wheel/touch) + **semantic zoom** (cull labels by scale via CSS var) + **goal-line
  filtering = class toggles** (`.lit`/`.dim`) over the tag schema (#10, no new data model).
- **Mobile-first, light-mode, Jengo palette** — full control of the card aesthetic
  (a WebGL canvas can't match it and isn't crawlable).
- **Escape hatch:** reach for Sigma/WebGL **only if** profiling shows the full
  1,521-node DOM janks on target mobile; even then keep the static index for SEO.
  Mitigation before that: lazy-mount the dimmed long-tail cloud (mandatory-visible
  set = Foundations + active goal line is ~80 nodes).

The slice render (`src/pages/learn/japanese/grammar/index.astro`) is already this
pattern (stage-grouped, server-positioned) — extend it to full pan/zoom + filtering.

## Status & next session (2026-05-30)

**Pilot done.** The enrichment pilot confirmed the catalog is AI-recoverable: the
failure mode is OCR garble, not unknown grammar. Prep step built (`prep_grammar_nodes.py`)
→ **`grammar_nodes.csv`** = **1,090 candidate nodes**, of which **64 collision-risk +
20 garble-risk** are auto-flagged as the judgment-heavy worklist; ~1,006 are clean.

**Execution decision (changed):** enrichment is done **by Claude in-session via this
chat interface — NOT the API.** The Anthropic API key in `JengoApp/.env` has no
credits, and the user prefers the in-session hand-pass anyway (full review, asks
questions on ambiguity). The Batch-API pipeline (`enrich_grammar_nodes.py`) is built
and validated up to the billing wall — **parked as a fallback** if credits are added.

**DONE so far:** high-risk pass **98/98** → `grammar_enriched.csv` (106 records, QA PASS).
`CALIBRATION.md` frozen. `qa_grammar_nodes.py` built. Clean pilot (23 source terms →
`grammar_enrich_pilot.csv`, throwaway, pre-/overlap notes below).

**Scripts (in `JengoApp/scripts/`):** `prep_grammar_nodes.py` (catalog→worklist, regex
bug fixed), `qa_grammar_nodes.py` (QA, done), `enrich_grammar_nodes.py` (API enrichment,
parked on billing).

---

## ► CLEAN-PASS HANDOFF (next session — start here)

**Goal:** enrich the remaining **992 clean + 53 missing_only** rows of
`grammar_nodes.csv` into `grammar_enriched.csv`, applying **`CALIBRATION.md`** (the
frozen spec — read it first). "Clean" ≠ easy: the pilot measured **~42% need judgment**
and ~980/1,006 rows have NO English gloss (reconstruct meaning from romaji + see-also +
volume). Apply the collision guard to **every** row.

**Step 0 — reconcile the pilot.** The 26 pilot records were written **before** the
homograph-regex fix. Three are now superseded by homograph-aware nodes in the main file
and must be **dropped/redone**, not merged blindly: pilot `iru-3` (要る) → main has
`iru-4`; pilot `kureru` (くれる) → main has it; pilot `nante-2`. The other ~23 pilot
records are good clean work — fold them in (and add `review_reason` to pilot rows
`nai-de-mo-nai`, `ni-itatte-wa`). Easiest: delete the pilot file and re-enrich its 23
terms inside the normal clean order so nothing is special-cased.

**Step 1 — execution: LOCKED = (B) single-thread in-chat** (user chose consistency over
speed, 2026-05-30). One model the whole pass — **Opus** (the ~42% reconstruction-judgment
rows want the strong model; switching models mid-pass is the cross-model variance we're
avoiding). Sonnet single-thread is the only sanctioned fallback if session-count must drop.
Naive agent fan-out was rejected (42%-judgment + latent collisions). Caps below.
**Cost:** in-session = ~6 sessions on the subscription (no per-node $); the parked Batch
path would be ~$3 Sonnet / ~$14 Opus total if credits are ever added.
Catch-net regardless: **run `qa_grammar_nodes.py`**, then spot-read ~15%.

**Step 2 — enrich** (resumable; cursor = `grammar_enrich_progress.json`, set `mode:"clean"`).
  - Fixed order: clean rows **by term**. Read only your slice (offset/limit) — never the
    whole CSV.
  - **Append** to `grammar_enriched.csv`; flush every ~25 rows so compaction loses ≤1 chunk.
  - **Re-anchor every ~50 rows:** restate the CALIBRATION freq/family rubric.
  - **Slugs must be globally unique** — check against existing slugs before writing
    (cross-pass clash already seen: `nante`).

**Step 3 — QA + resolve.**
  - `python3 scripts/qa_grammar_nodes.py grammar_enriched.csv [shards…] --source grammar_nodes.csv`
    → must be PASS (0 hard). Fix dangling prereqs; pending prereqs auto-resolve as nodes appear.
  - **Prereq-resolution fix step:** once the clean pass is complete, flip any still-unresolved
    bare prereq slugs to `*` (non-catalog foundation) — these are the `*te-form`/`*nai-form`
    type anchors. (`te-mo`, `dake`, `bakari`, `koto`, `to-shite` should all become real nodes.)

**Step 4 — then:** external-source reconciliation (#15: Bunpro/Tae Kim/JLPT — catch
sense-collisions, fill DBJG gaps, re-check the 22 low-confidence high-risk nodes), then
build **one vertical slice** (Foundations line + one branch, fully tagged) to validate
the model before the tree UI.

**Calibration question RESOLVED (2026-05-31): KEEP.** Lexical / borderline-lexical
items stay as nodes. Per CALIBRATION §2: keep grammar senses; an entirely-lexical row
→ `fold_into_parent` + `freq=rare`, `jlpt=none`, `conf=low`, review note — **never
deleted**. Borderline adverbs (明らかに/案外/中途半端) kept as `adverbial` with a review
note. Reversible later with one filter on `fold_into_parent`/review_reason.

## Session batching rule (avoid context rot)

In-chat enrichment drifts (inconsistent freq/family/confidence) and risks compaction
long before the 1M window fills. Cap each session by *working enrichment tokens*, not
the hard limit. Footprint ≈ **~300 tokens/clean node**, **~700/high-risk node** (incl.
sense reasoning + user Q&A).

**Per-session caps (whichever hits first):**
- **High-risk pass:** ≤ **50** nodes/session (judgment-bound, not token-bound). 84 total → ~2 sessions.
- **Clean pass:** ≤ **175–200** nodes/session (~250 only if calibration still feels stable). ~1,006 → ~5–6 sessions.
- **Hard backstop:** if working context nears **~150K tokens**, finish the current chunk and stop regardless of count.
- Total job ≈ **7–9 sessions**.

**Protocol (makes sessions resumable + drift-resistant):**
1. **Fixed order:** all `risk != ""` rows first (by term), then clean rows (by term).
2. **Read only your slice** of `grammar_nodes.csv` (offset/limit) — never load all 1,090 (~87K tokens wasted).
3. **Append** results to `grammar_enriched.csv`; flush every **25 clean / 10 high-risk**
   so compaction never loses more than one chunk.
4. **Cursor file** `JengoApp/scripts/ocr_output/grammar_enrich_progress.json` =
   `{mode: "risk"|"clean", last_term, done_count, total}` — update on every flush; next
   session reads it first and resumes after `last_term`.
5. **Re-anchor every ~50 nodes:** restate the tag rubric briefly to fight calibration drift.
6. **Session end:** update this block's status line with the cursor (e.g. "risk pass 50/84 done,
   resume after `noni`").

**Model:** **Opus** drives the 84 high-risk nodes (collision guard #14 is judgment
the strongest model does best); reassess Opus-vs-Sonnet for the ~1,006 clean bulk
after calibration is seen to hold (drift-resistance #72-rule vs. cost).

**Enrichment cursor:** risk pass **COMPLETE 98/98**. Clean pass **COMPLETE
967/992 terms done** (2026-06-02), cursor `mode:"clean"`, `last_term="ǎ shita"`.
The 25-term gap to 992 is **all intentional cross-row-dup drops** (their pattern
lives under another slug) — 10 from Session 6 (`toka 2 toka`, `~tokatoka`,
`towazu o towazu`, `wa oroka`, `wake ga nai`, `yori/no hoka…`, `yoru to ni yoru to`,
`~ba~hodo`, `~de are- de are`, `~mo mo`) + 15 from earlier sessions (hazu ga nai,
te mo, te miru, te kudasai, tatte, to ie domo, to shite mo, no da, etc.). Output
`grammar_enriched.csv` = **1,075 records**, QA **PASS** (0 hard, 0 dangling, 0
unresolved bare prereqs — `tokoro`/`yue-ni` now enriched and resolved). Confidence
dist: 640 high / 320 med / 115 low. Session 1 covered `(datta)`→`desu` (256 recs);
Session 2 `dochira ka to ieba`→`kiraida` (+175); Session 3 `kitto`→`nasu` (+175,
K→N, `/effort medium` — no calibration change); Session 4 `naze ka`→`sei` (+168,
N→S: the に〜/の〜/を〜 formal-connective spine + s-starters); Session 5
`sekkaku`→`to wa kagiranai` (+175, S→T: て-form auxiliary/aspect family + そ-discourse
connectors + と〜 quotative/connective spine); **Session 6 covered `toka`→`ǎ shita`
(+126, T→end, run on `/effort high`)**: the とき/ところ temporal-nominalizer cluster,
the は〜 topic-frame + concessive spine (はさておき/は別として/は言うまでもなく), the
よう/ように volitional+manner family (resolved the long-pending `*youni` anchor), the
ず classical-negative spine (ずに/ずにはいられない/ずして/ずとも), and the `~X~Y` paired-
listing family (たり〜たり, か〜か, やら〜やら, でも〜でも…). **Clean pass done →
proceed to Step 4 (external-source reconciliation, then build one vertical slice).**
Helper
`scripts/append_enriched.py` (validates enums + global slug-uniqueness, appends,
advances cursor) — feed it a JSON batch + the new last_term.
Clean-pass notes for next session: (a) many て→で voiced allomorphs (であげる/でいる/
でおく…) were emitted with `fold_into_parent` = their て-form parent slug (te-ageru,
te-iru…) — those parents land under 't', will resolve then; (b) the `dake de (wa)
naku` family already has 7 near-dup rows (slugs `dake-de-wa-naku-3..7`) all flagged
merge; expect more cross-ref dups; (c) lexical question (CALIBRATION §2) handled
conservatively — borderline adverbs (明らかに/案外/中途半端) kept as `adverbial` with a
review note, never deleted; (d) pending prereqs `koto`/`nara`/`to-shite` are real
upcoming terms — leave as-is, they auto-resolve.
**Session 2 learnings:** (e) **slug macron convention = `ou`/`uu`** (ō→ou, ū→uu,
matching existing deshou/darou) — but `qa_grammar_nodes.py` `slugify()` *drops*
macrons (yōni→"yni"), so a prereq pointing at an unenriched よう-family node can't
be auto-classified as pending and shows as a hard `dangling`. Workaround used:
`*`-prefix it (`*youni`), which the Step-3 post-pass reconciles to the real node
once 'y' is enriched (same pattern as `*to-quotative`→`to-quotative`). (f) Genuine
non-catalog foundations must be `*`-prefixed (`*counter`, `*ba-conditional`,
`*ta-form`) or QA hard-fails. (g) Cross-pass dup hit: `hazu-ga-nai` already existed
from the risk pass (term "Vpot hazu ga nai") — dropped my clean dup. (h) Many
OCR-`2`-artifact / repetition garbles in D–K reconstructed conservatively at
`conf=low` with merge notes (`ichi-to-shite-nai`, `kanarazushimo-nai`,
`kesshite-nai`, `ni-kimatte-iru`, `ni-kakete-wa`, `ju-made-mo-nai`).
**Session 3 (K→N, kitto→nasu) learnings:** (i) **effort level is irrelevant to
this pass** — judgment is fixed by the frozen CALIBRATION rubric + collision guard,
so `/effort medium` only set the per-session *count* target (aimed the lower ~175
end of the cap), not per-node rigor. Reported to user. (j) Heavy near-dup clusters
in this slice (`mono(da)`×2→mono-da/mono-da-2, `nashi de(wa)`/`nashi de wa`→
nashi-de-wa/nashi-de-wa-2, `nashi ni(wa)`/`nashi ni wa`→nashi-ni-wa/nashi-ni-wa-2,
`nai koto mo nai`/`mo/wa nai`, `nani-nai`/`nanra-nai`, `mottomo`→split 最も vs
concessive もっとも) — all kept distinct with `-N` suffix + dup-suspect review note
per CALIBRATION (no cross-row merge in-pass). (k) Two cross-row dups already enriched
in earlier passes were **dropped, not re-created**: `ni-koshita-koto-wa-nai` (risk
pass) and slug `nante` (→ used `nante-2` for the exclamatory sense). (l) Same macron
issue as Session 2: prereq `youni` (よう-family) hard-failed QA because slugify drops
ō; `*`-prefixed to `*youni` for the Step-3 post-pass. (m) Lexical/borderline rows
kept per §2 with conf=low + fold/drop note (`kiraida` already there; `nasu` 成す,
`motte-iru` 持っている→folds into te-iru). QA PASS 0 hard after the youni fix.
**Session 4 (naze ka→sei) learnings:** (n) This slice is dominated by the formal
**に〜/の〜/を〜 grammaticalized-connective spine** (に対して, に関して, によって,
をめぐって, を通じて, をはじめ…) — almost all clean N2/N1 `connective`/`particle`,
mostly `conf=high`. (o) Many `/`-slash source terms are te-form + adnominal of one
pattern (`ni hanshite/hansuru`); primary slug = first variant, the adnominal →
`-2` dup-suspect (ni-hanshite-2, ni-kanshite-2, ni-taishite-2). (p) The によって
family had **4 OCR dup rows** → ni-yotte (primary) + ni-yotte-2/3/4 (conf=low,
dup-suspect). (q) **6 cross-row dups dropped or renamed at append time** (QA caught
them as slug clashes vs earlier passes): dropped `ni-koshita-koto-wa-nai`, `no da`
(=existing no-da 'In da'), `ni-hikikae`, `ni-kimatte-iru`, `ni-shita-tokoro-de`,
`no-nan-no-tte`; **emotive を renamed `o-3`→`o-4`** (o/o-2/o-3 already = object/path/
separation を — emotive ものを is a distinct 4th sense, kept). (r) OCR-fused garbles
reconstructed at conf=low: `ni-kankei-naku` (←"ni ni kankei kakete naku wa"=に関係なく),
`okinji-enai` (←を禁じ得ない, dropped を head), `o-oite-hoka-ni-wa-nai` (stray '2'),
`wa-oroka` (←"oroka wa oroka"=はおろか; merge w/ any W-pass row), `oda` (unrecoverable,
fold→no-da, candidate drop). (s) Lexical-fold per §2: `negau`, `okonau` 行う,
`o-kinzuru` 禁ずる kept conf=low with drop-candidate notes (never deleted).
**Session 5 (sekkaku→to wa kagiranai) learnings:** (t) **PREREQ SEPARATOR IS `|`,
NOT comma** — `append_enriched.py` does not validate prereq syntax, so 8 comma-joined
prereqs slipped through and QA hard-failed as `dangling` (the whole `"tai,te-mo"`
read as one slug; `*`-leading comma-joins were silently *skipped*, masking the bug).
Fixed by replacing `,`→`|`. Use `|` for every multi-prereq from now on. (u) Big
clean families landed here: the て-form spine (てあげる/てくれる→te-kudasaru/てもらう/
ていただく auxiliary; ている/てある/ておく/てしまう aspect; てはいけない/てもいい/てほしい
modality) — most `essential`/`common`, `conf=high`; **te-iru and shimau enriched →
resolved two long-standing pending prereqs**. (v) **6 cross-row dups dropped** (already
enriched earlier): te-mo, tatte, te-kudasai, te-miru, to-ie-domo, to-shite-mo. (w)
Internal `-2` dup-suspects kept per CALIBRATION (no in-pass merge): taku-to-mo-nai/-2,
takute-mo-nai/-2, tame-ni/-2, tara-sugu/-2, sono-ue/sono-ue-ni, sukoshi-mo/-nai,
to-iu-yori/-wa, to-iu-fu-ni/to-iu-you-fu-ni/to-iu-youni. (x) Macron slugs follow the
ou/aa convention (souda, saa, sou-ka-to-itte, to-douji-ni, to-iu-youni); none are
referenced as bare prereqs so no slugify-drop hard-fail this slice. (y) One
unrecoverable OCR row left conf=low canonical="": `to-itsu-de-mo` (gloss→度に). (z)
Lexical-fold/borderline per §2: shiru 知る (kept for 知っている), sukida 好きだ, sukunai
少ない, takusan, sumaseru/sumu — conf med/low with notes, never deleted.
**Session 6 (toka→ǎ shita, T→end — FINAL clean slice) learnings:** (aa) **10
cross-row dups dropped** (pattern already enriched under another slug, never
re-created): `toka 2 toka`/`~tokatoka`→toka-toka, `towazu o towazu`→o-towazu,
`wa oroka`→wa-oroka, `wake ga nai`→wake-ga-nai, `yori/no hoka…`→yori-hoka-nai,
`yoru to ni yoru to`→ni-yoru-to, `~ba~hodo`→ba-hodo, `~de are- de are`→de-are-de-are,
`~mo mo`→mo-mo. Verified against the existing-slug set *before* writing — caught
them up front rather than at append. (bb) Internal `-N` dup-suspects kept per
CALIBRATION (no in-pass merge): bakari-de-wa-naku-4, dake-de-wa-naku-8/9,
tari-tari-2, tari-tari-suru-2, yara-yara (vs yarayara), you-ni-mo-nai/-2,
yaya-mo-sureba/-suru-to, yahari/yappari/yahari-yappari, zenzen/zenzen-nai,
totemo/totemo-nai, wa-are/wa-atte-mo, wa-ikenai/wa-naranai, wa-da/wa-desu. (cc)
**`youni` enriched as a rich multi-sense node (resemblance/purpose/manner) →
resolved the long-pending `*youni` anchor** referenced by yona/yoni-so-that; also
enriched tokoro, yue-ni, shimau-adjacent ず-family. (dd) Macron convention held
(ou/oo/aa): you-*, oomune, oozei, aa-shita; ǎ→ああ (aa-shita), ō→おお (oomune 概ね)
vs ō→おう (you- volitional) disambiguated by the actual word. (ee) Bare-romaji
listing patterns `~X~Y` reconstructed as family=particle, mostly uncommon/rare,
conf med/low (ga-nara, ni-nai, wa-wa lowest). (ff) Lexical-fold per §2: wakeru
分ける, oozei 大勢 kept conf=low family=other with "candidate to drop" notes, never
deleted. (gg) **append_enriched.py path quirk:** run the builder with the source
path as `ocr_output/grammar_nodes.csv` (cwd=scripts/); pass QA `--source
grammar_nodes.csv` (basename only — it resolves relative to the enriched file's
dir). (hh) **Final QA: PASS, 0 hard, 0 dangling, 0 unresolved bare prereqs.**

---

## Step 4a — External-source reconciliation (PASS 1 DONE, 2026-06-02)

The #15 catch-net. Compared all **1,075 enriched nodes** against external grammar
references; QA still **PASS** (0 hard) after all edits. Scripts in `JengoApp/scripts/`.

**Reference built** (`ocr_output/`):
- `bunpro_deck_index.json` — **910** Bunpro grammar points, JLPT-tagged (N5–N1), the
  primary form-match + level source. (Downloaded from the public wkanki GitLab mirror.)
- `jlpt_grammar_ref.csv` — **696** JLPTsensei points (japanese/romaji/meaning/level),
  scraped by `fetch_jlpt_grammar.py`. Adds the English glosses Bunpro lacks (collision
  check). N5:76 N4:128 N3:156 N2:156 N1:180. *jlptsensei rate-limits hard — N2 p4 (~37
  rows, o-/sa- forms, redundant w/ Bunpro) was unreachable; the rest came via WebFetch.*
- Tae Kim's 62 lesson topics (in `bunpou/japanese-grammar-db`) = conceptual checklist
  for the Foundations line; lesson-title level, not form-matchable.

**Matching** (`reconcile_external.py`): Japanese-form↔Japanese-form with tolerant
variant normalization (strip 〜/～, split `/`・ alternatives, paren-optional, circled-
number ①② + superscript markers) **plus** a romaji→slug axis (our slugs are romaji).
Outputs `grammar_gap.csv`, `grammar_jlpt_diff.csv`, `grammar_match_report.csv`.
`triage_reconcile.py` → `grammar_gap_triaged.csv` (categorized) + `grammar_jlpt_fix.csv`.

**Findings:**
- **Coverage:** 601/1,075 of our nodes are externally validated; the other **474 are
  DBJG-unique** (rare/literary/classical long-tail — expected per decision #2).
- **Gaps (#15b, fill DBJG lacks):** **635 distinct** external points not in our tree.
  After triage: **519 grammar_candidate** (N1:176 N2:109 N3:111 N4:88 N5:35), **139 of
  which appear in BOTH sources** (highest-confidence add list); the rest = 78 structural
  labels, 12 demonstratives, 14 short-particle, 12 bare-kanji vocab (out of scope).
  → **This is the next enrichment batch** (see Step 4b). Verified zero false-gaps on a
  spot-check (に過ぎない→ni-suginai, つつ→tsutsu match; あっての/がてら/こととて genuinely absent).
- **JLPT-badge fixes (#15a):** **85** corrections applied where Bunpro+JLPTsensei agree
  on a level unambiguously different from ours (magnitude-1 + 2 verified jumps), audit in
  `grammar_jlpt_applied.csv`. E.g. `iru` ている N3→N5, `darou` N4→N5. JLPT is badge-only
  (#6) so this is safe; freq/family/meaning untouched.
- **Sense-collisions caught (#14/#15a):** `you` (advanced 〜よう(が/に) wrongly form-matched
  volitional よう), `yori-2` (lexical 寄り vs comparative より), `toka` (listing vs hearsay
  とか（で）), plus `ni-shite-2` (external にして='at certain conditions' ≠ our 'both~and').
  Routed to `grammar_collision_suspect.csv` / flagged in review_reason — NOT auto-changed.
- **22 low-conf high-risk nodes re-checked** (`recheck_low_conf.py`): 15 externally
  confirmed → low→med (conf dist now **640 high / 335 med / 100 low**); 7 correctly stay
  low (lexical 要る/寄り/やる/自分, dup `noni-3`, ambiguous `o-unresolved` folded into `o`).

## Step 4b — Remaining (next sessions)

1. **Gap-fill enrichment** of the 519 grammar_candidates.
   - **DONE (2026-06-02): 139 dual-source (Bunpro+JLPTsensei) candidates enriched** →
     appended to `grammar_enriched.csv` (now **1,215 records**, QA PASS, 0 hard/soft/
     dangling). These had JLPTsensei glosses so reconstruction was easy; almost all came
     back `conf=high`. Slice was N1:33 N2:44 N3:35 N4:20 N5:7. Notes: 4 `med` rows
     (denakute-nan-darou, kare-kare, dake-wa, no-mo-mottomo-da); honorific/humble rows
     tagged keigo (de-gozaimasu/gozaimasu=teineigo, irassharu/nasaru=sonkeigo,
     te-itadakemasen-ka=kenjougo); gap-fill rows carry `src_risk=gapfill`,
     `src_volumes=ext`, `src_glosses`=the external gloss for provenance. Foundation
     prereqs use `*te-form`/`*nai-form`/`*masu-stem`/`*ta-form`/`*ba-conditional`/
     `*volitional-form`; intra-batch prereqs (ni-kagiru, kara-miru-to, kiru, gozaimasu,
     te-iru, etc.) resolve. **One gotcha:** てもいい's existing slug is `te-mo-ii`
     (not `temo-ii`) — check `_used_slugs` before referencing.
   - **DONE (2026-06-02): the 380 single-source candidates** → 2 more batches.
     **(1b) JLPTsensei-only (153 rows, had glosses):** 150 enriched, 3 dropped as dups of
     the dual-source batch (janai / mitai-na→mitai-ni / temo-ii-desu→te-mo-ii). **(1c)
     Bunpro-only (227 rows, NO gloss → reconstructed from the Japanese form):** 156
     enriched, **71 dropped as dups** — these grammar points were already enriched in the
     original clean pass under a kanji/kana variant the reconciler's matcher missed
     (e.g. ながらに/からある/にとって/即ち/却って/と共に/遂に/必ずしも…). **Dedup method that
     worked:** normalize-compare each candidate's Japanese against existing
     canonical+reading (strip 〜～()・), then a second pass where `append_enriched.py`'s
     slug-uniqueness catch flags any kanji-vs-kana slug clash before writing. Reconstruction
     confidence was high — these are clean Bunpro forms, not garbled OCR. **Net: all 519
     candidates processed → 445 enriched + 74 already-covered dups dropped.**
2. **Resolve the 4 collision-suspects** — **DONE (2026-06-02).** `you` (kept N2; external
   N5 = volitional よう, a separate node), `yori-2` (kept lexical 寄り; external = comparative
   particle より = node `yori`), `ni-shite-2` (kept "both~and"; external "at age/condition"
   maps to node `ni-shite` sense 1) — all annotated as false external form-matches in
   `review_reason`. `toka` was a genuine multi-sense → **split: new `toka-2` node** for the
   hearsay 〜とか(で) (N2, family=quotation); `toka` stays listing/vague (N4). Resolutions
   logged in `grammar_collision_suspect.csv` (`resolution` column).
3. **Build one vertical slice** — **DONE (2026-06-03).** Foundations line (60 nodes,
   9 stages) + 8 materialized form-anchors + the Read-novels literary branch (22-node
   curated route over the 145-member `register⊇{literary}` filter). Generator
   `scripts/build_slice.py` → `src/data/grammar_slice.json` (in-repo since 2026-06-05;
   see SLICE.md Artifacts); static render at `/learn/japanese/grammar`. Validation
   **PASS** (82/82 slugs resolve, 0 dangling, 0 ordering violations). **Three IA findings
   in `SLICE.md`:** (a) prereq-depth (#6) collapses to ≤2 tiers — the curated **stage**
   (#9) is the layout axis, prereq edges become the faint mesh; (b) the `*`-form anchors
   are referenced 225× and must be promoted to real nodes/pages; (c) a same-surface
   dedup/sense review (て/te-2 dup vs が-subject/が-"but" split) is needed before the full
   tree — not mechanically separable. The subway-line model (#10) worked with **no new
   data model**; the register **set** tag earned its complexity.

**Prior cursor (risk):** risk pass **COMPLETE 84/84**, then +14 (regex fix) = 98/98.
Output `JengoApp/scripts/ocr_output/grammar_enriched.csv` = **92 records** (8 splits:
amari-2, datte-2, kagiri-2, kara-2, no-2, suru→o-suru/ga-suru, to→to-conditional/
to-quotative, yō→you/you-2). Confidence: 28 high / 45 med / 19 low. No duplicate slugs.
**Worklist correction:** high-risk = `risk ⊇ {collision,garble}` = **84** (the 53
`missing_only` rows are NOT high-risk — they fold into the clean pass).
**`CALIBRATION.md` written** (frozen enrichment spec — rules + romaji-reconstruction
discipline + worked examples). **Clean pilot done** (25 rows → `grammar_enrich_pilot.csv`):
**58% high / 42% need judgment** (15h/8m/3l). "Clean" = no OCR flag, NOT mechanical —
~980/1,006 rows have no English gloss, so the model reconstructs meaning from romaji +
see-also + volume. 4 latent issues found in 25 rows: hidden multi-sense (`koto`),
unflagged `¹³⁴` superscripts (`iru³`/`kureru¹`), cross-pass slug clash (`nante`→nante-2),
cross-row dup (`dake de naku`). **Agent verdict:** disciplined fan-out only — agents need
CALIBRATION.md + see-also index + used-slug list + strong model (Opus/Sonnet, never
Haiku) + scripted QA + ~15% spot-read. Naive fan-out unsafe (42%-judgment rows).

**BUG FIXED (2026-05-30):** `prep_grammar_nodes.py` `HOMOGRAPH_RE` now matches the full
superscript range `¹²³⁴⁵⁶⁷⁸⁹⁰`. Re-ran prep (non-destructive, still 1,090 nodes):
collision 64→78, high-risk **84→98**. The 14 newly-surfaced rows (de³, iru¹/³, ka/ka¹,
kureru/kureru¹, kuru¹, mono ka¹, ni¹/³, noni¹, o³, yaru¹) were then enriched — **high-risk
pass now COMPLETE 98/98 → 106 records** (38h/46m/22l, no dup slugs). Several resolved
earlier ambiguities (mono ka¹ "definitely not" pins emphatic ものか; iru¹ "exist"/iru³
要る "need" separate the conflated iru family). Clean pass to-do: **992 + 53 missing_only**.

### Calibration rules (harvested from the 84 high-risk nodes — seed for CALIBRATION.md)
1. **Potential → `family=modality`** (not `passive`); spontaneous/honorific られる → `honorific`; plain passive → `passive`. One romaji `rareru` legitimately becomes 3+ nodes by superscript.
2. **Vocab-sense drop:** when a polysemous term mixes grammar + lexical senses (suru 'do', ya 'store'/屋, iku 'go', yori 'side'/寄り, morau 'receive'), KEEP only grammar senses as nodes; a node that is *entirely* lexical → `fold_into_parent` + `freq=rare`, `jlpt=none`, `conf=low`.
3. **Auxiliary vs aspect:** benefactive てあげる/てくれる/てもらう/てやる = `auxiliary`; directional/temporal ていく/てくる/ている/てある/たことがある = `aspect`.
4. **No-gloss homograph pairs** (soko de'/², yaru/²): both senses known but the '/² → sense mapping is unrecoverable from the row → assign best-guess, `conf=low/med`, name the guess in review_reason.
5. **Merged-garble rule:** when QA `merged_suspect`/`unbalanced` fuses several patterns into one term, reconstruct + keep the PRIMARY pattern, set `conf=low`, and list the fused-in patterns in review_reason ("others need own nodes") so reconciliation re-adds them.
6. **`~2` prefix = the dictionary's homograph² of a shared base** (e.g. `~2 bakari de naku`) — pair it to node 1 via prereq + flag possible merge; don't treat as unrelated.
7. **Prereq slugs are best-effort:** write the plausible slug; `*`-prefix only known non-catalog foundations (te-form, nai-form, ba-conditional, volitional-form, counter). A post-pass resolves every prereq slug against the final node set and flips unresolved bare slugs to `*` (e.g. `to-quotative` started as `*to-quotative`, later became a real node).
8. **Particle `freq`:** core case/topic particles (は theme, が subject, を object, に dest/IO, で means/place, と 'and', も 'also', から 'from') = `essential`, `N5`; their advanced/contrastive/literary uses = separate nodes at `common`/`uncommon`. `freq` is real usefulness, NOT JLPT (JLPT is its own tag).
