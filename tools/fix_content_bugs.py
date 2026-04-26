#!/usr/bin/env python3
"""Fix obvious content-word bugs in wordlist.js (mistranslations / weird mappings).

Out of scope: full §10.4 derivational re-audit.
This is a surgical fix for words that show up in common test text.

Usage:
    python3 tools/fix_content_bugs.py [--dry-run]
"""
import re
import sys
from pathlib import Path

# (key, current-buggy-value, corrected-value)
FIXES = [
    # Verbs
    ("ask", "請", "問"),                    # 請 = please/invite, not "ask"
    ("asked", "灰", "問ed"),                # 灰 = ash, nonsense
    ("walk", "行", "歩"),                   # 行 conflicts with go; walk = 歩
    ("walked", None, "歩ed"),               # was missing
    ("told", "我告訴", "告t"),              # literal "I tell" — irregular past
    ("wonder", "驚疑", "想"),               # 想 better fits "wonder"
    ("smiled", None, "笑ed"),               # was missing; smile → 笑顔 → smile→笑+ed
    # Nouns
    ("word", "變成", "詞"),                 # 變成 = become, unrelated
    ("present", "禮品", "現在"),            # 禮品 = gift; "present" mostly = current
    ("green", "綠化", "緑"),                # 綠化 = greenify; just 緑
    ("sky", None, "天"),                    # was missing
    ("sunshine", None, "日光"),             # was missing
    # Adverbs
    ("quietly", None, "静地"),              # was missing; quiet→安靜 + ly→地
    # More verbs
    ("think", "想思", "思"),                # spec M3 root for thought→思t
    ("thinks", None, "思s"),                # was missing
    ("passes", "通行证", "通過es"),         # 通行证 = passport, totally wrong
    ("passed", "合格", "通過ed"),           # 合格 = passed exam
]


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    path = Path(__file__).resolve().parent.parent / "wordlist.js"
    src = path.read_text(encoding="utf-8")
    out = src

    fixed = []
    added = []
    skipped = []

    for key, expected_current, target in FIXES:
        pattern = rf'("{re.escape(key)}":\s*)"([^"]*)"'
        m = re.search(pattern, out)
        if m:
            current = m.group(2)
            if current == target:
                skipped.append((key, "already correct"))
                continue
            if expected_current is not None and current != expected_current:
                skipped.append((key, f"unexpected current value: {current!r} (expected {expected_current!r})"))
                continue
            out = re.sub(pattern, lambda mm, t=target: f'{mm.group(1)}"{t}"', out, count=1)
            fixed.append((key, current, target))
        else:
            if expected_current is not None:
                skipped.append((key, "key not found, but expected to update"))
                continue
            # Insert new entry just before the closing `\n};`
            m2 = re.search(r'\n};\s*\Z', out)
            if not m2:
                print(f"ERROR: cannot find closing brace for adding {key!r}", file=sys.stderr)
                return 1
            new_entry = f'\n  "{key}": "{target}",'
            out = out[: m2.start()] + new_entry + out[m2.start():]
            added.append((key, target))

    print(f"{'DRY RUN' if dry_run else 'APPLY'}: {path}")
    print(f"  Fixed: {len(fixed)}")
    for k, c, t in fixed:
        print(f"    {k!r}: {c!r} → {t!r}")
    print(f"  Added: {len(added)}")
    for k, t in added:
        print(f"    {k!r}: {t!r}")
    print(f"  Skipped: {len(skipped)}")
    for k, reason in skipped:
        print(f"    {k!r}: {reason}")

    if not dry_run and (fixed or added):
        path.write_text(out, encoding="utf-8")
        print("\nWritten.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
