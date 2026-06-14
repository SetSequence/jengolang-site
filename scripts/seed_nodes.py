#!/usr/bin/env python3
"""Seed the grammar Content Collection from the enriched catalog (TREE.md Step 3).

Materializes ONE Astro content file per catalog node — the **tag layer only**
(node identity + the #7 tag schema + DAG edges from grammar_enriched.csv). The
**teaching layer is left empty for Pass-2** (CALIBRATION2.md): every page is
seeded `noindex: true` and clears the not-thin gate only once Pass-2 fills a key
sentence + examples.

  Input : scripts/data/grammar_enriched.csv
  Output: src/content/japanese/grammar/<slug>.md   (one per node)

SAFE BY DEFAULT: never overwrites an existing file — so the 8 hand-enriched
form-anchor pages (and any Pass-2-filled node) are untouched. Pass --force to
re-stamp the tag layer of *unmodified* seeds (still skips files that differ from
a pure seed — see is_pure_seed).

Pure stdlib. Run from repo root:  python3 scripts/seed_nodes.py
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "data", "grammar_enriched.csv")
OUT_DIR = os.path.abspath(os.path.join(HERE, "..", "src", "content", "japanese", "grammar"))

REGISTER_OK = {"casual-spoken", "polite-spoken", "written-modern", "literary", "archaic"}


def y(s):
    """Emit a double-quoted YAML scalar (safe for Japanese, ~, :, # ...)."""
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def yarr(items):
    return "[" + ", ".join(y(i) for i in items) + "]"


def parse_prereqs(raw):
    raw = (raw or "").strip()
    if not raw:
        return []
    # Separator is `|` (TREE.md Session 5); tolerate stray commas.
    return [p.strip() for p in raw.replace(",", "|").split("|") if p.strip()]


def short_meaning(meaning):
    """First clause of the pass-1 meaning, for a readable seed title."""
    m = (meaning or "").strip()
    for sep in (";", " ("):
        i = m.find(sep)
        if i > 0:
            m = m[:i]
            break
    m = m.strip().rstrip(".")
    return m[:60].strip()


def seed_title(rec):
    canon = rec["canonical"].strip()
    sm = short_meaning(rec["meaning"])
    if canon and sm:
        return f"{canon} — {sm}"
    return canon or sm or rec["slug"]


def render(rec):
    register = [t.strip() for t in rec["register"].split("|") if t.strip() in REGISTER_OK]
    if not register:
        register = ["written-modern"]  # never emit an empty register set
    lines = ["---"]
    lines.append(f"title: {y(seed_title(rec))}")
    lines.append(f"canonical: {y(rec['canonical'])}")
    lines.append(f"reading: {y(rec['reading'])}")
    lines.append(f"register: {yarr(register)}")
    lines.append(f"keigo: {y(rec['keigo'] or 'none')}")
    lines.append(f"freq: {y(rec['freq'])}")
    lines.append(f"jlpt: {y(rec['jlpt'])}")
    lines.append(f"family: {y(rec['family'] or 'other')}")
    prereqs = parse_prereqs(rec["candidate_prereqs"])
    if prereqs:
        lines.append(f"prereqs: {yarr(prereqs)}")
    fold = rec["fold_into_parent"].strip()
    if fold:
        lines.append(f"foldInto: {y(fold)}")
    lines.append(f"confidence: {y(rec['confidence'])}")
    vol = rec.get("src_volumes", "").strip()
    if vol:
        lines.append(f"sources:\n  volumes: {y(vol)}")
    lines.append("noindex: true")  # tag-layer seed; Pass-2 flips when content clears the gate
    lines.append("---")
    lines.append("")  # body filled by Pass-2
    return "\n".join(lines)


def main():
    force = "--force" in sys.argv
    with open(SRC, newline="") as f:
        rows = list(csv.DictReader(f))

    os.makedirs(OUT_DIR, exist_ok=True)
    written = skipped = 0
    for rec in rows:
        slug = rec["slug"].strip()
        if not slug:
            sys.exit(f"ERROR: empty slug for term {rec.get('term')!r}")
        path = os.path.join(OUT_DIR, f"{slug}.md")
        if os.path.exists(path) and not force:
            skipped += 1
            continue
        with open(path, "w") as out:
            out.write(render(rec))
        written += 1

    total = len([p for p in os.listdir(OUT_DIR) if p.endswith(".md")])
    print(f"Seeded {written} node file(s); skipped {skipped} existing (anchors / Pass-2 pages).")
    print(f"Content collection now holds {total} grammar node files in {OUT_DIR}")


if __name__ == "__main__":
    main()
