import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

// Per-node grammar content schema — LOCKED in TREE.md ("Per-node content schema").
// Tag layer = seeded from grammar_enriched.csv; teaching layer = Pass-2 (CALIBRATION2.md).
// Every teaching slot is OPTIONAL: presence is a per-node judgment call, not a default.

const register = z.enum([
  "casual-spoken",
  "polite-spoken",
  "written-modern",
  "literary",
  "archaic",
]);

// jp uses 漢字{かんじ} furigana markup → parsed to <ruby> at render time.
const ex = z.object({
  jp: z.string(),
  en: z.string(),
  note: z.string().optional(),
  level: z.enum(["intro", "core", "advanced"]).optional(),
});

// A sense = the sense-defining slots; only present on multi-sense (>=2) nodes.
const sense = z.object({
  label: z.string(),
  equivalents: z.array(z.string()).default([]),
  keySentence: ex.optional(),
  examples: z.array(ex).default([]),
});

const grammar = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/japanese/grammar" }),
  schema: z.object({
    // — tag layer (seeded from grammar_enriched.csv) → Header badges —
    title: z.string(),
    canonical: z.string(),
    reading: z.string(),
    register: z.array(register),
    keigo: z.enum(["none", "teineigo", "sonkeigo", "kenjougo"]),
    freq: z.enum(["essential", "common", "uncommon", "rare"]),
    jlpt: z.enum(["N5", "N4", "N3", "N2", "N1", "none"]),
    family: z.string(),
    prereqs: z.array(z.string()).default([]), // slugs — NAV chrome (rail)
    related: z.array(z.string()).default([]), // see-also slugs — NAV chrome
    foldInto: z.string().optional(),
    confidence: z.enum(["high", "med", "low"]),
    stage: z
      .object({ line: z.string(), index: z.number(), label: z.string() })
      .optional(),
    sources: z
      .object({ volumes: z.string().optional(), external: z.string().optional() })
      .optional(),

    // — teaching layer (Pass-2; every field below is an OPTIONAL slot) —
    nuance: z.string().optional(), // 2 Meaning — short optional prose
    equivalents: z.array(z.string()).default([]), // 2 Meaning
    keySentence: ex.optional(), // 3 hero, base form
    examples: z.array(ex).default([]), // 6 full set
    senses: z.array(sense).optional(), // present ONLY for multi-sense (>=2)
    formation: z
      .array(
        z.object({
          attaches_to: z.string(),
          form: z.string(),
          example: z.string().optional(),
          sense: z.string().optional(),
        }),
      )
      .default([]), // 4
    usageSetting: z.string().optional(), // 4 where/when deployed
    variants: z
      .array(
        z.object({
          form: z.string(),
          reading: z.string().optional(),
          register: z.array(register).optional(),
          note: z.string().optional(),
        }),
      )
      .default([]), // 5
    restrictions: z
      .array(z.object({ text: z.string(), sense: z.string().optional() }))
      .default([]), // 7
    contrasts: z
      .array(
        z.object({
          slug: z.string(),
          label: z.string(),
          distinction: z.string(),
          sense: z.string().optional(),
        }),
      )
      .default([]), // 8
    notes: z
      .array(z.object({ text: z.string(), sense: z.string().optional() }))
      .default([]), // 9 residual only
    noindex: z.boolean().default(true), // tiered SEO fill
  }),
});

export const collections = { grammar };
