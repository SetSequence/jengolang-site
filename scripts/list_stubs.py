#!/usr/bin/env python3
"""List un-enriched grammar stub nodes, prioritized for Pass-2 long-tail fill.

A "stub" = a Content Collection node whose teaching layer is empty (`noindex: true`).
Pass-2 fill order is LOCKED (TREE.md "Resuming Pass-2 long-tail"): highest-value first
= freq=essential before common before uncommon before rare, and within a freq band,
low JLPT first (N5→N1) because that is where the SEO/GEO traffic is (JENGOLANG.md
content priority). This script just surfaces that worklist so a session doesn't have
to re-derive the query — it reads frontmatter only, no deps.

Usage (from repo root):
  python3 scripts/list_stubs.py                 # full prioritized list + freq counts
  python3 scripts/list_stubs.py --freq essential   # one band (the usual next batch)
  python3 scripts/list_stubs.py --freq common --limit 30
  python3 scripts/list_stubs.py --enriched      # instead list DONE nodes (noindex:false)

Pure stdlib. The render/build is the real validator — after a batch, run `npm run build`
(catches dangling contrast/prereq slugs + schema errors) and the Pass-2 QA hooks in
CALIBRATION2.md §7.
"""
import argparse
import glob
import os
import re

CONTENT_DIR = "src/content/japanese/grammar"
FREQ_ORDER = {"essential": 0, "common": 1, "uncommon": 2, "rare": 3, "": 4}
JLPT_ORDER = {"N5": 0, "N4": 1, "N3": 2, "N2": 3, "N1": 4, "none": 5, "": 6}


def field(front, key):
    m = re.search(rf'^{key}:\s*"?([^"\n]+)"?', front, re.M)
    return m.group(1).strip() if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--freq", choices=["essential", "common", "uncommon", "rare"],
                    help="only this frequency band")
    ap.add_argument("--limit", type=int, default=0, help="cap rows printed (0 = all)")
    ap.add_argument("--enriched", action="store_true",
                    help="list enriched (noindex:false) nodes instead of stubs")
    args = ap.parse_args()

    rows = []
    for path in glob.glob(os.path.join(CONTENT_DIR, "*.md")):
        text = open(path, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---", text, re.S)
        front = m.group(1) if m else ""
        is_stub = "noindex: true" in front
        if args.enriched == is_stub:
            continue  # want enriched but this is a stub (or vice-versa)
        freq = field(front, "freq")
        if args.freq and freq != args.freq:
            continue
        rows.append((freq, field(front, "jlpt"), field(front, "family"),
                     os.path.basename(path)[:-3], field(front, "title")))

    rows.sort(key=lambda r: (FREQ_ORDER.get(r[0], 4), JLPT_ORDER.get(r[1], 6), r[3]))

    label = "ENRICHED" if args.enriched else "STUB"
    from collections import Counter
    counts = Counter(r[0] for r in rows)
    print(f"{len(rows)} {label} nodes"
          + (f" (freq={args.freq})" if args.freq else "")
          + f" — by freq: {dict(counts)}\n")
    shown = rows[: args.limit] if args.limit else rows
    for freq, jlpt, fam, slug, title in shown:
        print(f"  {freq:9} {jlpt:4} {fam:12} {slug:26} {title}")
    if args.limit and len(rows) > args.limit:
        print(f"\n  … {len(rows) - args.limit} more")


if __name__ == "__main__":
    main()
