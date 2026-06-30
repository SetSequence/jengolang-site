// Goal routes — the "subway lines" of the grammar map (TREE.md #10).
// Each goal is a query over the tag schema that selects a coherent, useful
// subset of the catalog, surfaced as a standalone SEO/GEO landing page at
// /learn/japanese/grammar/path/[id]. The predicate is the single source of
// truth: the same `match` drives membership on the landing page and (by id)
// the lit route on the hub.

import type { CollectionEntry } from "astro:content";

type GrammarData = CollectionEntry<"grammar">["data"];

export interface Goal {
  id: string;
  label: string; // short, for chips / cross-links
  h1: string; // page H1
  title: string; // <title> + og
  description: string; // meta description (the SEO query target)
  lede: string; // hero paragraph
  intent: string; // one line: who this route is for
  accent: string; // oklch theme colour for the route
  tint: string; // matching pale background
  // Optional sub-faceting shown in the in-page filter. JLPT chips only make
  // sense when a goal spans multiple levels (a single-level JLPT goal hides them).
  jlptFacet: boolean;
  match: (d: GrammarData) => boolean;
}

const jlptGoal = (
  lvl: "N5" | "N4" | "N3" | "N2" | "N1",
  accent: string,
  tint: string,
  blurb: string,
  lede: string,
): Goal => ({
  id: `jlpt-${lvl.toLowerCase()}`,
  label: `JLPT ${lvl}`,
  h1: `JLPT ${lvl} Grammar List`,
  title: `JLPT ${lvl} Grammar List — Every Point, Mapped — Jengo`,
  description:
    `Complete JLPT ${lvl} grammar list: every ${lvl} grammar point with a plain-English ` +
    `explanation, examples and furigana. ${blurb}`,
  lede,
  intent: `Sitting the JLPT ${lvl} — or gauging where you are against it.`,
  accent,
  tint,
  jlptFacet: false,
  match: (d) => d.jlpt === lvl,
});

export const GOALS: Goal[] = [
  jlptGoal(
    "N5",
    "oklch(52% 0.11 156)",
    "oklch(96% 0.02 156)",
    "The beginner core — particles, the copula, て-form and the first conditionals.",
    "The complete N5 grammar set — the absolute beginner core. Particles, the " +
      "copula, verb bases, the て-form and the first conditionals. Master these " +
      "and every other point on the map has something to attach to.",
  ),
  jlptGoal(
    "N4",
    "oklch(52% 0.11 200)",
    "oklch(96% 0.02 200)",
    "Upper-beginner — passive, causative, conditionals, giving & receiving, plain-form modality.",
    "Every N4 grammar point. The upper-beginner layer: passive and causative, " +
      "the full conditional set, giving-and-receiving, and the plain-form modality " +
      "that lets you stop speaking in textbook sentences.",
  ),
  jlptGoal(
    "N3",
    "oklch(52% 0.12 250)",
    "oklch(96% 0.02 250)",
    "The intermediate bridge — the grammar that unlocks real native material.",
    "All N3 grammar — the intermediate bridge. This is the band where set " +
      "expressions, nuance particles and connectives pile up; clearing it is what " +
      "turns native material from a wall into something you can read.",
  ),
  jlptGoal(
    "N2",
    "oklch(50% 0.12 300)",
    "oklch(96% 0.022 300)",
    "Upper-intermediate — the dense set-phrase and formal-register layer.",
    "Every N2 grammar point. The upper-intermediate layer is mostly set phrases " +
      "and written-register patterns — high volume, heavily tested. The map groups " +
      "them by family so the sheer count stops feeling random.",
  ),
  jlptGoal(
    "N1",
    "oklch(48% 0.13 340)",
    "oklch(96% 0.024 340)",
    "Advanced — literary, formal and emphatic grammar for the top of the exam.",
    "The full N1 grammar list — the advanced band. Literary and formal patterns, " +
      "stiff written connectives and emphatic constructions. Many overlap the " +
      "Read-novels route; the rest is exam-room formality.",
  ),
  {
    id: "read-novels",
    label: "Read novels",
    h1: "Grammar to Read Japanese Novels",
    title: "Grammar to Read Japanese Novels — Literary & Classical — Jengo",
    description:
      "Every grammar point you need to read Japanese literary prose: classical " +
      "auxiliaries, written-style copula, literary particles and connectives — " +
      "each with examples and furigana.",
    lede:
      "The literary route. Modern textbooks stop where novels begin — at the " +
      "written-style copula, the classical auxiliaries (ごとし, べし, ず) and the " +
      "literary particles that fill printed prose. This is that grammar, gathered " +
      "in one place and ordered so it builds on what you already know.",
    intent: "Cracking open novels, literary essays or classical-flavoured prose.",
    accent: "oklch(48% 0.13 290)",
    tint: "oklch(96% 0.022 290)",
    jlptFacet: true,
    match: (d) =>
      d.register.includes("literary") || d.register.includes("archaic"),
  },
  {
    id: "casual-spoken",
    label: "Casual & spoken",
    h1: "Casual & Spoken Japanese Grammar",
    title: "Casual & Spoken Japanese Grammar — Anime & Conversation — Jengo",
    description:
      "The grammar of real spoken Japanese: contractions, sentence-ending " +
      "particles, casual connectives and the colloquial patterns you actually " +
      "hear in anime, dramas and conversation.",
    lede:
      "The spoken route. The patterns that fill conversation, anime and drama " +
      "but get a single line in textbooks — contractions (ちゃう, とく), the " +
      "sentence-ending particles that carry all the attitude, and the casual " +
      "connectives that hold informal speech together.",
    intent: "Following anime, dramas and real conversation without subtitles.",
    accent: "oklch(54% 0.12 40)",
    tint: "oklch(96% 0.024 40)",
    jlptFacet: true,
    match: (d) => d.register.includes("casual-spoken"),
  },
  {
    id: "keigo",
    label: "Keigo",
    h1: "Keigo — Polite & Business Japanese Grammar",
    title: "Keigo — Polite & Business Japanese Grammar — Jengo",
    description:
      "The honorific system, mapped: 尊敬語, 謙譲語 and 丁寧語 — the respectful, " +
      "humble and polite grammar that workplace and service Japanese runs on, " +
      "with examples and furigana.",
    lede:
      "The keigo route. Japan's honorific system — respectful (尊敬語), humble " +
      "(謙譲語) and polite (丁寧語) — is the grammar that workplace, service and " +
      "formal Japanese is built on. Here it is as one connected set instead of a " +
      "scattered list of special verbs.",
    intent: "Working in Japanese, or any setting where register is everything.",
    accent: "oklch(46% 0.10 156)",
    tint: "oklch(96% 0.018 156)",
    jlptFacet: true,
    match: (d) => d.keigo !== "none",
  },
];

export const GOAL_BY_ID = new Map(GOALS.map((g) => [g.id, g]));
