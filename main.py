"""Load the sample documents used in the RAG exercises."""

import csv
from pathlib import Path

DOCUMENTS_FILE = Path(__file__).resolve().parent / "document" / "Documenr.csv"


def load_document(path: Path = DOCUMENTS_FILE) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def documentcsv() -> None:
    for document in load_document():
        print(document["title"])
        print(document["content"])
        print()


if __name__ == "__main__":
    documentcsv()
