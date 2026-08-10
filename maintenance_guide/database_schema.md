# 人物 / 奖项数据库 · 表结构（schema）

> 更新日期：2026-08-10
> 数据库：SQLite
> 表清单见 `database_tables.md`；本文件细化各表字段。**当前只细化 `people`（主表）与 `person_relation`（社会关系）**，其余表待续。

---

## 一、`people` 人物主表（约 15 个字段）

**只放 1:1 属性；所有多值属性（职业/领域/机构/奖项/关系）全部拆到多对多关系表，不进主表。**

| # | 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|---|
| 1 | `id` | INTEGER | PK, AUTOINCREMENT | 内部主键 |
| 2 | `qid` | TEXT | **UNIQUE** | **Wikidata Q-ID，全局唯一身份标识**（消歧核心，如 Q6722=Gauss） |
| 3 | `name_en` | TEXT | NOT NULL | 英文名（保留维基消歧后缀，如 `David Abrahams (mathematician)`） |
| 4 | `name_zh` | TEXT | | 中文名 |
| 5 | `name_variants` | TEXT | | 别名/变体，JSON 数组（如 `["Gregory", "Grigoriy"]`） |
| 6 | `gender` | TEXT | | 性别（male/female/other） |
| 7 | `birth_date` | TEXT | | 出生日期（ISO，如 1777-04-30；仅年份 1777 亦可） |
| 8 | `death_date` | TEXT | | 逝世日期（ISO；NULL=在世） |
| 9 | `birth_place` | TEXT | | 出生地 |
| 10 | `death_place` | TEXT | | 逝世地 |
| 11 | `description` | TEXT | | Wikidata 一句话描述（如 "German mathematician and physicist (1777–1855)"） |
| 12 | `wiki_url` | TEXT | | Wikipedia 链接 |
| 13 | `local_dir` | TEXT | UNIQUE | 本地页面目录（pages/<Name>/），NULL=未抓取 |
| 14 | `primary_occupation` | TEXT | | **主导职业（冗余展示快照）**：存职业**名称字符串**（如 'mathematician'），只用于列表展示，**不建索引、不参与检索**；真实归属与检索走 `person_occupation`（rank=0 即主导） |
| 15 | `created_at` / `updated_at` | TEXT | | 审计时间戳（可选） |

### 设计要点

- **牛顿同时是数学家 + 物理学家**：主表**不设** `occupation` 列。在 `person_occupation` 挂两行：
  ```
  (牛顿, mathematician)
  (牛顿, physicist)
  ```
  `primary_occupation` 仅冗余「mathematician」用于列表快速显示；
- **qid 唯一**：同名不同人（多个 Abel / Jordan）靠 qid 区分，`name_en` 保留维基消歧后缀；无 qid 的（如仅列表页采集）先用 `name_en` 兜底，抓取后回填；
- **生卒语义**：`birth_date`/`death_date` 用 ISO 日期字符串（兼容「仅年份」），展示层再格式化为「1922–1990（享年68）」；
- **不用外键指向职业/领域**：那是多对多关系表的事。

---

## 二、社会关系：`person_relation` + `relation_types`

### 2.1 `relation_types` 关系类型字典

| relation_key | 中文 | 方向 | 示例 |
|---|---|---|---|
| `parent-child` | 父子/直系亲属 | 有向（父→子） | 祖冲之 → 祖暅之 |
| `advisor-student` | 师生 | 有向（师→生） | Pfaff → Gauss |
| `colleague` | 同事 | 无向 | — |
| `collaborator` | 合作者 | 无向 | — |
| `co-honored` | 荣誉共同体 / 并称 | 无向 | 阿贝尔 ⇄ 伽罗瓦（数学双星） |
| `rival` | 对手 / 仇敌 | 无向 | 康托尔 ⇄ 克罗内克 |
| `controversy` | 争议 | 无向 | 牛顿 ⇄ 莱布尼茨（微积分优先权） |
| `spouse` | 夫妻 | 无向 | — |

### 2.2 `person_relation` 关系表

| # | 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|---|
| 1 | `id` | INTEGER | PK | 内部主键 |
| 2 | `from_id` | INTEGER | NOT NULL, FK→people(id) | 关系发起方（有向关系的「源」，无向关系任取一方） |
| 3 | `to_id` | INTEGER | NOT NULL, FK→people(id) | 关系接收方（有向关系的「目标」） |
| 4 | `relation_type` | TEXT | NOT NULL, FK→relation_types(relation_key) | 关系类型 |
| 5 | `note` | TEXT | | 备注（如「微积分发明优先权之争」「数学双星」） |
| 6 | `source` | TEXT | | 数据来源（Wikidata / 人工标注 / 文献） |

```sql
CREATE TABLE person_relation (
    id            INTEGER PRIMARY KEY,
    from_id       INTEGER NOT NULL REFERENCES people(id),
    to_id         INTEGER NOT NULL REFERENCES people(id),
    relation_type TEXT    NOT NULL REFERENCES relation_types(relation_key),
    note          TEXT,
    source        TEXT,
    UNIQUE (from_id, to_id, relation_type)   -- 防重复录入
);
```

### 2.3 关系使用示例

| 需求 | 数据（from → to, type, note） | 查询 |
|---|---|---|
| 祖冲之 → 祖暅之 父子 | (祖冲之, 祖暅之, `parent-child`, NULL) | `WHERE relation_type='parent-child'` |
| 阿贝尔 ⇄ 伽罗瓦 数学双星 | (阿贝尔, 伽罗瓦, `co-honored`, "数学双星") | `WHERE relation_type='co-honored'` |
| 康托尔 ⇄ 克罗内克 仇敌 | (康托尔, 克罗内克, `rival`, NULL) | `WHERE relation_type='rival'` |
| 牛顿 ⇄ 莱布尼茨 争议 | (牛顿, 莱布尼茨, `controversy`, "微积分发明优先权之争") | `WHERE relation_type='controversy'` |
| 学术家谱（递归查 Gauss 导师链） | `WITH RECURSIVE` 沿 `advisor-student` | 见下 |

**无向关系约定**：`rival`/`controversy`/`colleague` 等无向类型，插入时按 `MIN(id) → MAX(id)` 方向存储（`UNIQUE` 保证不重复），查询时 `from_id IN (?,?) AND to_id IN (?,?)` 双向命中。

**有向关系约定**：`parent-child`（父→子）、`advisor-student`（师→生）有明确方向，递归查询只用单向边。

### 2.4 递归查询示例（学术家谱）

```sql
WITH RECURSIVE lineage(id) AS (
    SELECT id FROM people WHERE name_en = 'Carl Friedrich Gauss'   -- 起点
    UNION
    SELECT r.to_id FROM person_relation r JOIN lineage l ON r.from_id = l.id
    WHERE r.relation_type = 'advisor-student'                      -- 向学生方向扩展
)
SELECT * FROM people WHERE id IN lineage;
```

---

## 三、`occupations` 职业字典 + `person_occupation`

### 3.1 `occupations`

| # | 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|---|
| 1 | `id` | INTEGER | PK | |
| 2 | `name_en` | TEXT | UNIQUE, NOT NULL | 职业英文（mathematician / physicist / writer / poet / economist…） |
| 3 | `name_zh` | TEXT | | 职业中文（数学家 / 物理学家 / 文学家 / 诗人…） |

> 职业语义对应 Wikidata `occupation` 属性。新增职业 = 加一行。

### 3.2 `person_occupation`（人 ↔ 职业，多对多）

| # | 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|---|
| 1 | `person_id` | INTEGER | NOT NULL, FK→people(id) | |
| 2 | `occupation_id` | INTEGER | NOT NULL, FK→occupations(id) | |
| 3 | `rank` | INTEGER | DEFAULT 0 | 主次排序（0=主职业；牛顿主=mathematician） |

```sql
CREATE TABLE person_occupation (
    person_id     INTEGER NOT NULL REFERENCES people(id),
    occupation_id INTEGER NOT NULL REFERENCES occupations(id),
    rank          INTEGER DEFAULT 0,
    PRIMARY KEY (person_id, occupation_id)
);
```

---

## 四、`fields` 领域字典 + `person_field`

### 4.1 `fields`

| # | 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|---|
| 1 | `id` | INTEGER | PK | |
| 2 | `name_en` | TEXT | UNIQUE, NOT NULL | 领域英文（number theory / algebra / condensed matter / literature / poetry…） |
| 3 | `name_zh` | TEXT | | 领域中文 |

> 对应 Wikidata `field_of_work` 属性；文学家可挂 literature/poetry 等领域。

### 4.2 `person_field`（人 ↔ 领域，多对多）

| # | 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|---|
| 1 | `person_id` | INTEGER | NOT NULL, FK→people(id) | |
| 2 | `field_id` | INTEGER | NOT NULL, FK→fields(id) | |
| 3 | `rank` | INTEGER | DEFAULT 0 | 主次排序 |

---

## 五、`awards` 奖项字典 + `award_laureate` 获奖关系

### 5.1 `awards`

| # | 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|---|
| 1 | `id` | INTEGER | PK | |
| 2 | `name_en` | TEXT | UNIQUE, NOT NULL | 奖项英文（Fields Medal / Turing Award / Nobel Prize in Literature…） |
| 3 | `name_zh` | TEXT | NOT NULL | 奖项中文（菲尔兹奖 / 图灵奖 / 诺贝尔文学奖…） |
| 4 | `award_type` | TEXT | NOT NULL | 类别：`math_top`(数学四大) / `math_icm`(ICM 配套) / `cs`(计算机) / `statistics`(统计) / `nobel`(诺贝尔家族) / `cross`(跨学科) / `honor`(院士/奖章类) |
| 5 | `tier` | INTEGER | | 梯队 1/2/3（对应 `math_awards_tiers.md`） |
| 6 | `org` | TEXT | | 颁发机构（ACM / 瑞典皇家科学院…） |
| 7 | `established` | INTEGER | | 设立年份（1966 / 1901…） |
| 8 | `wiki_url` | TEXT | | Wikipedia 链接 |
| 9 | `icon_key` | TEXT | UNIQUE | 徽标 key（nobel / kyoto / fields…；NULL=无徽标） |

> 数据源：`awards_list.md`（30+ 奖项）+ `math_awards_tiers.md`（tier）。

### 5.2 `award_laureate`（人 ↔ 奖项，多对多）

| # | 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|---|
| 1 | `person_id` | INTEGER | NOT NULL, FK→people(id) | |
| 2 | `award_id` | INTEGER | NOT NULL, FK→awards(id) | |
| 3 | `year` | INTEGER | NOT NULL | 获奖年份（图灵=获奖年份；数学奖=颁奖年份） |
| 4 | `edition` | INTEGER | | 届次（图灵奖第几届；数学奖 ICM 届次可空） |
| 5 | `share_type` | TEXT | | 独享 solo / 共享 shared / 可空 |
| 6 | `note` | TEXT | | 备注（「首位华人」「最年轻得主」…） |
| 7 | `source` | TEXT | | 数据来源（Wikipedia / Wikidata / 人工核对） |

```sql
CREATE TABLE award_laureate (
    person_id INTEGER NOT NULL REFERENCES people(id),
    award_id  INTEGER NOT NULL REFERENCES awards(id),
    year      INTEGER NOT NULL,
    edition   INTEGER,
    share_type TEXT,
    note      TEXT,
    source    TEXT,
    PRIMARY KEY (person_id, award_id, year)   -- 防重复录入
);
CREATE INDEX idx_al_award ON award_laureate(award_id);
CREATE INDEX idx_al_year  ON award_laureate(year);
```

> **核心表**：交叉荣誉（双料/三料）、「图灵+阿贝尔」等查询全部由它 GROUP BY / JOIN 得出。对应 `HONORS` 字典（36 人交叉荣誉）与 `all_cross_reference.md`。

---

## 六、`institutions` 机构字典 + `person_institution`

### 6.1 `institutions`

| # | 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|---|
| 1 | `id` | INTEGER | PK | |
| 2 | `name_en` | TEXT | UNIQUE, NOT NULL | 机构名（University of Göttingen…） |
| 3 | `name_zh` | TEXT | | 中文名 |

### 6.2 `person_institution`（人 ↔ 机构，多对多）

| # | 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|---|
| 1 | `person_id` | INTEGER | NOT NULL, FK→people(id) | |
| 2 | `inst_id` | INTEGER | NOT NULL, FK→institutions(id) | |
| 3 | `relation` | TEXT | NOT NULL | 关系类型：`employer` / `educated_at` / `member_of` / `affiliation` |
| 4 | `start_year` / `end_year` | INTEGER | | 起止年份（可空） |

```sql
CREATE TABLE person_institution (
    person_id INTEGER NOT NULL REFERENCES people(id),
    inst_id   INTEGER NOT NULL REFERENCES institutions(id),
    relation  TEXT NOT NULL,
    start_year INTEGER,
    end_year   INTEGER,
    PRIMARY KEY (person_id, inst_id, relation)
);
```

---

## 七、展示层（可选）：`episodes` + `badge_defs`

> 这两张属于图灵奖视频/beamer 展示层配置。若数据库只承载纯数据，可留在生成器配置文件中不建表。

### 7.1 `episodes`（对应 `gen_turing.py: EPISODES`）

| # | 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|---|
| 1 | `id` | INTEGER | PK | |
| 2 | `ep_key` | TEXT | UNIQUE, NOT NULL | ep01–ep10 |
| 3 | `dir` | TEXT | | episode-01-theory-computation… |
| 4 | `main` | TEXT | | tex 主文件名 |
| 5 | `title_zh` | TEXT | | 主题（理论计算机科学…） |
| 6 | `subtitle_zh` | TEXT | | 副标题（计算复杂性·算法·随机性…） |
| 7 | `year_range` | TEXT | | 年份区间（1966–2023） |
| 8 | `note` | TEXT | | 备注（从 Cook 到 Wigderson…） |

### 7.2 `badge_defs`（对应 `AWARD_ICONS` + `BADGE_DEFS`）

| # | 字段 | 类型 | 约束 | 说明 |
|---|---|---|---|---|
| 1 | `icon_key` | TEXT | PK | 中文 key：诺贝尔 / 京都 / 沃尔夫… |
| 2 | `latex_cmd` | TEXT | | LaTeX 徽标命令（\nobelbadge…） |
| 3 | `symbol` | TEXT | | 符号（\faIcon{award} / $\blacklozenge$…） |
| 4 | `color` | TEXT | | 品牌色 key（nobelclr…，对应 COLORS RGB） |
| 5 | `letter` | TEXT | | 字母（N / K / W…） |
| 6 | `full_name_zh` | TEXT | | 全称（诺贝尔奖 / 京都奖…） |

> 数据源：`gen_turing.py AWARD_ICONS`（19 条）+ `gen_turing_beamer.py BADGE_DEFS`（19 条，含 symbol/color/letter）。

---

## 八、检索策略（多值标签怎么查）

**两种检索场景用不同机制，不要混用：**

### 8.1 精确过滤（「谁是物理学家」「菲尔兹+阿贝尔双料」）
→ 走**规范化关系表 + B-tree 索引**，不用冗余列、不用 JSON、不用位图：

```sql
-- 列出所有物理学家
SELECT p.* FROM people p
JOIN person_occupation po ON po.person_id = p.id
JOIN occupations o        ON o.id = po.occupation_id
WHERE o.name_en = 'physicist';

-- 图灵 + 阿贝尔 双料（按人分组统计获奖数）
SELECT p.id, p.name_en, COUNT(*) AS n
FROM award_laureate al JOIN people p ON p.id = al.person_id
WHERE al.award_id IN (SELECT id FROM awards WHERE name_en IN ('Turing Award','Abel Prize'))
GROUP BY p.id HAVING n = 2;
```

### 8.2 模糊全文检索（搜「牛顿 微积分」「群论 数学家」）
→ 用 **FTS5 虚拟表**（与关系表两套机制），把多值标签 JOIN 拼接后物化进索引：

```sql
CREATE VIRTUAL TABLE people_fts USING fts5(
    name_en, name_zh, name_variants, description,
    occupations,   -- 由 person_occupation JOIN 拼接成 'mathematician physicist' 文本
    fields,        -- 同上
    content=''
);
-- 中文友好：建表时用 tokenize = 'trigram'（支持子串匹配），或入库前用 jieba 预分词
SELECT * FROM people_fts WHERE people_fts MATCH 'physicist AND calculus';
```

### 8.3 为什么不用位图 / JSON 做检索

| 方案 | 问题 |
|---|---|
| **JSON 列** `["mathematician","physicist"]` | `json_each()` 展开无法走索引 → 万行级全表扫；只适合展示，不适合过滤 |
| **位图 bit** | 位宽受限（64 位=最多 64 种职业），职业字典会随 10000+ 人增长；不可读、难维护、无法带 rank |
| **关系表**（本设计） | JOIN + 索引毫秒级；新增职业加一行；可带 rank/年份等属性 |

> 位图仅适用于「数量固定且 ≤64 的枚举」，如 `awards.award_type`（约 7 种）；职业/领域这种会增长的字典一律用关系表。

### 8.4 冗余列 `primary_occupation` 的定位

- 存职业**名称字符串**（非 id），仅用于**列表/封面展示**，不建索引、不参与检索；
- 检索一律 JOIN `person_occupation`（真实归属），`rank=0` 即主导职业；
- 冗余列可与关系表互相校验一致性（`verify.py` 检查 `primary_occupation == person_occupation(rank=0)`）。

---

## 九、表清单总览（12 张）

| 表 | 状态 | 核心字段 |
|---|---|---|
| `people` | ✅ 已细化 | qid/name_en/name_zh/variants/生卒/地点/描述/wiki/local_dir/primary_occupation |
| `occupations` / `person_occupation` | ✅ 已细化 | name_en(+zh)；person+occupation+rank |
| `fields` / `person_field` | ✅ 已细化 | name_en(+zh)；person+field+rank |
| `awards` / `award_laureate` | ✅ 已细化 | 名称/类型/梯队/机构/设立/wik/icon；person+award+year+edition+share |
| `institutions` / `person_institution` | ✅ 已细化 | name_en(+zh)；person+inst+relation+起止年 |
| `person_relation` + `relation_types` | ✅ 已细化 | from/to/type/note/source |
| `episodes` | ✅ 已细化（展示层） | ep_key/title/subtitle/range/note |
| `badge_defs` | ✅ 已细化（展示层） | icon_key/latex_cmd/symbol/color/letter/full_name |
