# greatminds 数据库（MySQL 版）· 使用说明

> 本目录为 MySQL 版（从 SQLite 版迁移，2026-08-10）
> 数据库：`greatminds`（MySQL 9.x，Homebrew 本机，**仅监听 127.0.0.1**）
> 原 SQLite 版（`db/` 目录）已删除，如需 SQLite 源 schema 参考：`schema_sqlite_reference.sql`

---

## 一、连接数据库

```bash
# 命令行（root，本机无密码）
mysql -u root greatminds

# 中文正常显示
mysql -u root --default-character-set=utf8mb4 greatminds
```

## 二、查看表 / 视图

```sql
SHOW TABLES;                 -- 14 张表
SHOW FULL TABLES WHERE TABLE_TYPE='VIEW';   -- 5 个视图
DESCRIBE people;             -- 查看某表结构
```

## 三、常用查询

```bash
# 多奖得主（潜藏信息挖掘）
mysql -u root --default-character-set=utf8mb4 -e "USE greatminds; SELECT * FROM v_multi_award ORDER BY award_count DESC;"

# 奖项组合矩阵（哪些组合真实存在）
mysql -u root --default-character-set=utf8mb4 -e "USE greatminds; SELECT * FROM v_award_matrix ORDER BY n_persons DESC;"

# 某人全部获奖
mysql -u root --default-character-set=utf8mb4 -e "USE greatminds; SELECT award_zh, year FROM v_award_full WHERE name_en='J.-P. Serre';"

# 三料得主（Fields+Wolf+Abel）
mysql -u root --default-character-set=utf8mb4 -e "USE greatminds; SELECT p.name_en FROM people p WHERE (SELECT COUNT(*) FROM award_laureate al JOIN awards a ON a.id=al.award_id WHERE al.person_id=p.id AND a.name_en IN ('Fields Medal','Wolf Prize in Mathematics','Abel Prize')) = 3;"

# 某人社会关系
mysql -u root --default-character-set=utf8mb4 -e "USE greatminds; SELECT * FROM v_person_relations_bi WHERE person='G.H. Hardy';"
```

## 四、数据重建（从零）

数据源为各奖项目录的 Markdown 表，脚本按序执行（**必须保持此顺序**）：

```bash
cd MySQL
mysql -u root -e "DROP DATABASE greatminds; CREATE DATABASE greatminds CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
mysql -u root greatminds < schema_mysql.sql

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

> 脚本使用 `pymysql` 连接（见 `db_mysql.py`），自动将 SQLite 语法（`?` 占位符、`INSERT OR IGNORE`）转换为 MySQL。依赖：`pip3 install --break-system-packages pymysql`。

## 五、导出复查

```bash
python3 export_people.py --tsv                 # 一人一行 TSV（Excel 友好）
python3 export_people.py --tsv --only Serre    # 只看某人
python3 export_people.py                       # 每节一人（详细分节）
python3 export_people.py --one-line            # Markdown 表格
```

## 六、目录文件

| 文件 | 说明 |
|---|---|
| `schema_mysql.sql` | MySQL 建表 + 视图 + 字典种子 |
| `data_mysql.sql` | 一次性数据导入 SQL（SQLite→MySQL 迁移产物） |
| `migrate_sqlite2mysql.py` | SQLite→MySQL 迁移脚本（数据导出） |
| `convert_to_mysql.py` | 脚本改造工具（sqlite3→pymysql） |
| `build_seed_section.py` | 种子段提取工具（schema 维护用） |
| `db_mysql.py` | pymysql 连接模块（含 SQLite 语法适配） |
| `seed_*.py`（10 个） | 各奖项/榜单灌入脚本 |
| `export_people.py` | 导出工具 |
| `people_full.md` / `people_one_line.tsv` | 导出快照 |
| `schema_sqlite_reference.sql` | 原 SQLite schema（参考） |

## 七、当前表结构一览

| 表 | 行数 | 说明 |
|---|---|---|
| `people` | 337 | 人物主表 |
| `occupations` | 14 | 职业字典 |
| `person_occupation` | 337 | 人 ↔ 职业 |
| `fields` | 114 | 研究领域字典 |
| `person_field` | 383 | 人 ↔ 领域 |
| `awards` | 42 | 奖项字典 |
| `award_laureate` | 298 | 人 ↔ 奖项 |
| `rankings` | 108 | 排行榜 |
| `institutions` | 0 | 机构（待灌入） |
| `person_institution` | 0 | 人 ↔ 机构（待灌入） |
| `relation_types` | 8 | 关系类型字典 |
| `person_relation` | 3 | 人物关系 |
| `episodes` | 10 | 图灵视频分集 |
| `badge_defs` | 19 | 徽标定义 |
| `v_person_relations` | 3 | 关系视图 |
| `v_person_relations_bi` | 6 | 关系双向视图 |
| `v_multi_award` | 35 | 多奖得主视图 |
| `v_award_matrix` | 7 | 奖项组合矩阵 |
| `v_award_full` | 298 | 人物-奖项全明细 |
