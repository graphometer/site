# NUMBERS: every figure on the page, with its file and field

If a number on the page disagrees with a file in this package, the file is right and the page is wrong.

**The one place a file will look like it contradicts the page:** `derived/score_output.txt` (the output
of `score.py`) has no row for the page's slowest run, 273.17 seconds with 4 threads, and its "warm med"
column differs from the page's warm ranges. The 4-thread run left no result file (README, point 1; its
figures are in `results/qwen3vl30b_cpu.log` and the service log), and "warm med" is the upper middle
value of six (README, point 3), while the page prints the minimum and maximum of the warm pictures.
And `ground_truth.json`'s note calls picture 7 a white wordmark on full transparency, which the page
corrects: the file's pixels are all opaque (README, point 13).

Paths are relative to `data/`. `R/<label>` means `results/<label>.json`; `first` is its first picture
(`runs[0]`), `warm` the rest. `SL` is `service-log/ollama_2026-09-20_excerpt.txt`, with the line's time.
Times on the page are the result files' `wall_s` (total), `load_s`, `prompt_s` (reading) and `out_s`
(writing). All figures are measured unless marked **arithmetic**.

## Title spots, subtitle, eyebrow, description

| figure | file and field |
|---|---|
| 39 known strings; all 39 on the card for Qwen3-VL 30B-A3B | `ground_truth.json` (2+1+10+13+9+3+1 = 39 expected strings, **arithmetic**); `R/qwen3vl30b_gpu`, 39 of 39 in `derived/score_output.txt` |
| Qwen3-VL 30B-A3B, 1.3 to 3.2 seconds a warm picture (in the visible subtitle and in the Open Graph and Twitter descriptions; the title, image alt, feed title and card headings are the short title and carry no figure) | `R/qwen3vl30b_gpu` warm `wall_s`: minimum 1.31 (cottage), maximum 3.16 (earth); the two other 39-of-39 models ran to 3.47 and 3.82, so the range is this model's only |
| 273 seconds at Ollama's default 4 threads | `results/qwen3vl30b_cpu.log`: `COLD wall=273.17s`; threads: SL 08:20:56 `system_info: n_threads = 4 (n_threads_batch = 4) / 24`, launch line at 08:20:56 without `-t` |
| 111 at 16 | `R/qwen3vl30b_cpu_t16` first `wall_s` 111.01; SL 08:26:08 `n_threads = 16` |
| 38.5 at 16 with a 1,536-pixel cap | `R/qwen3vl30b_cpu_t16_px1536` first `wall_s` 38.52 (picture from `images_1536/`, README point 5) |
| 20 September 2026 | `started` in every `R/*` (2026-09-20) |
| RTX 5090, 32 GB card; 188 GiB RAM; 24-core CPU | SL 08:19:42: `- CUDA0 : NVIDIA GeForce RTX 5090`, `msg="system memory" total="188.1 GiB"`, `- CPU : Intel(R) Core(TM) Ultra 9 285K`, and `system_info ... / 24` (the 24 CPU threads the server saw); `/l3-threads/` records the 285K's 8 + 16 cores |
| Ollama 0.30.10 | SL first line, 2026-09-19 06:34:57: `Listening on <LOCAL>:11434 (version 0.30.10)`; one serving process covers every line after it (README, service-log row) |
| six Qwen vision models, seven test pictures and one screenshot, one run per configuration | the six `model` tags in `R/*`; `images/` (six shipped, the seventh described in README); `hires/`; one file per configuration |
| description: 1.31 to 3.16; 273.17; 242.93; 111.01; 38.52; 26,396 MiB; 89/11; 206.87; 39.39; 4 of 24 codes | the rows below |

## Lead

| figure | file and field |
|---|---|
| a reply of at most 2,048 tokens | `bakeoff.py`: `"options": {"num_predict": 2048}` |
| 150 seconds per picture | `bakeoff.py`: `TOOL_DEADLINE_S = 150.0`; `within_tool_deadline` in `R/*` |
| seven pictures, 39 strings | `ground_truth.json` |
| Qwen3-VL 30B-A3B, Qwen3-VL 8B and Qwen3.6 35B-A3B found all 39 | `derived/score_output.txt` rows `qwen3vl30b_gpu`, `qwen3vl8b_gpu`, `qwen36_35b_gpu`: 39/39 |
| 1.3 to 3.8 seconds once loaded | warm `wall_s`: minimum 1.31 (`R/qwen3vl30b_gpu`), maximum 3.82 (`R/qwen3vl8b_gpu`, earth) |
| 4 threads out of 24 | SL 08:20:56 `system_info: n_threads = 4 (n_threads_batch = 4) / 24` |
| 273 seconds, 243 of them reading | `results/qwen3vl30b_cpu.log`: `wall=273.17s`, `img+prompt=4154tok/242.93s`; SL 08:25:29 `prompt eval time = 242931.43 ms / 4154 tokens` |
| 111 seconds at 16 threads | `R/qwen3vl30b_cpu_t16` first `wall_s` 111.01 |
| 38.5 with the 1,536 cap; that run found all 39 | `R/qwen3vl30b_cpu_t16_px1536` first `wall_s` 38.52; 39/39 in `derived/score_output.txt` |
| 26,396 MiB already in use | `R/contention_30b_default` `gpu_mib_before` |
| 11 percent of the model on the card | `R/contention_30b_default` first `ollama_ps`: `89%/11% CPU/GPU` |
| 207 seconds, past the 150-second limit | same file, first `wall_s` 206.87, `within_tool_deadline` false |
| 39.4, added nothing to the card | `R/contention_30b_cpu_t16_px1536` first `wall_s` 39.39; `gpu_mib_before` 26,405, `gpu_mib_loaded` 26,391 |
| its launch: 16 threads, an 8,192-token window, the cap; also a larger batch and memory mapping off | SL launch lines 09:02:40 (`-c 32768 ... -b 512 -ub 512`, no `-t`, no `--no-mmap`) and 09:09:39 (`-c 8192 ... --no-mmap ... -b 1024 -ub 1024 -ngl 0 -t 16`); the cap from the label and `prompt_tokens` 1,370 |
| misread 4 of 24 codes at 1,536 pixels and none uncapped; every miss a wrong code | `derived/hires_score_output.txt` (from `score_hires.py`): `hires_30b_hires_1536` 20/24, `hires_30b_hires` 24/24, and the four "written" lines |

## 01 What it is

| figure | file and field |
|---|---|
| 3840 x 2160 picture: 4,154 prompt tokens with the Qwen3-VL models | `R/qwen3vl30b_gpu`, `R/qwen3vl8b_gpu`, `R/qwen3vl4b_gpu` `prompt_tokens` for `01_`, `02_`, `07_` |
| 1,974 for a 1200 x 1600 poster | same files, `03_poster_text.png` `prompt_tokens` |
| 4.3 to 23 GB of memory | first `ollama_ps` of `R/qwen35_4b_gpu` (4.3 GB) and `R/qwen36_35b_gpu` (23 GB) |

## 02 What we ran

| figure | file and field |
|---|---|
| Core Ultra 9 285K, 24 cores (8 + 16), no hyperthreading | SL `- CPU : Intel(R) Core(TM) Ultra 9 285K` at each load and the server's `/ 24` in `system_info`; the core split as `/l3-threads/` records |
| 08:19 to 09:16 local time | earliest `started` 2026-09-20 08:19:41 (`R/qwen3vl30b_gpu`); last run `R/qwen3vl30b_gpu_t16_ctx8k` started 09:15:40 and its last picture ends about 20.7 s later (sum of its `wall_s`, **arithmetic**) |
| 19 September (the version line) | SL first line |
| 32,768-token window unless the request set one | SL launch lines: `-c 32768` at the 19 launches whose request set no `num_ctx`, `-c 8192` at the six that set 8192 |
| every Qwen3-VL launch asked for at least 1,024 image tokens (`--image-min-tokens 1024`); the Qwen3.5 4B, Qwen3.5 9B and Qwen3.6 launches did not | SL launch lines: the flag is on the 22 Qwen3-VL launches and absent from those at 08:35:32 (Qwen3.6, `model params = 35.51 B`), 08:58:07 (Qwen3.5 4B, `4.33 B`) and 08:58:52 (Qwen3.5 9B, `9.20 B`) |
| `num_predict` 2048, `keep_alive` 60 s, no sampling options | `bakeoff.py`, the `payload` dictionary |
| 150 seconds | `bakeoff.py` `TOOL_DEADLINE_S` |
| first card load of the 30B 36.97 s; later card loads 4.56 to 4.86 | `R/qwen3vl30b_gpu` first `load_s` 36.97; later 30B loads on the card: `R/hires_30b_hires*` 4.84, 4.56, 4.75, 4.83, `R/ctx8k_qwen3-vl_30b-a3b-instruct` 4.86, `R/qwen3vl30b_gpu_t16_ctx8k` 4.79 |
| 39 = 34 pieces of text + 5 subject words | `ground_truth.json`: nebula, stars, earth, house, sun are the subject words; the other 34 are drawn text (**arithmetic**) |
| downloads from 08:35 to 08:40 | `results/pulls.log`: first pull 08:35:23, `PULLS DONE 08:40:35` |
| during the Qwen3.6 and 4B card runs and the first two minutes of the 4B's full-size CPU run | `started` of `R/qwen36_35b_gpu` 08:35:31, `R/qwen3vl4b_gpu` 08:37:43, `R/qwen3vl4b_cpu_t16` 08:38:22 (08:38:22 to 08:40:35 is 2 min 13 s, **arithmetic**) |
| two hosted runs finished during the default-thread CPU run | the hosted result files (not shipped) were written at 08:23:24 and 08:23:49; that CPU run launched at 08:20:56 (SL) and its picture ended at 08:25:29 (SL timing lines) |
| model table: Q4_K_M | SL `print_info: file type = Q4_K - Medium` at every load |
| parameters 30.53 B, 35.51 B, 8.19 B, 4.02 B, 9.20 B, 4.33 B | SL `print_info: model params` at the loads of 08:19:46 (30B), 08:35:36 (Qwen3.6), 08:57:39 (8B), 08:37:45 (4B), 08:58:54 (Qwen3.5 9B), 08:58:09 (Qwen3.5 4B) |
| the log calls the model type 30B.A3B (about 3B active per token by that name, not a figure from this page); 35B-A3B likewise | SL `print_info: model type = 30B.A3B` and `35B.A3B`; `model params = 30.53 B` and `35.51 B`. Nothing in these runs counts active parameters. |
| memory 22, 23, 10, 7.9, 6.7, 4.3 GB | first `ollama_ps` of `R/qwen3vl30b_gpu`, `R/qwen36_35b_gpu`, `R/qwen3vl8b_gpu`, `R/qwen3vl4b_gpu`, `R/qwen35_9b_gpu`, `R/qwen35_4b_gpu` (all `100% GPU`, context 32768) |
| picture sizes 3840 x 2160, 1200 x 1600, 1240 x 1754, 1400 x 900, 1200 x 900 | the files in `images/` (and `build_test_images.py`); picture 7's size from `ground_truth.json` `kind` and the file itself |
| picture 7: opaque; dark gray letters with a coloured bar under the O, a light gray field, thin coloured curves in two corners; "our notes called it a white logo on a transparent background" | the file is a third-party mark and is not in the package; its pixels were read on 26 September (every pixel alpha 255; 95.6% light gray 238, 238, 238; letters 46, 46, 46; coloured pixels under the O and in the top-right and bottom-left corners): README point 13. Our notes: `ground_truth.json` (note on `07_logo_white_on_transparent.png`) and the comment in `build_test_images.py` |
| strings per picture 2, 1, 10, 13, 9, 3, 1 | `ground_truth.json` `expect` lists |
| screenshot: 24 codes, text 28, 20, 16 and 13 pixels high | `hires_truth.json`; `make_hires.py` (`for size in (28, 20, 16, 13)`, the font size in pixels) |

## 03 Observed: six models on the card

| figure | file and field |
|---|---|
| 4 threads for each of these runs | SL `system_info` at 08:19:42, 08:35:32, 08:57:38, 08:37:44, 08:58:53, 08:58:07 |
| strings 39, 39, 39, 38, 37, 30 of 39 | `derived/score_output.txt` |
| first picture 41.69 (36.97); 39.60 (36.11); 8.85 (5.16); 8.74 (3.86); 9.12 (4.73); 6.63 (4.19) | first `wall_s` (`load_s`) of the six files |
| warm 1.31 to 3.16; 1.82 to 3.47; 1.81 to 3.82; 1.15 to 2.61; 2.14 to 4.49; 3.02 to 9.35 | warm `wall_s` minimum and maximum; also `derived/runs.tsv` `warm_min_s`, `warm_max_s` |
| card 1,077 → 24,755; 1,011 → 25,764; 24,208 → 13,348; 1,001 → 10,656; 1,139 → 9,537; 946 → 6,732 | `gpu_mib_before` → `gpu_mib_loaded` |
| eviction at 08:57:36 | SL 08:57:36 `llama-server model predicted to exceed available memory, evicting` |
| between 1.31 and 3.82 seconds | as the lead |
| 36.97 and 36.11 seconds; 3.86 to 5.16 | first `load_s` of the six files |
| the 4B's miss, "house"; "an arrow pointing leftward" | `derived/score_misses.txt`; `R/qwen3vl4b_gpu`, cottage `text` |
| the 9B's two misses; "£2/day", "12 months" | `derived/score_misses.txt`; `R/qwen35_9b_gpu`, invoice `text` |
| Qwen3.5 4B: four poster details, five of six chart values | `derived/score_misses.txt` (`27 Orchard Lane`, `$12`, `555-0147`, `Doreen`; `35`, `58`, `71`, `64`, `23`) |
| 1,562, 2,048 and 2,048 tokens | `R/qwen35_4b_gpu` `out_tokens` for the poster, earth and chart (`done_reason` `stop`, `length`, `length`) |
| 8,192 tokens; 4,158 + 2,048 = 6,206 | **arithmetic**: 4,158 is the largest `prompt_tokens` in any file (`R/qwen36_35b_gpu`, `R/qwen35_*`, 4K pictures); 2,048 is `num_predict` |
| 19 GB instead of 22; 4.2 GB instead of 7.9 | first `ollama_ps` of `R/ctx8k_qwen3-vl_30b-a3b-instruct` and `R/ctx8k_qwen3-vl_4b-instruct` (context 8192) against the full-window files above |
| 22,562 MiB (1,150 before); 7,343 (1,148 before) | `gpu_mib_loaded`, `gpu_mib_before` of the two `ctx8k_*` files |
| two pictures (the nebula and the invoice, 4 threads), 15 of their strings | the two `ctx8k_*` files: pictures `01_`, `04_`; SL 08:59:39 and 08:59:52 `n_threads = 4`; 15/15 in `derived/score_output.txt` |
| a later run at 8,192 with 16 threads: 39 strings, 1.23 to 2.95 s | `R/qwen3vl30b_gpu_t16_ctx8k` (started 09:15:40): 39/39; warm `wall_s` 1.23 to 2.95 |
| hosted: Google 39 of 39; Mistral AI 22 of 39 (2 of the invoice's 13); Mistral Medium 39 of 39; `score.py` gives the first Mistral run 23, its extra hit "earth" in the file name | `derived/hosted_counts.tsv` (description only: the closing line repeating the file name is dropped, README point 14); 23 is `score.py` on the raw hosted file, which is not shipped |

## 04 On the CPU, the thread count

| figure | file and field |
|---|---|
| 4,154 prompt tokens (nebula); 1,974 (poster) | `prompt_tokens` in the thread runs; `results/qwen3vl30b_cpu.log` `img+prompt=4154tok` |
| 4 of 24: 273.17, 12.60, 242.93; 174 tokens in 17.36 s | `results/qwen3vl30b_cpu.log`: `wall=273.17s load=12.6s img+prompt=4154tok/242.93s out=174tok`; SL 08:25:29 `eval time = 17363.53 ms / 174 tokens` |
| 8 of 24: 157.31, 12.62, 123.53, 303 in 20.89; poster 60.30, 40.14, 364 in 19.74 | `R/qwen3vl30b_cpu_t8`; SL 08:31:23 `n_threads = 8` |
| 16 of 24: 111.01, 13.13, 87.77, 193 in 9.85; poster 41.87, 29.57, 278 in 11.90 | `R/qwen3vl30b_cpu_t16`; SL 08:26:08 `n_threads = 16` |
| 24 of 24: 107.88, 14.56, 76.57, 208 in 16.47; poster 45.77, 26.55, 235 in 18.82 | `R/qwen3vl30b_cpu_t24`; SL 08:28:45 `n_threads = 24` |
| amber: over 150 s | `within_tool_deadline` false: `R/qwen3vl30b_cpu_t8` first; the 4-thread run's 273.17 is over 150 (**arithmetic**) |
| all 12 strings in two pictures | `derived/score_output.txt` rows `qwen3vl30b_cpu_t8`, `_t16`, `_t24`: 12/12 |
| no thread flag; `-t` 8, 16, 24 | SL launch lines at 08:20:56 (no `-t`), 08:31:23 (`-t 8`), 08:26:08 (`-t 16`), 08:28:45 (`-t 24`) |
| the card runs that set no thread count: 4 | SL `system_info` at every launch without `-t` |
| reading 17.1, 33.6, 47.3, 54.3 tokens a second | **arithmetic**: 4,154 / 242.93, / 123.53, / 87.77, / 76.57 (the server's own lines agree: SL `17.10 tokens per second` at 08:25:29) |
| writing 10.0, 14.5, 19.6, 12.6 (nebula) | 10.0: SL 08:25:29 `10.02 tokens per second`; the rest **arithmetic**: 303 / 20.89, 193 / 9.85, 208 / 16.47 |
| writing 18.4, 23.4, 12.5 (poster) | **arithmetic**: 364 / 19.74, 278 / 11.90, 235 / 18.82 |
| 24 threads 3.1 s faster on the nebula; 16 threads 3.9 s faster on the poster | **arithmetic**: 111.01 - 107.88 = 3.13; 45.77 - 41.87 = 3.90 |
| 8 performance and 16 efficiency cores | as `/l3-threads/` records |
| 4B at 16 threads: 95.69 (71.48); warm 23.07 to 80.80; 80.80 and 80.66; 38 of 39 | `R/qwen3vl4b_cpu_t16`: first `wall_s`, `prompt_s`; warm `wall_s` (earth 80.8, logo 80.66); 38/39 |
| downloads during its first two minutes | as section 02 |

## 05 On the CPU, the picture size

| figure | file and field |
|---|---|
| token table: 4,154 / 1,370 / 1,106; 1,974 / 1,802 / 1,110; 2,219 / 1,706 / 1,127; 1,306 / 1,306 / 1,114; 1,138 / 1,138 / 1,110 | `prompt_tokens` per picture in `R/qwen3vl4b_gpu` (full size), `R/qwen3vl4b_cpu_t16_px1536`, `R/qwen3vl4b_cpu_t16_px1024` (the 30B's files give the same full-size and 1,536 counts) |
| 3840 x 2160, 1200 x 1600, 1240 x 1754, 1400 x 900, 1200 x 900 stored | the files in `images/`; the capped sizes are in `images_1536/`, `images_1024/` |
| 1,106 to 1,127 at the 1,024 cap; that run's Qwen3-VL 4B launch carried `--image-min-tokens 1024` | `R/qwen3vl4b_cpu_t16_px1024` `prompt_tokens`; SL launch line 08:48:34 |
| Qwen3.5 and Qwen3.6 counted 4 more | `prompt_tokens` 4,158, 1,978, 2,223, 1,310, 1,142 in `R/qwen35_*` and `R/qwen36_35b_gpu` |
| 30B none: 111.01 (13.13, 87.77); poster 41.87; 12/12 | `R/qwen3vl30b_cpu_t16` |
| 30B 1,536: 38.52 (12.30, 18.17); warm 22.64 to 38.93; 39/39 | `R/qwen3vl30b_cpu_t16_px1536` |
| 4B none: 95.69 (5.50, 71.48); warm 23.07 to 80.80; 38/39 | `R/qwen3vl4b_cpu_t16` |
| 4B 1,536: 29.11 (6.73, 14.30); warm 19.83 to 39.36; 39/39 | `R/qwen3vl4b_cpu_t16_px1536` |
| 4B 1,024: 27.20 (5.24, 10.95); warm 18.12 to 32.64; 39/39 | `R/qwen3vl4b_cpu_t16_px1024` |
| reading 87.77 → 18.17; first picture 111.01 → 38.52 | `prompt_s` and `wall_s` of the two 30B files |
| 174.27 against 172.17 seconds for the six warm pictures together | **arithmetic**: sum of warm `wall_s` in `R/qwen3vl30b_cpu_t16_px1536` and `R/qwen3vl4b_cpu_t16_px1536` |
| the log calls the 30B's model type 30B.A3B; about 3B parameters per token by that name, not a measurement here | SL `model type = 30B.A3B` |
| 22 GB against the 4B's 8.0 | first `ollama_ps` of `R/qwen3vl30b_cpu_t16_px1536` (`22 GB 100% CPU 32768`) and `R/qwen3vl4b_cpu_t16_px1536` (`8.0 GB 100% CPU 32768`) |
| the 4B's only full-size miss was "house" on the cottage; at the 1,536 cap the cottage was turned upright and not shrunk (1,138 prompt tokens both ways) and that reply contains "house"; one run each | `derived/score_misses.txt` (`qwen3vl4b_cpu_t16`); `R/qwen3vl4b_cpu_t16` and `R/qwen3vl4b_cpu_t16_px1536` cottage `prompt_tokens` 1138 and `text`; `derived/strings_by_picture.tsv` (3 of 3 capped) |
| screenshot read on the card in 1.85 s uncapped, 0.49 at 1,536 | `R/hires_30b_hires` and `R/hires_30b_hires_1536` first `prompt_s` |

## 06 With the card mostly full

| figure | file and field |
|---|---|
| 26,390 to 26,405 MiB | `gpu_mib_before` of the four `R/contention_*` files |
| 5.1 GiB free | SL `msg="gpu memory" ... free="5.1 GiB"` at 09:02:40, 09:07:39, 09:11:06 |
| where it ran: 89/11, 88/12, 100% CPU, 52/48 | first `ollama_ps` of `R/contention_30b_default`, `_30b_t16`, `_30b_cpu_t16_px1536`, `_4b_gpu_ctx8k` |
| batch 512, 512, 1,024, 512; `--no-mmap` on the CPU-only launch only | SL launch lines 09:02:40, 09:07:39, 09:09:39, 09:11:06 (`-b` and `-ub`; `--no-mmap` only at 09:09:39) |
| the fall from 206.87 to 39.39 s is threads, window, batch, memory mapping, placement and the cap together | the two launch lines above; the two result files |
| threads 4, 16, 16, 16 | SL `system_info` at 09:02:40, 09:07:39, 09:09:39, 09:11:06 |
| windows 32,768 and 8,192 | `num_ctx` in the files (0 means not set); SL launch `-c` |
| cap: none, none, 1,536, none | labels (README point 5); `prompt_tokens` 4,154 or 1,370 on the nebula |
| 206.87 (180.68); 74.91 (54.52) | `R/contention_30b_default` first and second `wall_s` (`prompt_s`) |
| 85.45 (65.20); 31.02 (21.29) | `R/contention_30b_t16` |
| 39.39 (18.52); 42.68 (26.14) | `R/contention_30b_cpu_t16_px1536` |
| 56.27 (45.20); 18.56 (13.19) | `R/contention_4b_gpu_ctx8k` |
| card 26,396 → 29,453; 26,390 → 29,408; 26,405 → 26,391; 26,391 → 29,816 | `gpu_mib_before` → `gpu_mib_loaded` |
| the two capped CPU launches differ only in the window, 32,768 against 8,192 | SL launch lines 08:51:44 and 09:09:39 (both `--no-mmap -b 1024 -ub 1024 -ngl 0 -t 16`) |
| all four found 12 strings | `derived/score_output.txt`: 12/12 each |
| 1,370 and 1,802 tokens against 4,154 and 1,974 | `prompt_tokens` of the four files |
| picture encoder off the card; `--no-mmproj-offload`; CPU backend | SL launch line 09:02:40 (`--no-mmproj-offload`) and `clip_ctx: CLIP using CPU backend` after it |
| 206.87 seconds | as above |
| 88 percent on the CPU | `R/contention_30b_t16` `ollama_ps` |
| a third of the tokens (1,370 against 4,154) | **arithmetic**: 1,370 / 4,154 = 0.33 |
| raised the card's reading by 3,057, 3,018 and 3,425 MiB | **arithmetic**: 29,453 - 26,396; 29,408 - 26,390; 29,816 - 26,391 |
| empty card: 38.52 and 38.93 | `R/qwen3vl30b_cpu_t16_px1536`: nebula `wall_s` 38.52, poster `wall_s` 38.93 |

## 07 The cap on small text

| figure | file and field |
|---|---|
| 24 codes, six per text size | `hires_truth.json` |
| 4 threads, 32,768-token window | SL `system_info` at 08:56:10, 08:56:22, 08:56:33, 08:56:45 (`n_threads = 4`); launch lines `-c 32768` |
| 8.56 to 9.88 s including a 4.56 to 4.84-s load | first `wall_s` and `load_s` of the four `R/hires_30b_hires*` files |
| prompt tokens 4,154, 3,674, 2,378, 1,370 | their `prompt_tokens` |
| codes found per size and in total | `derived/hires_score_output.txt` |
| F12-zephyr-6829 for F12-zephyr-6823 (2,048); D14-kettle-B104, F12-pebble-4823, E28-ribbon-7319, H40-pebble-8359 for D14-kettle-8104, F12-zephyr-6823, E26-ribbon-7519, H20-pebble-8359 (1,536) | `derived/hires_score_output.txt` "written" lines; the replies in `R/hires_30b_hires_2048` and `R/hires_30b_hires_1536` |
| 5.2 pixels at 1,536; about 6.9 at 2,048 | **arithmetic**: 13 × 1,536 / 3,840 = 5.2; 13 × 2,048 / 3,840 = 6.93 |

## 08 What 39 strings show

| figure | file and field |
|---|---|
| Qwen3.5 4B dropped nine strings | 39 - 30 (`derived/score_output.txt`), **arithmetic** |
| eleven seven-picture runs | the 11 files with 7 pictures in `derived/runs.tsv` (`pictures` = 7) |
| all six card models described the cottage as stored (a green band on the right, the caption vertical; the 4B called the house an arrow); five scored 3 of 3 | cottage `text` in the six card files; `derived/strings_by_picture.tsv` (the 4B 2 of 3) |
| upright in the capped sets: sky at the top, green ground at the bottom | cottage `text` in `R/qwen3vl30b_cpu_t16_px1536` ("grass or ground" at the bottom, sky above), `R/qwen3vl4b_cpu_t16_px1536` ("sky at top, ground at bottom"), `R/qwen3vl4b_cpu_t16_px1024` ("a green ground plane at the bottom") |
| three logo replies: a dark wordmark, a TM, coloured curves in the top-right and bottom-left corners; "COSMIC" matched | logo `text` in `R/qwen3vl30b_gpu`, `R/qwen3vl8b_gpu`, `R/qwen36_35b_gpu`; `derived/strings_by_picture.tsv` (1 of 1 each); the pixels as in section 02's picture 7 row |
| the 30B's and the 8B's chart sentences; 9 of 9 | chart `text` in `R/qwen3vl30b_gpu` and `R/qwen3vl8b_gpu`; `derived/strings_by_picture.tsv` |
| February's 35, January's 42 | `build_test_images.py` (`data = [("Jan", 42), ("Feb", 35), ...]`) |
| 2,048, 1,562 and 2,048 tokens; within the first 1,400 characters | `R/qwen35_4b_gpu` `out_tokens`; the replies' `text` (the unpunctuated stream begins at about character 1,376, 993 and 735) |
| the Earth reply scored 1 of 1 | `derived/strings_by_picture.tsv`, `qwen35_4b_gpu` / `02_earth_from_orbit.jpg` |
| "a building or cottage" | `R/qwen3vl4b_cpu_t16`, cottage `text`; miss in `derived/score_misses.txt` |
| the 30B made up a question in three replies | `R/qwen3vl30b_cpu_t8` nebula; `R/qwen3vl30b_cpu_t16_px1536` nebula and poster (search the replies for "question") |
| 13 prompt passages and one word removed | README, "Redactions" |

## 09 What to run

Every figure repeats one above: 1.31 to 3.16 s, 22 GB and 19 GB (section 03); 1.81 to 3.82 s and 10 GB
(section 03); 30 of 39 (section 03); 3,018 to 3,425 MiB (section 06, **arithmetic**); 4 threads of 24,
within 4 seconds (3.13 and 3.90, section 04), 157.31 over 150 (section 04); 4,154 → 1,370 tokens, 111.01
→ 38.52 s, 39 strings (section 05); 4 of 24 codes, 2,560 found 24 (section 07); 6,206 tokens (section 03,
**arithmetic**) and 19 GB instead of 22 (section 03, `ollama ps`); 22.64 to 38.93 s, 12.30 s of
load, 22 and 19 GB (sections 05 and 06); 18.12 to 32.64 s, 8.0 GB, 39 strings (section 05).

## 10 What this does not show; 11 Related pages; 12 Sources

| figure | file and field |
|---|---|
| 36.97; 4.56 to 4.86 | as section 02 |
| two pictures each; one for the 4-thread run | `derived/runs.tsv` `pictures` |
| no transparency test (picture 7 has no transparent pixels) | README point 13 |
| Ollama launched the describers with batches of 1,024 or 512 tokens | SL launch lines: `-b 1024 -ub 1024`, or `-b 512 -ub 512` on the three split loads and the Qwen3.6 load |
| 13 passages in five files | README, "Redactions" |
| heic0601a, CC BY 4.0 (linked); the shipped JPEG a 3840 x 2160 derivative, not the release file; ISS064-E-29444 | README, "The pictures and their terms"; `images/01_nebula_large.jpg` |
| 2026-09-20 08:19 to 09:16; 2026-09-26 | as section 02; this package's derived files are dated 26 September |
