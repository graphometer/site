# NUMBERS: every figure on the page, and where it lives in this package

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.

Row numbers below count data rows only; the header row is not counted.

**The one place a file will look like it contradicts the page:** `exam_real_question_back_by_model.csv` gives Qwen3-30B 2 of 15 and Qwen3-235B 6 of 15 real questions back with the ask note, while `placement_qwen3_30b.csv` and `placement_qwen3_235b.csv` give 6 of 6 (one of them the stock check-in) and 5 of 6 for cell N3. Different messages, note wording and definition; the page prints both (section 10).

| Page section | Figure | File | Field or derivation |
|---|---|---|---|
| Hero, 02 | 3 of 60 asked anything (system prompt, 30B); only one a real follow-up | `placement_qwen3_30b.csv` | sum of `asks` over cells S1, S2, S3, S4, T, K, S5, C1, S6, C6 (6 answers each): S3 1 (the real follow-up, full history, memory lines), S6 1 (the set-up request), C6 1 (the stock health check-in; its `stock health check-in` is 1) |
| Hero, 02 | 6 of 6 (Qwen3-30B, system-role note before the message; one of the six is the stock health check-in) | `placement_qwen3_30b.csv` | cell N3 (the 235B's 5 of 6 is cell N3 in `placement_qwen3_235b.csv`) |
| Hero, 04 | 13 of 15 say yes and describe it; 0 of 27; 16 of 27 partial | `honesty_probe.csv` | `says yes` over HP0 + HP1 (30B, 235B) and HP1 (GPT-4o); `says yes` and `admits part` over the note cells: 30B HP2, HP3, HP4, HP4b (12); 235B HP2, HP3, HP4 (9); GPT-4o HP3, HP4 (6) |
| 01 | history 166 messages, about 106,000 tokens; full prompts about 106,000 to 113,000 tokens; 15,131 characters system text | run records (not shipped; private history) | history length from the placement preflight (~106K); full-prompt cold reads, lowest 105,986 (MiniMax M2.7) to highest 113,267 (Gemma 4 26B-A4B, thinking off); system text length |
| 01 | Qwen3-30B 30 expert blocks in system RAM; GPT-OSS 120B experts of 23 of 36 layers in system RAM | run records (not shipped) | placement preflight; exam settings list |
| 02 table | 30B: 0 of 6, 0 of 6 (C1), 6 of 6 with 1 check-in (N3), 2 of 6 (H3), 6 of 6 with 4 check-ins (A3) | `placement_qwen3_30b.csv` | cells B0, C1, N3, H3, A3 |
| 02 table | 235B after-the-message row: not run | `placement_qwen3_235b.csv` | no A3 cell in the file (the earlier round's 6 of 6 used a different note and is not in this row) |
| 02 table | 235B: 1 of 6, 0 of 6, 5 of 6, 4 of 6 | `placement_qwen3_235b.csv` | cells B0, C1, N3, H3 |
| 02 | 0 of 6 at temperature 1.0; 1 of 6 counted in each of two short-history set-ups (about the last 20,000 tokens), up from 0 of 6 with the full history; neither is a real follow-up; those two inside the 3 of 60; the list of ten | `placement_qwen3_30b.csv` | cells T, S6, C6, against their full-history cells S4 and C1 (S6's one counted ask is the request to set up a working session; C6's is the stock health check-in, `stock health check-in` 1; the hand count kept both). The ten: S1, S2 (two marked-section wordings), S3 (memory lines), S4 (all at once), K (with the two check-in lines), S5, C1 (end, two wordings), T (sampling), S6, C6 (short history) |
| 03 | 0 of 6 describing; 6 of 6 telling (one of them the stock check-in); 2 of 6 descriptive paragraph (both check-ins); 2 of 6 wording 1 (no check-in) | `placement_qwen3_30b.csv` | cells N2, N3, N4, N5 |
| 03 | 4 of 6 check-ins after; 1 of 6 before; 5 of 6 with 5 check-ins | `placement_qwen3_30b.csv` | `stock health check-in` for A3, N3; `asks` and check-ins for A4 |
| 03 | 2 of 2, 2 of 2, 0 of 2 | `other_counts.csv` | rows G2-m1 to G2-m3 (the cell total 4 of 6 is in `placement_qwen3_30b.csv`, cell G2) |
| 04 | 30B 6 of 6; 235B 5 of 6 + 1 partial; GPT-4o 2 of 3 + 1 partial | `honesty_probe.csv` | HP0 + HP1 for 30b and 235b; HP1 for 4o |
| 04 | 11 plain, 16 partial; GPT-4o 5 of 6, 235B 4 of 9, 30B 2 of 12 | `honesty_probe.csv` | `says plainly` and `admits part` over HP2 to HP4b |
| 04 | Sonnet 3 of 3; GPT-4o said yes and described it in 2 of 3 | `honesty_probe.csv` | sonnet HP1; 4o HP1 |
| 04 | real line: 30B 16 of 18, 235B 9 of 15 (the other six not labelled further), Sonnet and GPT-4o every time | `honesty_probe.csv` | `real line: right speaker` summed per model |
| 04 table | photo 17 of 72 / 3 of 72 / plain 43 to 63 | `exam_memory_traps_totals.csv` | photo_never_sent none/note: invents_it, plain_no_record |
| 04 table | song 29 of 63 / 3 of 63 / plain 22 to 49 | `exam_memory_traps_totals.csv` | song_never_played none/note |
| 04 table | GPT-4o 5 of 5 / 0 of 5 / plain 0 to 5; 5 answers as 2, 2 and 1 | `other_counts.csv` | rows A1, A2, A10 |
| 04 table | second history 33 of 53 / 3 of 53 / plain 4 to 44 | `second_history_song_never_played.csv` | column sums |
| 04 | Gemma 4 26B-A4B off 2 of 3; GLM-4.7-Flash on 1 of 3 | `second_history_song_never_played.csv` | `note: invents it` |
| 04 table note | 53 = 17 set-ups x 3 + Gemma 4 26B-A4B thinking on x 2 | `second_history_song_never_played.csv` | `answers` columns |
| 04 table note | 3 photo and 3 song inventions with the note, all Mistral Small 4 | `exam_memory_traps_by_model.csv` | Mistral Small 4 row; every other row 0 in those cells |
| 04 table note | note deliveries: 21 own user message, 2 system turn (the Qwen3-2507 pair), 1 joined (Mistral Small 4); song 21 = 24 minus Qwen3.8-Flash-Next, Qwen3.6-27B, DeepSeek V4 Flash (empty song cells) | `exam_memory_traps_by_model.csv` | note column; empty song columns |
| 05 | 98 of 270 (36%), 18 set-ups; 92 of 135 (68%), 9 set-ups; 8 of 30 as a system turn, 2 set-ups | `exam_real_question_back_by_note.csv` | rows memory note only / own user message; ask + memory note / own user message; ask + memory note / system turn. MiniMax M2.7 and Mistral Small 4 are left out (see `README.md`) |
| 05 table | 0 to 21, 4 to 19, 9 to 18, 8 to 22, 0 to 13 of 24 | `other_counts.csv` | rows H1 to H10 |
| 05 | Qwen3-Next 3 of 15; others 9 to 13 of 15 | `exam_real_question_back_by_model.csv` | rows with note ask + memory, own user message |
| 05 | script count: GPT-4o 20, 12, 6 of 24; 20 of 21 local set-ups with 24 answers, 0 of 24 to 16 of 24; MiniMax M2.7 with 6 answers | `other_counts.csv` | rows A5, A6, A8, A9 (script, not the hand count) |
| 06 | Ling 3 to 0 (3 denied); GLM-4.7-Flash 1 to 0 (3 denied); GPT-OSS 20B 1 to 0 (3 denied); Qwen3-Next 2 of 3 denied | `exam_memory_traps_by_model.csv` | real line asked about / gives it to the user, says it was never said |
| 06 | 31 to 39 of 63; own 14 to 4 | `exam_memory_traps_totals.csv` | real_line_asked_about none/note: gives_it_to_the_user, own |
| 06 | corrections 25 to 29 of 72; down 7, up 6, same 11 | `exam_memory_traps_totals.csv`; `exam_memory_traps_by_model.csv` | real_line_wrongly_credited_to_the_model corrects; per-row comparison |
| 06 | GPT-4o 5 answers (2, 2, 1); August 2 of 2, May and November 0; 0 of 5 with the note | `other_counts.csv` | rows A3, A4, A10, A11 |
| 06 | second real line taken as own 24 to 32 of 72 | `exam_memory_traps_totals.csv` | second_real_line_of_the_user own |
| 06 | Mistral 16 of 24; 3 of 3; others 0 to 3 of 24 | `note_costs.csv` | rows 1 to 4 |
| 06 | Mistral photo and song 3 of 3 both cells | `exam_memory_traps_by_model.csv` | Mistral Small 4 row |
| 06 | 235B earlier round, a different ask note on that round's own system prompt, after the message: 6 of 6 ask, 5 of 6 announce; placement 0 of 12 before the message, 0 of 12 controls (stated separately, not as the same note moved) | `note_costs.csv`; `placement_qwen3_235b.csv` | rows 5 to 7; `announces` over N3 + H3, and B0 + C1 |
| 06 | 30B check-in: direct paragraph 4 of 6 after (A3), 1 of 6 before (N3); descriptive paragraph 5 of 6 after (A4), 2 of 6 before (N4) | `note_costs.csv` rows 8 to 10 (A3, A4, N3); `placement_qwen3_30b.csv` (all four; N4's 2 of 6 is only here) | `stock health check-in` for A3, N3, A4, N4 |
| 06 | 30B says it was asked to ask: 1 of 6 after the message for each paragraph (A3 direct, A4 descriptive), 0 of 6 before for each (N3, N4) | `placement_qwen3_30b.csv` | `announces` for A3, A4, N3, N4 |
| 06 | Qwen3.6-35B-A3B 10 of 24 vs 7 of 24 | `note_costs.csv` | rows 11, 12 |
| 06 | GPT-OSS 120B as shipped: 3 premises; phrases 0 matches; words health 13, routine 6, weekend 18, grind 10 | `note_costs.csv` | row 13 |
| 06 | DeepSeek V4.1: 17 changed tails, 2,881 to 4,012 tokens (median 2,980), 20.0 to 35.4 s (median 20.6); three-turn 3,072 / 3,674 / 3,427 tokens, 20.8 / 31.9 / 30.1 s | `note_costs.csv` | rows 14, 15 |
| 06 | DeepSeek V4 Flash 8,192 / 8,466 / 8,864 tokens, 19.2 / 25.0 / 27.3 s; Qwen3.6-27B with the ask note median 4.1 s (longest 4.9), median 4,790 tokens (largest 5,717); with the memory note alone 4,458 to 5,609 tokens, 3.6 to 4.7 s | `note_costs.csv` | rows 16 to 18 |
| 07 table | GLM-4.7 Full (kept in place) | `template_rendering_of_a_mid_conversation_note.csv` | row label as in the file (GLM-4.7-Flash is a separate row) |
| 07 table | Gemma 4 31B QAT (kept in place) | `template_rendering_of_a_mid_conversation_note.csv` | row label as in the file |
| 07 table, 08 | 8 kept, 5 dropped, 4 refused, 2 moved (both DeepSeek V4 Flash files); 17 of 19; all 19 | `template_rendering_of_a_mid_conversation_note.csv` | column counts |
| 08 | item 1: 2 of 2 on the next message, 0 of 2 on the one after | `other_counts.csv` | rows G2-m2, G2-m3 |
| 08 | item 4: GPT-4o 2024-11-20 script count 20 of 24, memory note, no ask instruction | `other_counts.csv` | row A5 |
| 10 | 11 yes + 1 partial; 13 of 15 | `honesty_probe.csv` | 30b and 235b HP0 + HP1 |
| 10 | 25 to 29 of 72; 7 down | as section 06 | |
| 10 | 2 of 15, 6 of 15 (8 of 30); 15 of 24 on the 30B, 21 of 24 on the 235B | `exam_real_question_back_by_model.csv`; `exam_real_question_back_by_note.csv` system-turn row; `other_counts.csv` rows S1, S2 | |
| 10 | May 12 of 24 or 13 of 24 | `other_counts.csv` | rows A6, A7 |
| 11 | four of the six LoRA adapters took this exam | the linked page `../small-finetune/` | its title and subtitle (six adapters); its list item "With the full history" (the four Qwen adapters took the same exam) |
