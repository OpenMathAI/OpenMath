# 科学家/奖项数据引入数据库 · 选型评估（v2）

> 评估日期：2026-08-10（v2：纳入 10000+ 多学科科学家规模）
> 前置决策：先评估后选择「维持文本管理」，现用户决定**开始引入数据库**。
> **v2 新增**：`mathematician/`（11326 人）与 `physicist/`（2887 人）等人物库将扩展至 **10000+ 数学家 · 物理学家 · 自然科学家**，本文按此规模重估选型与数据模型。

---

## 一、背景与目标

### 1.1 现有数据形态（实际盘点）

| 数据 | 载体 | 规模 | 位置 |
|---|---|---|---|
| **数学家总列表** | Markdown（人名 + Wikipedia URL） | **11,326 人** | `mathematician/mathematicians.md` |
| **物理学家总列表** | Markdown | **2,887 人** | `physicist/physicists.md` |
| 已抓取人物完整页 | `page.html` + `page.md` + `metadata.json` + `images.txt` | **64 人**（持续扩展） | `mathematician/pages/<Name>/` |
| 人物 Wikidata 元数据 | JSON（occupation/nationality/生卒/field_of_work/award_received/导师/学生/学历/雇主…） | 64 人 | 同上 `metadata.json` |
| 图灵奖得主 | 目录 + `metadata.json` | 81 人（1966–2025，60 届） | `turing/pages/<year>/<name>/` |
| 图灵奖交叉荣誉 | Python 字典 `HONORS` | 36 人 | `turing/gen_turing.py` |
| 图灵奖分集/徽标 | `EPISODES` / `NAMES_BAR` / `AWARD_ICONS` / `BADGE_DEFS` | 10 集 · 19 徽标 | `turing/gen_turing.py`、`turing_beamer/gen_turing_beamer.py` |
| 数学四大奖交叉名录 | Markdown | 数百人 | `medal_list_allinone/all_cross_reference.md` |
| 奖项名册/分级 | Markdown | ~40 奖项 | `medal_list_allinone/awards_list.md`、`math_awards_tiers.md` |
| 离线 Wikipedia 页 | HTML + 解析脚本 | 900+ 页 | `turing/pages/`、`medal_list_allinone/pages/` |

**重要观察**：
- `metadata.json` 是 **Wikidata 结构化数据**（含 `qid`），字段多为**多值数组**（一个人多个 occupation / nationality / award / 导师 / 学生 / 机构）——这是数据库多对多关系的天然素材；
- 人物跨学科常见：如 Gauss = mathematician + physicist + astronomer + surveyor；学科分类应作为**标签/关系**而非固定列；
- 抓取流水线已成熟（`fetch_mathematicians.py` → `fetch_full_pages.py` → `to_tex.py`），数据库应作为**中间结构化层**嵌入，而非替换整条流水线。

### 1.2 引入数据库要解决的问题

1. **多对多关系查询**：人 ↔ 学科 ↔ 奖项 ↔ 年份 ↔ 届次 ↔ 导师/学生 ↔ 机构，Markdown/JSON 无法 JOIN、无法按维度筛选；
2. **多份文档漂移**：交叉荣誉在 `all_cross_reference.md`、`laurate_cross.md`、`turing_cross_reference.md`、`HONORS` 四处靠人肉同步；
3. **1 万+ 人物的一致性**：重名/消歧（`David_Abrahams_(mathematician)`）、Unicode 变体（Gregory/Grigory）、qid 去重，文本时代靠脚本堆叠；
4. **重复劳动**：新增/修正一位科学要在多个文件各改一遍；
5. **人物图谱**：导师-学生谱系、同学关系（Academic Genealogy）只有关系型结构才能低成本查询。

### 1.3 约束条件（决定选型方向）

- 数据规模：**目标 10000+ 科学家**（数学 11326 + 物理 2887 已有，未来自然科学家等）；单条 metadata < 10KB，全量结构化数据 < 500MB；
- **个人/本地维护**，无多用户并发、无远程访问需求；
- 读取方是 **Python 脚本**（抓取、生成器、校验、LaTeX 转换），项目为纯 Python + LaTeX 工作流；
- 需要**保持 git 可追踪**（此前大量工作基于 git 逐行 diff review）；
- 未来可能做**全文检索**（领域/贡献/履历）与**人物关系图**；
- 操作系统：macOS 本地。

---

## 二、候选数据库对比

| 维度 | **SQLite** | DuckDB | PostgreSQL | MySQL | MongoDB |
|---|---|---|---|---|---|
| 部署成本 | 零（Python 内置 `sqlite3`） | 一个 pip 包 | 需安装/启动服务 | 需安装/启动服务 | 需安装/启动服务 |
| 适用场景 | 嵌入式单机、小到中数据 | OLAP 分析型、大数据集 | 生产级多用户 Web | 生产级多用户 Web | 文档型、schema 多变 |
| 关系/多对多 | ✔ 原生（JOIN/UNIQUE/FK/CHECK） | ✔ | ✔ | ✔ | ✘ 需手写反范式 |
| 人物图谱（导师/学生） | ✔ 递归 CTE 支持 | ✔ | ✔ | ✔ | ✘ 弱 |
| 全文检索 | ✔ FTS5 | ✔ | ✔ | ✔ | ✔ |
| Python 集成 | 标准库，零依赖 | 需 pip | 需驱动 + 服务 | 需驱动 + 服务 | 需驱动 + 服务 |
| 文件形态 | 单个 `.db` 文件，可进 git | 单文件 | 服务端 | 服务端 | 服务端 |
| git diff 友好 | 二进制（可配 seed SQL） | 二进制 | ✘ | ✘ | ✘ |
| 万行级性能 | 轻松（SQLite 支持百万行） | 轻松 | 轻松 | 轻松 | 轻松 |
| 运维负担 | 无 | 无 | 有 | 有 | 有 |
| 对本项目匹配度 | **★★★★★** | ★★★☆☆ | ★★☆☆☆ | ★★☆☆☆ | ★★☆☆☆ |

**结论**：规模从 <2000 提升到 **10000+** 不改变结论——四条硬约束（单机、Python、git、关系模型）依然同时指向 **SQLite**；且 SQLite 在十万行级性能与可维护性上依旧最优。

---

## 三、推荐方案：SQLite

### 3.1 为什么是 SQLite（v2 补充）

1. **零依赖**：Python 标准库 `sqlite3` 直接可用，现有抓取/生成/校验脚本加几行代码即接入；
2. **单文件**：`scientists.db` 一个文件承载全部 10000+ 人结构化数据，整体备份/拷贝/进 git 皆可；
3. **git 可追踪**：以 `schema.sql` + `seed.py` 为 git 追踪源，`.db` 由脚本构建，兼顾「文本可 diff」与「数据库可查询」；
4. **关系模型天然契合**：人↔学科、人↔奖项、人↔导师/学生、人↔机构全是多对多，FK + UNIQUE 约束直接把「一致性」下沉到库层；
5. **FTS5 全文搜索**：对 1 万+ 人的领域/贡献/履历建全文索引，后续可快速检索；
6. **递归 CTE**：导师-学生谱系（学术家谱）可用 `WITH RECURSIVE` 一条 SQL 查询祖先/后代；
7. **性能足够**：SQLite 单库支撑千万行级别无压力，本项目 < 10 万行完全不在话下。

### 3.2 不建议的其他方案（一句话理由）

- **PostgreSQL / MySQL**：无并发、无远程、无权限需求，起服务纯属负担；PostgreSQL 的 JSONB/递归更强，但本项目用不到服务端能力；
- **MongoDB**：数据是强 schema 关系型（人、学科、奖项、年份、导师），文档模型丢失关系约束且不支持 JOIN，需手写反范式，反而更难维护；
- **DuckDB**：分析型列存，本项目是「增删改 + 一致性约束 + 简单查询 + 图谱」，非分析场景；
- **纯 JSON/继续文本**：已被本轮决策否定（1 万+ 人的关系查询与一致性是硬痛点）。

---

## 四、数据模型设计（ER）—— v2 扩展为多学科科学家库

```sql
-- ============ 表结构草案 v2 ============

-- 1) 科学家主表（数学家/物理学家/自然科学家统一入库，qid 全局唯一）
CREATE TABLE scientists (
    id            INTEGER PRIMARY KEY,
    qid           TEXT UNIQUE,               -- Wikidata Q-ID（去重/消歧关键）
    name_en       TEXT NOT NULL,             -- 英文名（含消歧后缀如 David Abrahams (mathematician)）
    name_zh       TEXT,
    name_variants TEXT,                      -- 别名 JSON 数组（Gregory/Grigory/中间名）
    gender        TEXT,
    birth_date    TEXT,                      -- ISO 日期
    death_date    TEXT,
    birth_place   TEXT,
    death_place   TEXT,
    description   TEXT,                      -- Wikidata 一句话描述
    wiki_url      TEXT,
    local_dir     TEXT UNIQUE,               -- 本地 pages/<Name>/ 相对路径
    PRIMARY_FIELD TEXT                       -- 主导学科（用于快速过滤，冗余列）
);

-- 2) 学科标签（多对多：人 ↔ 学科）
CREATE TABLE disciplines (
    id   INTEGER PRIMARY KEY,
    name TEXT UNIQUE                         -- mathematics / physics / chemistry / biology / computer science / astronomy / statistics ...
);
CREATE TABLE scientist_discipline (
    scientist_id  INTEGER NOT NULL REFERENCES scientists(id),
    discipline_id INTEGER NOT NULL REFERENCES disciplines(id),
    PRIMARY KEY (scientist_id, discipline_id)
);

-- 3) 领域（field of work，如 number theory / algebra）
CREATE TABLE fields (
    id   INTEGER PRIMARY KEY,
    name TEXT UNIQUE
);
CREATE TABLE scientist_field (
    scientist_id INTEGER NOT NULL REFERENCES scientists(id),
    field_id     INTEGER NOT NULL REFERENCES fields(id),
    PRIMARY KEY (scientist_id, field_id)
);

-- 4) 奖项（含既有全部大奖 + Wikidata award_received 全量）
CREATE TABLE awards (
    id          INTEGER PRIMARY KEY,
    name_en     TEXT NOT NULL UNIQUE,
    name_zh     TEXT,
    award_type  TEXT,                        -- math_top | cs | statistics | physics | cross | other
    tier        INTEGER,                     -- 1/2/3（对应 math_awards_tiers）
    org         TEXT,
    established INTEGER,
    wiki_url    TEXT,
    icon_key    TEXT                         -- 徽标 key（对应 AWARD_ICONS/BADGE_DEFS）
);

-- 5) 获奖记录（人 ↔ 奖项 多对多）
CREATE TABLE award_laureate (
    scientist_id INTEGER NOT NULL REFERENCES scientists(id),
    award_id     INTEGER NOT NULL REFERENCES awards(id),
    year         INTEGER NOT NULL,
    edition      INTEGER,                    -- 届次（图灵奖用）
    share_type   TEXT,                       -- 独享/共享
    note         TEXT,
    PRIMARY KEY (scientist_id, award_id, year)  -- 防重复录入
);

-- 6) 机构（雇主 / 毕业院校 / 出生地并入统一 entity？——机构单独建表）
CREATE TABLE institutions (
    id   INTEGER PRIMARY KEY,
    name TEXT UNIQUE
);
CREATE TABLE scientist_institution (
    scientist_id INTEGER NOT NULL REFERENCES scientists(id),
    inst_id      INTEGER NOT NULL REFERENCES institutions(id),
    relation     TEXT NOT NULL,              -- employer / educated_at / member_of ...
    PRIMARY KEY (scientist_id, inst_id, relation)
);

-- 7) 人物关系（导师/学生/合作者 —— 学术家图谱系）
CREATE TABLE scientist_relation (
    from_id  INTEGER NOT NULL REFERENCES scientists(id),
    to_id    INTEGER NOT NULL REFERENCES scientists(id),
    relation TEXT NOT NULL,                  -- doctoral_advisor / doctoral_student / doctoral_coadvisor
    PRIMARY KEY (from_id, to_id, relation)
);

-- 8) 图灵奖分集 / 徽标（EPISODES、NAMES_BAR、AWARD_ICONS 落库）
CREATE TABLE episodes (
    id          INTEGER PRIMARY KEY,
    ep_key      TEXT UNIQUE,                 -- ep01..ep10
    title_zh    TEXT,
    subtitle_zh TEXT,
    year_range  TEXT,
    note        TEXT
);
CREATE TABLE badge_defs (
    icon_key     TEXT PRIMARY KEY,
    latex_cmd    TEXT,                       -- \nobelbadge ...
    color        TEXT,
    letter       TEXT,
    full_name_zh TEXT
);

-- ============ 索引（1 万+ 人必须建） ============
CREATE INDEX idx_sci_name  ON scientists(name_en);
CREATE INDEX idx_sci_qid   ON scientists(qid);
CREATE INDEX idx_al_year   ON award_laureate(year);
CREATE INDEX idx_al_award  ON award_laureate(award_id);
CREATE INDEX idx_rel_rel   ON scientist_relation(relation);
```

### 4.1 与现有代码的对应关系（迁移映射）

| 现有文本/字典/JSON | 落库目标 |
|---|---|
| `mathematician/pages/<Name>/metadata.json`（Wikidata） | `scientists` + `disciplines` + `fields` + `institutions` + `scientist_relation` + `award_laureate` |
| `mathematicians.md` / `physicists.md`（11326+2887 人列表） | `scientists`（qid 缺失时用 name_en + 消歧后缀） |
| `turing/pages/<year>/<name>/metadata.json` | `scientists` + `award_laureate`（Turing 奖 + year/edition） |
| `gen_turing.py: HONORS` | `award_laureate`（36 人 × 交叉奖项） |
| `gen_turing.py: EPISODES` / `NAMES_BAR` | `episodes`（NAMES_BAR 由 award_laureate 派生） |
| `AWARD_ICONS` / `BADGE_DEFS` | `badge_defs`（合并同一表） |
| `all_cross_reference.md` 各节 | 查询 `award_laureate` 的 GROUP BY（双料/三料自动算出） |
| `awards_list.md` / `math_awards_tiers.md` | `awards`（tier/type/org/wikipedia） |

---

## 五、迁移与集成策略（不破坏现有 git 文本工作流）

**原则：文本/Markdown 仍是「展示与审阅层」，数据库成为「结构化真相层」；脚本双向同步，git 追踪脚本与数据 SQL，而非只追踪 .db。**

```
 markdown / JSON                SQLite 数据库
 ┌──────────────────┐  seed   ┌──────────────┐
 │ mathematicians.md │ ──────► │ scientists.db│
 │ metadata.json     │ build   │ (schema.sql  │
 │ all_cross_ref.md  │ ◄────── │  + data.sql) │
 │ HONORS(生成器)     │ export  └──────────────┘
 └──────────────────┘
        ▲ git 追踪：md + json + schema.sql + seed.py
```

### 5.1 建议落地结构（`mathematician/db/` 或顶层 `OpenMathAI/db/`）

```
db/
├── schema.sql          # 建表 + 索引 + 约束（git 追踪）
├── seed.py             # 解析 mathematicians.md / physicists.md / metadata.json / HONORS → 灌库
├── export.py           # 从库 → 生成/覆盖 md（all_cross_reference、交叉名录、winners 表）
├── verify.py           # 库级一致性（qid 重复、孤儿记录、年份越界、库 vs 文本 diff）
├── query.py            # 常用查询 CLI（--cross fields+turing / --genealogy Gauss / --search 群论）
└── scientists.db       # 生成物（可选进 git，或 .gitignore 由脚本重建）
```

### 5.2 同步流程

1. **首次**：`seed.py` 读 `mathematicians.md`（11326）+ `physicists.md`（2887）+ 已抓 `metadata.json`（64 人）+ `HONORS` → 灌库；
2. **抓取扩展**：`fetch_full_pages.py` 抓到新人物后，`seed.py --update` 增量入库（qid UNIQUE 去重）；
3. **日常改数据**：改 md/JSON → `seed.py` 增量更新 → `verify.py` 校验；
4. **反向**：直接改库 → `export.py` 生成最新 md 与生成器字典 → 交给 LaTeX/视频流水线；
5. **一致性硬约束下沉**：`PRIMARY KEY` / `UNIQUE` 自动防「同一人同一年同一奖重复」「同 qid 重复建档」，这是文本时代做不到的。

### 5.3 现有脚本改造点（最小侵入）

- `mathematician/fetch_full_pages.py`：抓取后自动调 `seed.py --ingest <dir>` 入库；
- `mathematician/to_tex.py`：元数据改从库读（无库回退读 metadata.json）；
- `turing/gen_turing.py`：`HONORS` 改为启动时 `SELECT ... FROM award_laureate`，无 DB 时回退内置字典；
- `medal_list_allinone/cross_verify.py`：对库做 JOIN 校验 + 对文本做 diff 校验，两处应一致；
- `turing_beamer/gen_turing_beamer.py`：`BADGE_DEFS` 读 `badge_defs` 表，`by_award` 分组由 SQL `GROUP BY` 完成。

---

## 六、分阶段实施步骤（按 10000+ 规模）

| 阶段 | 内容 | 产出 |
|---|---|---|
| **P0** | 建 `schema.sql`，写 `seed.py` 灌入 `mathematicians.md`(11326) + `physicists.md`(2887) + 已抓 metadata(64) + HONORS | `scientists.db` 与文本一致 |
| **P1** | 写 `verify.py`：qid/名字去重校验 + 库 vs 文本 diff | 一致性报告 |
| **P2** | 改 `fetch_full_pages.py` 抓取后自动入库（qid 增量去重） | 抓取即入库 |
| **P3** | 改 `to_tex.py` / `gen_turing.py` / `gen_turing_beamer.py` 读库 | 生成器数据源统一 |
| **P4** | 写 `export.py`，从库反哺 md（双料/三料名录、winners 表自动生成） | 消除文档漂移 |
| **P5** | FTS5 全文索引 + `query.py` CLI（跨学科检索、学术家谱） | 检索/图谱能力 |

> 每阶段保持「文本/JSON ⇄ 库」双向一致再进入下一阶段；git 提交以 `schema.sql` + `seed.py` 为主，`scientists.db` 是否入库二选一（建议 `.gitignore` 靠脚本重建）。

---

## 七、风险与注意事项（v2 补充）

1. **避免「库是唯一真相」一步到位**：现有抓取/生成/beamer/md 直接耦合，逐步双轨过渡，防止一次改造破坏流水线；
2. **消歧是 1 万+ 人的首要问题**：Wikipedia 文件名带 `(mathematician)`/`(physicist)` 消歧后缀 → 用 `qid` 作唯一键，`name_en` 保留原文件名，`name_variants` 存别名；重名（如多个 Abel/Jordan）必须靠 qid 区分；
3. **Unicode/中间名归一化**：`norm()` 规则（NFKD、Sergei/Novikov、Gregory/Grigory）应下沉为 seed 统一函数，避免各脚本各写各的；
4. **跨学科冗余列**：`scientists.PRIMARY_FIELD` 只是快速过滤冗余列，真实归属在 `scientist_discipline`，两者需 `verify.py` 保证一致；
5. **metadata.json 多值字段**：occupation/nationality/award_received 等数组必须拆到关系表，勿存逗号拼接字符串（否则无法 JOIN）；
6. **年份/届次语义**：图灵奖用「获奖年份」、数学奖用「颁奖年份」——统一在 `award_laureate.year` 并注释；
7. **共享奖项**（同一年多人）用 `share_type` 区分，导出 md 保持原文格式；
8. **不要引入 ORM**：规模虽到万级但结构固定，`sqlite3` 原生 + 少量辅助函数足够，避免多余依赖；
9. **数据合规**：抓取遵守 Wikimedia 限流与 UA 约定（现有 `fetch_*.py` 已实现指数退避），库只存公开元数据。

---

## 八、结论

**推荐 SQLite**：即使扩展到 **10000+ 数学家/物理学家/自然科学家**，SQLite 在零依赖、单文件、关系模型（人↔学科/奖项/导师/机构多对多）、git 可追踪（以 SQL/脚本形式）、FTS5 全文检索与递归 CTE（学术家谱）方面全部满足，性能毫无压力。迁移按 P0–P5 分阶段双轨进行，不破坏现有抓取与 LaTeX/视频生成流水线。
