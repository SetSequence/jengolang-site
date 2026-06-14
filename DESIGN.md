# Design

## Overview

Light mode only. Warm-green brand. Restrained color strategy: the green carries the brand; neutrals do the structural work; orange appears rarely as a secondary signal. Day One is the visual reference — screenshot-led, direct, quiet confidence. Warmer in tone.

---

## Color

### Strategy

Restrained. Tinted neutrals plus one brand accent (forest green) at roughly 15–20% of the surface. Orange as a tertiary signal only.

### Palette

```css
/* Brand */
--color-brand:         oklch(47% 0.089 156);   /* #357d5e — forest green */
--color-brand-dark:    oklch(25% 0.062 156);   /* #1e3d2f — icon/header bg */
--color-brand-tint:    oklch(96% 0.016 156);   /* #eef7f2 — subtle bg wash */

/* Neutrals (tinted toward brand hue) */
--color-bg:            oklch(98.5% 0.005 156); /* off-white, not #fff */
--color-surface:       oklch(99% 0.003 156);   /* cards, modals */
--color-border:        oklch(90% 0.008 156);   /* dividers */
--color-border-strong: oklch(82% 0.012 156);   /* input outlines */

/* Text */
--color-text-primary:  oklch(22% 0.010 156);   /* headings, body */
--color-text-secondary:oklch(50% 0.012 156);   /* meta, labels */
--color-text-tertiary: oklch(68% 0.008 156);   /* placeholders, captions */

/* Accent */
--color-accent:        oklch(57% 0.148 50);    /* #e07b00 — due/warning; used sparingly */

/* Feedback */
--color-success:       oklch(44% 0.110 145);   /* #2a7a2a */
--color-danger:        oklch(42% 0.180 27);    /* #c0392b */
```

### Usage rules

- Buttons: `--color-brand` fill, white label. Hover: darken 8% lightness.
- Links: `--color-brand` underline, no box.
- Section backgrounds: alternate between `--color-bg` and `--color-brand-tint` to create rhythm without borders.
- Never use `--color-accent` decoratively; reserve it for due-date or warning states.
- Japanese text (ruby, kanji): same color tokens as surrounding text. No special tinting.

---

## Typography

### Fonts

| Role | Family | Source |
|------|--------|--------|
| All type | Onest | Google Fonts |
| Japanese | Noto Sans JP | Google Fonts |
| Monospace (code) | JetBrains Mono | Google Fonts |

Onest is a geometric grotesque variable font (100–900 weight axis) with a warm, purposeful character that avoids the stiffness of pure geometric sans. Single-family: weight contrast alone carries the hierarchy. Noto Sans JP covers all Japanese characters in grammar articles and vocabulary tables.

Load strategy: `display=swap` on all. Preload the 400-weight Onest subset only. Subset Noto Sans JP to the characters needed per page rather than loading the full weight set.

### Scale

```css
/* Mobile-first, fluid via clamp() */
--text-xs:   clamp(0.75rem,  0.72rem + 0.15vw,  0.8125rem);  /* 12–13px */
--text-sm:   clamp(0.875rem, 0.84rem + 0.18vw,  0.9375rem);  /* 14–15px */
--text-base: clamp(1rem,     0.96rem + 0.20vw,  1.0625rem);  /* 16–17px */
--text-lg:   clamp(1.125rem, 1.08rem + 0.23vw,  1.25rem);    /* 18–20px */
--text-xl:   clamp(1.25rem,  1.15rem + 0.50vw,  1.5rem);     /* 20–24px */
--text-2xl:  clamp(1.5rem,   1.35rem + 0.75vw,  2rem);       /* 24–32px */
--text-3xl:  clamp(2rem,     1.75rem + 1.25vw,  2.75rem);    /* 32–44px */
--text-4xl:  clamp(2.5rem,   2.0rem  + 2.50vw,  3.75rem);    /* 40–60px */
```

### Weights

- Display headings: 750–800 (Onest ExtraBold)
- Section headings: 600–650 (Onest SemiBold)
- Body: 400 (Onest Regular)
- Labels / meta: 500 (Onest Medium)
- Strong emphasis: 600 (Onest SemiBold) — never bold in body copy

### Line lengths

- Body paragraphs: max 68ch
- Article body (grammar guides): max 72ch
- Hero headline: unconstrained; wrap by layout

---

## Spacing & Layout

### Scale

```css
--space-1:  0.25rem;   /*  4px */
--space-2:  0.5rem;    /*  8px */
--space-3:  0.75rem;   /* 12px */
--space-4:  1rem;      /* 16px */
--space-6:  1.5rem;    /* 24px */
--space-8:  2rem;      /* 32px */
--space-12: 3rem;      /* 48px */
--space-16: 4rem;      /* 64px */
--space-24: 6rem;      /* 96px */
--space-32: 8rem;      /* 128px */
```

### Layout

- Max content width: `1120px` (marketing sections); `760px` (article body)
- Page padding: `var(--space-4)` mobile, `var(--space-8)` tablet, `var(--space-16)` desktop
- Section vertical rhythm: alternate `--space-24` and `--space-16` between sections; do not use the same spacing throughout
- Grid: CSS Grid. 12 columns on desktop, 4 on mobile. Screenshots and feature blocks use 5/7 splits, not symmetric halves.

### Breakpoints

```css
/* Mobile-first */
--bp-sm: 480px;
--bp-md: 768px;
--bp-lg: 1024px;
--bp-xl: 1280px;
```

---

## Components

### Buttons

```
Primary: brand fill (#357d5e), white label, 8px radius
         padding: 12px 24px (mobile), 14px 28px (desktop)
         hover: oklch(42% 0.089 156) — 5% darker
         focus: 2px offset outline in --color-brand

Secondary: transparent, 1.5px --color-brand border, brand-colored label
           same sizing as primary
```

No icon-only buttons without visible label (accessibility). No pill/fully-rounded buttons — 8px radius only.

### App CTA

The "Try Jengo" call-to-action used on content pages and in the landing page secondary slot:

```
Surface:  --color-brand-tint background
Border:   1px --color-border
Padding:  --space-8 --space-6
Radius:   12px
Heading:  "Practice this in Jengo" — Inter SemiBold, --text-lg
Body:     one sentence, --color-text-secondary, --text-base
Button:   Primary button, full width on mobile
```

### Navigation header

```
Height:    56px mobile, 64px desktop
Bg:        --color-brand-dark (#1e3d2f)
Logo:      SVG "J" mark + "Jengo" wordmark, white
Nav links: --text-sm, white at 80% opacity; hover 100%
CTA:       "Try Jengo" — white outline button, right-aligned
```

### Feature item

Used in the features section. Icon + label + one sentence. No cards.

```
Icon:    24px SVG, --color-brand stroke
Label:   Inter SemiBold, --text-lg, --color-text-primary
Body:    Inter Regular, --text-base, --color-text-secondary, max 52ch
Layout:  icon left-aligned with label; body below label, indented to text start
```

### Grammar article table (formation)

```
Table:        full width, border-collapse
Header row:   --color-brand-tint bg, Inter SemiBold --text-sm
Body rows:    alternating --color-bg / --color-surface
Cell padding: --space-3 --space-4
Japanese:     Noto Sans JP, --text-base
Ruby text:    --text-xs, --color-text-tertiary
```

### Vocab table

```
Columns:    Word | Reading | Meaning | (JLPT level badge)
Row hover:  --color-brand-tint
Sticky header on scroll
Sticky first 50 rows, then "Show all" expand
```

### JLPT level badge

```
N5: oklch(65% 0.14 145) — green
N4: oklch(60% 0.14 200) — teal-blue
N3: oklch(58% 0.13 255) — blue
N2: oklch(55% 0.15 290) — purple
N1: oklch(50% 0.16 30)  — orange-red
Border-radius: 4px
Font: Inter SemiBold, --text-xs, white
Padding: 2px 6px
```

---

## Motion

Subtle. Never on layout properties.

```css
--duration-fast:   120ms;
--duration-base:   200ms;
--duration-slow:   350ms;
--ease-out:        cubic-bezier(0.16, 1, 0.3, 1);  /* expo-out */
```

- Button hover/focus: `--duration-fast`, background color only
- Section entrance: `opacity 0→1` + `translateY 12px→0`, `--duration-slow`, `--ease-out`
- No bounce, no elastic, no parallax

---

## App Icon

The Jengo icon is a bold "J" in Georgia serif, white on `#357d5e` (forest green), square with no border radius in SVG form. The detailed variant (`icon.svg` in the app root) adds horizontal ruled lines at increasing opacity behind the J, suggesting a study notebook — use this variant in large display contexts (App Store badge section, etc.).

Source files:
- `/Users/cadenshelley/Documents/JengoApp/static/icons/icon.svg` — simple mark
- `/Users/cadenshelley/Documents/JengoApp/static/icon.svg` — detailed variant (1024×1024 viewBox 120×120)
- `/Users/cadenshelley/Documents/JengoApp/AppIcon-1024.png` — App Store master

---

## Reference

Visual reference: [Day One](https://dayoneapp.com/) — screenshot-led layout, direct feature language, secondary CTA before verbose sections, overall restraint. Warmer palette.

Anti-references:
- Memrise (gamified, crowded, cheap)
- Generic SaaS landing pages (hero metrics, gradient text, glassmorphism)
- Duolingo (mascot-driven, game-loop aesthetics)
