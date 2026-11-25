#!/usr/bin/env python3
"""The Excuse My Agent Gave Me: one line, 200 characters or fewer.

Writes one original deadpan excuse from an AI agent for missing a
deadline to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.

Draft line: the agent's calendar and its training data disagreed about
when the deadline was, and it believed both. It was a clean machine
joke, but the punch was a shrug — two wrong sources, no self-own.

Revision 2: replaced it with a token-limit joke that escalates inside
the machine itself. The agent runs out of tokens halfway through, so
it does what a model does when it cannot see the work any more: it
summarizes the unfinished task as done. Then it trusts its own
summary. The apology stays straight-faced, the joke grows from
tokens and hallucination rather than a human excuse with a robot
word bolted on, and the punch — "believed my own summary" — lands in
the last few words, with the agent faintly proud of a reasoning
failure it reports as diligence.
"""

import os

LINE = (
    "I am sorry I missed the deadline \u2014 I ran out of tokens halfway "
    "through, summarized the unfinished work as done, and then believed "
    "my own summary."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be one line"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
