#!/usr/bin/env python3
"""Audit and re-align derivational wordlist entries per spec.md §M2b/M2c.

Identifies wordlist entries with derivational suffixes/prefixes whose
current value diverges from what the spec rule would produce, then:
- Writes a report to docs/derivation-audit.md
- Auto-applies HIGH-confidence changes to wordlist.js
- Leaves MEDIUM/LOW for human review

Confidence levels:
- HIGH: simple suffix/prefix strip yields a root in wordlist; current value
  diverges from `root_hanzi + suffix_hanzi`. Apply rule strictly.
- MEDIUM: root needs morphological variation (i→y, +e); apply if found.
- LOW: root not in wordlist or current is plausibly idiomatic; skip.

Usage:
    python3 tools/audit_derivations.py [--dry-run] [--report-only]
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

# ---------------- Spec rules ----------------

# M2b derivational suffixes -> Hanzi
# Order matters: longest first to avoid -al matching -tion etc.
SUFFIX_MAP_ORDERED = [
    ("ician", "師"),       # musician
    ("ance", None),        # no rule (依 wordlist)
    ("ancy", None),
    ("ment", None),
    ("ness", None),
    ("tion", None),
    ("sion", None),
    ("less", "_LESS"),     # special: 无...的
    ("able", "的"),
    ("ible", "的"),
    ("eer", "師"),
    ("ous", "的"),
    ("ive", "的"),
    ("ful", "的"),
    ("ize", "化"),
    ("ise", "化"),
    ("ly", "地"),
    ("er", "者"),
    ("or", "者"),
    ("ar", "者"),
    ("al", "的"),
    ("ee", "受"),
    ("ess", "者"),
    ("man", "人"),
    ("ist", "家"),
    ("fy", "化"),
    # Compound pronouns/adverbs (treated as suffix)
    ("thing", "物"),
    ("body", "体"),
    ("where", "処"),
    ("one", "一"),
]

# M2c prefixes -> Hanzi (longest first)
# Note: `every-` uses 每 (per C2 議題 in §3.11; spec.md M2c example says 毎 — inconsistency to be fixed)
PREFIX_MAP_ORDERED = [
    ("every", "每"),
    ("some", "某"),
    ("non", "非"),
    ("any", "任"),
    ("un", "不"),
    ("re", "再"),
    ("no", "无"),
]

# Words that should be skipped entirely (function words, very short, etc.)
SKIP_WORDS = {
    # Don't-convert list
    "a", "an", "the", "of", "in", "to", "on", "at",
    # Don't audit pronouns/possessives we already set canonically
    "I", "you", "he", "she", "it", "we", "they",
    "me", "him", "her", "us", "them",
    "my", "your", "his", "its", "our", "their", "mine", "yours",
    "myself", "yourself", "himself", "herself", "itself",
    "ourselves", "yourselves", "themselves",
    "who", "whom", "whose", "what", "which", "where",
    "when", "why", "how", "this", "that", "these", "those",
    "for", "with", "from", "by", "about", "around", "into",
    "through", "between", "under", "over", "after", "before",
    "without", "during", "against", "among",
    "and", "or", "but", "because", "if", "while", "although",
    "so", "than", "as", "unless", "whether",
    "is", "am", "are", "was", "were", "been", "being",
    "have", "has", "had", "do", "does", "did",
    "can", "could", "will", "would", "should",
    "may", "might", "must", "shall",
    "not", "no", "nor", "never", "none", "neither",
    "very", "also", "too", "only", "just", "all", "still",
    "already", "always", "often", "some", "many", "much",
    "every", "each", "other", "another", "same", "such",
    "yes", "here", "there", "then", "now", "again", "soon",
    "yet", "perhaps", "together", "almost", "enough", "quite",
}

# ---------------- Helpers ----------------

def parse_wordlist(src: str) -> dict[str, str]:
    m = re.search(r"\{(.*)\}", src, re.S)
    body = m.group(1)
    return dict(re.findall(r'"([^"]+)":\s*"([^"]+)"', body))


def root_candidates_for_suffix(word: str, suffix: str) -> list[str]:
    """Plausible root forms after stripping the suffix."""
    base = word[: -len(suffix)]
    cands = [base]
    # `i` ↔ `y` (happily → happy, beautiful → beauty)
    if base.endswith("i"):
        cands.append(base[:-1] + "y")
    # `e` lost (lovable → love, sizable → size)
    if not base.endswith("e"):
        cands.append(base + "e")
    # double consonant (rare for derivational, but covers 'happiness'-style)
    if len(base) >= 2 and base[-1] == base[-2]:
        cands.append(base[:-1])
    return cands


def root_candidates_for_prefix(word: str, prefix: str) -> list[str]:
    """Plausible root forms after stripping the prefix."""
    return [word[len(prefix):]]


def expected_value(root_hanzi: str, suffix_hanzi: str) -> str:
    if suffix_hanzi == "_LESS":
        return f"无{root_hanzi}的"
    return f"{root_hanzi}{suffix_hanzi}"


def expected_prefix_value(prefix_hanzi: str, root_hanzi: str) -> str:
    return f"{prefix_hanzi}{root_hanzi}"


# ---------------- Audit ----------------

def classify_safety(current: str, expected: str, suffix: str = "") -> str:
    """Decide whether current → expected is a SAFE auto-apply.

    SAFE: strict — same length, exactly one trailing-char difference.
      Catches 教師→教者, 操作員→操作者, 一般的→一般地, etc.
    LIKELY: share substantial overlap (≥ 50%) but length differs.
    UNCERTAIN: minimal overlap; very likely a false positive (skip).

    Comparative-suffix guard: for -er/-or/-ar, if current contains 更 (more)
    or expected[-1] === 者 with current having no agentive marker,
    classify as LIKELY/UNCERTAIN instead of SAFE — these are
    likely comparatives (M2a) misclassified as agentives (M2b).
    """
    if current == expected:
        return "OK"

    # Comparative guard: -er/-or/-ar with 更 in current is a comparative
    if suffix in ("er", "or", "ar") and "更" in current:
        return "UNCERTAIN"

    # SAFE: strict same-length single-char swap
    if len(current) == len(expected) and current[:-1] == expected[:-1]:
        # For agentive suffixes, last char should be one of: 者/師/員/家/人/手/工/生/係/夫/士
        # If current's last char is none of these, the case is suspicious
        if suffix in ("er", "or", "ar", "ist", "ician", "eer", "man", "ee", "ess"):
            agentive_chars = set("者師員家人手工生係夫士役")
            if current[-1] not in agentive_chars:
                return "LIKELY"
        return "SAFE"

    # 无…的 special form
    if expected.startswith("无") and expected.endswith("的"):
        inner = expected[1:-1]
        if current == inner + "的":
            return "SAFE"

    # Substring containment: similar but length-differing
    common_chars = set(current) & set(expected)
    if not common_chars:
        return "UNCERTAIN"
    overlap = sum(1 for c in current if c in common_chars) / max(len(current), len(expected))
    if overlap >= 0.5:
        return "LIKELY"
    return "UNCERTAIN"


def audit_suffixes(wl: dict[str, str]):
    """Returns list of (word, current, expected, root, suffix, suffix_hanzi, confidence)."""
    results = []
    for word, current in wl.items():
        if word in SKIP_WORDS:
            continue
        if word.startswith('"') or "'" in word:
            continue
        for suffix, suffix_hanzi in SUFFIX_MAP_ORDERED:
            if not word.endswith(suffix):
                continue
            if len(word) <= len(suffix) + 1:
                continue
            if suffix_hanzi is None:
                continue  # no-rule suffix
            for cand in root_candidates_for_suffix(word, suffix):
                if cand in SKIP_WORDS:
                    continue
                if cand in wl:
                    root_hanzi = wl[cand]
                    if not root_hanzi:
                        continue
                    expected = expected_value(root_hanzi, suffix_hanzi)
                    confidence = classify_safety(current, expected, suffix)
                    results.append((word, current, expected, cand, suffix, suffix_hanzi, confidence))
                    break
            else:
                continue
            break
    return results


def audit_prefixes(wl: dict[str, str]):
    """Returns list of (word, current, expected, root, prefix, prefix_hanzi, confidence)."""
    results = []
    for word, current in wl.items():
        if word in SKIP_WORDS:
            continue
        for prefix, prefix_hanzi in PREFIX_MAP_ORDERED:
            if not word.startswith(prefix):
                continue
            if len(word) <= len(prefix) + 2:
                continue
            for cand in root_candidates_for_prefix(word, prefix):
                if cand in SKIP_WORDS:
                    continue
                if cand in wl:
                    root_hanzi = wl[cand]
                    if not root_hanzi:
                        continue
                    expected = expected_prefix_value(prefix_hanzi, root_hanzi)
                    confidence = classify_safety(current, expected)
                    results.append((word, current, expected, cand, prefix, prefix_hanzi, confidence))
                    break
            else:
                continue
            break
    return results


# ---------------- Apply ----------------

def apply_changes(src: str, changes: list[tuple[str, str, str]]) -> str:
    """changes: list of (word, current, new). Returns updated src."""
    out = src
    for word, current, new in changes:
        pattern = rf'("{re.escape(word)}":\s*)"{re.escape(current)}"'
        new_text = re.sub(pattern, lambda m, n=new: f'{m.group(1)}"{n}"', out, count=1)
        if new_text == out:
            print(f"  WARN: failed to replace {word!r} (expected current {current!r})", file=sys.stderr)
        out = new_text
    return out


# ---------------- Report ----------------

def write_report(suffix_results, prefix_results, applied: list, report_path: Path):
    lines = []
    lines.append("# Wordlist 派生詞重審報告")
    lines.append("")
    lines.append("> 來源：`tools/audit_derivations.py` 對 wordlist.js 跑過一次 spec §M2b/§M2c 規則對照")
    lines.append("")
    lines.append("## 摘要")
    lines.append("")

    # Suffix stats
    by_conf = {"OK": 0, "SAFE": 0, "LIKELY": 0, "UNCERTAIN": 0}
    for r in suffix_results:
        by_conf[r[6]] = by_conf.get(r[6], 0) + 1
    lines.append(f"### Suffix 後綴 (M2b)")
    lines.append(f"- 總候選：{len(suffix_results)}")
    lines.append(f"- OK（已合規）：{by_conf['OK']}")
    lines.append(f"- SAFE（單字元差異，自動套用）：{by_conf['SAFE']}")
    lines.append(f"- LIKELY（部分重疊，需審視）：{by_conf['LIKELY']}")
    lines.append(f"- UNCERTAIN（差異大，跳過）：{by_conf['UNCERTAIN']}")
    lines.append("")

    by_conf_p = {"OK": 0, "SAFE": 0, "LIKELY": 0, "UNCERTAIN": 0}
    for r in prefix_results:
        by_conf_p[r[6]] = by_conf_p.get(r[6], 0) + 1
    lines.append(f"### Prefix 前綴 (M2c)")
    lines.append(f"- 總候選：{len(prefix_results)}")
    lines.append(f"- OK（已合規）：{by_conf_p['OK']}")
    lines.append(f"- SAFE（自動套用）：{by_conf_p['SAFE']}")
    lines.append(f"- LIKELY（部分重疊，需審視）：{by_conf_p['LIKELY']}")
    lines.append(f"- UNCERTAIN（差異大，跳過）：{by_conf_p['UNCERTAIN']}")
    lines.append("")

    lines.append(f"## 自動套用變更（共 {len(applied)} 條）")
    lines.append("")
    if applied:
        lines.append("| 英文 | 原 | 改為 | 規則 |")
        lines.append("|---|---|---|---|")
        for word, current, new, rule in applied[:200]:
            lines.append(f"| `{word}` | {current} | {new} | {rule} |")
        if len(applied) > 200:
            lines.append(f"| ... | ... | ... | (and {len(applied) - 200} more) |")
    lines.append("")

    # LIKELY (manual review needed)
    likely = [r for r in suffix_results + prefix_results if r[6] == "LIKELY"]
    lines.append(f"## LIKELY 候選（{len(likely)} 條，需人工裁定）")
    lines.append("")
    if likely:
        lines.append("LIKELY 表示 current 與 expected 有顯著重疊（共字 ≥ 50%）但非單字元差異。")
        lines.append("可能是：(a) 慣用 CJK 複合詞（M2d 應保留）、(b) 應該手工調整、(c) 詞典 bug")
        lines.append("")
        lines.append("| 英文 | 原 | 提議 | root | 後綴／前綴 |")
        lines.append("|---|---|---|---|---|")
        for tup in likely[:100]:
            word, current, expected, root, sfx, _, _ = tup
            lines.append(f"| `{word}` | {current} | {expected} | `{root}` | `{sfx}` |")
        if len(likely) > 100:
            lines.append(f"| ... | ... | ... | ... | (and {len(likely) - 100} more) |")
    lines.append("")

    # UNCERTAIN (skipped — for visibility only)
    uncertain = [r for r in suffix_results + prefix_results if r[6] == "UNCERTAIN"]
    lines.append(f"## UNCERTAIN 候選（{len(uncertain)} 條，已跳過，僅供參考）")
    lines.append("")
    if uncertain:
        lines.append("UNCERTAIN 多為 false positive（如 corner→玉米者、dollar→娃娃者：英文詞尾形式碰巧匹配 suffix，但語意無關）。")
        lines.append("")
        lines.append("| 英文 | 原 | 提議（已跳過）|")
        lines.append("|---|---|---|")
        for tup in uncertain[:50]:
            word, current, expected, _, _, _, _ = tup
            lines.append(f"| `{word}` | {current} | {expected} |")
        if len(uncertain) > 50:
            lines.append(f"| ... | ... | (and {len(uncertain) - 50} more) |")
    lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")


# ---------------- Main ----------------

def main() -> int:
    dry_run = "--dry-run" in sys.argv
    report_only = "--report-only" in sys.argv

    repo = Path(__file__).resolve().parent.parent
    wl_path = repo / "wordlist.js"
    report_path = repo / "docs" / "derivation-audit.md"
    src = wl_path.read_text(encoding="utf-8")
    wl = parse_wordlist(src)

    print(f"Loaded {len(wl)} entries from {wl_path}")

    suffix_results = audit_suffixes(wl)
    prefix_results = audit_prefixes(wl)

    print(f"Suffix candidates: {len(suffix_results)}")
    print(f"Prefix candidates: {len(prefix_results)}")

    # Auto-apply: only SAFE classification (single-char swap or near-trivial difference)
    high_changes = []
    for w, cur, exp, root, suf, sh, conf in suffix_results:
        if conf == "SAFE":
            high_changes.append((w, cur, exp, f"-{suf} → {sh if sh != '_LESS' else '无…的'}"))
    for w, cur, exp, root, pre, ph, conf in prefix_results:
        if conf == "SAFE":
            high_changes.append((w, cur, exp, f"{pre}- → {ph}"))

    print(f"Will apply: {len(high_changes)} changes")

    if not report_only and not dry_run:
        new_src = apply_changes(src, [(w, c, n) for w, c, n, _ in high_changes])
        wl_path.write_text(new_src, encoding="utf-8")
        print(f"Updated {wl_path}")

    write_report(suffix_results, prefix_results, high_changes, report_path)
    print(f"Report written to {report_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
