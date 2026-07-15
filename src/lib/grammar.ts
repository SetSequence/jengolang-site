// Shared grammar-catalog taxonomy + helpers.
// Single source of truth for the tree hub (index.astro) and the goal-route
// landing pages (path/[goal].astro), so family order, ranks and colours never
// drift between the two views.

export const FAMILY_ORDER = [
  "particle", "copula", "adjective", "aspect", "conditional", "auxiliary",
  "modality", "quotation", "nominalizer", "causative", "passive", "honorific",
  "connective", "adverbial", "counter", "form", "interjection", "other",
] as const;

export const FAMILY_LABEL: Record<string, string> = {
  particle: "Particles", copula: "Copula", adjective: "Adjectives",
  aspect: "Aspect & phase",
  conditional: "Conditionals", auxiliary: "Auxiliaries", modality: "Modality & mood",
  quotation: "Quotation & report", nominalizer: "Nominalizers",
  causative: "Causative", passive: "Passive", honorific: "Keigo & honorifics",
  connective: "Connectives", adverbial: "Adverbials", counter: "Counters",
  form: "Verb forms", interjection: "Interjections", other: "Other",
};

export const FREQ_RANK: Record<string, number> = {
  essential: 0, common: 1, uncommon: 2, rare: 3,
};
export const JLPT_RANK: Record<string, number> = {
  N5: 0, N4: 1, N3: 2, N2: 3, N1: 4, none: 5,
};

export const jlptColor: Record<string, string> = {
  N5: "oklch(55% 0.10 156)",
  N4: "oklch(55% 0.10 200)",
  N3: "oklch(55% 0.11 250)",
  N2: "oklch(52% 0.12 300)",
  N1: "oklch(50% 0.13 340)",
  none: "oklch(60% 0.01 156)",
};

// Node titles are "canonical — gloss"; pull the gloss for the card meaning line.
export function glossOf(d: { title: string }): string {
  const i = d.title.indexOf("—");
  return i >= 0 ? d.title.slice(i + 1).trim() : d.title;
}

export interface CardNode {
  slug: string;
  canonical: string;
  reading: string;
  gloss: string;
  register: string[];
  freq: string;
  jlpt: string;
  family: string;
  written: boolean;
}

export interface FamilyGroup {
  key: string;
  label: string;
  nodes: CardNode[];
}

// Group view-model nodes by family in FAMILY_ORDER; within a family, sort by
// frequency, then JLPT, then canonical surface. Empty families are dropped.
export function groupByFamily(nodes: CardNode[]): FamilyGroup[] {
  const byFamily = new Map<string, CardNode[]>();
  for (const n of nodes) {
    if (!byFamily.has(n.family)) byFamily.set(n.family, []);
    byFamily.get(n.family)!.push(n);
  }
  return FAMILY_ORDER.filter((f) => byFamily.has(f)).map((f) => ({
    key: f,
    label: FAMILY_LABEL[f] ?? f,
    nodes: byFamily.get(f)!.sort(
      (a, b) =>
        (FREQ_RANK[a.freq] ?? 9) - (FREQ_RANK[b.freq] ?? 9) ||
        (JLPT_RANK[a.jlpt] ?? 9) - (JLPT_RANK[b.jlpt] ?? 9) ||
        a.canonical.localeCompare(b.canonical, "ja"),
    ),
  }));
}
