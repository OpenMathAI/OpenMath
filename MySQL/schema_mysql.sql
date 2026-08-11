-- ============================================================================
-- greatminds 人物/奖项数据库 schema（MySQL 8/9）
-- 由 SQLite 版（db/schema.sql）转换：InnoDB + utf8mb4 + 自增主键
-- 安全：仅监听 127.0.0.1（bind-address=127.0.0.1）
-- ============================================================================

SET NAMES utf8mb4;

-- ----------------------------------------------------------------------------
-- 1) 人物主表
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS people (
    id                 INT AUTO_INCREMENT PRIMARY KEY,
    qid                VARCHAR(32) UNIQUE,
    name_en            VARCHAR(255) NOT NULL,
    name_zh            VARCHAR(255),
    name_variants      TEXT,
    gender             VARCHAR(16),
    birth_date         VARCHAR(16),
    death_date         VARCHAR(16),
    description        TEXT,
    primary_occupation VARCHAR(128),
    has_biography      TINYINT DEFAULT 0,
    has_social_data    TINYINT DEFAULT 0 COMMENT '社会关系+研究领域已入库标志（1=已入库）',
    created_at         DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at         DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    KEY idx_name_en  (name_en),
    KEY idx_has_bio  (has_biography),
    KEY idx_has_social (has_social_data)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 2) 职业字典 + 人↔职业
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS occupations (
    id       INT AUTO_INCREMENT PRIMARY KEY,
    name_en  VARCHAR(128) UNIQUE NOT NULL,
    name_zh  VARCHAR(128)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS person_occupation (
    person_id     INT NOT NULL,
    occupation_id INT NOT NULL,
    `rank`          INT DEFAULT 0,
    PRIMARY KEY (person_id, occupation_id),
    CONSTRAINT fk_po_person FOREIGN KEY (person_id) REFERENCES people(id) ON DELETE CASCADE,
    CONSTRAINT fk_po_occ    FOREIGN KEY (occupation_id) REFERENCES occupations(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 3) 研究领域 + 人↔领域
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS fields (
    id      INT AUTO_INCREMENT PRIMARY KEY,
    name_en VARCHAR(128) UNIQUE NOT NULL,
    name_zh VARCHAR(128)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS person_field (
    person_id INT NOT NULL,
    field_id  INT NOT NULL,
    `rank`      INT DEFAULT 0,
    PRIMARY KEY (person_id, field_id),
    CONSTRAINT fk_pf_person FOREIGN KEY (person_id) REFERENCES people(id) ON DELETE CASCADE,
    CONSTRAINT fk_pf_field  FOREIGN KEY (field_id) REFERENCES fields(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 4) 奖项字典 + 人↔奖项
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS awards (
    id           INT AUTO_INCREMENT PRIMARY KEY,
    name_en      VARCHAR(255) UNIQUE NOT NULL,
    name_zh      VARCHAR(255) NOT NULL,
    award_type   VARCHAR(32) NOT NULL,
    tier         INT,
    org          VARCHAR(255),
    established  INT,
    wiki_url     VARCHAR(512),
    icon_key     VARCHAR(128)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS award_laureate (
    person_id   INT NOT NULL,
    award_id    INT NOT NULL,
    year        INT NOT NULL,
    edition     INT,
    share_type  VARCHAR(16),
    note        TEXT,
    source      VARCHAR(128),
    PRIMARY KEY (person_id, award_id, year),
    CONSTRAINT fk_al_person FOREIGN KEY (person_id) REFERENCES people(id) ON DELETE CASCADE,
    CONSTRAINT fk_al_award  FOREIGN KEY (award_id) REFERENCES awards(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
CREATE INDEX idx_al_award  ON award_laureate(award_id);
CREATE INDEX idx_al_year   ON award_laureate(year);
CREATE INDEX idx_al_person ON award_laureate(person_id);

-- ----------------------------------------------------------------------------
-- 5) 机构 + 人↔机构
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS institutions (
    id      INT AUTO_INCREMENT PRIMARY KEY,
    name_en VARCHAR(255) UNIQUE NOT NULL,
    name_zh VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS person_institution (
    person_id  INT NOT NULL,
    inst_id    INT NOT NULL,
    relation   VARCHAR(32) NOT NULL,
    start_year INT,
    end_year   INT,
    PRIMARY KEY (person_id, inst_id, relation),
    CONSTRAINT fk_pi_person FOREIGN KEY (person_id) REFERENCES people(id) ON DELETE CASCADE,
    CONSTRAINT fk_pi_inst   FOREIGN KEY (inst_id) REFERENCES institutions(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------------------------------------------------------
-- 5b) 国家/政权字典 + 人物-国籍（多对多，含历史政权）
--      一人多国籍（如 von Neumann: Hungary + USA）；历史政权（Soviet Union 等）
--      is_current=0，successor 指向现代后继国，可按现代国归一过滤
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS countries (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    name_en    VARCHAR(128) UNIQUE NOT NULL,  -- 'Kingdom of Prussia' / 'Germany'
    name_zh    VARCHAR(128),
    is_current TINYINT DEFAULT 0,             -- 1=现代现存国，0=历史政权
    era        VARCHAR(64),                   -- 存续期 '1701-1871'
    successor  VARCHAR(128),                  -- 后继国（如 'Germany'）
    iso        VARCHAR(8)                     -- 现代 ISO 代码（如 DE）；历史政权可空
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS person_nationality (
    person_id  INT NOT NULL,
    country_id INT NOT NULL,
    `rank`     INT DEFAULT 0,                 -- Wikidata nationality 顺序
    era_note   VARCHAR(128),                  -- 备注（如 'historical'）
    PRIMARY KEY (person_id, country_id),
    CONSTRAINT fk_pn_person  FOREIGN KEY (person_id) REFERENCES people(id) ON DELETE CASCADE,
    CONSTRAINT fk_pn_country FOREIGN KEY (country_id) REFERENCES countries(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
CREATE INDEX idx_pn_country ON person_nationality(country_id);
CREATE INDEX idx_pn_person  ON person_nationality(person_id);

-- ----------------------------------------------------------------------------
-- 6) 社会关系 + 关系类型
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS relation_types (
    relation_key VARCHAR(64) PRIMARY KEY,
    name_zh      VARCHAR(64),
    directed     TINYINT DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS person_relation (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    from_id       INT NOT NULL,
    to_id         INT NOT NULL,
    relation_type VARCHAR(64) NOT NULL,
    note          TEXT,
    source        VARCHAR(128),
    UNIQUE KEY uq_rel (from_id, to_id, relation_type),
    CONSTRAINT fk_pr_from FOREIGN KEY (from_id) REFERENCES people(id) ON DELETE CASCADE,
    CONSTRAINT fk_pr_to   FOREIGN KEY (to_id) REFERENCES people(id) ON DELETE CASCADE,
    CONSTRAINT fk_pr_type FOREIGN KEY (relation_type) REFERENCES relation_types(relation_key)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
CREATE INDEX idx_rel_type ON person_relation(relation_type);
CREATE INDEX idx_rel_from ON person_relation(from_id);
CREATE INDEX idx_rel_to   ON person_relation(to_id);

-- ----------------------------------------------------------------------------
-- 6b) 排行榜
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS rankings (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    person_id INT NOT NULL,
    list_key  VARCHAR(128) NOT NULL,
    `rank`      INT NOT NULL,
    orig_rank INT,
    tag       TEXT,
    status    VARCHAR(255),
    UNIQUE KEY uq_rank (person_id, list_key),
    CONSTRAINT fk_rk_person FOREIGN KEY (person_id) REFERENCES people(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
CREATE INDEX idx_rank_list ON rankings(list_key, `rank`);

-- ----------------------------------------------------------------------------
-- 7) 展示层：视频分集 + 徽标定义
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS episodes (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    ep_key      VARCHAR(16) UNIQUE NOT NULL,
    dir         VARCHAR(255),
    main        VARCHAR(255),
    title_zh    VARCHAR(255),
    subtitle_zh VARCHAR(255),
    year_range  VARCHAR(64),
    note        TEXT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS badge_defs (
    icon_key     VARCHAR(64) PRIMARY KEY,
    latex_cmd    VARCHAR(128),
    symbol       VARCHAR(128),
    color        VARCHAR(64),
    letter       VARCHAR(8),
    full_name_zh VARCHAR(128)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---- 关系类型字典 ----
INSERT INTO `relation_types` (`relation_key`, `name_zh`, `directed`) VALUES
 ('parent-child',      '父子/直系亲属', 1),
 ('advisor-student',   '师生',          1),
 ('colleague',         '同事',          0),
 ('collaborator',      '合作者',        0),
 ('co-honored',        '荣誉共同体/并称',0),
 ('rival',             '对手/仇敌',     0),
 ('controversy',       '争议',          0),
 ('spouse',            '夫妻',          0);

-- ---- 职业字典（可随抓取扩展）----
INSERT INTO `occupations` (`name_en`, `name_zh`) VALUES
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
INSERT INTO `awards` (`name_en`, `name_zh`, `award_type`, `tier`, `org`, `established`, `wiki_url`, `icon_key`) VALUES
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
INSERT INTO `badge_defs` (`icon_key`, `latex_cmd`, `symbol`, `color`, `letter`, `full_name_zh`) VALUES
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
INSERT INTO `episodes` (`ep_key`, `dir`, `main`, `title_zh`, `subtitle_zh`, `year_range`, `note`) VALUES
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

-- ----------------------------------------------------------------------------
-- 视图：人物关系（双向）
-- ----------------------------------------------------------------------------
CREATE OR REPLACE VIEW v_person_relations AS
SELECT
  a.name_en AS from_name, a.name_zh AS from_zh,
  b.name_en AS to_name,   b.name_zh AS to_zh,
  rt.name_zh AS relation, rt.relation_key,
  pr.note, pr.source
FROM person_relation pr
JOIN people a ON a.id = pr.from_id
JOIN people b ON b.id = pr.to_id
JOIN relation_types rt ON rt.relation_key = pr.relation_type;

CREATE OR REPLACE VIEW v_person_relations_bi AS
SELECT from_name AS person, relation, to_name AS other, note, source FROM v_person_relations
UNION ALL
SELECT to_name  AS person, relation, from_name AS other, note, source FROM v_person_relations;

-- ----------------------------------------------------------------------------
-- 视图：交叉奖项（多奖得主 + 组合矩阵 + 全明细）
-- ----------------------------------------------------------------------------
CREATE OR REPLACE VIEW v_multi_award AS
SELECT p.id AS person_id, p.name_en, p.name_zh,
       COUNT(*) AS award_count,
       GROUP_CONCAT(CONCAT(a.name_zh, ' ', al.year) SEPARATOR '；') AS awards_detail
FROM award_laureate al
JOIN people p ON p.id = al.person_id
JOIN awards a  ON a.id = al.award_id
GROUP BY p.id, p.name_en, p.name_zh
HAVING COUNT(*) > 1;

CREATE OR REPLACE VIEW v_award_matrix AS
SELECT a1.name_zh AS award_a, a2.name_zh AS award_b,
       COUNT(DISTINCT al1.person_id) AS n_persons
FROM award_laureate al1
JOIN award_laureate al2 ON al1.person_id = al2.person_id AND al1.award_id < al2.award_id
JOIN awards a1 ON a1.id = al1.award_id
JOIN awards a2 ON a2.id = al2.award_id
GROUP BY al1.award_id, al2.award_id, a1.name_zh, a2.name_zh;

CREATE OR REPLACE VIEW v_award_full AS
SELECT p.id AS person_id, p.name_en, p.name_zh,
       a.name_zh AS award_zh, a.name_en AS award_en,
       al.year, al.edition, al.share_type, al.note
FROM award_laureate al
JOIN people p ON p.id = al.person_id
JOIN awards a  ON a.id = al.award_id;

-- 4) 交叉汇总视图：获奖数 + 奖项年限 + 研究领域（分开聚合，避免笛卡尔积；万级数据适用）
CREATE OR REPLACE VIEW v_cross_summary AS
SELECT p.id AS person_id, p.name_en, p.name_zh,
       t.n AS award_count, t.awards_detail, f.fields_detail
FROM people p
JOIN (
    SELECT person_id, COUNT(DISTINCT award_id) n,
           GROUP_CONCAT(CONCAT(a.name_zh, ' ', al.year) ORDER BY al.year SEPARATOR '；') AS awards_detail
    FROM award_laureate al JOIN awards a ON a.id = al.award_id
    GROUP BY person_id
) t ON t.person_id = p.id
LEFT JOIN (
    SELECT pf.person_id,
           GROUP_CONCAT(DISTINCT f.name_en ORDER BY f.name_en SEPARATOR '、') AS fields_detail
    FROM person_field pf JOIN fields f ON f.id = pf.field_id
    GROUP BY pf.person_id
) f ON f.person_id = p.id;
