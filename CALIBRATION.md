# CALIBRATION — Grammar-Node Enrichment Spec (frozen)

The **single source of judgment** for enriching `grammar_nodes.csv` → node records.
Read this in full before enriching any slice. It exists so that every enricher —
the main thread *or* a fan-out agent — applies the **same** calibration, because the
risk in a long pass is not OCR, it is **inconsistent judgment** (freq/family/confidence
drift) and **confident wrong meaning reconstruction**.

Owns: the enrichment rubric. Design/IA = `TREE.md`. Ingestion = `GRAMMAR.md`. Output
schema also encoded in `JengoApp/scripts/enrich_grammar_nodes.py` (`SCHEMA`/`OUT_FIELDS`).

---

## 0. The thing that makes this hard

**~980 of 1,006 "clean" rows have NO English meaning** — only the romaji term, a
volume (B/I/A), and (for 603) a `<see-also>` pointer. "Clean" means *no OCR
collision/garble flag* — NOT "easy." You are **reconstructing the grammar point from
the romaji string**. A bare romaji term is itself a collision risk (`nari` = listing
なり〜なり / "as soon as" 〜なり / classical copula なり). **Apply the collision guard to
EVERY row, not just pre-flagged ones.**

---

## 1. How to enrich one row (the loop)

1. **Read the term as romaji** and silently **enumerate every grammar sense** you know
   for it. (Lexical/vocabulary senses do not count — see Rule 2.)
2. **Disambiguate** using, in priority order: any **superscript** (`¹²³ ' ~2` = the
   dictionary already split this homograph — respect the split); the **`<see-also>`**
   pointer(s) (what it is grouped with names the sense — `darō <de arō>` → だろう
   conjecture); the **English gloss** if present (pins the sense); the **volume**
   (B=Basic/early, I=Intermediate, A=Advanced/rare/literary — a difficulty + sense
   signal).
3. If exactly one sense fits → enrich it, `confidence` by Rule 9.
4. If **>1 grammar sense** still plausibly fits the SAME row → set `confidence`
   low/med and name the ambiguity in `review_reason`, even if you have a default.
   **Never silently pick one sense for an ambiguous row.**
5. If the row genuinely holds **multiple distinct grammar patterns** (not OCR-fused,
   genuinely polysemous like `kagiri`, `yō`) → **emit one record per grammar sense**
   (Rule 3), distinct slugs.

---

## 2. Vocab-sense drop (what is NOT a node)

This is a **grammar** tree. A node is a *teachable grammar pattern*, not a word.
- A polysemous term mixing grammar + lexical senses → keep ONLY the grammar senses
  (`suru`: keep お〜する / がする, drop "do/play/cost"; `ya`: keep listing や, drop 屋
  "store"; `iku`: keep ていく, drop "go"; `yori`: keep より "than", drop 寄り "side").
- A row that is **entirely lexical** (a plain verb/noun, no grammatical function) →
  `fold_into_parent` = the parent term, `freq=rare`, `jlpt=none`, `confidence=low`,
  `review_reason` = "lexical, not grammar — candidate to drop". Don't silently delete.
- Giving/receiving verbs as MAIN verbs (あげる/くれる/もらう "give/receive") = borderline;
  keep as `family=other` nodes (they have grammatical viewpoint behavior). Their
  て-form auxiliaries (てあげる…) are separate `family=auxiliary` nodes.

---

## 3. Splitting & folding

- **Split** (one source row → several node records): genuine multi-sense terms.
  One record per grammar sense, each a distinct slug (`kagiri`, `kagiri-2`).
- **Fold** (`fold_into_parent` set): a row that is a trivial compositional add-on to a
  parent you'd teach as one note, or an entirely-lexical row (Rule 2).
- **Merge-dup**: identical terms are already merged by `prep_grammar_nodes.py`. If you
  spot two *different* rows that are the same pattern (e.g. `ga` advanced vs `ga²`
  "but"), do NOT merge across rows yourself — flag the suspected merge in
  `review_reason`; reconciliation handles cross-row merges.

---

## 4. Slugs (node identity = URL)

- kebab-case from the romaji term: lowercase; spaces, `~`, and parenthesised tails →
  hyphens (`bakari ni`→`bakari-ni`, `aida (ni)`→`aida-ni`, `~de mo`→`de-mo`); strip
  other punctuation.
- **Homograph markers** (`¹ ² ³ ' ~2`): drop the marker, disambiguate with a numeric
  suffix in encounter order (`aru`/`aru-2`/`aru-3`).
- **MUST be unique across the ENTIRE enriched file**, not just your slice. On collision
  with an existing slug (incl. another pass's — e.g. two `nante` rows), append the
  next free `-N`. The QA pass re-checks global uniqueness.

## 5. canonical / reading / meaning

- `canonical`: standard Japanese form (kana, or kanji+kana). `""` if you cannot
  reconstruct it confidently (then `confidence=low`).
- `reading`: full kana reading.
- `meaning`: ONE concise English line. No dictionary verbosity. Lead with the function.
- `senses[]`: only when ONE node keeps >1 closely-related use (の possessive+nominalizer);
  `{label, canonical, meaning}` each. Normal single-sense node → `[]`.

## 6. register (a SET)

Media where the pattern is actually used, ⊆ {casual-spoken, polite-spoken,
written-modern, literary, archaic}. Core grammar used everywhere =
[casual-spoken, polite-spoken, written-modern]. Formal/written-leaning → drop
casual-spoken. Literary-only → [literary] (+[archaic] if classical).

## 7. keigo ∈ {none, teineigo, sonkeigo, kenjougo}

`none` unless the pattern IS honorific/humble/polite. お〜する/ご〜する = kenjougo;
honorific られる / お〜になる = sonkeigo; です/ます = teineigo.

## 8. freq ∈ {essential, common, uncommon, rare}

**Real usefulness to a modern self-study learner — NOT JLPT** (JLPT is its own tag).
- `essential`: core particles &早期 grammar everyone needs (は/が/を/に/で/と/も/から,
  て-form aux, ている, plain past).
- `common`: frequent in real spoken/written Japanese.
- `uncommon`: appears but you can go a while without it.
- `rare`: literary/archaic/formal-only, niche (であれ〜であれ, にして"both~and").

## 9. jlpt ∈ {N5..N1, none}

Best-guess exam level; `none` if not a JLPT point. Independent of `freq`.

## 10. family (single best) ∈ {conditional, causative, passive, aspect, modality,
quotation, connective, nominalizer, particle, auxiliary, adverbial, honorific, copula,
counter, interjection, other}

Decisions that recur:
- **Potential** (られる "can", 〜得る) → `modality` (there is no "potential"; NOT passive).
- **Passive** られる → `passive`. **Spontaneous/honorific** られる → `honorific`.
- **Benefactive** てあげる/てくれる/てもらう/てやる → `auxiliary`.
- **Directional/temporal aspect** ていく/てくる/ている/てある/たことがある/ところだ → `aspect`.
- **Case/binding particles** (は が を に で と も の …) → `particle`.
- **Conjecture/appearance/advisability** (そうだ/ようだ/らしい/べき/ものか) → `modality`.
- **Clause connectors** (が/けど/のに/ので/ば-result/から-reason listing と/や) → `connective`
  or `particle` (use `connective` when it joins clauses, `particle` when it binds nouns).
- **Nominalizers** (の/こと/ところ-as-nom) → `nominalizer`.
- Entirely-lexical fold rows → `other`.

## 11. candidate_prereqs (0–4, slugs)

- The **slug** of each prerequisite node ("you must understand X before Y").
- `*`-prefix ONLY known **non-catalog foundations**: `*te-form`, `*nai-form`,
  `*masu-stem`, `*ta-form`, `*ba-conditional`, `*volitional-form`, `*counter`, `*toka`.
- Otherwise write the plausible catalog slug. A **post-pass resolves every prereq slug
  against the final node set** and flips unresolved bare slugs to `*` (a prereq may
  become a real node later in the pass, e.g. `*to-quotative` → `to-quotative`). Do not
  block on resolution.

## 12. confidence ∈ {high, med, low} + review_reason

- `high`: well-known, unambiguous, meaning + tags certain.
- `med`: mostly sure; minor doubt (reconstructed reading, formal nuance, homograph
  split you're fairly sure of).
- `low`: obscure romaji, no-gloss with multiple plausible senses, garble residue,
  `canonical=""`, suspected cross-row merge, or vocab-fold.
- `review_reason`: **med/low MUST carry a short, specific reason**; high SHOULD be
  empty but MAY carry a brief clarifying cross-ref note (e.g. "てくれる = kureru-2").
  A flagged row is cheap; a confident wrong one is expensive.

---

## 13. Known prep gaps → QA must catch

1. **`prep_grammar_nodes.py` homograph regex missed `¹ ³ ⁴`** (only `² ' 2`). So
   superscripted homographs (`iru³`, `kureru¹`) sit UNFLAGGED in the clean set. Treat
   ANY trailing superscript digit as a homograph marker and disambiguate.
2. **Latent multi-sense** rows with a single/empty gloss were not collision-flagged
   but are polysemous (`koto`, `nari`, `nante`). The Rule-1 loop catches these.
3. **Stray tokens in terms**: page numbers (`tokoro o 312`), leading `>`/`>>`/`-`,
   tripled OCR (`to to to …`) — strip before slugging; reconstruct the pattern.

## 14. Post-merge QA checklist (the catch-net for fan-out drift)

> Implemented by **`JengoApp/scripts/qa_grammar_nodes.py`** — run it over the
> high-risk file + every shard together:
> `python3 scripts/qa_grammar_nodes.py grammar_enriched.csv shard_*.csv --source grammar_nodes.csv`
> Hard errors (exit 1): bad enum, duplicate slug, dangling prereq, missing high-risk
> node. Pending prereqs (unenriched-but-real) are reported, not failures.


- Every enum field valid (register subset, keigo/freq/jlpt/family in range).
- **Slug global uniqueness** (across all shards + the high-risk file).
- Every `candidate_prereqs` slug resolves to a node OR is `*`-prefixed; flip unresolved.
- `confidence=high` rows have empty `review_reason`; `low` rows have one.
- Distribution sanity: flag a shard whose freq/family/jlpt histogram deviates sharply
  from the others (a sign one enricher drifted).
- Re-scan for **superscript terms** and **bare romaji with >1 known sense** that came
  back `high` with no senses[] — likely missed collisions.
- Spot-read a random ~10% of each shard against this spec.

---

## 15. Worked examples

| term (romaji) | signal | → node |
|---|---|---|
| `darō <de arō>` (I, no eng) | see-also であろう | だろう, conjecture "probably", modality, common, N4 |
| `tsutsu` (no gloss, missing_only) | bare romaji | 〜つつ, "while ~ing / although", connective, uncommon, N2, literary-leaning |
| `te mo ii` (B, no gloss) | bare | 〜てもいい, permission "may ~", modality, essential, N5, prereq `*te-form` |
| `kureru¹` (B, "gives to me") | superscript¹ + gloss | くれる, giving toward speaker, other, essential, N5; てくれる = separate auxiliary node |
| `gachi <kirai ga aru>` (A\|I) | see-also "tendency" | 〜がち, "tend to / prone to", adverbial, uncommon, N2 |
| `nari` (A, no gloss) | bare, multi-sense | LOW conf — enumerate なり〜なり / 〜なり"as soon as" / copula; flag ambiguous |

---

## Pass-2 (teaching content) lives in CALIBRATION2.md

This file (Pass-1, frozen, DONE) governs **node metadata** reconstruction →
`grammar_enriched.csv`. The **teaching-content** enrichment (meaning + tags → the full
TREE.md content schema: Meaning → Key sentence → Formation → Variants → Examples →
Can't-use → Confused-with → Notes + sense layer) is a **separate job** with its own
frozen spec: **`CALIBRATION2.md`**. Pass-2 enrichers read that file (self-contained);
they do not need to reload this one.
