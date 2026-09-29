# Kurt Wüthrich（库尔特·维特里希）立传提示词

> qid=Q110957 · 1938-10-04 生于瑞士 Aarberg（在世，卒日留白） · 瑞士化学家/生物物理学家 · 21 世纪 · 诺贝尔化学奖（2002）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Kurt_Wüthrich/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金框公式展示框 + 时间线页，是本次 21 世纪批次的统一版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。肖像：页面有 "Wüthrich in 2022" 照片但 images.txt 未提取到 URL——执行时先经 Wikipedia REST API `/page/summary/Kurt_Wüthrich` 查 infobox 原图名下载（500px）；404 则用装饰圆占位，并在 Review-1 记录。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{vial}\enspace 溶液中看见蛋白质的人\enspace·\enspace 瑞士`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素（瑞士 | ETH Zürich / Scripps | 蛋白质 NMR 结构测定）。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地、教育（Bern/Basel）、博士导师、核心领域、主要任职（ETH/Scripps/ShanghaiTech）、荣誉。事实取自本地 page.md infobox，不得杜撰；页面无载卒日——在世身份页卒栏写「在世（1938– ）」。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「NMR 谱线 / 共振峰」母题——离散峰点暗示二维谱中的交叉峰。
5. **表格语义化 + 公式框**（★ 高斯/Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——NOE 距离约束、BPTI 共振归属即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Kurt Wüthrich（中文惯称：库尔特·维特里希；勿写「武特里希」）
- **生卒**：1938-10-04 生于瑞士伯尔尼州 Aarberg（在世，卒日页面无载——全篇卒处一律留白）
- **国籍**：Switzerland（瑞士）
- **身份**：化学家/生物物理学家（Swiss chemist/biophysicist），2002 诺贝尔化学奖得主
- **家庭**：页面无载婚姻、子女——**全篇不写家庭内容**
- **教育轨迹**：
  - University of Bern：本科修读化学、物理、数学
  - University of Basel：博士，1964 年授予，导师 Silvio Fallab；论文题目为铜化合物在自动氧化反应中的催化活性
- **职业轨迹**：巴塞尔短期博士后 → 1965–1967 UC Berkeley（Robert E. Connick，转入新发展的 NMR）→ 1967–1969 Bell Telephone Laboratories（Murray Hill，Robert G. Shulman）→ 1969 回瑞士加入 ETH Zürich，1980 升生物物理学教授 → 现同时维持 ETH Zürich、The Scripps Research Institute（La Jolla）、ShanghaiTech University iHuman Institute 三处实验室
- **研究领域**：核磁共振（NMR）波谱学——生物大分子（蛋白质）溶液三维结构测定、蛋白质 NMR、横向弛豫优化波谱 TROSY、ST2-PT

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **瑞士少年（1938）**：生于伯尔尼州小镇 Aarberg，先修化学/物理/数学——数理根基后来化为波谱学的语言。
2. **巴塞尔博士（1964）**：师从 Silvio Fallab，研究铜化合物催化自动氧化——从电子顺磁共振（EPR）起步。
3. **伯克利转轨（1965–1967）**：在 Robert E. Connick 处做博士后，接触新发展的 NMR，研究金属配合物水合——EPR 到 NMR 的关键一跃。
4. **贝尔实验室（1967–1969）**：与 Robert G. Shulman 共事，负责首批超导 NMR 谱仪之一，开始研究蛋白质的结构与动力学——此后终生沿此路线。
5. **ETH 岁月（1969– ）**：1969 回苏黎世加入 ETH，1980 升生物物理学教授——瑞士本土成长的世界级实验室。
6. **与 Ernst 的二维 NMR 合作**：回瑞士后与诺贝尔奖得主 Richard R. Ernst 合作发展首批二维 NMR 实验（2D NMR 的发明者是 Ernst，勿写 Wüthrich 发明二维 NMR）。
7. **NOE 测距**：确立核 Overhauser 效应（NOE）作为测量蛋白质内部原子间距离的便利手段——把波谱峰变成结构约束。
8. **完全共振归属**：据此完成牛胰蛋白酶抑制剂（BPTI）、胰高血糖素等的完全共振归属——溶液中蛋白质结构的基石。
9. **1991 双奖**：Louisa Gross Horwitz Prize 与瑞士 Marcel Benoist Prize 同年加冕。
10. **1990s 国际荣誉链**：Louis-Jeantet 医学奖（1993）、京都奖先进技术部门（1998）、Otto Warburg Medal（1999）。
11. **2002 诺贝尔化学奖（一半）**：官方理由 "for his development of nuclear magnetic resonance spectroscopy for determining the three-dimensional structure of biological macromolecules in solution"——溶液中测生物大分子三维结构的 NMR 方法学。
12. **全球三实验室**：ETH Zürich + Scripps（La Jolla）+ 上海科技大学 iHuman Institute；曾任 Edinburgh（1997–2000）、香港中文大学（荣誉教授）、延世大学客座。
13. **晚年与传承**：2010 美国科学与工程节 "Lunch with a Laureate"、World.Minds 基金会执行顾问委员会；三部专著（1976/1986/1995）；2018-04-02 获中国永久居留卡（定居上海）——一句客观带过。

## 3. 配色方案（高斯/Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深湖蓝 deepnavy） | `#14324F` | NMR 谱线的深与静（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（蛋白质 NMR badgeNMR） | `#2E5A9E` | 蓝共振归属 / BPTI |
| 分类色 2（溶液结构 badgeSol） | `#1B7A43` | 绿溶液三维结构 / NOE 测距 |
| 分类色 3（二维谱 badge2D） | `#D97B29` | 琥珀二维 NMR / 与 Ernst 合作 |
| 分类色 4（全球实验室 badgeGlob） | `#C0395B` | 玫瑰 ETH / Scripps / ShanghaiTech |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「NMR 交叉峰 / 共振谱线」的离散排布。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**SEA** — Alex-Productions（`music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav`，不要复制 wav 文件，Makefile 里直接引用该路径）
- **风格**：开阔 / 沉静 / 带海一般的纵深
- **匹配理由**：
  - "开阔纵深" 匹配 NMR 结构生物学——在无形的溶液里"看"见大分子，一如在深海上辨认洋流
  - "沉静" 匹配其气质——半个多世纪只做一条线：蛋白质 NMR
  - 瑞士湖光与伯尔尼州出身呼应 "SEA" 的水意象（Aarberg 临水之乡 → 溶液中的结构）
- **时长**：以实际 wav 为准，> 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 溶液中看见蛋白质的人 / Kurt Wüthrich 1938– + 四色 badge + 右上头像 + 国籍行（瑞士）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/任职/领域/荣誉）
03  维特里希的一生 — Sanger 式时间线（10 节点：1938→1964→1965→1967→1969→1980→1991→1998→2002→2018）
04  早年与教育：Aarberg→Bern→Basel (1938–1964) — 表格「时间|事件|结果」
05  贝尔实验室：从 EPR 到蛋白质 NMR (1965–1969) — 表格「阶段|环境|结果」
06  二维 NMR 与 NOE 测距 (1969–) — 表格「问题|方法|结果」+ 公式框：NOE 距离约束
07  溶液中的三维结构 — 表格「问题|方法|结果」+ 公式框：BPTI 完全共振归属
08  荣誉链 (1991–1999) — 高斯式「类别|代表|意义」表格（Horwitz/Benoist/Louis-Jeantet/京都/Otto Warburg）
09  2002 诺贝尔化学奖 — 金框 citation 原文页（NMR 方法学）+ 「一半」口径标注
10  全球三实验室 — 高斯 FFT 页式流程图（ETH Zürich → Scripps → ShanghaiTech iHuman）
11  NMR 结构生物学遗产 — 表格「著作|年份|意义」（1976/1986/1995 三部曲）
12  科学传播与公共事务 — 表格「场合|角色|结果」（Lunch with a Laureate / World.Minds / ForMemRS 2010 / Bijvoet 2008）
13  瑞士与东方 — 表格「机构|身份|年份」（Edinburgh/港中文/延世客座；2018 上海永居一句客观）
14  结尾 — 「在看不见的溶液里，为蛋白质画下第一张肖像。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2002 奖项口径 | 同年得主三人（Fenn、Tanaka 在另一批 chem21-batch-01）：本地页面仅载 Wüthrich 得**该奖的一半**（"half of the Nobel Prize in Chemistry"）——勿写「独享 2002 全奖」，也**不要**把 Fenn/Tanaka 的软解吸电离理由混入本篇 |
| 2002 获奖理由 | 官方措辞 "for his development of nuclear magnetic resonance spectroscopy for determining the three-dimensional structure of biological macromolecules in solution"——强调**测定溶液中生物大分子三维结构的 NMR 方法学**，勿泛化成「发明 NMR」 |
| 二维 NMR 归属 | 首批二维 NMR 实验是与 **Richard R. Ernst 合作**发展（2D NMR 发明者 Ernst，1991 诺奖）；Wüthrich 的独立贡献是**把 NOE 用于测蛋白质内距离**并建立溶液结构测定方法——勿写「Wüthrich 发明二维 NMR」 |
| 年份勿混 | Berkeley 1965–1967（两年，Connick）；Bell Labs 1967–1969（两年，Shulman）；1969 入 ETH；1980 升生物物理学教授——勿写「1969 任教授」 |
| 博士论文 | 巴塞尔 1964，导师 **Silvio Fallab**，论文是铜化合物催化自动氧化（EPR 起步）——勿写博士阶段就做蛋白质 NMR |
| 在世口径 | 1938-10-04 生，**在世**——身份页、时间线、结尾一律卒处留白写「在世」 |
| 家庭 | 页面**无载**婚姻与子女——全篇不写家庭，勿从 Wikidata 脑补 |
| 中国永久居留 | 2018-04-02 获中国永久居留卡（上海）——仅一句客观事实，不做延伸评价 |
| 上海科技大学 | 页面作 iHuman Institute of ShanghaiTech University——勿写成「全职回国」 |
| 引语红线 | 本地页面**无直接引语**——全篇不得出现带引号的「原话」，一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q110957 | ✅（复用库内 #3729 回填） |
| name_zh | 库尔特·维特里希 | ✅ |
| name_en | Kurt Wüthrich（库内既有形式） | ✅ |
| birth_date | 1938-10-04 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | Switzerland | ✅ |
| primary_occupation | biophysicist | ✅ |
| field_of_work | NMR spectroscopy（person_field 细分：NMR spectroscopy / structural biology / protein NMR / biophysics，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后由主控置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作者**（仅 page.md 正文或 infobox 明载者；metadata.json 无关系字段，无 metadata-only 禁入库项）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Silvio Fallab | 师→生（博士导师） | 巴塞尔大学博士导师，1964 获博士 |
| advisor-student | Robert E. Connick | 师→生（博士后导师） | 1965–1967 UC Berkeley 博士后，转入 NMR |
| colleague | Robert G. Shulman | 无向 | 1967–1969 贝尔实验室共事，负责首批超导 NMR 谱仪之一 |
| colleague | Richard R. Ernst | 无向 | 合作发展首批二维 NMR 实验；Ernst 为 1991 诺贝尔化学奖得主（库内 #3726，规范名 Richard R. Ernst） |

> **不建项说明**：2002 同年得主 John B. Fenn / Koichi Tanaka 属 chem21-batch-01——为避免跨批分裂 stub，本篇**不建** co-honored，由主控统筹；页面正文无其他明载人物关系。

## 8. 奖项清单

- Nobel Prize in Chemistry（2002，该奖的一半；理由为 NMR 方法学——口径见 §5）
- Marcel Benoist Prize（1991）
- Louisa Gross Horwitz Prize（1991）
- Louis-Jeantet Prize for Medicine（1993）
- Kyoto Prize（Advanced Technology，1998）
- Otto Warburg Medal（1999）
- Bijvoet Medal，Bijvoet Center for Biomolecular Research（2008）
- Foreign Member of the Royal Society，ForMemRS（2010）
- Endel Lippmaa Memorial Medal，爱沙尼亚科学院（2017）
- Fray International Sustainability Award，SIPS 2018（FLOGEN Star Outreach）
- EMBO Membership；Oesper Award（infobox 另载）

## 9. 机构清单

- 教育：University of Bern（化学/物理/数学）→ University of Basel（PhD 1964，导师 Silvio Fallab）
- 任职：UC Berkeley 博士后（1965–1967）→ Bell Telephone Laboratories, Murray Hill（1967–1969）→ ETH Zürich（1969–，1980 生物物理学教授）→ The Scripps Research Institute, La Jolla → ShanghaiTech University iHuman Institute
- 客座/荣誉：University of Edinburgh（1997–2000）、香港中文大学（荣誉教授）、Yonsei University

## 10. 终审清单

- [ ] 生卒 1938-10-04 / 在世留白，出生地 Aarberg（伯尔尼州）
- [ ] 2002 诺奖「一半」口径 + citation 原文逐字准确；未混入 Fenn/Tanaka 理由
- [ ] 二维 NMR 归 Ernst 合作；Wüthrich 贡献为 NOE 测距 + 溶液结构方法学
- [ ] Berkeley/Bell Labs 年份准确（各两年）；ETH 1980 升教授
- [ ] 全篇无编造引语、无编造家庭内容
- [ ] 2018 上海永居仅一句客观；三实验室表述准确
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Kurt_Wüthrich/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：REST API 查 infobox 原图下载（500px）；404 则装饰圆占位并记录
- [ ] **国籍**：封面顶部明示瑞士
- [ ] **引语核对**：本篇应无引号原话（页面无直接引语）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 21 世纪批次各篇格式对齐
