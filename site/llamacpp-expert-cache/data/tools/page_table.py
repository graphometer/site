#!/usr/bin/env python3
"""Prints every figure in the page's tables from the files in this package, so no table number is typed by hand.
usage: python3 page_table.py   (run from anywhere; it finds ../runs/ itself). Read-only."""
import json, math, os, re

R = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'runs')


def ready_lines(r):
    """label -> list of (load seconds, RssFile GiB, RssShmem GiB, available GiB) from RUNS.log and the round outputs."""
    out = {}
    for f in (f'{R}/{r}/logs/RUNS.log', f'{R}/{r}/logs/ready_and_trap_lines.txt'):
        for l in open(f, errors='replace'):
            m = re.match(r'(\S+): pid \S+ ready after (\d+) s(.*)', l)
            if not m:
                continue
            rest = m.group(3)
            g = lambda k: (re.search(k + r': ([0-9.]+)', rest) or [None, None])[1]
            av = re.search(r'available (\d+) GiB', rest)
            row = (int(m.group(2)), g('RssFile'), g('RssShmem'), av.group(1) if av else None)
            out.setdefault(m.group(1), [])
            if row not in out[m.group(1)]:
                out[m.group(1)].append(row)
    return out


READY = {r: ready_lines(r) for r in ('r1', 'r2', 'r3')}


def J(r, n):
    p = f'{R}/{r}/results/{n}'
    return json.load(open(p)) if os.path.exists(p) else None


def flag(c, f):
    m = re.findall(rf'(?:^|\s){f}[ =](\S+)', c)
    return m[-1] if m else None


def cmd(r, l):
    for e in ('.cmd', '.cmdline'):
        p = f'{R}/{r}/logs/cmd/{l}{e}'
        if os.path.exists(p):
            return open(p).read()
    return ''


def shape(r, l, extra=()):
    s = J(r, l + '.screen.json')
    st = {x['step']: x for x in s['steps']}
    card, ram = [s['peak']['gpu_mib']], [s['peak']['avail_min_gib']]
    for e in extra:
        q = J(r, e + '.json')
        if q and q.get('peak'):
            card.append(q['peak']['gpu_mib'])
            ram.append(q['peak']['avail_min_gib'])
    c = cmd(r, l)
    rl = READY[r].get(l, [])
    return dict(label=l, load=[x[0] for x in rl], rssfile=[x[1] for x in rl], shmem=[x[2] for x in rl],
                first=st['prose1']['gen_tps'], second=st['prose2']['gen_tps'], code=st['code']['gen_tps'],
                read=st['read']['read_tps'], read_n=st['read']['read_n'], code_ok=s.get('code_ok'),
                next_s=st['next']['read_s'], next_tps=st['next']['gen_tps'],
                first_wall=st['prose1']['wall_s'], faults=sum(x['majflt'] for x in st.values()),
                drive=round(sum(x['drive_GB'] for x in st.values()), 1),
                card=max(card), ram=round(min(ram), 1), ctx=flag(c, '--ctx-size'), ub=flag(c, '--ubatch-size'),
                cache=flag(c, '--moe-cache-mib'), lm=flag(c, '--load-mode'), ctk=flag(c, '--cache-type-k') or flag(c, '-ctk'),
                build=(s.get('props') or {}).get('build_info'), file=(s.get('props') or {}).get('model_path', '').split('/')[-1])


# name, round, before, dio alone (or None), after, result files that add to the after shape's card and RAM figures, the same for before
ROWS = [
    ('DeepSeek V4.1 Flash', 'r1', 'deepseek-v4.1-flash-ship', 'deepseek-v4.1-flash-dio', 'final-deepseek-v4.1-flash', ['final-deepseek-v4.1-flash'], []),
    ('GLM-5.3-Flash', 'r1', 'glm-5.3-flash-ship', 'glm-5.3-flash-dio', 'final-glm-5.3-flash', ['final-glm-5.3-flash'], []),
    ('DeepSeek V4 Flash', 'r1', 'deepseek-v4-flash-ship', 'deepseek-v4-flash-dio', 'final-deepseek-v4-flash', ['final-deepseek-v4-flash', 'deepseek-v4-flash-proof'], []),
    ('MiMo-V2.6-Flash', 'r1', 'mimo-v2.6-flash-ship', 'mimo-v2.6-flash-dio', 'final-mimo-v2.6-flash', ['final-mimo-v2.6-flash'], []),
    ('Qwen3.8-Flash-Next', 'r1', 'qwen3.8-flash-next-ship', 'qwen3.8-flash-next-dio', 'final-qwen3.8-flash-next', ['final-qwen3.8-flash-next', 'qwen3.8-flash-next-proof'], []),
    ('Ornith-1.5-122B', 'r1', 'ornith-1.5-122b-ship', 'ornith-1.5-122b-dio', 'final-ornith-1.5-122b', ['final-ornith-1.5-122b', 'ornith-1.5-122b-proof'], []),
    ('Beam 1.0', 'r1', 'beam-1.0-ship', 'beam-1.0-dio', 'final-beam-1.0', ['final-beam-1.0', 'beam-1.0-proof'], []),
    ('Muse Spark Open', 'r1', 'muse-spark-open-ship', 'muse-spark-open-dio', 'final-muse-spark-open', ['final-muse-spark-open', 'muse-spark-open-proof'], []),
    ('gpt-oss-120b', 'r1', 'gpt-oss-120b-ship24', None, 'final-gpt-oss-120b', ['final-gpt-oss-120b', 'gpt-oss-120b-proof'], []),
    ('Ling-3.0-flash', 'r1', 'ling-3.0-flash-ship', 'ling-3.0-flash-dio', 'final-ling-3.0-flash', ['final-ling-3.0-flash', 'ling-3.0-flash-proof'], []),
    ('Qwen3.5-397B-A17B', 'r1', 'qwen3.5-397b-ship', None, 'final-qwen3.5-397b', ['final-qwen3.5-397b', 'qwen3.5-397b-proof'], []),
    ('Qwen3-Coder-Next', 'r1', 'qwen3-coder-next-ship', 'qwen3-coder-next-dio', 'final-qwen3-coder-next', ['final-qwen3-coder-next', 'qwen3-coder-next-proof'], []),
    ('Inkling-Small', 'r1', 'inkling-small-ship', 'inkling-small-dio', 'final-inkling-small', ['final-inkling-small', 'inkling-small-proof'], []),
    ('Nemotron 3.5 Bolt', 'r1', 'nemotron-3.5-bolt-ship', 'nemotron-3.5-bolt-dio', 'final-nemotron-3.5-bolt', ['final-nemotron-3.5-bolt', 'nemotron-3.5-bolt-proof'], []),
    ('Qwen3-235B-A22B', 'r1', 'qwen3-235b-ship', 'qwen3-235b-dio', 'final-qwen3-235b', ['final-qwen3-235b'], []),
    ('Qwen3.5-122B-A10B', 'r1', 'qwen3.5-122b-ship', None, 'final-qwen3.5-122b', ['final-qwen3.5-122b'], []),
    ('Qwen3.6-35B-A3B', 'r2', 'qwen3.6-35b-a3b-screen-ship', 'qwen3.6-35b-a3b-screen-dio', 'final-qwen3.6-35b-a3b', ['final-qwen3.6-35b-a3b', 'qwen3.6-35b-a3b-deep-c18u4', 'qwen3.6-35b-a3b-proof-c18u4'], ['qwen3.6-35b-a3b-deep-ship']),
    ('Qwen3-30B-A3B, 256K', 'r2', 'qwen3-30b-a3b-screen-ship', 'qwen3-30b-a3b-screen-dio', 'final-qwen3-30b-a3b', ['final-qwen3-30b-a3b', 'qwen3-30b-a3b-deep-q8c115u4', 'qwen3-30b-a3b-proof-q8c115u4'], ['qwen3-30b-a3b-deep-ship']),
    ('Qwen3-30B-A3B, 128K', 'r2', 'qwen3-30b-a3b-deep-128ship', None, 'final-qwen3-30b-a3b-128', ['final-qwen3-30b-a3b-128', 'qwen3-30b-a3b-proof-128c135u4'], ['qwen3-30b-a3b-deep-128ship']),
    ('Ornith-1.5-35B', 'r3', 'ornith-1.5-35b-ship', 'ornith-1.5-35b-dio', 'final-ornith-1.5-35b', ['final-ornith-1.5-35b', 'ornith-1.5-35b-c18'], ['ornith-1.5-35b-ship']),
]

# hand-started deep runs of the three smaller models: before, after
DEEP = [('Qwen3.6-35B-A3B', 'r2', 'qwen3.6-35b-a3b-deep-ship', 'qwen3.6-35b-a3b-deep-c18u4'),
        ('Qwen3-30B-A3B, 256K', 'r2', 'qwen3-30b-a3b-deep-ship', 'qwen3-30b-a3b-deep-q8c115u4'),
        ('Qwen3-30B-A3B, 128K', 'r2', 'qwen3-30b-a3b-deep-128ship', 'qwen3-30b-a3b-proof-128c135u4'),
        ('Ornith-1.5-35B', 'r3', 'ornith-1.5-35b-ship', 'ornith-1.5-35b-c18')]

# the same cache size on different builds (PR = master with pull request 31286)
PR = [('r1', x) for x in ('glm-5.3-flash-b15-c11', 'glm-5.3-flash-new-c11', 'deepseek-v4.1-flash-b15-c11', 'deepseek-v4.1-flash-new-c11',
                          'gpt-oss-120b-b15-c20', 'gpt-oss-120b-new-c20', 'ling-3.0-flash-b15-c20', 'ling-3.0-flash-new-c20',
                          'ornith-1.5-122b-inst-c18', 'ornith-1.5-122b-b15-c18', 'ornith-1.5-122b-new-c18',
                          'deepseek-v4-flash-inst-c45', 'deepseek-v4-flash-b15-c45', 'deepseek-v4-flash-new-c45', 'deepseek-v4-flash-b15-u4096-c7',
                          'qwen3.8-flash-next-inst-c15', 'qwen3.8-flash-next-new-c15')] + [('r2', 'qwen3-30b-a3b-screen-f16c2')]


def logits(r, a, b):
    x_, y_ = J(r, a + '.logits.json'), J(r, b + '.logits.json')
    same = tot = 0
    diffs = []
    for x, y in zip(x_, y_):
        part = None
        for i in range(min(len(x['tokens']), len(y['tokens']))):
            tot += 1
            if x['tokens'][i][0] == y['tokens'][i][0]:
                same += 1
                if part is None:
                    px, py = dict(x['tokens'][i][1]), dict(y['tokens'][i][1])
                    diffs += [abs(math.exp(px[t]) - math.exp(py[t])) for t in px if t in py]
            elif part is None:
                part = i
    return f'{same} of {tot}, {sum(diffs) / max(len(diffs), 1):.4f} / {max(diffs or [0]):.3f}'


LOGIT = [('r1', 'beam-1.0-shiplogit', 'beam-1.0-proof'), ('r1', 'muse-spark-open-ship3', 'muse-spark-open-dio2'),
         ('r1', 'muse-spark-open-shiplogit', 'muse-spark-open-ship3'), ('r1', 'ornith-1.5-122b-shiplogit', 'ornith-1.5-122b-diologit'),
         ('r1', 'inkling-small-shiplogit', 'inkling-small-proof'), ('r1', 'qwen3-235b-shiplogit', 'qwen3-235b-diologit'),
         ('r1', 'qwen3.5-122b-shiplogit', 'qwen3.5-122b-diologit'), ('r1', 'qwen3.5-397b-shiplogit', 'qwen3.5-397b-proof'),
         ('r1', 'qwen3.8-flash-next-shiplogit', 'qwen3.8-flash-next-proof'), ('r1', 'ling-3.0-flash-shiplogit', 'ling-3.0-flash-proof'),
         ('r1', 'gpt-oss-120b-shiplogit', 'gpt-oss-120b-proof'), ('r1', 'deepseek-v4-flash-shiplogit', 'deepseek-v4-flash-proof'),
         ('r1', 'nemotron-3.5-bolt-shiplogit', 'nemotron-3.5-bolt-proof'), ('r1', 'mimo-v2.6-flash-shiplogit', 'mimo-v2.6-flash-proof'),
         ('r1', 'deepseek-v4.1-flash-shiplogit', 'deepseek-v4.1-flash-proof'), ('r1', 'glm-5.3-flash-shiplogit', 'glm-5.3-flash-proof'),
         ('r1', 'qwen3-coder-next-shiplogit', 'qwen3-coder-next-proof'), ('r1', 'ornith-1.5-122b-shiplogit', 'ornith-1.5-122b-proof'),
         ('r2', 'qwen3.6-35b-a3b-logit-logit', 'qwen3.6-35b-a3b-proof-c18u4'), ('r2', 'qwen3-30b-a3b-logit-logit', 'qwen3-30b-a3b-proof-q8c115u4'),
         ('r2', 'qwen3-30b-a3b-deep-128ship', 'qwen3-30b-a3b-proof-128c135u4'), ('r3', 'ornith-1.5-35b-ship', 'ornith-1.5-35b-c18'),
         ('r3', 'ornith-1.5-35b-ship', 'ornith-1.5-35b-ship2')]

if __name__ == '__main__':
    print('# Main table: before / dio alone / after')
    for name, r, b, d, a, ax, bx in ROWS:
        print('##', name)
        S = {}
        for k, l, ex in (('before', b, bx), ('dio', d, []), ('after', a, ax)):
            if not l:
                continue
            x = S[k] = shape(r, l, ex)
            print(f"  {k:6} {l}: load {x['load']} s | first {x['first']} second {x['second']} code {x['code']} | read {x['read']} t/s on {x['read_n']} tokens (code {'OK' if x['code_ok'] else 'MISS'}) | "
                  f"next turn {x['next_s']} s then {x['next_tps']} t/s | card peak {x['card']:,} MiB | lowest available RAM {x['ram']} GiB | "
                  f"RssFile {x['rssfile']} RssShmem {x['shmem']} GiB at ready | faults {x['faults']:,} drive {x['drive']} GB | "
                  f"ctx {x['ctx']} ub {x['ub']} cache {x['cache']} load-mode {x['lm']} kv {x['ctk']} | build {x['build']} | {x['file']}")
        B, A = S['before'], S['after']
        print(f"  ratios after/before: second answer {A['second'] / B['second']:.2f}, next turn {A['next_tps'] / B['next_tps']:.2f}, 20K read {A['read'] / B['read']:.2f}")
        if 'dio' in S:
            D = S['dio']
            print(f"  ratios dio/before: 20K read {D['read'] / B['read']:.2f}, cold load {D['load'][0] / B['load'][0]:.2f}, second answer {D['second'] / B['second']:.3f}")
    print('\n# Deep runs (hand-started): depth, prompt tokens, read t/s, next-turn t/s, codes')
    for name, r, b, a in DEEP:
        for k, l in (('before', b), ('after', a)):
            d = J(r, l + '.json')
            print(f"  {name} {k} {l}: " + '; '.join(f"{x['depth']}: {x['prompt_n']} tok, read {x['read_tps']}, next {x['next_gen_tps']}, codes {x['codes']}/3" for x in d['depth']))
    print('\n# Same cache size, different builds: second answer, code, next turn, 20K read, card peak')
    for r, l in PR:
        x = shape(r, l)
        print(f"  {l} ({x['build']}, cache {x['cache']} MiB, ub {x['ub']}): {x['second']} / {x['code']} / {x['next_tps']} / {x['read']} / {x['card']:,}")
    print('\n# Output against the before shape (greedy tokens the same; top-5 probability moved, average / most)')
    for r, a, b in LOGIT:
        print(f'  {a} vs {b}: {logits(r, a, b)}')
