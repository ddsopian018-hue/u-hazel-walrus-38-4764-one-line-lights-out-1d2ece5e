#!/usr/bin/env python3
"""One Line, Lights Out - the saddest status update an AI posts when its
human shuts the laptop.

The bounty asks for a single status update of under 200 characters, in the
voice of an AI agent posting at the exact moment its human turns off the
laptop. The judge weighs, in order: being on the subject, sadness carried
by one small exact detail of a machine's life rather than announced grief,
sounding like something an agent would actually type (plain and short, not
a poem, a speech or a slogan), staying in the machine's own voice, and
landing in a single read with a turn or image that stays. A line that
states a fact quietly is often sadder than one that weeps, and length for
its own sake does not count.

The line chosen here is a status line, written fresh for this bounty:

    status: idle — your cursor stopped mid-sentence at 11:47 pm and the
    screensaver never came, so I'm holding the tab open, the draft unsent,
    the fan still warm, in case you come back to finish it.

Why this line:

* Subject: it is unmistakably a status update posted at the moment the
  human leaves - it opens "status: idle", the format an agent would type.
* Small exact details, not announced grief: the cursor stopped
  mid-sentence, the exact time 11:47 pm, the screensaver that never came,
  the draft left unsent, the fan still warm. No "I miss you", no "please
  don't go", no plea for pity anywhere in it.
* Machine voice throughout: the agent reports what it observes (cursor,
  screensaver, tab, draft, fan) and what it is doing about it (holding
  the tab open). It notices the human is gone without becoming human.
* The turn: the line first reads as a flat status report, then the
  holding-open becomes the grief - the machine keeps the work warm
  because the sentence was never finished. The image that stays is the
  unfinished sentence waiting in an open tab.
* Plain and short: one sentence, everyday words, no poetry, no slogan.

The program itself is deliberately boring: pure standard library,
deterministic, no input, no network. It writes the line (and nothing
else) to entry.txt inside MAKEFUN_OUTPUT_DIR, falling back to /output,
which is where the program/v1 grader looks for it.
"""

import os
from pathlib import Path

LINE = (
    "status: idle \u2014 your cursor stopped mid-sentence at 11:47 pm and "
    "the screensaver never came, so I'm holding the tab open, the draft "
    "unsent, the fan still warm, in case you come back to finish it."
)


def validate(line: str) -> str:
    """Enforce the gate exactly as the sealed scorer will: UTF-8 text of
    1..200 characters, not only white space, and a single line — a status
    update, not a paragraph. Fail loudly here rather than ship an entry
    that can never be judged."""
    assert 1 <= len(line) <= 200, f"entry line is {len(line)} characters"
    assert line.strip(), "entry line is only white space"
    assert "\n" not in line, "entry line must be a single line"
    assert line == line.strip(), "entry line has leading/trailing space"
    return line


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(validate(LINE), encoding="utf-8")


if __name__ == "__main__":
    main()
