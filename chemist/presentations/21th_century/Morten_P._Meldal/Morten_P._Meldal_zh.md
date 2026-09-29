# Morten P. Meldal（莫滕·梅尔达尔）立传提示词

> qid=Q6914509 · 1954-01-16 生于丹麦（在世，卒日留白） · 丹麦化学家 · 21 世纪 · 诺贝尔化学奖（2022，与 Carolyn Bertozzi、Karl Barry Sharpless 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Morten_P._Meldal/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金色公式展示框 + 气泡背景。
> ★ 数据源说明：本篇 page.md 仅 49 行（无 Early life / Personal life / 完整荣誉列表小节），是全批次最短的页面之一——**所有内容严格以实载为准，严禁脑补**；信息不足处宁可少写，不得虚构。

---

## 0. 正文形式说明（参考 Frederick Sanger 模板，★ 硬性要求）

1. **封面头像缺位 → 装饰圆占位**（★ 本篇特例）：images.txt 为空，无任何图片——右上角用主色装饰圆 + 点击化学意象占位（tikz 圆内可绘叠氮-炔 1,2,3-三唑五元环简笔），并加小字注「肖像暂缺」。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{link}\enspace CuAAC 点击反应的发明人\enspace·\enspace 丹麦`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧装饰圆头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地（页面仅载 Denmark）、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「点击化学」母题——两个小圆一触即合（click），暗示叠氮与炔烃的高效环加成。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Morten Peter Meldal（中文惯称：莫滕·梅尔达尔）
- **生卒**：1954-01-16 生于丹麦（页面未载具体城市，出生地留"丹麦"勿杜撰；在世，卒日留白勿写）
- **国籍**：Denmark（丹麦）
- **身份**：化学家；哥本哈根大学化学教授
- **家庭**：页面无载（勿杜撰配偶/子女）
- **教育轨迹**：
  - Technical University of Denmark, DTU（BS、MS、PhD 化学工程；PhD 1983，论文《Reactions of Unsaturated Sugars with Hydrogen Halides》，导师 Klaus Bock，方向为碳水化合物的合成化学）
- **导师**：Klaus Bock（博士导师）
- **研究领域**：有机化学——点击化学（CuAAC）、多肽合成（固相合成仪器与方法）、组合化学库、N-酰基亚胺离子化学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **丹麦工程师之子（1954）**：页面无载童年细节——身份页只写出生丹麦、1954-01-16，其余从略（诚实呈现数据边界）。
2. **DTU 三级学位**：BS、MS、PhD 皆在丹麦技术大学（化学工程）；博士师从 Klaus Bock，做不饱和糖与卤化氢反应——碳水化合物的合成化学起步。
3. **三站博后（1983–1988）**：DTU → 剑桥大学 MRC 分子生物学实验室（LMB）→ 哥本哈根大学——有机化学博后，横跨固相多肽与分子生物学重镇。
4. **DTU 助理教授（1996）**：博后十年后回 DTU 任助理教授。
5. **嘉士伯实验室（1998–）**：主持化学系合成组——CuAAC 点击反应在此孕育。
6. **多 column 合成仪器（职业生涯早期）**：发明用于多肽与有机合成的多柱合成技术，以及大规模 split-mix 组合库的组装方法——仪器与方法学双料贡献。
7. **CuAAC 点击反应（2002 前后）**：首次提出乙炔与叠氮的环加成用于多肽、蛋白偶联、聚合物与材料科学——**与 Valery V. Fokin 和 K. Barry Sharpless 同时但相互独立**地发展出铜催化版本。
8. **正交性证明**：Meldal 组证明该反应对绝大多数官能团化学呈"正交"（orthogonal）——点击化学命名的实验根基之一。
9. **光学编码技术**：近年发展光学编码方法。
10. **固相上的有机+多肽融合**：有机化学与多肽化学在固相载体上的融合——N-酰基亚胺离子组合库，细胞基 on-bead 筛选 G 蛋白偶联受体活性物质。
11. **Betamab Therapeutics（2019–2021）**：基于 beta-body（抗体模拟肽）概念共同创办，公司 2021 年关闭——转化之路的起伏，如实呈现。
12. **2022 诺贝尔化学奖**：与 Carolyn R. Bertozzi、Karl Barry Sharpless 三人共享，"for the development of click chemistry and bioorthogonal chemistry"——CuAAC 与生物正交化学合流。
13. **丹麦荣誉**：Dannebrog 骑士勋章；H.C. Ørsted 金奖；多肽化学界荣誉（du Vigneaud Award、Hirschmann Award，年份页面未列）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（宝蓝 royalblue） | `#283593` | 点击化学"一触即合"的精确底色（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（点击化学 badgeClick） | `#2E5A9E` | 蓝 CuAAC / 叠氮-炔环加成 |
| 分类色 2（多肽合成 badgePeptide） | `#1B7A43` | 绿固相多 column 合成 / split-mix 库 |
| 分类色 3（组合化学 badgeCombo） | `#D97B29` | 琥珀N-酰基亚胺离子 / on-bead 筛选 |
| 分类色 4（转化与应用 badgeApply） | `#C0395B` | 玫瑰偶联/材料科学 / Betamab |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），两个小圆相触即合的「click」意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**PAST** — Alex-Productions（`music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav`；不要复制 wav 文件，Makefile 指向源路径）
- **风格**：沉静回望 / 纪录片质感
- **匹配理由**：
  - "PAST（过往）" 匹配其叙事气质——从 1980 年代碳水化合物化学与多肽仪器到 2022 年诺奖，是几十年沉潜的回望
  - "沉静" 匹配嘉士伯实验室式的北欧科研气质——不事张扬、方法为本
  - 与本批其他曲目错开（Doudna=Shine Like The Sun、List=Pathfinder、MacMillan=New Lands、Bertozzi=Timeless）
- **时长**：须 make video 时以 ffmpeg `-shortest` 自动对齐 15 页时长

## 4. Slide 规划（15 页，Sanger 式结构；★ 页面短，多页以"方法学脉络"扩充而非虚构生平）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — CuAAC 点击反应的发明人 / Morten P. Meldal 1954– + 四色 badge + 右上装饰圆（肖像缺位注记）+ 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右 2×2 信息网格（生卒/本名/国籍/出生地=丹麦/教育/博士/师承/领域/荣誉；家庭栏注"页面无载"）
03  梅尔达尔的一生 — 高斯式时间线（9 节点：1954→1983→1983–88 三站博后→1996→1998→2002→2019→2022，页面实载年份）
04  DTU：碳水化合物化学起步 (–1983) — 表格「阶段|内容|结果」（BS/MS/PhD；Klaus Bock；不饱和糖 + 卤化氢）
05  三站博后 (1983–1988) — 表格「站点|领域|收获」（DTU → MRC LMB 剑桥 → 哥本哈根）
06  多 column 合成与组合库 (1990s–) — 表格「问题|方法|结果」（多柱合成仪器 / split-mix 库）
07  嘉士伯实验室与 CuAAC (1998–2002) — 表格「问题|方法|结果」+ 公式框：叠氮-炔 [3+2] 环加成 → 1,2,3-三唑（Cu(I) 催化）
08  与 Sharpless/Fokin 的平行独立 — 高斯式对比页：三方同时独立发展的对比表格（Meldal 固相多肽偶联 / Sharpless-Fokin 溶液催化）+ 正交性证明
09  正交性：点击化学的根基 — 表格「官能团环境|反应|相容性」+ 公式框：orthogonal to the majority of functional group chemistries
10  固相融合与 GPCR 筛选 (2000s–2010s) — 表格「方法|内容|结果」（N-酰基亚胺离子库 / on-bead 细胞筛选 / 光学编码）
11  2022 诺贝尔化学奖 — 高斯 FFT 页式流程（Sharpless 2001 点击概念 → CuAAC 独立实现 → Bertozzi 活体生物正交 → 三人共享）；获奖理由原句
12  Betamab 与转化起伏 (2019–2021) — 表格「年份|事件|结果」（beta-body 公司创办→关闭；如实呈现）
13  荣誉清单 — 高斯式「类别|代表|意义」表格（Nobel 2022 / Dannebrog 骑士 / H.C. Ørsted 金奖 / du Vigneaud & Hirschmann 多肽奖；年份未列者注明）
14  结尾 — 「好的反应应该像扣上搭扣——一按即合，别处不动。」（意译点击化学理念，非原话直引）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2022 诺奖口径 | 与 Carolyn Bertozzi、Karl Barry Sharpless **三人共享**，官方理由 "for the development of click chemistry and bioorthogonal chemistry"；Meldal 的是 **CuAAC 反应**那一半——勿把生物正交化学写进其页（那是 Bertozzi 的贡献方向） |
| CuAAC 独立性 | 页面原句 "concurrently with but independent of Valery V. Fokin and K. Barry Sharpless"——**同时但独立**；勿写"师承 Sharpless"或"在 Sharpless 指导下"；也勿写"领先/首先"排序（页面未分先后） |
| 页面边界 | page.md 仅 49 行：无童年、无家庭、无配偶子女、无完整荣誉年表——身份页家庭栏注「页面无载」，荣誉年份未列者写"年份页面未列"，**严禁编造** |
| 出生地 | 仅载 Denmark（1954-01-16）——勿杜撰具体城市 |
| 学位口径 | DTU 的 BS、MS、PhD 皆化学工程（chemical engineering）；博士论文方向是碳水化合物的合成化学——勿写成"有机化学博士" |
| Fokin 角色 | Valery V. Fokin 与 CuAAC 平行独立、未获诺奖——可作对比页人物，关系类型用 competitor（并行独立发展），勿写"合作者"（其与 Sharpless 的合作是 Sharpless 侧叙事，本页无载） |
| Sharpless 对手方名 | 规范名 **Karl Barry Sharpless**（batch-01 已建档），勿写 "K. Barry Sharpless"（页面首段缩写形式）——yaml 用全名 |
| Bertozzi 对手方名 | 规范名 **Carolyn Bertozzi**（本批同批建档），页面诺奖句作 "Carolyn R. Bertozzi"——yaml 与 Beamer 用 "Carolyn Bertozzi" 防分裂 |
| Betamab | 2019 创办、**2021 年关闭**（closed）——如实写"关闭"，勿写"成功退出" |
| 荣誉年份 | Hirschmann/du Vigneaud/Bjerrums/Dannebrog/Ørsted 各奖年份页面均未列——引用时注明"年份页面未列" |
| 在世口径 | 1954-01-16 生，在世，卒日留白 |
| 引语红线 | 页面**全文无引语**——Beamer 全篇间接转述，结尾页标注"意译" |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q6914509 | ✅ |
| name_zh | 莫滕·梅尔达尔 | ✅ |
| name_en | Morten P. Meldal | ✅ |
| birth_date | 1954-01-16 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | Denmark | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分：organic chemistry / click chemistry / peptide chemistry / carbohydrate chemistry，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 共同得主 / 平行独立者**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Klaus Bock | 师→生（博士导师） | DTU，1983 年不饱和糖与卤化氢反应论文，碳水化合物合成化学 |
| co-honored | Carolyn Bertozzi | 无向 | 2022 诺贝尔化学奖共同得主（生物正交化学方向） |
| co-honored | Karl Barry Sharpless | 无向 | 2022 诺贝尔化学奖共同得主（点击化学概念） |
| competitor | Valery V. Fokin | 无向 | CuAAC 反应同时但独立发展（页面原句 concurrently with but independent of） |

> **不予入库**（页面无载）：家庭成员（页面完全无载）；MRC LMB / 嘉士伯实验室同事（无具名关系细节）；Betamab 联合创办人（未具名）。

## 8. 奖项清单

- **Nobel Prize in Chemistry（2022，与 Bertozzi、Sharpless 共享）**；年份以页面为准
- Ralph F. Hirschmann Award in Peptide Chemistry（年份页面未列）
- Vincent du Vigneaud Award（年份页面未列）
- Ellen et Niels Bjerrums Chemistry Prize（年份页面未列）
- Knight of the Order of the Dannebrog（丹尼布洛骑士勋章，年份页面未列）
- H. C. Ørsted Gold Medal（年份页面未列）
- Clarivate Citation Laureates（年份页面未列）

## 9. 机构清单

- 教育：Technical University of Denmark, DTU（BS、MS、PhD 1983）
- 任职：DTU（博后 1983–1988 前段；1996 助理教授）；MRC Laboratory of Molecular Biology, Cambridge（博后，1983–1988 中段）；University of Copenhagen（博后 1983–1988 末段；现任化学教授）；Carlsberg Laboratory（1998 至今，化学系合成组负责人）
- 创业：Betamab Therapeutics ApS（2019 共同创办，beta-body 概念；2021 年关闭）

## 10. 终审清单

- [ ] 生卒 1954-01-16 / 在世留白，出生地仅"丹麦"
- [ ] 2022 诺奖"三人共享"与 CuAAC 分工表述准确；官方理由原句
- [ ] CuAAC "同时但独立"表述准确，不排序不虚构师承
- [ ] Sharpless 用全名 Karl Barry Sharpless、Bertozzi 用 Carolyn Bertozzi（防分裂 stub）
- [ ] 页面无载项（童年/家庭/荣誉年份）如实标注"页面无载/年份未列"
- [ ] Betamab 2021 关闭如实呈现
- [ ] 全篇无直接引语，结尾页标注"意译"
- [ ] 封面装饰圆占位并注明肖像缺位
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Morten_P._Meldal/page.md`（49 行）建立事实基准，逐页对照 Beamer tex 全部事实——**凡超出该页内容的表述一律删除**
- [ ] 头像：装饰圆占位（肖像缺位注记）
- [ ] 国籍：封面顶部明示丹麦
- [ ] 引语核对：本篇页面无引语，全篇应为间接转述
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与本批其他篇目（Doudna/List/MacMillan/Bertozzi）格式对齐

---

> **名单状态**：由主控统一收尾（`chemist/generate_21th_century_list.py`）。
