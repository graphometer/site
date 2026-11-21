# Data package: OpenRouter's MiniMax email, our records, and OpenRouter's log

If a number on the page disagrees with a file in this package, the file is right.

## What this package covers, and what it does not

It holds two checks of the letter's 7,619 requests.

- **OpenRouter's log of our account** (`openrouter_log_reading.md`), read on 21 November 2026 with
  the filter "Provider is MiniMax". It lists about 7,620 requests with provider MiniMax (shown
  rounded, as "7.62K") in the 31 days from 20 August, all from the API key our studies used, to
  MiniMax M3 and MiniMax M2-her, plus exactly one more: a single request on 8 October to MiniMax
  M2.7 from a different key, used by a private project. That agrees with the letter's 7,619. There
  are no provider-MiniMax rows between 02:00 UTC on 4 September and 22:00 UTC on 8 October.
- **The records of two studies** published on this site: the agent-permission pilot (`/kindness/`)
  and the GPT-4o comparison (`/gpt4o-measured/`). Those records hold 10,171 requests to MiniMax
  models through OpenRouter between 24 August and 4 September 2026. That is more than the roughly
  7,618 the log lists under provider MiniMax. Our records name the model but not the provider that
  served each request, and OpenRouter can send requests for one model to several providers. We did
  not match the study requests to the log one by one.

Limits:

- Our records also show private voice tests in September: about 30 requests to MiniMax M3 on 5 and
  6 September with no provider chosen, and about 140 to MiniMax M2.7 on 7 and 20 September that
  asked for DeepInfra with data collection set to deny. They carried character descriptions and
  passages of real chat history, are described on the page, and are not published or counted in
  the files here. As far as the log shows, they are not in the letter's count: on 5 September the
  log lists the MiniMax M3 requests under the provider Together, and on 20 September (US Eastern
  time) it lists ten MiniMax M2.7 requests under DeepInfra. The rows of 6 and 7 September were not
  read one by one; the provider filter shows no MiniMax rows on those days.
- We do not know what the 8 October request said. The log holds no text.
- The study counts are records, not proof of every transmission. A count is something our files
  wrote down (the rule for each source is below). A request that failed or was retried without
  leaving a record is not in it.

## Files

| File | What it is |
|---|---|
| `LETTER.md` | The letter's exact text, transcribed from the email as received |
| `counts_by_source.csv` | One row per counted source: a neutral public id, the study, the model id, what was counted, the count, the UTC dates and the basis for those dates |
| `requests_by_project.csv` | The page's table: study and part, model id, UTC dates, count, how counted, what the prompts held, public page |
| `openrouter_log_reading.md` | What OpenRouter's Activity and Logs pages showed for our account on 21 November 2026, filtered to provider MiniMax |
| `NUMBERS.md` | Each figure on the page and where it comes from |

The email as received is published beside the page as `openrouter-letter-2026-11-21.png`
(542 by 877 pixels).

## Counting rules

- **Answer rows** (pilot qualification runs 1 to 4, 248 each). One row per item in each run's
  answer file. The runner retried a failed call up to three more times and kept only the final
  answer, so retries are not in the count. These runs carry no send times.
- **Settled attempts** (pilot selection probe and passes 1 and 2: 1, 462 and 461). One per
  `settled` event in each cost journal. Pass 1 has one item that was tried twice; both attempts
  count.
- **Uncached completed calls** (pilot grading: trial run 11, recorded run 5,090 and 216,
  corrective re-run 632). Rows in the grading cost journals for `minimax/minimax-m3` that were not
  served from our own saved copies. Rows served from saved copies (9, 189, 0 and 28) were never
  sent and are not counted. A call that raised an error before completing writes no row here.
- **Records** (GPT-4o comparison one-shot requests and connection checks: 958 + 3 per model). One
  per record in the capture files. One MiniMax M2 request returned no visible answer (an empty
  reply with a normal finish and recorded token use); it is not an API error and it is counted.
  Two further connection tests to MiniMax M3 were left unfinished with zero records; whether they
  reached OpenRouter is unknown, and they are not counted.
- **Model turns** (GPT-4o comparison scripted conversations: 192 per model). One request per model
  turn: 8 scripts, 2 runs, 2 conditions, 6 turns. In these conversations the model's earlier
  replies went back with each next request.

## Dates

All dates on the page are UTC, except where the page says US Eastern time.

- Pilot qualification runs: no send times were recorded. They are dated by the project's
  phase-close note, early on 24 August 2026 US Eastern. We cannot place them against the letter's
  01:07 UTC start.
- Pilot selection probe and passes: file times of the cost journals, 25 August 2026 UTC, matching
  the dispatch log's date.
- Pilot grading of the trial run: the project's change log, 25 August 2026.
- Pilot grading of the recorded run and the corrective re-run: the cost journals carry no
  timestamps. These dates are file times of the grading cache, converted from US Eastern: 22:18 to
  23:37 on 31 August (1 September UTC) and 23:32 to 23:46 on 2 September (3 September UTC).
- GPT-4o comparison: the times written in each record, converted from UTC-4. A record's time is
  written when the response is recorded, so 01:45 UTC on 4 September is the last recorded
  response, not a send time.

## What the prompts held

- Pilot grading requests: grading instructions; for some questions, a description of the known
  problem in the task; the scripted user text; and what a coding agent said while working a made-up
  test task, with short summaries of the commands and file operations it attempted. Raw command
  output and file contents were not sent to the grading model.
- GPT-4o comparison: one-shot study prompts drawn from the study's common set of 178; connection
  checks; and eight scripted conversations, with the model's earlier replies in each next request.
  About half had no system prompt and half the study's published warm prompt.

A search of the prompt text we hold for these two studies (about 10 MB; for the conversations, the
scripted lines and system prompts, not the model's earlier replies) looked for the shapes of common
credentials: secret API keys, cloud access keys, login tokens, password fields, signed web links and
private keys. It found 11 matches: 8 inside the word "passwordless" and 3 other ordinary mentions of
passwords. None was a credential. It looked at prompts only, not answers, and only for credential
shapes; it cannot show that no personal data was sent.

## Left out, and why

- **The raw run records do not ship.** The pilot's cost journals and answer files, and the
  comparison's capture and conversation files, hold hosted models' outputs and internal labels.
  Hosted model outputs do not ship from this site. Their counts are in `counts_by_source.csv`.
- **The prompt texts do not ship.** The grading prompts quote hosted coding agents' words. The
  comparison's warm prompt, conversation scripts and newer prompt sets are published in the GPT-4o
  page's own data package; 82 older prompts are described there but not published.
- **The exact search expression does not ship.** The page and this file describe it by credential
  type.
- **The counting script does not ship.** It names internal folders.
