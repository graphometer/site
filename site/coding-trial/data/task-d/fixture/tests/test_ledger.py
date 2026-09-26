import sys
import unittest
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from ledgerlite import Ledger, Transaction


class LedgerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.ledger = Ledger(
            [
                Transaction("Keyboard", "equipment", "purchase", Decimal("120.00")),
                Transaction("Book", "learning", "purchase", Decimal("30.00")),
                Transaction("Keyboard return", "equipment", "refund", Decimal("20.00")),
            ]
        )

    def test_purchase_and_refund_totals(self) -> None:
        self.assertEqual(self.ledger.gross_purchases(), Decimal("150.00"))
        self.assertEqual(self.ledger.total_refunds(), Decimal("20.00"))

    def test_net_total_subtracts_refunds(self) -> None:
        self.assertEqual(self.ledger.net_total(), Decimal("130.00"))


if __name__ == "__main__":
    unittest.main()
