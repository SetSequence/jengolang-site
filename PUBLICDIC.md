# Public Dictionary — Plan

## Concept

A standalone, crawlable public dictionary at `jengolang.com/dictionary` backed by the same Jengo FastAPI endpoints. Two surfaces, one API — no logic duplication.

## Goals

- SEO-indexed word and kanji pages (long-tail keyword capture)
- Internal cross-linking for topical authority (words ↔ kanji ↔ categories)
- "Study in Jengo" CTAs → app conversion funnel
- In-app dictionary gets a "View page" link back to the public URL

## Architecture

```
FastAPI (Railway)          Astro SSR (Cloudflare Pages)
  /dictionary/search   ←── /dictionary/[word]
  /dictionary/kanji    ←── /kanji/[char]
  (public, no auth)        (server-rendered, crawlable)
```

- Astro SSR with `@astrojs/cloudflare` adapter — on-demand rendering, not static build (JMDict is 200k+ entries, static generation is impractical)
- Each page request hits FastAPI at runtime and renders full HTML for crawlers

## What Needs to Change

### Jengo backend
- Dictionary search endpoints must be public (no auth required)
- Confirm CORS allows requests from `jengolang.com`
- Decide: same endpoints + public flag, or separate `/public/dictionary/*` prefix

### Astro site
1. Enable SSR adapter (`@astrojs/cloudflare`)
2. Add routes:
   - `src/pages/dictionary/[word].astro` — word entry page
   - `src/pages/kanji/[char].astro` — kanji breakdown page
   - `src/pages/dictionary/index.astro` — search landing
3. Sitemap — seed word list at build time or generate separately via script
4. SEO metadata per entry (title, description, structured data / JSON-LD)
5. Internal links: kanji in entry → `/kanji/[char]`, tags → category pages

### Cross-surface seam
- Public page: "Study in Jengo" button → deep-links to app dictionary entry
- In-app dictionary: "Share / View page" link → `jengolang.com/dictionary/[word]`

## Open Questions (pick up here)

- Are dictionary endpoints currently auth-gated? (determines scope of backend change)
- Should unauthenticated hits be rate-limited or cached at Cloudflare?
- Kanji pages: pull from JMDict or a separate KANJIDIC source?
- Category/tag pages (e.g. `/dictionary/tag/noun`) — phase 1 or defer?
- URL encoding strategy for CJK characters in routes

## Deferred

- Multilingual definitions (huge lift, phase 2+)
- Full radical/stroke-count search UI on public pages
- Analytics / conversion tracking between public dictionary → app signup
