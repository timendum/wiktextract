from .models import WordEntry

TAGS = {
    "男性": "masculine",
    "女性": "feminine",
    "通性": "common",
    "中性": "neuter",
    "単数": "singular",
    "複数": "plural",
    "不変": "invariable",
    "男性複数": ["masculine", "plural"],
    # テンプレート:context/data
    "くだけた表現": "informal",
    "しばしば": "often",
    "まれ": "rare",
    "アイルランド": "Ireland",
    "アフリカ": "Africa",
    "アメカメカ": "Amecameca",
    "アメリカ合衆国": "US",
    "アルスター": "Ulster",
    "アルゼンチン": "Argentina",
    "アングロ・ノルマン": "Anglo-Norman",
    "アンダルシア": "Andalusia",
    "イェ方言": "Ijekavian",
    "イギリス": "UK",
    "イラン": "Iran",
    "イロン方言": "Iron",
    "インターネット": "Internet",
    "インターネットスラング": "Internet",
    "ウクライナ": "Ukraine",
    "ウルグアイ": "Uruguay",
    "ウーリ語": "Uri",
    "エクアドル": "Ecuador",
    "エ方言": "Ekavian",
    "オノマトペ": "onomatopoeic",
    "オルムルム": "Ormulum",
    "オークニー": "Orkney",
    "オーストリア": "Austrian",
    "カイピラ方言": "Caipira",
    "カイ方言": "Kajkavian",
    "カサレヴサ": "Katharevousa",
    "カナダ": "Canada",
    "カルコーフォロ語": "Carcoforo",
    "ガスコーニュ": "Gascony",
    "ガーンジー": "Guernsey",
    "キューバ": "Cuba",
    "キリスト教": "Christian",
    "クロアチア": "Croatian",
    "グアテマラ": "Guatemala",
    "グレッソネイ語": "Gressoney",
    "ケニア": "Kenya",
    "ケベック": "Quebec",
    "ケルン語": "Kölsch",
    "ケント": "Kentish",
    "コイネー": "Koine",
    "コノート": "Connacht",
    "コロンビア": "Colombia",
    "コンゴ": "Congo",
    "サカティアングイス": "Zacatianguis",
    "サーク": "Sark",
    "シェットランド": "Shetland",
    "シク教": "Sikhism",
    "シンガポール": "Singapore",
    "ジャイナ教": "Jainism",
    "ジャマイカ": "Jamaica",
    "ジャージー": "Jersey",
    "ジンバブエ": "Zimbabwe",
    "スイス": "Switzerland",
    "スコットランド": "Scotland",
    "ストゥシルヴァン": "Sutsilvan",
    "スペイン": "Spain",
    "スルシルヴァン": "Sursilvan",
    "スルミラン": "Surmiran",
    "セルビア": "Serbian",
    "セルリング": "Sylt",
    "タイ英語": "Thailand",
    "タラシケヴィツァ": "Taraškievica",
    "タントユカ": "Tantoyuca",
    "ダリー語": "Dari",
    "チコナメル": "Chiconamel",
    "チコンテペク": "Chicontepec",
    "チャ方言": "Chakavian",
    "チリ": "Chile",
    "ティマウ": "Timau",
    "テペツィントラ": "Tepetzintla",
    "テマパチェ": "Temapache",
    "ディゴル方言": "Digor",
    "デモティキ": "Demotic",
    "トスカナ語": "Tuscany",
    "ドイツ": "Germany",
    "ドイツ南部": "Southern-Germany",
    "ナチズム": "Nazism",
    "ナミビア": "Namibia",
    "ニカラグア": "Nicaragua",
    "ニューカッスル": "Tyneside",
    "ニュージーランド": "New-Zealand",
    "ヌオロ": "Nuorese",
    "バレンシア": "Valencia",
    "パナマ": "Panama",
    "ヒンズー教": "Hinduism",
    "ビザンツ": "Byzantine",
    "ビバロ・アルピーネ語": "Vivaro-Alpine",
    "フィリピン": "Philippines",
    "フェリング・エームラング": "Föhr-Amrum",
    "フォルマッツァ語": "Formazza",
    "フランス": "French",
    "ブラジル": "Brazil",
    "プロテスタント": "Protestant",
    "プロヴァンス": "Provençal",
    "プーター": "Puter",
    "ヘルゴラント": "Helgoland",
    "ベネズエラ": "Venezuela",
    "ベルギー": "Belgium",
    "ペルー": "Peru",
    "ホンジュラス": "Honduras",
    "ボスニア": "Bosnian",
    "ボリビア": "Bolivia",
    "ポルトガル": "Portugal",
    "マンスター": "Munster",
    "マーシア": "Mercian",
    "ミストラル式綴り": "Mistralian",
    "メキシコ": "Mexico",
    "モンテネグロ": "Montenegro",
    "モーリング": "Mooring",
    "ユダヤ教": "Judaism",
    "ヨーロッパ": "Europe",
    "ラングドック": "Languedoc",
    "リヒテンシュタイン": "Liechtenstein",
    "リプアーリ語": "Ripuarian",
    "リムーザン": "Limousin",
    "リメッラ語": "Rimella",
    "ルイジアナ": "Louisiana",
    "ルゼルナ": "Luserna",
    "ログドーロ": "Logudorese",
    "ロシア": "Russia",
    "ヴァラダール": "Vallander",
    "ヴィーディングハルデ": "Wiedingharde",
    "不可算": "uncountable",
    "不変化名詞": "indeclinable",
    "不活動体": "inanimate",
    "他動詞": "transitive",
    "代名詞的用法": "pronominal",
    "俗語": "slang",
    "修辞学": "rhetoric",
    "倒語": "slang",
    "再帰動詞": "reflexive",
    "初期中英語": "Early-Middle-English",
    "助動詞": "auxiliary",
    "卑語": "vulgar",
    "単数形で": "singular",
    "単数形のみ": "singular singular-only singular",
    "印": "India",
    "叙法": "modal",
    "叙述用法のみ": "predicative",
    "口語": "informal",
    "古用法": "dated",
    "古語・廃語": "archaic",
    "可算": "countable",
    "地名": "place",
    "地域": "regional",
    "基数": "cardinal",
    "多文化的ロンドン英語": "Multicultural-London-English",
    "婉曲表現": "euphemistic",
    "幼児語": "childish",
    "序数": "ordinal",
    "廃語": "obsolete",
    "強い": "strong",
    "形容詞的": "attributive",
    "後期中英語": "Late-Middle-English",
    "恐らく": "possibly",
    "慣用的表現": "idiomatic",
    "排斥された語": "proscribed",
    "控えめに": "mildly",
    "換喩的に": "metonymically",
    "文章語": "literary",
    "方言": "dialectal",
    "時々": "sometimes",
    "欠如動詞": "defective",
    "正式・堅": "formal",
    "歴史": "historical",
    "比喩": "figuratively",
    "比喩的に": "figuratively",
    "比較形有り": "comparable",
    "比較形無し": "not-comparable",
    "活動体": "animate",
    "滑稽": "humorous",
    "特に": "especially",
    "状態動詞": "stative",
    "略語": "abbreviation",
    "疑問詞": "interrogative",
    "皮肉": "ironic",
    "破格": "nonstandard",
    "筋肉": "anatomy",
    "米語": "US",
    "絶対単数": "singular-only singular",
    "絶対複数": "plural-only plural",
    "能格動詞": "ergative",
    "自他動詞": "ambitransitive",
    "自動詞": "intransitive",
    "英連邦": "Commonwealth",
    "蔑称": "offensive",
    "複合語で": "in-compounds",
    "複数形で": "plural",
    "西部": "Western",
    "視覚方言": "pronunciation-spelling",
    "詩的表現": "poetic",
    "豪": "Australian",
    "転じて": "broadly",
    "軽侮語": "pejorative",
    "近代ラテン語": "Netherlands",
    "逐語的に": "literally",
    "通常": "usually",
    "通常複数形で": "plural-normally",
    "造語": "neologism",
    "関係詞": "relative",
    "限定": "definite",
    "集合名詞": "collective",
    "集合的に": "collective",
    "非人称": "impersonal",
    "非標準": "uncommon",
    "頭字語": "initialism",
    "首都": "uppercase",
}

TOPICS = {
    # テンプレート:context/data
    "BDSM": "BDSM",
    "LGBT": "LGBT",
    "SF": "science fiction",
    "アイスホッケー": "ice hockey",
    "アメリカンフットボール": "American football",
    "アーチェリー": "archery",
    "イスラム教": "Islam",
    "イデオロギー": "ideology",
    "ウイルス学": "virology",
    "エネルギー": "energy",
    "カトリック": "Catholicism",
    "カードゲーム": "cards",
    "カーリング": "curling",
    "キリスト教": "Christianity",
    "クリケット": "cricket",
    "グラフィカルユーザインタフェース": "graphical user interface",
    "グラフ理論": "graph theory",
    "コンピュータグラフィックス": "computer graphics",
    "ゴルフ": "golf",
    "サイクリング": "cycling",
    "サッカー": "soccer",
    "サーフィン": "surfing",
    "シャンチー": "xiangqi",
    "スカッシュ": "squash",
    "スキー": "skiing",
    "スケート": "skating",
    "スケートボード": "skateboarding",
    "スヌーカー": "snooker",
    "スノーボード": "snowboarding",
    "スポーツ": "sports",
    "ソフトウェア": "software",
    "ソフトボール": "softball",
    "ゾロアスター教": "Zoroastrianism",
    "ダンス": "dance",
    "ダーツ": "darts",
    "チアリーディング": "cheerleading",
    "チェス": "chess",
    "テニス": "tennis",
    "テレビ": "television",
    "ハンドボール": "handball",
    "ハードウェア": "computer hardware",
    "バスケットボール": "basketball",
    "バレーボール": "volleyball",
    "ビジネス": "business",
    "ビリヤード": "billiards",
    "ファシズム": "fascism",
    "ファッション": "fashion",
    "フェミニズム": "feminism",
    "フェンシング": "fencing",
    "フットボール": "football",
    "ブリッジ": "bridge",
    "プログラミング": "programming",
    "ボウリング": "bowling",
    "ボクシング": "boxing",
    "ボディビル": "bodybuilding",
    "ボート競技": "rowing",
    "ポーカー": "poker",
    "モータースポーツ": "motor racing",
    "ラクロス": "lacrosse",
    "ラグビー": "rugby",
    "レスリング": "wrestling",
    "交通": "transport",
    "人口学": "demography",
    "仏教": "Buddhism",
    "代数学": "algebra",
    "代数幾何学": "algebraic geometry",
    "会計": "accounting",
    "体操": "gymnastics",
    "保険": "insurance",
    "倫理学": "ethics",
    "光学": "optics",
    "免疫学": "immunology",
    "共産主義": "communism",
    "写真": "photography",
    "分類学": "taxonomy",
    "力学": "mechanics",
    "動物学": "zoology",
    "化学": "chemistry",
    "化粧品": "cosmetics",
    "医学": "medicine",
    "医療": "healthcare",
    "単位": "units of measure",
    "占星術": "astrology",
    "印刷": "printing",
    "古生物学": "paleontology",
    "哲学": "philosophy",
    "哺乳類学": "mammalogy",
    "商取引": "trading",
    "園芸": "horticulture",
    "地理": "geography",
    "地質学": "geology",
    "地震学": "seismology",
    "外科学": "surgery",
    "大工仕事": "carpentry",
    "天体物理学": "astrophysics",
    "天文学": "astronomy",
    "娯楽": "entertainment",
    "季節": "seasons",
    "宗教": "religion",
    "宝飾": "jewelry",
    "家具": "furniture",
    "寄生虫学": "parasitology",
    "将棋": "shogi",
    "岩石学": "petrology",
    "工学": "engineering",
    "幾何学": "geometry",
    "建築": "architecture",
    "微生物学": "microbiology",
    "心理学": "psychology",
    "性": "sexuality",
    "性行為": "sex",
    "情報学": "information science",
    "情報技術": "computing",
    "戦争": "war",
    "技術": "technology",
    "政府": "government",
    "政治": "politics",
    "教育": "education",
    "数学": "mathematics",
    "数論": "number theory",
    "文学": "literature",
    "文法": "grammar",
    "文献学": "philology",
    "料理": "cuisine",
    "旅行": "travel",
    "昆虫学": "entomology",
    "時間": "time",
    "有機化学": "organic chemistry",
    "林業": "forestry",
    "柔道": "judo",
    "植物学": "botany",
    "武器": "weapon",
    "歯学": "dentistry",
    "歴史": "history",
    "歴史学": "historiography",
    "気候": "climatology",
    "気象": "weather",
    "水泳": "swimming",
    "泌尿器科学": "urology",
    "法律": "legal",
    "活版印刷": "typography",
    "流体力学": "fluid dynamics",
    "海事": "nautical",
    "海洋学": "oceanography",
    "消防": "firefighting",
    "火器": "firearms",
    "火山学": "volcanology",
    "無機化学": "inorganic chemistry",
    "熱力学": "thermodynamics",
    "物理学": "physics",
    "犯罪学": "criminology",
    "狩猟": "hunting",
    "生化学": "biochemistry",
    "生態学": "ecology",
    "生物学": "biology",
    "生理学": "physiology",
    "疑似科学": "pseudoscience",
    "疫学": "epidemiology",
    "病理学": "pathology",
    "発生学": "embryology",
    "相撲": "sumo",
    "眼科学": "ophthalmology",
    "社会学": "sociology",
    "社会科学": "social science",
    "社会言語学": "sociolinguistics",
    "神学": "theology",
    "神経学": "neurology",
    "神経解剖学": "neuroanatomy",
    "神話": "mythology",
    "神道": "Shinto",
    "科学": "sciences",
    "競馬": "horse racing",
    "精神医学": "psychiatry",
    "紋章学": "heraldry",
    "紡績": "weaving",
    "細胞学": "cytology",
    "細菌学": "bacteriology",
    "経営学": "management",
    "経済": "economics",
    "統計学": "statistics",
    "線型代数学": "linear algebra",
    "翻訳研究": "translation studies",
    "老年学": "gerontology",
    "考古学": "archaeology",
    "肉": "meat",
    "腫瘍学": "oncology",
    "自動車": "automobile",
    "自動車機器": "automotive",
    "航空": "aviation",
    "航空工学": "aeronautics",
    "色": "color",
    "花粉学": "palynology",
    "芸術": "arts",
    "著作権": "copyright",
    "薬理学": "pharmacology",
    "藻類学": "phycology",
    "蠍": "beer",
    "血液学": "hematology",
    "衣類": "clothing",
    "製造": "manufacturing",
    "解剖学": "anatomy",
    "解析学": "mathematical analysis",
    "言語": "language",
    "言語学": "linguistics",
    "詩": "poetry",
    "語彙論": "lexicology",
    "語用論": "pragmatics",
    "調理": "cooking",
    "論理学": "logic",
    "資本主義": "capitalism",
    "超心理学": "parapsychology",
    "軍事": "military",
    "辞書学": "lexicography",
    "農業": "agriculture",
    "通貨": "numismatics",
    "運動": "exercise",
    "道路": "road",
    "遺伝学": "genetics",
    "都市": "city",
    "都道府県": "prefectures of Japan",
    "酒": "beer",
    "重量挙げ": "weightlifting",
    "野球": "baseball",
    "野菜": "vegetable",
    "金融": "finance",
    "釣り": "fishing",
    "鉄道": "rail transport",
    "鉱物学": "mineralogy",
    "陸上競技": "athletics",
    "集合論": "set theory",
    "電子工学": "electronics",
    "電気": "electricity",
    "電磁気学": "electromagnetism",
    "電話": "telephone",
    "音声学": "phonetics",
    "音楽": "music",
    "音韻論": "phonology",
    "韻律": "prosody",
    "食品": "food",
    "馬術": "equestrianism",
    "魚": "fish",
    "魚類学": "ichthyology",
    "鳥類学": "ornithology",
    "麻雀": "mahjong",
}


def translate_raw_tags(data: WordEntry) -> None:
    raw_tags = []
    for raw_tag in data.raw_tags:
        if raw_tag in TAGS:
            add_tag(raw_tag, data)
        elif "/" in raw_tag:
            for r_tag in raw_tag.split("/"):
                r_tag = r_tag.strip()
                if r_tag in TAGS:
                    add_tag(r_tag, data)
        elif raw_tag in TOPICS and hasattr(data, "topics"):
            data.topics.append(TOPICS[raw_tag])
        else:
            raw_tags.append(raw_tag)
    data.raw_tags = raw_tags


def add_tag(raw_tag: str, data: WordEntry) -> None:
    tr_tag = TAGS[raw_tag]
    if isinstance(tr_tag, str) and tr_tag not in data.tags:
        data.tags.append(TAGS[raw_tag])
    elif isinstance(tr_tag, list):
        for t_tag in tr_tag:
            if t_tag not in data.tags:
                data.tags.append(t_tag)