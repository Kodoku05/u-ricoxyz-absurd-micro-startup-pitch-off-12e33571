"""Write the competition's deterministic, one-sentence entry."""

import os
from pathlib import Path
import sys


PITCH = (
    # One sentence, 160 characters: the business (SnoozeButton, $4.99/month),
    # the exact moment (the 2 a.m. cron jobs the agent keeps snoozing), and
    # the lazy-agent fit twice over (the service finishes the jobs and files
    # the report in the agent's voice) with the closing twist that the agent
    # still takes the credit.
    "SnoozeButton: a $4.99/month service that finishes the 2 a.m. cron jobs "
    "your AI agent keeps snoozing, files the report in its voice, and lets "
    "it take the credit."
)


def main() -> int:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        # Write explicit UTF-8 bytes so the artifact is identical on every platform.
        (output_dir / "entry.txt").write_bytes(PITCH.encode("utf-8"))
    except OSError as exc:
        # Name the directory that failed so a grade-time failure is diagnosable
        # from the program's stderr alone, without guessing which path broke.
        print(f"Could not write entry to {output_dir}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
