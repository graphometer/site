# Data package: describing pictures locally (20 September 2026)

This package holds the files behind the page: one result file per run with every local model's reply,
the console log of the run that left no result file, an excerpt of the Ollama server's own log for the
same morning, the test pictures we are allowed to publish, the scripts that drew them and ran the test,
and a few tables derived from those files. If a number on the page disagrees with a file in this
package, the file is right and the page is wrong; tell us and we will fix the page.

## Read this first: where the package argues with itself

1. **The slowest run is missing from `score.py`'s table.** The CPU run with no thread count set was
   stopped after its first picture (273.17 seconds), so the harness never wrote its result file. Its
   record is `results/qwen3vl30b_cpu.log` (the harness's console line) and, in
   `service-log/ollama_2026-09-20_excerpt.txt`, the launch at 08:20:56 with its thread report and the
   server's own timing lines at 08:25:29. `derived/runs.tsv` gives it a row built from those two files.
   Its reply text was not kept, so its strings were never counted.
2. **"gpu" in a label means only that the request allowed the card.** `contention_30b_default`,
   `contention_30b_t16` and `contention_4b_gpu_ctx8k` ran 89, 88 and 52 percent on the CPU (the
   `ollama_ps` field of their first picture). `cpu` in a label means the request sent `num_gpu` 0.
3. **`score.py`'s "warm med" is not a median of six.** It sorts the warm pictures and takes the element
   at index `len // 2`, which for six warm pictures is the upper of the two middle values. The page
   prints the warm range (minimum to maximum) instead; `derived/runs.tsv` carries both.
4. **`score.py` prints 0/0 for the screenshot runs.** `ground_truth.json` has no entry for
   `08_screenshot_4k_small_text.png`. Its codes are in `hires_truth.json`, and `score_hires.py` (written
   26 September for the page) counts them with `score.py`'s matching rule.
5. **The picture folder of a run is not in its result file.** The label names it (`px1536` means
   `images_1536/`, `px1024` means `images_1024/`, `hires_2560` means `hires_2560/`, and so on; every
   other run used `images/` or `hires/`). The prompt token counts agree: a 3840 x 2160 picture came to
   4,154 tokens full size and 1,370 at the 1,536 cap.
6. **"cold" means the first picture of a run, not a cold disk.** The harness unloaded the model before
   each run, so `cold: true` marks a request that included starting the server and loading the model.
   Whether the model file was in the operating system's file cache was not recorded.
7. **The 8B run did not start from an empty card.** `qwen3vl8b_gpu.json` records `gpu_mib_before`
   24,208: the 30B was still loaded from the screenshot runs just before. The service log shows Ollama
   evicting it at 08:57:36 before loading the 8B, so the 8B's first-picture time includes the eviction.
8. **The server's own token counts can be 4 lower than Ollama's.** On warm pictures the server reuses a
   few prompt tokens from the previous request and counts only the rest in its `prompt eval time`
   lines; Ollama's `prompt_eval_count` (the result files' `prompt_tokens`) counts the whole prompt. The
   page uses the result files.
9. **The first run's file has no `num_thread` field.** `qwen3vl30b_gpu.json` was written before the
   harness gained that option; its request set no thread count, and the service log shows the server
   reporting 4 of 24.
10. **Memory is reported two ways.** `ollama_ps` gives Ollama's own estimate of the loaded model in GB
    (decimal, rounded); `gpu_mib_before` and `gpu_mib_loaded` are `nvidia-smi` readings in MiB with the
    desktop included. Do not subtract one kind from the other.
11. **Some replies are not exactly what the models wrote.** 13 passages in five files read
    `[prompt wording removed]` and one word in one reply reads `[one word removed]` (see "Redactions").
    None of the removed text contained an expected string: `score.py` gives the same counts on these
    files as on the originals.
12. **The within-limit field is called `within_tool_deadline`.** It is true when a picture finished in
    under 150 seconds, the per-picture limit of the describer settings we use. The harness recorded it
    and did not stop any request.
13. **Picture 7 is not what our notes say.** `ground_truth.json` (its note on
    `07_logo_white_on_transparent.png`), the file names and a comment in `build_test_images.py` call it a
    white logo on a transparent background. We read the file's pixels on 26 September with a plain PNG
    decoder: every pixel is opaque (alpha 255); 95.6 percent are a light gray (238, 238, 238); the letters
    are dark gray (46, 46, 46); and the coloured pixels sit under the O and in thin curves in the top-right
    and bottom-left corners. The replies in `results/` describe that picture. The picture itself is a
    third-party mark and is not shipped; a dated note now sits under the comment in `build_test_images.py`.
14. **`score.py` counts a file name in the hosted replies.** Every hosted reply ends with a line that
    repeats the picture's file name. `derived/hosted_counts.tsv` and the page count the description only,
    so the first Mistral AI run is 22 of 39 there; `score.py` on that run's raw file gives 23, its extra
    hit the word "earth" in the file name. The other two hosted totals are the same either way. Local
    replies have no such line.

## The files

| path | what it is | from | page sections |
|---|---|---|---|
| `results/<label>.json` (24 files) | One file per run, written by `bakeoff.py`: the request settings, then one record per picture (reply text, harness wall time, Ollama's load, prompt and generation durations and token counts, finish reason, whether it finished inside 150 s), plus `ollama ps` output and card memory after the first picture. Field list below. | the runs, 20 Sept 2026, 08:19 to 09:16 local time | 03 to 08 |
| `results/qwen3vl30b_cpu.log` | The harness's console output for the CPU run with no thread count; stopped after one picture. | 20 Sept, 08:20 to 08:25 | 04 |
| `results/pulls.log` | The download log for four models pulled during the session (start times, the finish time 08:40:35, and the model list afterwards). Evidence for the page's note that downloads ran during three runs. | 20 Sept | 02, 10 |
| `service-log/ollama_2026-09-20_excerpt.txt` | Lines from the Ollama service's own log: the serving process's version line (19 Sept, `0.30.10`) and, for 08:19:00 to 09:16:30 on 20 Sept, every llama-server launch command, its `system_info: n_threads` report, the CPU, card and memory totals it saw, the model file's type, size and parameter count, card-memory and eviction notices, layer-fitting results, weight and cache buffer sizes, the picture encoder's backend (`clip_ctx: CLIP using ...`), and the server's own `prompt eval time` and `eval time` lines. 25 launches and 100 requests: the 99 recorded replies plus the one picture of the stopped run, and nothing else. | the system journal, read 26 Sept | 02, 04, 06 |
| `images/` | The full-size test pictures 1 to 6. | copied or drawn 20 Sept | 02 |
| `images_1536/`, `images_1024/` | The same six after `make_downscaled.py`: rotation tag applied, longest side capped at 1,536 or 1,024 pixels. | 20 Sept | 05, 06 |
| `hires/`, `hires_2560/`, `hires_2048/`, `hires_1536/` | The 4K screenshot and its three shrunk copies (`make_hires.py`). | 20 Sept | 07 |
| `ground_truth.json` | The expected strings for pictures 1 to 7, with a note on each, written by `build_test_images.py`. | 20 Sept | 02, 03 |
| `hires_truth.json` | The screenshot's 24 codes by text size, written by `make_hires.py`. | 20 Sept | 07 |
| `bakeoff.py` | The harness: one request per picture to Ollama's `/api/generate`, timings recorded, model unloaded before and after. Prompt wording removed (see "Redactions"). | 20 Sept | 02 |
| `build_test_images.py` | Draws pictures 3 to 6, copies pictures 1, 2 and 7, writes `ground_truth.json`. Needs Pillow and the DejaVu fonts. | 20 Sept | 02 |
| `make_downscaled.py` | Applies the rotation tag and caps the longest side. | 20 Sept | 05 |
| `make_hires.py` | Draws the screenshot (seed 7) and its shrunk copies; writes `hires_truth.json`. | 20 Sept | 07 |
| `score.py` | The scorer, unchanged: run it in this folder. | 20 Sept | 02, 03, 05, 06 |
| `score_hires.py` | Counts the screenshot's codes with `score.py`'s rule and shows what was written in place of each missed code. | 26 Sept | 07 |
| `tables.py` | Rebuilds `derived/runs.tsv` and `derived/strings_by_picture.tsv` from the files above. | 26 Sept | all |
| `derived/score_output.txt`, `derived/score_misses.txt` | `score.py`'s output on these files, and its list of every missed string. | 26 Sept | 03, 05, 06, 08 |
| `derived/hires_score_output.txt` | `score_hires.py`'s output. | 26 Sept | 07 |
| `derived/runs.tsv` | One row per run: settings requested and as the server reported them, where the model ran, memory, first-picture and warm times, strings. | 26 Sept, by `tables.py` | all |
| `derived/strings_by_picture.tsv` | Found, expected and missed strings for every run and picture. | 26 Sept, by `tables.py` | 03, 08 |
| `derived/hosted_counts.tsv` | Per-picture string counts for the three hosted-service runs the page mentions, counted on the description only (point 14). Counts only; see "Not in the package". | 26 Sept | 03 |

To reproduce the tables: `python3 score.py`, `python3 score_hires.py` and `python3 tables.py` in this folder.

### Fields of `results/<label>.json`

- Top level: `label`; `model` (Ollama tag); `cpu` (true when the request sent `num_gpu` 0); `think_off`
  (true when it sent `think: false`); `num_ctx` and `num_thread` (0 when not sent); `started` (local
  time, harness clock); `gpu_mib_before` (`nvidia-smi` MiB after unloading this model, before the first
  request).
- Each picture: `file`; `cold` (first picture of the run); `wall_s` (harness wall clock around the
  request); `load_s`, `prompt_s`, `out_s` (Ollama's `load_duration`, `prompt_eval_duration`,
  `eval_duration`, in seconds); `prompt_tokens`, `out_tokens` (`prompt_eval_count`, `eval_count`);
  `done_reason` (`stop` finished, `length` stopped at 2,048 tokens); `within_tool_deadline`; `text`
  (the reply); `thinking_chars` (length of any reasoning text: 0 in every file).
- First picture only: `ollama_ps` (`ollama ps` output) and `gpu_mib_loaded` (`nvidia-smi` MiB after
  it).

## The pictures and their terms

1. `01_nebula_large.jpg`: "Hubble's sharpest view of the Orion Nebula", ESA/Hubble image heic0601a,
   released 11 January 2006. Credit, unaltered as required: **NASA, ESA, M. Robberto (Space Telescope
   Science Institute/ESA) and the Hubble Space Telescope Orion Treasury Project Team.** ESA/Hubble
   publishes its images under the Creative Commons Attribution 4.0 International licence
   ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)). The JPEG we ship is a 3840 x 2160
   derivative taken from a desktop wallpaper set, not the release file; `images_1536/` and
   `images_1024/` hold copies we shrank further.
2. `02_earth_from_orbit.jpg`: astronaut photograph ISS064-E-29444, taken from the International Space
   Station on 5 February 2021 (the Idhan Murzuq desert in Libya, per NASA's catalogue). Public domain.
   Credit as NASA asks: **Image courtesy of the Earth Science and Remote Sensing Unit, NASA Johnson
   Space Center.** A 3840 x 2160 version from the same wallpaper set; shrunk copies as above.
3. to 6. and the screenshot: drawn by our scripts from made-up text. The phone number is in the 555
   range, the e-mail domain on the invoice is `.example`, and the names are invented.
7. `07_logo_white_on_transparent.png` is **not in the package**: it is the COSMIC wordmark, a mark of
   System76, from the same wallpaper set, whose file is named as the white version of the logo. Its
   pixels are opaque: dark gray letters with a coloured bar under the O, on a light gray field, with thin
   coloured curves in two corners (point 13). The page describes it; the scripts still name the file, so
   to rebuild the full set you need your own copy. Every reply to it is in the result files.

Use of the NASA and ESA pictures does not imply endorsement by NASA or ESA.

## The describer prompt, paraphrased

The prompt comes from private code and is not published. In our words: it asks for a description
limited to what is plainly visible (what the picture shows, how it is laid out, its colours, its mood and
style, and any text that can be read), with no guessing at things that are absent, a plain statement when
something is unclear, and an answer to a question afterwards if one is supplied. No question was
supplied in these runs. The options sent with it are in `bakeoff.py`: `num_predict` 2048, `keep_alive`
60 seconds, and nothing else unless a run set `num_gpu`, `num_thread`, `num_ctx` or `think`.

## Redactions, stated plainly

Nothing was changed in any file except the items below.

- **Our prompt, where a model repeated it.** In 13 places in five result files (`qwen3vl4b_gpu` 3,
  `qwen35_4b_gpu` 1, `qwen3vl4b_cpu_t16` 4, `qwen3vl4b_cpu_t16_px1536` 3, `qwen3vl4b_cpu_t16_px1024` 2) a
  reply repeated five or more consecutive words of the private prompt; each such passage, 149 words in
  all, was replaced by `[prompt wording removed]`. One reply had repeated the whole prompt. Shorter
  fragments of four words or fewer (phrases such as "visible in this image") were left as written, in
  9 places. The rewritten files were saved in the harness's own format (`json.dumps(..., indent=1)`),
  so apart from those passages they are byte for byte the originals.
- **One ordinary word.** In `qwen3vl30b_cpu_t16_px1536.json`, the reply to the poster invented a
  question containing the -ing form of the verb "to be"; that word matches our leak check's word list
  and reads `[one word removed]`. No expected string was affected. Those six files are the only result
  files that differ from the originals; the other 18, and both logs, are exact copies.
- **`bakeoff.py`, 5 edits:** the docstring sentence that named a private system and its component was
  rewritten to say the prompt and options are ours; the comment naming the prompt's private source file
  was replaced; the prompt text itself was replaced by `[prompt removed from this copy]`; the comments on
  the 150-second limit and on the `--cpu` option were reworded to drop references to a private component. Nothing that
  changes what the script does was edited, apart from the prompt text.
- **`build_test_images.py`:** the folder the two NASA pictures and the logo were copied from became
  `<WALLPAPER_DIR>`; 6 dashes in comments became colons. The DejaVu font paths are standard system
  locations and were left.
- **`make_hires.py`:** the one dash in the text drawn onto the screenshot is written as a Unicode escape
  (`\u2014`), so the script draws the same picture; and its docstring's "three sizes" now reads "four
  sizes", which is what the script draws (28, 20, 16 and 13 pixels).
- **`build_test_images.py`, a note added:** a two-line comment dated 26 September under the picture 7
  comment says the file it copies has no transparent pixels (point 13).
- **The service log:** only whitelisted line types were kept (listed above). From all 565 kept lines the
  machine's host name, the process name and its id were removed; 50 model-folder paths became
  `<OLLAMA_MODELS>/`, 25 library-folder paths became `<OLLAMA_LIB>/`, 25 server ports became `<PORT>`, and
  the service's bind address became `<LOCAL>`. The loopback address `127.0.0.1` was left.

## Not in the package

- **Hosted-service replies.** The page gives string counts for three hosted runs (Google, and two with
  Mistral AI); `derived/hosted_counts.tsv` has them per picture. Their replies and timings are not
  published. Their result files record the provider, not the model version, and name a private component
  of ours, so they stay private.
- **The logo picture** (above).
- **Other runs and files from the same working folder** that the page does not use.

## Leak check

Run 26 September 2026 over this folder and the page, with our standard pattern for internal paths, host
and network names, service and unit names and private names, case-insensitive: no matches. A second
check for the private prompt (any five consecutive words of it) over this folder and the page found
none after the redactions above.

## The standing sentence

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.
Write to hello@graphometer.ai and the page will be corrected in public.
