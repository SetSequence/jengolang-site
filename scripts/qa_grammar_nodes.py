"""
qa_grammar_nodes.py

Quality-assurance pass over enriched grammar-node CSV(s) — the catch-net for the
enrichment pass (esp. agent fan-out drift on the clean bulk). Implements the
CALIBRATION.md §14 checklist. Stdlib only.

It is designed to run over SEVERAL files at once (e.g. the high-risk file plus
each agent's clean shard) so that slug-uniqueness and prereq-resolution are
checked GLOBALLY, not per shard.

Checks
  hard (exit 1):
    - enum out of range (register set / keigo / freq / jlpt / family / confidence)
    - duplicate slug across ALL loaded rows
    - candidate_prereqs slug that neither resolves to a node nor is *-prefixed
    - (with --source) a collision/garble source row missing from the enriched set
  soft (reported, no fail):
    - confidence!=high with empty review_reason  (flagged row needs a reason)
    - confidence==high WITH a review_reason       (info: high rows should be clean)
    - canonical empty while confidence!=low
    - term carries a homograph marker but came back high + no senses + no reason
      (likely an undisambiguated collision — eyeball it)
  reports (no flags):
    - per-file freq / family / jlpt histograms + cross-file outlier hints
    - (with --source) clean-pass coverage: how many clean rows remain
    - a random spot-read sample (~--sample-pct of rows)

Usage
    python3 scripts/qa_grammar_nodes.py                         # QA grammar_enriched.csv
    python3 scripts/qa_grammar_nodes.py FILE1 FILE2 ...         # QA several shards together
    python3 scripts/qa_grammar_nodes.py --source grammar_nodes.csv   # + coverage cross-check
    python3 scripts/qa_grammar_nodes.py --sample-pct 15 --out qa.csv

Outputs: prints the report; writes flagged rows + a `qa_flags` column to --out
         (default scripts/data/grammar_enrich_qa.csv).
"""
from __future__ import annotations

import argparse
import csv
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

OCR = Path(__file__).resolve().parent / "data"  # in-repo catalog dir (was ocr_output)

# --- enum vocab — MUST stay in sync with enrich_grammar_nodes.py SCHEMA ---------
REGISTERS = {"casual-spoken", "polite-spoken", "written-modern", "literary", "archaic"}
KEIGO = {"none", "teineigo", "sonkeigo", "kenjougo"}
FREQ = {"essential", "common", "uncommon", "rare"}
JLPT = {"N5", "N4", "N3", "N2", "N1", "none"}
FAMILY = {
    "conditional", "causative", "passive", "aspect", "modality", "quotation",
    "connective", "nominalizer", "particle", "auxiliary", "adverbial",
    "honorific", "copula", "counter", "interjection", "other",
    "adjective",  # い/な-adjective conjugation (Foundations adjectives unit)
    "form",  # promoted form anchors: te-form, masu-stem, ta-form, … (Build step 1)
}
CONFIDENCE = {"high", "med", "low"}

HOMOGRAPH_RE = re.compile(r"[¹²³⁴⁵⁶⁷⁸⁹⁰2'’`]+\s*$")


def slugify(term: str) -> str:
    """Approximate the CALIBRATION slug rule — for matching prereqs to source terms.
    Not exact (hand slugs add -N for homographs), but enough to tell a pending
    prereq (a real grammar point still unenriched) from a dangling typo."""
    t = re.sub(r"^[>\-~\s]*\d*\s*", "", term)        # leading junk: >, -, ~N, digits
    t = HOMOGRAPH_RE.sub("", t).strip()
    t = t.replace("(", "").replace(")", "")
    t = re.sub(r"[~\s/]+", "-", t.strip())
    t = re.sub(r"[^a-z0-9\-]", "", t.lower())
    return re.sub(r"-+", "-", t).strip("-")

REQUIRED_COLS = {"term", "slug", "register", "keigo", "freq", "jlpt", "family",
                 "candidate_prereqs", "confidence", "review_reason"}


def load(paths: list[Path]) -> list[dict]:
    rows: list[dict] = []
    for p in paths:
        if not p.exists():
            sys.exit(f"file not found: {p}")
        with p.open(encoding="utf-8") as f:
            rdr = csv.DictReader(f)
            missing = REQUIRED_COLS - set(rdr.fieldnames or [])
            if missing:
                sys.exit(f"{p.name} missing columns: {sorted(missing)}")
            for r in rdr:
                r["_file"] = p.name
                rows.append(r)
    return rows


def check_row(r: dict) -> tuple[list[str], list[str]]:
    """Return (hard_flags, soft_flags) for one row."""
    hard, soft = [], []

    regs = [x for x in (r["register"] or "").split("|") if x]
    if not regs:
        hard.append("register_empty")
    for x in regs:
        if x not in REGISTERS:
            hard.append(f"bad_register:{x}")
    if r["keigo"] not in KEIGO:
        hard.append(f"bad_keigo:{r['keigo']}")
    if r["freq"] not in FREQ:
        hard.append(f"bad_freq:{r['freq']}")
    if r["jlpt"] not in JLPT:
        hard.append(f"bad_jlpt:{r['jlpt']}")
    if r["family"] not in FAMILY:
        hard.append(f"bad_family:{r['family']}")
    if r["confidence"] not in CONFIDENCE:
        hard.append(f"bad_confidence:{r['confidence']}")

    conf = r["confidence"]
    reason = (r["review_reason"] or "").strip()
    if conf in {"med", "low"} and not reason:
        soft.append("flagged_no_reason")
    if not (r.get("canonical") or "").strip() and conf != "low":
        soft.append("empty_canonical_not_low")
    return hard, soft


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", default=[str(OCR / "grammar_enriched.csv")],
                    help="enriched CSV(s); default grammar_enriched.csv")
    ap.add_argument("--source", default=None,
                    help="grammar_nodes.csv — enables collision/garble coverage check")
    ap.add_argument("--merges", default=None,
                    help="dedup_decisions.json — a source term merged into an existing "
                         "survivor node counts as covered (not missing) in the coverage check")
    ap.add_argument("--sample-pct", type=float, default=10.0,
                    help="percent of rows to print for spot-reading (default 10)")
    ap.add_argument("--out", default=str(OCR / "grammar_enrich_qa.csv"))
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    paths = [Path(f) if Path(f).is_absolute() else (OCR / f if (OCR / f).exists() else Path(f))
             for f in args.files]
    rows = load(paths)
    print(f"loaded {len(rows)} records from {len(paths)} file(s): {[p.name for p in paths]}\n")

    hard_total = 0
    flagged: list[dict] = []
    for r in rows:
        hard, soft = check_row(r)
        if hard or soft:
            r2 = dict(r)
            r2["qa_flags"] = ";".join(hard + soft)
            flagged.append(r2)
            hard_total += len(hard)

    # ---- global slug uniqueness ----
    by_slug: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_slug[r["slug"]].append(r)
    dup_slugs = {s: v for s, v in by_slug.items() if len(v) > 1}
    if dup_slugs:
        hard_total += len(dup_slugs)
        for s, v in dup_slugs.items():
            for r in v:
                r2 = dict(r); r2["qa_flags"] = f"dup_slug:{s}"
                flagged.append(r2)

    # ---- load source (for prereq pending/dangling split + coverage) ----
    src_rows = None
    source_slugs: set[str] = set()
    if args.source:
        sp = Path(args.source) if Path(args.source).is_absolute() else OCR / args.source
        src_rows = list(csv.DictReader(sp.open(encoding="utf-8")))
        source_slugs = {slugify(r["term"]) for r in src_rows}

    # ---- prereq resolution ----
    # A bare prereq slug must resolve to an enriched node. When it doesn't:
    #   pending  = it slugifies to a real source term still unenriched (will resolve
    #              once the clean pass creates that node) -> soft, not a failure.
    #   dangling = matches no node and no source term -> likely a typo or should be
    #              *-prefixed -> hard error.
    # Without --source we cannot tell them apart, so all unresolved are hard.
    slug_set = set(by_slug)
    pending: list[tuple[str, str]] = []
    dangling: list[tuple[str, str]] = []
    for r in rows:
        for pre in (r["candidate_prereqs"] or "").split("|"):
            pre = pre.strip()
            if not pre or pre.startswith("*") or pre in slug_set:
                continue
            if args.source and pre in source_slugs:
                pending.append((r["slug"], pre))
            else:
                dangling.append((r["slug"], pre))
    hard_total += len(dangling)

    # ---- report: errors ----
    print("=" * 60)
    print(f"HARD ERRORS: {hard_total}")
    if dup_slugs:
        print(f"  duplicate slugs ({len(dup_slugs)}): {list(dup_slugs)[:10]}")
    enum_bad = [r for r in flagged if any(f.startswith(('bad_', 'register_empty')) for f in r['qa_flags'].split(';'))]
    if enum_bad:
        print(f"  enum violations ({len(enum_bad)}): "
              f"{[(r['slug'], r['qa_flags']) for r in enum_bad[:8]]}")
    if dangling:
        print(f"  dangling prereqs ({len(dangling)}): {dangling[:10]}")
        print("    (matches no node AND no source term — fix typo or *-prefix it)")
    if hard_total == 0:
        print("  none ✓")

    # ---- report: pending (not failures) ----
    if pending:
        uniq = sorted({p for _, p in pending})
        print(f"\nPENDING PREREQS: {len(pending)} refs to {len(uniq)} unenriched nodes "
              f"(resolve after clean pass): {uniq[:12]}")

    # ---- report: soft flags ----
    soft_counts = Counter()
    for r in flagged:
        for f in r["qa_flags"].split(";"):
            if not f.startswith(("bad_", "register_empty", "dup_slug")):
                soft_counts[f] += 1
    print(f"\nSOFT FLAGS: {sum(soft_counts.values())}")
    for f, n in soft_counts.most_common():
        print(f"  {f}: {n}")

    # ---- info-only signals (expected; not flags) ----
    homo_high = sum(1 for r in rows if HOMOGRAPH_RE.search(r["term"])
                    and r["confidence"] == "high")
    high_noted = sum(1 for r in rows if r["confidence"] == "high"
                     and (r["review_reason"] or "").strip())
    print(f"\nINFO: {homo_high} high-confidence homograph rows (expected — spot-check a few); "
          f"{high_noted} high rows carry a clarifying note")

    # ---- distributions ----
    print("\n" + "=" * 60)
    print("DISTRIBUTIONS")
    for axis in ("confidence", "freq", "family", "jlpt"):
        c = Counter(r[axis] for r in rows)
        print(f"  {axis}: {dict(c.most_common())}")
    if len(paths) > 1:
        print("\n  per-file freq fractions (outlier hint):")
        for p in paths:
            fr = [r for r in rows if r["_file"] == p.name]
            c = Counter(r["freq"] for r in fr)
            frac = {k: round(c[k] / len(fr), 2) for k in FREQ if c[k]}
            print(f"    {p.name} (n={len(fr)}): {frac}")

    # ---- coverage cross-check ----
    if src_rows is not None:
        hr = {r["term"] for r in src_rows if "collision" in r["risk"] or "garble" in r["risk"]}
        clean = {r["term"] for r in src_rows if not ("collision" in r["risk"] or "garble" in r["risk"])}
        done_terms = {r["term"] for r in rows}
        missing_hr = hr - done_terms
        if args.merges:
            import json as _json
            mdec = _json.load(open(args.merges))
            present = {r["slug"] for r in rows}
            merged_ok = {t for t, surv in mdec.get("merged_terms", {}).items()
                         if surv in present}
            merged_hr = missing_hr & merged_ok
            if merged_hr:
                print(f"\n  ({len(merged_hr)} high-risk terms merged into survivors, "
                      f"covered: {sorted(merged_hr)[:10]})")
            missing_hr = missing_hr - merged_ok
        clean_done = clean & done_terms
        print("\n" + "=" * 60)
        print("COVERAGE (vs source)")
        print(f"  high-risk: {len(hr & done_terms)}/{len(hr)} enriched"
              + (f"  MISSING {len(missing_hr)}: {sorted(missing_hr)[:10]}" if missing_hr else " ✓"))
        print(f"  clean:     {len(clean_done)}/{len(clean)} enriched"
              f"  (remaining {len(clean - done_terms)})")
        if missing_hr:
            hard_total += len(missing_hr)

    # ---- spot-read sample ----
    random.seed(args.seed)
    k = max(1, round(len(rows) * args.sample_pct / 100))
    sample = random.sample(rows, min(k, len(rows)))
    print("\n" + "=" * 60)
    print(f"SPOT-READ SAMPLE ({len(sample)} rows — verify against CALIBRATION.md)")
    for r in sorted(sample, key=lambda x: x["slug"]):
        print(f"  {r['slug']:22} {r.get('canonical',''):14} [{r['freq']}/{r['family']}/{r['jlpt']}/{r['confidence']}] "
              f"{r.get('meaning','')[:46]}")

    # ---- write flagged ----
    if flagged:
        out = Path(args.out) if Path(args.out).is_absolute() else OCR / args.out
        cols = [c for c in rows[0] if c != "_file"] + ["qa_flags"]
        # dedupe flagged rows (a row can be flagged by both row-check and slug-check)
        merged: dict[tuple, dict] = {}
        for r in flagged:
            key = (r["_file"], r["slug"], r["term"])
            if key in merged:
                merged[key]["qa_flags"] += ";" + r["qa_flags"]
            else:
                merged[key] = r
        with out.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            w.writerows(merged.values())
        print(f"\nwrote {len(merged)} flagged rows -> {out}")

    print(f"\n{'FAIL' if hard_total else 'PASS'} (hard errors: {hard_total})")
    sys.exit(1 if hard_total else 0)


if __name__ == "__main__":
    main()
