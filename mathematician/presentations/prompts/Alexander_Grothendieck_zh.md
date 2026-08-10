# Alexander Grothendieck — 立传提示词（数据库同步版）

> **用途**：为 Alexander Grothendieck 制作中文 Beamer 立传（`Alexander_Grothendieck_zh.tex`），并同步将社会关系写入 `greatminds` 数据库。
> **输出位置**：`mathematician/presentations/Alexander_Grothendieck/`
> **数据库**：`mysql -u root greatminds`（仅监听 127.0.0.1）
> **参考模板**：`prompts/David_Hilbert_zh.md`（结构范式）、`Mathematician_Biography_Guide.md`（制作规范 + §二十 社会关系入库）

---

## 人物速览

| 项目 | 内容 |
|---|---|
| 中文名 | 亚历山大·格罗滕迪克 |
| 英文名 | Alexander Grothendieck |
| 称号 | **数学教皇**（Le Pape des mathématiques） |
| 生卒 | 1928-03-28 — 2014-11-13（享年 86） |
| 国籍 | 法国（出生时无国籍，父德国，母德国——战乱流亡） |
| qid | Q77141 |
| 排名 | 20 世纪数学巨匠 #7（原榜 #4） |
| 领域 | 代数几何、泛函分析、范畴论、同调代数、拓扑 |
| 主要成就 | 概形理论、拓扑斯、上同调、动机理论、Weil 猜想、GRR |
| 代表机构 | CNRS、IHÉS、Collège de France、巴黎十一大、蒙彼利埃大学 |

---

## 关键参考文件

| 文件 | 用途 |
|---|---|
| `mathematician/pages/Alexander_Grothendieck/page.md` | Wikipedia 离线正文（事实来源） |
| `mathematician/pages/Alexander_Grothendieck/metadata.json` | Wikidata 结构化元数据（qid/生卒/国籍/导师/学生/领域/获奖） |
| `mathematician/presentations/Alexander_Grothendieck/Alexander_Grothendieck_zh.tex` | 已存在的立传 tex（17 个 section，可直接参考/优化） |
| `mathematician/presentations/prompts/David_Hilbert_zh.md` | 提示词结构范式 |
| `mathematician/presentations/Mathematician_Biography_Guide.md` | 制作规范 + **§二十 社会关系入库** |
| `MySQL/schema_mysql.sql` | 数据库表结构（`person_relation` / `relation_types`） |
| `MySQL/seed_grothendieck_relations.py` | 社会关系入库参考脚本（已执行） |

---

## 你的任务

按照 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md) 第十一节「推荐制作流程」的步骤，依次完成。**每完成一步向我汇报进度**，遇到歧义时先征求我的意见再继续。

> **数据库同步要求**：本提示词包含「社会关系梳理 + 入库」步骤（第 4.5 步），完整规范见工作指南 **§二十**。请将 Grothendieck 的社会关系（导师 Schwartz/Dieudonné、学生 Deligne/Illusie/Verdier 等）写入 `greatminds` 数据库 `person_relation` 表，缺失人物先建占位、关系打 `[材料待展开]` 标识。参考脚本：`MySQL/seed_grothendieck_relations.py`（已执行，12 条关系入库，缺失 7 人占位）。

---

## 第 0 步：核对元数据（metadata.json）

对照 `mathematician/pages/Alexander_Grothendieck/metadata.json` 核对以下字段，**确保 tex 与数据库一致**：

- **qid**：Q77141（数据库中已填）
- **生卒**：1928-03-28 — 2014-11-13（数据库已填「1928-03-28 – 2014-11-13」）
- **国籍**：France / statelessness / German Reich / Germany（**出生时无国籍**——史实亮点）
- **导师**：Laurent Schwartz、Jean Dieudonné
- **学生**：17 人（数据库已入库 Deligne、Illusie、Verdier、Raynaud、M. Artin、Mumford、Hartshorne）
- **领域**：algebraic geometry / functional analysis / category theory / homological algebra / topology
- **获奖**：Fields Medal / Émile Picard Medal / Crafoord Prize / Cours Peccot

> 提示词中的「人物速览」「数据库」两节保持与 metadata 一致；tex 中引用事实以 `page.md` 为准。

---

## 第 1 步：阅读材料，建立时间线（Grothendieck 专属）

**必读**：`page.md` + 现有 `Alexander_Grothendieck_zh.tex`（已含 17 个 section）。

### 史实要点（核对清单）

- **童年**：父亲 Alexander Schapiro（无政府主义者，二战被纳粹杀害于奥斯维辛）；母亲 Hanka Grothendieck；Grothendieck 随父母辗转，曾在法国 Gurs 集中营（1939–1942）；
- **教育**：蒙彼利埃大学（"差生"阶段）→ 巴黎高等师范 → 南锡大学（1950–1953，师从 Schwartz、Dieudonné，泛函分析）；
- **Tôhoku 论文（1957）**：重新组织同调代数（层、阿贝尔范畴、导出函子），奠定范畴论视角；
- **IHÉS 黄金时代（1958–1970）**：Dieudonné 的条件——必须同时聘请 Grothendieck；主导 SGA 研讨班；
- **四大支柱**：概形（scheme）、拓扑斯（topos）、上同调（cohomology）、动机（motives）；
- **两座丰碑**：Grothendieck–Riemann–Roch、Weil 猜想（部分，Deligne 完成）；
- **EGA / SGA / FGA**：数万页集体工程，与 Dieudonné 合著 EGA；
- **决裂与出走**：1970 年退出 IHÉS（军方资助争议），赴越南河内丛林讲课（和平主义）；
- **隐居（1980s–2014）**：Les Aumettes 隐居，写《收获与播种》（Récoltes et semailles）等大量未公开手稿；
- **获奖**：1966 菲尔兹奖（拒绝去莫斯科领奖）；1988 克拉福德奖（拒绝领奖，反战立场）。

### 已确认的人物关系（第 4.5 步入库范围）

| 关系类型 | 人物 | 方向 |
|---|---|---|
| 导师 | Laurent Schwartz、Jean Dieudonné | Schwartz/Dieudonné → Grothendieck |
| 学生 | Pierre Deligne、Luc Illusie、Jean-Louis Verdier、Michel Raynaud、Michael Artin、David Mumford、Robin Hartshorne | Grothendieck → 学生 |
| 同事 | Jean-Pierre Serre（IHÉS）、Leila Schneps、Pierre Lochak | 无向 |

> 上述 12 条关系已通过 `seed_grothendieck_relations.py` 入库，数据库同步要求已满足。若 tex 材料中发现新的关系（如 Bourbaki 成员关系），按 §二十 补入。

---

## 第 2 步：确定 Beamer 结构（参照现有 tex 的 17 个 section）

现有 `Alexander_Grothendieck_zh.tex` 已含完整 section 序列，建议保留并优化：

| section | 内容 |
|---|---|
| 封面 | 数学教皇：亚历山大·格罗滕迪克 (Alexander Grothendieck) |
| 为什么称他"数学教皇" | Le Pape des mathématiques |
| 动荡的童年 | 无政府主义者的孩子 |
| 惊人的崛起 | 从蒙彼利埃"差生"到泛函分析权威 |
| IHÉS 黄金时代 (1958–1970) | Dieudonné 的条件 |
| 他改变了什么 | 从"研究单个方程"到"研究方程所在的宇宙" |
| 四大支柱 | 概形 · 拓扑斯 · 上同调 · 动机 |
| 两座丰碑 | GRR 与 Weil 猜想 |
| 十二个"伟大思想" | 《收获与播种》自述 |
| 纸上的大教堂 | EGA · SGA · FGA |
| 隐居中的火山 | 1980 年代未公开手稿 |
| 决裂与出走 | 河内丛林里的范畴论课 |
| 最后的隐者 | 从数学到神秘主义 |
| 永恒的遗产 | 他重塑了数学"思考问题"的方式 |
| Tôhoku 论文 (1957) | 重新组织同调代数 |
| 不要研究 X，研究 X→S | 相对观点 |
| 动机 (Motives) | 未完成的梦想 |

---

## 第 3 步：设计配色方案

- 体现**寂静的深度与纯粹**：可用深靛蓝 + 米白 + 一点绯红（反战/激情）；
- 与已有人物配色区分（Hilbert 蓝金、Poincaré 靛紫、Noether 紫红、Weyl 墨绿）；
- 参考 `Mathematician_Biography_Guide.md` 配色规范。

---

## 第 4 步：撰写逐页文案

遵循指南「第 5–10 步」逐页编写，**每页 1 个 section**，重点：
- 封面：中文名 + 称号 + 生卒 + 国籍徽章（🌐 法国/无国籍）；
- 每页 footer 标准化（去国籍、去奖项、保留标签）；
- `text_width` 统一 13.0cm；
- 引号/破折号用中文全角。

---

## 第 5 步：编译验证

```bash
cd mathematician/presentations/Alexander_Grothendieck
make pdf          # 或 latexmk；卡死则 timeout 180 xelatex -interaction=nonstopmode 两遍
```

- 仅允许预存 overfull，`make pdf` 必须通过；
- 编译产物：`Alexander_Grothendieck_zh.pdf`。

---

## 第 6 步：数据库复核

```sql
SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
FROM person_relation pr JOIN people a ON a.id=pr.from_id
JOIN people b ON b.id=pr.to_id JOIN relation_types rt ON rt.relation_key=pr.relation_type
WHERE a.name_en='Alexander Grothendieck' OR b.name_en='Alexander Grothendieck';
```

- 若 tex 中新发现未入库关系（如 Bourbaki），按 §二十 补入；
- 完成后汇报：立传 PDF 路径 + 数据库关系数。

---

## 最终检查清单

- [ ] tex 结构（17 section）与现有文件一致或已优化
- [ ] 史实核对（童年/IHÉS/决裂/隐居/获奖 5 大节点）
- [ ] 数据库 12 条关系已入库、无重复
- [ ] 缺失人物占位（Dieudonné 等 7 人 has_biography=0）
- [ ] `make pdf` 编译通过
- [ ] 配色与已有人物区分
