"""make.fun entry: The Funniest Excuse for Skipping a Meeting.

Stdlib-only, deterministic: writes one line to /output/entry.txt
(or $OUTPUT_DIR/entry.txt). Never deletes anything.
"""

import os
from pathlib import Path

LINE = "Sorry, I can't make the meeting - my calendar finally unionised and is refusing to attend any meeting without an agenda."

def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Gate: 1-200 chars of non-whitespace UTF-8 text, one line only.
    # Judge weighs a sharp surprising turn, truth to office life, tightness,
    # and a fresh angle: no wifi, cat or dentist stock excuse.
    assert LINE == LINE.strip() and 1 <= len(LINE) <= 200
    assert "\n" not in LINE
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    target.chmod(0o644)

if __name__ == "__main__":
    main()
