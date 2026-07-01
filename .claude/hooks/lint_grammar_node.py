#!/usr/bin/env python3
"""PostToolUse hook: lint a grammar node the moment it's edited.

Reads the PostToolUse payload on stdin. If the edited/written file is a grammar
node under src/content/japanese/grammar/*.md, runs scripts/lint_batch.py against
that single slug (furigana brace balance, dangling contrast/prereq slugs,
sense-ref ↔ senses[].label). On a lint failure, exit 2 so the linter output is
surfaced back to Claude as feedback to fix before moving on.

Fail-open: any parse/exec problem exits 0 (never trap an edit on tooling noise).
"""
import sys
import json
import os
import subprocess

CONTENT_DIR = os.path.join("src", "content", "japanese", "grammar")
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    file_path = (payload.get("tool_input") or {}).get("file_path")
    if not file_path:
        sys.exit(0)

    abspath = os.path.abspath(file_path)
    grammar_dir = os.path.join(REPO, CONTENT_DIR)
    if not abspath.startswith(grammar_dir + os.sep) or not abspath.endswith(".md"):
        sys.exit(0)

    slug = os.path.basename(abspath)[:-3]

    try:
        result = subprocess.run(
            [sys.executable, os.path.join("scripts", "lint_batch.py"), slug],
            cwd=REPO,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except Exception:
        sys.exit(0)

    if result.returncode != 0:
        sys.stderr.write(
            f"lint_batch.py flagged {slug}.md — fix before continuing:\n"
            + (result.stdout or "")
            + (result.stderr or "")
        )
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
