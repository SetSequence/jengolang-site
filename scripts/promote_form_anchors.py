#!/usr/bin/env python3
"""Build step 1: promote the 8 *-form anchors to real catalog nodes.

- Adds the 6 missing form-anchor rows (ta-form, nai-form, ba-conditional,
  volitional-form, causative-form, counter); te-form + masu-stem already exist.
- Normalizes all 8 anchors to family=form.
- Flips `*<anchor>` -> `<anchor>` in every row's candidate_prereqs (the 8 forms
  only; leaves the out-of-scope *youni / *toka / *to-quotative / *hodo as-is).

Idempotent: re-running adds nothing new and re-flips nothing already flipped.
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "data", "grammar_enriched.csv")

ANCHOR_SLUGS = [
    "te-form", "masu-stem", "ta-form", "nai-form",
    "ba-conditional", "volitional-form", "causative-form", "counter",
]

# 6 rows to add (te-form + masu-stem already present). Field order matches header.
NEW_ROWS = [
    {  # ta-form
        "term": "Vta", "slug": "ta-form", "canonical": "た形", "reading": "たけい",
        "meaning": "the plain past (た) form of verbs and adjectives; the base for たら, たり, and clauses like 〜たことがある",
        "register": "casual-spoken|polite-spoken|written-modern", "keigo": "none",
        "freq": "essential", "jlpt": "N5", "family": "form",
        "candidate_prereqs": "te-form", "confidence": "high",
        "review_reason": "foundation form (non-catalog anchor *ta-form now realized as a node)",
        "src_volumes": "I",
    },
    {  # nai-form
        "term": "Vnai", "slug": "nai-form", "canonical": "ない形", "reading": "ないけい",
        "meaning": "the plain negative (ない) form of verbs; the base for なかった, なくて, ないで and many negative patterns",
        "register": "casual-spoken|polite-spoken|written-modern", "keigo": "none",
        "freq": "essential", "jlpt": "N5", "family": "form",
        "candidate_prereqs": "", "confidence": "high",
        "review_reason": "foundation form (non-catalog anchor *nai-form now realized as a node)",
        "src_volumes": "I",
    },
    {  # ba-conditional
        "term": "Vba", "slug": "ba-conditional", "canonical": "ば形", "reading": "ばけい",
        "meaning": "the provisional conditional (〜ば) form: 'if/when ~', built from the e-row stem plus ば",
        "register": "casual-spoken|polite-spoken|written-modern", "keigo": "none",
        "freq": "essential", "jlpt": "N4", "family": "form",
        "candidate_prereqs": "", "confidence": "high",
        "review_reason": "foundation form (non-catalog anchor *ba-conditional now realized as a node)",
        "src_volumes": "I",
    },
    {  # volitional-form
        "term": "Vyou", "slug": "volitional-form", "canonical": "意向形", "reading": "いこうけい",
        "meaning": "the volitional (〜よう/おう) form: 'let's ~ / I'll ~ / shall we ~'; the base for ようとする and ようとおもう",
        "register": "casual-spoken|polite-spoken|written-modern", "keigo": "none",
        "freq": "essential", "jlpt": "N4", "family": "form",
        "candidate_prereqs": "", "confidence": "high",
        "review_reason": "foundation form (non-catalog anchor *volitional-form now realized as a node)",
        "src_volumes": "I",
    },
    {  # causative-form
        "term": "Vsaseru", "slug": "causative-form", "canonical": "使役形", "reading": "しえきけい",
        "meaning": "the causative (〜せる/させる) form: 'make/let someone do'; the base for the causative-passive and for 〜させてください",
        "register": "casual-spoken|polite-spoken|written-modern", "keigo": "none",
        "freq": "common", "jlpt": "N4", "family": "form",
        "candidate_prereqs": "nai-form", "confidence": "high",
        "review_reason": "foundation form (non-catalog anchor *causative-form now realized as a node)",
        "src_volumes": "I",
    },
    {  # counter
        "term": "counter", "slug": "counter", "canonical": "助数詞", "reading": "じょすうし",
        "meaning": "counter suffixes attached to numerals to count things, people, and occurrences (〜個, 〜人, 〜回, 〜枚)",
        "register": "casual-spoken|polite-spoken|written-modern", "keigo": "none",
        "freq": "essential", "jlpt": "N5", "family": "form",
        "candidate_prereqs": "", "confidence": "high",
        "review_reason": "foundation form (non-catalog anchor *counter now realized as a node)",
        "src_volumes": "I",
    },
]


def flip_prereqs(raw):
    if not raw:
        return raw
    parts = [p.strip() for p in raw.replace(",", "|").split("|") if p.strip()]
    out = []
    for p in parts:
        if p.startswith("*") and p[1:] in ANCHOR_SLUGS:
            out.append(p[1:])
        else:
            out.append(p)
    return "|".join(out)


def main():
    with open(CSV, newline="") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        rows = list(reader)

    existing = {r["slug"] for r in rows}

    flipped = 0
    for r in rows:
        before = r.get("candidate_prereqs", "")
        after = flip_prereqs(before)
        if after != before:
            r["candidate_prereqs"] = after
            flipped += 1
        # normalize the two pre-existing anchors to family=form
        if r["slug"] in ("te-form", "masu-stem") and r.get("family") != "form":
            r["family"] = "form"

    added = 0
    for nr in NEW_ROWS:
        if nr["slug"] in existing:
            continue
        full = {k: "" for k in header}
        full.update(nr)
        rows.append(full)
        added += 1

    with open(CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)

    print(f"rows now: {len(rows)}  | added: {added}  | prereq-rows flipped: {flipped}")
    remaining = sum(
        1 for r in rows
        for p in (r.get("candidate_prereqs") or "").split("|")
        if p in ("*" + a for a in ANCHOR_SLUGS)
    )
    print(f"remaining *-anchor refs (should be 0): {remaining}")


if __name__ == "__main__":
    main()
