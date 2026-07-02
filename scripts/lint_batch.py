#!/usr/bin/env python3
"""Pre-build lint for a Pass-2 enrichment batch (stdlib only, fast).

Catches the issues that otherwise only surface during `npm run build` (or worse,
not at all): furigana brace imbalance, dangling contrast/prereq slugs, and
sense-refs that don't match a senses[].label. Run it over the slugs you just
edited before the full build.

  python3 scripts/lint_batch.py he-iku kuru ni-iku        # specific slugs
  python3 scripts/lint_batch.py --all                     # every node
  python3 scripts/lint_batch.py --enriched                # only noindex:false nodes

Exit code 1 if any problem is found (so it can gate a build).
"""
import argparse
import glob
import os
import re
import sys

CONTENT_DIR = "src/content/japanese/grammar"


def front_of(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    return m.group(1) if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*", help="slugs to lint (omit with --all/--enriched)")
    ap.add_argument("--all", action="store_true", help="lint every node")
    ap.add_argument("--enriched", action="store_true", help="lint only noindex:false nodes")
    args = ap.parse_args()

    all_slugs = {os.path.basename(f)[:-3] for f in glob.glob(os.path.join(CONTENT_DIR, "*.md"))}

    if args.all or args.enriched:
        targets = []
        for s in sorted(all_slugs):
            front = front_of(open(os.path.join(CONTENT_DIR, s + ".md"), encoding="utf-8").read())
            if args.enriched and "noindex: true" in front:
                continue
            targets.append(s)
    else:
        targets = args.slugs
    if not targets:
        ap.error("give slugs, or --all / --enriched")

    problems = 0
    for s in targets:
        path = os.path.join(CONTENT_DIR, s + ".md")
        if not os.path.exists(path):
            print(f"MISSING file: {s}")
            problems += 1
            continue
        text = open(path, encoding="utf-8").read()

        # furigana: brace balance + no empty {} in every jp string
        for jp in re.findall(r'jp:\s*"([^"]*)"', text):
            if jp.count("{") != jp.count("}"):
                print(f"BRACE imbalance  {s}: {jp}")
                problems += 1
            if "{}" in jp:
                print(f"EMPTY furigana   {s}: {jp}")
                problems += 1

        # dangling contrast / related slugs
        for sl in re.findall(r'slug:\s*"([^"]+)"', text):
            if sl not in all_slugs:
                print(f"DANGLING contrast {s} -> {sl}")
                problems += 1

        # prereqs must exist as a node or be a *-anchor
        for block in re.findall(r'prereqs:\s*\[([^\]]*)\]', text):
            for p in re.findall(r'"([^"]+)"', block):
                if p not in all_slugs and not p.startswith("*"):
                    print(f"DANGLING prereq  {s} -> {p}")
                    problems += 1

        # foreign-script intrusions (Hangul/Jamo/Cyrillic) — OCR/IME slips that build silently
        for i, line in enumerate(text.splitlines(), 1):
            if re.search(r"[가-힣ᄀ-ᇿ㄰-㆏Ѐ-ӿ]", line):
                print(f"FOREIGN script   {s}:{i}: {line.strip()[:80]}")
                problems += 1

        # every sense:<label> ref must match a senses[].label
        labels = set(re.findall(r'-\s*label:\s*"([^"]+)"', text))
        for ref in re.findall(r'\n\s+sense:\s*"([^"]+)"', text):
            if ref not in labels:
                print(f"SENSE-REF        {s} -> {ref} (no matching senses[].label)")
                problems += 1

    n = len(targets)
    if problems:
        print(f"\nLINT FAIL — {problems} problem(s) across {n} node(s)")
        sys.exit(1)
    print(f"LINT OK — {n} node(s) clean")


if __name__ == "__main__":
    main()
