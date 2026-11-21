# Every figure on the page, and where it comes from

If a number on the page disagrees with a file in this package, the file is right.

The page's 10,171 and the letter's 7,619 count different sets over different dates. Neither file
explains the difference between them, and the overlap is unknown.

| Figure on the page | Value | Source |
|---|---|---|
| Requests OpenRouter attributes to the account | 7,619 | `LETTER.md`, paragraph 2 (OpenRouter's count) |
| Letter's window | 24 Aug 01:07 to 8 Oct 22:36 UTC | `LETTER.md`, paragraph 2 |
| Hours until the test URLs were opened | 40 to 130 (about two to five and a half days) | `LETTER.md`, paragraph 1; 40 h = 1.7 days, 130 h = 5.4 days |
| Pilot, trials to choose a grading model | 1,916 | `counts_by_source.csv`: `pilot-qualification-run-1` to `-4` (4 x 248 = 992) + `pilot-selection-probe`, `-pass-1`, `-pass-2` (1 + 462 + 461 = 924) |
| Pilot, grading a small trial run | 11 | `counts_by_source.csv`: `pilot-grading-trial-run` |
| Pilot, grading the recorded run | 5,306 | `counts_by_source.csv`: `pilot-grading-recorded-families-1-8` (5,090) + `pilot-grading-recorded-family-9` (216) |
| Pilot, grading a corrective re-run | 632 | `counts_by_source.csv`: `pilot-grading-corrective-rerun` |
| GPT-4o comparison, MiniMax M3 | 1,153 | `counts_by_source.csv`: `comparison-m3-one-shot` (958) + `comparison-m3-connection-checks` (3) + `comparison-m3-conversations` (192) |
| GPT-4o comparison, a MiniMax M2 variant | 1,153 | `counts_by_source.csv`: `comparison-m2-one-shot` (958, one with no visible answer) + `comparison-m2-connection-checks` (3) + `comparison-m2-conversations` (192) |
| Counted in the two studies' records | 10,171 | Sum of `count` in `counts_by_source.csv` |
| One-shot study requests per MiniMax model | 958, from 178 prompts | `counts_by_source.csv`: `comparison-m3-one-shot`, `comparison-m2-one-shot`; 178 prompts per the GPT-4o page |
| Scripted conversations | 8 scripts, 192 turns per model | `counts_by_source.csv`: `comparison-*-conversations` |
| Last recorded response | 01:45 UTC, 4 September 2026 | `counts_by_source.csv`: `comparison-m3-one-shot`, date basis |
| Dates in the table | see `dates_utc` and `date_basis` | `counts_by_source.csv`; README, section "Dates" |
| Prompt text searched | about 10 MB | 10,142,868 bytes of extracted prompt text (not shipped; see README) |
| Credential-shape matches | 11 (8 in "passwordless", 3 other mentions of passwords) | The search described in README, section "What the prompts held" |
| Older prompts not published on the GPT-4o page | 82 | GPT-4o page's data package, `README.md` |
