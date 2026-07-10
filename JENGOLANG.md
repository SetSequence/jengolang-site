# JENGOLANG.md — jengolang.com Hub Plan

## Vision
jengolang.com becomes a language learning content hub: grammar guides, vocab lists, and SEO-ranked articles that funnel readers into the Jengo app. The app moves to app.jengolang.com. Revenue via non-intrusive display ads on content pages only (never in the app).

---

## Architecture

### Domain Structure
| URL | Purpose |
|-----|---------|
| `jengolang.com` | Hub home page |
| `jengolang.com/jengo` | Jengo app marketing / showcase landing page |
| `jengolang.com/learn/[language]/grammar/[slug]` | Grammar guides |
| `jengolang.com/learn/[language]/vocab/[slug]` | Vocab lists |
| `jengolang.com/learn/[language]` | Language index |
| `app.jengolang.com` | Jengo app (current Railway deploy) |
| `app.jengolang.com/privacy` | Jengo privacy policy (lives on Railway, not hub) |

Language segment is required in all content paths — designed for multi-language from day one, Japanese first.

### Tech Stack
- **Content site**: Astro — static output, deploys to Cloudflare Pages (free tier)
- **App**: FastAPI on Railway (unchanged), served at `app.jengolang.com`
- **Routing**: Cloudflare handles subdomain split — `app.*` proxies to Railway, root goes to Cloudflare Pages
- **Content format**: Markdown/MDX files in `content/` directory, version-controlled in a new repo

### Repo Structure (new repo: `jengolang-site`)
```
jengolang-site/
├── src/
│   ├── pages/
│   │   ├── index.astro              # Hub home page
│   │   ├── jengo.astro              # Jengo app showcase / marketing landing page
│   │   └── learn/
│   │       └── [language]/
│   │           ├── index.astro      # Language hub page
│   │           ├── grammar/
│   │           │   └── [slug].astro # Grammar article template
│   │           └── vocab/
│   │               └── [slug].astro # Vocab list template
│   ├── components/
│   │   ├── Header.astro
│   │   ├── Footer.astro
│   │   ├── ArticleLayout.astro
│   │   ├── VocabTable.astro
│   │   └── AppCTA.astro             # "Try it in Jengo" call-to-action
│   └── layouts/
│       ├── BaseLayout.astro
│       └── ContentLayout.astro
├── content/
│   └── japanese/
│       ├── grammar/
│       │   └── *.md
│       └── vocab/
│           └── *.md
└── public/
```

---

## Pages

### 1. Hub Home (`jengolang.com`) — BUILT 2026-07-09
The root is **not** an app-marketing page anymore — it's the **Jengolang hub** (the
"1B toolkit-led" Claude-design handoff, ported into `src/pages/index.astro`). It presents
the whole service, then funnels to the app promo. Story-mode framing is gone.

**What it is:** a dark toolkit hero — *"Everything for Japanese, in one place."* — with a
phone mockup showing the in-app toolkit (Dictionary / Flashcards / Grammar / Train, tiles
auto-cycle), then a "rest of Jengolang" row of discoverable web tools.

**Tools row (honest state, no Live/Soon badges):**
- **Grammar** — the one real web tool → `/learn/japanese/grammar`
- **Dictionary** — tagged **"In app only"** → links to `/jengo` (no web tool yet)
- **Word lists** — tagged **"In app only"** → links to `/jengo` (no web tool yet)

**Key routing decision:** every "Open Jengo" CTA points to **`/jengo`** (the promo), *not*
straight to `app.jengolang.com`. The hub shows everything first; the promo shows platforms
and converts. Privacy stays external (`app.jengolang.com/privacy`).

Built to the existing `grammar/index.astro` idiom: `:root` oklch tokens, `is:global` style,
real `<head>` with `canonical` + `description` + WebSite JSON-LD, `prerender`, responsive,
`prefers-reduced-motion` guards.

### 1a. Jengo App Promo (`jengolang.com/jengo`)
The app-marketing / conversion page — screenshot-forward, one purpose: convert. This is the
destination of the hub's "Open Jengo" CTAs. **Still stale** (old story-mode copy); rewrite
brief is `PROPOSED-NEW-MARKETING.md` (section-by-section + paste-ready copy from
`JengoApp/docs/Appstore-docs.md`). Caden redesigns via Claude design with current App Store
screenshots.

**Visual reference:** Day One (dayoneapp.com) — screenshot-forward, direct feature language, no sparkly copy, secondary CTA before verbose sections. Warmer than Day One: use Jengo app color theme, add icons alongside feature descriptions.

**Page structure (in order):**
1. Hero — headline + one-line description + primary CTA (App Store / `app.jengolang.com`) + iOS App Store badge
2. Platform strip — browser / iOS / (Android future); instant signal that it's multiplatform
3. Features — icon + short direct label + one sentence each. No marketing fluff.
4. Screenshots — app UI doing real work, not abstract graphics
5. Secondary CTA — before social proof, catches people who are already convinced
6. Creator note — photo of Caden + short personal story: lived in Japan 2 years studying, kept drowning in flashcards but reading alone didn't build vocabulary fast enough; built Jengo to solve that gap
7. User reviews / social proof
8. Footer — links to grammar hub, about, privacy

**Tagline candidates (pick during build):**
- "The Japanese dictionary and flashcard app that works offline."
- "Look it up. Lock it in."
- "Your dictionary and your flashcards, one offline loop."

**Core message to convey:** Jengo IS a dictionary and a flashcard app — the loop competitors make you cobble together from jisho.org + Anki. Look a word up, send it straight to spaced-repetition flashcards, and review anywhere because it all works offline. One tool instead of two. Target user is a self-study learner past the very basics — not being taught grammar or kana, just building and retaining vocabulary.

At-level reading practice (stories generated around the words you're learning, for mining new words back into flashcards) is the **paid layer on top (Pro)** — not the pitch. Lead with the dictionary + flashcards loop; reading is what Pro adds once that loop is stable.

> Identity decision-of-record: JengoApp `GAMEPLAN.md` §1 — "Dictionary + Flashcards toolkit," offline is the *how*, AI reading is the *paid tier*. **Do not revive the old "reader" / "vocabulary woven into stories" / "in context" framing** — that was the pre-pivot story-mode identity and is retired.

**Design rules:**
- Light mode, not sterile white — pull accent colors from Jengo app palette
- Icons on every feature item (SVG, no emojis)
- Screenshots carry the content weight; body copy stays short
- No stock photos, no abstract illustrations
- Mobile-first
- No dark mode (app doesn't have one yet)

### 2. Grammar Guide Pages (`/learn/japanese/grammar/[slug]`)
Each article targets one grammar point or JLPT-level concept.

**Grammar category structure (in reading order):**
1. **Pre-beginner** — hiragana, katakana, basic conjugation. Not grammar per se; link out to established resources (e.g. Tofugu). Not built on-site.
2. **Essentials** — non-negotiable grammar that must be understood before anything else can be explained. Other beginner explanations will reference these. Exact contents defined after reviewing the source PDF.
3. **Ranked** — all remaining grammar ordered by frequency/usefulness, most useful first. JLPT level is metadata (helps learners gauge exam relevance) not the primary sort key.
4. **Rare** (tentative) — grammar that exists but is almost never used in speech or on the exam.

**Article structure:**
- Title (the grammar pattern, e.g. "〜ている — Ongoing Actions and States")
- Category tag + JLPT level tag
- Plain-English explanation
- Formation table (verb forms, conjugation)
- 5–10 example sentences with furigana and English
- Exceptions and special notes
- "See also" links to related grammar
- "Practice this in Jengo" CTA at the bottom

**Content generation:** LLM-generated in batches to avoid context rot. Fix errors on report. For patterns where generation is unclear, reference the source book.

**Frontmatter schema:**
```yaml
title: string
description: string        # used for meta description
category: essentials | ranked | rare
jlpt: N5 | N4 | N3 | N2 | N1
rank: number               # sort order within ranked category
slug: string
tags: string[]
related: string[]          # slugs of related articles
```

### 3. Vocab List Pages (`/learn/japanese/vocab/[slug]`)

**Sources and pipeline:**
- N5–N3: existing Jengo word lists
- N1–N2: PDF indexes (OCR → clean → merge with Jengo N1/N2 lists → deduplicate → sanitize)
- Deduplication rule: keep the lower (easier) level when a word appears in multiple lists
- If the PDF-sourced N1/N2 lists are significantly larger than Jengo's current lists after merge, publish both a standard list and an extended list (e.g. N2 and N2+) side by side on the same page

**Page structure:**
- Title + description
- Static preview table: word, reading, meaning (first ~50 entries)
- Download section — CSV, Anki (`.apkg`), JSON; PDF as a possible future addition
  - If extended list exists: N2 and N2+ downloads shown side by side
- "Add to Jengo" deep-link (future feature — add to app backlog when site has traction)

### 4. Language Index (`/learn/japanese`)
Overview page for Japanese content. Lists all grammar guides (organized by JLPT level) and vocab lists. Acts as a hub for internal linking — important for SEO.

---

## SEO Strategy

### On-Page
- Every article has a unique `<title>` and `<meta description>` targeting a specific query
- Structured data (JSON-LD): `Article`, `FAQPage` where appropriate
- Furigana rendered as `<ruby>` tags — crawlable, accessible
- Internal linking: every article links to 2–3 related articles + language index
- Canonical URLs set on all pages

### Crawlability infrastructure — SET UP 2026-07-09
- **`site: 'https://jengolang.com'`** set in `astro.config.mjs` (required for absolute sitemap URLs).
- **`@astrojs/sitemap`** integration installed → build emits `sitemap-index.xml` + `sitemap-0.xml`
  (all prerendered pages: `/`, `/jengo`, every grammar page). Note the Cloudflare adapter writes
  these under `dist/client/`; SSR-only routes aren't included (nearly everything is prerendered).
- **`public/robots.txt`** allows all crawling and points to `sitemap-index.xml`.
- Still manual (Google Search Console, not in repo): submit the sitemap; "Request indexing" on `/`.

### Serving vs. indexing — the stale old-app results
Searching `jengolang.com` can still surface a **very old version of the app**. This is **not**
the server — the root serves the new hub, and all old app deep-links (`/login`, `/dictionary`,
`/decks`, …) correctly **404**. It's **Google's stale index**: pre-migration the app lived at the
root and Google cached it there; those URLs now 404, so Google shows its old snapshot until it
recrawls. The sitemap + robots above are the recrawl nudge; finish in Search Console (submit +
Removals on the old app URLs).
- **Optional forwarding:** 301 the known old app deep-links → `app.jengolang.com/...` via
  `public/_redirects` so Google hands its stale entries to the new home. Needs the authoritative
  old-path list; a `/*` splat would collide with the marketing/grammar routes — list explicit paths.
- **Bug:** the existing `jengolang.com/app` redirect (a Cloudflare **dashboard** Redirect Rule,
  not in this repo) appends the path → lands on `app.jengolang.com/app` instead of the app root.
  Fix in the Cloudflare dashboard.

### Target Query Types
| Query type | Example | Page type |
|-----------|---------|-----------|
| Grammar lookup | "〜ている grammar" | Grammar article |
| JLPT prep | "JLPT N5 grammar list" | Grammar index or vocab list |
| Learning method | "best way to learn Japanese" | Landing or hub page |
| Vocab lookup | "Japanese weather words" | Vocab list |

### Content Priority (Phase 1 — Japanese)
Start with JLPT N5 and N4 — highest search volume from beginners, lowest competition compared to N2/N1.
1. All N5 grammar points (~80 articles)
2. All N4 grammar points (~150 articles)
3. JLPT N5 and N4 vocab lists
4. 10–15 thematic vocab lists (high search volume topics)

### GEO (Generative Engine Optimization)
AI search (ChatGPT, Gemini, Perplexity) tends to cite pages that:
- Directly answer a specific question
- Have clear, structured formatting (tables, numbered steps)
- Are linked to from other authoritative pages

The grammar article format above is designed to satisfy this. No extra work needed beyond quality content.

---

## Ads Strategy

- **Platform**: Google AdSense (or Ezoic once traffic justifies it — Ezoic pays higher RPM)
- **Placement**: Content pages only — never on the app, never on the landing page
- **Format**: One banner below the article header, one at the end — no interstitials, no pop-ups
- **Revenue expectation**: $1–5 CPM. Meaningful revenue (~$500+/mo) requires ~100k monthly page views. Treat as long-term, not near-term.

---

## Migration Plan (jengolang.com → app.jengolang.com)

1. ✓ Add `app` CNAME in Cloudflare pointing to the Railway app
2. Deploy new landing page to Cloudflare Pages at `jengolang.com`
3. Set up redirect: `jengolang.com/app` → `app.jengolang.com` (for any old links)
4. Update all in-app links and email templates that reference `jengolang.com` to `app.jengolang.com`
5. Add a one-time banner in the app notifying existing users of the new URL

---

## Roadmap

### Phase 0 — Infrastructure (1–2 days)
- [x] Create new GitHub repo (`jengolang-site`) — separate from the Jengo backend repo
- [x] Init Astro project inside it (`npm create astro@latest`)
- [x] Connect repo to Cloudflare Pages (Dashboard → Pages → Connect to Git)
- [x] Configure Cloudflare: `app.jengolang.com` CNAME → Railway, `jengolang.com` → Cloudflare Pages
- [~] Set up redirect: `jengolang.com/app` → `app.jengolang.com` — exists as a dashboard Redirect Rule but appends `/app` (lands on `/app`, not the app root); fix in dashboard. Old app deep-links still 404 (see SEO → Serving vs. indexing).

### Phase 1 — Hub Home + App Promo (2–3 days)
- [x] Run `/impeccable teach` to generate PRODUCT.md — impeccable installed globally at `~/.claude/skills/impeccable/`
- [x] Build `jengolang.com` hub home (`index.astro`, 1B toolkit-led, 2026-07-09) — replaces the old story-mode landing
- [x] Mobile-first layout (hub is responsive, hero stacks, reduced-motion guarded)
- [x] "Open Jengo" CTAs wired to `/jengo` (the promo), which in turn converts to `app.jengolang.com`
- [ ] Rewrite the `/jengo` app promo off story-mode copy (see §1a + `PROPOSED-NEW-MARKETING.md`)
- [ ] iOS App Store badge on `/jengo` (link live after App Store submission)
- [ ] Creator note section with photo (Caden, 2 years in Japan, built Jengo to solve the flashcard-vs-reading gap) — on `/jengo`

### Phase 2 — Content Architecture (2–3 days)
- [ ] Build Astro content templates (grammar article, vocab list, language index)
- [ ] Implement MDX frontmatter schema
- [ ] Add `AppCTA` component to all content pages
- [ ] Set up JSON-LD structured data
- [x] Set up sitemap generation — `@astrojs/sitemap` + `site:` + `robots.txt` (2026-07-09; see SEO → Crawlability)

### Phase 3 — Japanese Content (ongoing, weeks–months)
- [ ] Write all N5 grammar articles (~80)
- [ ] Write all N4 grammar articles (~150)
- [ ] Publish JLPT N5 and N4 vocab lists
- [ ] Publish 10 thematic vocab lists
- [ ] Submit sitemap to Google Search Console

### Phase 4 — Monetization
- [ ] Apply for Google AdSense (requires live content — do this after Phase 3 has ~20+ articles)
- [ ] Add ad slots to content layout
- [ ] Monitor RPM, evaluate Ezoic at 10k+ monthly sessions

### Phase 5 — Additional Languages
- [ ] Replicate content architecture for Korean, Mandarin, etc.
- [ ] Translate/create equivalent grammar guides
- [ ] Update language index page

---

## Open Questions
- Grammar essentials: exact contents TBD after reviewing source PDF
- App Store submission timeline affects how prominent download CTAs are on Phase 1 landing page
- PDF download format for vocab lists: deferred, revisit if demand is clear

---

## N1/N2 Vocab PDF Pipeline

Source: scanned PDFs (image-only, no text layer). Scripts live in `scripts/`.

### Scan Settings
- OCR: Google Cloud Vision `DOCUMENT_TEXT_DETECTION`, `languageHints: ["ja"]`
- Render: PyMuPDF (`fitz`) at 1.5× zoom before sending to Vision
- Output: `scripts/ocr_output/{n1,n2}_raw.json` (one object per page)

### Index Page Layout
Each page has 3 columns of word entries:
- Col 1 word blocks: x ≈ 46 (some OCR drift to x ≈ 219–221)
- Col 1 page numbers: x ≈ 200–235
- Col 2 word blocks: x ≈ 228–280
- Col 2 page numbers: x ≈ 390–430
- Col 3 word blocks: x ≈ 440–500
- Col 3 page numbers: x ≈ 580–640
- Column boundary col1/col2: **x < 225** (raised from 215 to capture col1 OCR-drift entries)
- Column boundary col2/col3: x < 420

### Entry Format
```
[□ | ■ | | | [] [~] hiragana_reading [kanji] page_number
```
- `□`/`■` are entry bullet markers; `|` and `[` are common OCR artifacts for `□`
- Prefix/suffix words use `~`: `~元`, `はん~`
- Page number always follows the complete entry (reading + optional kanji)
- Kanji sometimes appears in a separate block directly below the reading

### Header Cutoff (per page)
- Page 1 (index title present): ignore blocks with y < 155
- Pages 2+: ignore blocks with y < 65

### Section Headers
- Single hiragana character from the full syllabary (あ–ん + dakuten/handakuten variants)
- Must be treated as hard stops — lookahead never crosses a section header
- Must be filtered from output (not real entries)

### Cleaning Rules (`clean_vocab_ocr.py`)
1. Assign blocks to columns by x coordinate
2. Sort each column by y (top to bottom)
3. Skip pure digit blocks (standalone page numbers)
4. `split_entry_blocks()`: split fused blocks on entry markers or kana tokens ≥3 chars following kanji/digit (3-char threshold prevents splitting okurigana like 明+くる)
5. `parse_entry()`: token-based — consume leading digit → marker → affix prefix → kana reading → kanji → trailing digit
6. Lookahead (≤50px same column): grab page num or kanji from next block; stop at section headers or new word entries
7. Pass 3 — cross-column page-num assignment: for entries still missing a page number, search all digit blocks on the page within 250px right and ±40px vertically

### Validation (`validate_vocab.py`)
- JMdict (`jamdict`) confirms (reading, kanji) pairs
- Outputs `{stem}_valid.csv` (confirmed) and `{stem}_review.csv` (flagged)
- Review reasons: `not_in_jmdict`, `kanji_field_has_no_kanji`, `single_char_header`

### Fix Rules (`apply_vocab_fixes.py`)
After validation, triage entries are auto-fixed:
- `USE_JMDICT`: single JMdict suggestion → replace OCR kanji
- `STRIP_DIGIT`: digit prefix in kanji field → strip it
- `MERGED` + JMdict match: two entries fused → take first kanji-bearing JMdict form
- `MERGED` + no JMdict match: demote to kana-only
- `KANA_ONLY`: clear kanji field
- `REVIEW`: affix entries and ambiguous multi-suggestion cases → `{stem}_manual.csv`

Kana-only valid entries are checked against JMdict: if a kanji form exists, the first kanji-bearing form is added.

### Known OCR Limitations
- Some characters (e.g. 柵) are never detected by Vision — genuine misses, not parser bugs
- Kanji occasionally placed in a separate block below the reading rather than inline
- Col 1 entries near x ≈ 219–221 sometimes drift into the col2 zone (handled by boundary at 225)

### Pipeline Order (single scan)
```
ocr_vocab_pdfs.py     →  {n}_raw.json
clean_vocab_ocr.py    →  {n}_clean.csv
validate_vocab.py     →  {n}_valid.csv, {n}_review.csv
review_vocab.py       →  {n}_triage.csv, {n}_kana.csv
apply_vocab_fixes.py  →  {n}_final.csv, {n}_manual.csv
```
After pipeline: uninstall `jamdict` and `jamdict-data` (`pip3 uninstall jamdict jamdict-data`).

---

## Re-scanning with a Second PDF (v2 Reconciliation)

If a better-quality scan becomes available, run the full reconciliation pipeline instead of overwriting the original. Neither scan is a complete superset of the other — combining them produces a more complete list.

### When to use this
- A new scan of the same book is available (`N1 SCAN v2.pdf`, `N2 SCAN v2.pdf`)
- Target word count is ~2200 per level

### Pipeline Order (dual-scan reconciliation)
```
compare_scans.py n1        →  {n}_v2_raw.json, {n}_v2_clean.csv, diff CSVs
reconcile_n1.py n1         →  {n}_reconciled.csv  (~2190–2200 entries)
run_pipeline_reconciled.py n1  →  {n}_rec_final.csv  (JMdict-validated)
fix_final_entries.py n1    →  applies known reading-drift and MERGED fixes
```
Repeat with `n2` for N2.

### compare_scans.py
- OCRs `{LEVEL} SCAN v2.pdf` → `{level}_v2_raw.json` (skips if already done)
- Cleans → `{level}_v2_clean.csv`
- Diffs against existing `{level}_clean.csv`; writes `{level}_diff_only_in_v1.csv`, `{level}_diff_only_in_v2.csv`, `{level}_merged.csv`

### reconcile_n1.py
Merges v1 and v2 clean CSVs into one validated list:
1. Clean both: strip digit-prefixed kanji, extract first kanji segment from fused fields, filter artifact readings (contain kanji, fused >9-char kana)
2. Cluster near-duplicate readings by dakuten normalisation (`あんび`/`あんぴ` → same cluster)
3. Per cluster: pick best kanji (score penalises digits, 2-char+ kana runs inside kanji field)
4. JMdict validation pass: confirmed → keep; unconfirmed with 1 suggestion → fix kanji; unconfirmed with 0 suggestions but clean kanji → keep; otherwise demote to kana-only
5. Drop kana-only entries where a kanji version exists for the same reading

### fix_final_entries.py
Applies two categories of post-pipeline manual fixes (hardcoded per level):
1. **MERGED entries** where valid kanji was stripped because JMdict doesn't index adverbial forms (`一様に`, `漠然と`, `悠々と`, `均等に`, etc.)
2. **Reading-drift entries** where a dakuten error in the reading caused demotion to kana-only instead of correction (e.g. `れんぼう`→`れんぽう`/連邦, `ぽっしゅう`→`ぼっしゅう`/没収)

### Known post-reconciliation checks
- All (reading, kanji) pairs are JMdict-confirmed (or manually verified)
- Kana-only entries that have JMdict kanji forms are upgraded automatically by `apply_vocab_fixes.py`
- Remaining kana-only entries are either genuinely kana (JMdict has no kanji form) or came from triage KANA_ONLY (demoted from bad kanji)
- OCR characters that Vision never detects (e.g. 柵) remain as genuine misses

---

## Grammar Index OCR Pipeline

Source: `Dictionary of Japanese Grammar Index.pdf` — the romaji "Japanese Index"
of the DBJG / DIJG / DAJG series (21 pages, image-only). **Different rules from
the vocab pipeline**: Latin-script terms, so there is *no JMdict validation* —
the entire validate/fix/reconcile half of the vocab flow does not exist. QA is
purely structural. Scripts live in `JengoApp/scripts/`.

### Scan Settings
- OCR: Google Cloud Vision `DOCUMENT_TEXT_DETECTION`, `languageHints: ["en"]`
- Render: PyMuPDF at **3x** zoom (page is only 510x792pt → 1530x2376px)
- Output: `scripts/ocr_output/grammar_raw.json` (one object per page) + `.txt`

### Index Page Layout
- **2 columns** split at the page midpoint (`COL_SPLIT = 765`). Left-column
  references sit ~x720; the right column starts ~x850.
- Running header `<page> JAPANESE INDEX` at the top — cut by `y < 150`.
- Section headers are single Latin capitals (A, B, C …) — set `section`, filtered out.

### Entry Format
```
term [<see-also> | "english gloss" | [grammar label]] ...leader... reference
```
- **Reference is dual-type**: a page number → entry is in *this* volume; a
  letter `B` → DBJG, `I` → DIJG. This index belongs to the **Advanced (DAJG)**
  volume, so numeric refs map to `volume = A` (`HOME_VOLUME` constant).
- `<...>` = "X is found under Y" see-also; `"..."` = English gloss; `[...]` =
  grammar label (`[Counter]`, `[Wh-word]`, `[V]`). All captured into `gloss`.
- Leading `–`/`-` = sub-entry (`type = sub`); `~` = affix marker, kept in term.
- `→` arrow = cross-reference (`type = xref`, target captured), no page ref.

### Cleaning Rules (`clean_grammar_ocr.py`)
1. Assign words to columns by x-centre; cluster into physical lines by y-centre.
2. **Wrapped-entry merge** — the hard part. A line continues the previous entry
   when the pending entry is *incomplete* AND (hanging-indented past the column
   margin OR has an open `<`/`[`/`"` delimiter). Merge depth is **capped at 2
   lines** (`MAX_CONT`) so a single OCR-dropped delimiter damages at most 2
   entries instead of merging a whole column.
   - "complete" = ends in a reference, trailing leader dots, a closed gloss, or
     an arrow. The completeness gate is what stops runaway chaining.
   - Column margin = the *mode* of entry left-x (robust to far-left OCR outliers
     that would wreck a plain min()).
3. **Wrapped reference** — a line that is only a page number / letter (after a
   gloss filled the entry's line) is re-attached to the pending entry.
4. `parse_entry()` — split off arrow→xref, then trailing reference, then glosses
   (`<>` / `""` / `[]`), leaving the term; strip leader dots/ellipses, displaced
   superscript digits, and a leading sub-entry dash.

### QA (`qa_grammar.py`)
No dictionary to validate against, so QA only flags rows for manual review →
`grammar_qa.csv` (flagged rows + a `flags` column). Flags: `missing_ref`,
`empty_term`, `short_term`, `unbalanced`, `merged_suspect`, `bad_page`,
`bad_volume`, `xref_no_target`, `duplicate`.

### Pipeline Order
```
ocr_grammar_pdf.py    →  grammar_raw.json / .txt
clean_grammar_ocr.py  →  grammar_clean.csv  (term,gloss,volume,page,type,xref_target,section,src_page)
qa_grammar.py         →  grammar_qa.csv     (flagged rows only)
```

### Known OCR Limitations
- **Single-letter B/I references are frequently dropped by Vision** (the lone
  letter sits at the far right past the leader dots). ~23% of entries land with
  no parsed reference — the dots are detected but the trailing letter is not.
  These are genuine OCR misses (the source layout always carries a reference),
  surfaced as `missing_ref` for manual fill — not a parser bug.
- Superscript homograph numbers (`ne²`) OCR inconsistently as `2`/`'`; a leading
  displaced digit is stripped from the term.
- A dropped closing `>`/`"` merges up to 2 neighbouring entries (capped),
  flagged `merged_suspect` / `unbalanced`.

### Re-scan Reconciliation (`reconcile_grammar.py`)
A second scan fills references the first missed (the dropped B/I letters). Same
idea as the vocab v2 reconciliation but the second scan here is *lower quality*,
so the rules are conservative.

- **OCR a second scan as `grammar_v2`.** `ocr_grammar_pdf.py` and
  `clean_grammar_ocr.py` are scan-aware: `--pdf`, `--pages START END`, and
  `--columns`. The cleaner **auto-detects layout from page aspect** — portrait =
  one book page (2 columns), landscape = a 2-page spread (4 columns, split on
  even width-fractions; book gutter dead-centre).
- v2 used here = the Japanese Index inside the full *A Dictionary of Advanced
  Japanese Grammar* book (**pp.414-424**, landscape 4-column spreads — pages
  before are the English index, page 424's right half is References).
- **Reconcile rule:** the primary scan is always trusted. The secondary only
  *fills primary rows with no reference*, never overwrites. A blank is filled only
  when unambiguous (term → single plausible secondary ref, or a clear gloss match
  among senses); ambiguous cases go to `grammar_fill_review.csv`. "Plausible" =
  volume B/I, or volume A with page 1..900 (drops noisy stray pages).
- Outputs: `grammar_reconciled.csv` (primary + filled blanks, `ref_source` =
  v1/v2 column), `grammar_fill_review.csv`, `grammar_diff_only_in_v2.csv`.
- Reusable: point `--secondary grammar_v3` at a better scan later and re-run.

```
ocr_grammar_pdf.py v2                          →  grammar_v2_raw.json
clean_grammar_ocr.py --stem grammar_v2         →  grammar_v2_clean.csv  (auto 4-col)
ocr_grammar_pdf.py v3                          →  grammar_v3_raw.json   (clean standalone)
clean_grammar_ocr.py --stem grammar_v3         →  grammar_v3_clean.csv  (auto 2-col)
reconcile_grammar.py --secondary grammar_v3 grammar_v2   →  grammar_reconciled.csv
qa_grammar.py --stem grammar_reconciled        →  grammar_reconciled_qa.csv
```

**Scans used:** v1 + v2 (low-quality, pp.414-424) + v3 (clean standalone index,
21 portrait pages). Reconcile order `grammar_v3 grammar_v2` fills from the clean
scan first, then the noisy one for anything v3 still missed. v3 also *corrects*
v2's spurious page-A guesses (v2 mis-read several B/I cross-volume refs as
`A <page>`; v3 wins because it is listed first).

**Result:** blank references 238 → 62 (135 filled: 110 from v3, 25 from v2),
QA-flagged down to 5% (89/1502). Of the 25 v2 fills, 19 are A-page (lowest
confidence — verify via `ref_source` column); the 110 v3 + 6 v2-I are reliable.
The dash-tolerance fix (refs OCR'd as `B -`, leaders as dashes) also recovered
~128 refs in v1 on its own. Remaining 62 blanks are faint refs missed by all
three scans → manual fill (`grammar_reconciled_qa.csv`, flag `missing_ref`).

---

## Deck Files (`static/decks/`)

### Levels
| File | Entries |
|------|---------|
| `N5.json` | 702 |
| `N4.json` | 653 |
| `N3.json` | 2071 |
| `N2.json` | 2562 — existing deck merged with PDF-sourced list |
| `N1.json` | 3345 — existing deck merged with PDF-sourced list |

N1 and N2 are larger than the originals because they are merged from both the original curated deck and the PDF-extracted word index. This is the single authoritative list per level — no split variants.

### Deduplication rule
A word belongs to the lowest level it appears in. All five decks are deduplicated: any entry already in a lower-level deck is removed from higher ones. N1 is deduplicated against N2 and all lower levels.

### Format
```json
[{"lemma": "単語", "surface": "単語"}, ...]
```
`lemma` is the dictionary/kanji form (or hiragana if kana-only). `surface` matches `lemma`. No `~` affixes, no digits, no mixed ASCII/Japanese.

### Rebuilding decks after a new scan
```bash
python3 scripts/compare_scans.py n1 && python3 scripts/compare_scans.py n2
python3 scripts/reconcile_n1.py n1 && python3 scripts/reconcile_n1.py n2
python3 scripts/run_pipeline_reconciled.py n1 && python3 scripts/run_pipeline_reconciled.py n2
python3 scripts/fix_final_entries.py n1 && python3 scripts/fix_final_entries.py n2
# Then merge into N1.json/N2.json using the dedup+merge logic in this session's scripts
```
