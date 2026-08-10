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

数据或 schema 变更后，可删除库文件重新构建（字典种子会重新灌入；人物数据需重新跑 `seed.py`）：

```bash
cd db
rm -f greatminds.db
sqlite3 greatminds.db < schema.sql
```

## 八、当前表结构一览

| 表 | 类型 | 行数 | 说明 |
|---|---|---|---|
| `people` | 实体 | 0 | 人物主表（数学家/物理学家/文学家…） |
| `occupations` | 字典 | 13 | 职业 |
| `person_occupation` | 多对多 | 0 | 人 ↔ 职业 |
| `fields` | 字典 | 0 | 研究领域 |
| `person_field` | 多对多 | 0 | 人 ↔ 领域 |
| `awards` | 字典 | 42 | 奖项（数学四大/图灵/诺贝尔家族/统计…） |
| `award_laureate` | 多对多 | 0 | 人 ↔ 奖项（交叉荣誉核心） |
| `institutions` | 字典 | 0 | 机构 |
| `person_institution` | 多对多 | 0 | 人 ↔ 机构 |
| `relation_types` | 字典 | 8 | 社会关系类型（父子/师生/仇敌/争议…） |
| `person_relation` | 多对多 | 0 | 人物关系 |
| `episodes` | 展示层 | 10 | 图灵奖视频分集 |
| `badge_defs` | 展示层 | 19 | 徽标定义 |
