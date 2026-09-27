#!/usr/bin/env python3
"""Recompute arithmetic from the shipped headers and recorded responses."""
import collections
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODELS = {'inkling-small': 42, 'qwen397': 57, 'deepseek': 43, 'inkling-975b': 66}

def calculate():
    models, tensor_rows, file_rows, anchors = {}, [], [], []
    for model, cpu_layers in MODELS.items():
        shards = json.loads((ROOT / (model + '-headers.json')).read_text())
        meta = shards[0]['metadata']
        arch = meta['general.architecture']
        total, active = meta[arch + '.expert_count'], meta[arch + '.expert_used_count']
        layers = meta[arch + '.block_count']
        draft_layers = meta.get(arch + '.nextn_predict_layers', 0)
        categories = collections.defaultdict(int)
        cpu_bytes = gpu_expert_bytes = remote_bytes = embedding_row_bytes = 0
        tensors = [t for s in shards for t in s['tensors']]
        assert len({t['name'] for t in tensors}) == len(tensors)
        for shard in shards:
            file_rows.append(dict(model=model, file=shard['file'],
                file_size_bytes=shard['file_size_bytes'],
                header_bytes_read=shard['header_bytes_read'],
                header_sha256=shard['header_sha256']))
            for t in shard['tensors']:
                n, size = t['name'], t['bytes']
                layer = int(n.split('.')[1]) if n.startswith('blk.') else None
                draft = layer is not None and layer >= layers - draft_layers
                routed = n.endswith(('_up_exps.weight','_gate_exps.weight','_down_exps.weight'))
                nominal, counted, location = size, 0, 'GPU configured'
                if draft:
                    category, nominal = 'draft weights', 0
                    location = 'GPU draft; traffic depends on proposals'
                elif routed:
                    assert t['dims'][-1] == total
                    nominal = size * active // total
                    assert size * active % total == 0
                    category = 'routed experts'
                    if layer < cpu_layers:
                        counted = nominal
                        cpu_bytes += counted
                        location = 'system RAM'
                    else:
                        gpu_expert_bytes += nominal
                    if model == 'inkling-975b' and layer >= 42:
                        remote_bytes += nominal
                elif '_shexp.' in n or '_inp_shexp.' in n:
                    category = 'shared experts and shared gate'
                elif n == 'token_embd.weight':
                    category = 'input embedding'
                    nominal = size // t['dims'][1]
                    embedding_row_bytes = nominal
                    location = 'input lookup; excluded from expert-only denominator'
                elif n.startswith('output'):
                    category = 'output head and output norms'
                elif any(x in n for x in ('attn_', 'ssm_', 'shortconv_', 'indexer')):
                    category = 'attention and recurrent state weights'
                elif n.endswith(('ffn_up.weight','ffn_down.weight','ffn_gate.weight')):
                    category = 'dense feed-forward'
                else:
                    category = 'routing, norms and other weights'
                categories[category] += size
                tensor_rows.append(dict(model=model,file=shard['file'],tensor=n,
                    dimensions='x'.join(map(str,t['dims'])),quantization=t['type'],
                    stored_bytes=size,category=category,placement=location,
                    expert_RAM_bytes_per_logical_token=counted,
                    nominal_weight_bytes_per_pass=nominal))
        models[model] = dict(architecture=arch,blocks=layers,draft_blocks=draft_layers,
            experts=total,active_experts=active,cpu_expert_layers_setting=cpu_layers,
            file_bytes=sum(s['file_size_bytes'] for s in shards),
            category_stored_bytes=dict(categories),expert_RAM_bytes_per_token=cpu_bytes,
            GPU_active_expert_bytes_per_token=gpu_expert_bytes,
            input_embedding_row_bytes=embedding_row_bytes,
            pair_remote_expert_bytes_per_token=remote_bytes,
            pair_local_expert_bytes_per_token=cpu_bytes-remote_bytes)
        if model != 'inkling-975b':
            for rep in (1,2):
                name = f'{model}-prose-r{rep}.json'
                j = json.loads((ROOT / 'runs' / name).read_text())
                t = j['timings']
                anchors.append(dict(model=model,record='runs/'+name,
                    repetition=rep,rate=t['predicted_per_second'],
                    generated_tokens=t['predicted_n'],prompt_tokens=j['usage']['prompt_tokens'],
                    visible_words=len(j['choices'][0]['message']['content'].split()),
                    finish_reason=j['choices'][0]['finish_reason'],
                    selected=(model != 'deepseek' or rep == 2),
                    effective_expert_GB_s=cpu_bytes*t['predicted_per_second']/1e9))
    selected = [a['effective_expert_GB_s'] for a in anchors if a['selected']]
    rate_range = [min(selected), max(selected)]
    target = models['inkling-975b']['expert_RAM_bytes_per_token']
    result = dict(models=models,anchors=anchors,effective_expert_GB_s_range=rate_range,
        inkling975_prediction_tokens_s=[x*1e9/target for x in rate_range],
        units='GB is decimal: 1000000000 bytes. All bandwidth and prediction values are arithmetic.')
    (ROOT/'arithmetic.json').write_text(json.dumps(result,indent=2)+'\n')
    for name,rows in [('tensors.csv',tensor_rows),('files.csv',file_rows)]:
        with (ROOT/name).open('w') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(json.dumps({k:v for k,v in result.items() if k not in ('models','anchors')},indent=2))

if __name__ == '__main__':
    calculate()
