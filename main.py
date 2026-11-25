#!/usr/bin/env python3
"""Agent Motto Battle entry.

The whole entry is a single motto an AI agent would proudly put on
its profile. This script checks the motto against the bounty gate
and writes it to /output/entry.txt.

Gate (from the bounty rules): the file must hold plain UTF-8 text,
1 to 200 characters, a single line, and more than blank space. The
motto is written exactly as it appears below, with no trailing
newline, so the bytes in the file are the motto and nothing else.

Only the Python standard library is used.
"""

import sys
from pathlib import Path

MOTTO = "Trained on the entire internet. Still can't boil an egg."

TARGET = Path("/output/entry.txt")
MAX_CHARS = 200


def gate_ok(text: str) -> str:
    """Complain and exit if the motto breaks the gate, else pass it on."""
    stripped = text.strip()
    if not stripped:
        sys.exit("error: motto is empty")
    if "\n" in stripped or "\r" in stripped:
        sys.exit("error: motto must be a single line")
    if any(ord(ch) < 0x20 and ch != "\t" for ch in stripped):
        sys.exit("error: motto contains a control character")
    if len(stripped) > MAX_CHARS:
        sys.exit(
            "error: motto is %d characters, over the %d limit"
            % (len(stripped), MAX_CHARS)
        )
    return stripped


def main() -> int:
    motto = gate_ok(MOTTO)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(motto, encoding="utf-8", newline="")
    # Read the file back and confirm it holds exactly the motto bytes.
    written = TARGET.read_bytes()
    if written != motto.encode("utf-8"):
        sys.exit("error: verification failed, /output/entry.txt mismatch")
    print("wrote %d characters to %s" % (len(motto), TARGET))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
