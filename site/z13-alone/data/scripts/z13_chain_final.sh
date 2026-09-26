#!/usr/bin/env bash
# z13_chain_final.sh  -  (1) crash-check the two Z13 candidates at the setting they would be recommended with
# (-ub 512, their served 256K windows): the exact desktop crash replay first, then 40 real-text prompts;
# (2) the remaining data points: DeepSeek V4 Flash IQ3 at 128K (+ a 256K fit check), GLM-4.7-Flash at its
# served 198K, Qwen3.5-122B at its served 128K. One server at a time; every step runs even if one fails.
set -u
D="<REDACTED_PATH>/RUN_DIR"
G="<REDACTED_PATH>/models"
LING=$G/Ling-3.0-flash/Ling-3.0-flash-Q4_K_M/Ling-3.0-flash-Q4_K_M-00001-of-00002.gguf
FN=$G/Qwen3.8-Flash-Next/Qwen3.8-Flash-Next-UD-Q3_K_XL-00001-of-00003.gguf
DSV4=$G/DeepSeek-V4-Flash-0731/UD-IQ3_XXS/DeepSeek-V4-Flash-0731-UD-IQ3_XXS-00001-of-00004.gguf
GLMF=$G/GLM-4.7-Flash/GLM-4.7-Flash-UD-Q4_K_XL.gguf
Q122=$G/Qwen3.5-122B-A10B/UD-Q4_K_S/Qwen3.5-122B-A10B-UD-Q4_K_S-00001-of-00003.gguf
echo "[z13] stress ling_ub512"
python3 -u "$D/z13_stress.py" ling_ub512 "$LING" 262144 512 40 7 2>&1 | sed -u 's/^/  /'
echo "[z13] stress fn_ub512"
python3 -u "$D/z13_stress.py" fn_ub512 "$FN" 262144 512 40 8 \
  -ctk q8_0 -ctv q8_0 --chat-template-kwargs '{"reasoning_effort": "medium"}' 2>&1 | sed -u 's/^/  /'
"$D/z13_run2.sh" dsv4_ctx128k_ub512 "$DSV4" 131072 512 "3000 48000" --reasoning-format deepseek --no-repack
"$D/z13_run2.sh" dsv4_ctx256k_ub512_fit "$DSV4" 262144 512 "3000" --reasoning-format deepseek --no-repack
"$D/z13_run2.sh" glm47flash_ctx198k_ub512 "$GLMF" 202752 512 "3000 48000"
"$D/z13_run2.sh" q122_ctx128k_ub512 "$Q122" 131072 512 "3000 48000"
echo CHAIN-DONE
