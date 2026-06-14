#!/usr/bin/env python3
"""Apply the same-surface dedup decisions (TREE/SLICE Finding 3) to the catalog.

Reads scripts/data/dedup_decisions.json (dropped_slug -> survivor_slug), drops the
merged rows from grammar_enriched.csv, and repoints every prereq / fold_into_parent
reference from a dropped slug to its survivor. Pure stdlib, re-runnable (idempotent:
once the dropped rows are gone there is nothing left to drop).

Safety gates (hard-exit on any violation):
  - every survivor exists in the catalog
  - no survivor is itself a dropped slug (no merge chains)
  - no dropped slug is part of the build_slice.py curated path
Writes a decision log to scripts/data/dedup_applied.md.
"""
import csv, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "data", "grammar_enriched.csv")
DEC_PATH = os.path.join(HERE, "data", "dedup_decisions.json")
LOG_PATH = os.path.join(HERE, "data", "dedup_applied.md")
BUILD_PATH = os.path.join(HERE, "build_slice.py")

csv.field_size_limit(10**7)


def parse_refs(s):
    """Split a prereq/ref field into tokens, preserving order. Sep is | (and , legacy)."""
    return [t.strip() for t in re.split(r"[|,]", s or "") if t.strip()]


def main():
    dec = json.load(open(DEC_PATH))
    merges = dec["merges"]

    with open(CSV_PATH, newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)

    slugs = {r["slug"] for r in rows}

    # --- safety gates -------------------------------------------------------
    errs = []
    for dropped, survivor in merges.items():
        if dropped not in slugs:
            errs.append(f"dropped slug not in catalog (already merged?): {dropped}")
        if survivor not in slugs:
            errs.append(f"survivor slug not in catalog: {survivor}")
        if survivor in merges:
            errs.append(f"merge chain: {dropped}->{survivor} but {survivor} is also dropped")

    # no dropped slug may be part of the curated slice path
    build_src = open(BUILD_PATH).read()
    curated = set(re.findall(r'"([a-z0-9][a-z0-9-]*)"', build_src))
    for dropped in merges:
        if dropped in curated:
            errs.append(f"dropped slug is in build_slice curated path: {dropped}")

    if errs:
        print("SAFETY GATE FAILED:")
        for e in errs:
            print("  -", e)
        sys.exit(1)

    # --- apply: drop rows, repoint references -------------------------------
    kept = [r for r in rows if r["slug"] not in merges]
    dropped_rows = [r for r in rows if r["slug"] in merges]

    REF_FIELDS = ("candidate_prereqs", "fold_into_parent")
    repoint_count = {f: 0 for f in REF_FIELDS}
    for r in kept:
        for fld in REF_FIELDS:
            if fld not in r:
                continue
            toks = parse_refs(r.get(fld))
            new = []
            changed = False
            seen = set()
            for t in toks:
                star = t.startswith("*")
                bare = t[1:] if star else t
                if bare in merges:
                    bare = merges[bare]
                    changed = True
                tok = ("*" + bare) if star else bare
                if tok == r["slug"]:        # never self-reference after repoint
                    changed = True
                    continue
                if tok in seen:             # collapse dup refs created by merge
                    changed = True
                    continue
                seen.add(tok)
                new.append(tok)
            if changed:
                repoint_count[fld] += 1
                r[fld] = "|".join(new)

    with open(CSV_PATH, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(kept)

    # --- log ----------------------------------------------------------------
    by_survivor = {}
    for d, s in merges.items():
        by_survivor.setdefault(s, []).append(d)
    with open(LOG_PATH, "w") as f:
        f.write("# Same-surface dedup applied (TREE/SLICE Finding 3)\n\n")
        f.write(f"- Catalog: {len(rows)} -> {len(kept)} nodes ({len(dropped_rows)} merged)\n")
        f.write(f"- Prereq fields repointed: {repoint_count['candidate_prereqs']} rows; "
                f"fold_into_parent repointed: {repoint_count['fold_into_parent']} rows\n\n")
        f.write("## Merges (survivor <- dropped)\n\n")
        for s in sorted(by_survivor):
            f.write(f"- `{s}` <- {', '.join('`'+d+'`' for d in sorted(by_survivor[s]))}\n")

    print(f"OK: {len(rows)} -> {len(kept)} nodes, {len(dropped_rows)} merged.")
    print(f"repointed: prereqs={repoint_count['candidate_prereqs']} rows, "
          f"fold={repoint_count['fold_into_parent']} rows")
    print(f"log -> {LOG_PATH}")


if __name__ == "__main__":
    main()
