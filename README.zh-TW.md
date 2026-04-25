# HANJIFY — 英語漢字化工具

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

**HANJIFY** 將英文文本轉換為漢字表示——就像「羅馬拼音」的反向操作。

🔗 **線上體驗：** [hanjify.tzengyuxio.me](https://hanjify.tzengyuxio.me)

## 功能介紹

輸入英文文字，HANJIFY 會將已知的單字替換為對應的漢字，並以 ruby 標註顯示原文：

```
輸入：The little prince lived on a small planet.
輸出：其 小 王子 活於 上 一 小 行星。
     （漢字上方以小字顯示原始英文）
```

## 特色功能

- **即時轉換** — 內建約 4,800 組英漢對照詞彙
- **Ruby 標註** — 可切換顯示或隱藏漢字上方的英文原文
- **多語言介面** — 支援英文、繁體中文、簡體中文、日文
- **截圖匯出** — 將轉換結果擷取為 PNG 圖片（含浮水印）
- **範例文本** — 內建範例文字，一鍵試用

## 運作原理

1. 每個英文單字會在詞彙對照表（`wordlist.js`）中查詢
2. 若有對應漢字，以 `<ruby>` 標籤包裹替換
3. 若查無結果，會去除常見字尾（s、ed、ing 等）後重試
4. 無法對應的單字維持原樣顯示

## 轉換規範

轉換規則定義於 [`docs/spec.md`](docs/spec.md)——本工具的 single source of truth，涵蓋功能詞對照、形態學規則、字形採用、衝突避歧與邊界情境。本網頁工具與 [Claude Code `hanjify` skill](https://github.com/tzengyuxio/skills/tree/main/hanjify) 同樣依此規範實作。

## 本地執行

```bash
# 使用任意靜態檔案伺服器
python3 -m http.server 8000
# 開啟 http://localhost:8000
```

不需要建置工具，沒有套件依賴——純靜態 HTML/CSS/JS。

## 資料處理流程

詞彙表透過 Python 腳本維護：

| 腳本 | 用途 |
|------|------|
| `simple.py` | 從 Wikipedia/Wiktionary 取得單字列表 |
| `process_words.py` | 透過 DeepL API 批次翻譯 |
| `extract.py` | 將 CSV 轉換為 `wordlist.js` |

重新產生詞彙表：
```bash
python3 extract.py
```

## 技術架構

- 原生 HTML / CSS / JavaScript（無框架）
- Python 資料處理腳本
- GitHub Pages 靜態託管
- dom-to-image 截圖功能

## 授權

MIT 授權條款——詳見 [LICENSE](LICENSE)。

## 作者

[Tzeng Yuxio](https://github.com/tzengyuxio)
