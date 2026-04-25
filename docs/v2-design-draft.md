# Hanjify V2 Conversion Rules — Design Draft

> Date: 2026-04-06
> Status: Draft — for discussion, not yet implemented

---

## 1. Current Rules (V1) Summary

### Conversion Flow

1. Split input by lines, then by spaces
2. For each word:
   - Convert to lowercase
   - Strip leading `(` and trailing punctuation (`,` `.` `;` `!` `?` `:` `)` and `,"` `."` etc.)
   - Look up in `wordList` dictionary (~4,793 entries)
   - If not found, try stripping suffixes in order: `s`, `ing`, `ed`, `es` (first match wins)
   - Special case: uppercase `"I"` always preserved
3. Found words → `<ruby>漢字<rt>english</rt></ruby>`
4. Not found → pass through as-is

### Strengths

- **Graceful fallback**: Unknown words display as original English — nothing breaks
- **Zero dependencies**: Single HTML file, no build step, no frameworks
- **Ruby annotation**: Natural CJK typography convention, toggleable
- **Mixed-origin characters**: Hanzi from Chinese (simplified + traditional), Japanese kanji, Korean hanja, and archaic forms — feels "organically evolved" rather than tied to one culture

### Weaknesses

- **Only 4 suffix rules**: Many common word forms fail lookup (e.g., `running`, `cities`, `happier`)
- **No spelling restoration**: Doubled consonants (`running` → `runn`), y→ies changes not handled
- **No prefix handling**: `unhappy`, `redo`, `overwork` etc. won't decompose
- **No compound word splitting**: `bookshelf`, `sunshine` fail as single lookups
- **Hardcoded punctuation list**: Misses smart quotes, em-dashes, ellipses
- **Dictionary inconsistency**: Same morpheme may use different Hanzi across related words

---

## 2. V2 Proposed Design

### 2.1 Layered Morphological Analysis

The biggest improvement opportunity. Replace the 4-suffix list with a layered system:

#### Layer 1: Prefix stripping (optional)

Try removing common prefixes and look up the remainder:

```
un-    re-    pre-    dis-    mis-
over-  under- out-    non-
```

If `prefix + remainder` both resolve, display as: `un幸福` (prefix as okurigana before Hanzi).

#### Layer 2: Root lookup (dictionary)

Same as V1 — direct dictionary lookup on the base form.

#### Layer 3: Suffix stripping with spelling restoration

Try suffixes in priority order. Each suffix has restoration rules:

| Suffix | Restoration attempts (in order) |
|--------|-------------------------------|
| `-ies` | → replace with `-y` (cities → city) |
| `-ied` | → replace with `-y` (carried → carry) |
| `-ing` | → (1) remove (2) remove + de-double consonant (running → run) (3) remove + add `e` (making → make) |
| `-ed`  | → (1) remove (2) de-double (stopped → stop) (3) add `e` (loved → love) |
| `-er`  | → (1) remove (2) de-double (bigger → big) (3) add `e` (nicer → nice) |
| `-est` | → same as `-er` logic |
| `-es`  | → remove |
| `-s`   | → remove |
| `-ly`  | → remove |
| `-ful` | → remove |
| `-less`| → remove |
| `-ness`| → remove |
| `-ment`| → remove |
| `-able`/`-ible` | → remove; also try + `e` (lovable → love) |
| `-tion`/`-sion` | → try restoring verb form (creation → create) |
| `-ous` | → remove |

**De-doubling rule**: If the stem ends in a doubled consonant (e.g., `runn`), remove the last character and check if the result is in the dictionary.

**Design constraint**: Try at most 3 restoration variants per suffix. If none match, move to the next suffix. If no suffix works, fall back to original word (as-is display).

### 2.2 Okurigana System (Formalized)

V1 already has an implicit okurigana concept — the stripped suffix appears after the Hanzi. V2 makes this explicit:

- **Hanzi** = semantic root (from dictionary)
- **Okurigana** = grammatical/derivational suffix (English text)

Display examples:

| Input | Root | Okurigana | Display |
|-------|------|-----------|---------|
| running | run=走 | -ing | 走ing |
| carefully | care=注意 | -fully | 注意fully |
| unhappy | happy=幸福 | un- | un幸福 |
| cities | city=都市 | -ies | 都市ies |
| unbelievable | believe=信 | un- + -able | un信able |

For prefix + suffix combinations, both are displayed as okurigana around the Hanzi core.

### 2.3 Compound Word Splitting

When a word is not found in the dictionary, attempt to split it into two known words:

```
Algorithm:
  for i in range(len(word)-1, 2, -1):    # greedy, longest prefix first
    prefix = word[:i]
    suffix = word[i:]
    if prefix in wordList and suffix in wordList:
      return compose(wordList[prefix], wordList[suffix])
```

Examples:
- `bookshelf` → `book`(冊) + `shelf`(棚) → 冊棚
- `sunshine` → `sun`(日) + `shine`(輝) → 日輝
- `doorbell` → `door`(門) + `bell`(鈴) → 門鈴

**Constraint**: Only split into exactly 2 parts. Three-way splits risk false positives.

### 2.4 Punctuation Handling

Replace hardcoded list with regex:

```javascript
const LEADING_PUNCT = /^[("''"\u00BF\u00A1]+/;
const TRAILING_PUNCT = /[,.:;!?)"''"—\u2026\-]+$/;
```

This covers smart quotes, em-dashes, ellipses, and inverted punctuation marks.

### 2.5 Capitalization Strategy

| Pattern | Behavior |
|---------|----------|
| ALL CAPS (e.g., `NASA`, `FBI`) | Skip conversion — treat as proper noun/acronym |
| Title Case (e.g., `The`, `Happy`) | Convert normally, preserve original case in ruby |
| `"I"` (standalone) | Special case — preserve as-is (same as V1) |

### 2.6 Character Selection Philosophy

Carry forward the V1 philosophy:

> "If an English native speaker knew some Hanzi and looked up characters in a dictionary, what would they write?"

Add one new principle:

> **Root consistency**: The same morpheme should use the same Hanzi across all derived forms.

Example of the problem in V1:
- `act` = 演, `action` = 行動, `active` = 活動的 — three different Hanzi bases

V2 principle: If `act` = 演, then `action` should derive from 演 (e.g., 演動), not import a completely different Chinese translation.

This is primarily a **dictionary curation** concern, not a code change. But the improved morphological analysis supports it by reducing the need to manually add every derived form.

---

## 3. Comparison: V1 vs V2

| Aspect | V1 | V2 |
|--------|----|----|
| **Suffix stripping** | 4 suffixes, no spelling restoration | ~15+ suffixes with de-doubling and e-restoration |
| **Prefix handling** | None | 9 common prefixes |
| **Okurigana** | Implicit, only for stripped suffixes | Explicit system for both prefixes and suffixes |
| **Compound words** | Not handled | Greedy 2-way split |
| **Punctuation** | Hardcoded 13 patterns | Regex-based, extensible |
| **Capitalization** | Only `"I"` | ALL CAPS skip + title case preserved in ruby |
| **Dictionary structure** | Flat key-value | Same structure, but root-consistency principle |
| **Fallback** | Original text as-is | **Same** |
| **Architecture** | Single HTML file, no build | **Same** |
| **Ruby display** | `<ruby>` + `<rt>` | **Same** |
| **Character sources** | Mixed CJK origins | **Same philosophy** |

---

## 4. What V2 Does NOT Change

These V1 design decisions are correct and should be preserved:

1. **No build step** — vanilla HTML/CSS/JS
2. **Single-file architecture** — all logic in `index.html` + `wordlist.js`
3. **Graceful degradation** — unknown words pass through unchanged
4. **Ruby annotation** — standard CJK typography
5. **Mixed character origins** — not tied to any single CJK tradition
6. **"Not translation"** — Hanjification preserves English grammar, only substitutes vocabulary
7. **Fun-first** — the goal is enjoyment and guessing, not linguistic perfection

---

## 5. Implementation Priority (If Proceeding)

1. **High impact, moderate effort**: Expanded suffix stripping with spelling restoration
2. **Medium impact, low effort**: Regex punctuation + capitalization strategy
3. **Medium impact, moderate effort**: Compound word splitting
4. **Medium impact, high effort**: Prefix handling (needs okurigana display changes)
5. **Ongoing**: Dictionary root-consistency audit (curation, not code)

---

## 6. Open Questions

- Should the suffix/prefix rules be data-driven (a configuration table) or hardcoded?
- For compound word splitting: should the two Hanzi be joined directly (冊棚) or with a separator?
- How should prefix okurigana be rendered differently from suffix okurigana in the ruby display?
- Should there be an "advanced mode" toggle for users who want to see the morphological breakdown?
