# Hanjify 規範

> **Single source of truth** for the Hanjify project.
>
> 凍結日：2026-04-26 ｜ 來源：`spec-draft.md` 9 個議題（C1–C9）裁定結果

---

## 0. 前言

### 0.1 規範目的

定義 Hanjify 的字形與形態學規則，統一兩種實作的行為：

```
docs/spec.md（本檔，最終規範）
    ├─→ Web tool (~/works/hanjify)：wordlist.js / index.html / READMEs
    └─→ Claude Code skill (~/works/skills/hanjify)：SKILL.md
```

### 0.2 設計核心

1. **不是翻譯**：英語文法完全保留，只替換個別單詞為漢字
2. **混合策略**：屈折變化保留羅馬字、派生變化轉漢字
3. **wordlist 整詞優先**：規則為 fallback
4. **CJK 三地通用優先**：字源中立但通用性優先

### 0.3 工具實作分層

| 層 | 角色 |
|---|---|
| 規範（本文）| Single source of truth |
| wordlist.js | 整詞對應字典（查表優先，每詞單一對應）|
| LLM 實作（skill）| 上下文判斷，可覆寫 wordlist |
| 查表實作（web tool）| 用 wordlist 預設；罕見義項由使用者修正 |

---

## 1. 高層原則

### 1.1 功能詞納入政策

採部分轉換：
- **轉**：代名詞、助動詞、否定詞、大部分介詞與連詞、副詞
- **不轉**：純虛詞（`a/an/the/of/in/to/on/at`）— 詳見 §3.13

### 1.2 字源策略

CJK 三地通用優先：
- 字形三地皆通用 → 採之
- 無通用字 → 依個別選字原則（§8.3）

### 1.3 字形採用

繁體基底 + 簡化字／古字／日文新字體個別採用清單。詳見 §8 附錄 C。

### 1.4 多義字處理

- wordlist 每詞單一對應（取最高頻義）
- LLM 實作可上下文判斷，覆寫 wordlist
- 查表實作對罕見義項會誤判，由使用者手動修正

---

## 2. 形態學規則

### M1. 詞根 + 後綴

漢字代表詞根，英文屈折／派生後綴以羅馬字母直接附加（無空格）。

> 例：She moves the boxes carefully. → 她 動s the 箱es 慎ly.

### M2. 後綴與前綴策略（混合方案）

採取混合策略：**屈折變化保留羅馬字、派生變化轉漢字**。

**優先順序**：整詞查 wordlist → 命中即用；未命中則套後綴／前綴規則拆解；都不行則原文穿透。

#### M2a. 屈折變化 — 保留羅馬字

| 屈折 | 用途 | 範例 |
|---|---|---|
| `-s`／`-es` | 複數 | move→動 / moves→動s; box→箱 / boxes→箱es |
| `-ed` | 過去式（規則） | walk→歩 / walked→歩ed |
| `-ing` | 進行／動名詞 | run→走 / running→走ing |
| `-er` | 比較級 | big→大 / bigger→大er |
| `-est` | 最高級 | big→大 / biggest→大est |

不規則過去式／過去分詞另用 `-t` 標記（見 M3）。

#### M2b. 派生後綴 — 轉漢字（fallback 規則）

當 wordlist 無整詞對應時，「詞根漢字 + 後綴漢字」拼接：

| 後綴 | 漢字 | 範例 |
|---|---|---|
| **人物身份** | | |
| `-er`／`-or`／`-ar` | 者 | teacher→教者、actor→演者、scholar→斈者 |
| `-ist` | 家 | novelist→小說家 |
| `-ician` | 師 | musician→音楽師 |
| `-eer` | 師 | engineer→工程師 |
| `-man` | 人 | horseman→馬人 |
| `-ee` | 受 | employee→雇受 |
| `-ess` | 者（不標性別）| actress→演者；個別詞 wordlist 可覆寫，如 princess→王女 |
| **詞性轉換** | | |
| `-ly` | 地 | actually→實際地 |
| `-ful`／`-al`／`-ous`／`-ive` | 的 | beautiful→美的 |
| `-able`／`-ible` | 的 | readable→読的 |
| `-less` | 无…的 | useless→无使用的、harmless→无害的 |
| `-fy`／`-ize`／`-ise` | 化 | industrialize→工業化 |
| **抽象名詞** | | |
| `-tion`／`-sion`／`-ment`／`-ness`／`-ance`／`-ancy` | 依 wordlist | creation→創造、movement→運動 |
| **複合代詞／副詞** | | |
| `-thing` | 物 | something→某物、nothing→无物 |
| `-body` | 体 | somebody→某体、anybody→任体 |
| `-where` | 処 | anywhere→任何処 |
| `-one` | 一 | someone→某一 |

#### M2c. 派生前綴 — 轉漢字（fallback 規則）

| 前綴 | 漢字 | 範例 |
|---|---|---|
| `un-` | 不 | unhappy→不喜、unknown→不知 |
| `non-` | 非 | non-smoker→非煙者 |
| `re-` | 再 | rebuild→再建、restart→再起 |
| `any-` | 任 | anybody→任体 |
| `some-` | 某 | something→某物 |
| `every-` | 每 | everyone→每一 |
| `no-` | 无 | nobody→无体、nothing→无物 |

#### M2d. wordlist 整詞優先

整詞 wordlist 對應永遠優先於拆解規則。例：

| 詞 | wordlist 對應 |
|---|---|
| princess | 王女（不走 -ess→者）|
| review | 審查（不走 re-→再）|
| return | 帰（不走 re-→再）|
| meeting | 会議（不走 -ing→拆解）|

讓特殊／約定俗成詞義保留，規則只在 wordlist 未覆蓋時 fallback。

### M3. 不規則過去式

不規則過去式與過去分詞使用詞根漢字＋`-t` 統一標記。

> 例：I thought about what I saw and went home.
> → 我 思t 関於 何 我 見t 与 行t 家.

完整不規則動詞表見附錄 A。

**Ruby 標記**：整段標 `<ruby>行t<rt>went</rt></ruby>`。

### M4. 既有 CJK 複合詞

當英文詞對應到既有 CJK 複合詞時，整體使用，不拆分。

> 例：Education gives us freedom and knowledge.
> → 教育 与s 吾等 自由 与 知識.

### M5. 比較級與最高級

`-er`、`-est` 後綴附加；周遍式 `more`/`most` + 形容詞，轉為 `更`/`最`。

> 例：The most intelligent one won. → the 最 聰明 一 勝ed.

### M6. 全文一致性

同一英文詞根全文必須對應同一漢字。轉換工具須建立 mapping table 並維持一致性。

### M7. 縮寫展開

縮寫先展開再轉換：

| 縮寫 | 展開 |
|---|---|
| don't | do not |
| won't | will not |
| can't | cannot |
| isn't | is not |
| wouldn't | would not |
| I'm | I am |
| it's | it is |
| they're | they are |
| we'll | we will |

### M8. 片語

當片語有既有對應時整體轉換；否則逐詞轉換。完整片語表見附錄 B（含片語動詞 §B.1 與連詞片語 §B.2）。

### M9. 過去分詞作形容詞

不規則過去分詞作形容詞時，與動詞同型，沿用 `-t` 標記（不另設 `-n` 標記）。

> 例：A written letter lay on the broken table.
> → 一 書t 信 横ed 於 the 破t 卓.

---

## 3. Function Word 對照表

### 3.1 Articles（不轉）

| Eng | 漢字 |
|---|---|
| a, an, the | （不轉，保留英文）|

### 3.2 Personal Pronouns

| Eng | 漢字 | Eng | 漢字 |
|---|---|---|---|
| I / me | 予 | we / us | 吾等 |
| you | 尔 | they / them | 彼等 |
| he / him | 彼 | | |
| she / her（受格）| 伊 | | |
| it | 它 | | |

### 3.3 Possessive（以 `之` 為所有格標記）

| Eng | 漢字 | Eng | 漢字 |
|---|---|---|---|
| my / mine | 予之 | our | 吾等之 |
| your / yours | 尔之 | their | 彼等之 |
| his | 彼之 | | |
| her（所有格）| 伊之 | | |
| its | 它之 | | |

### 3.4 Reflexive（以 `自` 為反身標記）

| Eng | 漢字 | Eng | 漢字 |
|---|---|---|---|
| myself | 予自 | ourselves | 吾等自 |
| yourself | 尔自 | yourselves | 尔等自 |
| himself | 彼自 | themselves | 彼等自 |
| herself | 伊自 | | |
| itself | 它自 | | |

### 3.5 Interrogative & Relative

| Eng | 漢字 |
|---|---|
| who / whom | 誰 |
| whose | 誰之 |
| what | 何 |
| where | 何処 |
| why | 何故 |
| how | 如何 |
| **which** | **何**（疑問詞）／**其中**（關係代名詞）— 啟發式分流 |
| **when** | **何時**（疑問詞）／**当**（連詞）— 啟發式分流 |

#### `when` / `which` 啟發式分流規則

- 句首大寫 + 子句末 `?` → 疑問詞形（何時／何）
- 其他情境 → 連詞／關係代名詞形（当／其中）

實作：把每行依 `.!?` 切子句記錄結尾；目標詞出現時查所在子句結尾。間接疑問句（`I don't know when he came`）會被誤判為連詞，但讀起來尚可。

### 3.6 Demonstrative（避歧 he / them）

| Eng | 漢字 |
|---|---|
| this | 這 |
| that | 那 |
| these | 這等 |
| those | 那等 |

### 3.7 Prepositions

| Eng | 漢字 | 備註 |
|---|---|---|
| of | （不轉）| |
| in | （不轉）| |
| to | （不轉）| Infinitive `to`（want **to** go）也保留 |
| on | （不轉）| |
| at | （不轉）| |
| for | 為 | |
| with | 与 | 與 and 同字（intentional） |
| from | 从 | |
| by | 以 | |
| about | 関於 | |
| around | 周辺 | |
| into | 入 | |
| through | 經 | |
| between | 間 | 與 during 同字（intentional） |
| **under** | **下於** | 避歧 down→下 |
| **over** | **上於** | 避歧 up→上 |
| after | 後 | |
| before | 前 | |
| **without** | **不与** | with-out → with（与）+ out（不） |
| during | 間 | 與 between 同字（intentional） |
| against | 反対 | |
| among | 其中 | 與 which（關代）同字 |

### 3.8 Conjunctions

| Eng | 漢字 | 備註 |
|---|---|---|
| and | 与 | 與 with 同字（intentional） |
| or | 或 | |
| but | 但 | |
| because | 因為 | |
| if | 若 | |
| when（連詞）| 当 | 詳見 §3.5 啟發式 |
| while | 正当 | |
| although | 雖然 | |
| so | 故 | |
| than | 於 | 與 on/at 同字（intentional）|
| as | 如 | 複合連詞另見附錄 B.2 |
| unless | 除非 | |
| whether | 是否 | |

### 3.9 Auxiliary Verbs

助動詞用單字＋形態學後綴標示時態（`是/是ed/是t`、`有/有ed`、`行/行ed`、`能/能ed`、`将/将ed`、`可/可ed`）。

| Eng | 漢字 | Eng | 漢字 |
|---|---|---|---|
| is / am / are | 是 | will | 将 |
| was / were | 是ed | would | 将ed |
| been | 是t | should | 応 |
| being | 是ing | may | 可 |
| have / has | 有 | might | 可ed |
| had | 有ed | must | 須 |
| do / does | 行 | shall | 宜 |
| did | 行ed | | |
| can | 能 | | |
| could | 能ed | | |

### 3.10 Negation

| Eng | 漢字 |
|---|---|
| not | 不 |
| no | 无 |
| nor | 亦不 |
| never | 从不 |
| none | 无一 |
| neither | 亦不（與 nor 同字，intentional）|

### 3.11 Common Adverbs & Determiners

| Eng | 漢字 | Eng | 漢字 |
|---|---|---|---|
| very | 甚 | every | 每 |
| also / too | 亦 | each | 各 |
| only | 唯一 | other | 其他 |
| just | 僅 | another | 另 |
| all | 全 | same | 相樣 |
| **still** | 仍 | such | 如此 |
| already | 既 | yes | 是 |
| always | 始終 | here | 此処 |
| often | 常常 | there | 彼処（位置）／there（存在句）|
| some | 某 | then | 則 |
| many / much | 多（intentional）| now | 今 |
| **enough** | **足夠**（避歧 foot→足）| again | 再 |
| **yet** | **卻**（避歧 高尚等）| soon | 不久 |
| perhaps | 或許 | quite | 頗為 |
| **together** | **共集** | almost | 幾乎 |

### 3.12 特殊情境

#### Infinitive `to` vs Prepositional `to`

| 情境 | 範例 | 處理 |
|---|---|---|
| 方向／目標 | go **to** London | 至（轉換）|
| 不定式標記 | want **to** go | to（保留英文）|

> 註：`to → 至` 在 §3.7 規則上原為「不轉」，但若帶有方向／目標義（後接名詞）時可使用。實際上由於 `to` 列入不轉清單，多數情境保留英文即可。

#### Existential `there` vs Locative `there`

| 情境 | 範例 | 處理 |
|---|---|---|
| 位置 | I went **there** | 彼処 |
| 存在句 | **There** is a book | there（保留英文）|

### 3.13 不轉清單

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
| Infinitive `to`（位於動詞前）| want **to** go |
| Existential `there`（存在句虛主詞）| **There** is a book |

#### C. 類別保留（依 W6 / W8）

| 類別 | 規則 |
|---|---|
| 西方專有名詞（人名／地名／品牌）| 保留英文（W6）|
| 無 CJK 對應的技術縮寫（DNA／HTTP／API／WiFi）| 保留英文（W8）|

---

## 4. Word Selection 規則

### W1. 具象名詞 — 象形優先 [Hard]
具象名詞優先採象形漢字。例：sun→日、moon→月、water→水、mountain→山。

### W2. 抽象名詞 — 複合詞構造 [Hard]
抽象名詞採既有 CJK 複合詞；無既有複合詞時，組合兩個義符字。例：freedom→自由、knowledge→知識。

### W3. 動詞 — 單字優先 [Hard]
動詞優先單字，後綴附加。例：eat→食、see→見、walk→歩。

### W4. 形容詞 — 詞根＋後綴 [Hard]
形容詞詞根對應漢字，比較級／派生形以後綴附加。例：big→大、beautiful→美的（透過 M2b `-ful → 的`）。

### W5. 功能詞 — 嚴格查表 [Hard]
功能詞嚴格查 §3 對照表，不允許變體。

### W6. 專有名詞 — 保留英文（含 CJK 例外）[Hard]

#### 基底原則
所有專有名詞保留英文（含西方人名、地名、品牌）。

#### CJK 文化圈例外
中日韓越（含港澳臺）原本就以漢字書寫者，使用漢字：

| 類別 | 例 |
|---|---|
| 國名／地區 | 中国、日本、韓国、越南、台湾、香港、澳門、新加坡 |
| 首都／大城市 | 東京、首爾、北京、河內、京都、上海、釜山 |
| 歷史人物 | 孔子、老子、孫逸仙、秀吉 |
| 山河海域 | 富士山、長江、黃海、阿里山 |

#### wordlist 既有對應例外
若 wordlist 已收錄漢字翻譯（例：America→米国、China→中国），則沿用。

#### 西方人名一律保留英文
Einstein、Bach、Newton、Mozart 等（音譯字三地不同，無 pan-CJK 中立解）。

### W7. 數字 — CJK 數字 [Hard]
書寫形式數字用漢字（一／二／三／百／千），年份／日期保留阿拉伯數字。

> 例：Three hundred people gathered on October 15, 2024.
> → 三百 人s 集ed 於 October 十五, 2024.

### W8. 技術術語 — 保留英文（已有 CJK 對應的使用對應）[Soft]
- 無 CJK 對應的縮寫保留英文：DNA、HTTP、API、WiFi 等
- 已有 CJK 對應的術語使用對應：algorithm→演祘法、computer→電脳、telephone→電話

### W9. 字源中立 [Soft]
多個漢字可選時，依序：
1. CJK 三地通用字（與 H2-B 配套）
2. 筆畫較簡（既有結構優先；草書楷化／偏旁簡化字次之）
3. 表意更直接

簡體字若筆畫較簡且有古字來源（非草書楷化或偏旁簡化字），可選用。

### W10. 複合名詞 [Soft]
複合名詞優先採既有 CJK 複合詞；無對應時拆分組合或保留英文。例：sunlight→日光、bookshelf→書棚。

---

## 5. Formatting 規則

### F1. 英文標點 [Hard]
標點符號採英文（`. , ? ! : ; "" ''`），不採中文標點（`。，？！「」：；`）。

### F2. 英文詞距 [Hard]
詞間空格採英文（空格分隔），不採中文連續排版（無空格）。

### F3. 保留文件結構 [Hard]
段落、換行、標題、列表、引用區塊等文件結構保持原樣。

### F4. Hanjified 段落不夾標注 [Hard]
純漢字化段落只包含漢字＋羅馬後綴，不夾帶英文原文或標注；標注一律放在 Ruby 段。

---

## 6. 衝突避歧規則

### 6.1 規則

1. **衝突判定**：function word 的單字漢字若與**詞類／角色不同**的另一高頻詞共用同一漢字 → 衝突
2. **衝突解決**：受影響的 function word 改用雙字漢字（不擾動 content word）
3. **判定範圍**：完全同字才算（不擴及子串／同音）

### 6.2 Intentional homography 例外

下列同字情境**詞類／語意角色相近**，視為刻意的歧義共享：

| 詞對 | 共用字 | 角色 |
|---|---|---|
| on / at | 於 | 位置介詞 |
| between / during | 間 | 時空區間 |
| and / with | 与 | 連結／伴隨 |
| many / much | 多 | 量詞 |
| but / yes | 然 | 轉折／肯定 |

### 6.3 已處理衝突清單

| Function word | 衝突對象 | 改用 |
|---|---|---|
| under | down（副詞）| 下於 |
| over | up（副詞）| 上於 |
| enough | foot（名詞）| 足夠 |
| yet | 高尚／時尚等 | 卻 |

新衝突在使用回報後追加處理。

### 6.4 字母當量

每 1 漢字 ≈ 3 字母當量。長單字雙字規則：英文字母數 ÷ 漢字當量 ≥ 2 時可使用雙字漢字。

例：`because`(7) / `因`(3 當量) = 2.33 ≥ 2 → 用「因為」(7/6=1.17 OK)

例外：位置介詞 under/over 即使比例未達 2 仍用雙字（屬 6.3 衝突避歧）。

---

## 7. 附錄 A：常見不規則動詞表（M3 適用）

過去式與過去分詞統一用 `-t` 標記（M9 規定過去分詞作形容詞時亦用 `-t`，不另設 `-n`）。

| 原型 | 漢字 | 過去式 | 過去分詞 |
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

---

## 8. 附錄 B：常見片語表（M8 適用）

### B.1 片語動詞

| 片語 | 漢字 | 範例 |
|---|---|---|
| give up | 放棄 | She gave up → 伊 放棄ed |
| break down | 崩壊 | The car broke down → the 車 崩壊ed |
| look for | 探 | I look for it → 予 探 它 |
| find out | 発見 | We found out → 吾等 発見t |
| carry out | 執行 | They carried out → 彼等 執行ed |
| turn off | 消 | Turn off the light → 消 the 光 |
| set up | 設立 | They set up → 彼等 設立ed |
| pick up | 拾 | Pick up the book → 拾 the 書 |
| make up | 構成 | Words make up sentences → 詞s 構成 句s |
| point out | 指摘 | He pointed out → 彼 指摘ed |
| bring up | 提起 | She brought up → 伊 提起t |
| come back | 帰 | They came back → 彼等 帰t |

### B.2 連詞片語（`as X as` 系列）

`as` 在複合連詞中採字面拆字升級為片語，wordlist 以 multi-word entry 收錄：

| 片語 | 漢字 | 範例 |
|---|---|---|
| as well as | 如善如 | Tom 喜s 苹果s **如善如** 香蕉s. |
| as long as | 如長如 | 予 留t **如長如** 予 能. |
| as soon as | 如即如 | 来 **如即如** 可能. |
| as much as | 如多如 | 予 食t **如多如** 予 欲t. |
| as many as | 如多如 | (同上) |
| as far as | 如远如 | 予 知 **如远如** ... |
| as if | 如若 | 它 看ed **如若** 真. |
| as though | 如雖 | (同上) |

> 設計理念：以漢字逐字對應英文結構，讀者識得 `as X as` 即可解讀 `如X如`。不嘗試翻譯為 CJK 慣用語（如 `並且／只要`），保持「結構對應」純粹性。

---

## 9. 附錄 C：字形採用清單

### 9.1 採用字形清單（繁體 → 採用）

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

### 9.2 不簡化清單（明確保留繁體）

`黑、動、傳、隊、鄰、勝、華、畢、風、圍、織、識、圖、線、筆`

### 9.3 個別選字原則

當待採字形需要選擇時，依序考量：

1. 符合本意或符合古字
2. 結構簡單（既有結構，筆畫數不重要）
3. 通用元件
4. 順筆與否
5. 是否既有俗字
6. CJK 三地通用優先（W9 / H2-B 配套）

---

## 10. 階段二修整待辦

凍結 spec.md 後，依下表對 wordlist.js / index.html / SKILL.md / READMEs 進行修整。

### 10.1 wordlist.js 字形混用修整

| 繁／採用混用 | 修為 |
|---|---|
| 對／対／对 | 対 |
| 時／时 | 时 |
| 經／経 | 経 |
| 來／来 | 来 |
| 選／选 | 选 |
| 遠／远 | 远 |
| 電／电 | 电 |
| 雞／鷄 | 鷄 |
| 筆／笔 | 筆（不簡化）|
| 將／将 | 将（you'll → 您将）|

### 10.2 wordlist.js Function Word bug 修正

修正 §H4 列出的 7 個多義誤對應：

| 詞 | 原 wordlist | 修為 |
|---|---|---|
| mine | 礦井 | 予之 |
| still | 安靜 | 仍 |
| during | 期間 | 間 |
| into | 成 | 入 |
| under | 根據 | 下於 |
| over | 越過 | 上於 |
| without | 不帶 | 不与 |

### 10.3 wordlist.js Function Word 全表寫入

依 §3 對照表，補入 web tool 缺漏的 64 條 function word（冠詞、助動詞、否定詞、多數副詞），並修正既有與規範不一致的 56 條。

### 10.4 wordlist.js 派生詞重審

依 §M2b / §M2c 規則，重審 1,010 個派生後綴詞 + 334 個前綴詞（共佔 wordlist 的 28%），LLM 工具輔助生成差異報告，人工裁定後寫入。

### 10.5 index.html 轉換邏輯擴充

- 補擴 suffix 列表（覆蓋 §M2a 屈折＋ §M2b 派生）
- 新增不規則動詞表查表（附錄 A）
- 縮寫展開預處理（M7）
- 啟發式分流（when / which，§3.5）
- 不轉清單檢查（§3.13）

### 10.6 SKILL.md 同步重寫

依本規範重寫 SKILL.md M2 章節（採 C1-C 混合方案），其餘章節對照本規範同步調整。

### 10.7 READMEs 引用本規範

`~/works/hanjify/README*.md` 與 `~/works/skills/hanjify/README.md` 加上本規範引用。

### 10.8 驗收

用 `~/works/skills/hanjify/test-samples/little-prince.md` 跑 web tool 驗收，比對 `little-prince_hanjified.md`，差異應只剩內容詞層面，function word 完全一致。
