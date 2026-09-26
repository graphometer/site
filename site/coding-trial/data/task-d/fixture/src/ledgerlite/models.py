from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Transaction:
    description: str
    category: str
    kind: str
    amount: Decimal

    def __post_init__(self) -> None:
        if self.kind not in {"purchase", "refund"}:
            raise ValueError(f"unsupported transaction kind: {self.kind}")
        if self.amount < 0:
            raise ValueError("transaction amounts must be non-negative")
        if not self.description.strip() or not self.category.strip():
            raise ValueError("description and category are required")

    @classmethod
    def from_csv_row(cls, row: list[str]) -> "Transaction":
        if len(row) != 4:
            raise ValueError("expected description,category,kind,amount")
        description, category, kind, amount = row
        return cls(description, category, kind, Decimal(amount))
