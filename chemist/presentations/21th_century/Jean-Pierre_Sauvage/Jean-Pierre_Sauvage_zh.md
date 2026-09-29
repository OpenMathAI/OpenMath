# Jean-Pierre Sauvage（让-皮埃尔·索瓦日）立传提示词

> qid=Q3169751 · 1944-10-21 – 在世 · 法国配位化学家 · 21 世纪 · 诺贝尔化学奖（2016，与 Sir J. Fraser Stoddart、Bernard L. Feringa 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Jean-Pierre_Sauvage/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金色公式框 + 时间线页，是本次执行的版式语言。

---

## 0. 正文形式说明（参考桑格立传模板，★ 硬性要求）

1. **封面有头像位**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 `images.txt` **无真实肖像**（仅 1985 索烃晶体结构图与 1993 分子三叶结晶体结构图）——封面用主色装饰圆占位（圆内 `\faIcon{link}` 呼应互锁环），图注注明「装饰圆占位 · 页面无肖像」；正文两张晶体结构图务必用作插图（索烃/三叶结是本篇的视觉主角）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{book-open}\enspace 分子链环的建筑师\enspace·\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素（斯特拉斯堡大学 · 索烃/化学拓扑 · 2016 诺贝尔化学奖）。
3. **必须有身份信息页**（★ 必做）：左侧头像（装饰圆）+ 右侧 2×2 信息网格，至少含：生卒、本名 Jean-Pierre Sauvage、国籍 France、出生地 Paris、教育（ECPM Strasbourg 1967 / Université Louis-Pasteur PhD 1971）、博士导师 Jean-Marie Lehn、核心领域（coordination chemistry / supramolecular chemistry）、机构（University of Strasbourg）、荣誉。事实取自本地 page.md，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「链环 / 拓扑」母题——两两相扣的圆环暗示机械互锁。
5. **表格语义化 + 公式框**（★ 桑格版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Jean-Pierre Sauvage（法语发音 [ʒɑ̃pjɛʁ sovaʒ]；中文惯称：让-皮埃尔·索瓦日）
- **生卒**：1944-10-21 生于法国巴黎 → 在世（页面无卒日，全篇留白处理）
- **国籍**：France（法国）
- **身份**：配位化学家（coordination chemist）；斯特拉斯堡大学荣休教授（emeritus professor）
- **教育轨迹**：
  - 1967 毕业于斯特拉斯堡国立高等化学学校（National School of Chemistry of Strasbourg，今 ECPM Strasbourg）
  - 1971 Université Louis-Pasteur 博士（论文 *Les Diaza-polyoxa-macrobicycles et leur cryptats*，导师 Jean-Marie Lehn；博士工作期间参与首批 cryptand 配体的合成）
  - 博士后：Malcolm L. H. Green 实验室；后回斯特拉斯堡
- **导师**：Jean-Marie Lehn（1987 诺贝尔化学奖得主；supramolecular chemistry 创立者）
- **研究领域**：配位化学、超分子化学——基于配位化合物的索烃/分子结合成（化学拓扑）、分子机器；其他研究包括 CO2 电化学还原与光合反应中心模型

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **战时巴黎（1944）**：1944 年 10 月生于巴黎——战后一代化学家的起点。
2. **斯特拉斯堡之根（1967）**：国立高等化学学校毕业，此后一生与斯特拉斯堡绑定。
3. **Lehn 门下与穴醚（1971）**：在 1987 年诺奖得主 Lehn 指导下完成博士论文，参与首批 cryptand（穴醚）配体的合成——超分子化学的第一线。
4. **Green 实验室博士后**：赴 Malcolm L. H. Green 实验室做博士后（金属有机方向），随后返回斯特拉斯堡。
5. **1983：第一个索烃**：以两步策略首次合成索烃（catenane）——两个环状分子像锁链一样机械互锁而非共价相连；诺奖委员会称其为「迈向分子机器至关重要的第一步」。
6. **Cu(I) 模板策略**：以配位化学为骨架——铜离子作为模板把构件排布到位再关环；此后索烃与分子结的合成都立足于此（1993 年分子三叶结晶体结构中可见两个 Cu(I) 模板离子）。
7. **分子拓扑学**：化学拓扑（molecular topology）是其工作主轴——索烃、分子三叶结（molecular trefoil knot）等机械互锁体系的系统合成。
8. **分子机器的构象响应**：科学工作聚焦「对外部信号改变构象、从而模拟机器功能的分子」。
9. **旁支不废**：CO2 的电化学还原与光合反应中心模型——配位化学家的另一条战线。
10. **法兰西科学院（1990/1997）**：1990-03-26 当选通讯院士，1997-11-24 成为正式院士。
11. **2016 诺贝尔化学奖**：与 Sir J. Fraser Stoddart、Bernard L. Feringa 共享，官方理由 "for the design and synthesis of molecular machines"；三人分工——Sauvage 索烃（第一步）、Stoddart 轮烷与分子开关、Feringa 分子马达。
12. **美国科学院外籍院士（2019-04）**：当选 US National Academy of Sciences foreign associate。
13. **高影响力**：截至 2021 年，Google Scholar h-index 109、Scopus 100——配位化学家的「拓扑长跑」。

## 3. 配色方案（桑格式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（铜绿 verdigris） | `#175E54` | Cu(I) 模板与铜绿母题（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（索烃 badgeCatenane） | `#B0722A` | 铜橙·1983 第一个索烃 / 机械互锁 |
| 分类色 2（分子结 badgeKnot） | `#2E5A9E` | 蓝铜·1993 三叶结 / 化学拓扑 |
| 分类色 3（分子机器 badgeMachine） | `#7A1E28` | 深红·构象响应 / 分子机器第一步 |
| 分类色 4（能源方向 badgeEnergy） | `#4A5D23` | 橄榄绿·CO2 还原 / 光合反应中心模型 |
| 背景 | `#F7F6F9` | 浅灰白（与桑格版一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），两两相扣的圆环暗示索烃的机械键。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**With Me** — Alex-Productions（`music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav`；不要复制 wav 文件，Makefile 里直接引用原路径）
- **风格**：优雅 / 律动 / 手法精巧
- **匹配理由**：
  - 「精巧」匹配 Cu(I) 模板策略——以金属离子为手，把两个环编在一起
  - 「律动」匹配「分子机器」主题——互锁双环可以相对运动
  - 「优雅」匹配法国斯特拉斯堡学派的师承气质（Lehn → Sauvage）
- **时长**：按 Makefile 默认 `-shortest` 对齐 15 页即可

## 4. Slide 规划（15 页，桑格式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 分子链环的建筑师 / Jean-Pierre Sauvage 1944– + 四色 badge + 右上头像占位 + 国籍行「法国」
02  身份信息页（★ 必做）— 左头像占位 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/博士导师/领域/机构/荣誉）
03  索瓦日的一生 — 桑格式时间线（10 节点：1944→1967→1971→1983→1985→1990→1993→1997→2016→2019）
04  早年与 ECPM (1944–1967) — 表格「时间|事件|结果」
05  Lehn 门下：穴醚与博士 (1967–1971) — 表格「阶段|内容|结果」+ 公式框：cryptand ⊂ 金属离子（主客体）
06  1983：第一个索烃 — 表格「问题|方法|结果」+ 公式框：两环机械互锁 = 机械键；配 1985 索烃晶体结构图
07  Cu(I) 模板策略 — 表格「挑战|方法|结果」+ 公式框：Cu(I) 模板 → 定向关环
08  分子拓扑：三叶结 (1993) — 表格「问题|方法|结果」；配分子三叶结晶体结构图（含两个 Cu(I)）
09  2016 诺贝尔化学奖 — 公式框：官方获奖理由 "for the design and synthesis of molecular machines"（与 Stoddart / Feringa 共享，三人三步：索烃→轮烷→马达）
10  旁支战线：CO2 与光合反应中心 — 表格「问题|方法|结果」
11  荣誉与学会 — 桑格式「类别|代表|意义」表格 + itemize 清单（法兰西科学院 1990/1997 / Légion d'honneur 1999 / Ordre national du Mérite 2016 / NAS 外籍 2019）
12  斯特拉斯堡 — 桑格 LMB 页式流程图（1967 求学 → 1971 博士 → 1980s 索烃 → 荣休教授）
13  遗产：分子机器的第一环 — 四分类遗产盒 + 公式框：h-index 109（Google Scholar, 2021）
14  结尾 — 「把两个环扣在一起，机器就有了第一个关节。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2016 获奖理由 | 官方措辞 "for the design and synthesis of molecular machines"（本页原文引述一致）；**勿泛化成「发明分子机器」** |
| 共享口径 | 2016 为**三人共享**——Sauvage（1983 索烃，第一步）/ Stoddart（轮烷与分子开关）/ Feringa（分子马达）；页面原文："The other two recipients ... later creating a rotaxane and a molecular rotor"；对另两人一律用规范全名 Sir J. Fraser Stoddart / Bernard L. Feringa |
| 在世口径 | 页面无卒日——全篇写 1944-10-21 – 在世，**禁止编造卒年** |
| 索烃年份 | 诺奖工作=**1983** 首次合成索烃；1985 是晶体结构报道年（Chem. Commun. 244–247）；1993 是分子三叶结（Recl. Trav. Chim. 427–428）——三个年份勿混 |
| Cu 模板措辞 | 页面明载「基于配位化合物的索烃与分子结合成」及三叶结晶体结构中「两个 Cu(I) 模板离子」——可写 Cu(I) 模板策略；**勿写「铜离子模板效应由其独创」这类页面无载的优先权断言** |
| 博士导师 | Jean-Marie Lehn（博士论文 1971，Université Louis-Pasteur）——Lehn 是 **1987** 诺奖得主，勿写成 2016 或他人；Lehn 库内既有记录（id=3988），对手方名必须用「Jean-Marie Lehn」 |
| 博士后 | Malcolm L. H. Green 实验室——页面未载年份，**不写年份**；对手方名用「Malcolm L. H. Green」 |
| 学位拆分 | ECPM Strasbourg（1967 工程师训，页面作「毕业」非学位名目）与 Université Louis-Pasteur（PhD 1971）勿混 |
| 教职 | 现为斯特拉斯堡大学**荣休教授**（emeritus）——勿写成在职 |
| 院士年份 | 法兰西科学院：通讯院士 1990-03-26 → 正式院士 1997-11-24；US NAS foreign associate 2019-04——三组年份勿混 |
| h-index | 109（Google Scholar，2021）与 100（Scopus，2021）双口径——引用须注明来源与年份 |
| 引语红线 | 本页**无任何直接引语**——中文引号内不得出现无法在 page.md 溯源的「原话」，一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q3169751（回填既有记录 #4020） | ✅ |
| name_zh | 让-皮埃尔·索瓦日 | ✅ |
| name_en | Jean-Pierre Sauvage（与库内 #4020 记录精确一致，UPD 复用） | ✅ |
| birth_date | 1944-10-21 | ✅ |
| death_date | 空（在世） | ✅ |
| nationality | France | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | supramolecular chemistry（person_field 细分见下表，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| name_en | rank | name_zh |
|---|---|---|
| supramolecular chemistry | 0 | 超分子化学 |
| coordination chemistry | 1 | 配位化学 |
| molecular machines | 2 | 分子机器 |
| chemical topology | 3 | 化学拓扑 |

## 7. 社会关系入库清单

**师长 / 同行 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Jean-Marie Lehn | 师→生（博士导师） | Université Louis-Pasteur 博士导师（1971 论文穴醚大双环），Lehn 为 1987 诺奖得主 |
| colleague | Malcolm L. H. Green | 无向 | 博士后东家（页面未载年份） |
| co-honored | Fraser Stoddart | 无向 | 2016 诺贝尔化学奖共同得主 |
| co-honored | Ben Feringa | 无向 | 2016 诺贝尔化学奖共同得主 |

> **禁入库名单**：页面无其他明载个人关系；metadata.json 无额外关系字段。注意：Lehn 侧 yaml（Jean-Marie_Lehn.yaml）已有指向 Sauvage 的 advisor-student 行，两侧经 (from,to,type) 归一后幂等合并，**勿重复插入**。
> **对手方命名红线**：Stoddart/Feringa/Lindahl 等对手方一律用本批约定规范全名 Fraser Stoddart / Ben Feringa（防分裂 stub）。

## 8. 奖项清单

- CNRS Bronze Medal；CNRS Silver Medal（年份页面未载——如实标注）
- French Academy of Sciences（1990 通讯院士 / 1997 正式院士）
- Knight of the Légion d'honneur（1999）
- Grand Officer of the Ordre national du Mérite（2016）
- Nessim-Habif Award；Prelog Medal and Lecture；Centenary Prize；Grand prix Pierre-Süe；Order of the Rising Sun, Gold and Silver Star（年份页面未载——如实标注）
- Member of the US National Academy of Sciences（foreign associate，2019-04）
- Nobel Prize in Chemistry（2016，与 Stoddart / Feringa 共享）

## 9. 机构清单

- 教育：ECPM Strasbourg（National School of Chemistry of Strasbourg，1967 毕业）；Université Louis-Pasteur（PhD 1971，Lehn 实验室）；博士后 Malcolm L. H. Green 实验室
- 任职：University of Strasbourg（Strasbourg University；现荣休教授 emeritus professor）

## 10. 终审清单

- [ ] 生卒 1944-10-21 – 在世（全篇无卒日留白一致）；出生地 Paris
- [ ] 2016 三人共享（Stoddart / Feringa）表述准确；获奖理由 "for the design and synthesis of molecular machines" 口径准确
- [ ] 三人分工不串位：Sauvage=索烃（1983）/ Stoddart=轮烷 / Feringa=分子马达
- [ ] 1983 索烃 / 1985 晶体结构 / 1993 三叶结三个年份准确
- [ ] 博士导师 Jean-Marie Lehn（1971）；博士后 Malcolm L. H. Green（不写年份）
- [ ] 科学院年份三组准确（1990-03-26 / 1997-11-24 / 2019-04）
- [ ] 全篇无编造引语；「第一次/唯一」断言仅限页面明载（第一个合成索烃）
- [ ] 正文采用桑格式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make pdf` 编译通过，0 错误、vbox≤10pt、hbox≤50pt

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Jean-Pierre_Sauvage/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：装饰圆占位（页面无肖像），图注注明；两张晶体结构图（索烃/三叶结）就位
- [ ] 国籍：封面顶部明示法国
- [ ] 引语核对：本篇无引语——若 tex 中出现引号内英文原话须删改
- [ ] 编译验证：`make distclean && make pdf`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox<10pt、hbox<50pt 可接受）
- [ ] 身份信息页布局与桑格模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批（Modrich / Sancar / Stoddart / Feringa）及桑格既有格式对齐

---

> **名单状态**：`chemist/generate_21th_century_list.py` 由主控统一收尾，执行者不改。
> **数据事实来源唯一**：`chemist/presentations/21th_century/pages/Jean-Pierre_Sauvage/page.md`；页面无载的数据如实标注「页面无载」，禁止编造。
