# Wordlist 派生詞重審報告

> 來源：`tools/audit_derivations.py` 對 wordlist.js 跑過一次 spec §M2b/§M2c 規則對照

## 摘要

### Suffix 後綴 (M2b)
- 總候選：320
- OK（已合規）：69
- SAFE（單字元差異，自動套用）：0
- LIKELY（部分重疊，需審視）：65
- UNCERTAIN（差異大，跳過）：186

### Prefix 前綴 (M2c)
- 總候選：61
- OK（已合規）：14
- SAFE（自動套用）：0
- LIKELY（部分重疊，需審視）：3
- UNCERTAIN（差異大，跳過）：44

## 自動套用變更（共 0 條）


## LIKELY 候選（68 條，需人工裁定）

LIKELY 表示 current 與 expected 有顯著重疊（共字 ≥ 50%）但非單字元差異。
可能是：(a) 慣用 CJK 複合詞（M2d 應保留）、(b) 應該手工調整、(c) 詞典 bug

| 英文 | 原 | 提議 | root | 後綴／前綴 |
|---|---|---|---|---|
| `accurately` | 精確地 | 精確的地 | `accurate` | `ly` |
| `actually` | 实際地 | 实際的地 | `actual` | `ly` |
| `anywhere` | 任何処 | 任処 | `any` | `where` |
| `arrival` | 到着 | 到着的 | `arrive` | `al` |
| `changeable` | 可変的 | 変換的 | `change` | `able` |
| `classical` | 古典的 | 経典的 | `classic` | `al` |
| `colorful` | 多彩的 | 彩的 | `color` | `ful` |
| `commonly` | 一般地 | 一般的地 | `common` | `ly` |
| `completely` | 完全地 | 完璧地 | `complete` | `ly` |
| `daily` | 每日 | 日地 | `day` | `ly` |
| `dangerous` | 危険 | 危険的 | `danger` | `ous` |
| `effectively` | 効果地 | 効果的地 | `effective` | `ly` |
| `electrical` | 电気的 | 电的 | `electric` | `al` |
| `employer` | 雇用者 | 用者 | `employ` | `er` |
| `entirely` | 完全地 | 全体地 | `entire` | `ly` |
| `exactly` | 正是地 | 正確地 | `exact` | `ly` |
| `extremely` | 極地 | 極端地 | `extreme` | `ly` |
| `finally` | 終於地 | 最終地 | `final` | `ly` |
| `freezer` | 冷凍庫 | 冷凍者 | `freeze` | `er` |
| `gradually` | 逐漸地 | 漸進的地 | `gradual` | `ly` |
| `handful` | 满手的 | 手的 | `hand` | `ful` |
| `harmful` | 有害 | 害的 | `harm` | `ful` |
| `heater` | 加熱 | 熱者 | `heat` | `er` |
| `highly` | 高度地 | 高地 | `high` | `ly` |
| `historical` | 歷史的 | 歷史的的 | `historic` | `al` |
| `hourly` | 毎时地 | 时地 | `hour` | `ly` |
| `immediately` | 立即地 | 即时地 | `immediate` | `ly` |
| `initially` | 当初地 | 初回地 | `initial` | `ly` |
| `legal` | 法的 | 腳的 | `leg` | `al` |
| `lively` | 快活地 | 生活地 | `live` | `ly` |
| `loser` | 敗者 | 失者 | `lose` | `er` |
| `lower` | 降低 | 低者 | `low` | `er` |
| `mailman` | 郵便配达人 | 郵便人 | `mail` | `man` |
| `meaningful` | 有意義的 | 意味的 | `meaning` | `ful` |
| `musical` | 音楽劇的 | 音楽的 | `music` | `al` |
| `naturally` | 自然地 | 自然的地 | `natural` | `ly` |
| `nearly` | 近乎地 | 近地 | `near` | `ly` |
| `necessarily` | 必然地 | 必要地 | `necessary` | `ly` |
| `normally` | 普通地 | 通常地 | `normal` | `ly` |
| `novelist` | 小說家 | 小説家 | `novel` | `ist` |
| `painful` | 痛苦的 | 痛的 | `pain` | `ful` |
| `particularly` | 特別地 | 特殊地 | `particular` | `ly` |
| `partly` | 一部地 | 部分地 | `part` | `ly` |
| `policeman` | 警人 | 警察人 | `police` | `man` |
| `postman` | 郵人 | 郵寄人 | `post` | `man` |
| `potter` | 陶者 | 鍋者 | `pot` | `er` |
| `prayer` | 祈禱 | 祈禱者 | `pray` | `er` |
| `previously` | 之前地 | 前的地 | `previous` | `ly` |
| `protective` | 保護的 | 保障的 | `protect` | `ive` |
| `really` | 真的地 | 真正的地 | `real` | `ly` |
| `reasonable` | 合理的 | 理由的 | `reason` | `able` |
| `receiver` | 接収器 | 接収者 | `receive` | `er` |
| `recently` | 最近 | 最近地 | `recent` | `ly` |
| `regardless` | 无論的 | 无尊重的 | `regard` | `less` |
| `relatively` | 比較的地 | 相対的地 | `relative` | `ly` |
| `reliable` | 可靠的 | 依靠的 | `rely` | `able` |
| `roller` | 滾子 | 滾者 | `roll` | `er` |
| `singer` | 歌者 | 歌唱者 | `sing` | `er` |
| `slowly` | 慢慢地 | 慢地 | `slow` | `ly` |
| `smaller` | 較小 | 小者 | `small` | `er` |
| `successfully` | 成功地 | 成功的地 | `successful` | `ly` |
| `supporter` | 支持者 | 支援者 | `support` | `er` |
| `traditionally` | 伝統地 | 伝統的地 | `traditional` | `ly` |
| `usually` | 通常 | 通常地 | `usual` | `ly` |
| `winner` | 勝者 | 贏者 | `win` | `er` |
| `renew` | 更新 | 再新 | `new` | `re` |
| `sometime` | 某时 | 某时間 | `time` | `some` |
| `unreasonable` | 不理可 | 不合理的 | `reasonable` | `un` |

## UNCERTAIN 候選（230 條，已跳過，僅供參考）

UNCERTAIN 多為 false positive（如 corner→玉米者、dollar→娃娃者：英文詞尾形式碰巧匹配 suffix，但語意無關）。

| 英文 | 原 | 提議（已跳過）|
|---|---|---|
| `active` | 活動的 | 演的 |
| `annually` | 毎年 | 年次地 |
| `apparently` | 似乎地 | 明白地 |
| `approval` | 承認 | 批准的 |
| `barely` | 勉强地 | 裸地 |
| `beaker` | 燒杯 | 喙者 |
| `broker` | 経紀商 | 无一文者 |
| `builder` | 建築工人 | 建立者 |
| `burial` | 葬 | 埋葬的 |
| `burner` | 燃燒器 | 燒傷者 |
| `businessman` | 商人 | 生意人 |
| `capable` | 有能的 | 上限的 |
| `career` | 職業 | 車師 |
| `careful` | 慎重的 | 关懷的 |
| `careless` | 跅的 | 无关懷的 |
| `carrier` | 載体 | 送者 |
| `carter` | 馬伕 | 手推車者 |
| `center` | 中心 | 分者 |
| `central` | 中央 | 中心的 |
| `cheerful` | 陽気的 | 歓声的 |
| `clearly` | 顕然地 | 清除地 |
| `closely` | 密切地 | 关閉地 |
| `closer` | 更密切 | 关閉者 |
| `comfortable` | 快適的 | 寬服的 |
| `conductor` | 驅動程式 | 行動者 |
| `considerable` | 相当的 | 認为的 |
| `controversial` | 有争议 | 論争的 |
| `conventional` | 従来型 | 慣習的 |
| `corner` | 角 | 玉米者 |
| `countable` | 数可 | 點祘的 |
| `creative` | 有創意的 | 作成的 |
| `creator` | 創始者 | 作成者 |
| `creeper` | 匍匐茎 | 爬行者 |
| `currently` | 現在地 | 當下地 |
| `customer` | 客 | 習慣者 |
| `deal` | 取引 | de的 |
| `dealer` | 経銷商 | 取引者 |
| `dear` | 亲愛 | de者 |
| `deer` | 鹿 | de者 |
| `desirable` | 合意的 | 欲望的 |
| `dial` | 撥號 | 翹辮子的 |
| `director` | 董事 | 直接者 |
| `dollar` | 美元 | 娃娃者 |
| `drawer` | 出票人 | 汲取者 |
| `dresser` | 建 | 穿衣者 |
| `driver` | 驅動程式 | 駕駛者 |
| `dropper` | 滴管 | 滴劑者 |
| `duster` | 撣子 | 灰塵者 |
| `earlier` | 早更 | 早者 |
| `early` | 早 | 耳地 |
| ... | ... | (and 180 more) |
