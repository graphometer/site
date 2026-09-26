import argparse
import csv
from pathlib import Path

from .ledger import Ledger
from .models import Transaction
from .report import render_text


def load_csv(path: Path) -> Ledger:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = csv.reader(handle)
        return Ledger(Transaction.from_csv_row(row) for row in rows if row)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Summarize a transaction CSV file")
    parser.add_argument("path", type=Path)
    args = parser.parse_args(argv)
    print(render_text(load_csv(args.path)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
