// Confusable-comparison sets (CRITIQUE.md P1.3 / ON-RAILS §7.3 item 3).
// A "compare set" is a small hand-curated group of grammar points learners
// routinely mix up (the four conditionals first). The side-by-side page at
// /learn/japanese/grammar/compare/[set] AGGREGATES data that already lives on
// the member nodes — each node's keySentence, equivalents, and contrasts[] —
// rather than authoring new grammar prose. Only the framing copy here is new.
//
// `members` are node slugs in teaching order. `family` lets the hub's family
// header link to the set. Every member should carry a contrasts[] entry for
// each other member so the pairwise grid is complete (verified for conditionals).

export interface CompareSet {
  id: string; // URL slug
  label: string; // short list-y label for chips/links, e.g. "と・ば・たら・なら"
  family: string; // grammar family whose hub header links here (one set per family)
  h1: string;
  title: string; // <title> + og
  description: string; // meta description (SEO query target)
  lede: string;
  members: string[]; // node slugs, teaching order
}

export const COMPARE_SETS: CompareSet[] = [
  {
    id: "conditionals",
    label: "と・ば・たら・なら",
    family: "conditional",
    h1: "と, ば, たら, なら — which Japanese “if” do you use?",
    title: "と vs ば vs たら vs なら — Japanese Conditionals Compared | Jengo",
    description:
      "The four Japanese conditionals と, ば, たら, and なら side by side: what each one means, when to use it, and the exact differences that trip learners up.",
    lede:
      "Japanese has four ways to say “if / when,” and they are not interchangeable. Here they are side by side — what each one is for, and the specific distinctions between every pair.",
    members: ["to-conditional", "ba", "tara", "nara"],
  },
];

export const COMPARE_BY_ID = new Map(COMPARE_SETS.map((s) => [s.id, s]));

export const compareSetForSlug = (slug: string): CompareSet | undefined =>
  COMPARE_SETS.find((s) => s.members.includes(slug));

export const compareSetForFamily = (family: string): CompareSet | undefined =>
  COMPARE_SETS.find((s) => s.family === family);
