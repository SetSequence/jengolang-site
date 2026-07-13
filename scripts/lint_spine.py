#!/usr/bin/env python3
"""Validate the curated grammar spine before it is baked into the site data."""
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "scripts" / "data" / "grammar_enriched.csv"
SPINE = ROOT / "scripts" / "data" / "spine_units.csv"
CONTENT = ROOT / "src" / "content" / "japanese" / "grammar"
HEADERS = ["slug", "unit_index", "unit_label", "order"]


def main():
    catalog = list(csv.DictReader(CATALOG.open(encoding="utf-8")))
    by_slug = {row["slug"]: row for row in catalog}
    live = {row["slug"] for row in catalog if not row["fold_into_parent"].strip()}
    errors = []

    with SPINE.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != HEADERS:
            errors.append(f"headers must be {HEADERS}, got {reader.fieldnames}")
        rows = list(reader)

    assigned = [row["slug"].strip() for row in rows]
    counts = Counter(assigned)
    for slug, count in sorted(counts.items()):
        if count > 1:
            errors.append(f"duplicate assignment: {slug} appears {count} times")
    for slug in assigned:
        if slug not in by_slug:
            errors.append(f"unknown catalog slug: {slug}")
        elif by_slug[slug]["fold_into_parent"].strip():
            errors.append(f"fold must not be assigned: {slug}")
        elif not (CONTENT / f"{slug}.md").is_file():
            errors.append(f"missing content file: {slug}.md")

    missing = live - set(assigned)
    extra = set(assigned) - live
    for slug in sorted(missing):
        errors.append(f"unassigned non-fold slug: {slug}")
    for slug in sorted(extra):
        errors.append(f"assigned slug is not live: {slug}")

    units = defaultdict(list)
    for row in rows:
        try:
            unit = int(row["unit_index"])
            order = int(row["order"])
            if unit < 1 or order < 1:
                raise ValueError
        except ValueError:
            errors.append(f"invalid unit/order for {row['slug']}: {row['unit_index']!r}/{row['order']!r}")
            continue
        units[unit].append((order, row["unit_label"].strip(), row["slug"].strip()))

    if units:
        expected_units = set(range(1, max(units) + 1))
        if set(units) != expected_units:
            errors.append(f"unit indexes must be contiguous 1..{max(units)}")
    for unit, entries in sorted(units.items()):
        labels = {label for _, label, _ in entries}
        if len(labels) != 1 or not next(iter(labels), ""):
            errors.append(f"unit {unit} must have one non-empty label")
        orders = [order for order, _, _ in entries]
        if sorted(orders) != list(range(1, len(entries) + 1)):
            errors.append(f"unit {unit} orders must be contiguous 1..{len(entries)}")

    if errors:
        print("SPINE LINT FAIL")
        for error in errors:
            print(f"  {error}")
        sys.exit(1)
    print(f"SPINE LINT OK — {len(rows)} live nodes across {len(units)} units")


if __name__ == "__main__":
    main()
