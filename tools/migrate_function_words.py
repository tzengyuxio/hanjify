#!/usr/bin/env python3
"""Update wordlist.js function words to spec.md §3 canonical values.

For each entry in SPEC_FUNCTION_WORDS:
- if key exists in wordlist: replace value
- if key absent: append entry just before the closing brace

Excluded keys (per §3.13 不轉清單): a, an, the, of, in, to, on, at —
these stay out of wordlist; web tool keeps them as English.

Usage:
    python3 tools/migrate_function_words.py [--dry-run]
"""
import re
import sys
from pathlib import Path

# Function word -> canonical hanzi value, per spec.md §3
SPEC_FUNCTION_WORDS = {
    # §3.2 Personal Pronouns
    "I": "予",
    "me": "予",
    "you": "尔",
    "he": "彼",
    "him": "彼",
    "she": "伊",
    "her": "伊",
    "it": "它",
    "we": "吾等",
    "us": "吾等",
    "they": "彼等",
    "them": "彼等",
    # §3.3 Possessive
    "my": "予之",
    "your": "尔之",
    "his": "彼之",
    "its": "它之",
    "our": "吾等之",
    "their": "彼等之",
    "mine": "予之",
    "yours": "尔之",
    # §3.4 Reflexive
    "myself": "予自",
    "yourself": "尔自",
    "himself": "彼自",
    "herself": "伊自",
    "itself": "它自",
    "ourselves": "吾等自",
    "yourselves": "尔等自",
    "themselves": "彼等自",
    # §3.5 Interrogative & Relative
    "who": "誰",
    "whom": "誰",
    "what": "何",
    "where": "何処",
    "why": "何故",
    "how": "如何",
    "whose": "誰之",
    "when": "当",  # default conjunction; heuristic switches to 何時
    "which": "其中",  # default relative; heuristic switches to 何
    # §3.6 Demonstrative
    "this": "這",
    "that": "那",
    "these": "這等",
    "those": "那等",
    # §3.7 Prepositions (omits 不轉清單 of/in/to/on/at)
    "for": "為",
    "with": "与",
    "from": "从",
    "by": "以",
    "about": "関於",
    "around": "周辺",
    "into": "入",
    "through": "経",
    "between": "間",
    "under": "下於",
    "over": "上於",
    "after": "後",
    "before": "前",
    "without": "不与",
    "during": "間",
    "against": "反対",
    "among": "其中",
    # §3.8 Conjunctions
    "and": "与",
    "or": "或",
    "but": "但",
    "because": "因為",
    "if": "若",
    "while": "正当",
    "although": "雖然",
    "so": "故",
    "than": "於",
    "as": "如",
    "unless": "除非",
    "whether": "是否",
    # §3.9 Auxiliary verbs
    "is": "是",
    "am": "是",
    "are": "是",
    "was": "是ed",
    "were": "是ed",
    "been": "是t",
    "being": "是ing",
    "have": "有",
    "has": "有",
    "had": "有ed",
    "do": "行",
    "does": "行",
    "did": "行ed",
    "can": "能",
    "could": "能ed",
    "will": "将",
    "would": "将ed",
    "should": "応",
    "may": "可",
    "might": "可ed",
    "must": "須",
    "shall": "宜",
    # §3.10 Negation
    "not": "不",
    "no": "无",
    "nor": "亦不",
    "never": "从不",
    "none": "无一",
    "neither": "亦不",
    # §3.11 Common Adverbs & Determiners
    "very": "甚",
    "also": "亦",
    "too": "亦",
    "only": "唯一",
    "just": "僅",
    "all": "全",
    "still": "仍",
    "already": "既",
    "always": "始終",
    "often": "常常",
    "some": "某",
    "many": "多",
    "much": "多",
    "every": "每",
    "each": "各",
    "other": "其他",
    "another": "另",
    "same": "相樣",
    "such": "如此",
    "yes": "是",
    "here": "此処",
    "there": "彼処",
    "then": "則",
    "now": "今",
    "again": "再",
    "soon": "不久",
    "yet": "卻",
    "perhaps": "或許",
    "together": "共集",
    "almost": "幾乎",
    "enough": "足夠",
    "quite": "頗為",
}


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    path = Path(__file__).resolve().parent.parent / "wordlist.js"
    src = path.read_text(encoding="utf-8")

    updated = []
    added = []
    unchanged = []
    out = src

    # Update or mark-for-add
    for key, target in SPEC_FUNCTION_WORDS.items():
        # Match `"key": "value",` or with optional trailing comma
        # Be careful to escape special chars in key (none expected)
        pattern = rf'("{re.escape(key)}":\s*)"([^"]*)"'
        m = re.search(pattern, out)
        if m:
            current = m.group(2)
            if current == target:
                unchanged.append(key)
            else:
                out = re.sub(pattern, lambda mm, t=target: f'{mm.group(1)}"{t}"', out, count=1)
                updated.append((key, current, target))
        else:
            added.append((key, target))

    # Append new entries before the closing `};`
    if added:
        # Build insertion text
        new_lines = "\n".join(f'  "{k}": "{v}",' for k, v in added)
        # Insert before the last `}` which closes the object
        # Match the last entry line that has trailing comma OR no comma + closing }
        # Strategy: find `}` near end, insert before it
        # The format ends like: `"heisei": "平成"\n};`
        # We need to add a comma after that final entry.
        m = re.search(r'(\n)([^"]*"[^"]+"\s*:\s*"[^"]*")\s*(\n};)\s*\Z', out)
        if not m:
            print("ERROR: cannot find tail pattern in wordlist.js", file=sys.stderr)
            return 1
        # Add trailing comma to existing last entry, then new entries, then close
        new_tail = f"{m.group(1)}{m.group(2)},\n{new_lines}\n}};"
        out = out[:m.start()] + new_tail
        if not out.endswith("\n"):
            out += "\n"

    print(f"{'DRY RUN' if dry_run else 'APPLY'}: {path}")
    print(f"  Total spec entries: {len(SPEC_FUNCTION_WORDS)}")
    print(f"  Unchanged (already correct): {len(unchanged)}")
    print(f"  Updated: {len(updated)}")
    print(f"  Added: {len(added)}")
    if updated:
        print("\n  Updated entries (first 20):")
        for k, c, t in updated[:20]:
            print(f"    {k!r}: {c!r} → {t!r}")
        if len(updated) > 20:
            print(f"    ... and {len(updated) - 20} more")
    if added:
        print(f"\n  Added entries (first 20):")
        for k, t in added[:20]:
            print(f"    {k!r}: {t!r}")
        if len(added) > 20:
            print(f"    ... and {len(added) - 20} more")

    if not dry_run and (updated or added):
        path.write_text(out, encoding="utf-8")
        print("\nWritten.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
