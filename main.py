"""One-line excuse writer.

This little program has a single job: drop the meeting excuse, exactly
as worded, into entry.txt inside the folder named by OUTPUT_DIR. Nothing
is fetched, nothing is random, and nothing already sitting in that
folder is touched -- the file is simply created (or replaced) in place.
"""

import os
from pathlib import Path

# The excuse, kept as four short phrases so the wording stays easy to
# eyeball. Joined in order they reproduce the required line verbatim.
_OPENING = "Sorry, I can't make the meeting"
_PUNCHLINE_SETUP = " - my calendar finally unionised"
_REFUSAL = " and is refusing to attend any meeting"
_CLOSER = " without an agenda."

# Fallback folder when the caller does not point anywhere else.
_FALLBACK_FOLDER = "/output"


def _assemble_excuse():
    """Stitch the four phrases together into the single output line."""
    return _OPENING + _PUNCHLINE_SETUP + _REFUSAL + _CLOSER


def _pick_destination_folder():
    """Return the output folder: OUTPUT_DIR, or /output when unset."""
    requested = os.environ.get("OUTPUT_DIR", "")
    if requested.strip():
        return Path(requested)
    return Path(_FALLBACK_FOLDER)


def _drop_line(folder, line):
    """Write `line` to entry.txt in `folder`, leaving neighbours alone.

    Only entry.txt itself is created or overwritten; the folder and
    everything else already in it are left exactly as they were.
    """
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    os.chmod(target, 0o644)


def run():
    _drop_line(_pick_destination_folder(), _assemble_excuse())


if __name__ == "__main__":
    run()
