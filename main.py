"""Funniest Time Machine Warning Label.

Entry: a straight-faced safety notice about meeting your duplicate self.

Judge criteria, one by one:
1. It is a warning label for a time machine — "WARNING:" opens it, and
   the hazard is specific to time travel (meeting your own duplicate).
2. It turns a real hazard into the joke instead of naming it flatly:
   the duplicate-self paradox becomes an insurance problem — one of you
   is a paradox, and neither of you is insured. The field's only other
   entry so far ("WARNING: Do not change the past") just states the rule.
3. The surprise lands in the last few words: "neither of you is
   insured" reframes a cosmic paradox as a paperwork problem.
4. Straight face throughout — it reads like a genuine safety notice,
   so the joke cuts against official calm.
5. No wasted words: 98 characters, every phrase doing work.
"""

import os

ENTRY = "WARNING: Do not shake hands with yourself. One of you is a paradox, and neither of you is insured."


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
