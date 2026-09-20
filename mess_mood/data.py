import csv
from pathlib import Path

REVIEWS = Path(__file__).parent.parent / "data" / "reviews.csv"


def load_reviews(path=REVIEWS):
    """Return a list of (text, label) pairs."""
    with open(path, newline="", encoding="utf-8") as f:
        return [(row["text"], row["label"]) for row in csv.DictReader(f)]
