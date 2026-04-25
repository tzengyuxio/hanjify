# Hanjify 規範草案 — 裁定表

> 日期：2026-04-26
> 狀態：草案 — 等待使用者裁定後凍結為 `spec.md`
> 範圍：本檔為**規範草案**，待逐項裁定完成後，將凍結成 `docs/spec.md`，作為 web tool 與 Claude Code skill 的 single source of truth。

---

## 0. 前言

### 0.1 規範目的

統一 `~/works/hanjify/`（網頁工具）與 `~/works/skills/hanjify/`（Claude Code skill）兩邊的轉換規則，避免同一輸入在兩處產出不同結果。

### 0.2 規範架構

```
docs/spec.md（最終規範，本檔的下一階段）
    ├─→ web tool：wordlist.js / index.html / README*.md
    └─→ skill：SKILL.md / README.md
```

### 0.3 裁定方式

每一條目以表格陳列，欄位依序為：英文 / Skill 對應 / Web 對應 / 觀察 / 裁定。

「裁定」欄已預填**建議**，使用者可：
- 直接接受（建議的選項保留）
- 改為對方版本（劃掉建議、勾選另一邊）
- 提出第三選項（在欄位內手寫漢字）
- 留意見（在欄位內補充註記，等待進一步討論）

### 0.4 標記說明

- **建議：Skill** — 推薦採 skill 規範的版本
- **建議：Web** — 推薦採 web tool 現況的版本
- **建議：Skill（視 H1）** — 此條目為 web 缺漏，是否納入轉換取決於高層議題 H1 的結論
- **🐛 Web bug** — Web 對應為明顯詞義錯誤（DeepL 翻譯歧義），無爭議性

---

## 1. 高層議題（請優先裁定）

這四個議題會影響後續 140 條 function word 的裁定意義，請先表態。

---

### 議題 H1：功能詞要不要納入轉換？

**衝突核心：**
此議題影響 64 條 web 缺漏條目（冠詞、所有助動詞、多數介詞、否定詞、許多副詞）的去留。

**Web tool 現況的設計理念：**
日文與韓文借用漢字時，多半只借「實詞」（名詞、動詞、形容詞），功能詞通常保留原文。理由：功能詞普遍很短，全部漢字化會增加視覺密度，反而降低可讀性。

**Skill 現況的設計理念：**
全部轉換能形成內部一致的書寫系統，每個英文詞都有對應的漢字呈現。

**衝突點：**
不轉功能詞會造成「割裂感」（`the 猫 座ed on the 蓆`——英文與漢字交雜的視覺斷裂）；但全轉又會稀釋訊息密度（`其` 反覆出現）。

**選項：**

| 選項 | 內容 | 優點 | 缺點 |
|---|---|---|---|
| **H1-A** | **全部轉換**（採 skill 規範） | 系統一致 | 視覺密度高、`其` 稀釋訊息 |
| **H1-B** | **只轉實詞**（採 web tool 現況） | 視覺清爽、貼近日韓借字慣例 | 割裂感、若不轉 `is/was` 動詞時態丟失 |
| **H1-C** | **部分轉換** | 折衷：轉代名詞、助動詞（實詞型功能詞）；不轉冠詞、短介詞（`a/an/the/of/in/to/for/on/at/by`） | 規則需細分、學習成本中等 |
| **H1-D** | **可選轉換** | Web tool 加 toggle，使用者自選 | 工程複雜度上升、規範變兩套 |

**我的觀察：**
- 日韓的「借字模式」其實都包含助動詞（日文 `です/ます`、韓文 `이다`），只是這些是黏著語的助詞。英文的助動詞（`is/was/will`）較接近「半實詞」，不轉的話無法表達時態
- 純粹的虛詞（冠詞 `a/the`、短介詞 `of/in/to`）是最值得保留為英文的——它們本身語義稀薄、頻次極高，全轉視覺成本最大
- H1-C 是最有產品感的選項，但需要明確劃分「實詞型功能詞」與「純功能詞」

**建議：H1-C（部分轉換）**

**裁定：**  ▢ H1-C

**意見欄：**

> 有一點我不懂，不轉 is/was 為什麼會造成動詞時態丟失？ is/was 保留的話不是正好可以反應時態嗎？

---

### 議題 H2：字源中立 vs. 慣例優先

**衝突核心：**
Skill 規則 W9 規定「字源中立」（pan-CJK，不偏向任何單一傳統）。但實務上有時某個傳統的字形更通用、更易讀。

**典型案例：**
- `every` — Skill `毎`（日文新字體）vs Web `每`（中文標準）
- `画/絵/絵畫` — picture 應採哪個？
- `応/應` — should 採哪個？

**選項：**

| 選項 | 政策 |
|---|---|
| **H2-A** | 嚴格 pan-CJK 中立（採 skill W9） |
| **H2-B** | CJK 通用優先，無爭議時取最普及版本 |
| **H2-C** | 個案處理：每個有爭議的字單獨裁定 |

**建議：H2-B（通用優先）**——理由：規範的目標是讓讀者能理解，pan-CJK 中立是手段不是目的。當某個字形在三地都通用（如 `每`），優先採之；只有當沒有通用字形時才回到 W9 機械中立。

**裁定：** ▢ H2-B

**意見欄：**

> Every - 每; picture - 画; should - 応

---

### 議題 H3：簡體字處理

**衝突核心：**
Web tool 現有對照中存在大量簡體字（`从、关於、虽然、因为、虽、反对、何时、不过、险些、頗为` 等）。基於 W9 字源中立應採繁體；但簡體本身也是 CJK 的一部分。

**選項：**

| 選項 | 政策 |
|---|---|
| **H3-A** | 簡體一律改繁體 |
| **H3-B** | 簡體保留，視為 CJK 多樣性 |
| **H3-C** | 個案處理 |

**建議：H3-A（一律改繁體）**——理由：H1-C 若採行，留下的功能詞應以繁體為主；簡體字的 `从、关、虽` 對非簡體讀者陌生，且與其他繁體字混雜會破壞視覺統一。

**裁定：** ✓ H3-C

**意見欄：**

> 「从」可以保留使用; and 使用「与」; 「当」「无」也可以保留
> 部分使用日文漢字：「関」「対」（包含但不限於，如果筆畫相差大，繁體筆畫多，就以日文漢字為主，如「応」）
> 其他以繁體為主

**結論（C2 已決議）：**
- 基底為繁體中文
- 採用簡／古字／日文新字體共 ~60 字（見**附錄 C**）
- 保留繁體不簡化共 15 字（見**附錄 C**）
- 個別選字原則：本意／符合古字、結構簡單、通用元件、順筆、既有俗字、CJK 三地通用優先（與 H2-B 一致）

---

### 議題 H4：詞義誤對應（Web tool bugs）

**衝突核心：**
Web tool 用 DeepL 自動翻譯時產生的義項錯置。

**已知 bug：**

| 英文 | Web（錯誤） | 應為 | 錯誤類型 |
|---|---|---|---|
| `mine`（所有格） | 礦井 | 我之 | 把所有格誤解為名詞「礦坑」 |
| `still`（副詞「仍」） | 安靜 | 仍 | 把副詞誤解為形容詞「安靜的」 |
| `during`（介詞） | 期間 | 間 | 用名詞「期間」對應介詞 |
| `into`（方向） | 成 | 入 | 適合 turn into，不適合 walk into |
| `under`（位置） | 根據 | 下 | 用「根據」（under the rule）失去空間義 |
| `over`（位置） | 越過 | 上 | 偏動作義，但介詞 over 多半表「在...之上」 |
| `without`（否定） | 不帶 | 無 | 太具體（不帶錢），無法涵蓋抽象用法 |

（內容詞區的 bug 待第二輪稽核時處理，此處只處理 function word。）

**建議：H4-A（全部修正）**

**裁定：** ✓ H4-A 全部修正

**意見欄：**

> `mine` 也有作為礦坑或地雷之意，此時該怎樣處理好？

**結論（C6 已決議）：採 C6-a，規範與實作分層**

#### 多義字處理原則

- **wordlist**：每個英文詞對應單一漢字（取最常見義項）
- **LLM 實作**（如 hanjify skill）：依上下文判斷義項，可覆寫 wordlist 預設
- **查表實作**（如 web tool）：使用 wordlist 預設；對罕見義項會誤判，由使用者手動修正

#### 範例：mine

| 句子 | LLM 實作 | 查表實作 |
|---|---|---|
| This is mine. | 此 是 予之. | 此 是 予之. |
| Coal mine. | 煤 鉱. | 煤 mine.（誤判，可接受）|
| Land mine. | 地雷. | 地 mine.（誤判，可接受）|

#### wordlist 修整目標

- 當前 §H4 列出 7 個 function word 多義 bug（mine/still/during/into/under/over/without）—— 階段二必須修正
- 其他多義字 bug（如 bear/bank/light/spring 等）採「使用回報後再修」的反應式策略，不主動枚舉

---

## 2. 形態學規則（採 SKILL.md 版本）

以下規則直接採用 SKILL.md 的 M1–M9 完整內容。請逐條檢視，有疑問或希望修改處在意見欄留言。

### M1. Root + Suffix（漢字詞根＋英文後綴）[Hard]

漢字代表詞根，英文屈折/派生後綴以羅馬字母直接附加（無空格）。

> 例：She moves the boxes carefully. → 她 動s 其 箱es 慎ly.

**意見：** 這部分應該比較無歧義, 可以照規則

### M2. 後綴與前綴策略（C1-C 混合方案）[Hard]

採取混合策略：**屈折變化保留羅馬字、派生變化轉漢字**。

**整體優先順序：** 整詞查 wordlist → 命中即用；未命中則套後綴／前綴規則拆解；都不行則原文穿透。

#### M2a. 屈折變化 — 保留羅馬字

純文法屈折附加為英文後綴，與漢字詞根直接相連（無空格）：

| 屈折 | 用途 | 範例 |
|---|---|---|
| `-s`／`-es` | 複數 | move→動 / moves→動s; box→箱 / boxes→箱es |
| `-ed` | 過去式（規則） | walk→歩 / walked→歩ed |
| `-ing` | 進行／動名詞 | run→走 / running→走ing |
| `-er` | 比較級 | big→大 / bigger→大er |
| `-est` | 最高級 | big→大 / biggest→大est |

> 不規則過去式／過去分詞使用 `-t` 標記（見 M3）。

#### M2b. 派生後綴 — 轉漢字（fallback 規則）

當 wordlist 無整詞對應時，「詞根漢字 + 後綴漢字」拼接：

| 後綴 | 漢字 | 範例 |
|---|---|---|
| **人物身份** | | |
| `-er`／`-or`／`-ar` | 者 | teacher→教者、actor→演者、scholar→斈者 |
| `-ist` | 家 | novelist→小說家 |
| `-ician` | 師 | musician→音楽師 |
| `-eer` | 師 | engineer→工程師 |
| `-man` | 人 | horseman→馬人、sportsman→運動人 |
| `-ee` | 受 | employee→雇受、examinee→試受 |
| `-ess` | 者（不標性別） | actress→演者；個別詞 wordlist 可覆寫，如 princess→王女 |
| **詞性轉換** | | |
| `-ly` | 地 | actually→實際地、quickly→速地 |
| `-ful`／`-al`／`-ous`／`-ive` | 的 | beautiful→美的、agricultural→農業的 |
| `-able`／`-ible` | 的 | readable→読的、edible→食的 |
| `-less` | 无…的 | useless→无使用的、careless→无慎的、harmless→无害的 |
| `-fy`／`-ize`／`-ise` | 化 | simplify→簡化、industrialize→工業化 |
| **抽象名詞** | | |
| `-tion`／`-sion`／`-ment`／`-ness`／`-ance`／`-ancy` | 依 wordlist（無統一規則） | creation→創造、movement→運動、acceptance→認受狀 |
| **複合代詞／副詞** | | |
| `-thing` | 物 | something→某物、nothing→无物 |
| `-body` | 体 | somebody→某体、anybody→任体 |
| `-where` | 処 | anywhere→任何処、somewhere→某処 |
| `-one` | 一 | someone→某一、everyone→毎一 |

> ✓ `-less` 採用 **无…的**（C9 已決）：語義 = lacking/without，與 -ful 對稱（useful→使用的 / useless→无使用的）。规範詳見上表。

#### M2c. 派生前綴 — 轉漢字（fallback 規則）

| 前綴 | 漢字 | 範例 |
|---|---|---|
| `un-` | 不 | unhappy→不喜、unknown→不知、unable→不能 |
| `non-` | 非 | non-smoker→非煙者 |
| `re-` | 再 | rebuild→再建、restart→再起、reuse→再用 |
| `any-` | 任 | anybody→任体、anywhere→任何処 |
| `some-` | 某 | something→某物、somebody→某体 |
| `every-` | 毎 | everyone→毎一、everywhere→毎処 |
| `no-` | 无 | nobody→无体、nothing→无物 |

#### M2d. wordlist 整詞優先原則

整詞 wordlist 對應永遠優先於拆解規則。例：

| 詞 | wordlist 對應 | 若走規則會是 | 採用 |
|---|---|---|---|
| princess | 王女 | 主-ess→主者 | wordlist：王女 |
| review | 審查 | re-見→再見 | wordlist：審查 |
| return | 帰 | re-返→再返 | wordlist：帰 |
| meeting | 会議 | 会-ing→会議（有意義名詞）| wordlist：会議 |

讓特殊／約定俗成詞義得以保留，規則只在 wordlist 未覆蓋時 fallback。

#### M2e. 設計理由

- **派生後綴採「結構對應」（不做語意翻譯）**：每個後綴對應一個固定漢字，不依個別詞義細分。例：所有 `-er` 一律 → 者，不再區分 師／員／家。
- **`re- → 再`**：「再」字頻較低（與 again 偶有重疊），「重」與「重要／重力」衝突大、字頻過高。
- **`un- → 不`**：「非」與「非常 = very」嚴重衝突（wordlist 已有 `unusual → 非常` bug）；「不」最自然普適。
- **`non- → 非`**：與 un- 區分，表達範疇否定（non-X = 非 X 範疇）。

### M3. Irregular Past Forms（不規則過去式）[Hard]

不規則過去式與過去分詞使用詞根漢字＋`-t` 統一標記。

> 例：I thought about what I saw and went home.
> → 我 思t 関於 何 我 見t 與 行t 家.

完整不規則動詞表見**附錄 A**。

**意見：** 統一使用 `-t` 沒有問題，不過這樣 ruby 應該如何標記？日文裡的不規則動詞有什麼可以借鑑的嗎？

### M4. Established CJK Compounds（既有複合詞）[Hard]

當英文詞對應到既有 CJK 複合詞時，整體使用，不拆分。

> 例：Education gives us freedom and knowledge. → 教育 与s 吾等 自由 與 知識.

**意見：** 這條規則ok

### M5. Comparative and Superlative（比較級／最高級）[Hard]

`-er`、`-est` 後綴附加；周遍式 more/most + 形容詞，轉為 `更`/`最`。

> 例：The most intelligent one won. → 其 最 聰明 一 勝ed.

**意見：** 這條規則ok

### M6. Consistency Across Text（全文一致性）[Hard]

同一英文詞根全文必須對應同一漢字。轉換工具須建立 mapping table 並維持一致性。

**意見：** 這條規則ok

### M7. Contractions（縮寫展開）[Hard]

縮寫先展開再轉換：`don't → do not`、`it's → it is`、`I'm → I am`、`isn't → is not`、`wouldn't → would not`、`can't → cannot`、`won't → will not`、`they're → they are`、`we'll → we will` 等。

**意見：** 可以

### M8. Phrasal Verbs（片語動詞）[Soft]

當片語動詞有既有 CJK 對應時整體轉換；否則逐詞轉換。詳見**附錄 B**。

**意見：** 這條規則ok

### M9. Past Participle as Adjective（過去分詞作形容詞）[Hard]

不規則過去分詞作形容詞時，使用 `-n` 標記，與過去式 `-t` 區分。

> 例：A written letter lay on the broken table. → 一 書n 信 横ed 於 其 破n 卓.

**注意：** Web tool 的查表模型難以判斷語境（adjective vs verb）。實作時可考慮：
- 簡化版：`-en/-n` 結尾直接視為過去分詞作形容詞
- 完整版：保留給 LLM-driven skill 處理

**意見：** 既然英文語法中是同型, 那麼用漢字表示的英文也應該同型，不需要因為一個詞作為形容詞而改變形式。

---

## 3. Function Word 裁定表（140 條）

### 3.1 Articles（3 條）

| Eng | Skill | Web | 觀察 | 裁定 |
|---|---|---|---|---|
| a | 一 | (缺) | 冠詞，純功能詞 | ▢ 不轉  **建議：視 H1**（H1-A → 一；H1-B/C → 不轉） |
| an | 一 | (缺) | 同 a | ▢ 不轉  **建議：視 H1** |
| the | 其 | (缺) | 定冠詞，全文最高頻 | ▢ 不轉  **建議：視 H1** |

**意見：** _

---

### 3.2 Personal Pronouns（12 條）

| Eng | Skill | Web | 觀察 | 裁定 |
|---|---|---|---|---|
| I | 我 | 予 | Skill 通用古典；Web「予」現代讀者陌生 | ▢ 其他：予 |
| you | 汝 | 尔 | Skill 標準古典；Web「尔」為簡體 | ▢ 其他：尔 |
| he | 彼 | 伊 | Skill 標準；Web「伊」與 she 同字會歧義 | ▢ 其他：彼 |
| she | 她 | (缺) | 補上以避免與 he 混淆 | ▢ 其他：伊 |
| it | 它 | (缺) | 中性代名詞 | ▢ 其他：它 |
| we | 吾等 | 吾等 | 一致 | ✓ 一致 |
| they | 彼等 | 渠等 | Skill 標準；Web「渠」過於方言 | ▢ 其他：彼等 |
| me | 我 | (缺) | 與主格 I 同字 | 與主格 I 同字 |
| him | 彼 | (缺) | 與主格 he 同字 | 與主格 him 同字 |
| her (受格) | 她 | 伊 | Web 同 he 字會歧義 | 與主格 her 同字 |
| us | 吾等 | (缺) | 與主格 we 同字 | 與主格 we 同字 |
| them | 彼等 | 渠等 | 與 they 同問題 | 與主格 they 同字 |

**意見：** I 當初選用「予」，是考量到筆畫較少，字型簡單。「尔」亦如是。they/them 選用「彼等」，可能會偏 he/him, 失去中性，因此有考慮使用「渠等」，但可能更不易理解，故留彼等。

---

### 3.3 Possessive（9 條）

Skill 規範：以 `之` 作為所有格標記。

| Eng | Skill | Web | 觀察 | 裁定 |
|---|---|---|---|---|
| my | 我之 | (缺) | 規律：代名詞＋之 | 予之 |
| your | 汝之 | (缺) | 同上 | 尔之 |
| his | 彼之 | (缺) | 同上 | 彼之 |
| her (所有格) | 她之 | 伊 | Web 與受格、he 全部混在「伊」一字 | 伊之 |
| its | 它之 | (缺) | 同上規律 | 它之 |
| our | 吾等之 | (缺) | 同上規律 | 吾等之 |
| their | 彼等之 | (缺) | 同上規律 | 彼等之 |
| mine | 我之 | 礦井 | 🐛 Web bug（誤把所有格當「礦坑」） | 予之 |
| yours | 汝之 | (缺) | 同上規律 | 尔之 |

**意見：** _

---

### 3.4 Reflexive（8 條）

Skill 規範：以 `自` 作為反身標記，與代名詞系統契合。Web 混用日文「自身」、中文「本身」、籠統「自己」。

| Eng | Skill | Web | 觀察 | 裁定 |
|---|---|---|---|---|
| myself | 我自 | 私自身 | Web 用日文系統 | 予自 |
| yourself | 汝自 | 尔自身 | Web 簡體＋日文 | 尔自 |
| himself | 彼自 | 彼自身 | Web 用日文系統 | 彼自 |
| herself | 她自 | 彼女自身 | Web 全日文化 | 伊自 |
| itself | 它自 | 它本身 | Web 用中文「本身」 | 它自 |
| ourselves | 吾等自 | (缺) | 同上規律 | 吾等自 |
| yourselves | 汝等自 | (缺) | 同上規律 | 尔等自 |
| themselves | 彼等自 | 自己 | Web 用籠統「自己」失去人稱 | 彼等自 |

**意見：** _

---

### 3.5 Interrogative & Relative（9 條）

| Eng | Skill | Web | 觀察 | 裁定 |
|---|---|---|---|---|
| who | 誰 | 誰 | 一致 | ✓ 一致 |
| whom | 誰 | (缺) | 與 who 同字 | 誰 |
| what | 何 | 何 | 一致 | ✓ 一致 |
| which | 何 | 其中 | Web「其中」是介詞義；what/which 同字符合古文 | **何**（疑問詞）／**其中**（關係代名詞）— 啟發式分流，定案 |
| whose | 誰之 | (缺) | who+之，符合所有格規律 | 誰之 |
| where | 何処 | 何処 | 一致 | ✓ 一致 |
| when | 何時 | 何时 | Web 簡體 | 何時 |
| why | 何故 | 何故 | 一致 | ✓ 一致 |
| how | 如何 | 如何 | 一致 | ✓ 一致 |

**意見：** `which` 作為介詞時，應該如何對應？使用「何」會讓句子的語意不順。

**結論（C5 衍生，C5-d 修正）：** which 比照 when 採啟發式分流——
- 句首大寫 `Which` + 子句末 `?` → **何**（疑問詞）
- 其他情境 → **其中**（關係代名詞）

實作同 when 規則：把每行依 `.!?` 切子句記錄結尾，which 出現時查所在子句結尾。

理由：「其中」古文本即有「在...裡面」義，與 prep+which 結構（in/of/by/from + which）契合度高；裸 which 句（the book which I read）略冗但可接受。

---

### 3.6 Demonstrative（4 條）

| Eng | Skill | Web | 觀察 | 裁定 |
|---|---|---|---|---|
| this | 此 | 這 | Skill 古典單字；Web 現代中文 | 這 |
| that | 彼 | 那 | 同上；但 Skill 的「彼」與 he 同字會歧義（語境通常可區分） | 那 |
| these | 此等 | (缺) | this + 等 | 這等 |
| those | 彼等 | (缺) | that + 等；但與 they/them 同字會歧義 | 那等 |

**意見：** WEB 使用「這/那」正是為了避免與「he/him」發生重複。

---

### 3.7 Prepositions（22 條）

| Eng | Skill | Web | 觀察 | 裁定 |
|---|---|---|---|---|
| of | 之 | (缺) | 純虛詞，最高頻 | ▢ 不轉 |
| in | 在 | (缺) | 純虛詞 | ▢ 不轉 |
| to | 至 | (缺) | 注意：infinitive to（want **to** go）保留為英文 | ▢ 不轉 |
| for | 為 | (缺) | | 為 |
| with | 與 | (缺) | 與連詞 and 同字 | 与 |
| on | 於 | (缺) | 與 at 同字（intentional homography） | ▢ 不轉 |
| at | 於 | (缺) | 同上 | ▢ 不轉 |
| from | 自 | 从 | Web 簡體 | 从 |
| by | 以 | (缺) | | 以 |
| about | 関於 | 关於 | Web 簡體（关） | 関於 |
| around | 周 | 周辺 | Skill 單字；Web 雙字 | 周辺 |
| into | 入 | 成 | 🐛 Web 詞義誤（「成」適合 turn into） | 入 |
| through | 經 | 透過 | Skill 單字、字源更普適 | 經 |
| between | 間 | 間 | 一致 | ✓ 一致 |
| under | 下 | 根據 | 🐛 Web 詞義誤（用「根據」失去空間義） | **下於**（避歧 up/down，定案）|
| over | 上 | 越過 | Web 偏動作義；介詞 over 多表「在...之上」 | **上於**（避歧 up/down，定案）|
| after | 後 | 後 | 一致 | ✓ 一致 |
| before | 前 | 以前 | Skill 單字 | 前 |
| without | 無 | 不帶 | 🐛 Web 太具體 | **不与**（with-out → with（与）+ out（不），定案）|
| during | 間 | 期間 | 🐛 Web 用名詞對介詞 | 間 |
| against | 對 | 反对 | Web 簡體＋雙字 | 反対 |
| among | 中 | 其中 | Skill 單字 | 其中 |

CC 意見：Skill 的 `on/at` 同字（於）、`with/and` 同字（與）、`between/during` 同字（間）是刻意的「intentional homography」（語境消歧）。如果你希望避免歧義，可以為這些對給予不同字。

**我的意見：**同意以上 CC 意見中關於刻意的語境消歧的做法。先前曾經有個規則是，太短的單字（例如三個字母以下）不提供漢字，因此會看到上表中有許多界系詞在 WEB 都是 "(缺)"。不過這個規則或許可以打破，讓部分短單字，有明確意思不容易有歧義的也有對應漢字。

without 上面寫「不与」，另外兩個保留意見是「与不」、「与出」

---

### 3.8 Conjunctions（13 條）

| Eng | Skill | Web | 觀察 | 裁定 |
|---|---|---|---|---|
| and | 與 | (缺) | 與介詞 with 同字 | 与 |
| or | 或 | (缺) | | 或 |
| but | 然 | (缺) | 與 yes（然）同字（intentional） | 但 |
| because | 因 | 因为 | Web 簡體＋雙字 | 因為 |
| if | 若 | 若 | 一致 | ✓ 一致 |
| when (連詞) | 當 | 何时 | Web 用疑問詞「何时」對連詞，且簡體 | **当**（連詞）／**何時**（疑問詞） — 啟發式分流，定案 |
| while | 時 | 正当 | Skill 單字、Web 簡體 | 正当 |
| although | 雖 | 虽然 | Web 簡體＋雙字 | 雖然 |
| so | 故 | (缺) | | 故 |
| than | 於 | 於 | 一致；與 on/at 同字 | ✓ 一致 |
| as | 如 | (缺) | | 如 |
| unless | 除非 | 除非 | 一致 | ✓ 一致 |
| whether | 是否 | 是否 | 一致 | ✓ 一致 |

**意見：** 有提到 "when" 作為連詞時寫作「當」，但是程式碼有辦法簡單判斷疑問詞或連接詞嗎？其次，`because` 這單字比較長，因此使用「因為」，而不是單一漢字「因」

**結論（C4 已決議）：** 採啟發式分流——
- 句首大寫 `When` + 子句末 `?` → **何時**（疑問詞）
- 其他情境 → **当**（連詞）

實作：把每行依 `.!?` 切子句記錄結尾，`when` 出現時查所在子句結尾。間接疑問句（`I don't know when he came`）會被誤判為連詞，但讀起來尚可。

---

### 3.9 Auxiliary Verbs（22 條）

Skill 規範：助動詞用單字＋形態學後綴標示時態（`是/是ed/是t`、`有/有ed`、`行/行ed`、`能/能ed`、`將/將ed`、`可/可ed`）。

| Eng | Skill | Web | 觀察 | 裁定 |
|---|---|---|---|---|
| is | 是 | (缺) | | ▢ Skill |
| am | 是 | 是 | 一致 | ✓ 一致 |
| are | 是 | (缺) | 與 is/am 同字 | ▢ Skill |
| was | 是ed | (缺) | 過去式以 -ed 標示 | ▢ Skill |
| were | 是ed | (缺) | 同 was | ▢ Skill |
| been | 是t | (缺) | 不規則過去分詞 -t | ▢ Skill |
| being | 是ing | (缺) | -ing 進行式 | ▢ Skill |
| have | 有 | 有 | 一致 | ✓ 一致 |
| has | 有 | (缺) | 與 have 同字 | ▢ Skill |
| had | 有ed | (缺) | | ▢ Skill |
| do | 行 | (缺) | 與動詞 go（行）同字（intentional） | ▢ Skill |
| does | 行 | (缺) | | ▢ Skill |
| did | 行ed | (缺) | | ▢ Skill |
| can | 能 | (缺) | | ▢ Skill |
| could | 能ed | (缺) | | ▢ Skill |
| will | 將 | (缺) | | ▢ Skill |
| would | 將ed | (缺) | | ▢ Skill |
| should | 應 | (缺) | | 応 |
| may | 可 | (缺) | | ▢ Skill |
| might | 可ed | (缺) | | ▢ Skill |
| must | 須 | (缺) | | ▢ Skill |
| shall | 宜 | (缺) | | ▢ Skill |

**意見：** 助動詞是「實詞型功能詞」的核心——若採 H1-B 完全不轉，動詞時態（was/were/will be）將整段失去。建議無論採 H1-A 或 H1-C，助動詞都應納入轉換。

---

### 3.10 Negation（6 條）

| Eng | Skill | Web | 觀察 | 裁定 |
|---|---|---|---|---|
| not | 不 | (缺) | 否定核心，極高頻 | 不 |
| no | 無 | (缺) | | 无 |
| nor | 亦不 | 也不 | Web 簡體式（也） | 亦不 |
| never | 從不 | 从不 | Web 簡體 | 从不 |
| none | 無一 | 无 | Web 簡體＋失去「一個都沒」 | 无一 |
| neither | 亦不 | 既不 | Skill 與 nor 同字（intentional） | 亦不 |

**意見：** _

---

### 3.11 Common Adverbs & Determiners（32 條）

| Eng | Skill | Web | 觀察 | 裁定 |
|---|---|---|---|---|
| very | 甚 | (缺) | | 甚 |
| also | 亦 | 还 | Web 簡體（还） | 亦 |
| too | 亦 | (缺) | 與 also 同字 | 亦 |
| only | 僅 | 唯一 | Skill 單字、Web 雙字 | 唯一 |
| just | 僅 | (缺) | 與 only 同字 | 僅 |
| all | 皆 | 全 | 兩者皆通；Skill「皆」更古典 | 全 |
| still | 仍 | 安靜 | 🐛 Web 詞義誤 | 仍 |
| already | 已 | 既 | 兩者古文都通；「已」更直觀 | 既 |
| always | 常 | 始終 | Skill 單字、Web 雙字 | 始終 |
| often | 頻 | 常常 | Skill 單字 | 常常 |
| some | 某 | (缺) | | 某 |
| many | 多 | 許多 | Skill 單字 | 多 |
| much | 多 | 多 | 一致 | ✓ 一致 |
| every | 毎 | 每 | **議題 H2**：Skill 用日文新字體，Web 用中文標準 | 每 |
| each | 各 | (缺) | | 各 |
| other | 他 | 其他 | Skill 單字、Web 雙字 | 其他 |
| another | 他一 | 另 | Skill 為 other+一；Web 單字「另」也直觀 | 另 |
| same | 同 | 相樣 | Skill 單字；Web「相樣」非標準詞 | 相樣 |
| such | 如此 | (缺) | | 如此 |
| yes | 然 | (缺) | 與 but（然）同字（intentional） | 是 |
| here | 此処 | 此処 | 一致 | ✓ 一致 |
| there | 彼処 | 彼処 | 一致；注意 existential there 保留為英文 | ✓ 一致 |
| then | c | (缺) | | 則 |
| now | 今 | 今 | 一致 | ✓ 一致 |
| again | 再 | 再 | 一致 | ✓ 一致 |
| soon | 即 | 不久 | Skill 單字 | 不久 |
| yet | 尚 | 卻 | 兩字皆通；but/yet 在英文有別，「卻」偏轉折、「尚」偏「尚未」 | 卻 |
| perhaps | 或許 | 或許 | 一致 | ✓ 一致 |
| together | 共 | 在一起 | Skill 單字、Web 三字（破壞詞距） | **共集**（定案）|
| almost | 幾乎 | 険些 | Skill 通用、Web「險些」太古僻 | 幾乎 |
| enough | 足 | 十分 | Skill 單字、語義精確；Web「十分」偏「非常」 | 足夠 |
| quite | 頗 | 頗为 | Web 簡體（为） | 頗為 |

**意見：** `enough` 用單字「足」，易與`foot`混淆; 關於 `yet`, 「尚」雖然有「尚未」的意思，但若單獨存在，且放句尾 (yet 通常在句尾)，不易判斷是高尚、崇尚或是時尚等意。不難單純看英文對應的漢字是否符合意思，還要看該漢字的存在是否會造成歧義。
`together` 加上「集」的含義，作為「共集」。雖然現代漢語中或日文中沒有「共集」這種說法，但這是英文不是中文翻譯，因此不用拘泥於漢語詞的對應。

---

### 3.12 特殊情境

#### Infinitive `to` vs Prepositional `to`

| 情境 | 範例 | 處理 |
|---|---|---|
| 方向／目標 | go **to** London | 至（轉換） |
| 不定式標記 | want **to** go | to（保留英文） |

**裁定：** ▢ 採此規則

#### Existential `there` vs Locative `there`

| 情境 | 範例 | 處理 |
|---|---|---|
| 位置 | I went **there** | 彼処 |
| 存在句 | **There** is a book | there（保留英文） |

**裁定：** ✓ 採此規則

**意見：** _

---

### 3.13 不轉清單（C8 結論）

下列詞或情境**保留英文，不進行漢字轉換**：

#### A. 純功能詞（8 個）

| 類別 | 詞 |
|---|---|
| 冠詞 | `a`, `an`, `the` |
| 短虛介詞 | `of`, `in`, `to`, `on`, `at` |

理由：純位置／關係虛詞、極高頻、3 字母以下，全轉視覺成本最大。

#### B. 情境保留（2 種）

| 情境 | 範例 |
|---|---|
| Infinitive `to`（不定式標記，位於動詞前） | want **to** go |
| Existential `there`（存在句虛主詞） | **There** is a book |

#### C. 類別保留（依 W6 / W8 既有規則）

| 類別 | 處理 | 規則 |
|---|---|---|
| 西方專有名詞（人名／地名／品牌） | 保留英文 | W6（C5-b） |
| 無 CJK 對應的技術術語 | 保留英文 | W8（DNA、HTTP、API、WiFi）|

> 註：`as` 雖在 `as if / as well as / as long as` 等複合連詞中讀來生硬，但採「片語化」處理（見附錄 B），不歸入不轉清單。

---

## 4. Word Selection 規則 W1–W10（採 SKILL.md 版本）

請逐條檢視，有疑問處在意見欄留言。

### W1. Concrete Nouns — Visually Descriptive Characters [Hard]
具象名詞優先採象形漢字。例：sun→日、moon→月、water→水、mountain→山。
**意見：** 同意

### W2. Abstract Nouns — Compound Construction [Hard]
抽象名詞採既有 CJK 複合詞；無既有複合詞時，組合兩個義符字。例：freedom→自由、knowledge→知識。
**意見：** 同意

### W3. Verbs — Single Character Preferred [Hard]
動詞優先單字，後綴附加。例：eat→食、see→見、walk→歩。
**意見：** 同意

### W4. Adjectives — Hanzi Root + English Suffix [Hard]
形容詞詞根對應漢字，比較級／派生形以後綴附加。例：big→大、beautiful→美ful。
**意見：** 同意

### W5. Function Words — Strict Table Lookup [Hard]
功能詞嚴格查第 3 章對照表，不允許變體。
**意見：** 同意

### W6. Proper Nouns — Keep Original English [Hard]
專有名詞（人名、地名、品牌）保留英文，不轉換。例：John 行t 至 London.
**意見：** 東方的專有名詞（CJK 語境）可以翻譯，例如 Sun Yat-sen 翻成「孫逸仙」

**結論（C5 已決議）：採 C5-b 為基底＋wordlist 例外**

- **基底原則**：所有專有名詞保留英文（含西方人名、地名、品牌）
- **CJK 文化圈例外**（中日韓越含港澳臺，原本就以漢字書寫者）：使用漢字
  - 國名／地區：中国、日本、韓国、越南、台湾、香港、澳門
  - 首都／大城市：東京、首爾、北京、河內、京都、上海、釜山
  - 歷史人物：孔子、老子、孫逸仙、秀吉
  - 山河海域：富士山、長江、黃海、阿里山
- **wordlist 既有對應例外**：若 wordlist 已收錄漢字翻譯（例如 America→米国、China→中国），則沿用
- **西方人名一律保留英文**：Einstein、Bach、Newton、Mozart 等（音譯字三地不同，無 pan-CJK 中立解）

### W7. Numbers — CJK Numerals [Hard]
書寫形式數字用漢字（一/二/三/百/千），年份／日期保留阿拉伯數字。
**意見：** 同意

### W8. Technical Terms — Keep English [Soft]
無自然漢字對應的術語（DNA、HTTP、API、WiFi 等縮寫）保留英文；已有 CJK 對應的術語使用對應（**algorithm→演祘法**、computer→電脳、telephone→電話）。
**意見：** 同意

### W9. Character Tradition Neutrality [Soft]
多個漢字可選時，依序：(1) CJK 三地通用字 (2) 筆畫較簡 (3) 表意更直接。
**注意：H2 議題若採 H2-B（通用優先），W9 的 (1) 條會優先於 (2) 與 (3)。**
**意見：** 原則ok, 若無通用字, 簡體字的筆畫較簡，且有古字來源（不是草書楷化，或偏旁簡化字），則可選用簡體字。

### W10. Compound Nouns [Soft]
複合名詞優先採既有 CJK 複合詞；無對應時拆分組合或保留英文。例：sunlight→日光、bookshelf→書棚。
**意見：** 同意

---

## 5. Formatting 規則 F1–F4（採 SKILL.md 版本）

### F1. English Punctuation [Hard]
標點符號採英文（. , ? ! : ; "" ''），**不採中文標點**（。，？！「」：；）。
**意見：** 同意

### F2. English Word Spacing [Hard]
詞間空格採英文（空格分隔），**不採中文連續排版**（無空格）。
**意見：** 同意

### F3. Preserve Document Structure [Hard]
段落、換行、標題、列表、引用區塊等文件結構保持原樣。
**意見：** 同意

### F4. No Annotations in Hanjified Section [Hard]
純漢字化段落只包含漢字＋羅馬後綴，不夾帶英文原文或標注；標注一律放在 Ruby 段。
**意見：** 同意

---

## 5b. 衝突避歧規則（C7）

### 5b.1 規則

1. **衝突判定**：function word 的單字漢字若與**詞類／角色不同**的另一高頻詞共用同一漢字，視為衝突
2. **衝突解決**：受影響的 function word 改用雙字漢字（不擾動 content word）
3. **判定範圍**：完全同字才算衝突（不擴及子串／同音）

### 5b.2 Intentional homography 例外（不視為衝突）

下列同字情境**詞類／語意角色相近**，視為刻意的歧義共享：

| 詞對 | 共用字 | 角色 |
|---|---|---|
| on / at | 於 | 位置介詞 |
| between / during | 間 | 時空區間 |
| and / with | 与 | 連結／伴隨 |
| many / much | 多 | 量詞 |
| but / yes | 然 | 轉折／肯定 |

### 5b.3 已處理衝突清單

| Function word | 衝突對象 | 原單字 | 改用雙字 |
|---|---|---|---|
| under | down（副詞）| 下 | **下於** |
| over | up（副詞）| 上 | **上於** |
| enough | foot（名詞）| 足 | **足夠** |
| yet | 高尚／時尚等 | 尚 | **卻** |

新衝突在使用回報後追加處理。

---

## 6. 附錄 A：常見不規則動詞表（M3 / M9 適用）

來源：SKILL.md M3 + 常見英文不規則動詞表，整理為 web tool 可程式化使用的格式。

### 過去式 → `-t` 標記

| 原型 | 漢字 | 過去式 | 過去分詞作動詞 |
|---|---|---|---|
| go | 行 | went → 行t | gone → 行t |
| see | 見 | saw → 見t | seen → 見t |
| think | 思 | thought → 思t | thought → 思t |
| eat | 食 | ate → 食t | eaten → 食t |
| come | 来 | came → 来t | come → 来t |
| give | 与 | gave → 与t | given → 与t |
| take | 取 | took → 取t | taken → 取t |
| write | 書 | wrote → 書t | written → 書t |
| speak | 言 | spoke → 言t | spoken → 言t |
| say | 言 | said → 言t | said → 言t |
| know | 知 | knew → 知t | known → 知t |
| stand | 立 | stood → 立t | stood → 立t |
| sit | 座 | sat → 座t | sat → 座t |
| find | 発見 | found → 発見t | found → 発見t |
| buy | 買 | bought → 買t | bought → 買t |
| run | 走 | ran → 走t | run → 走t |
| hold | 持 | held → 持t | held → 持t |
| break | 破 | broke → 破t | broken → 破t |
| make | 作 | made → 作t | made → 作t |
| get | 得 | got → 得t | gotten/got → 得t |
| tell | 告 | told → 告t | told → 告t |
| hear | 聞 | heard → 聞t | heard → 聞t |
| feel | 感 | felt → 感t | felt → 感t |
| leave | 去 | left → 去t | left → 去t |
| keep | 保 | kept → 保t | kept → 保t |
| send | 送 | sent → 送t | sent → 送t |
| bring | 持来 | brought → 持来t | brought → 持来t |
| read | 読 | read → 読t | read → 読t |
| sleep | 眠 | slept → 眠t | slept → 眠t |
| meet | 会 | met → 会t | met → 会t |

### 過去分詞作形容詞 → `-n` 標記（M9）

| 過去分詞 | 漢字 + 標記 | 範例 |
|---|---|---|
| written | 書n | a written letter → 一 書n 信 |
| broken | 破n | a broken table → 一 破n 卓 |
| forgotten | 忘n | a forgotten book → 一 忘n 書 |
| spoken | 言n | the spoken language → 其 言n 言語 |
| known | 知n | a known fact → 一 知n 事実 |
| given | 与n | a given task → 一 与n 任務 |
| taken | 取n | a taken seat → 一 取n 席 |
| eaten | 食n | the eaten apple → 其 食n 苹果 |

**意見：** _

---

## 7. 附錄 B：常見片語表（M8 適用）

### 7.1 片語動詞

| 片語 | 漢字 | 範例 |
|---|---|---|
| give up | 放棄 | She gave up → 她 放棄ed |
| break down | 崩壊 | The car broke down → 其 車 崩壊ed |
| look for | 探 | I look for it → 我 探 它 |
| find out | 発見 | We found out → 吾等 発見t |
| carry out | 執行 | They carried out → 彼等 執行ed |
| turn off | 消 | Turn off the light → 消 其 光 |
| set up | 設立 | They set up → 彼等 設立ed |
| pick up | 拾 | Pick up the book → 拾 其 書 |
| make up | 構成 | Words make up sentences → 詞s 構成 句s |
| point out | 指摘 | He pointed out → 彼 指摘ed |
| bring up | 提起 | She brought up → 她 提起t |
| come back | 帰 | They came back → 彼等 帰t |

### 7.2 連詞片語（`as X as` 系列）

`as` 在複合連詞中採字面拆字升級為片語，wordlist 以 multi-word entry 收錄：

| 片語 | 漢字 | 範例 |
|---|---|---|
| as well as | 如善如 | Tom 喜s 苹果s **如善如** 香蕉s. |
| as long as | 如長如 | 予 留t **如長如** 予 能. |
| as soon as | 如即如 | 来 **如即如** 可能. |
| as much as | 如多如 | 予 食t **如多如** 予 欲t. |
| as many as | 如多如 | (同上)|
| as far as | 如远如 | 予 知 **如远如** ... |
| as if | 如若 | 它 看ed **如若** 真. |
| as though | 如雖 | (同上) |

> 設計理念：以漢字逐字對應英文結構，讀者識得 `as X as` 即可解讀 `如X如`。不嘗試翻譯為 CJK 慣用語（如 `並且／只要`），保持「結構對應」純粹性。

**意見：** _

---

## 8. 附錄 C：字形採用清單（H3 / C2 結論）

### 8.1 採用字形清單（繁體 → 採用）

> 規範以**繁體中文為基底**；下列字一律改用「採用」欄字形。其他未列字維持繁體。

#### A. 共通字（CN-simp + JP shinjitai 同形）

| 繁 | 採用 | | 繁 | 採用 |
|---|---|---|---|---|
| 來 | 来 | | 國 | 国 |
| 數 | 数 | | 體 | 体 |
| 寶 | 宝 | | 將 | 将 |
| 與 | 与 | | 黨 | 党 |
| 醫 | 医 | | 參 | 参 |
| 斷 | 断 | | 屬 | 属 |

#### B. CN 簡化字採用

| 繁 | 採用 | | 繁 | 採用 |
|---|---|---|---|---|
| 從 | 从 | | 當 | 当 |
| 無 | 无 | | 時 | 时 |
| 單 | 单 | | 戰 | 战 |
| 選 | 选 | | 舉 | 举 |
| 達 | 达 | | 園 | 园 |
| 遠 | 远 | | 電 | 电 |
| 務 | 务 | | 離 | 离 |
| 親 | 亲 | | 雖 | 虽 |
| 殺 | 杀 | | 靈 | 灵 |
| 壓 | 压 | | 盡 | 尽 |
| 眾 | 众 | | 塵 | 尘 |

#### C. JP 新字體採用

| 繁 | 採用 | | 繁 | 採用 |
|---|---|---|---|---|
| 機 | 机 | | 樂 | 楽 |
| 鐵 | 鉄 | | 經 | 経 |
| 關 | 関 | | 對 | 対 |
| 應 | 応 | | 效 | 効 |
| 溫 | 温 | | 腦 | 脳 |
| 擴 | 拡 | | 發 | 発 |
| 觀 | 観 | | 齡 | 齢 |
| 燒 | 焼 | | 兒 | 児 |
| 獎 | 奨 | | 淺 | 浅 |
| 錢 | 銭 | | | |

#### D. 古字／俗字／異體字採用

| 繁 | 採用 | 說明 |
|---|---|---|
| 學 | 斈 | 古字 |
| 覺 | 斍 | 古字 |
| 算 | 祘 | 古字 |
| 氣 | 气 | 古字 |
| 世 | 卋 | 異體字 |
| 獸 | 嘼 | 古字 |
| 雞 | 鷄 | 異體字 |
| 收 | 収 | 俗字 |

### 8.2 不簡化清單（明確保留繁體）

`黑、動、傳、隊、鄰、勝、華、畢、風、圍、織、識、圖、線、筆`

### 8.3 個別選字原則（取字考量）

當待採字形需要選擇時，依序考量：

1. 符合本意或符合古字
2. 結構簡單（既有結構，筆畫數不重要）
3. 通用元件
4. 順筆與否
5. 是否既有俗字
6. **CJK 三地通用優先**（H2-B 配套）

### 8.4 階段二待修整（wordlist 既有混用條目）

wordlist 既有以下繁體／採用混用，依規範修正：

| 字 | 採用方向 |
|---|---|
| 對／対／对 → 対 | 整理為 **対** |
| 時／时 → 时 | 整理為 **时** |
| 經／経 → 経 | 整理為 **経** |
| 來／来 → 来 | 整理為 **来** |
| 選／选 → 选 | 整理為 **选** |
| 遠／远 → 远 | 整理為 **远** |
| 電／电 → 电 | 整理為 **电** |
| 雞／鷄 → 鷄 | 整理為 **鷄** |
| 筆／笔 → 筆 | 整理為 **筆**（不簡化） |
| 將／将 → 将 | wordlist 僅 1 條（you'll→您將 → 您将） |

---

## 9. 待確認問題清單

完成裁定後，請在此確認：

- [x] H1 已選定（功能詞納入政策）
- [x] H2 已選定（字源中立 vs. 慣例優先）
- [x] H3 已選定（簡體字處理）
- [x] H4 已確認（詞義誤對應修正）
- [x] 第 3 章 140 條 function word 全部裁定（包含留意見的條目）
- [x] M1–M9 各條無重大異議
- [x] W1–W10 各條無重大異議
- [x] F1–F4 各條無重大異議
- [ ] 附錄 A、B 內容認可

完成後，請告訴我 "可以凍結 spec" 或具體哪幾條需要進一步討論，我會：
1. 將本檔重新整理為 `docs/spec.md`（去掉裁定欄、保留最終決定）
2. 啟動階段二，依規範同步修改 wordlist.js / index.html / SKILL.md / READMEs

---

> **本檔位置：** `~/works/hanjify/docs/spec-draft.md`
> **規範來源比對：** `~/works/skills/hanjify/SKILL.md`、`~/works/hanjify/wordlist.js`
> **最終目標：** `~/works/hanjify/docs/spec.md`（凍結後產出）
