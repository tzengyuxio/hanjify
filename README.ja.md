# HANJIFY — 英語漢字化ツール

[English](README.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh-CN.md) | [한국어](README.ko.md)

**HANJIFY** は英語テキストを漢字表記に変換するツールです——ローマ字化の逆バージョンです。

🔗 **デモサイト：** [hanjify.tzengyuxio.me](https://hanjify.tzengyuxio.me)

## 機能紹介

英語テキストを入力すると、HANJIFY が既知の単語を対応する漢字に置き換え、ルビで原文を表示します：

```
入力：The little prince lived on a small planet.
出力：其 小 王子 活於 上 一 小 行星。
     （漢字の上にルビで元の英語を表示）
```

## 主な機能

- **リアルタイム変換** — 約4,800語の英漢対照辞書を内蔵
- **ルビ表示** — 漢字上部の英語原文の表示/非表示を切り替え可能
- **多言語UI** — 英語、繁体字中国語、簡体字中国語、日本語に対応
- **スクリーンショット** — 変換結果をPNG画像として保存（透かし付き）
- **サンプルテキスト** — 内蔵のサンプルですぐにお試し可能

## 仕組み

1. 各英単語を辞書（`wordlist.js`）で検索
2. 対応する漢字がある場合、`<ruby>` タグで置換
3. 見つからない場合、一般的な接尾辞（s、ed、ing など）を除去して再検索
4. 対応できない単語はそのまま表示

## 変換仕様

変換ルールは [`docs/spec.md`](docs/spec.md) に定義されています——本ツールの single source of truth であり、機能語対応、形態素ルール、字形採用、衝突回避、境界事例を網羅しています。本ウェブツールと [Claude Code `hanjify` skill](https://github.com/tzengyuxio/skills/tree/main/hanjify) は同じ仕様を実装しています。

## ローカル実行

```bash
# 任意の静的ファイルサーバーを使用
python3 -m http.server 8000
# http://localhost:8000 を開く
```

ビルドツール不要、依存パッケージなし——純粋な静的 HTML/CSS/JS です。

## データパイプライン

辞書データは Python スクリプトで管理：

| スクリプト | 用途 |
|-----------|------|
| `simple.py` | Wikipedia/Wiktionary から単語リストを取得 |
| `process_words.py` | DeepL API で一括翻訳 |
| `extract.py` | CSV を `wordlist.js` に変換 |

辞書の再生成：
```bash
python3 extract.py
```

## 技術スタック

- 素の HTML / CSS / JavaScript（フレームワークなし）
- Python データ処理スクリプト
- GitHub Pages でホスティング
- dom-to-image でスクリーンショット生成

## ライセンス

MIT ライセンス——詳細は [LICENSE](LICENSE) を参照。

## 作者

[Tzeng Yuxio](https://github.com/tzengyuxio)
