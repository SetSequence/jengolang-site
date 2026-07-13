#!/usr/bin/env python3
"""Find listed prerequisites that appear after an early grammar node."""
import argparse
import csv
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPINE = ROOT / "scripts" / "data" / "spine_units.csv"
CONTENT = ROOT / "src" / "content" / "japanese" / "grammar"
PREREQS = re.compile(r"^prereqs:\s*(\[[^\n]*\])\s*$", re.MULTILINE)


def listed_prereqs(path):
    match = PREREQS.search(path.read_text(encoding="utf-8"))
    return json.loads(match.group(1)) if match else []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--units", type=int, default=10)
    args = parser.parse_args()

    with SPINE.open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))
    positions = {
        row["slug"]: (int(row["unit_index"]), int(row["order"]))
        for row in rows
    }
    problems = []
    checked = 0
    for row in rows:
        slug = row["slug"]
        position = positions[slug]
        if position[0] > args.units:
            continue
        checked += 1
        for prereq in listed_prereqs(CONTENT / f"{slug}.md"):
            prereq = prereq.lstrip("*")
            if prereq in positions and positions[prereq] > position:
                problems.append((slug, position, prereq, positions[prereq]))

    if problems:
        print("BEGINNER SPINE AUDIT FAIL")
        for slug, position, prereq, prereq_position in problems:
            print(
                f"  {slug} (Unit {position[0]}, #{position[1]}) requires "
                f"{prereq} (Unit {prereq_position[0]}, #{prereq_position[1]})"
            )
        sys.exit(1)
    print(
        f"BEGINNER SPINE AUDIT OK — {checked} nodes through Unit {args.units} "
        "have no listed prerequisite that comes later"
    )


if __name__ == "__main__":
    main()
