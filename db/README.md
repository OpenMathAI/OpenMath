# 人物 / 奖项数据库 · 使用说明

> 数据库：SQLite（macOS 自带 `sqlite3`，无需安装）
> 库文件：`db/greatminds.db`（由 `db/schema.sql` 构建，含建表 + 种子数据）
> 设计文档：`maintenance_guide/database_tables.md`（表清单）、`database_schema.md`（表结构）、`database_evaluation.md`（选型）

---

## 一、进入数据库

```bash
sqlite3 /Users/ericksun/workspace/codebuddy/OpenMathAI/db/greatminds.db
```

看到 `sqlite>` 提示符即为交互模式，可输入 SQL 语句或 `.` 开头的命令。

## 二、交互模式常用命令

```sql
.tables                          -- 列出所有表
.schema                          -- 查看所有建表语句
.schema people                   -- 查看某张表的建表语句
.headers on                      -- 显示列名（推荐）
.mode column                     -- 表格对齐显示（推荐）
.mode line                       -- 每列一行显示（字段多时更清晰）
.quit                            -- 退出
```

## 三、一次性查询（不进交互模式）

```bash
# 列出所有表
sqlite3 db/greatminds.db ".tables"

# 带表头 + 列对齐查看某张表
sqlite3 -header -column db/greatminds.db "SELECT * FROM awards;"

# 查行数
sqlite3 db/greatminds.db "SELECT COUNT(*) FROM awards;"
```

> 提示：在项目根目录执行时库路径为 `db/greatminds.db`；在 `db/` 目录内则直接用 `greatminds.db`。

## 四、常用查询示例

```bash
# 全部奖项（名称 / 类型 / 梯队）
sqlite3 -header -column db/greatminds.db \
  "SELECT id, name_zh, award_type, tier FROM awards ORDER BY tier;"

# 数学四大奖（tier 1-2）
sqlite3 -header -column db/greatminds.db \
  "SELECT name_zh, name_en, tier FROM awards WHERE tier <= 2 ORDER BY tier;"

# 诺贝尔家族
sqlite3 -header -column db/greatminds.db \
  "SELECT name_zh FROM awards WHERE award_type='nobel';"

# 带徽标的奖项
sqlite3 -header -column db/greatminds.db \
  "SELECT a.name_zh, b.icon_key, b.letter FROM awards a JOIN badge_defs b ON a.icon_key = b.icon_key;"

# 职业字典
sqlite3 -header -column db/greatminds.db "SELECT * FROM occupations;"

# 关系类型字典
sqlite3 -header -column db/greatminds.db "SELECT * FROM relation_types;"

# 图灵奖视频分集
sqlite3 -header -column db/greatminds.db "SELECT ep_key, title_zh, year_range FROM episodes;"

# 某人的全部研究领域（多对多，含主次排序 rank）
sqlite3 -header -column db/greatminds.db \
  "SELECT p.name_en, f.name_en, pf.rank FROM person_field pf JOIN people p ON p.id=pf.person_id JOIN fields f ON f.id=pf.field_id WHERE p.name_en='John von Neumann' ORDER BY pf.rank;"

# 谁同时擅长 泛函分析 + 概率论（多领域交集查询）
sqlite3 -header -column db/greatminds.db \
  "SELECT p.name_en FROM person_field pf1 JOIN person_field pf2 ON pf1.person_id = pf2.person_id JOIN people p ON p.id = pf1.person_id JOIN fields f1 ON f1.id = pf1.field_id AND f1.name_en='functional analysis' JOIN fields f2 ON f2.id = pf2.field_id AND f2.name_en='probability theory';"

# 各领域有多少人（按人数排序）
sqlite3 -header -column db/greatminds.db \
  "SELECT f.name_en, COUNT(*) n FROM person_field pf JOIN fields f ON f.id = pf.field_id GROUP BY f.id ORDER BY n DESC LIMIT 10;"

# 领域最多的通才 Top 10（一人多领域统计）
sqlite3 -header -column db/greatminds.db \
  "SELECT p.name_en, COUNT(*) n FROM person_field pf JOIN people p ON p.id=pf.person_id GROUP BY p.id ORDER BY n DESC LIMIT 10;"

# ---- 社会关系（视图封装，一行即查） ----

# 全部关系（单向视图）
sqlite3 -header -column db/greatminds.db "SELECT from_name, relation, to_name, note FROM v_person_relations;"

# 查某人所有关系（双向视图，无需关心方向）
sqlite3 -header -column db/greatminds.db \
  "SELECT person, relation, other, note FROM v_person_relations_bi WHERE person='G.H. Hardy';"

# 关系类型字典
sqlite3 -header -column db/greatminds.db "SELECT relation_key, name_zh FROM relation_types;"
```

## 五、图形界面（可选）

- **DB Browser for SQLite**：免费开源，打开 `greatminds.db` 即可可视化浏览表、执行 SQL、导出数据。
  - 下载：<https://sqlitebrowser.org/>
- **VS Code 插件**：安装 "SQLite Viewer" 或 "SQLite" 扩展，点击 `.db` 文件即可浏览。

## 六、Python 方式

```python
import sqlite3
conn = sqlite3.connect('/Users/ericksun/workspace/codebuddy/OpenMathAI/db/greatminds.db')
rows = conn.execute("SELECT name_zh, tier FROM awards ORDER BY tier").fetchall()
print(rows)
```

## 七、重建数据库

数据或 schema 变更后，按固定顺序重建（注意：`biography` 必须在 `relations` 之前，因为 relations 会新增人物）：

```bash
cd db
rm -f greatminds.db
sqlite3 greatminds.db < schema.sql
python3 seed_ranking.py        # 20 世纪排名 108 人（people + rankings + 奖项）
python3 seed_fields.py         # 研究领域（Wikidata field_of_work + 标签提取）
python3 seed_biography.py      # 立传标志（扫描 presentations/）
python3 seed_relations.py      # 社会关系 + 补充人物（祖冲之/祖暅之）
python3 seed_fields_medal.py   # 菲尔兹奖 68 位得主
python3 seed_wolf_prize.py     # 沃尔夫奖 68 位得主
python3 seed_abel_prize.py     # 阿贝尔奖 29 位得主
python3 seed_chern_medal.py    # 陈省身奖章 5 位得主
python3 seed_turing.py         # 图灵奖 81 位得主
python3 seed_copss.py          # COPSS 会长奖 46 位得主
```

## 八、当前表结构一览

| 表 | 类型 | 行数 | 说明 |
|---|---|---|---|
| `people` | 实体 | 336 | 人物主表（数学家/物理学家/文学家…） |
| `occupations` | 字典 | 14 | 职业 |
| `person_occupation` | 多对多 | 336 | 人 ↔ 职业 |
| `fields` | 字典 | 114 | 研究领域 |
| `person_field` | 多对多 | 383 | 人 ↔ 领域 |
| `awards` | 字典 | 42 | 奖项（数学四大/图灵/诺贝尔家族/统计…） |
| `award_laureate` | 多对多 | 298 | 人 ↔ 奖项（交叉荣誉核心） |
| `rankings` | 字典 | 108 | 排行榜（20 世纪数学巨匠） |
| `institutions` | 字典 | 0 | 机构 |
| `person_institution` | 多对多 | 0 | 人 ↔ 机构 |
| `relation_types` | 字典 | 8 | 社会关系类型（父子/师生/仇敌/争议…） |
| `person_relation` | 多对多 | 3 | 人物关系 |
| `episodes` | 展示层 | 10 | 图灵奖视频分集 |
| `badge_defs` | 展示层 | 19 | 徽标定义 |
| `v_person_relations` | 视图 | 3 | 关系单向视图 |
| `v_person_relations_bi` | 视图 | 6 | 关系双向视图（查某人全部关系） |
