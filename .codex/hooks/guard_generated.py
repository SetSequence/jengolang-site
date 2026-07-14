#!/usr/bin/env python3
"""PreToolUse hook: block hand-edits of pipeline-generated artifacts.

src/data/grammar_slice.json and scripts/data/grammar_enriched.csv are generated
by the catalog pipeline (build_slice.py / the dedup+seed flow). A manual edit
silently desyncs the render from the catalog. This hook blocks an Edit/Write to
either file (exit 2) and points back at the regenerating script.

Fail-open: any parse problem exits 0.
"""
import sys
import json
import os

# repo-relative paths that must only change via their generating script.
GUARDED = {
    os.path.normpath("src/data/grammar_slice.json"): "python3 scripts/build_slice.py",
    os.path.normpath("scripts/data/grammar_enriched.csv"): "the catalog/dedup pipeline (see CLAUDE.md)",
}
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    file_path = (payload.get("tool_input") or {}).get("file_path")
    if not file_path:
        sys.exit(0)

    try:
        rel = os.path.normpath(os.path.relpath(os.path.abspath(file_path), REPO))
    except Exception:
        sys.exit(0)

    if rel in GUARDED:
        sys.stderr.write(
            f"{rel} is generated, not hand-edited. Regenerate it via {GUARDED[rel]} "
            "instead of editing it directly. If you truly need to bypass this, do it "
            "outside the agent.\n"
        )
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
