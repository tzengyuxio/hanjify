# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

HANJIFY is a static web tool that converts English text into Hanzi (Chinese character) representation — a reverse "Romanization" concept. Live at https://hanjify.tzengyuxio.me.

## Architecture

Single-page application with no build step:

- **`index.html`** — All HTML, CSS, and JS in one file. Contains the i18n system, text conversion logic, screenshot feature, and UI.
- **`wordlist.js`** — ~4,800 English-to-Hanzi mappings as a JS object (`const wordList = {...}`). Generated from CSV by `extract.py`.
- **Python scripts** — Data pipeline for maintaining the word list:
  - `simple.py` — Fetches word lists from Wikipedia/Wiktionary, maps to frequency data
  - `process_words.py` — Batch translation via DeepL API
  - `extract.py` — Converts CSV (`hanjify_translated.csv`) to `wordlist.js`

## Running Locally

```bash
python3 -m http.server 8000
# Visit http://localhost:8000
```

No build, no dependencies, no package manager. Just serve static files.

## Deployment

GitHub Actions (`.github/workflows/deploy.yml`) auto-deploys to GitHub Pages on push to `main`. Custom domain via `CNAME`.

## Core Conversion Algorithm

In `index.html`, the conversion:
1. Splits input by lines and spaces
2. Strips punctuation and parentheses from each word
3. Tries dictionary lookup; if not found, strips common suffixes (`s`, `ing`, `ed`, `es`, etc.)
4. Found words render as `<ruby>漢字<rt>english</rt></ruby>`; unfound words pass through as-is
5. Special case: uppercase `"I"` preserved

## i18n System

Hard-coded `languages` object with 4 locales: `en`, `zh_tw`, `zh_cn`, `ja`. Language selected via `?lang=` URL parameter or UI buttons. All UI strings including FAQ content are in this object.

## Regenerating wordlist.js

```bash
python3 extract.py
```

Reads `hanjify_translated.csv`, outputs `wordlist.js`. Backs up existing file automatically.

## Key Conventions

- The project is intentionally minimal — vanilla HTML/CSS/JS, no frameworks
- Code comments are in Traditional Chinese
- `wordlist.js` should only be regenerated via `extract.py`, not hand-edited (except small additions)
- `og-image.png` is the OpenGraph preview image for social sharing
