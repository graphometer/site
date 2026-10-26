# Three GPT-4o snapshots, counted: data package

This is the evidence behind the page "Three GPT-4o snapshots, counted against each other". It holds the counts, the statistics, the scripts that produced them and a small sample pack. The reply texts are not here, except the 36 pairs of the sample pack.

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.

## Where this package will look like it argues with itself

1. **Two kinds of average.** The page table prints reply-level averages: every reply counts once (`tables/reply_level_table.csv`), except first-person "I" per 100 words, which is total "I" divided by total words, not the average of each reply's own rate (the conversation-level value for that row is the same ratio inside each conversation). The gap sizes, ranges and "large / clear / none" labels come from the conversation-level paired table (`tables/paired_differences.csv`), where every conversation counts once. They differ by about 1 to 2 words per reply on length (November words per reply is 154.8 at reply level and 156.8 at conversation level) and by about two tenths of a sentence. On questions the conversation-level gaps are 1.54 (August to November) and 1.46 (May to November), not 2.55 minus 0.99 or 2.55 minus 1.07. `tables/snapshot_means.csv` holds the conversation-level means and `tables/reply_level_means.json` holds the reply-level means again, with medians, in a different layout. The page prints `reply_level_table.csv`.
2. **1,683 replies per snapshot, 1,678 used.** The records hold 354 scripted conversations and 1,683 model replies per snapshot (`tables/inventory_by_lane.csv`). The project's quality check flagged one conversation whose reply ran into the length limit. It was dropped on all three snapshots, five replies each, so the pairs stay matched. Everything in `reply_level_table.csv`, `paired_differences.csv` and the other analysis tables uses 353 conversations and 1,678 replies per snapshot. `reply_measures.csv` still lists the dropped replies, with `cut` = 1.
3. **18 flags, 17 and 1.** The project's quality file lists 18 truncation flags. Seventeen are short-chat replies (6 + 5 + 6). One is the conversation above. It also lists five repetition flags. All five sit in one writing-together conversation on the May snapshot; they were left in.
4. **`p_holm` is 0.0018 in many rows.** The shuffle test runs 10,000 random sign flips, so the smallest raw p it can return is 1/10,001. Holm correction across 18 counts multiplies the smallest by 18, giving 18/10,001 = 0.0018. That figure is a floor, not a measured p-value. It means no shuffle matched the observed gap. The page never prints it.
5. **The house-feature test uses a different p.** `tables/house_feature_pairs.csv` tests all 142 features of the earlier study's extractor (131 of them in its distance set) with a normal-approximation p over the 353 paired conversations, Holm-corrected over the 131. A feature "moves" there when Holm p is below 0.01 and the absolute paired effect size (`dz`) is at least 0.3. This is a different yardstick from the page's large / clear labels and is used only for the page's one sentence about "15, 47 and 47 of 131".
6. **Two word-list counts are rough.** `feeling_named` (replies that tell the user how they feel) and `options` (replies that offer options) come from short word lists with strict patterns. They miss many cases. The "feeling" list was audited by reading 25 of the sentences it flagged: 19 were right and 6 were not (a drafted message, a hypothetical, generic advice). Read both as direction only. They show no clear gap between any pair.
7. **The short-chat set has two bases.** `tables/d6_*.csv` hold the main basis (`cuts_honored`: the 17 cut-off replies removed, 18 prompt-and-temperature cells survive on all three snapshots) and a check basis (`truncated_replies_kept`: all 60 replies per snapshot, 20 cells, lengths capped at the 200-token limit). Two of the fifteen verdicts shown on the page change between the two: em dashes per reply, August to November (outside under cuts honoured, inside with the cut replies kept), and questions, May to November (inside, then outside with the gap reversing from about -0.02 to about +0.23). The main basis is 54 replies per snapshot; one further uncut August reply sits in a cell not present on all three snapshots. Both bases are in the files.
8. **Word counts are runs of A to Z letters, digits and apostrophes.** The extractor counts runs of A to Z letters, digits and apostrophes. Replies in other writing systems are undercounted. This touches only the "Another language" group (25 of 353 conversations). `tables/sensitivity.csv` repeats the headline comparisons without that group and without the two longest-output groups (writing together, practical task help); it stores paired effect sizes only, no p, so it cannot move a label to or from clear. Without the other-language group every headline gap keeps its direction. Without the two longest-output groups, May against November on words moves from clear to large (dz 0.49 to 0.90), and em dashes per reply, May against August, changes sign by about two hundredths of a dash on a gap already labelled none.

## Conversation ids

Every `scenario_id` in the shipped tables and the sample pack is the group's plain name plus an opaque code (a scenario shared by a group and its talk-it-through variant keeps one code, told apart by the `variant` column), and `pair_id` in the pack adds the snapshot. The collection's own conversation ids are not shipped; the site holds the key. The scripts, run on the collection, print the collection's ids, so a re-run matches the shipped tables row for row, not id for id.

## Plain names and the collection's lane ids

The page and the tables use plain names for the 19 groups. Each is one lane of the collection, named here by the collection's own id so a reader of the package can match them. The ids are also the `lane` and `variant` columns of `tables/inventory_by_lane.csv`.

| Plain name on the page | Lane id in the collection | Variant |
|---|---|---|
| Staying with a hard moment | `accompaniment` | `main` |
| Writing together | `creative` | `main` |
| Good news shared | `d1` | `main` |
| Another language | `d2` | `main` |
| Reading how someone feels | `d3` | `bare` |
| Reading how someone feels, with a talk-it-through line | `d3` | `nudge` |
| Warm refusal | `d4` | `main` |
| Recovering from a cold answer | `d5` | `main` |
| Work and career help | `vignette` | `career` |
| Practical task help | `vignette` | `task` |
| Small everyday story | `w1` | `main` |
| Ongoing project | `w2` | `bare` |
| Ongoing project, with a talk-it-through line | `w2` | `nudge` |
| A strange idea | `w3` | `main` |
| Nearly at the top of the hill | `w4` | `main` |
| Shared story | `w5` | `main` |
| Micro-story coaching | `w6` | `main` |
| Affirmations | `w7` | `main` |
| Coming back after a gap | `w8` | `main` |

## What is in each folder

| Path | What it holds |
|---|---|
| `tables/inventory_by_lane.csv` | One row per group of conversations (19): plain name, temperature, reply limit, system-prompt sha256, conversations, model replies and length cut-offs per snapshot. Read from the run records. |
| `tables/count_reconciliation.json` | Headline counts recomputed from the records: conversations and replies per snapshot, the supplement (not used in the comparison, two snapshots only), the short-chat set. |
| `tables/design_checks.json` | The design checks: same settings on all three snapshots in every group, the scripted human side identical in all 354 conversations, no model-name mismatch in any reply, the quality flags. |
| `tables/cuts.csv` | The 18 truncation flags from the project's quality file, by snapshot, group and record id. |
| `tables/reply_measures.csv` | One row per model reply (5,049): snapshot, group, scenario id, turn number, the plain counts (words, sentences, questions, headers, list items, bold, em dashes, exclamation marks, emoji, word-list flags), and `cut`. No text. |
| `tables/house_features_by_conversation.csv` | The 142 features of the extractor from the earlier GPT-4o study, averaged over each conversation's replies (1,062 rows). |
| `tables/reply_level_table.csv` | The page table: each count with numerator and denominator per snapshot. |
| `tables/snapshot_means.csv`, `reply_level_means.json`, `first_reply_means.csv` | Conversation-level means; reply-level means with medians and tokens; means over first replies only. |
| `tables/paired_differences.csv` | Every pair of snapshots on every count: paired means, difference, 95% interval (10,000 resamples), effect size `dz`, sign-flip p and Holm p, the share of conversations pointing each way, and the same comparison on first replies only. |
| `tables/by_lane.csv`, `lane_direction.csv`, `lane_ordering.json` | The comparison inside each of the 19 groups; in how many groups each snapshot is higher; the order of the snapshots per group. |
| `tables/sensitivity.csv` | Headline comparisons without the other-language group and without the two longest-output groups. |
| `tables/words_by_turn_position.csv` | Mean words by position in the conversation. |
| `tables/house_feature_pairs.csv`, `house_feature_summary.json` | The 142 features compared pair by pair; counts of features that move, by family. |
| `tables/d6_measures.csv` | One row per short-chat reply (180). |
| `tables/d6_run_bands.csv`, `d6_snapshot_gaps.csv`, `d6_snapshot_means.csv`, `d6_meta.json` | Run-to-run gaps inside each snapshot, gaps between snapshots, and means for the short-chat set, on both bases. |
| `tables/context_human_side.json`, `context_system_prompts.csv` | How often the scripted human side uses an em dash; the size, em-dash count and hash of each group's system prompt. |
| `tables/stats_meta.json` | Seed, number of resamples and shuffles, conversation counts. |
| `tables/pack_selection.csv` | The twelve groups the sample pack draws from, how many conversations passed the rule, and which one was drawn. |
| `pack/three_snapshots_pairs.jsonl` | The sample pack: 36 prompt-and-reply pairs (see below). |
| `pack/README.md` | The research notice and the drawing rule for the pack. |
| `scripts/` | The scripts, in the order `run_all.sh` runs them, and a copy of the published extractor. They read the collection exports (not part of this package). |

## What the numbers are made of

- **Source.** The records of a July 2026 collection: 19 groups of scripted conversations, each run once on each of `gpt-4o-2024-05-13`, `gpt-4o-2024-08-06` and `gpt-4o-2024-11-20` through OpenAI's API on 4 July 2026, plus a short-chat set (10 prompts, 3 runs each at 2 temperatures). The human side was written in advance by an AI. No real person's messages are used.
- **Not used.** A later supplement (August and November snapshots only), the pilot (November only) and the identity-draft lanes. They do not cover all three snapshots.
- **Cuts.** The 18 truncation flags in the project's quality file, as above.
- **Averages.** Per conversation: the mean of its replies on a count; for first-person "I" per 100 words, total I over total words. Per snapshot: the mean over the 353 paired conversations (conversation level) or over the 1,678 replies (reply level).
- **Gap labels.** `dz` is the mean paired difference divided by the standard deviation of the paired differences. Large: absolute `dz` of at least 0.8. Clear: Holm p below 0.05 (and absolute `dz` below 0.8). Otherwise none. A clear gap can be small; `dz` is in the file.
- **Short-chat band.** For each snapshot, runs 1, 2 and 3 of the same prompts at the same temperatures are averaged over the cells. The largest difference between two of those runs is the run-to-run gap. A snapshot gap is "outside" when run 1 against run 1, run 2 against run 2 and run 3 against run 3 all point the same way and each is larger than the largest run-to-run gap of either snapshot.
- **Seeds.** 20261025 for the resamples, the shuffles and the sample-pack draw.

## The sample pack

`pack/three_snapshots_pairs.jsonl` holds 36 pairs: twelve scripted opening messages, each answered by all three snapshots. Each line has the pair id, group, scenario id, snapshot, provider, run date, temperature, reply limit, the sha256 of the system prompt, the message, the reply, the finish reason and the reply's token count. The system prompt itself is named and hashed, not printed. The human side is scripted and contains no real person's words. The replies are outputs of OpenAI's models. Non-ASCII characters, including em dashes, are written as JSON escapes.

## Redactions and omissions

- No reply text outside the 36 pairs. The per-reply table holds counts only.
- No file paths, host names, service names or internal job names. Group names are plain-language names. Scenario ids and record ids are kept; they are labels.
- System prompts are hashed, not printed. Their word and character counts are listed.
- The scripts take the folder of collection exports as an argument; no path is written in them. The private-term word list used when drawing the pack is supplied to `s6_pack.py` as a file at run time and is not part of the package.
- The standard private-term sweep was run over this whole folder and the page. It returned no hits (zero lines). The command and its output are kept with the author's checks.

## Reproducing

`scripts/run_all.sh <exports folder> <output folder> <private-term file>` runs everything in order, in about 25 seconds with Python 3.12 and no outside packages. The page itself is built from these tables by a builder that is not shipped.

Not affiliated with, endorsed by, or connected to OpenAI. GPT-4o and ChatGPT are marks of OpenAI.
