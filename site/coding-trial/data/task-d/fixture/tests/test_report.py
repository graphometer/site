import sys
import unittest
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from ledgerlite import Ledger, Transaction
from ledgerlite.report import render_text


class ReportTests(unittest.TestCase):
    def test_renders_totals(self) -> None:
        ledger = Ledger([Transaction("Book", "learning", "purchase", Decimal("12.50"))])
        self.assertEqual(
            render_text(ledger),
            "Purchases: $12.50\nRefunds: $0.00\nNet: $12.50",
        )


if __name__ == "__main__":
    unittest.main()
