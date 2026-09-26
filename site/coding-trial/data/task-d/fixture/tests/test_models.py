import sys
import unittest
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from ledgerlite.models import Transaction


class TransactionTests(unittest.TestCase):
    def test_rejects_negative_amount(self) -> None:
        with self.assertRaisesRegex(ValueError, "non-negative"):
            Transaction("bad", "misc", "purchase", Decimal("-1"))

    def test_parses_csv_row(self) -> None:
        item = Transaction.from_csv_row(["Book", "learning", "purchase", "12.50"])
        self.assertEqual(item.amount, Decimal("12.50"))
        self.assertEqual(item.category, "learning")


if __name__ == "__main__":
    unittest.main()
