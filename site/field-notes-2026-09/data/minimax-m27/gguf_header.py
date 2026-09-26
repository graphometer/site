#!/usr/bin/env python3
"""Standalone GGUF metadata reader - no numpy, no gguf-py dependency.

This machine's system python3 has no numpy, so `gguf-py` cannot be imported here; the GGUF
header format is simple enough to read directly, which is also the safer option (it never
touches tensor data, only the KV block at the head of shard 1).

Usage: gguf_header.py SHARD1.gguf [--template]
"""
import struct
import sys

GGUF_MAGIC = b"GGUF"
(U8, I8, U16, I16, U32, I32, F32, BOOL, STRING, ARRAY, U64, I64, F64) = range(13)
FMT = {U8: "<B", I8: "<b", U16: "<H", I16: "<h", U32: "<I", I32: "<i",
       F32: "<f", BOOL: "<?", U64: "<Q", I64: "<q", F64: "<d"}
SIZE = {U8: 1, I8: 1, U16: 2, I16: 2, U32: 4, I32: 4, F32: 4, BOOL: 1,
        U64: 8, I64: 8, F64: 8}


class R:
    def __init__(self, f):
        self.f = f

    def raw(self, n):
        b = self.f.read(n)
        if len(b) != n:
            raise EOFError("short read")
        return b

    def scalar(self, t):
        return struct.unpack(FMT[t], self.raw(SIZE[t]))[0]

    def string(self):
        n = self.scalar(U64)
        return self.raw(n).decode("utf-8", "replace")

    def value(self, t):
        if t == STRING:
            return self.string()
        if t == ARRAY:
            et = self.scalar(U32)
            n = self.scalar(U64)
            if et == STRING:
                # do not materialise 200k tokeniser strings; skip and report the count
                for _ in range(n):
                    self.raw(self.scalar(U64))
                return f"<array of {n} strings, skipped>"
            if et == ARRAY:
                return f"<nested array, {n} entries, skipped>"
            vals = [self.scalar(et) for _ in range(n)]
            if len(vals) > 16:
                return f"<array[{et}] of {n}: {vals[:8]} … {vals[-4:]}>"
            return vals
        return self.scalar(t)


def main():
    path = sys.argv[1]
    want_template = "--template" in sys.argv
    with open(path, "rb") as f:
        r = R(f)
        if r.raw(4) != GGUF_MAGIC:
            print("NOT A GGUF FILE")
            return 2
        ver = r.scalar(U32)
        ntensors = r.scalar(U64)
        nkv = r.scalar(U64)
        print(f"file            {path}")
        print(f"gguf_version    {ver}")
        print(f"tensor_count    {ntensors:,d}")
        print(f"kv_count        {nkv:,d}")
        print("-" * 72)
        kvs = {}
        for _ in range(nkv):
            k = r.string()
            t = r.scalar(U32)
            v = r.value(t)
            kvs[k] = v
        template = kvs.pop("tokenizer.chat_template", None)
        for k in sorted(kvs):
            v = kvs[k]
            s = str(v)
            if len(s) > 220:
                s = s[:220] + f" …(+{len(s)-220} chars)"
            print(f"{k:48s} {s}")
        if template is not None:
            print("-" * 72)
            print(f"tokenizer.chat_template          <{len(template)} chars>")
            for probe in ("enable_thinking", "reasoning_effort", "thinking",
                          "<think>", "</think>", "thinking_budget", "tools",
                          "tool_call", "add_generation_prompt"):
                print(f"  template mentions {probe!r:26s} : {probe in template}")
            if want_template:
                print("-" * 72)
                print(template)
    return 0


if __name__ == "__main__":
    sys.exit(main())
