#!/usr/bin/env python3
"""Migrate wordlist.js glyph variants to the canonical forms per spec.md §10.1.

Usage:
    python3 tools/migrate_glyphs.py [--dry-run]

Replacements (繁/異 → 採用):
- 對／对 → 対 (JP shinjitai)
- 時 → 时
- 經 → 経
- 來 → 来
- 選 → 选
- 遠 → 远
- 電 → 电
- 雞 → 鷄
- 將 → 将
- 笔 → 筆 (reverse: do not simplify 筆)
"""
import sys
import re
from pathlib import Path

REPLACEMENTS = [
    ("對", "対"),
    ("对", "対"),
    ("時", "时"),
    ("經", "経"),
    ("來", "来"),
    ("選", "选"),
    ("遠", "远"),
    ("電", "电"),
    ("雞", "鷄"),
    ("將", "将"),
    ("笔", "筆"),
]


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    path = Path(__file__).resolve().parent.parent / "wordlist.js"
    src = path.read_text(encoding="utf-8")

    counts = []
    out = src
    for old, new in REPLACEMENTS:
        n = out.count(old)
        out = out.replace(old, new)
        counts.append((old, new, n))

    print(f"{'DRY RUN' if dry_run else 'APPLY'}: {path}")
    for old, new, n in counts:
        print(f"  {old} → {new}: {n} replacement(s)")
    total = sum(c[2] for c in counts)
    print(f"  total: {total}")

    if not dry_run and total > 0:
        path.write_text(out, encoding="utf-8")
        print("Written.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
