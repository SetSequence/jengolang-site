// Client-side grammar progress store (localStorage), shared by the path index,
// unit pages, and node pages so the schema and key never drift between them.
const KEY = "jengo.grammar.progress.v1";

export interface Progress {
  revision: number;
  nodes: Record<string, string>;
}

export function loadProgress(): Progress {
  try {
    const saved = JSON.parse(localStorage.getItem(KEY) || "null");
    if (saved) return { revision: 1, ...saved, nodes: saved.nodes || {} };
  } catch {}
  return { revision: 1, nodes: {} };
}

export const saveProgress = (state: Progress) =>
  localStorage.setItem(KEY, JSON.stringify(state));

export const isLearned = (state: Progress, slug: string) =>
  state.nodes[slug] === "learned" || state.nodes[slug] === "auto-verified";
