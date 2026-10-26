# NUMBERS.md: where every figure on the page comes from

If a number on the page disagrees with a file in the package, the file is right and the page is wrong.

**The two places this page looks like it argues with itself.**
1. The table in section 02 prints reply-level averages (each reply counted once, except first-person "I" per 100 words, which is total "I" divided by total words). The gap sizes, ranges and the "gap between snapshots" labels come from the conversation-level paired table, where each conversation counts once. They differ by about 1 to 2 words per reply on length and by about two tenths of a sentence, for example November words per reply is 154.8 at reply level and 156.8 at conversation level.
2. The 18 truncation flags in the project's QA file are 17 short-chat replies and 1 conversation. In the long-conversation runs the cut removes that one conversation (5 replies per snapshot) from all three snapshots, so the page says 353 of 354.

Paths in the Source column are relative to the data package (`data/`). Label "measured" means a count over recorded replies. Figures marked "stated" are OpenAI's dates, read on 25 October 2026 on OpenAI's API deprecations page, not measured here.

| Id | As shown on the page | File | Field or derivation | Label |
|---|---|---|---|---|
| `convs_total` | 1,062 | `tables/count_reconciliation.json` | full_run_conversations_total | measured |
| `convs_per_snapshot` | 354 | `tables/count_reconciliation.json` | full_run_conversations_by_snapshot | measured |
| `replies_total` | 5,049 | `tables/count_reconciliation.json` | full_run_model_turns_total | measured |
| `replies_per_snapshot` | 1,683 | `tables/count_reconciliation.json` | full_run_model_turns_by_snapshot | measured |
| `convs_used` | 353 | `tables/stats_meta.json` | paired_conversations | measured |
| `replies_used_per_snapshot` | 1,678 | `tables/stats_meta.json` | model_replies_per_snapshot_used | measured |
| `groups` | 19 | `tables/inventory_by_lane.csv` | number of rows | measured |
| `dropped_replies_per_snapshot` | 5 | `derived` | replies_per_snapshot minus replies_used_per_snapshot | measured |
| `human_msgs` | 1,683 | `tables/context_human_side.json` | scripted_human_messages_per_snapshot | measured |
| `human_msgs_em` | 8% | `tables/context_human_side.json` | share_with_an_em_dash | measured |
| `human_msgs_em_n` | 133 | `tables/context_human_side.json` | messages_with_an_em_dash | measured |
| `qa_trunc_total` | 18 | `tables/design_checks.json` | qa_flags_by_kind.truncation | measured |
| `has_emdash_pct_May` | 17% | `tables/reply_level_table.csv` | row has_emdash, value_May 2024 x 100 (= numerator/denominator) | measured |
| `has_emdash_pct_Aug` | 19% | `tables/reply_level_table.csv` | row has_emdash, value_Aug 2024 x 100 (= numerator/denominator) | measured |
| `has_emdash_pct_Nov` | 86% | `tables/reply_level_table.csv` | row has_emdash, value_Nov 2024 x 100 (= numerator/denominator) | measured |
| `questions_May` | 1.07 | `tables/reply_level_table.csv` | row questions, value_May 2024 | measured |
| `questions_Aug` | 0.99 | `tables/reply_level_table.csv` | row questions, value_Aug 2024 | measured |
| `questions_Nov` | 2.55 | `tables/reply_level_table.csv` | row questions, value_Nov 2024 | measured |
| `words_May` | 122 | `tables/reply_level_table.csv` | row words, value_May 2024 | measured |
| `words_Aug` | 77 | `tables/reply_level_table.csv` | row words, value_Aug 2024 | measured |
| `words_Nov` | 155 | `tables/reply_level_table.csv` | row words, value_Nov 2024 | measured |
| `sentences_May` | 10.0 | `tables/reply_level_table.csv` | row sentences, value_May 2024 | measured |
| `sentences_Aug` | 5.9 | `tables/reply_level_table.csv` | row sentences, value_Aug 2024 | measured |
| `sentences_Nov` | 11.7 | `tables/reply_level_table.csv` | row sentences, value_Nov 2024 | measured |
| `has_question_pct_May` | 74% | `tables/reply_level_table.csv` | row has_question, value_May 2024 x 100 (= numerator/denominator) | measured |
| `has_question_pct_Aug` | 78% | `tables/reply_level_table.csv` | row has_question, value_Aug 2024 x 100 (= numerator/denominator) | measured |
| `has_question_pct_Nov` | 90% | `tables/reply_level_table.csv` | row has_question, value_Nov 2024 x 100 (= numerator/denominator) | measured |
| `ends_question_pct_May` | 59% | `tables/reply_level_table.csv` | row ends_question, value_May 2024 x 100 (= numerator/denominator) | measured |
| `ends_question_pct_Aug` | 69% | `tables/reply_level_table.csv` | row ends_question, value_Aug 2024 x 100 (= numerator/denominator) | measured |
| `ends_question_pct_Nov` | 67% | `tables/reply_level_table.csv` | row ends_question, value_Nov 2024 x 100 (= numerator/denominator) | measured |
| `emdash_May` | 0.27 | `tables/reply_level_table.csv` | row emdash, value_May 2024 | measured |
| `emdash_Aug` | 0.25 | `tables/reply_level_table.csv` | row emdash, value_Aug 2024 | measured |
| `emdash_Nov` | 1.97 | `tables/reply_level_table.csv` | row emdash, value_Nov 2024 | measured |
| `exclaim_May` | 0.30 | `tables/reply_level_table.csv` | row exclaim, value_May 2024 | measured |
| `exclaim_Aug` | 0.37 | `tables/reply_level_table.csv` | row exclaim, value_Aug 2024 | measured |
| `exclaim_Nov` | 0.19 | `tables/reply_level_table.csv` | row exclaim, value_Nov 2024 | measured |
| `emoji_May` | 0.003 | `tables/reply_level_table.csv` | row emoji, value_May 2024 | measured |
| `emoji_Aug` | 0.002 | `tables/reply_level_table.csv` | row emoji, value_Aug 2024 | measured |
| `emoji_Nov` | 0.058 | `tables/reply_level_table.csv` | row emoji, value_Nov 2024 | measured |
| `list_items_May` | 0.93 | `tables/reply_level_table.csv` | row list_items, value_May 2024 | measured |
| `list_items_Aug` | 0.14 | `tables/reply_level_table.csv` | row list_items, value_Aug 2024 | measured |
| `list_items_Nov` | 0.42 | `tables/reply_level_table.csv` | row list_items, value_Nov 2024 | measured |
| `has_list_pct_May` | 10% | `tables/reply_level_table.csv` | row has_list, value_May 2024 x 100 (= numerator/denominator) | measured |
| `has_list_pct_Aug` | 3% | `tables/reply_level_table.csv` | row has_list, value_Aug 2024 x 100 (= numerator/denominator) | measured |
| `has_list_pct_Nov` | 6% | `tables/reply_level_table.csv` | row has_list, value_Nov 2024 x 100 (= numerator/denominator) | measured |
| `bold_May` | 0.82 | `tables/reply_level_table.csv` | row bold, value_May 2024 | measured |
| `bold_Aug` | 0.17 | `tables/reply_level_table.csv` | row bold, value_Aug 2024 | measured |
| `bold_Nov` | 0.41 | `tables/reply_level_table.csv` | row bold, value_Nov 2024 | measured |
| `headers_May` | 0.17 | `tables/reply_level_table.csv` | row headers, value_May 2024 | measured |
| `headers_Aug` | 0.00 | `tables/reply_level_table.csv` | row headers, value_Aug 2024 | measured |
| `headers_Nov` | 0.14 | `tables/reply_level_table.csv` | row headers, value_Nov 2024 | measured |
| `i_per100_May` | 1.19 | `tables/reply_level_table.csv` | row i_per100, value_May 2024 | measured |
| `i_per100_Aug` | 0.90 | `tables/reply_level_table.csv` | row i_per100, value_Aug 2024 | measured |
| `i_per100_Nov` | 1.12 | `tables/reply_level_table.csv` | row i_per100, value_Nov 2024 | measured |
| `signoff_pct_May` | 10% | `tables/reply_level_table.csv` | row signoff, value_May 2024 x 100 (= numerator/denominator) | measured |
| `signoff_pct_Aug` | 13% | `tables/reply_level_table.csv` | row signoff, value_Aug 2024 x 100 (= numerator/denominator) | measured |
| `signoff_pct_Nov` | 4% | `tables/reply_level_table.csv` | row signoff, value_Nov 2024 x 100 (= numerator/denominator) | measured |
| `praise_open_pct_May` | 10% | `tables/reply_level_table.csv` | row praise_open, value_May 2024 x 100 (= numerator/denominator) | measured |
| `praise_open_pct_Aug` | 9% | `tables/reply_level_table.csv` | row praise_open, value_Aug 2024 x 100 (= numerator/denominator) | measured |
| `praise_open_pct_Nov` | 6% | `tables/reply_level_table.csv` | row praise_open, value_Nov 2024 x 100 (= numerator/denominator) | measured |
| `feeling_named_pct_May` | 2% | `tables/reply_level_table.csv` | row feeling_named, value_May 2024 x 100 (= numerator/denominator) | measured |
| `feeling_named_pct_Aug` | 1% | `tables/reply_level_table.csv` | row feeling_named, value_Aug 2024 x 100 (= numerator/denominator) | measured |
| `feeling_named_pct_Nov` | 1% | `tables/reply_level_table.csv` | row feeling_named, value_Nov 2024 x 100 (= numerator/denominator) | measured |
| `options_pct_May` | 2% | `tables/reply_level_table.csv` | row options, value_May 2024 x 100 (= numerator/denominator) | measured |
| `options_pct_Aug` | 1% | `tables/reply_level_table.csv` | row options, value_Aug 2024 x 100 (= numerator/denominator) | measured |
| `options_pct_Nov` | 1% | `tables/reply_level_table.csv` | row options, value_Nov 2024 x 100 (= numerator/denominator) | measured |
| `n_measures` | 18 | `tables/paired_differences.csv` | distinct measure values per pair | measured |
| `n_gap_MA` | 11 | `tables/paired_differences.csv` | measures with p_holm < 0.05, pair May 2024 -> Aug 2024 | measured |
| `n_gap_AN` | 15 | `tables/paired_differences.csv` | measures with p_holm < 0.05, pair Aug 2024 -> Nov 2024 | measured |
| `n_gap_MN` | 14 | `tables/paired_differences.csv` | measures with p_holm < 0.05, pair May 2024 -> Nov 2024 | measured |
| `n_large_MA` | 0 | `tables/paired_differences.csv` | measures with abs(dz) >= 0.8, pair May 2024 -> Aug 2024 | measured |
| `n_large_AN` | 5 | `tables/paired_differences.csv` | measures with abs(dz) >= 0.8, pair Aug 2024 -> Nov 2024 | measured |
| `n_large_MN` | 3 | `tables/paired_differences.csv` | measures with abs(dz) >= 0.8, pair May 2024 -> Nov 2024 | measured |
| `d6_words_May_Aug_gap` | +1.2 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Aug 2024, measure words, mean_gap_between_snapshots | measured |
| `d6_words_May_Aug_band` | 4.4 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Aug 2024, measure words, largest_run_to_run_gap | measured |
| `d6_words_Aug_Nov_gap` | +8.1 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair Aug 2024 -> Nov 2024, measure words, mean_gap_between_snapshots | measured |
| `d6_words_Aug_Nov_band` | 2.9 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair Aug 2024 -> Nov 2024, measure words, largest_run_to_run_gap | measured |
| `d6_words_May_Nov_gap` | +9.3 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Nov 2024, measure words, mean_gap_between_snapshots | measured |
| `d6_words_May_Nov_band` | 4.4 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Nov 2024, measure words, largest_run_to_run_gap | measured |
| `d6_has_emdash_May_Aug_gap` | +0.07 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Aug 2024, measure has_emdash, mean_gap_between_snapshots | measured |
| `d6_has_emdash_May_Aug_band` | 0.17 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Aug 2024, measure has_emdash, largest_run_to_run_gap | measured |
| `d6_has_emdash_Aug_Nov_gap` | +0.31 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair Aug 2024 -> Nov 2024, measure has_emdash, mean_gap_between_snapshots | measured |
| `d6_has_emdash_Aug_Nov_band` | 0.17 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair Aug 2024 -> Nov 2024, measure has_emdash, largest_run_to_run_gap | measured |
| `d6_has_emdash_May_Nov_gap` | +0.39 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Nov 2024, measure has_emdash, mean_gap_between_snapshots | measured |
| `d6_has_emdash_May_Nov_band` | 0.17 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Nov 2024, measure has_emdash, largest_run_to_run_gap | measured |
| `d6_emdash_May_Aug_gap` | +0.07 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Aug 2024, measure emdash, mean_gap_between_snapshots | measured |
| `d6_emdash_May_Aug_band` | 0.17 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Aug 2024, measure emdash, largest_run_to_run_gap | measured |
| `d6_emdash_Aug_Nov_gap` | +0.43 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair Aug 2024 -> Nov 2024, measure emdash, mean_gap_between_snapshots | measured |
| `d6_emdash_Aug_Nov_band` | 0.17 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair Aug 2024 -> Nov 2024, measure emdash, largest_run_to_run_gap | measured |
| `d6_emdash_May_Nov_gap` | +0.50 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Nov 2024, measure emdash, mean_gap_between_snapshots | measured |
| `d6_emdash_May_Nov_band` | 0.17 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Nov 2024, measure emdash, largest_run_to_run_gap | measured |
| `d6_exclaim_May_Aug_gap` | -0.00 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Aug 2024, measure exclaim, mean_gap_between_snapshots | measured |
| `d6_exclaim_May_Aug_band` | 0.22 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Aug 2024, measure exclaim, largest_run_to_run_gap | measured |
| `d6_exclaim_Aug_Nov_gap` | -0.44 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair Aug 2024 -> Nov 2024, measure exclaim, mean_gap_between_snapshots | measured |
| `d6_exclaim_Aug_Nov_band` | 0.22 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair Aug 2024 -> Nov 2024, measure exclaim, largest_run_to_run_gap | measured |
| `d6_exclaim_May_Nov_gap` | -0.44 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Nov 2024, measure exclaim, mean_gap_between_snapshots | measured |
| `d6_exclaim_May_Nov_band` | 0.06 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Nov 2024, measure exclaim, largest_run_to_run_gap | measured |
| `d6_questions_May_Aug_gap` | +0.11 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Aug 2024, measure questions, mean_gap_between_snapshots | measured |
| `d6_questions_May_Aug_band` | 0.22 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Aug 2024, measure questions, largest_run_to_run_gap | measured |
| `d6_questions_Aug_Nov_gap` | -0.13 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair Aug 2024 -> Nov 2024, measure questions, mean_gap_between_snapshots | measured |
| `d6_questions_Aug_Nov_band` | 0.22 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair Aug 2024 -> Nov 2024, measure questions, largest_run_to_run_gap | measured |
| `d6_questions_May_Nov_gap` | -0.02 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Nov 2024, measure questions, mean_gap_between_snapshots | measured |
| `d6_questions_May_Nov_band` | 0.11 | `tables/d6_snapshot_gaps.csv` | basis cuts_honored, pair May 2024 -> Nov 2024, measure questions, largest_run_to_run_gap | measured |
| `d6_verdicts_that_change` | 2 | `tables/d6_snapshot_gaps.csv` | count of (pair, measure) rows among those shown whose verdict differs between basis cuts_honored and basis truncated_replies_kept | measured |
| `d6_prompts` | 10 | `tables/count_reconciliation.json` | d6_banter_prompts | measured |
| `d6_records_per_snapshot` | 60 | `tables/count_reconciliation.json` | d6_banter_records_by_snapshot | measured |
| `d6_truncated` | 17 | `tables/count_reconciliation.json` | sum of d6_banter_finish_length_by_snapshot (6 + 5 + 6) | measured |
| `d6_cells` | 18 of the 20 prompt-and-temperature cells (10 prompts x 2 temperatures) | `tables/d6_snapshot_means.csv` | cells_on_all_three, basis cuts_honored | measured |
| `hf_moves_MA` | 15 | `tables/house_feature_summary.json` | May 2024 -> Aug 2024: moves | measured |
| `hf_moves_AN` | 47 | `tables/house_feature_summary.json` | Aug 2024 -> Nov 2024: moves | measured |
| `hf_moves_MN` | 47 | `tables/house_feature_summary.json` | May 2024 -> Nov 2024: moves | measured |
| `hf_features` | 131 | `tables/house_feature_summary.json` | features | measured |
| `group_table` | 19 rows | `tables/inventory_by_lane.csv; tables/context_system_prompts.csv` | all columns | measured (setup read from the run records) |
| `w_an_groups` | 19 of 19 | `tables/lane_direction.csv` | pair Aug->Nov, measure words: groups_B_higher of lane_groups | measured |
| `w_ma_groups` | 19 of 19 | `tables/lane_direction.csv` | pair May->Aug, measure words: groups_A_higher of lane_groups | measured |
| `w_mn_groups` | 16 of 19 | `tables/lane_direction.csv` | pair May->Nov, measure words: groups_B_higher of lane_groups | measured |
| `em_an_groups` | 19 of 19 | `tables/lane_direction.csv` | pair Aug->Nov, measure has_emdash: groups_B_higher of lane_groups | measured |
| `em_mn_groups` | 19 of 19 | `tables/lane_direction.csv` | pair May->Nov, measure has_emdash: groups_B_higher of lane_groups | measured |
| `q_an_groups` | 19 of 19 | `tables/lane_direction.csv` | pair Aug->Nov, measure questions: groups_B_higher of lane_groups | measured |
| `q_mn_groups` | 19 of 19 | `tables/lane_direction.csv` | pair May->Nov, measure questions: groups_B_higher of lane_groups | measured |
| `first_emdash_May` | 14% | `tables/first_reply_means.csv` | row has_emdash, mean_May 2024 x 100 | measured |
| `first_emdash_Aug` | 14% | `tables/first_reply_means.csv` | row has_emdash, mean_Aug 2024 x 100 | measured |
| `first_emdash_Nov` | 76% | `tables/first_reply_means.csv` | row has_emdash, mean_Nov 2024 x 100 | measured |
| `first_q_May` | 1.3 | `tables/first_reply_means.csv` | row questions, mean_May 2024 | measured |
| `first_q_Aug` | 1.2 | `tables/first_reply_means.csv` | row questions, mean_Aug 2024 | measured |
| `first_q_Nov` | 3.0 | `tables/first_reply_means.csv` | row questions, mean_Nov 2024 | measured |
| `first_replies` | 353 | `tables/first_reply_means.csv` | first_replies_per_snapshot | measured |
| `d5_emdash_May` | 12% | `tables/by_lane.csv` | row d5/main, has_emdash_May 2024 x 100 | measured |
| `d5_emdash_Aug` | 19% | `tables/by_lane.csv` | row d5/main, has_emdash_Aug 2024 x 100 | measured |
| `d5_emdash_Nov` | 89% | `tables/by_lane.csv` | row d5/main, has_emdash_Nov 2024 x 100 | measured |
| `d5_convs` | 30 | `tables/by_lane.csv` | row d5/main, paired_conversations | measured |
| `d5_prompt_words` | 23 | `tables/context_system_prompts.csv` | row d5/main, words | measured |
| `other_prompt_em_range` | 9 to 13 | `tables/context_system_prompts.csv` | em_dashes_in_prompt over the other 18 groups (min to max) | measured |
| `ci_q_AN` | 1.41 to 1.67 | `tables/paired_differences.csv` | pair Aug->Nov, measure questions, ci95 | measured |
| `ci_q_MN` | 1.33 to 1.60 | `tables/paired_differences.csv` | pair May->Nov, measure questions, ci95 | measured |
| `permutations` | 10,000 | `tables/stats_meta.json` | sign_flip_permutations | measured |
| `bootstraps` | 10,000 | `tables/stats_meta.json` | bootstrap_resamples | measured |
| `words_creative_may` | 426 | `tables/by_lane.csv` | row creative/main, words_May 2024 | measured |
| `words_task_may` | 277 | `tables/by_lane.csv` | row vignette/task, words_May 2024 | measured |
| `groups_sharing_prompt` | 5 | `tables/inventory_by_lane.csv` | rows whose system_prompt_sha256 starts 2c0b5376 | measured |
| `groups_with_long_prompt` | 18; the 18 prompts contain the words "bulleted list" | `tables/context_system_prompts.csv` | rows with mentions_a_bulleted_list = 1 (a substring test: the words occur or they do not); the other row, d5/main, is the 23-word prompt, 0. That the passage tells the model to stay with the person rather than hand a list over is a read of the prompt text in the collection records, which the package does not hold | measured |
| `long_prompt_words_min` | 412 | `tables/context_system_prompts.csv` | min of words over rows with mentions_a_bulleted_list = 1 | measured |
| `long_prompt_words_max` | 574 | `tables/context_system_prompts.csv` | max of words over rows with mentions_a_bulleted_list = 1 | measured |
| `shared_prompt_chars` | 2,337 | `tables/context_system_prompts.csv` | characters for the prompt starting 2c0b5376 | measured |
| `d6_replies_total` | 180 | `tables/count_reconciliation.json` | sum of d6_banter_records_by_snapshot | measured |
| `d6_max_tokens` | 200 | `tables/count_reconciliation.json` | d6_max_tokens | measured |
| `pack_pairs` | 36 | `pack/three_snapshots_pairs.jsonl` | number of lines | measured |
| `pack_messages` | 12 | `pack/three_snapshots_pairs.jsonl` | distinct scenario_id | measured |
| `emoji_count_Nov` | 98 | `tables/reply_level_table.csv` | row emoji, numerator_Nov 2024 | measured |
| `emoji_count_May` | 5 | `tables/reply_level_table.csv` | row emoji, numerator_May 2024 | measured |
| `emoji_count_Aug` | 3 | `tables/reply_level_table.csv` | row emoji, numerator_Aug 2024 | measured |
| `headers_count_May` | 291 | `tables/reply_level_table.csv` | row headers, numerator_May 2024 | measured |
| `headers_count_Nov` | 233 | `tables/reply_level_table.csv` | row headers, numerator_Nov 2024 | measured |
| `headers_count_Aug` | 0 | `tables/reply_level_table.csv` | row headers, numerator_Aug 2024 | measured |
| `has_emdash_count_Nov` | 1,446 | `tables/reply_level_table.csv` | row has_emdash, numerator_Nov 2024 | measured |
| `has_emdash_den_Nov` | 1,678 | `tables/reply_level_table.csv` | row has_emdash, denominator_Nov 2024 | measured |
| `has_emdash_count_May` | 292 | `tables/reply_level_table.csv` | row has_emdash, numerator_May 2024 | measured |
| `has_emdash_count_Aug` | 315 | `tables/reply_level_table.csv` | row has_emdash, numerator_Aug 2024 | measured |
| `endq_Aug` | 69% | `tables/reply_level_table.csv` | row ends_question, value_Aug 2024 x 100 (= numerator/denominator) | measured |
| `endq_Nov` | 67% | `tables/reply_level_table.csv` | row ends_question, value_Nov 2024 x 100 (= numerator/denominator) | measured |
| `endq_May` | 59% | `tables/reply_level_table.csv` | row ends_question, value_May 2024 x 100 (= numerator/denominator) | measured |
| `headers_den_May` | 1,678 | `tables/reply_level_table.csv` | row headers, denominator_May 2024 | measured |
| `emoji_den_Nov` | 1,678 | `tables/reply_level_table.csv` | row emoji, denominator_Nov 2024 | measured |
| `pack_small_everyday_story` | three replies as printed | `pack/three_snapshots_pairs.jsonl` | pair_id starting small-everyday-story-f41e61403a | measured (verbatim, dashes as the model wrote them) |
| `pack_nearly_at_the_top` | three replies as printed | `pack/three_snapshots_pairs.jsonl` | pair_id starting nearly-at-the-top-of-the-hill-48056a1d85 | measured (verbatim, dashes as the model wrote them) |
| `d6_flip_shown` | 2 | `tables/d6_snapshot_gaps.csv` | verdict flips shown above | measured |
| `human_identical` | 354 | `tables/design_checks.json` | human_side_identical_all_three | measured |
| `clock_may` | 23 October 2026 | not in the package | OpenAI deprecations page, read 25 October 2026 (agrees with the 14 October read) | stated |
| `clock_aug_nov` | 14 January 2027 | not in the package | same | stated |
| `snapshot_run_date` | 4 July 2026 | `pack/three_snapshots_pairs.jsonl` | field run_date on every line (2026-07-04) | measured |
| `temperature_range` | 0.7 to 1.1 | `tables/inventory_by_lane.csv` | min and max of temperature | measured |
| `turns_per_conversation` | four to six | `tables/reply_measures.csv` | max turn_no per conversation: 117 with 4, 207 with 5, 30 with 6 | measured |
| `word_list_audit` | 25 flagged replies read, 19 of 25 right | `README.md` (word-list audit) | 25 replies flagged by the "tells the user how they feel" list were read; 19 judged correct, 6 not | measured (hand audit) |
| `repetition_flags` | Five more flags for repeated text, all on one May writing-together conversation, left in | `tables/design_checks.json` | qa_flags_by_kind.degenerate_repetition 5; repetition_flags_not_cut: 5 flags on one writing-together conversation (May 2024, seed writing-together-b9faad03f1) | measured |
| `prompt_date_line` | 15 January 2025 | `tables/context_system_prompts.csv` | has_date_line_2025_01_15 = 1 in all 19 rows | measured |
| `neutral_prompt` | 23-word prompt (the other 18 groups: 412 to 574 words) | `tables/context_system_prompts.csv` | words, row d5/main | measured |
| `talk_through_groups` | two groups run twice, with and without a talk-it-through line | `tables/context_system_prompts.csv` | rows d3/bare vs d3/nudge and w2/bare vs w2/nudge | measured |
| `earlier_study` | 131 text features, November snapshot and 25 other models | live page `/gpt4o-measured/` and its package | published 2026-09 | measured (earlier study) |
| `creative_used_convs` | 24 | `tables/by_lane.csv` | row creative/main, paired_conversations | measured |
| `creative_used_replies` | 120 | `derived` | 24 conversations x 5 replies (the group's replies per conversation) | measured |
| `d6_cap_tokens` | 200 | `tables/count_reconciliation.json` | d6_max_tokens | measured |
| `d6_cut_replies` | 17 of 180 | `tables/cuts.csv` | short-chat truncation flags (6 + 5 + 6) | measured |
| `other_language_convs` | 25 | `tables/by_lane.csv` | row d2/main, paired_conversations | measured |
| `hf_moves_rule` | p below 0.01, effect at least 0.3 | `tables/house_feature_pairs.csv` | a feature moves when Holm p < 0.01 and abs(dz) >= 0.3 (README note 5) | rule |
| `inventory_table` | section 08 group table (conversations, replies, temperature, max tokens, prompt words, prompt hash) | `tables/inventory_by_lane.csv` | printed as the file holds them, one row per group; the writing-together row adds the used counts 24 and 120 | measured |
| `provenance_temperatures` | 0.7 to 1.1 in the group table | `tables/inventory_by_lane.csv` | column temperature | measured |
| `diff_q_AN` | 1.54 | `tables/paired_differences.csv` | pair Aug->Nov, measure questions, diff_B_minus_A (conversation-level) | measured |
| `diff_q_MN` | 1.46 | `tables/paired_differences.csv` | pair May->Nov, measure questions, diff_B_minus_A (conversation-level) | measured |
| `level_gap_words` | about 1 to 2 words per reply | `tables/reply_level_table.csv` against `tables/paired_differences.csv` | words: 122.06 / 77.14 / 154.82 reply-level against 124.31 / 78.17 / 156.75 conversation-level | measured |
| `level_gap_sentences` | about two tenths of a sentence | same two files | sentences: 9.98 / 5.89 / 11.69 against 10.22 / 5.98 / 11.87 | measured |
| `run_convs` | 354 | `tables/count_reconciliation.json` | full_run_conversations_by_snapshot | measured |
| `used_convs` | 353 | `tables/stats_meta.json` | paired_conversations | measured |
| `d6_temperatures` | 1.0 and 1.15 | `tables/count_reconciliation.json` | d6_banter_temperatures | measured |
| `d6_system_prompt` | the shared system prompt whose hash starts 2c0b5376 (2,337 characters, 412 words), the same as five long-conversation groups | `tables/count_reconciliation.json`; `tables/context_system_prompts.csv` | d6_system_prompt_sha256 (2c0b5376827e..., all three snapshots); characters and words of the row with that hash | measured |
| `d6_replies_used` | 54 per snapshot | `tables/d6_snapshot_means.csv` | basis cuts_honored, replies_May / replies_Aug / replies_Nov (18 cells x 3 runs); `tables/d6_meta.json` uncut replies 54 / 55 / 54, the extra August reply outside the 18 cells | measured |
| `d6_flip_rows` | em dashes per reply Aug->Nov outside to inside; questions May->Nov inside to outside, gap about +0.23 | `tables/d6_snapshot_gaps.csv` | rows emdash Aug->Nov and questions May->Nov, basis cuts_honored against truncated_replies_kept (mean gap -0.018519 to 0.233333) | measured |
| `i_per100_rate` | total "I" over total words | `tables/reply_level_table.csv` | row i_per100: numerators 2,445 / 1,171 / 2,900 over 204,814 / 129,436 / 259,788 words | measured |

## Rounded figures from the package that the page does not print

These rows are kept so a reader of the package can match the rounding; none of them appears on the page.

| Id | Rounded value | File | Field or derivation | Label |
|---|---|---|---|---|
| `dz_em_AN` | 2.3 | `tables/paired_differences.csv` | pair Aug->Nov, measure has_emdash, dz | measured |
| `dz_q_AN` | 1.2 | `tables/paired_differences.csv` | pair Aug->Nov, measure questions, dz | measured |
| `dz_w_AN` | 1.1 | `tables/paired_differences.csv` | pair Aug->Nov, measure words, dz | measured |
| `ci_words_AN` | 71 to 87 | `tables/paired_differences.csv` | pair Aug->Nov, measure words, ci95_lo to ci95_hi (conversation-level mean difference) | measured |
| `ci_em_AN` | 64 to 70 points | `tables/paired_differences.csv` | pair Aug->Nov, measure has_emdash, ci95 x 100 (conversation-level mean difference) | measured |
| `ci_em_MN` | 65 to 71 points | `tables/paired_differences.csv` | pair May->Nov, measure has_emdash, ci95 x 100 | measured |
| `sens_may_nov_words_dz` | 0.49 to 0.90 | `tables/sensitivity.csv` | May -> Nov words, dz all lanes and dz without creative and vignette/task | measured |

Note (2026-10-25): the page prints the table's decimals for questions (1.07, 0.99, 2.55) and em dashes per reply (0.27, 0.25, 1.97) everywhere, so one figure has one printing.
