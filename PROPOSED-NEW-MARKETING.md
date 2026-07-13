# PROPOSED-NEW-MARKETING.md

> **SUPERSEDED for content (2026-07-11).** The finalized, build-ready content spec now
> lives in **`JENGO-PROMO-CONTENT.md`** — that is the single source of truth for copy,
> features, screenshots, and structure (with the pricing/social-proof/reading facts
> locked). This file is kept as the original brief/rationale. When they disagree,
> `JENGO-PROMO-CONTENT.md` wins.

**Status:** Proposal / handoff brief. **Nothing here is implemented.** This is the
starting point for a Claude-design redesign of the Jengo promo page. Source copy is
pulled from `JengoApp/docs/Appstore-docs.md` (the live App Store listing, already in
the new voice). Screenshots to be supplied by Caden (current App Store set).

---

## Why this rewrite exists

The current promo page (`src/pages/jengo.astro` and its twin `src/pages/index.astro`)
sells the **retired story-mode identity**: "Between a reader and a flashcard app,"
"Jengo generates it into a paragraph," "Your words. In context.," a "Story mode"
feature. Jengo pivoted. The identity is now **a Japanese Dictionary + Flashcards app
that works offline** — the loop competitors make you cobble together from jisho.org +
Anki. Reading practice is a **paid layer on top (Pro)**, not the pitch.

Identity decision-of-record: `JengoApp/GAMEPLAN.md` §1 — "Dictionary + Flashcards
toolkit," offline is the *how*, AI reading is the *paid tier*. App Store subtitle is
moving from "Your vocab woven into stories" (stale) to **"Smart Dictionary + Flashcards."**

---

## Positioning

- **One-liner (GAMEPLAN §1):** *The Japanese dictionary and flashcard app that works
  offline — and writes reading practice around the words you're learning.*
- **The core loop to sell:** Look a word up → add it to flashcards in a tap → review
  offline. One app instead of jisho.org + Anki, with no copy-paste hop between them.
- **What to demote:** reading / generated stories = **Pro / coming soon**, mentioned
  once as "what Pro adds," never as the spine.
- **Do NOT use:** "reader," "vocabulary woven into stories," "your words in context,"
  "generates a paragraph," "immersion." Retired.

### Hero copy options (pick one during design)

Heading:
- "Look it up. Lock it in."
- "The dictionary and flashcards, finally one app."
- "Your Japanese dictionary and flashcards — offline."

Sub (from the App Store pitch):
> Japanese is hard enough — the tools shouldn't be. Jengo wires the dictionary, your
> flashcards, lookups, and audio into one app. Look something up, add it to your deck,
> and keep going. Works fully offline.

Hero animation: the current page animates a typewriter word ("…FASTER."). Keep the
mechanic if useful, but cycle words that fit the new identity, e.g. **FASTER. /
OFFLINE. / IN ONE TAP.** — not the paragraph-generation demo.

---

## Section-by-section rewrite

Current page order and how each block should change. Left = what's live (story-mode);
right = proposed.

| Current block | Proposed replacement |
|---|---|
| Hero: "…FASTER." + "Between a reader and a flashcard app" | New hero copy above; App Store badge stays (jengo.astro only — see two-page note) |
| Interactive demo: "Your words. In context." — flag unknown words in a generated paragraph | **Dictionary-lookup demo**: type romaji → entry appears (reading, meaning, audio) → tap "Add to flashcards" → card-added confirmation. Shows the loop directly. Reuse the existing cursor/typewriter animation rig. |
| "The problem with immersion — Native material buries vocabulary" | **"The problem today — Two apps, one clumsy hop."** You look words up in one app and retype them into another. The reading, the audio, the context — lost in the copy-paste. |
| "The problem with flashcards — Flashcards drill without context" | Fold into the block above, or: **"Two tools that don't talk."** A dictionary that can't remember and a flashcard app that can't look anything up. |
| "The Jengo approach — Your words, in context, every time." (builds paragraphs) | **"One loop, no friction."** Look it up, add it from the entry, review offline. Dictionary and flashcards share one app, one word list, one tap. |
| "Review less. Remember more." (spaced repetition) | **Keep** — still accurate. Modern spaced repetition (FSRS) schedules each word right before you'd forget it. |
| — (new) | **"Works on the train."** Fully offline — the whole dictionary and your decks live on your device. Sync catches up when you're back online (desktop, Android, iOS). |

---

## Features grid rewrite

Current cards: *Ready-made decks · Listening mode · Statistics · Story mode · AI assists.*
Proposed (sourced from `Appstore-docs.md` Dictionary/Flashcards bullets):

- **Search any way it comes to you** — draw it, or type romaji, kana, kanji, English,
  or wildcards (`!`/`?`) for characters you can't recall.
- **Add to flashcards in a tap** — straight from the dictionary entry.
- **Modern spaced repetition** — FSRS schedules each word at the moment you'd forget it.
- **Ready-made decks** — JLPT N5 through N1 built in, or import your own list.
- **Real audio + pitch accent** — hear words and sentences; see how they actually sound.
- **Kanji handwriting search** — can't type a kanji? Draw it.
- **Works fully offline** — with sync across desktop, Android, and iOS.
- **AI assists** — plain-English explanations and fresh example sentences on demand.
- **~~Story mode~~ → At-level reading (Pro, coming soon)** — generated stories at your
  level for mining new words back into flashcards. This is the ONE reading mention;
  frame as "what Pro adds," de-emphasized.

Keep "Statistics" if a screenshot supports it; "Listening mode" folds into "Real audio."

---

## Screenshots

Caden to supply the current App Store screenshot set (see `Appstore-docs.md` →
Screenshots path). Lead the page with screenshots that show the loop, in this priority:

1. Dictionary entry (definition, reading, audio, "add to flashcards")
2. Add-to-flashcards / deck confirmation
3. Flashcard review (the Japanese-first card layout)
4. Offline indicator / decks list
5. Handwriting search or wildcard search (differentiator)

Replace the current story/paragraph screenshots (`sc-study.png` captioned "generated
story," etc.) entirely.

---

## Creator note

Keep "From the builder." The origin — years in Japan, the gap between flashcards and
real language — is true and still supports the Pro reading layer. Optional tweak:
lead the gap with the tooling friction ("I was forever bouncing between a dictionary
and Anki") so it lands the dictionary-+-flashcards thesis before the reading one.

---

## Two-page note (RESOLVED 2026-07-09)

`/` is now the **Jengolang hub** (`index.astro`, rebuilt from the 1B toolkit-led design):
a dark toolkit hero + phone mockup + the "rest of Jengolang" tool cards. Its "Open Jengo"
CTAs point to **`/jengo`** (not straight to the app), so the promo page is where a visitor
goes to see everything Jengo offers + its platforms before downloading.

`jengo.astro` (served at `/jengo`) stays as the app showcase and is **what this brief
rewrites** — off the current story-mode copy to the Dictionary + Flashcards identity.

(Correction to an earlier note here: the two pages were *not* "byte-identical except 12
lines." Before this change they had diverged significantly — `jengo.astro` was the newer,
maintained fork with the App Store button + demo fixes; `index.astro` was the stale
original. That's now moot — `index.astro` is the hub.)

---

## Open questions

- Which hero heading/tagline?
- Is the interactive lookup demo worth building, or lead with a static screenshot?
- App Store badge: `jengo.astro` links `id6765958942`; confirm it's the live listing.
- Which AI assists are free vs Pro? (affects how the "AI assists" card is framed)
