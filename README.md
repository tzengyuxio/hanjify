# HANJIFY — English Hanjification Tool

[繁體中文](README.zh-TW.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

**HANJIFY** converts English text into Chinese character (Hanzi) representation — like Romanization, but in reverse.

🔗 **Live Demo:** [hanjify.tzengyuxio.me](https://hanjify.tzengyuxio.me)

## What It Does

Enter English text, and HANJIFY replaces known words with their Hanzi equivalents using ruby annotations:

```
Input:  The little prince lived on a small planet.
Output: 其 小 王子 活於 上 一 小 行星。
        (with ruby text showing original English above each character)
```

## Features

- **Real-time conversion** with a dictionary of ~4,800 word mappings
- **Ruby text annotations** — toggle to show/hide original English above Hanzi
- **Multi-language UI** — English, Traditional Chinese, Simplified Chinese, Japanese
- **Screenshot export** — capture output as PNG with watermark
- **Example texts** — built-in samples to try instantly

## How It Works

1. Each English word is looked up in a curated dictionary (`wordlist.js`)
2. If found, the word is replaced with its Hanzi equivalent wrapped in `<ruby>` tags
3. If not found, common suffixes (s, ed, ing, etc.) are stripped and retried
4. Unmatched words pass through unchanged

## Running Locally

```bash
# Serve with any static file server
python3 -m http.server 8000
# Then visit http://localhost:8000
```

No build tools, no dependencies — just static HTML/CSS/JS.

## Data Pipeline

The word list is maintained through Python scripts:

| Script | Purpose |
|--------|---------|
| `simple.py` | Fetch word lists from Wikipedia/Wiktionary |
| `process_words.py` | Batch translate via DeepL API |
| `extract.py` | Convert CSV to `wordlist.js` |

To regenerate the word list:
```bash
python3 extract.py
```

## Tech Stack

- Vanilla HTML / CSS / JavaScript (no frameworks)
- Python for data processing
- GitHub Pages for hosting
- dom-to-image for screenshot generation

## License

MIT License — see [LICENSE](LICENSE) for details.

## Author

[Tzeng Yuxio](https://github.com/tzengyuxio)
