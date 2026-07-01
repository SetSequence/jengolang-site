#!/usr/bin/env python3
"""Build the grammar skill-tree VERTICAL SLICE (TREE.md Step 4b, item 3).

A vertical slice = the curated **Foundations line** + one **goal branch**
("Read novels" / literary), fully tagged, used to validate the IA model
(prereq-DAG backbone + subway-line tag overlays) BEFORE the tree UI is built.

Input : scripts/data/grammar_enriched.csv  (the enriched catalog)
Output: src/data/grammar_slice.json        (the slice manifest, imported directly
        by the Astro static render at src/pages/learn/japanese/grammar)

What it does:
  1. Loads the enriched catalog.
  2. Resolves the FORM anchors (te-form, masu-stem, ...) — now real catalog rows
     (Build step 1) — and tags them kind="anchor" for their tier-0 form grouping.
  3. Resolves the hand-curated Foundations spine + literary route to real records,
     hard-erroring on any slug that is not in the catalog (catches typos/dups).
  4. Computes tier = prereq depth over the slice sub-DAG (anchors = tier 0).
  5. Validates: slug existence, prereq resolution, Foundations-first ordering,
     and reports curation findings (OCR dup-merges the curation had to resolve).
  6. Emits grammar_slice.json + prints a human-readable report.

Pure stdlib. Run from anywhere:  python3 scripts/build_slice.py
"""
import csv
import json
import os
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))            # jengolang-site/scripts
SRC = os.path.join(HERE, "data", "grammar_enriched.csv")    # the catalog (in-repo)
# Single canonical output: the Astro render imports this directly.
OUT = os.path.abspath(os.path.join(HERE, "..", "src", "data", "grammar_slice.json"))

# ---------------------------------------------------------------------------
# FORM anchors (TREE.md #16 / CALIBRATION §11) — the conjugation bases a learner
# must control. Build step 1 (SLICE Finding 2) PROMOTED these from `*`-prefixed
# non-catalog prereqs to REAL catalog rows + teaching pages, so they now resolve
# straight from grammar_enriched.csv like any other node. They keep a distinct
# tier-0 "form" grouping in the render. Ordered bases-first for display.
# ---------------------------------------------------------------------------
ANCHOR_SLUGS = [
    "verb-classes", "masu-stem", "te-form", "ta-form", "nai-form",
    "ba-conditional", "volitional-form", "causative-form", "counter",
]

# ---------------------------------------------------------------------------
# FOUNDATIONS LINE — the curated, near-linear mandatory spine every goal route
# shares (TREE.md #9). Grouped into pedagogical STAGES — and the stage is the
# real vertical axis, NOT prereq depth: the slice proved the enriched prereq
# DAG is too sparse to layer the spine (it collapses to ≤2 tiers, see report).
# ONE canonical slug per concept; OCR dups deliberately dropped (audited below).
# ---------------------------------------------------------------------------
FOUNDATION_STAGES = [
    ("Copula & the は～だ frame",  ["da", "desu", "wa-2", "no-3", "janai", "datta"]),
    ("Core case & binding particles",
        ["ga-2", "o", "ni-2", "ni-3", "de", "ka", "e", "to-2", "mo", "kara-3",
         "made", "ne", "yo"]),
    ("Verb bases & politeness",   ["masu-stem", "masu-form", "te-form", "nai", "kudasai"]),
    ("て-form uses & aspect",
        ["te", "te-kudasai", "te-iru", "te-kara", "te-mo-ii", "te-wa-ikenai",
         "te-shimau", "te-miru"]),
    ("Benefactive giving/receiving",
        ["ageru", "kureru", "ageru-2", "kureru-2", "morau"]),
    ("Desire & basic modality",
        ["tai", "hoshii", "darou", "deshou", "kamoshirenai", "hazu"]),
    ("The four conditionals",     ["to-conditional", "tara", "ba", "nara"]),
    ("Clause connectives & temporal frames",
        ["kara", "node", "kedo", "ga-3", "noni", "nagara", "toki", "mae-ni", "ato-de"]),
    ("Nominalizers & comparison",
        ["koto", "no-ga-suki", "no-hou-ga", "yori-no-hou-ga", "ichiban"]),
]
FOUNDATIONS = [s for _, slugs in FOUNDATION_STAGES for s in slugs]

# ---------------------------------------------------------------------------
# READ-NOVELS BRANCH — a subway line (TREE.md #10). The *filter* that lights it
# is register ⊇ {literary, archaic}; the curated *route* below is the bold
# recommended path through that filter, ordered Foundations-first → classical.
# (The full filter membership — all literary/archaic nodes — is computed and
# stored as `filter_members`; the route is the highlighted subset.)
# ---------------------------------------------------------------------------
BRANCH = {
    "id": "read-novels",
    "name": "Read novels",
    "url": "/learn/japanese/grammar/path/read-novels",
    "tagline": "Every grammar point you need to read Japanese literary prose.",
    # the filter preset that defines membership (a query over the tag schema):
    "filter": {"register_any": ["literary", "archaic"]},
    # the curated bold route through the literary set, ordered by dependency.
    # Stages continue the Foundations numbering conceptually (branch begins
    # where Foundations ends) but live on their own labelled rungs.
    "route_stages": [
        ("Written-style copula & classical negatives",
            ["de-aru", "zu", "nu", "neba-naranai", "mai", "de-arou"]),
        ("Classical auxiliaries: likeness, obligation, prohibition",
            ["gotoshi", "ka-no-gotoku", "beku", "bekarazu"]),
        ("Literary particles of restriction & emphasis",
            ["nomi", "sura", "dani", "tsutsu"]),
        ("Literary connectives & temporal 'as soon as'",
            ["nari", "ya-ina-ya", "to-ie-domo", "mono-o", "yue-ni", "katsute",
             "ni-atte", "ori-ni"]),
    ],
}
BRANCH["route"] = [s for _, slugs in BRANCH["route_stages"] for s in slugs]

# ---------------------------------------------------------------------------
# GOAL PATHS (ON-RAILS.md) — membership + ordering for every goal route live
# build-side (single source of truth; goals.ts is presentation only). Each goal
# becomes an ORDERED, BANDED path: the band is the numbered backbone, the first
# band's first few nodes are the "start here" rail. Order within a band is by
# frequency (the "what next" signal in a shallow forest), then JLPT, family,
# surface. The band AXIS is goal-type-specific — whatever the learner reasons in.
# ---------------------------------------------------------------------------
FREQ_RANK = {"essential": 0, "common": 1, "uncommon": 2, "rare": 3}
JLPT_RANK = {"N5": 0, "N4": 1, "N3": 2, "N2": 3, "N1": 4, "none": 5}
# mirrors lib/grammar.ts FAMILY_ORDER so within-band order never drifts
FAMILY_ORDER = [
    "particle", "copula", "aspect", "conditional", "auxiliary", "modality",
    "quotation", "nominalizer", "causative", "passive", "honorific",
    "connective", "adverbial", "counter", "form", "interjection", "other",
]
FAM_RANK = {f: i for i, f in enumerate(FAMILY_ORDER)}
JLPT_LEVELS = ["N5", "N4", "N3", "N2", "N1"]

# keigo bands: pedagogical order polite → respectful → humble (§2)
KEIGO_BANDS = [
    ("teineigo", "丁寧語 — Polite (です・ます register)"),
    ("sonkeigo", "尊敬語 — Respectful (elevating others)"),
    ("kenjougo", "謙譲語 — Humble (lowering yourself)"),
]
# casual bands: freq is the honest axis (948 nodes, only generic families) (§2)
FREQ_BANDS = [
    ("essential", "Spoken essentials — start here"),
    ("common", "Core conversational patterns"),
    ("uncommon", "Less common, still useful"),
    ("rare", "Rare & advanced spoken"),
]

GOAL_SPECS = [
    {"id": "jlpt-n5", "axis": "jlpt", "level": "N5"},
    {"id": "jlpt-n4", "axis": "jlpt", "level": "N4"},
    {"id": "jlpt-n3", "axis": "jlpt", "level": "N3"},
    {"id": "jlpt-n2", "axis": "jlpt", "level": "N2"},
    {"id": "jlpt-n1", "axis": "jlpt", "level": "N1"},
    {"id": "read-novels", "axis": "curated"},
    {"id": "casual-spoken", "axis": "freq",
        "member": lambda r: "casual-spoken" in r["register"]},
    {"id": "keigo", "axis": "keigo", "member": lambda r: r["keigo"] != "none"},
]


def goal_sort_key(r):
    """Within-band order: freq → JLPT → family → surface (ON-RAILS §1.2)."""
    return (
        FREQ_RANK.get(r.get("freq", ""), 9),
        JLPT_RANK.get(r.get("jlpt", ""), 9),
        FAM_RANK.get(r.get("family", ""), 99),
        r.get("canonical", ""),
    )


def build_goals(all_rows, branch_route, filter_members, spine_slugs):
    """Compute the ordered, banded path for every goal (ON-RAILS §1, §2).

    `spine_slugs` = Foundations + anchors. JLPT goals carry Foundations as a
    numbered Band 0 rendered from slice.foundations, so their own bands EXCLUDE
    spine slugs; register goals show Foundations as a compact spine and likewise
    exclude it. The page joins these slugs to the content collection for written
    state and gloss; here we only need ordering + the slim record."""
    by_slug = {r["slug"]: r for r in all_rows}
    spine = set(spine_slugs)

    def live(r):  # drop folds; they redirect to a parent
        return not (r.get("fold_into_parent") or "").strip()

    goals = []
    for spec in GOAL_SPECS:
        axis = spec["axis"]
        rest = []

        if axis == "jlpt":
            cap = JLPT_RANK[spec["level"]]
            members = [r for r in all_rows
                       if live(r) and r["jlpt"] in JLPT_RANK
                       and r["jlpt"] != "none" and JLPT_RANK[r["jlpt"]] <= cap
                       and r["slug"] not in spine]
            raw_bands = []
            for lvl in JLPT_LEVELS[:cap + 1]:
                ns = sorted([r for r in members if r["jlpt"] == lvl], key=goal_sort_key)
                if ns:
                    raw_bands.append((lvl, f"JLPT {lvl}", ns))
            foundations_mode = "band0"

        elif axis == "keigo":
            members = [r for r in all_rows if live(r) and spec["member"](r)]
            raw_bands = []
            for key, label in KEIGO_BANDS:
                ns = sorted([r for r in members if r["keigo"] == key], key=goal_sort_key)
                if ns:
                    raw_bands.append((key, label, ns))
            foundations_mode = "spine"

        elif axis == "freq":
            members = [r for r in all_rows if live(r) and spec["member"](r)
                       and r["slug"] not in spine]
            raw_bands = []
            for key, label in FREQ_BANDS:
                ns = sorted([r for r in members if r["freq"] == key], key=goal_sort_key)
                if ns:
                    raw_bands.append((key, label, ns))
            foundations_mode = "spine"

        elif axis == "curated":  # read-novels: keep the hand-authored route_stages
            stage_map = {}
            for n in branch_route:
                idx = n["stage"]["index"]
                stage_map.setdefault(idx, [n["stage"]["label"], []])
                stage_map[idx][1].append(by_slug[n["slug"]])
            raw_bands = [(f"stage-{idx}", lbl, ns)
                         for idx, (lbl, ns) in sorted(stage_map.items())]
            route_slugs = {n["slug"] for n in branch_route}
            rest = sorted(s for s in filter_members
                          if s not in route_slugs and s not in spine)
            members = [by_slug[s] for s in filter_members]
            foundations_mode = "spine"
        else:
            raise SystemExit(f"unknown goal axis: {axis}")

        out_bands, order = [], 0
        for i, (key, label, ns) in enumerate(raw_bands, start=1):
            recs = []
            for r in ns:
                order += 1
                rec = slim(r)
                rec["order"] = order
                recs.append(rec)
            out_bands.append({"index": i, "key": key, "label": label, "nodes": recs})

        goals.append({
            "id": spec["id"],
            "band_axis": axis,
            "foundations_mode": foundations_mode,
            "member_count": len(members),
            "path_count": order,
            "bands": out_bands,
            "rest_members": rest,
        })
    return goals


def parse_prereqs(raw):
    raw = (raw or "").strip()
    if not raw:
        return []
    # Separator is `|` (TREE.md Session 5 learning); tolerate stray commas.
    return [p.strip() for p in raw.replace(",", "|").split("|") if p.strip()]


def load_catalog():
    with open(SRC, newline="") as f:
        rows = list(csv.DictReader(f))
    return {r["slug"]: r for r in rows}, rows


def slim(rec):
    """Project a catalog row down to the fields the tree needs."""
    keep = ("slug", "canonical", "reading", "meaning", "senses", "register",
            "keigo", "freq", "jlpt", "family", "candidate_prereqs",
            "fold_into_parent", "confidence", "review_reason")
    out = {k: rec.get(k, "") for k in keep}
    out["kind"] = rec.get("kind", "catalog")
    return out


def resolve(slugs, catalog, anchor_recs, label):
    """Map an ordered slug list to records; hard-error on any miss."""
    recs, missing = [], []
    for s in slugs:
        if s in anchor_recs:
            recs.append(anchor_recs[s])
        elif s in catalog:
            recs.append(slim(catalog[s]))
        else:
            missing.append(s)
    if missing:
        sys.exit(f"ERROR [{label}]: {len(missing)} curated slug(s) not in catalog: {missing}")
    return recs


def compute_tiers(slice_nodes):
    """tier = longest prereq chain inside the slice. Anchors = 0. Prereqs that
    fall outside the slice are ignored for depth (they resolve in the full tree;
    here we only tier the sub-DAG so the layered layout is sensible)."""
    in_slice = {n["slug"]: n for n in slice_nodes}
    tier_cache = {}

    def tier_of(slug, stack):
        if slug in tier_cache:
            return tier_cache[slug]
        if slug in stack:  # cycle guard
            return 0
        node = in_slice.get(slug)
        if node is None or node.get("kind") == "anchor":
            tier_cache[slug] = 0
            return 0
        deps = [p for p in parse_prereqs(node.get("candidate_prereqs"))]
        # normalize *-anchors and only follow prereqs that are in the slice
        depth = 0
        for d in deps:
            if d in in_slice:
                depth = max(depth, 1 + tier_of(d, stack | {slug}))
        tier_cache[slug] = depth
        return depth

    for n in slice_nodes:
        n["tier"] = tier_of(n["slug"], frozenset())
    return slice_nodes


def main():
    catalog, all_rows = load_catalog()
    # Form anchors are now real catalog rows (Build step 1); resolve from the
    # catalog and tag kind="anchor" so they keep their tier-0 "form" grouping.
    missing_anchors = [s for s in ANCHOR_SLUGS if s not in catalog]
    if missing_anchors:
        sys.exit(f"ERROR [anchors]: form anchors not in catalog (promote them first): {missing_anchors}")
    anchor_recs = {s: {**slim(catalog[s]), "kind": "anchor"} for s in ANCHOR_SLUGS}

    # --- resolve curated lists -------------------------------------------------
    foundations = resolve(FOUNDATIONS, catalog, anchor_recs, "foundations")
    anchors_list = [anchor_recs[s] for s in ANCHOR_SLUGS]
    branch_route = resolve(BRANCH["route"], catalog, anchor_recs, "branch.route")

    # stamp the curated STAGE onto every node (the real layout axis) ------------
    stage_of = {}
    for i, (name, slugs) in enumerate(FOUNDATION_STAGES, start=1):
        for s in slugs:
            stage_of[s] = {"index": i, "label": name, "line": "foundations"}
    for j, (name, slugs) in enumerate(BRANCH["route_stages"], start=1):
        for s in slugs:
            stage_of[s] = {"index": j, "label": name, "line": "branch"}
    for n in foundations + branch_route:
        n["stage"] = stage_of[n["slug"]]

    # --- the full literary filter membership (the subway line's lit) -----------
    filter_members = sorted(
        (r["slug"] for r in all_rows
         if "literary" in r["register"] or "archaic" in r["register"]),
    )

    # --- ordered, banded goal paths (ON-RAILS.md) ------------------------------
    goals = build_goals(
        all_rows, branch_route, filter_members,
        spine_slugs=set(FOUNDATIONS) | set(ANCHOR_SLUGS),
    )

    # --- tiering ---------------------------------------------------------------
    all_slice = anchors_list + foundations + branch_route
    # de-dup by slug for tiering (a node may appear in both lists conceptually)
    seen, uniq = set(), []
    for n in all_slice:
        if n["slug"] in seen:
            continue
        seen.add(n["slug"])
        uniq.append(n)
    compute_tiers(uniq)
    tier_by_slug = {n["slug"]: n["tier"] for n in uniq}
    for n in foundations + branch_route + anchors_list:
        n["tier"] = tier_by_slug[n["slug"]]

    # --- validation ------------------------------------------------------------
    findings = []
    slice_slugs = {n["slug"] for n in uniq}

    # (a) prereq resolution: every prereq is a slice node (anchors now included),
    #     a catalog node, or a residual non-anchor *-ref. Report prereqs that fall
    #     outside the slice (these are the "rest of the tree" — expected, counted).
    prereq_outside = {}
    for n in foundations + branch_route:
        for p in parse_prereqs(n.get("candidate_prereqs")):
            base = p
            if base in slice_slugs:
                continue
            if base in catalog:
                prereq_outside.setdefault(n["slug"], []).append(base)
            elif base.startswith("*"):
                # residual out-of-scope *-ref (e.g. *youni) — resolves in full tree
                prereq_outside.setdefault(n["slug"], []).append(base)
            else:
                findings.append(f"DANGLING prereq {base!r} on {n['slug']}")

    # (b) Foundations-first ordering: every branch-route node's IN-SLICE prereqs
    #     must come from Foundations/anchors or earlier in the route (no branch
    #     node depends on a later branch node).
    route_index = {n["slug"]: i for i, n in enumerate(branch_route)}
    found_slugs = {n["slug"] for n in foundations} | set(ANCHOR_SLUGS)
    order_violations = []
    for i, n in enumerate(branch_route):
        for p in parse_prereqs(n.get("candidate_prereqs")):
            if p in route_index and route_index[p] > i:
                order_violations.append((n["slug"], p))

    # (c) Same-surface audit: catalog slugs sharing a canonical surface with a
    #     curated pick. These clusters mix TRUE OCR dups (て/te-2) and GENUINE
    #     sense-splits (が subject / が "but"; を object/path/separation) — and the
    #     two are NOT mechanically separable (the enriched meanings differ even
    #     for real dups). So this is an honest "needs dedup/sense review" flag,
    #     not an auto-merge list. The curation already picked one slug per rung.
    curated = {n["slug"] for n in foundations + branch_route}
    canon_to_slugs = {}
    for r in all_rows:
        canon_to_slugs.setdefault(r["canonical"], []).append(r["slug"])
    same_surface = []
    seen_canon = set()
    for n in foundations + branch_route:
        canon = n["canonical"]
        if not canon or canon in seen_canon:
            continue
        seen_canon.add(canon)
        cluster = canon_to_slugs.get(canon, [])
        if len(cluster) <= 1:
            continue
        kept = [s for s in cluster if s in curated]
        other = [s for s in cluster if s not in curated]
        same_surface.append({"canonical": canon, "kept": kept, "other_in_catalog": other})

    # --- assemble manifest -----------------------------------------------------
    manifest = {
        "generated": str(date.today()),
        "source": f"grammar_enriched.csv ({len(all_rows)} nodes)",
        "purpose": "Vertical slice validating the grammar skill-tree IA "
                   "(Foundations line + one goal branch) before the tree UI.",
        "anchors": anchors_list,
        "foundations": {
            "name": "Foundations",
            "description": "The mandatory near-linear spine every goal route "
                           "shares — copula, core particles, verb bases, the "
                           "て-form/aspect cluster, desire, conditionals, "
                           "connectives, nominalizers and comparison.",
            "node_count": len(foundations),
            "stages": [name for name, _ in FOUNDATION_STAGES],
            "nodes": foundations,
        },
        "branch": {
            **{k: BRANCH[k] for k in ("id", "name", "url", "tagline", "filter")},
            "route_count": len(branch_route),
            "filter_member_count": len(filter_members),
            "stages": [name for name, _ in BRANCH["route_stages"]],
            "route": branch_route,
            "filter_members": filter_members,
        },
        "goals": goals,
        "validation": {
            "foundations_count": len(foundations),
            "branch_route_count": len(branch_route),
            "anchors_count": len(anchors_list),
            "max_prereq_tier": max(n["tier"] for n in uniq),
            "dangling_prereqs": [f for f in findings if f.startswith("DANGLING")],
            "order_violations": order_violations,
            "prereqs_pointing_outside_slice": prereq_outside,
            "same_surface_clusters_need_review": same_surface,
        },
        "findings": [
            "LAYOUT: prereq-depth (decision #6) collapses to <=2 tiers across the "
            "whole slice — the enriched candidate_prereqs mostly point at *-form "
            "anchors, not at each other, so depth cannot order the spine. The "
            "curated STAGE (decision #9) is therefore the real vertical axis; "
            "prereq depth stays a secondary within-stage signal + edge source.",
            "ANCHORS: the 8 form anchors (te-form, masu-stem, ta-form, nai-form, "
            "ba-conditional, volitional-form, causative-form, counter) — referenced "
            "as prereqs ~225x — are now PROMOTED to real catalog rows + teaching "
            "pages (Build step 1); their `*` prereq refs were flipped to bare slugs.",
            "DEDUP: many surfaces carry several catalog slugs (て/te-2 OCR dup; "
            "が subject / が 'but' and を object/path/separation genuine sense-splits). "
            "The two are not mechanically separable, so a same-surface review pass is "
            "needed before the full tree ships; the curation picked one slug per rung.",
            "BRANCH: a register-set filter ('literary'∈register) cleanly selects a "
            "145-node subway line; a 22-node curated route through it is coherent and "
            "attaches to Foundations with zero ordering violations.",
        ],
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    # --- report ----------------------------------------------------------------
    v = manifest["validation"]
    print(f"Slice built from {len(all_rows)} catalog nodes.")
    print(f"  anchors (tier-0 forms) : {v['anchors_count']}")
    print(f"  Foundations line       : {v['foundations_count']} nodes")
    print(f"  Read-novels route      : {v['branch_route_count']} nodes "
          f"(of {len(filter_members)} in the literary filter)")
    print(f"  max prereq tier        : {v['max_prereq_tier']}  (<- collapses; stage drives layout)")
    print()
    print("Goal paths (ON-RAILS.md):")
    for g in goals:
        bands = " / ".join(f"{b['label']}:{len(b['nodes'])}" for b in g["bands"])
        print(f"  {g['id']:<14} [{g['band_axis']}/{g['foundations_mode']}] "
              f"{g['path_count']} on path, {g['member_count']} members"
              f"{', ' + str(len(g['rest_members'])) + ' rest' if g['rest_members'] else ''}")
        print(f"  {'':<14} {bands}")
    print()
    status = "PASS" if not v["dangling_prereqs"] and not v["order_violations"] else "FAIL"
    print(f"VALIDATION: {status}")
    print(f"  dangling prereqs       : {len(v['dangling_prereqs'])}")
    print(f"  order violations       : {len(v['order_violations'])}")
    print(f"  prereqs → outside slice: {sum(len(x) for x in v['prereqs_pointing_outside_slice'].values())} "
          f"(expected — they resolve in the full tree)")
    print(f"  same-surface clusters  : {len(v['same_surface_clusters_need_review'])} (need dedup/sense review)")
    print()
    for fnd in manifest["findings"]:
        print("  • " + fnd.split(":")[0] + ": " + fnd.split(":", 1)[1].strip()[:96] + "...")
    print()
    print(f"Wrote {OUT}")
    if status == "FAIL":
        sys.exit(1)


if __name__ == "__main__":
    main()
