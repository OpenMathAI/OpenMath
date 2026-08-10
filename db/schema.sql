-- ============================================================================
-- 人物 / 奖项数据库 schema（SQLite）· 库文件：greatminds.db
-- 主体为「人物」（数学家 / 物理学家 / 生物学家 / 化学家 / 计算机科学家 /
-- 文学家 / 经济学家 / 艺术家…），奖项仅是人物的一类属性（award_laureate）。
-- 覆盖奖项：Fields / Wolf / Abel / Chern / COPSS / Turing / Nobel 家族 / 京都 / 哥德尔 / 香农…
-- 设计文档：maintenance_guide/database_schema.md · 表清单：database_tables.md
-- ============================================================================

PRAGMA foreign_keys = ON;

-- ----------------------------------------------------------------------------
-- 1) 人物主表：只放 1:1 属性；多值属性（职业/领域/机构/奖项/关系）全部在关系表
-- ----------------------------------------------------------------------------
CREATE TABLE people (
    id                INTEGER PRIMARY KEY,
    qid               TEXT UNIQUE,               -- Wikidata Q-ID，全局唯一身份
    name_en           TEXT NOT NULL,             -- 英文名（含维基消歧后缀）
    name_zh           TEXT,
    name_variants     TEXT,                      -- 别名/变体，JSON 数组
    gender            TEXT,
    birth_date        TEXT,                      -- ISO 日期（兼容仅年份）
    death_date        TEXT,                      -- NULL = 在世
    birth_place       TEXT,
    death_place       TEXT,
    description       TEXT,                      -- Wikidata 一句话描述
    wiki_url          TEXT,
    local_dir         TEXT UNIQUE,               -- pages/<Name>/ 相对路径，NULL=未抓取
    primary_occupation TEXT,                     -- 冗余展示快照（名称字符串），不参与检索
    created_at        TEXT DEFAULT (datetime('now')),
    updated_at        TEXT DEFAULT (datetime('now'))
);

-- ----------------------------------------------------------------------------
-- 2) 职业字典 + 人↔职业（多对多）
-- ----------------------------------------------------------------------------
CREATE TABLE occupations (
    id       INTEGER PRIMARY KEY,
    name_en  TEXT UNIQUE NOT NULL,               -- mathematician / physicist / writer…
    name_zh  TEXT
);

CREATE TABLE person_occupation (
    person_id     INTEGER NOT NULL REFERENCES people(id)   ON DELETE CASCADE,
    occupation_id INTEGER NOT NULL REFERENCES occupations(id),
    rank          INTEGER DEFAULT 0,                       -- 0=主职业
    PRIMARY KEY (person_id, occupation_id)
);

-- ----------------------------------------------------------------------------
-- 3) 研究领域字典 + 人↔领域（多对多）
-- ----------------------------------------------------------------------------
CREATE TABLE fields (
    id      INTEGER PRIMARY KEY,
    name_en TEXT UNIQUE NOT NULL,                -- number theory / algebra / literature…
    name_zh TEXT
);

CREATE TABLE person_field (
    person_id INTEGER NOT NULL REFERENCES people(id) ON DELETE CASCADE,
    field_id  INTEGER NOT NULL REFERENCES fields(id),
    rank      INTEGER DEFAULT 0,
    PRIMARY KEY (person_id, field_id)
);

-- ----------------------------------------------------------------------------
-- 4) 奖项字典 + 人↔奖项（多对多，交叉荣誉核心）
-- ----------------------------------------------------------------------------
CREATE TABLE awards (
    id           INTEGER PRIMARY KEY,
    name_en      TEXT UNIQUE NOT NULL,
    name_zh      TEXT NOT NULL,
    award_type   TEXT NOT NULL,                  -- math_top/math_icm/cs/statistics/nobel/cross/honor
    tier         INTEGER,                        -- 1..6（对应 math_awards_tiers.md），NULL=未分级
    org          TEXT,                           -- 颁发机构
    established  INTEGER,                        -- 设立年份
    wiki_url     TEXT,
    icon_key     TEXT                            -- 徽标 key（对应 badge_defs.icon_key），NULL=无徽标；可多个奖项共用
);

CREATE TABLE award_laureate (
    person_id   INTEGER NOT NULL REFERENCES people(id)  ON DELETE CASCADE,
    award_id    INTEGER NOT NULL REFERENCES awards(id),
    year        INTEGER NOT NULL,
    edition     INTEGER,                               -- 届次（图灵奖用）
    share_type  TEXT,                                  -- solo/shared
    note        TEXT,
    source      TEXT,                                  -- Wikipedia/Wikidata/人工核对
    PRIMARY KEY (person_id, award_id, year)
);
CREATE INDEX idx_al_award ON award_laureate(award_id);
CREATE INDEX idx_al_year  ON award_laureate(year);
CREATE INDEX idx_al_person ON award_laureate(person_id);

-- ----------------------------------------------------------------------------
-- 5) 机构字典 + 人↔机构（多对多）
-- ----------------------------------------------------------------------------
CREATE TABLE institutions (
    id      INTEGER PRIMARY KEY,
    name_en TEXT UNIQUE NOT NULL,
    name_zh TEXT
);

CREATE TABLE person_institution (
    person_id  INTEGER NOT NULL REFERENCES people(id) ON DELETE CASCADE,
    inst_id    INTEGER NOT NULL REFERENCES institutions(id),
    relation   TEXT NOT NULL,                    -- employer/educated_at/member_of/affiliation
    start_year INTEGER,
    end_year   INTEGER,
    PRIMARY KEY (person_id, inst_id, relation)
);

-- ----------------------------------------------------------------------------
-- 6) 人物关系：社会关系类型字典 + 关系表（父子/师生/同事/并称/仇敌/争议…）
-- ----------------------------------------------------------------------------
CREATE TABLE relation_types (
    relation_key TEXT PRIMARY KEY,               -- parent-child / advisor-student …
    name_zh      TEXT,
    directed     INTEGER DEFAULT 0               -- 1=有向（父子、师生）；0=无向
);

CREATE TABLE person_relation (
    id            INTEGER PRIMARY KEY,
    from_id       INTEGER NOT NULL REFERENCES people(id) ON DELETE CASCADE,
    to_id         INTEGER NOT NULL REFERENCES people(id) ON DELETE CASCADE,
    relation_type TEXT    NOT NULL REFERENCES relation_types(relation_key),
    note          TEXT,                          -- 如「微积分发明优先权之争」
    source        TEXT,
    UNIQUE (from_id, to_id, relation_type)
);
CREATE INDEX idx_rel_type ON person_relation(relation_type);
CREATE INDEX idx_rel_from ON person_relation(from_id);
CREATE INDEX idx_rel_to   ON person_relation(to_id);

-- ----------------------------------------------------------------------------
-- 7) 展示层（可选）：视频分集 + 徽标定义
-- ----------------------------------------------------------------------------
CREATE TABLE episodes (
    id          INTEGER PRIMARY KEY,
    ep_key      TEXT UNIQUE NOT NULL,            -- ep01..ep10
    dir         TEXT,
    main        TEXT,                            -- tex 主文件名
    title_zh    TEXT,
    subtitle_zh TEXT,
    year_range  TEXT,
    note        TEXT
);

CREATE TABLE badge_defs (
    icon_key     TEXT PRIMARY KEY,               -- 诺贝尔 / 京都 / 沃尔夫…
    latex_cmd    TEXT,                           -- \nobelbadge…
    symbol       TEXT,                           -- \faIcon{award} / $\blacklozenge$…
    color        TEXT,                           -- nobelclr…
    letter       TEXT,                           -- N / K / W…
    full_name_zh TEXT
);

-- ============================================================================
-- 种子数据
-- ============================================================================

-- ---- 关系类型字典 ----
INSERT INTO relation_types (relation_key, name_zh, directed) VALUES
 ('parent-child',      '父子/直系亲属', 1),
 ('advisor-student',   '师生',          1),
 ('colleague',         '同事',          0),
 ('collaborator',      '合作者',        0),
 ('co-honored',        '荣誉共同体/并称',0),
 ('rival',             '对手/仇敌',     0),
 ('controversy',       '争议',          0),
 ('spouse',            '夫妻',          0);

-- ---- 职业字典（可随抓取扩展）----
INSERT INTO occupations (name_en, name_zh) VALUES
 ('mathematician',       '数学家'),
 ('physicist',           '物理学家'),
 ('biologist',           '生物学家'),
 ('chemist',             '化学家'),
 ('computer scientist',  '计算机科学家'),
 ('statistician',        '统计学家'),
 ('astronomer',          '天文学家'),
 ('economist',           '经济学家'),
 ('writer',              '文学家/作家'),
 ('poet',                '诗人'),
 ('philosopher',         '哲学家'),
 ('artist',              '艺术家'),
 ('engineer',            '工程师');

-- ---- 奖项字典（39+ 项，源自 awards_list.md + math_awards_tiers.md）----
INSERT INTO awards (name_en, name_zh, award_type, tier, org, established, wiki_url, icon_key) VALUES
 -- 数学四大奖
 ('Fields Medal',            '菲尔兹奖',      'math_top', 1, 'IMU', 1936, 'https://en.wikipedia.org/wiki/Fields_Medal', NULL),
 ('Abel Prize',              '阿贝尔奖',      'math_top', 1, 'Norwegian Academy', 2003, 'https://en.wikipedia.org/wiki/Abel_Prize', '阿贝尔'),
 ('Wolf Prize in Mathematics','沃尔夫数学奖', 'math_top', 1, 'Wolf Foundation', 1978, 'https://en.wikipedia.org/wiki/Wolf_Prize_in_Mathematics', '沃尔夫'),
 ('Chern Medal',             '陈省身奖章',    'math_top', 2, 'IMU', 2010, 'https://en.wikipedia.org/wiki/Chern_Medal', NULL),
 -- ICM 配套
 ('Nevanlinna Prize',        '内万林纳奖',    'math_icm', 2, 'IMU', 1982, 'https://en.wikipedia.org/wiki/Rolf_Nevanlinna_Prize', '内万林纳'),
 ('Gauss Prize',             '高斯奖',        'math_icm', 2, 'IMU/IMU', 2006, 'https://en.wikipedia.org/wiki/Gauss_Prize', NULL),
 -- 理论计算机 / 计算机专项
 ('Gödel Prize',             '哥德尔奖',      'cs', 3, 'EATCS+SIGACT', 1993, 'https://en.wikipedia.org/wiki/G%C3%B6del_Prize', '哥德尔'),
 ('Knuth Prize',             '高德纳奖',      'cs', 3, 'ACM SIGACT', 1996, 'https://en.wikipedia.org/wiki/Knuth_Prize', NULL),
 ('Dijkstra Prize',          '迪杰斯特拉奖',  'cs', 3, 'ACM PODC+EATCS', 2000, 'https://en.wikipedia.org/wiki/Dijkstra_Prize', NULL),
 ('IEEE John von Neumann Medal', 'IEEE 冯·诺依曼奖章', 'cs', 3, 'IEEE', 1990, 'https://en.wikipedia.org/wiki/IEEE_John_von_Neumann_Medal', '冯'),
 ('IEEE Richard W. Hamming Medal', 'IEEE 汉明奖章', 'cs', 3, 'IEEE', 1986, 'https://en.wikipedia.org/wiki/IEEE_Richard_W._Hamming_Medal', '汉明'),
 ('Claude E. Shannon Award', 'IEEE 香农奖',   'cs', 3, 'IEEE IT Society', 1973, 'https://en.wikipedia.org/wiki/Claude_E._Shannon_Award', '香农'),
 ('EATCS Award',             'EATCS 奖',      'cs', 3, 'EATCS', 2000, 'https://en.wikipedia.org/wiki/EATCS_Award', 'EATCS'),
 ('ACM A.M. Turing Award',   '图灵奖',        'cs', 1, 'ACM', 1966, 'https://en.wikipedia.org/wiki/Turing_Award', NULL),
 ('Millennium Technology Prize', '千禧科技奖', 'cross', 4, 'Technology Academy Finland', 2004, 'https://en.wikipedia.org/wiki/Millennium_Technology_Prize', '千禧'),
 ('Marconi Prize',           '马可尼奖',      'cs', 4, 'Marconi Society', 2000, 'https://en.wikipedia.org/wiki/Marconi_Prize', '马可尼'),
 -- 统计学
 ('COPSS Presidents'' Award', '考普斯会长奖', 'statistics', 5, 'ASA·SSC·IMS·ENAR·WNAR', 1981, 'https://en.wikipedia.org/wiki/COPSS_Presidents%27_Award', NULL),
 ('International Prize in Statistics', '国际统计学奖', 'statistics', 5, 'ASA+国际统计学会', 2017, 'https://en.wikipedia.org/wiki/International_Prize_in_Statistics', NULL),
 ('R. A. Fisher Lectureship', 'R. A. Fisher 讲座', 'statistics', 5, 'ASA', 1963, 'https://en.wikipedia.org/wiki/R._A._Fisher_Lectureship', NULL),
 ('C. R. Rao Award',         'C. R. 拉奥奖',  'statistics', 5, 'Penn State', 2003, 'https://en.wikipedia.org/wiki/C._R._Rao_Award', NULL),
 ('Norbert Wiener Prize',    '诺伯特·维纳奖', 'statistics', 5, 'AMS+SIAM', 1967, 'https://en.wikipedia.org/wiki/Norbert_Wiener_Prize_in_Applied_Mathematics', NULL),
 -- 诺贝尔家族
 ('Nobel Prize in Physics',  '诺贝尔物理学奖',      'nobel', 1, '瑞典皇家科学院', 1901, 'https://en.wikipedia.org/wiki/Nobel_Prize_in_Physics', '诺贝尔'),
 ('Nobel Prize in Chemistry','诺贝尔化学奖',        'nobel', 1, '瑞典皇家科学院', 1901, 'https://en.wikipedia.org/wiki/Nobel_Prize_in_Chemistry', '诺贝尔'),
 ('Nobel Prize in Physiology or Medicine', '诺贝尔生理学或医学奖', 'nobel', 1, '卡罗林斯卡学院', 1901, 'https://en.wikipedia.org/wiki/Nobel_Prize_in_Physiology_or_Medicine', '诺贝尔'),
 ('Nobel Prize in Literature', '诺贝尔文学奖',      'nobel', 1, '瑞典学院', 1901, 'https://en.wikipedia.org/wiki/Nobel_Prize_in_Literature', '诺贝尔'),
 ('Nobel Memorial Prize in Economic Sciences', '诺贝尔经济学奖', 'nobel', 1, '瑞典皇家科学院', 1969, 'https://en.wikipedia.org/wiki/Nobel_Memorial_Prize_in_Economic_Sciences', '诺贝尔'),
 -- 跨学科大奖
 ('Kyoto Prize',             '京都奖',        'cross', 6, '稻盛财团', 1984, 'https://en.wikipedia.org/wiki/Kyoto_Prize', '京都'),
 ('Shaw Prize',              '邵逸夫奖',      'cross', 6, '邵逸夫奖基金会', 2002, 'https://en.wikipedia.org/wiki/Shaw_Prize', NULL),
 ('Breakthrough Prize in Mathematics', '数学突破奖', 'cross', 6, 'Breakthrough Prize Foundation', 2013, 'https://en.wikipedia.org/wiki/Breakthrough_Prize_in_Mathematics', NULL),
 ('Crafoord Prize',          '克拉福德奖',    'cross', 6, '瑞典皇家科学院', 1980, 'https://en.wikipedia.org/wiki/Crafoord_Prize', NULL),
 ('MacArthur Fellows Program', '麦克阿瑟奖',  'cross', 6, 'MacArthur Foundation', 1981, 'https://en.wikipedia.org/wiki/MacArthur_Fellows_Program', NULL),
 ('Ramanujan Prize',         '拉马努金奖',    'cross', 6, 'ICTP', 2005, 'https://en.wikipedia.org/wiki/Ramanujan_Prize', NULL),
 ('Morningside Medal of Mathematics', '晨兴数学金奖', 'cross', NULL, 'ICCM', 1998, 'https://en.wikipedia.org/wiki/Morningside_Medal', NULL),
 -- 荣誉 / 院士 / 奖章
 ('Turing100 Lecture',      '图灵百年演讲',  'honor', NULL, 'ACM', 2012, NULL, NULL),
 ('National Medal of Science', '美国国家科学奖章', 'honor', NULL, 'NSF', 1959, 'https://en.wikipedia.org/wiki/National_Medal_of_Science', '国家科学奖章'),
 ('National Medal of Technology and Innovation', '美国国家技术奖章', 'honor', NULL, 'USPTO', 1980, 'https://en.wikipedia.org/wiki/National_Medal_of_Technology_and_Innovation', '国家技术奖章'),
 ('Member of the National Academy of Sciences', '美国国家科学院院士', 'honor', NULL, 'NAS', 1863, 'https://en.wikipedia.org/wiki/National_Academy_of_Sciences', '科学院院士'),
 ('Member of the National Academy of Engineering', '美国国家工程院院士', 'honor', NULL, 'NAE', 1964, 'https://en.wikipedia.org/wiki/National_Academy_of_Engineering', NULL),
 ('Fellow of the Royal Society', '英国皇家学会院士', 'honor', NULL, 'Royal Society', 1660, 'https://en.wikipedia.org/wiki/Fellow_of_the_Royal_Society', '皇家学会院士'),
 ('Governor General''s Innovation Award', '加拿大总督创新奖', 'honor', NULL, 'Government of Canada', 2016, 'https://en.wikipedia.org/wiki/Governor_General%27s_Innovation_Award', '加拿大总督'),
 ('Japan Prize',             '日本国际奖',    'cross', 6, 'Japan Prize Foundation', 1985, 'https://en.wikipedia.org/wiki/Japan_Prize', '日本国际'),
 ('Rumelhart Prize',         '鲁梅哈特奖',    'cross', NULL, 'Cognitive Science Society', 2001, 'https://en.wikipedia.org/wiki/Rumelhart_Prize', '鲁梅哈特');

-- ---- 徽标定义（源自 gen_turing.py AWARD_ICONS + gen_turing_beamer.py BADGE_DEFS）----
INSERT INTO badge_defs (icon_key, latex_cmd, symbol, color, letter, full_name_zh) VALUES
 ('诺贝尔',      '\nobelbadge',      '\faIcon{award}',    'nobelclr',      'N', '诺贝尔奖'),
 ('京都',        '\kyotobadge',      '$\blacklozenge$',   'kyotoclr',      'K', '京都奖'),
 ('沃尔夫',      '\wolfbadge',       '$\bigstar$',        'wolfclr',       'W', '沃尔夫奖'),
 ('哥德尔',      '\godelbadge',      '$\diamond$',        'godelclr',      'G', '哥德尔奖'),
 ('阿贝尔',      '\abelbadge',       '$\bigstar$',        'abelclr',       'A', '阿贝尔奖'),
 ('香农',        '\shannonbadge',    '$\bigstar$',        'shannonclr',    'S', 'IEEE 香农奖'),
 ('汉明',        '\hammingbadge',    '$\bigstar$',        'hammingclr',    'H', 'IEEE 汉明奖章'),
 ('日本国际',    '\japanbadge',      '$\heartsuit$',      'japanclr',      'J', '日本国际奖'),
 ('内万林纳',    '\nevanlinnabadge', '$\blacktriangle$',  'nevanclr',      'N', '内万林纳奖'),
 ('EATCS',       '\eatcsbadge',      '$\square$',         'eatcsclr',      'E', 'EATCS 奖'),
 ('马可尼',      '\marconibadge',    '$\bullet$',         'marconiclr',    'M', '马可尼奖'),
 ('冯',          '\neumannbadge',    '$\blacktriangle$',  'neumannclr',    'V', 'IEEE 冯·诺依曼奖'),
 ('千禧',        '\millenniumbadge', '$\blacklozenge$',   'millenniumclr', 'T', '千禧科技奖'),
 ('国家科学奖章', '\nsmbadge',       '$\spadesuit$',      'nsmclr',        'M', '美国国家科学奖章'),
 ('国家技术奖章', '\ntmbadge',       '$\star$',           'ntmclr',        'T', '美国国家技术奖章'),
 ('科学院院士',   '\nasbadge',       '$\blacksquare$',    'nasclr',        'N', '美国科学院院士'),
 ('皇家学会院士', '\frsbadge',       '$\checkmark$',      'frsclr',        'R', '英国皇家学会院士'),
 ('加拿大总督',   '\govbadge',       '$\blacklozenge$',   'govclr',        'C', '加拿大总督奖'),
 ('鲁梅哈特',     '\rumelhartbadge', '$\diamondsuit$',    'rumelclr',      'R', '鲁梅哈特奖');

-- ---- 图灵奖视频分集（源自 gen_turing.py EPISODES）----
INSERT INTO episodes (ep_key, dir, main, title_zh, subtitle_zh, year_range, note) VALUES
 ('ep01', 'episode-01-theory-computation',  'turing_ep01_zh', '理论计算机科学',     '计算复杂性 · 算法 · 随机性',     '1966 – 2023', '从 Cook 到 Wigderson'),
 ('ep02', 'episode-02-programming-languages','turing_ep02_zh','程序设计语言与软件方法学','编译 · 语言 · 工程',            '1966 – 2020', '从 Perlis 到 Ullman'),
 ('ep03', 'episode-03-ai-ml',              'turing_ep03_zh', '人工智能与机器学习',   'AI 奠基 · 深度学习 · 强化学习', '1969 – 2024', '从 Minsky 到 Sutton'),
 ('ep04', 'episode-04-os-architecture',    'turing_ep04_zh', '操作系统与体系结构',   'Unix · RISC · 编译器',          '1967 – 2017', '从 Wilkes 到 Patterson'),
 ('ep05', 'episode-05-database',           'turing_ep05_zh', '数据库与数据管理',     '关系模型 · 事务处理',           '1973 – 2014', '从 Bachman 到 Stonebraker'),
 ('ep06', 'episode-06-network-web',        'turing_ep06_zh', '网络与万维网',         'TCP/IP · 以太网 · WWW',         '2004 – 2022', '从 Cerf 到 Metcalfe'),
 ('ep07', 'episode-07-distributed-verification', 'turing_ep07_zh', '分布式系统与形式验证', '并发 · 共识 · 模型检验',   '1972 – 2013', '从 Dijkstra 到 Lamport'),
 ('ep08', 'episode-08-crypto-security',    'turing_ep08_zh', '密码学与量子信息',     '公钥密码 · 零知识 · 量子密钥',  '2000 – 2025', '从 Yao 到 Brassard'),
 ('ep09', 'episode-09-numerical-hpc',      'turing_ep09_zh', '数值计算与高性能计算', '浮点 · 纠错码 · HPC',           '1968 – 2021', '从 Hamming 到 Dongarra'),
 ('ep10', 'episode-10-graphics-hci',       'turing_ep10_zh', '计算机图形学与人机交互','图形 · 鼠标 · 可视化',          '1988 – 2019', '从 Sutherland 到 Hanrahan');
