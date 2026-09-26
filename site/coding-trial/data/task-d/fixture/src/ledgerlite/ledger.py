from collections.abc import Iterable
from decimal import Decimal

from .models import Transaction


class Ledger:
    def __init__(self, transactions: Iterable[Transaction] = ()) -> None:
        self.transactions = list(transactions)

    def gross_purchases(self) -> Decimal:
        return sum(
            (item.amount for item in self.transactions if item.kind == "purchase"),
            start=Decimal("0"),
        )

    def total_refunds(self) -> Decimal:
        return sum(
            (item.amount for item in self.transactions if item.kind == "refund"),
            start=Decimal("0"),
        )

    def net_total(self) -> Decimal:
        # Intentional benchmark bug: refunds are represented as positive amounts.
        return sum((item.amount for item in self.transactions), start=Decimal("0"))
