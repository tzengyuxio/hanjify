# Pending Translations

Words encountered in real-world / sample text that are not yet in
`wordlist.js`. When a batch is ready, route through the standard
pipeline: append to `words.txt` → run `process_words.py` (DeepL) →
manually edit `hanjify_translated.csv` → `extract.py`.

The "Suggested Hanji" column is a starting point only; final glyph
selection should follow `docs/spec.md` rules (variant unification,
function-word treatment, etc.).

| English | Suggested Hanji | Encountered in / notes |
| --- | --- | --- |
| bind | 縛 / 結 | "binding together" — verb, connect/tie |
| distant | 遠 / 遥 | adjective, "distant epochs" |
| epoch | 紀元 / 時代 | era / period of time |
| laboratory | 實驗室 | example text 4 ("study … in their laboratory") |
