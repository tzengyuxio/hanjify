# HANJIFY — 英语汉字化工具

[English](README.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

**HANJIFY** 将英文文本转换为汉字表示——就像"罗马拼音"的反向操作。

🔗 **在线体验：** [hanjify.tzengyuxio.me](https://hanjify.tzengyuxio.me)

## 功能介绍

输入英文文字，HANJIFY 会将已知的单词替换为对应的汉字，并以 ruby 标注显示原文：

```
输入：The little prince lived on a small planet.
输出：其 小 王子 活于 上 一 小 行星。
     （汉字上方以小字显示原始英文）
```

## 特色功能

- **实时转换** — 内置约 4,800 组英汉对照词汇
- **Ruby 标注** — 可切换显示或隐藏汉字上方的英文原文
- **多语言界面** — 支持英文、繁体中文、简体中文、日文
- **截图导出** — 将转换结果截取为 PNG 图片（含水印）
- **示例文本** — 内置示例文字，一键试用

## 运作原理

1. 每个英文单词会在词汇对照表（`wordlist.js`）中查询
2. 若有对应汉字，以 `<ruby>` 标签包裹替换
3. 若查无结果，会去除常见词尾（s、ed、ing 等）后重试
4. 无法对应的单词保持原样显示

## 转换规范

转换规则定义于 [`docs/spec.md`](docs/spec.md)——本工具的 single source of truth，涵盖功能词对照、形态学规则、字形采用、冲突避歧与边界情境。本网页工具与 [Claude Code `hanjify` skill](https://github.com/tzengyuxio/skills/tree/main/hanjify) 同样依此规范实作。

## 本地运行

```bash
# 使用任意静态文件服务器
python3 -m http.server 8000
# 打开 http://localhost:8000
```

不需要构建工具，没有包依赖——纯静态 HTML/CSS/JS。

## 数据处理流程

词汇表通过 Python 脚本维护：

| 脚本 | 用途 |
|------|------|
| `simple.py` | 从 Wikipedia/Wiktionary 获取单词列表 |
| `process_words.py` | 通过 DeepL API 批量翻译 |
| `extract.py` | 将 CSV 转换为 `wordlist.js` |

重新生成词汇表：
```bash
python3 extract.py
```

## 技术架构

- 原生 HTML / CSS / JavaScript（无框架）
- Python 数据处理脚本
- GitHub Pages 静态托管
- dom-to-image 截图功能

## 许可证

MIT 许可证——详见 [LICENSE](LICENSE)。

## 作者

[Tzeng Yuxio](https://github.com/tzengyuxio)
