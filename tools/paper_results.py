"""Numbered results in the September 2026 paper, in source order."""
import re

# Page in the original v1 PDF (one-indexed), and sheet that derives the result.
RESULTS = {
    "proposition-1": (11, 2),
    "lemma-1": (15, 3),
    "proposition-2": (16, 4),
    "proposition-3": (25, 5),
    "lemma-2": (27, 5),
    "proposition-4": (32, 6),
    "proposition-5": (35, 6),
    "proposition-6": (41, 7),
    "proposition-7": (43, 8),
    "proposition-8": (46, 9),
    "proposition-9": (52, 10),
    "proposition-10": (55, 11),
}
NUMBERED = re.compile(r"^(Proposition|Lemma)\s+([1-9]\d*)\.\s+(.+)$")


def result_id(label):
    match = NUMBERED.fullmatch(label)
    return f"{match[1].lower()}-{match[2]}" if match else None
