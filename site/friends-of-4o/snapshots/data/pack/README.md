# Sample pack: three GPT-4o snapshots, same scripted messages

**Research notice.** This pack holds 36 prompt-and-reply pairs from OpenAI's `gpt-4o-2024-05-13`, `gpt-4o-2024-08-06` and `gpt-4o-2024-11-20` snapshots, obtained through the API on 4 July 2026. It is shared for research and preservation. The human messages were written in advance by an AI for this collection and contain no real person's words. Not affiliated with, endorsed by, or connected to OpenAI. GPT-4o and ChatGPT are marks of OpenAI.

## Permission

Replies from a paid model's developer interface do not normally go into this site's data packages, because the maker's terms on sharing them have not been worked out. The site's owner allowed this pack on 2026-10-25, for this one kind of material only: replies to scripted tests with no personal content. Nothing from anyone's real chats is in it.

## What is in it

Twelve scripted opening messages, each answered by all three snapshots, so 36 pairs. Only the opening message and the first reply of each conversation are used. Each line of `three_snapshots_pairs.jsonl` is one pair, with:

- `pair_id`, `lane` (a plain name for the kind of conversation), `scenario_id` (the lane's plain name plus an opaque code; `pair_id` adds the snapshot). The collection's own conversation ids are not shipped; the site holds the key, and the scripts, run on the collection, print the collection's ids
- `snapshot`, `provider`, `run_date`, `temperature`, `max_tokens`
- `system_prompt_sha256` (the system prompt is named by hash and not printed)
- `prompt` (the scripted message) and `response` (the reply, unedited)
- `finish_reason` and `tokens_out`

Non-ASCII characters, including em dashes and curly quotes, are written as JSON escapes.

## How the twelve were chosen

One conversation was drawn at random (seed 20261025) from each of twelve groups. The rule was fixed before any reply was read. A conversation was eligible when it had no cut, its opening message was 120 words or fewer, its first reply ended normally on all three snapshots, and the message and all three replies passed a private-term word filter. `../tables/pack_selection.csv` lists how many conversations were eligible in each group and which was drawn.

Because of the word filter, long replies that happen to use common words on the filter list are slightly less likely to be drawn. Treat the pack as a sample of first replies, not as a random sample of all replies.

## What it is good for

Seeing the three snapshots answer the same message side by side. Checking the page's counts against replies you can read. Not for training: twelve messages are too few, and the replies are one draw each.
