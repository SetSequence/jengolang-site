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

## ► Orientation (read this first, 2026-06-14)

All design **LOCKED** (this doc); the Pass-2 teaching-content fill is **in progress**.
For **"what now"** — the current frontier, the per-pass operating loop, the gotchas, and
the cluster-prep subagent pattern — read **`PASS.md`** (the slim, evolves-each-pass cursor).
Pass-1 metadata enrichment is **done**; the dated build log and the Pass-1 handoff are
archived in **`HISTORY.md`** (history, not needed for forward work).

This file (`TREE.md`) now owns only the **durable design**: locked decisions, the per-node
content schema, app-funnel posture, and render tech. `CALIBRATION2.md` owns the Pass-2
judgment rubric; `CALIBRATION.md` the Pass-1 one. `GRAMMAR.md` owns ingestion;
`JENGOLANG.md` the wider site/SEO plan.

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

---

## History & operating docs

- **`PASS.md`** — current frontier + cursor + the per-pass loop + gotchas + subagent pattern (slim, evolves each pass).
- **`CALIBRATION2.md`** — Pass-2 teaching-content judgment rubric (frozen).
- **`CALIBRATION.md`** — Pass-1 metadata rubric (frozen, done).
- **`HISTORY.md`** — dated Pass-2 build log + Pass-1 enrichment handoff (archived from this doc).
- **`SLICE.md`** — vertical-slice IA findings.
