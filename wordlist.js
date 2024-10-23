const wordList = {
  "able": "能",
  "acid": "酸",
  "again": "再",
  "air": "气",
  "all": "全",
  "amount": "量",
  "angle": "角",
  "animal": "動物",
  "angry": "怒",
  "any": "任",
  "apple": "柰",
  "arch": "拱",
  "argument": "論",
  "arm": "武",
  "army": "武軍",
  "art": "芸術",
  "automatic": "自動",
  "April": "4月",
  "arithmetic": "祘術",
  "August": "8月",
  "acceleration": "加速",
  "age": "年齢",
  "also": "还",
  "amplitude": "振幅",
  "ankle": "踝",
  "approximation": "近似值",
  "arbitration": "仲裁",
  "arbitrary": "任意",
  "asset": "資產",
  "assistant": "協作員",
  "average": "平均",
  "axis": "軸",
  "airplane": "气机",
  "another": "另",
  "anybody": "任体",
  "anyhow": "任如何",
  "anyone": "任一",
  "anything": "任物",
  "anywhere": "任何処",
  "acting": "演技",
  "balance": "平衡",
  "ball": "球",
  "basket": "籃",
  "beautiful": "美的",
  "bed": "床",
  "bee": "蜂",
  "berry": "莓",
  "bird": "鳥",
  "bite": "咬",
  "bitter": "苦",
  "black": "黑",
  "blood": "血液",
  "body": "体",
  "bone": "骨",
  "book": "書",
  "boiling": "沸騰",
  "bottle": "瓶",
  "box": "箱",
  "branch": "枝",
  "brass": "黃銅",
  "brick": "磚",
  "bridge": "橋",
  "brother": "兄弟",
  "brush": "刷",
  "bucket": "桶",
  "bulb": "灯泡",
  "button": "鈕",
  "butter": "黄油",
  "bank": "川岸",
  "beef": "牛肉",
  "beer": "麦酒",
  "biology": "生物斈",
  "bankrupt": "破產",
  "beard": "髯",
  "break": "休断",
  "breakfast": "休断斋",
  "breast": "乳房",
  "bubble": "泡沫",
  "buoyancy": "浮力",
  "burial": "葬",
  "busy": "忙",
  "bedroom": "床室",
  "blackberry": "黑莓",
  "blackbird": "黑鳥",
  "cake": "糕",
  "card": "卡",
  "cat": "猫",
  "cause": "原因",
  "change": "変換",
  "chemical": "化斈",
  "chest": "胸",
  "circle": "円",
  "cloth": "衣",
  "clock": "时計",
  "cloud": "云",
  "cold": "冷",
  "collar": "領",
  "color": "彩",
  "come": "来",
  "comfort": "寬服",
  "committee": "委員会",
  "complete": "完璧",
  "conscious": "意識",
  "control": "控制",
  "cook": "料理",
  "copper": "銅",
  "copy": "複製",
  "cork": "軟木",
  "cough": "咳",
  "cow": "母牛",
  "crime": "犯罪",
  "cup": "杯",
  "current": "當下",
  "cut": "切",
  "check": "確可",
  "chemist": "化斈家",
  "chemistry": "化斈",
  "chorus": "合唱",
  "cocktail": "鷄尾",
  "cognac": "干邑",
  "calculation": "計祘",
  "capital": "資本",
  "carpet": "毯",
  "case": "案",
  "chair": "椅",
  "china": "中国",
  "choice": "選択",
  "civilization": "文明",
  "clay": "粘土",
  "client": "顧客",
  "climber": "登上者",
  "code": "代号",
  "collision": "衝突",
  "column": "列",
  "combination": "組合",
  "consumer": "消費者",
  "contour": "概要",
  "cool": "涼",
  "cost": "費用",
  "clockwork": "时計作",
  "clothing": "衣物",
  "cooker": "料理者",
  "damage": "損傷",
  "dark": "暗",
  "day": "日",
  "dear": "亲愛",
  "deep": "深",
  "degree": "程度",
  "design": "設計",
  "different": "差異",
  "digestion": "消化",
  "direction": "方向",
  "dirty": "污",
  "discussion": "討論",
  "distance": "距离",
  "dog": "犬",
  "door": "門",
  "down": "下",
  "doubt": "疑",
  "drink": "飲",
  "December": "12月",
  "decrease": "減少",
  "denominator": "分母",
  "department": "部門",
  "density": "密度",
  "difference": "差異",
  "ditch": "溝",
  "divorce": "离婚",
  "dream": "梦",
  "daylight": "日光",
  "ear": "耳",
  "early": "早",
  "earth": "地",
  "east": "東",
  "education": "教育",
  "egg": "卵",
  "electric": "電",
  "ever": "常",
  "every": "每",
  "existence": "存在",
  "expert": "專家",
  "eye": "目",
  "eight": "八",
  "eleven": "十一",
  "easy": "易",
  "economy": "経済",
  "enemy": "敵",
  "environment": "环境",
  "equation": "方程式",
  "export": "出埠",
  "eyebrow": "眉毛",
  "eyelash": "睫毛",
  "earthwork": "地作",
  "evergreen": "常青",
  "everybody": "每体",
  "everyday": "每日",
  "everyone": "每一",
  "everything": "每物",
  "everywhere": "每何処",
  "eyeball": "目球",
  "far": "遠",
  "farm": "農",
  "father": "父",
  "feather": "羽",
  "female": "女性",
  "finger": "指",
  "fire": "火",
  "first": "第一",
  "fish": "魚",
  "flag": "旗",
  "flight": "飛行",
  "flower": "花",
  "friend": "友",
  "fruit": "果",
  "future": "未来",
  "February": "2月",
  "fifteen": "十五",
  "fifth": "第五",
  "fifty": "五十",
  "five": "五",
  "four": "四",
  "fourteen": "十四",
  "fourth": "第四",
  "forty": "四十",
  "Friday": "金曜日",
  "failure": "失敗",
  "fertilizing": "施肥",
  "flood": "洪水",
  "friction": "摩擦",
  "fur": "毛",
  "furniture": "家具",
  "fatherland": "父土地",
  "fingerprint": "指印",
  "firearm": "火武",
  "firefly": "火飛",
  "fireman": "火人",
  "firework": "火作",
  "football": "足球",
  "footlights": "足光",
  "footnote": "足注",
  "footprint": "足印",
  "footstep": "足步",
  "farmer": "農者",
  "fired": "解雇",
  "firing": "射火",
  "general": "一般",
  "give": "給与",
  "goat": "山羊",
  "gold": "金",
  "good": "好",
  "government": "政府",
  "grain": "穀",
  "grass": "草",
  "gray": "灰",
  "guide": "概導",
  "geography": "地理",
  "geology": "地質斈",
  "geometry": "几何斈",
  "gate": "閘",
  "glacier": "氷河",
  "grand": "宏大",
  "grief": "悲",
  "ground": "地面",
  "guess": "猜",
  "goldfish": "金魚",
  "gunpowder": "火薬",
  "hair": "髮",
  "hand": "手",
  "happy": "喜",
  "hard": "硬",
  "hat": "帽",
  "hate": "憎",
  "have": "有",
  "healthy": "健康的",
  "heart": "心",
  "heat": "熱",
  "help": "助",
  "high": "高",
  "history": "歷史",
  "hole": "穴",
  "hope": "希望",
  "horse": "馬",
  "hour": "时",
  "how": "如何",
  "hundred": "百",
  "heavy": "重",
  "hill": "丘",
  "honey": "蜜",
  "hoof": "蹄",
  "husband": "夫",
  "highlands": "高土地",
  "highway": "高道",
  "horseplay": "馬遊",
  "horsepower": "馬力",
  "hourglass": "时玻璃",
  "however": "如何常",
  "I": "予",
  "ice": "氷",
  "ill": "恙",
  "important": "重要",
  "increase": "增加",
  "ink": "墨",
  "insect": "昆虫",
  "iron": "鉄",
  "island": "島",
  "international": "国際",
  "import": "入埠",
  "integer": "整数",
  "investigation": "調查",
  "investment": "投資",
  "indoors": "室內",
  "inland": "內陸",
  "jewel": "宝石",
  "journey": "旅",
  "January": "1月",
  "July": "7月",
  "June": "6月",
  "knee": "膝",
  "king": "王",
  "kidney": "腎",
  "land": "土地",
  "language": "語言",
  "law": "律令",
  "learning": "斈習",
  "leg": "腳",
  "less": "少",
  "left": "左",
  "light": "光",
  "lip": "唇",
  "list": "列単",
  "little": "小少",
  "long": "長",
  "loss": "損失",
  "love": "愛",
  "low": "低",
  "latitude": "緯度",
  "lava": "熔岩",
  "longitude": "経度",
  "lake": "湖",
  "lamp": "灯",
  "length": "長度",
  "liver": "肝",
  "machine": "机械",
  "male": "男性",
  "material": "材料",
  "mass": "質量",
  "military": "軍事",
  "milk": "奶",
  "mind": "心",
  "monkey": "猴",
  "month": "月",
  "moon": "月",
  "mother": "母",
  "mountain": "山",
  "mouth": "口",
  "much": "多",
  "music": "音楽",
  "March": "3月",
  "May": "5月",
  "micro-": "微",
  "Monday": "月曜日",
  "museum": "博物館",
  "many": "許多",
  "marble": "大理石",
  "marriage": "婚",
  "metabolism": "代謝",
  "mixture": "混合物",
  "moral": "道德",
  "mud": "泥",
  "name": "名",
  "narrow": "狭",
  "necessary": "必要",
  "needle": "針",
  "net": "网",
  "new": "新",
  "news": "新聞",
  "night": "夜",
  "north": "北",
  "nose": "鼻",
  "now": "今",
  "neutron": "中子",
  "nine": "九",
  "November": "11月",
  "numerator": "分子",
  "network": "网作",
  "newspaper": "新聞紙",
  "nothing": "无物",
  "noted": "著名",
  "oil": "油",
  "operation": "操作",
  "opinion": "意見",
  "other": "其他",
  "October": "10月",
  "one": "一",
  "organism": "有机体",
  "offspring": "子孫",
  "outlook": "展望",
  "page": "頁",
  "pain": "痛",
  "paper": "紙",
  "past": "過去",
  "pen": "筆",
  "picture": "写真",
  "pig": "豚",
  "play": "遊",
  "poison": "毒",
  "polish": "磨光",
  "political": "政治的",
  "poor": "貧",
  "position": "位置",
  "possible": "可能",
  "pot": "鍋",
  "print": "印",
  "produce": "生產",
  "prose": "散文",
  "pull": "拉",
  "purpose": "目的",
  "push": "推",
  "passport": "通埠",
  "Physics": "物理斈",
  "Physiology": "生理斈",
  "platinum": "白金",
  "police": "警察",
  "Psychology": "心理斈",
  "particle": "粒子",
  "path": "径",
  "people": "人民",
  "pool": "池",
  "population": "人口",
  "pressure": "压力",
  "proof": "証明",
  "purchase": "購",
  "pure": "純",
  "plaything": "遊物",
  "policeman": "警人",
  "postman": "郵人",
  "painting": "絵者",
  "pointer": "点者",
  "potter": "陶者",
  "printer": "印者",
  "prisoner": "囚者",
  "producer": "生產者",
  "question": "問題",
  "queen": "皇后",
  "quantity": "数量",
  "rain": "雨",
  "rat": "大鼠",
  "red": "赤",
  "reason": "理由",
  "regret": "悔",
  "religion": "宗教",
  "respect": "尊敬",
  "reward": "報酬",
  "rhythm": "律奏",
  "rice": "米",
  "right": "右",
  "ring": "环",
  "river": "河川",
  "road": "路",
  "roll": "滾",
  "room": "室",
  "root": "根",
  "run": "走",
  "radium": "鐳",
  "rectangle": "矩形",
  "repair": "修理",
  "resolution": "決議",
  "result": "結果",
  "rich": "富",
  "rigidity": "剛性",
  "rude": "無礼",
  "sad": "悲",
  "safe": "安全",
  "salt": "塩",
  "same": "相樣",
  "school": "斈校",
  "science": "科斈",
  "sea": "海",
  "seat": "席",
  "second": "第二",
  "secret": "秘",
  "secretary": "秘書",
  "seed": "種",
  "sense": "感斍",
  "shelf": "棚",
  "short": "短",
  "side": "側",
  "silk": "絲",
  "silver": "銀",
  "simple": "簡",
  "sister": "姐妹",
  "size": "幅",
  "sleep": "睡眠",
  "small": "小",
  "snow": "雪",
  "society": "社会",
  "soft": "軟",
  "song": "歌",
  "south": "南",
  "spring": "春",
  "square": "方形",
  "star": "星",
  "steam": "蒸气",
  "step": "步",
  "stomach": "胃",
  "stone": "石",
  "stop": "停止",
  "story": "事語",
  "strange": "怪奇",
  "street": "街",
  "sugar": "糖",
  "summer": "夏",
  "sun": "日",
  "swim": "泳",
  "Saturday": "土曜日",
  "September": "9月",
  "serum": "血清",
  "seven": "七",
  "six": "六",
  "sixteen": "十六",
  "sport": "運動",
  "Sunday": "日曜日",
  "sac": "袋",
  "schist": "片岩",
  "security": "安全",
  "selfish": "私利己",
  "sentence": "文句",
  "share": "共有",
  "shear": "剪断",
  "shoulder": "肩",
  "show": "秀",
  "similarity": "相似性",
  "skull": "頭蓋骨",
  "social": "社交",
  "statistics": "統計",
  "study": "研究",
  "success": "成功",
  "surface": "表面",
  "shorthand": "短手",
  "sidewalk": "側行",
  "somebody": "某体",
  "someday": "某日",
  "somehow": "某如何",
  "someone": "某一",
  "something": "某物",
  "sometime": "某时",
  "somewhat": "某何",
  "somewhere": "某何処",
  "sunlight": "阳光",
  "table": "桌",
  "tail": "尾",
  "take": "取",
  "tall": "高",
  "tax": "稅",
  "that": "彼",
  "theory": "理論",
  "thick": "厚",
  "thin": "薄",
  "thing": "物",
  "this": "此",
  "thought": "思想",
  "thread": "緒",
  "throat": "喉",
  "thunder": "雷",
  "time": "时間",
  "tin": "錫",
  "toe": "趾",
  "tongue": "舌",
  "town": "鎮",
  "tree": "木",
  "true": "真",
  "tea": "茶",
  "ten": "十",
  "third": "第三",
  "thirteen": "十三",
  "thirty": "三十",
  "thousand": "千",
  "three": "三",
  "Thursday": "木曜日",
  "torpedo": "魚雷",
  "Tuesday": "火曜日",
  "twelve": "十二",
  "twenty": "二十",
  "two": "二",
  "thickness": "厚度",
  "tide": "潮汐",
  "transparent": "透明",
  "travel": "旅行",
  "today": "今日",
  "tonight": "今夜",
  "umbrella": "傘",
  "unit": "单位",
  "up": "上",
  "use": "使用",
  "university": "大斈",
  "understanding": "理解",
  "universe": "宇宙",
  "unknown": "未明",
  "uptake": "上取",
  "violent": "暴力",
  "vapor": "漫蒸气",
  "velocity": "速度",
  "victory": "勝利",
  "vote": "票",
  "walk": "行",
  "wall": "墻",
  "war": "战",
  "warm": "暖",
  "water": "水",
  "wave": "波",
  "wax": "蜡",
  "way": "道",
  "weather": "天气",
  "week": "曜期",
  "weight": "重量",
  "west": "西",
  "what": "何",
  "when": "何时",
  "where": "何処",
  "while": "正当",
  "whistle": "哨",
  "white": "白",
  "who": "誰",
  "why": "何故",
  "wide": "寬",
  "wind": "風",
  "wine": "葡萄酒",
  "winter": "冬",
  "wood": "木材",
  "wool": "羊毛",
  "work": "工作",
  "worm": "蠕虫",
  "wound": "傷",
  "Wednesday": "水曜日",
  "wife": "妻",
  "world": "卋界",
  "waterfall": "水落",
  "weekend": "曜末",
  "whatever": "何常",
  "whenever": "何时常",
  "wherever": "何処常",
  "whitewash": "白洗",
  "whoever": "誰常",
  "woodwork": "木作",
  "year": "年",
  "yellow": "黃",
  "yesterday": "昨日",
  "you": "尔",
  "zinc": "鋅",
  "zoology": "動物斈",
  "yearbook": "年書",
  "colour": "彩",
  "grey": "灰",
  "citation": "引用",
  "during": "期間",
  "city": "市",
  "century": "卋紀",
  "using": "使用",
  "usually": "通常",
  "given": "給定",
  "single": "单",
  "similar": "相似",
  "we": "吾等",
  "created": "作成",
  "works": "作品",
  "continued": "継続",
  "team": "隊",
  "produced": "生產",
  "national": "国的",
  "version": "版本",
  "taken": "採取",
  "standard": "標準",
  "typically": "通常",
  "increased": "增加",
  "economic": "経済",
  "lost": "失",
  "changes": "変更",
  "research": "研究",
  "started": "开始",
  "player": "遊者",
  "limited": "限",
  "elements": "元素",
  "official": "公方",
  "students": "斈生",
  "method": "方法",
  "results": "結果",
  "influence": "影響",
  "culture": "文化",
  "problem": "難題",
  "action": "行動",
  "better": "良",
  "create": "作成",
  "formed": "形成",
  "chinese": "中国的",
  "cities": "市",
  "computer": "計祘者",
  "beginning": "始",
  "already": "既",
  "done": "完成",
  "books": "書籍",
  "rules": "規則",
  "methods": "方法",
  "decided": "決定",
  "japanese": "日本的",
  "relationship": "关係",
  "provides": "提供",
  "text": "文",
  "completed": "完成",
  "ability": "能力",
  "health": "健康",
  "highest": "最高",
  "elected": "选出",
  "adopted": "採用",
  "center": "中心",
  "individuals": "个人",
  "fail": "失敗",
  "resulting": "結果",
  "continue": "継続",
  "japan": "日本",
  "video": "影",
  "prevent": "防",
  "equipment": "設俻",
  "materials": "材料",
  "stories": "事語",
  "analysis": "分析",
  "activities": "活動",
  "report": "報告",
  "offered": "提供",
  "historical": "歷史的",
  "ancient": "古先",
  "cultural": "文化的",
  "unique": "独特",
  "plants": "植物",
  "causes": "原因",
  "efforts": "努力",
  "car": "車",
  "proved": "得証",
  "despite": "尽管",
  "management": "管理",
  "maximum": "最大",
  "weapons": "武器",
  "actions": "行動",
  "county": "県",
  "literature": "文斈",
  "centuries": "卋紀",
  "shape": "形状",
  "command": "命令",
  "recently": "最近",
  "think": "想思",
  "typical": "典型的",
  "external": "外部",
  "architecture": "建築",
  "importance": "重要性",
  "leader": "領袖",
  "purposes": "目的",
  "rare": "稀",
  "student": "斈生",
  "philosophy": "哲斈",
  "lives": "生活",
  "zero": "零",
  "territory": "領土",
  "freedom": "自由",
  "coast": "海岸",
  "begin": "始",
  "arms": "武器",
  "figures": "数字",
  "climate": "气候",
  "shared": "共有",
  "movie": "映画",
  "usage": "使用",
  "ensure": "確保",
  "indicate": "表示",
  "oldest": "最老",
  "portion": "部分",
  "height": "高度",
  "author": "作者",
  "hot": "熱",
  "expensive": "貴",
  "background": "背景",
  "job": "仕事",
  "writers": "作家",
  "big": "大",
  "permanent": "永久",
  "strategy": "策略",
  "elections": "选举",
  "household": "家庭",
  "atoms": "原子",
  "impossible": "不可能",
  "principles": "原則",
  "earliest": "最早",
  "district": "区",
  "task": "任务",
  "voltage": "電压",
  "arts": "芸術",
  "kill": "杀",
  "tool": "工具",
  "opportunity": "机会",
  "cultures": "文化",
  "molecules": "分子",
  "politics": "政治",
  "affect": "影響",
  "governments": "政府",
  "fundamental": "基本的",
  "try": "試",
  "artist": "芸術家",
  "protein": "蛋白質",
  "ideal": "理想的",
  "quantum": "量子",
  "audio": "音",
  "logic": "理則",
  "criticism": "批評",
  "huge": "巨大",
  "mechanical": "机械的",
  "instructions": "指示",
  "prominent": "著名",
  "attended": "出席",
  "electron": "電子",
  "village": "村",
  "detailed": "詳細",
  "learn": "斈",
  "lowest": "最低",
  "mathematical": "数斈的",
  "constitution": "憲法",
  "orbit": "軌道",
  "lands": "土地",
  "matters": "事項",
  "populations": "人口",
  "legislation": "立法",
  "fine": "佳",
  "indicated": "表示",
  "traditions": "伝統",
  "scientists": "科斈家",
  "kingdom": "王国",
  "vector": "矢量",
  "cancer": "癌",
  "responsibility": "責任",
  "historians": "歴史家",
  "novels": "小説",
  "weapon": "武器",
  "forest": "森林",
  "vertical": "垂直",
  "conference": "会議",
  "printing": "印刷",
  "depth": "深度",
  "criminal": "犯罪",
  "identical": "一同的",
  "convention": "慣習",
  "uniform": "制服",
  "bear": "熊",
  "invasion": "侵",
  "disk": "碟",
  "regard": "尊重",
  "incident": "事件",
  "biological": "生物斈的",
  "damaged": "破損",
  "prove": "証明",
  "option": "選項",
  "association": "協会",
  "beliefs": "信念",
  "stores": "店",
  "league": "联盟",
  "drugs": "薬物",
  "pitch": "音高",
  "comic": "漫画",
  "web": "网",
  "lose": "失",
  "divisions": "部門",
  "farmers": "農民",
  "themes": "主題",
  "youth": "青年",
  "historic": "歷史的",
  "superior": "優",
  "soul": "魂",
  "infantry": "步兵",
  "random": "无作为",
  "proposal": "提案",
  "waters": "水域",
  "foundation": "基礎",
  "doctrine": "教義",
  "meetings": "会議",
  "railway": "鉄道",
  "isolated": "孤立",
  "downtown": "下鎮",
  "editor": "編集者",
  "challenge": "挑战",
  "classification": "分类",
  "phenomenon": "現象",
  "responded": "回答",
  "horses": "馬",
  "notion": "概念",
  "musicians": "音楽家",
  "vacuum": "真空",
  "organisms": "生物",
  "cited": "引用",
  "execution": "執行",
  "creates": "作成",
  "remote": "遠",
  "differ": "相異",
  "precise": "精密",
  "customer": "客",
  "airport": "气埠",
  "denied": "否定",
  "satellite": "衛星",
  "quantities": "数量",
  "societies": "社会",
  "annually": "毎年",
  "lifetime": "終生涯",
  "regime": "政府体制",
  "honor": "名誉",
  "surfaces": "表面",
  "separation": "分离",
  "variables": "変数",
  "aim": "目的",
  "legs": "腳",
  "enemies": "敵",
  "objective": "目標",
  "rear": "後部",
  "ocean": "洋",
  "row": "行",
  "Mars": "火星",
  "Microsoft": "微軟",
  "emerged": "出現",
  "emperor": "皇帝",
  "voting": "投票",
  "supporter": "支持者",
  "recognize": "認識",
  "revolution": "革命",
  "binary": "二元",
  "injury": "傷",
  "animation": "動画",
  "ape": "猿",
  "artificial": "人工的",
  "awful": "糟糕的",
  "beauty": "美",
  "biracial": "二種族的",
  "boar": "豬",
  "bug": "虫",
  "bull": "公牛",
  "candy": "菓",
  "cattle": "牛",
  "chicken": "鷄",
  "deer": "鹿",
  "dentist": "歯医者",
  "dolphin": "海豚",
  "drake": "公鴨",
  "duck": "鴨",
  "duckling": "鴨仔",
  "earthworm": "地虫",
  "elephant": "象",
  "fox": "狐",
  "frog": "蛙",
  "gallery": "芸術館",
  "goose": "鵝",
  "guilt": "罪恶感",
  "hen": "母鷄",
  "lamb": "羔羊",
  "landmine": "地雷",
  "limb": "肢",
  "lion": "獅",
  "majority": "多数派",
  "memoir": "記略",
  "minority": "少数派",
  "ox": "閹牛",
  "panda": "猫熊",
  "pink": "粉紅",
  "publish": "出版",
  "puppy": "犬仔",
  "purple": "紫",
  "queue": "隊伍",
  "rainbow": "雨虹",
  "ram": "公羊",
  "remember": "思出",
  "rooster": "公鷄",
  "ruin": "毀",
  "scholarship": "奨斈金",
  "sheep": "綿羊",
  "sick": "病",
  "stupid": "愚",
  "Taiwan": "台湾",
  "tiger": "虎",
  "trust": "信賴",
  "whale": "鯨",
  "width": "寬度",
  "wolf": "狼",
  "wonder": "驚疑",
  "forget": "忘",
  "convinced": "確信",
  "unreasonable": "不理可",
  "disdain": "蔑",
  "sitting": "坐",
  "peep": "穴窺",
  "conversation": "交話",
  "climb": "登上",
  "resemble": "略似",
  "autumn": "秋",
  "deny": "否定",
  "webpage": "网頁",
  "guideline": "概南",
  "glory": "光栄"
};