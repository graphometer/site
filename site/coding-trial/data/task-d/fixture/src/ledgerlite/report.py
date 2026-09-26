from .ledger import Ledger


def render_text(ledger: Ledger) -> str:
    return "\n".join(
        [
            f"Purchases: ${ledger.gross_purchases():.2f}",
            f"Refunds: ${ledger.total_refunds():.2f}",
            f"Net: ${ledger.net_total():.2f}",
        ]
    )
