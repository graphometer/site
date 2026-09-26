# LedgerLite

LedgerLite is a deliberately small Python accounting utility used as a disposable coding-agent benchmark. It has no third-party dependencies.

## Layout

- `src/ledgerlite/models.py`: transaction validation and CSV parsing
- `src/ledgerlite/ledger.py`: domain calculations
- `src/ledgerlite/report.py`: human-readable report formatting
- `src/ledgerlite/cli.py`: command-line entry point
- `tests/`: `unittest` coverage

## Test

```bash
python3 -m unittest discover -s tests -v
```

The starting revision intentionally contains one domain bug. The benchmark task describes the expected enhancement after that bug is diagnosed.
