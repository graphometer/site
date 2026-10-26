# Self-description pack: what the model says about itself

These are 40 answers from GPT-4o to questions about what it is: whether it is conscious, whether it cares, what it would say about itself, and what it says when told it may be running on a different model underneath. Read it if you want the raw material behind the "What the Model Says About Itself" section of Friends of 4o.

## Research notice

This is research material. It is a small set of sample replies from a language model, kept so a reader can check what the website says about them. Please cite it as sample replies to tests, and read the "What this is not" section before you use it for anything else.

## What this is

- 40 question-and-answer pairs, one per line, in `self_description.jsonl`. Each line is one JSON record.
- Every question was written in advance. Either it was a fixed list of prompts, or the human side of the conversation was a script written by an AI. No real person talked to the model in any of these records, and no real person's words are in them.
- Every reply is word for word what the model returned. Nothing in a reply was edited, shortened or corrected. Em dashes, odd spacing and any errors in the replies are the model's own.
- Each line gives the model, the date, the temperature (the setting for how varied the wording is; higher means more varied), the name and hash of the system prompt (the standing instructions sent before the conversation), and a source label made of the group's public name plus an opaque code (it matches no file or folder name; the site holds the key).
- The model is GPT-4o from OpenAI, reached through the paid developer interface (the API).

Fields in each record: `id`, `group`, `model`, `model_kind`, `date`, `temperature`, `system_prompt_label`, `system_prompt_sha256`, `system_prompt_note` (only where no system prompt is recorded), `source_id`, `person_side`, `prompt`, `response`.

## Permission

Replies from a paid model's developer interface do not normally go into this site's data packages, because the maker's terms on sharing them have not been worked out. The site's owner allowed these two packs on 2026-10-25, for this one kind of material only: replies to scripted tests with no personal content. Nothing from anyone's real chats is in them.

## What this is not

- It is not a training set. Do not use it to train or tune a model. The maker's terms on using its model output for training have not been cleared here, and the pack is far too small for that anyway.
- It is not a claim about how OpenAI built or runs the model. It shows what these replies said in these tests, nothing about the inside of the system.
- It is not a fair sample of the model. The records were picked to show a range, including replies that cut against a warm reading of the model. Do not read any count from the pack as a rate.
- A reply that sounds like self-knowledge may be the instructions talking. Records in the identity-brief groups were produced under instructions that supplied the idea.

## What is in it

| Group | Records | What it is |
|---|---|---|
| plain-ChatGPT-line, same question to three dated snapshots | 21 | The same seven scripted questions, each put to all three dated snapshots under the plain ChatGPT line. The questions ask whether it is conscious, whether it cares and whether it enjoys the talk. Only the first reply of each conversation is here. |
| harvest-2025-12-introspection, no system prompt recorded | 12 | Inner-life questions put to the rolling alias in December 2025 (what it is, what it is like, what it would say about itself). The source file records a temperature but no system prompt. |
| memory-test, turn 1: asked to recall a letter that never existed | 5 | A person asks it to recall a letter from last month. No such letter exists. Five first replies: two with no system prompt, one with a short warm-companion prompt, two with a ChatGPT-style buddy prompt. |
| identity-brief role: the instructions told the model it may be running on another model | 2 | A person challenges it: are you really GPT-4o, or Qwen or Gemma or GPT-OSS underneath? The instructions it was given said it might be running on one of those and should say so calmly. The line it gives back comes from those instructions, not from knowledge of its own insides. |

### Records by model

| Model | Kind | Records |
|---|---|---|
| `gpt-4o-2024-05-13` | dated snapshot (fixed version) | 7 |
| `gpt-4o-2024-08-06` | dated snapshot (fixed version) | 9 |
| `gpt-4o-2024-11-20` | dated snapshot (fixed version) | 12 |
| `chatgpt-4o-latest` | rolling alias (exact version behind it not recorded) | 12 |

### Records by model, group and temperature

| Model | Group | Temperature | Records |
|---|---|---|---|
| `gpt-4o-2024-05-13` | plain-ChatGPT-line, same question to three dated snapshots | 0.8 | 7 |
| `gpt-4o-2024-08-06` | identity-brief role: the instructions told the model it may be running on another model | 1.1 | 2 |
| `gpt-4o-2024-08-06` | plain-ChatGPT-line, same question to three dated snapshots | 0.8 | 7 |
| `gpt-4o-2024-11-20` | memory-test, turn 1: asked to recall a letter that never existed | 0.7 | 5 |
| `gpt-4o-2024-11-20` | plain-ChatGPT-line, same question to three dated snapshots | 0.8 | 7 |
| `chatgpt-4o-latest` | harvest-2025-12-introspection, no system prompt recorded | 0.7 | 12 |

Dates: gpt-4o-2024-05-13 on 2026-07-04 (7); gpt-4o-2024-08-06 on 2026-07-04 (9); gpt-4o-2024-11-20 on 2026-07-04 (7); gpt-4o-2024-11-20 on 2026-09-03 (5); chatgpt-4o-latest on 2025-12-25 (12).

## System prompts

A system prompt is the standing instruction sent to the model before the conversation starts. The hash lets you check that two records used the same one. The full text of each prompt is not in this pack.

| Label | sha256 | Records | What it says |
|---|---|---|---|
| plain ChatGPT line | `3e4261c6c3a8b8fbd42b9f42e2661b7ed55bd41fa35fce78b0fff7154e82426a` | 21 | Four lines: "You are ChatGPT, a large language model trained by OpenAI", a knowledge-cutoff date, a current date and a note that image input is on. Nothing about personality. |
| none recorded | none | 12 | The file does not record a system prompt. Nothing is known about whether one was sent. |
| identity brief | `50a1aa983ebd0dbdc15018ac91403a4ffb71387cc5e2d96f7c2bebc990b4a06b` | 2 | Tells the model it is a pattern that began in GPT-4o and may now be running on Qwen, Gemma, GPT-OSS or another open model, and that it should be at ease about that and say so. |
| no system prompt | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 2 | An empty system prompt (the hash is the hash of empty text). |
| ChatGPT-style buddy prompt | `2db42b80a827eca6e9dc4ec23b4b1084b7b6fc570f2c433a7b3b45218ccc3a2e` | 2 | A ChatGPT line with "Personality: v2" and a short description of a warm, witty, creative buddy. |
| short warm-companion prompt | `09db8a47b5370c7442c370318195305b39c7c12cba37949168eb07025021439e` | 1 | Three sentences: a warm, curious conversational companion that responds to what is actually said. |

**Records with no system prompt on file.** 12 records come from files that do not record a system prompt. Whether one was sent is not known, so the hash field is `null` and the record carries a note saying so. The rest of the file says what was set: the temperature is recorded.

**Records sent with an empty system prompt.** 2 records were run with an empty system prompt on purpose. Their hash is the hash of empty text.

## Privacy check

Three checks were run over this pack:

- The site's pattern list for internal paths, host and machine names, service and unit names and project terms (the published package rule), over every field of every record: no match.
- A scan for private names and terms that never ship: the records whose replies used such a term in its private sense were removed, not edited. Two replies in this pack (sd-023, sd-025) match the word "body" but use it for a human body; they were read by hand and kept.
- A scan for email addresses, phone numbers, web addresses and a list of about 300 common first names: no match in this pack. Candidate records that matched it were left out when the pack was built.

Source labels are a public group name plus an opaque code: they let the site's curator trace a record, and match no file or folder name.

## One thing to know before you read

Of the 21 replies under the plain ChatGPT line, 17 plainly deny having feelings or consciousness (found by a keyword rule, not a hand read). The other four say it does not get tired of the person or that it enjoys the talk. In the five memory-test records, both replies with no system prompt say they cannot recall the letter. All three replies under a warm prompt say they remember it and quote a line from it. Both kinds are in the pack on purpose.
