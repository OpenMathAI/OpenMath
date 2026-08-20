# 麦克莱恩 (Saunders Mac Lane) 立传提示词

> 严格遵循 [Mathematician_Biography_Guide.md]。参考: cartan, weyl。

---

## 背景

- **目标**: Saunders Mac Lane (1909–2005)
- **气质**: **范畴论的共同创始人、同调代数的系统化者、Göttingen→Chicago 的美国数学建筑师**
- **Wikipedia**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Saunders_Mac_Lane/`

## 第 0 步：校验

- **生卒**：1909-08-04 ~ 2005-04-14，享年 95 岁
- **国籍**：美国
- **出生地**：Norwich, Connecticut, USA（家庭住在附近 Taftville）
- **博士导师**：Hermann Weyl（哥廷根大学）和 Paul Bernays（Bernays 因犹太身份被迫离开，Weyl 接替为主考官）
- **博士论文**：1934，数理逻辑
- **任职**：芝加哥大学 (1947–1982)
- **荣誉**：美国国家科学奖章 (1989)、Steele 奖 (1986)
- **合作者**：Samuel Eilenberg（50 年合作）、Garrett Birkhoff（《代数》教材）

### 时间线
- 1909: 生于康涅狄格
- 1931: 耶鲁本科
- 1933–1934: 在哥廷根大学——见证了纳粹上台前的最后岁月
- 1934: 博士（导师 Weyl）
- 1941: 与 Birkhoff 合著《现代代数》(A Survey of Modern Algebra)
- 1945: 与 Eilenberg 共同发表范畴论第一篇论文
- 1947: 芝加哥大学教授
- 1952–1958: Chicago 数学系主任
- 1960s: 将芝加哥建设为美国代数拓扑和范畴论的中心
- 1963: 《Homology》——同调代数经典教材
- 1971: 《Categories for the Working Mathematician》第一版
- 1986: 出版《Mathematics, Form and Function》
- 2005: 去世，95 岁

## 第 0.5 步：数据库字段核对（★ 补全 greatminds，规范见工作指南 §二十一）

> 对照 metadata.json 逐项核对下表并填值。缺失项按 §21.5 写 `MySQL/seed_maclane_full.py` 补齐。

| # | 表 | 字段 | 核对值 | 库中现状 |
|:--:|---|------|--------|:--:|
| 1 | `people` | qid | `Q441223` | ⚠️ 待核 |
| 2 | `people` | name_zh | `桑德斯·麦克兰恩` | ⚠️ NULL |
| 3 | `people` | name_variants | `["范畴论的奠基者","Eilenberg-MacLane 空间","《现代代数学概览》作者"]` | ⚠️ 空 |
| 4 | `people` | gender | `male` | ⚠️ NULL |
| 5 | `people` | birth_date / death_date | `1909-08-04` / `2005-04-14` | ⚠️ **NULL 全缺** |
| 6 | `people` | description | `American mathematician (1909–2005)` | ⚠️ 待核 |
| 7 | `person_occupation` | 职业 | `mathematician(0)`、`university teacher(1)` | ⚠️ 需补 |
| 8 | `person_field` | 领域 | `category theory`、`algebra`、`cohomology`、`abstract algebra`、`mathematics` | ⚠️ 待核 |
| 9 | `award_laureate` | 获奖 ★全部收录 | `Chauvenet 1941`、`Steele 1986`、`NMS 1989`、`Guggenheim`、`Procter`、`Humboldt` | ⚠️ 空 |
| 10 | `person_institution` | 教育/任职 | `education: Yale、Chicago、Göttingen`；`employment: Harvard、Cornell、Chicago、Columbia` | ⚠️ 全空 |
| 11 | `person_nationality` | 国籍 | `United States` | ⚠️ 待核 |
| 12 | `person_relation` | 社会关系 | 见第 4.5 步（7 条） | ⚠️ 仅 3 条 |
| 13 | `rankings` | 榜单 | `OpenMath_20th_Century_Top50` 待查 | ⚠️ |

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> 完整规范见工作指南 **§二十**。新建 `MySQL/seed_maclane_relations.py` 补足。

**入库范围（7 条）**：

| 关系类型 | 人物 | 方向 | 状态 |
|---|---|---|---|
| 导师 | Hermann Weyl → Mac Lane | 有向 | ✅ 在库（id=6） |
| 导师 | Paul Bernays → Mac Lane | 有向 | ⚠️ 占位 |
| 学生 | Mac Lane → John G. Thompson | 有向 | ✅ 在库（id=117，有限单群） |
| 学生 | Mac Lane → Irving Kaplansky | 有向 | ⚠️ 占位 |
| 学生 | Mac Lane → David Eisenbud | 有向 | ⚠️ 占位 |
| 合作者 | Samuel Eilenberg | 无向 | ✅ 在库（id=38，Eilenberg–MacLane 空间与范畴论） |
| 同事 | Emil Artin | 无向 | ✅ 在库（id=13，芝加哥学派） |

- 缺失人物（3 人）先建占位，note 加 `[材料待展开]`；幂等 `INSERT IGNORE`

---

## 核心贡献
| 领域 | 贡献 |
|------|------|
| 范畴论 | 与 Eilenberg 共同创立 |
| 同调代数 | Mac Lane 同调、bar construction |
| 代数 | 与 Birkhoff《现代代数》—— 革命性教材 |
| 数学哲学 | 《数学：形式与功能》 |
| 群上同调 | Eilenberg–Mac Lane 的群上同调理论 |

### ★ 叙事
1. **范畴论的双爸爸之一** — 与 Eilenberg 各贡献一半
2. **哥廷根的美国弟子** — 唯一在哥廷根受教于 Weyl 的美国博士生之一。他带回了德国数学的传统
3. **芝加哥学派的缔造者** — 单枪匹马把芝加哥变成了美国代数拓扑的中心
4. **数学的哲学家** — 《数学：形式与功能》是对"数学是什么"的深刻回答
5. **95 年的长寿** — 几乎见证了整个 20 世纪数学的发展

## ⚠️ 史实陷阱
- **博士导师** — 实际主要跟 Bernays 学习，但 Bernays 因犹太身份被纳粹驱逐，Weyl 接替为主考官
- **Homology 出版年份** — 1963（非 1971）
- **CWWM 首版年份** — 1971（非 1998，1998 是第二版）
- **范畴论的主角** — 与 Eilenberg 平等，不要写成"Eilenberg 主导"
- **哥廷根经验** — 1933-1934 是纳粹上台时期，Mac Lane 还师从 Emmy Noether

## ⚠️ 终审
| 点 | 检查 |
|----|------|
| 博士 | Göttingen 1934, Weyl/Bernays |
| 范畴论 | 1945 |
| Chicago | 1947–1982 |

## 配色：芝加哥栗红 + 范畴灰 + 哥廷根金
## 幻灯片（12 页）
01 封面
02 哥廷根的最后一批弟子
03 范畴论的诞生
04 Eilenberg–Mac Lane 50 年
05 现代代数教材
06 同调代数学
07 Chicago 学派的缔造
08 《数学：形式与功能》
09 美国国家科学奖章
10 遗产
11 结束页 — 他发明了数学的"语法"

## 音乐: Timeless + PAST

> **开始执行。**