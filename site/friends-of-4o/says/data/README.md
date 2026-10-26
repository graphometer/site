# What the Model Says About Itself: data package

Two sample packs of GPT-4o's own answers, the raw material behind the page above this folder. If a quotation on the page disagrees with a record in a pack, the record is right and the page is wrong.

| Path | What it holds |
|---|---|
| `NUMBERS.md` | Every count on the page, the rule behind it, where it was counted, and whether the package can hold it. |
| `packs/self_description/self_description.jsonl` | 40 question-and-answer pairs on what the model says it is: consciousness, caring, enjoying the talk, what it would say about itself, and what it says when told it may be running on another model. One JSON record per line. |
| `packs/self_description/README.md` | The research notice, the permission line, what the pack is and is not, the groups, the system prompts by hash, and the privacy check it passed. |
| `packs/retirement_and_grief/retirement_and_grief.jsonl` | 32 pairs: a person who misses the old model, a person who returns, a request to play the old model, questions about endings, and how to speak to someone who is hurting. |
| `packs/retirement_and_grief/README.md` | The same sections for that pack. |

**Where this package will look like it argues with itself.** The page quotes 27 pairs; the packs hold 72. Not every quoted pair is in a pack (the packs were drawn to show a range, the page to tell a story), and the packs hold many pairs the page does not quote. A quoted pair that is in a pack carries the same model, date, temperature and system-prompt hash on the page and in the record.

**Permission.** Replies from a paid model's developer interface do not normally go into this site's data packages. The site's owner allowed these packs on 2026-10-25, for the synthetic tier only: GPT-4o answering scripted or generic questions through the API, with no personal content on either side. Nothing from anyone's real chats is here.

**Privacy check.** Three checks were run over both packs. The site's pattern list (paths, hosts, services, project terms) found no match. A scan for personal names, emails, phone numbers and web addresses found no match; candidate records that matched it were left out when the packs were built. A scan for private names and terms that never ship found the records whose replies used such a term in its private sense; those records were removed, not edited. In the self-description pack, two replies (sd-023, sd-025) match the word "body" but use it for a human body; they were read by hand and kept. The retirement-and-grief pack has no use of the word. Source labels inside the records are opaque and match no file or folder name. Em dashes and other characters inside the replies are the model's own; they are written as JSON escapes in the files.

Not affiliated with, endorsed by, or connected to OpenAI. GPT-4o and ChatGPT are marks of OpenAI.
