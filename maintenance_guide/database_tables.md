# 人物 / 奖项数据库 · 表清单

> 更新日期：2026-08-10（v2：主表改为 `people`，学科字典改为 `occupations`，可容纳文学家/经济学家/艺术家等所有人）
> 数据库：SQLite（选型见 `database_evaluation.md`）
> 本文件只列**表清单**；每张表的字段结构见后续文档（`database_schema.md`）。

---

## 一、设计原则

**人物、职业、奖项都不是独立实体表，而是「字典表 + 多对多关系表」。**

1. **人物统一 1 张主表 `people`**：数学家 / 物理学家 / 生物学家 / 化学家 / 计算机科学家 / 统计学家 / 天文学家 / **文学家 / 经济学家 / 艺术家 / 哲学家…** 全部入库，职业用标签（多对多）挂载——因为一人可跨多职业（如 Gauss = 数学+物理+天文；Russell = 数学家+哲学家+文学家）。
2. **奖项统一 1 张字典表 `awards`**：Fields / Wolf / Abel / Chern / COPSS / Turing / Nobel 家族（物理/化学/生理医学/经济/**文学**）/ 京都 / 哥德尔 / 香农等 30+ 奖项全部入库，获奖关系用多对多表——避免「每奖一表」导致交叉查询要 JOIN N 张表。
3. **新增职业 / 奖项 / 人物 = 往字典或主表加一行**，永不建新表。
4. **qid 全局唯一键**：Wikidata Q-ID 涵盖所有人类实体，是跨学科/跨领域的唯一身份标识（解决重名消歧）。

---

## 二、表清单（核心 10 张 + 展示层 2 张 = 12 张）

| # | 表名 | 类型 | 用途 | 对应需求 |
|---|---|---|---|---|
| 1 | `people` | 实体（主表） | **人物主表**：数学家/物理学家/生物学家/化学家/计算机科学家/**文学家/经济学家/艺术家…** 全部统一，qid 全局唯一键 | 数学家、物理学家、生物学家、化学家、计算机科学家、诺贝尔文学奖得主… |
| 2 | `occupations` | 字典 | **职业字典**：mathematician / physicist / biologist / chemist / computer scientist / statistician / astronomer / **writer / poet / economist / artist / philosopher…** | 上述人物的「职业标签」 |
| 3 | `person_occupation` | 多对多 | 人物 ↔ 职业（一人可属多个职业） | — |
| 4 | `fields` | 字典 | 研究领域字典：number theory / algebra / condensed matter / algorithms / **literature / poetry…** | — |
| 5 | `person_field` | 多对多 | 人物 ↔ 研究领域 | — |
| 6 | `awards` | 字典 | **奖项字典**：Fields / Wolf / Abel / Chern / COPSS / Turing / Nobel 家族（含 **Nobel Prize in Literature**）/ 京都 / 哥德尔 / 香农 / 汉明 / 马可尼…（全部 30+，可持续加） | 菲尔兹奖、阿贝尔奖、COPSS 奖、Turing 奖、Wolf 奖、**诺贝尔文学奖**… |
| 7 | `award_laureate` | 多对多 | 人物 ↔ 奖项（含获奖年份 / 届次 / 共享方式 / 备注） | — |
| 8 | `institutions` | 字典 | 机构字典：雇主 / 毕业院校 / 学会 | — |
| 9 | `person_institution` | 多对多 | 人物 ↔ 机构（含关系类型：employer / educated_at / member_of） | — |
| 10 | `person_relation` | 多对多（自引用） | 人物关系：导师 / 学生 / 合作者（学术家谱、师承关系） | — |
| 11 | `episodes` | 展示层（可选） | 图灵奖视频分集（ep01–ep10） | — |
| 12 | `badge_defs` | 展示层（可选） | 徽标定义（19 种，对应 AWARD_ICONS / BADGE_DEFS） | — |

> 备注：表 11、12 属于视频/beamer 展示层配置。若希望数据库只承载纯数据，可只保留 **核心 10 张**，分集与徽标留在生成器配置文件（`gen_turing.py`）中。

---

## 三、表关系总览

```
                    occupations ◄──┐
                    fields ◄─────┐ │
                                 │ │
  institutions ◄──┐              │ │
                  │              │ │
  ┌───────────────┴──┐   ┌───────┴─┴────────┐        ┌───────────┐
  │ person_institution│  │ person_relation  │        │  awards   │
  │ (person ↔ 机构)   │   │ (导师/学生/合作) │        └─────┬─────┘
  └───────────────┬──┘   └─────────┬────────┘              │
                  │                 │                        │
                  │        ┌────────┴───────┐               │
                  └────────►│    people    │◄───────────────┘
                            │  （主表）     │◄───────┐
                            └──────┬───────┘        │
                                   │                │
                    ┌──────────────┴─┐     ┌────────┴───────┐
                    │ person_occupation│   │  person_field  │
                    │ (↔ 职业)        │    │ (↔ 领域)       │
                    └────────────────┘    └────────────────┘
              ┌──────────────┐
              │ award_laureate │◄── (awards 通过它挂到 people)
              │ (↔ 奖项)      │
              └──────────────┘
```

**核心关系**：
- `people` 与 `occupations` / `fields` / `awards` / `institutions` / `people`（自引用）之间全部为**多对多**；
- `award_laureate` 的联合主键 `(person_id, award_id, year)` 防止同一人同一年同一奖重复录入；
- `person_relation` 自引用支持递归 CTE 查询师承谱系（导师→学生的祖先/后代）。

---

## 四、各类别如何落到表中（示例）

| 你要的数据 | 落到哪张表 |
|---|---|
| 「列出所有**物理学家**」 | `occupations`（name='physicist'）→ `person_occupation` → `people` |
| 「**菲尔兹奖**得主」 | `awards`（name='Fields Medal'）→ `award_laureate` → `people` |
| 「**诺贝尔文学奖**得主」 | `awards`（name='Nobel Prize in Literature'）→ `award_laureate` → `people` |
| 「同时拿 **图灵 + 阿贝尔** 的人」 | 两条 `award_laureate` 记录 JOIN（或 GROUP BY 统计） |
| 「Gauss 的**导师/学生**谱系」 | `person_relation` + `WITH RECURSIVE` |
| 「Knuth 的**领域**」 | `person_field` → `fields` |
| 「**诺贝尔物理学奖 + 数学家** 身份」 | `award_laureate`（Nobel Physics）+ `person_occupation`（mathematician）交叉 |
| 「数学**四大奖双料/三料**」 | `award_laureate` GROUP BY person_id 统计奖项数 |
| 「**数学家 + 文学家** 双身份（如罗素）」 | `person_occupation` 两条记录（mathematician + writer/philosopher） |

---

## 五、下一步

- [ ] 细化每张表字段（`people` 的 qid/生卒/国籍/描述、`award_laureate` 的年份/届次…）→ `database_schema.md`
- [ ] 写 `schema.sql`（建表 + 索引 + 约束）
- [ ] 写 `seed.py`（从现有 md / metadata.json / HONORS 灌库）
