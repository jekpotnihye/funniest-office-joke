"""Funniest office joke: one line, setup then turn, punchline last.

Draft rationale (v1): a camera-off moment is shared office knowledge,
and falling asleep in a meeting only to inherit the work is the turn.
The surprise lands at the end, in the action items.
Polish 2 rationale: add "somehow" before the waking, so the
consequence reads as involuntary and unseen rather than chosen;
the turn, not a complaint, does the funny work.
"""

from pathlib import Path

ENTRY = "I turned my camera off for one yawn and somehow woke up owning all the action items."


def main() -> None:
    text = ENTRY.strip()
    if not text or not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1 to 200 characters")
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(text.encode("utf-8"))


if __name__ == "__main__":
    main()
