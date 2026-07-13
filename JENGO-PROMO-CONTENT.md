# JENGO-PROMO-CONTENT.md — Build-ready content spec for `/jengo`

**Status:** Finalized content spec. This is the single source of truth for the copy,
features, screenshots, and structure of the `/jengo` app-promo page. It supersedes the
content sections of `PROPOSED-NEW-MARKETING.md` (which was the earlier proposal/brief).

**How to use this:** Hand this to Claude Design. Every string here is paste-ready or a
clearly-labeled recommendation with alternatives. The designer decides *layout, hierarchy,
motion, and visual treatment* — not *what content exists*. If a section says "OMIT," it
must not appear. If it says "coming soon," it must not be dressed up as shipped.

**Hard facts locked (2026-07-11):**
- **Live now:** iOS app (App Store) + web app (`app.jengolang.com`). **iOS takes precedence** —
  App Store badge is the primary CTA, web is the secondary "open in browser."
- **Pricing: UNDECIDED.** The page is **pricing-agnostic**. Do **not** write "Pro," "free,"
  "subscription," "$", "upgrade," or "paid tier" anywhere. Reading/stories are just "coming soon."
- **Social proof: none exists yet.** No ratings, reviews, or user counts. Do **not** invent
  them. The testimonial/social-proof section is replaced (see §10).
- **Product reality:**
  - **Dictionary + Flashcards** = fully live, polished. **This is the entire pitch.**
  - **Grammar dictionary + learning path** = coming next (in-app). *(Separate from the web
    grammar guides already live at `/learn/japanese/grammar` — cross-link those, see §11.)*
  - **At-level reading / generated stories ("Read")** = coming soon, after grammar.
  - **Training Mode** = beta, in the app. Light mention only.
  - **Encounter + Listening** = abandoned alpha placeholders. **OMIT ENTIRELY.** Never name
    or screenshot them. **Do not use `Landing_page.PNG` / final slide-01 as a feature
    screenshot** — it advertises Encounter/Listening.

---

## 1. What research says drives clickthrough (the rules this page obeys)

Grounded in current landing-page + App-Store-conversion practice (sources at bottom). These
are the constraints the design must satisfy:

1. **The first screen is the whole gamble.** Visitors judge in seconds. Above the fold must
   carry: one outcome headline, one clarifying subline, one primary CTA, and a trust cue.
2. **One primary CTA per screenful.** No competing equal-weight buttons. App Store badge
   leads; web link is visibly secondary. Repeat the same CTA down the page (sticky on mobile).
3. **Lead with the outcome, not a feature tour.** The differentiator ("look it up → it's a
   flashcard") goes first; the feature list comes after the promise lands.
4. **Screenshots do the persuading; the first two are the pitch.** ~half of viewers never get
   past screenshot 2. Order them by persuasive power, not by app navigation order.
5. **Thumb-zone CTAs, 44px+ targets, mobile-first.** Sticky bottom CTA on mobile.
6. **Trust cue even without reviews.** With no ratings yet, founder credibility + concrete,
   verifiable product facts carry the trust load (§10).
7. **Structured, direct-answer copy (tables, steps, short FAQ) helps SEO + AI-search citation.**

---

## 2. Audience (who every line is written for)

**Primary:** the self-study Japanese learner **past the very basics** — knows kana, has some
grammar, and is now grinding vocabulary. Today they cobble a stack together: **jisho.org for
lookups + Anki for retention**, copy-pasting between them. JLPT-oriented (N5–N1).

**They are NOT:** absolute beginners needing kana/grammar taught, or classroom students. Don't
sell "learn Japanese from scratch." Sell "stop fighting your tools."

**How they'll arrive / what they're searching:** "jisho alternative," "Anki for Japanese,"
"Japanese dictionary app offline," "JLPT flashcard app," "handwriting kanji dictionary,"
"Japanese dictionary that adds to flashcards." Mirror that language.

---

## 3. Positioning & message hierarchy

**One-liner (north star):** *The Japanese dictionary and flashcards in one app.*

**The loop we sell (say it everywhere, in this order):**
**Look it up → add it to flashcards in one tap → review offline.** One app instead of
jisho.org + Anki, with no copy-paste hop between them.

**Message priority (top = most valuable, cut from the bottom if space is tight):**
1. Dictionary + flashcards are **one app** (the integrated loop).
2. Built to minize the amount of time spent grinding so you can enjoy the rest of your time on real content (Multicard view, FSRS, premade decks, integrated loops and explanations) 
3. Clean UI with intuitive features. Japanese is messy, your tools shouldn’t be.
2. **Add-to-flashcards from the entry** — the single biggest differentiator.
3. **Works fully offline.**
4. **Search any way** (romaji/kana/kanji/English/handwriting/wildcards/paste-a-sentence).
6. **JLPT N5–N1 decks built in** + import your own. AI can make new + refine existing flashcards. 
7. AI word explanations + on-demand examples (differentiator, but demote below the loop).
8. Audio + pitch accent.

**Retired language — never use:** "reader," "vocabulary woven into stories," "your words in
context," "generates a paragraph," "immersion," "story mode." Also never: "Pro," "free tier,"
price claims.

---

## 4. Hero

**Tone (per Caden, 2026-07-11):** no whimsy, no clever wordplay. The hero should *mean*
something and read as a stance, not a slogan. It signals the audience — serious self-study
learners past the basics — and separates Jengo from gamified apps.

**Headline — DECIDED:** **"Built for serious Japanese study."**
*(Positioning statement: says who it's for and what kind of tool it is. Not marketing-cute.)*
Same-register alternatives if design needs a variant:
- "The tools serious Japanese learners actually need."
- "Serious Japanese study, without the busywork."

**Subhead (paste-ready — carries the loop + keywords, does the concrete work):**
> A full Japanese dictionary and spaced-repetition flashcards in one app. Look a word up, add
> it to your deck in a tap, and review it anywhere — fully offline.

**Primary CTA:** official **Download on the App Store** badge → the live listing
(`id6765958942` — confirm it resolves to the live product page before ship).
**Secondary CTA (visibly lighter):** "Or open it in your browser →" → `app.jengolang.com`.

**Animation:** keep it restrained to match the serious tone. **Drop the "…FASTER."
typewriter gimmick.** If any motion, prefer something quiet and substantive — e.g. a subtle
fade/settle on the hero screenshot, or none. Respect `prefers-reduced-motion`.

---

## 5. Platform strip (instant "it's multiplatform" signal)

Placed right under the hero.
**Copy:** "On iPhone, and in any browser — your words sync between them."
- Show: **iOS** (primary) and **Web/desktop browser**. Both live.
- Use the **desktop web-app screenshot** (`Desktop/…12.17.06 PM.png` — sidebar + review
  forecast + Flashcards) to prove the browser experience is real, not a shrunk phone app.
- **Android:** the App Store description claims desktop/Android/iOS, but only iOS + web are
  confirmed live. **ANdroid is otw, but confirmed not complete** an Android build is
  actually shippable. If confirmed, add it; otherwise "web browser" covers desktop use.
---

## 6. Feature grid — FINAL (include exactly these)

Each = icon (SVG, no emoji) + short label + one sentence. Ordered by message priority.

1. **Add to flashcards in a tap** — Straight from the dictionary entry, with the reading,
   audio, and examples attached.
2. **An array of search tools** — Draw it, type romaji, kana, kanji, or English. Use
   `?`, `*`, or `!` as wildcards for characters you can't recall. Paste a whole sentence to
   look up every word at once.
3. **Works fully offline** — The entire dictionary and your decks live on your device. Syncs
   to the web when you're back online.
4. **Modern spaced repetition** — An FSRS scheduler shows each word at the moment you'd forget
   it. No setup, no fiddling with intervals.
5. **JLPT decks built in** — N5 through N1 ready to study (700–2,900 words per level), or
   import your own list.
6. **Kanji handwriting search** — Can't type a kanji you don't recognize? Draw it and Jengo
   finds it.
7. ** audio + pitch accent** — Hear words and sentences, and see how they actually sound.
8. **Plain-English explanations** — Get a word's core meaning, the words it's easily confused
   with, and how it's actually used — generated on demand.
9. **On-demand example sentences** — Pull fresh examples for any definition whenever you want
   more context.
10. **Multi-card review** — Clear the words you already know fast instead of flipping them one
    at a time.
11. **Make it yours** — Build your own cards quickly and tag decks with colored icons. Auto enhance/refine feature for lower quality cards.

**Optional (include only if a clean screenshot/visual supports it):**
- **Review forecast** — now available cleanly: the desktop web-app home
  (`Desktop/…12.17.06 PM.png`) shows the "coming up this week" bar chart **without** the
  abandoned modes. Safe to use. Good "you can see what's ahead" beat.
- **Statistics** — there's a stats tab, but no strong isolated screenshot in the current set.
  Omit unless Caden supplies one.

---

## 9. Screenshots — FINAL order + captions

Use the **raw** captures (clean device frames) or re-frame in the App Store house style. Lead
with the loop. First two = the whole pitch.

| # | File (Raw screenshots/) | Caption |
|---|---|---|
| 1 | `Dictionary_entry_with_examples.PNG` | "Look up any word — reading, meaning, audio, examples. Then keep it." *(shows the "In 1 deck" add button — the differentiator)* |
| 2 | `Flashcard_front_single.PNG` | "Review with modern spaced repetition." |
| 3 | `Dictionary.PNG` | "Search however the word comes to you — kana, kanji, romaji, English, or a pasted sentence." |
| 4 | `Handwriting.PNG` | "Can't type a kanji? Draw it." |
| 5 | `Explayined_word_dictionar.PNG` | "Plain-English explanations, on demand." |
| 6 | `Singlecard_backside.PNG` | "Japanese-first cards, built for reading." |
| 7 | `Multicardview_flashcards.PNG` | "Clear the easy words fast." |
| 8 | `Importable_Decks.PNG` | "JLPT N5–N1 decks built in, or import your own." |

**Desktop / web screenshots (use for the platform strip + a "works on desktop too" beat):**

| Desktop file | Use / caption |
|---|---|
| `Desktop/…12.17.06 PM.png` | Web-app home: sidebar + review forecast + Flashcards. **Platform-strip hero for "in your browser."** Clean — no beta modes. |
| `Desktop/…12.16.44 PM.png` | Desktop multi-card review (2-column). Alt for feature #10 "clear the easy words fast." |
| `Desktop/…12.16.56 PM.png` | Desktop Flashcards deck list (Read/Speak/JLPT decks, deck counts). Use only if a "your decks" beat is wanted; shows the **Training** banner (beta) — fine, don't caption it. |

**Never use as a feature screenshot:** the **mobile** study-home `Landing_page.PNG` (and final
slide-01) — it shows Encounter/Listening, which are OMITTED (§0). The **desktop** web home
above is a different, clean screen and IS safe.

**App Store house-style reference** (already-designed captions, for tone/type treatment):
"The Best Dictionary + Flashcards," "Draw to search," "Word explanations," "On-demand
examples," "Review many at once," "Easy to use spaced repetition." Green/cream palette, serif
display headline, single device in frame. Match this look for brand continuity.

---

## 10. Trust — what replaces "social proof" (there is none yet)

**Do NOT** include a testimonials block, star ratings, "10,000 learners," or press logos —
none exist and inventing them is off the table.

**Instead, carry trust with:**
- **The creator note** (§12) — a real person, real credentials, doing the building.
- **Concrete, verifiable product facts** stated plainly: "A full Japanese dictionary." "JLPT
  N5–N1, ~8,900 words across the built-in decks." "FSRS scheduling." "Works with no connection."
- **Honesty as a differentiator:** "Made by one developer, not a faceless app factory."
- **Optional "follow the build":** if Caden has a public X/dev account, link it as
  build-in-public credibility. Omit if none.
To protect privacy somewhat, DO NOT SURFACE THE NAME CADEN ANYWHERE. This includes file names. 



---

## 11. Secondary CTA (before the creator note)

Catches the already-convinced. Same CTA pair as the hero.
**Heading:** "Stop juggling apps and learning tools”
**Sub:** “and let Jengo do it for you.“
Primary App Store badge + secondary "open in browser."

---

## 12. Creator note ("From the builder")

Keep it. **Reuse the existing photo and copy from the current page** — both are real and on
message; don't rewrite them.

- **Photo:** reuse **`/caden-nara.jpg`** (already in `public/`, currently at the bottom of
  `jengo.astro`). Alt: "Caden Shelley at Todai-ji temple in Nara, Japan." No new photo needed.
- **Copy (already live — keep verbatim):**
  > **From the builder.**
  > I lived in Japan for two years, read grammar dictionaries cover to cover, worked through
  > dozens of books and hundreds of podcasts, spent three hours a day on flashcards and four
  > hours speaking with natives, and "learned" more than 15,000 words. **I did everything right.**
  >
  > But I knew there had to be a better way. **Jengo is the tool I always wanted, but never had.**

This copy carries the trust load (§10) and reinforces the "serious study" stance from the hero.
Keep it as the emotional anchor near the bottom, before the final CTA/footer.

---

## 13. What's next (honest roadmap — ONE modest block, no "Pro")

De-emphasized, near the bottom. Frames momentum without overselling unfinished work.
**Heading:** "Just getting started."
**Body:**
> Coming next: a built-in grammar dictionary and a guided learning path. After that, at-level
> reading — short passages built around the words you're actually learning, with tap-to-look-up
> and add-to-flashcards baked in. A beta Training Mode is already in the app for extra drilling.

Rules: **no "Pro," no price, no dates.** "Coming next / after that / beta" only. This is the
**single** reading mention on the page.

---

## 14. Footer + additional links

**Keep the visitor in the funnel — minimal outbound leaks.**
- **Grammar guides (live now, free, on this site):** link `/learn/japanese/grammar`. Strong,
  honest cross-link — a real companion tool that already works. Frame: "Free grammar guides,
  on the web now."
- **Jengolang hub:** `/`
- **Privacy:** `https://app.jengolang.com/privacy` (external, app-hosted)
- **App Store** + **web app** links repeated.

**Deliberately NOT on this page:** outbound links to Tofugu/other learning resources. Those
belong on the grammar/content pages, not the conversion page, where they'd leak clicks. (The
kana/Tofugu "link out" idea from JENGOLANG.md is for content pages, not `/jengo`.)

---

## 15. Features / details to OMIT (technical or not worth the space)

- **Encounter, Listening** — abandoned alpha. Never mention or show. (§0)
- **Sync internals / conflict resolution / server details** — "works offline, syncs" is the
  whole story.
- **FSRS parameter tuning, scheduling internals** — say "modern spaced repetition," stop there.
- **Furigana rendering, desktop audio fixes, queue-end scheduling fixes** — changelog detail,
  not marketing.
- **Do not oversell Training Mode / Battleground** — it's beta; one line in §13 max.
- **No pricing, no ratings, no user counts, no press.**

---

## 16. SEO / meta / structured data

- **`<title>`:** `Jengo — Japanese Dictionary & Flashcards, Offline`
- **Meta description:** `A full Japanese dictionary and spaced-repetition flashcards in one
  offline app. Look up any word by kanji, kana, romaji, English, or handwriting — and add it to
  your deck in a tap. JLPT N5–N1 decks built in.`
- **Canonical:** `https://jengolang.com/jengo`
- **JSON-LD:** `SoftwareApplication` (name: Jengo, applicationCategory: EducationApplication,
  operatingSystem: "iOS, Web"). **Omit `offers`/price** until pricing is decided.
- **JSON-LD `FAQPage`** using §17 (good for AI-search citation).
- Keep the existing page conventions: `prerender`, `is:global` styles, oklch tokens, real
  `<head>`, `prefers-reduced-motion` guards, mobile-first.

---

## 17. FAQ block (paste-ready — SEO + GEO; pricing-safe)

Answer only what's true today. **No pricing question** (undecided).

- **Does Jengo work offline?** Yes. The full dictionary and all your decks live on your device.
  It syncs to the web when you're back online.
- **What platforms is it on?** iPhone and any web browser today, with your words synced between
  them.
- **Can I look up a kanji I can't type?** Yes — draw it with handwriting search, or search by
  reading, romaji, or English meaning.
- **Does it have JLPT vocabulary?** Yes — JLPT N5 through N1 decks are built in, and you can
  import your own word lists.
- **How is this different from Anki + jisho.org?** It's both in one app. You look a word up and
  add it to spaced-repetition flashcards in a single tap. Jengo is also cleaner and more intuitive than alternatives because I designed it to show only what you need, when you need it. It elminates the friction of jumping between all your tools.
- **What kind of flashcard scheduling does it use?** A modern FSRS-6 (Free spaced repetition scheduler)
  that shows each word right before you'd forget it.

---

## 18. Open decisions (now resolved) + what's still on Caden

**Resolved:** CTA target (iOS primary, web secondary) · pricing framing (agnostic, no Pro) ·
social proof (none → founder + facts) · reading status (coming soon, one mention) ·
Encounter/Listening (omit) · **hero headline = "Built for serious Japanese study"** ·
**creator photo = reuse `/caden-nara.jpg`** · **desktop/web screenshots supplied** (clean, no
beta modes → platform strip + review-forecast beat un-blocked).

**Still needs Caden before ship:**
- Provide a **public build/X account** link if one exists (else omit §10 build-in-public line). CONFIRMED: NONE EXIST
