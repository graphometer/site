# What the model files themselves say

Every quantization, shard count, byte count and header figure the page prints, with the record it
was read from. Three kinds of record appear here, and each block says which one it is:

1. **A load header**: the lines the runtime printed when it read the file, copied from that run's
   own log.
2. **A file check**: the file listing or byte check a run made before it started.
3. **A start script header**: the first lines of the script that serves a model, as they stood in
   the backup taken on 2026-09-12. Paths are removed; the file name, the quantization and the size
   the script states are kept.

Nothing here is a measurement of speed. Paths, addresses and program names are removed.

---

## DeepSeek V4 Flash 0731, the 3-bit file (page rows 1 and 3)

Load header, from the run of 2026-09-14 that read the file across both machines:

```
llama_model_loader: - kv   0:  general.architecture     str = deepseek4
llama_model_loader: - kv   5:  general.name             str = Deepseek-V4-Flash-0731
llama_model_loader: - kv   8:  general.quantized_by     str = Unsloth
llama_model_loader: - kv   9:  general.size_label       str = 256x8.4B
llama_model_loader: - kv  10:  general.license          str = mit
llama_model_loader: - kv  39:  deepseek4.expert_shared_count u32 = 1
print_info: file type   = IQ3_XXS, 3.0625 bpw
print_info: file size   = 97.05 GiB (2.93 BPW)
print_info: arch                  = deepseek4
print_info: n_ctx_train           = 1048576
print_info: n_embd                = 4096
print_info: n_layer               = 43
print_info: n_head                = 64
print_info: n_expert              = 256
print_info: n_expert_used         = 6
print_info: model params          = 284.33 B
```

This is where the page's "284.33B in the base model" and "256 experts, 6 used per token plus 1
shared" come from. They are readings of the file, not the maker's published figures. The maker's
own model card at the pinned revision, which ships in `vendor/`, states no active-parameter
figure, so the page prints none.

File check: the four-shard listing and the five-shard listing of the 4-bit file are in
`two-box-deepseek-probes-2026-09-13-to-15.txt`, with their totals (104.2 GB and 155.1 GB).

## The files served in the direct sweep (page rows 5, 7, 9, 10, 11, 12, 13)

File names, from each run's own command line in `context-sweep-2026-09-12.tsv`'s campaign logs.
Only the file name is kept; the directory it sat in is not published.

| page row | model | file served on 2026-09-12 |
|---|---|---|
| 5 | Qwen3-235B-A22B Instruct 2507 | `Qwen3-235B-A22B-Instruct-2507-Q4_K_M.gguf` |
| 7 | Qwen3.8-27B | `Qwen3.8-27B-UD-Q5_K_XL.gguf` |
| 9 | Qwen3.8-Flash-Next 125B | `Qwen3.8-Flash-Next-UD-Q3_K_XL-00001-of-00003.gguf` (3 shards) |
| 10 | GLM-4.7-Flash 31B | `GLM-4.7-Flash-UD-Q4_K_XL.gguf` |
| 11 | GLM-4.7 Full 358B | `GLM-4.7-UD-IQ3_XXS-00001-of-00003.gguf` (3 shards) |
| 12 | Gemma-4-26B-A4B | `gemma-4-26B-A4B-it-UD-Q4_K_XL.gguf` |
| 13 | Gemma-4-31B IT QAT | `gemma-4-31B_q4_0-it.gguf` |

No byte count was recorded for any of these seven files in the September measurement records,
which is why the page prints a quantization and, for most of them, no size.

## Qwen3.8-27B, the size its start script states (page row 7)

Start script header, backup of 2026-09-12:

```
# start_server.sh, Qwen3.8-27B (unsloth UD-Q5_K_XL, 20.2 GB)
```

## Qwen3.6-27B (page row 8)

File check, from the start script written for it on 2026-09-13:

```
sz=$(stat -c %s "$MODEL"); [ "$sz" = 17612564704 ] || exit 2
```

Header of the file that runs (a header read, not a load):

```
general.architecture      qwen35
general.basename          Qwen3.6-27B
general.base_model.0.name Qwen3.6 27B
general.base_model.0.organization Qwen
general.quantized_by      Unsloth
general.size_label        27B
tensor_count              851
```

The second copy of this model that the campaign held is not in this package and was never served:
it is a repackaging made for another program's runner, and its header declares three values in
one field where llama.cpp requires four, so it would not load.

## Ling-3.0-flash (page row 14)

Header read of the first shard:

```
general.architecture                bailingmoe3
general.name                        Ling 3.0 Flash
general.license                     mit
general.size_label                  512x3.9B
general.file_type                   15
bailingmoe3.block_count             43
bailingmoe3.context_length          262144
bailingmoe3.expert_count            512
bailingmoe3.expert_used_count       8
bailingmoe3.expert_shared_count     1
bailingmoe3.leading_dense_block_count 2
tensor_count                        493
```

File check: 2 shards, 77,804,990,144 bytes, both byte for byte against the maker's published file
listing.

## Inkling-Small (page row 2)

Its header facts are in `inkling-probes-2026-09-14.md`: `unsloth` UD-Q3_K_XL, 4 shards,
119,554,379,840 bytes, 42 blocks, 256 experts, 6 used per token plus 2 shared.

## Kimi K2.7-Code (page row 20)

Load header, from the September run that read the file across both machines:

```
print_info: file type   = IQ1_M, 1.75 bpw
print_info: n_expert              = 384
print_info: model params          = 1.03 T
print_info: general.name          = Kimi-K2.7-Code
```

The file is an 8-shard `unsloth` build. No byte count for it was recorded in the September files.

## Muse Glimmer 30B (page row 22)

Start script header, backup of 2026-09-12: the file it serves is a `Q4_K_M` build with a separate
`Q4_K_M` draft model beside it. No byte count for either file was recorded in the September files.

## The rows with no file record at all

Rows 16 to 19 and 21 (Mistral Medium 3.5, Mistral Large 3, MiniMax M3, Laguna S 2.1, Kimi K3)
were not served in any September run in this package. What the page prints for them under
"quantization and file" is the installed configuration on the machine, which is our own operator
record and not a measurement. Mistral Medium 3.5 is the exception that is half recorded: it was
started and did not answer within the check's timeout, and the file its start script names is a
three-shard `UD-Q4_K_XL` build.
