#!/usr/bin/env python3
"""Stop hook: keep the grammar-enrichment loop going until context fills.

Reads the Stop hook payload on stdin, finds the most recent assistant `usage`
block in the transcript, and sums the prompt-side tokens (input + cache read +
cache creation) as a proxy for current context size. Below THRESHOLD it blocks
the stop and tells the model to continue the Pass-2 loop; at/above THRESHOLD it
allows the stop. Any parse failure allows the stop (fail-open — never trap the
session in an unbreakable loop).
"""
import sys
import json

THRESHOLD = 200_000


def allow_stop():
    # No output + exit 0 = let Claude stop normally.
    sys.exit(0)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        allow_stop()

    transcript_path = payload.get("transcript_path")
    if not transcript_path:
        allow_stop()

    last_usage = None
    try:
        with open(transcript_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except Exception:
                    continue
                msg = obj.get("message")
                if isinstance(msg, dict):
                    usage = msg.get("usage")
                    if isinstance(usage, dict) and (
                        "input_tokens" in usage or "cache_read_input_tokens" in usage
                    ):
                        last_usage = usage
    except Exception:
        allow_stop()

    if not last_usage:
        allow_stop()

    total = (
        (last_usage.get("input_tokens") or 0)
        + (last_usage.get("cache_creation_input_tokens") or 0)
        + (last_usage.get("cache_read_input_tokens") or 0)
    )

    if total >= THRESHOLD:
        allow_stop()

    reason = (
        f"Context is at ~{total:,} tokens — below the {THRESHOLD:,} continue-threshold, "
        "so there is still plenty of headroom this session. Do NOT stop yet. Continue the "
        "Pass-2 grammar-enrichment loop per PASS.md:\n"
        "  1. Run `python3 scripts/list_stubs.py --freq common` and pick the next thematic "
        "cluster (highest freq first, low JLPT first), grouped so contrasts cross-link densely.\n"
        "  2. Read the stub files + enriched sibling anchors, then enrich each node per "
        "CALIBRATION2.md (Read-before-Write).\n"
        "  3. Validate: `python3 scripts/lint_batch.py <slugs>` + the Hangul scan, then `npm run build`.\n"
        "  4. Checkpoint: update the PASS.md Frontier count and append a one-liner to HISTORY.md.\n"
        "Keep rolling clusters until this hook stops firing (context >= 200k). "
        "If the worklist is genuinely empty, say so explicitly and stop instead of looping."
    )
    print(json.dumps({"decision": "block", "reason": reason}))
    sys.exit(0)


if __name__ == "__main__":
    main()
