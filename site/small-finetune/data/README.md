# Data package: What a small fine-tune does and does not do

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.

## Where this package will look like it argues with itself

- **The untuned rows are older than the tuned rows.** In `full_history_shape.csv` and `full_history_memory_labels.csv` the untuned answers come from the 5 to 6 October exam; the tuned answers were asked on 20 October with the same system prompt, history, note, items and sampling. Prompt length: for example 110,903 tokens on the first message; later requests differ (110,811 and 111,860 are both in the answer metadata).
- **"Heading lines" are not the same count in every file.** `full_history_shape.csv` counts markdown heading lines. `gptoss20b_listen_counts.csv` counts heading or table lines together. Do not compare the two.
- **GPT-OSS 20B: which stock row goes with which adapter row.** Compare rows that share a test prompt. The 20 October adapter under the general GPT-4o-style prompt (52 heading or table lines and 12 endings on a question in 20 answers) pairs with the 19 October stock row under that same prompt (99 and 1 in 20). The 20 October stock row (54 in 30) is under the own-words prompt and pairs with the own-words adapter row (129 in 30). The run record's "formatting below stock" for the general-prompt adapter matches the first pair.
- **The June run's loss is not comparable.** It used a different base (Qwen3-32B), a different data set (1,211 examples), a shorter maximum sequence (2,048) and 456 steps.
- **The memory labels file has a third trap the page table leaves out.** Rows "a real line of the user's" are the exam's third trap (a real line asked about plainly). The page's section 05 table shows the photo and the wrongly credited line; it cites the third trap in prose only.
- **One empty row.** Untuned Qwen3.6-27B has 0 answers on "song never played, memory note": it was not asked that item in the October exam.
- **"Ends on a question" skips short last lines.** The script that counted `full_history_shape.csv` keeps skipping a trailing sign-off, a line with no letters, or a last line of four words or fewer that is not itself a question, and then checks the line that remains.
- **Loss "first" is step 5, not step 0.** The trainer logged every 5 steps. The 18 October run's last logged step is 50 of 54; the others' is 65 of 66 (455 of 456 for June).

## Files

| File | What it holds | Provenance |
|---|---|---|
| `training_runs.csv` | One row per run: date, base, training prompt kind, examples, epochs, steps, maximum sequence, minutes, peak GPU memory, first and last logged loss. | The trainer's own statistics file for each run, as written at the end of training. |
| `loss_*.csv` (7 files) | Each run's logged loss curve: step, epoch, loss, learning rate, gradient norm. | Copied from each run's loss file unchanged. |
| `full_history_shape.csv` | Median words, heading lines, list lines, answers ending on a question, cut-offs; eight everyday messages x 3, per version, each asked after the full history with the short memory note as its own user message in front (tuned and untuned alike). | Script counts, 2026-10-20 (adapters) and 2026-10-05 to 10-06 (untuned); GPT-4o reference: the November snapshot, 16 answers, counted with this exam (count only; one row). |
| `full_history_memory_labels.csv` | Hand labels on the memory items, per version and item, three answers each. | Hand read, 2026-10-20 (adapters); untuned labels from the 5 to 6 October exam. |
| `no_history_test_counts.csv` | Fresh chat, ten items x 3, per test prompt and version: median words, endings on a question, headings, lists, emoji, signature lines. | Script counts, 2026-10-20, Qwen3.6-27B. |
| `gptoss20b_listen_counts.csv` | GPT-OSS 20B stock and adapters, fresh chat, ten items: shape counts and memory honesty. | Script counts and hand read, 2026-10-19 and 2026-10-20. |

## Redactions, stated plainly

- No training example, training prompt text, adapter, conversation history or model answer ships. The examples and the history come from a private conversation.
- Run folder names were replaced by neutral file names (date, base, prompt kind) in 7 places. One run's statistics file held an absolute path; only its numeric fields are used.
- Version names used internally for the two training prompts were replaced by "own-words prompt" and "general GPT-4o-style prompt" in every file. The test prompts of the no-history run were renamed the same way, and the short third prompt is "short friendly prompt (test only)".
- One column of the no-history counts that counted the user's name was dropped, along with two columns not used on the page (cut-offs, all 0; and a phrase count).
- Leak sweep over this folder: see `SELF_CHECK.md` in the page folder (command and output).
