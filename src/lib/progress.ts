// Client-side grammar progress store (localStorage), shared by the path index,
// unit pages, and node pages so the schema and key never drift between them.
const KEY = "jengo.grammar.progress.v1";

export interface Progress {
  revision: number;
  nodes: Record<string, ProgressNode>;
}

export interface ProgressNode {
  state: "learned" | "unlearned";
  updated_at: string;
}

export function loadProgress(): Progress {
  try {
    const saved = JSON.parse(localStorage.getItem(KEY) || "null");
    if (saved) {
      const now = new Date().toISOString();
      const nodes = Object.fromEntries(Object.entries(saved.nodes || {}).map(([slug, value]) => [
        slug,
        typeof value === "string"
          ? { state: value === "auto-verified" ? "learned" : value, updated_at: now }
          : value,
      ]));
      const state = { revision: 1, nodes } as Progress;
      try { localStorage.setItem(KEY, JSON.stringify(state)); } catch {}
      return state;
    }
  } catch {}
  return { revision: 1, nodes: {} };
}

export function setLearned(state: Progress, slug: string, learned: boolean) {
  state.nodes[slug] = {
    state: learned ? "learned" : "unlearned",
    updated_at: new Date().toISOString(),
  };
}

export function saveProgress(state: Progress, slugs: string[] = []) {
  try { localStorage.setItem(KEY, JSON.stringify(state)); } catch {}
  if (window.self !== window.top && slugs.length) {
    window.parent.postMessage({
      type: "jengo:grammar-progress-change",
      changes: slugs.map((slug) => ({ slug, ...state.nodes[slug] })),
    }, "*");
  }
}

export function connectProgress(render: (state: Progress) => void) {
  const bridge = ((window as any).__jengoProgressBridge ||= {});
  bridge.render = render;
  if (!bridge.installed) {
    bridge.installed = true;
    window.addEventListener("message", (event) => {
      if (event.source !== window.parent) return;
      if (event.data?.type !== "jengo:grammar-progress" || !event.data.state) return;
      const local = loadProgress();
      const incoming = event.data.state as Progress;
      const changes = [];
      for (const [slug, node] of Object.entries(local.nodes)) {
        const other = incoming.nodes[slug];
        if (!other || node.updated_at > other.updated_at) {
          incoming.nodes[slug] = node;
          changes.push({ slug, ...node });
        }
      }
      try { localStorage.setItem(KEY, JSON.stringify(incoming)); } catch {}
      bridge.render?.(incoming);
      if (changes.length) {
        window.parent.postMessage({ type: "jengo:grammar-progress-change", changes }, "*");
      }
    });
  }
  if (window.self !== window.top) {
    window.parent.postMessage({ type: "jengo:grammar-progress-request" }, "*");
  }
}

export const isLearned = (state: Progress, slug: string) =>
  state.nodes[slug]?.state === "learned";
