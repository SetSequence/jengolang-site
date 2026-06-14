# CALIBRATION2 — Pass-2 Teaching-Content Enrichment Spec (frozen)

The **single source of judgment** for Pass-2: turning each enriched node's one-line
`meaning` + tags into the **teaching page** defined by the TREE.md content schema. Read
this in full before enriching any slice. Self-contained — you do **not** need to open
`CALIBRATION.md` (Pass-1); the few Pass-1 rules that still bind are summarized below.

- **Pass-1** (`CALIBRATION.md`, frozen, DONE) reconstructed node **metadata** →
  `grammar_enriched.csv`. That meaning/tags work is finished; don't redo it.
- **Pass-2** (this file) adds the **content layer**: Meaning → Key sentence → Formation →
  Variants → Examples → Can't-use → Confused-with → Notes, plus an optional sense layer.
- Owns: the teaching-content rubric. Page schema = `TREE.md` "Per-node content schema".
  IA = `TREE.md`. Ingestion = `GRAMMAR.md`. Pass-1 metadata rubric = `CALIBRATION.md`.

The risk here is **not** meaning reconstruction (Pass-1 fixed the meaning). It is
**slot-presence judgment** — which optional sections this specific point needs — and
**example quality**. Both are why this is a frozen spec and an Opus pass.

---

## 0. Inherited from CALIBRATION.md (still binding)

Pass-2 reads tags from the already-enriched CSV and rarely re-derives them, but when it
touches identity/tags these Pass-1 rules hold (authority = `CALIBRATION.md` §, frozen):

- **Slugs (§4):** kebab from romaji; homograph → numeric suffix; **globally unique**.
  Pass-2 normally references existing slugs (in `contrasts`/`prereqs`), not mints them. If
  a sense genuinely needs splitting into a new node, follow §3 split + §4 uniqueness.
- **Enum values:** `register` = a SET ⊆ {casual-spoken, polite-spoken, written-modern,
  literary, archaic} (§6); `keigo` ∈ {none, teineigo, sonkeigo, kenjougo} (§7); `freq` ∈
  {essential, common, uncommon, rare} = real usefulness, not JLPT (§8); `jlpt` ∈
  {N5..N1, none} (§9); `family` (§10). Keep any value you write in range.
- **Collision guard (§0/§14):** a bare form can hide senses — re-judge sense count (§4
  below) with the same enumerate-every-sense discipline.
- **confidence / review_reason (§12):** drive the non-thin gate (§5). `high` ⇒ empty
  reason; `med`/`low` ⇒ a short specific reason.

---

## 1. The core rule — presence is earned, not defaulted

The schema is a **superset of optional slots**. **Consistency lives in slot position /
colour / format** (when a section appears it is always the same place + styling).
**Presence is a per-node judgment**: include a slot **iff a learner of *this specific
point* needs it.** Not "the schema has the field" (→ don't fill it just because it
exists) and not "fill everything" (→ padding). One test, applied per slot:

> **"Would a real learner of this exact pattern be helped by this section — or is it
> filler / restating?"** If filler → omit. If genuinely helpful → include, tightly.

## 2. The two failure modes (the thing to actively avoid)

- **Over-fill (padding to look complete).** Manufacturing a "restriction" that is just
  the rule restated, or a "contrast" no learner confuses, or prose `nuance` that repeats
  the equivalents. This erodes trust and violates *streamlined*. **The presence of a
  high-value slot must be earned by a real need, never by symmetry.**
- **Under-fill (dropping the hard, high-value slots).** `restrictions` and `contrasts`
  are exactly what lazy enrichment skips — and they are the dictionary's missing feature
  + the GEO win. **If a genuine prohibition or a genuine confusable sibling exists, it is
  mandatory.** Effort is not a reason to omit.

Calibrate between these two, per slot, every node. When unsure whether a restriction/
contrast is "real," apply the learner-error test in §3.

## 3. Slot-by-slot include/omit tests

| Slot | Include when | Omit when | Guard |
|---|---|---|---|
| `equivalents` | **Always** (≥1). Multiple only when no single English word fits (は ≈ "as for / speaking of"). | — | Lead with function, not a literal gloss. |
| `nuance` (prose) | Only when *how it feels* (connotation, speaker attitude) needs a sentence a structured field would distort (わざわざ, なんて, は-topic). | **Default.** Mechanical grammar where equivalents + examples suffice. | ≤ 2 sentences. Never restate equivalents. |
| `keySentence` | **Always**, one **per sense**. Simplest natural sentence, **clean base form, no variants**. | — | This is the non-thin gate (§5). |
| `formation` | There is an attachment/conjugation rule to perform (almost all grammar). | Bare particles with nothing to conjugate (は, が) — a one-line attachment note goes in `usageSetting` instead. | Reference `*`-form anchors by slug. |
| `usageSetting` | A situational constraint beyond the register badge (written-only, male/female speech, specific social setting, keigo deployment). | The badges already say everything. | One line. |
| `variants` | Same-meaning alternate surface forms exist (なきゃ/なくちゃ/ねば; である; てる). | No common alternate form. | **Same meaning, diff form** — not senses, not separate nodes. |
| `examples` (full set) | Use varies enough that the hero under-teaches (different verb classes, the variants in action, multiple contexts). `level` grading **only** when difficulty genuinely varies. | A trivial pattern fully shown by the hero. | **Never force difficulty tiers.** Examples must *naturally* demonstrate the meaning (§4 quality bars). |
| `restrictions` ("can't use") | A learner would naturally produce a **wrong** sentence without the warning (aspect/tense clash, subject limits, illegal combination). | No notable prohibition exists. | **Learner-error test.** A real wrong sentence, not the rule restated. |
| `contrasts` ("confused with") | ≥1 sibling is **genuinely confusable** (the conditionals; ている vs てある; は vs が). Seed from same-`family`. | Nothing is confusable. | Each carries a crisp `distinction`; link the sibling `slug`. Never manufacture. |
| `notes` | A one-off that fits no other slot (memory-aid etymology, a fixed set phrase, an irregular exception). | **Default.** | Residual only — never a dumping ground. |

## 4. Quality bars + the senses-first decision

**Senses first (before any slot): how many senses?** (Pass-1 may have set `senses`; re-judge.)
- **Multi-sense** = identical form + formation, ≥2 meanings a learner would confuse or
  need separately (ている ongoing / resulting state). → `senses[]`, one
  `equivalents`/`keySentence`/`examples` **per sense**; `formation`/`restrictions`/
  `contrasts`/`notes` stay node-level, each item optionally pinned via `sense:<label>`.
- **Single-sense** = flat fields. A "second sense" that is only register/politeness →
  that's `variants`; a different form/particle → a **separate node**. Don't inflate count.

**Quality bars:**
- **Streamlined (the user's #1 rule).** Every field is exactly what the reader needs. No
  hedging, no restating the meaning in three slots. Cut a sentence that adds nothing.
- **Examples must *demonstrate*, not just *contain*.** The sentence should make the
  meaning obvious **before** the reader sees the English. Use realistic modern Japanese;
  **vary the vocabulary and context across examples** (don't reuse the same verb). English
  is natural, not a literal gloss.
- **Furigana on every kanji** via `漢字{かんじ}` markup, reading verified. (`子{こ}ども`.)
- **Hero = the simplest base form.** No contractions/variants in the key sentence.
- **Grade only when warranted** (`level`) — forcing intro/core/advanced on a flat pattern
  is ramming the rubric (§1).

## 5. Confidence & the non-thin gate (noindex flip)

- A Pass-1 `confidence=low` node (shaky meaning / `canonical=""`) → fill
  **conservatively**: `equivalents` + `keySentence` + `formation` only; **do NOT invent**
  restrictions/contrasts/nuance for a pattern you're unsure of. Carry the uncertainty in
  `review_reason`; it **stays `noindex`**.
- **Non-thin gate** (flips `noindex:false`): a key sentence **per sense** AND a populated
  `examples` set (≥3 across the node, or ≥2 per sense for multi-sense), AND `equivalents`.
  Below that, the page stays in the tree map but `noindex` (TREE SEO posture).
- Fill order is the **curated path first** (Foundations + active goal routes) so those
  clear the gate and index; long-tail later.

## 6. Worked examples (slot-presence in action)

Each shows which slots **fire** vs stay empty — the judgment, not just the content.

**A. 〜ている — "everything fires" (multi-sense, the dense case)**
`senses ✓✓ · variants ✓ · examples ✓ · restrictions ✓ · contrasts ✓ · nuance ✗ · notes ✗`
- senses: **①ongoing action** — `equiv` "≈ -ing / is ~ing"; hero `子{こ}どもが公園{こうえん}で遊{あそ}んでいる。` "A child is playing in the park." **②resulting state** — `equiv` "is (in the state of) ~"; hero `兄{あに}は結婚{けっこん}している。` "My brother is married."
- formation (node-level): `*te-form` + いる. usageSetting omitted (badges cover it).
- variants: `てる` (casual contraction — `子{こ}どもが遊{あそ}んでる`).
- restrictions: *Punctual verbs* (知{し}る, 死{し}ぬ, 結婚{けっこん}する) take **only** sense ②, never ①: `知{し}っている` = "know," never "is knowing." → pinned `sense:①`.
- contrasts: `te-aru` — 〜てある = state from a **deliberate** act (`窓{まど}が開{あ}けてある`) vs ている intransitive natural state (`窓{まど}が開{あ}いている`).
- nuance ✗ (equivalents + the two heroes already carry it), notes ✗.

**B. 〜つつ — "moderate / lean" (single-sense, literary)**
`equivalents ✓ · hero ✓ · formation ✓ · restrictions ✓ · contrasts ✓ · senses ✗ · variants ✗ · nuance ✗ · notes ✗`
- equiv "while ~ing (literary)"; hero `彼{かれ}は本{ほん}を読{よ}みつつ、お茶{ちゃ}を飲{の}んだ。` "He drank tea while reading."
- formation: `*masu-stem` + つつ. usageSetting: "written/formal; in speech use ながら."
- restrictions: both actions share **one subject** (learner-error: different-subject → wrong).
- contrasts: `nagara` — same "while," but ながら is neutral/spoken, つつ literary. (つつも concessive → its own node, link via `related`, not a sense.)
- senses/variants/nuance/notes ✗ — nothing real to add; **leaving them empty is correct, not lazy.**

**C. は (topic particle) — "nuance + contrast dominant" (particle shape)**
`equivalents ✓ · nuance ✓ · hero ✓ · restrictions ✓ · contrasts ✓ · formation ~ · variants ✗ · senses ✗`
- equiv "as for ~ / speaking of ~" (not directly translatable).
- **nuance FIRES** (rare): one tight para on topic-vs-subject + the contrastive feel — a structured field can't carry it.
- hero `私{わたし}は学生{がくせい}です。` "I'm a student."
- formation light → `usageSetting`: attaches to a noun/phrase; **replaces** が/を, **stacks** after others (には/では).
- restrictions: a question-word **answer** takes が, not は (`誰{だれ}がした → 私{わたし}がした`, not 〜は). Learner-error test passes.
- contrasts: `ga` — **the** canonical は vs が confusion; crisp `distinction` (topic/old-info vs subject/new-info).
- variants ✗; senses ✗ (contrastive-は → a `note` or, if Pass-1 split it, a separate node — don't inflate here).

**D. 〜なり "as soon as" — "low-confidence → minimal" (conservative fill)**
`equivalents ✓ · hero ✓ · formation ✓ · everything else ✗ · stays noindex`
- Pass-1 `confidence=med/low` (bare romaji, multi-sense family). equiv "the moment ~ / as soon as ~"; one cautious hero; formation: dictionary-form + なり.
- restrictions/contrasts/nuance **✗ — not invented** for an uncertain pattern.
- `review_reason`: "as-soon-as なり reconstructed; verify vs listing なり〜なり." **Stays `noindex`** until verified — fails the gate by design.

## 7. Pass-2 QA hooks

- **Furigana lint:** every kanji in `keySentence`/`examples` has a `{reading}`; readings parseable.
- **Gate check:** `noindex:false` ⇒ key sentence per sense + examples threshold met (§5); else flag.
- **Over-fill scan:** a `restrictions`/`contrasts` entry whose text merely restates the
  meaning/formation → flag as padding (§2).
- **Under-fill scan:** a node in a high-confusion `family` (conditional, aspect, particle)
  with **zero** `contrasts`, or an aspect/tense pattern with zero `restrictions` → flag for
  a second look (likely a dropped high-value slot).
- **Sense consistency:** every `sense:<label>` on a node-level item matches a `senses[].label`.
- **Spot-read ~10%** against §1–§4.
