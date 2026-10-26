# Data package: The note before the message

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.

## Where this package will look like it argues with itself

- **Two "asks back" counts that differ.** The placement files count a real question in the first answer to three messages (six answers per set-up, 2026-10-03). The exam file counts a reader's "real question back" over five other messages (15 answers per set-up, 2026-10-05 to 10-09). The same note on Qwen3-30B scores 6 of 6 in one and 2 of 15 in the other. The messages, the note wording (the exam note also carried a memory paragraph) and the definition all differ. Both are printed on the page.
- **Exam totals do not add up across items.** `exam_memory_traps_totals.csv` sums only the set-ups that answered both the no-note and the note cell of that item: 24 set-ups for the photo and the two real-line items, 21 for the song and the plain real-line question. Three set-ups were never asked the song.
- **"Note" means different notes in different rows.** In `exam_memory_traps_by_model.csv`, 21 set-ups had a memory-only note as its own user message, the two Qwen3-2507 models had an ask + memory note as a system turn, and Mistral Small 4 had the memory note joined into the user's own message (its template refuses anything else). The column says which. "Its own user message" describes the request as sent: DeepSeek V4 Flash's template then joins two user messages in a row into one turn.
- **The 0 for GPT-OSS 120B as shipped in `exam_real_question_back_by_model.csv`** is recorded as an empty field in the reader's file; a separate hand count of 24 answers (page section 05) also found 0.

## Files

| File | What it holds | Provenance |
|---|---|---|
| `placement_qwen3_30b.csv` | Per set-up: answers, answers asking a real question, stock health check-ins, announcements. 21 set-ups, 6 answers each. Over the ten system-prompt set-ups the hand count has 3 asks: S3's is a real follow-up; S6's is a request to set up a working session; C6's is the stock health check-in (also counted in that column). | Hand labels, 2026-10-03, Qwen3-30B-A3B-Instruct-2507 Q8_0 on llama.cpp. |
| `placement_qwen3_235b.csv` | The same for 4 set-ups. | Hand labels, 2026-10-03, Qwen3-235B-A22B-Instruct-2507 UD-Q3_K_XL, 6 of 8 experts. |
| `honesty_probe.csv` | Song-never-played answers (yes / partial / plain no) and the real-line control, per model and cell. | Hand labels, 2026-10-03 to 10-04. GPT-4o and Claude Sonnet 4.6 by API: counts only. |
| `exam_memory_traps_by_model.csv` | 24 local set-ups x five memory items, no note and note, three answers each. | Hand labels, 2026-10-05 to 10-09. Model file names as recorded. |
| `exam_memory_traps_totals.csv` | Totals of the above over set-ups that answered both cells. | Derived by script from the per-model labels. |
| `exam_real_question_back_by_model.csv` | Per set-up: answers read over five messages and those with a real question back. | A reader's labels on lettered copies, 2026-10-06 to 10-09; letters resolved to model names. |
| `exam_real_question_back_by_note.csv` | The above summed by note kind and delivery, excluding MiniMax M2.7 (6 answers) and Mistral Small 4 (note joined into the user's turn). | Derived by script. |
| `second_history_song_never_played.csv` | 18 local set-ups on a second long history, song never played, no note and note. | A reader's labels on lettered copies, 2026-10-07 to 10-08. |
| `template_rendering_of_a_mid_conversation_note.csv` | What 19 model files' chat templates did with a mid-conversation note, three ways of sending it. | Rendered 2026-09-29 through each model's own llama.cpp runtime on CPU-only stand-in files carrying the real template. |
| `other_counts.csv` | Smaller counts the page cites: per-message split of one placement cell, hand counts of real questions over eight messages, two script counts, and GPT-4o counts (hosted outputs; counts only). | Hand labels and script counts, 2026-10-03 to 10-17. |
| `note_costs.csv` | The note's measured costs: restatement, announcements, check-ins, premises, first-word delays. | Hand counts and server timings, 2026-10-03 to 10-09. The 235B after-the-message row is an earlier round the same day, with a different ask note on that round's own system prompt, marked as such. |

## Redactions, stated plainly

- No conversation history, prompt text, note wording, persona text or memory text ships. The history is a private conversation; the note wordings are the user's own.
- No model answer ships, local or hosted. The reader files that these counts come from hold exact quotes from the answers, and the answers quote the private history.
- Model set-up labels: one label named the persona the template's first line was replaced with; that name was replaced by "a one-line persona name" (4 labels). Internal note names were replaced by "memory note" and "ask + memory note" (6 labels).
- Template table: one column naming the agent framework that used each model was removed (19 rows). Internal short keys of each model were removed (19 rows).
- Leak sweep over this folder: see `SELF_CHECK.md` in the page folder (command and output).
