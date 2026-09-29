# William Howard Stein（威廉·霍华德·斯坦）立传提示词

> qid=Q156492 · 1911-06-25 – 1980-02-02 · 美国生物化学家 · 诺贝尔化学奖（1972，与 Anfinsen、Moore 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/William_Howard_Stein/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 公式展示框。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像按 `images.txt` 就位；若无真实肖像则装饰圆占位并如实标注）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 核糖核酸酶的读谱人\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育（Harvard/Columbia）、博士（导师/论文）、师承（Bergmann）、家庭、核心领域、机构、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「层析柱洗脱 / 氨基酸逐一析出」母题。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如「离子交换层析：2 周 → 5 天」。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：William Howard Stein（中文惯称：威廉·霍华德·斯坦）
- **生卒**：1911-06-25 生于纽约市（犹太家庭）→ 1980-02-02 逝于纽约市，享年 68
- **国籍**：United States（美国）
- **身份**：生物化学家（biochemist；1972 诺贝尔化学奖共同得主）
- **家庭**：父 Fred M. Stein 为商人，早退休投身纽约本地健康公益；母 Beatrice Borg Stein 为儿童权益活动家、创办课后活动——父母的公益热忱滋养其生命科学志趣。1936 年读博期间娶 Phoebe Hockstader（1913–1989），三子：William H. Stein, Jr.、David F. Stein、Robert J. Stein；全家长住纽约州（曼哈顿为主，短期居 Scarsdale）
- **教育轨迹**：
  - Lincoln School（哥伦比亚大学师范学院创办的"进步主义"学校；田野考察与科学项目启蒙）
  - 16 岁转入新英格兰 Phillips Exeter Academy 备考大学
  - 1929 入 Harvard University 化学本科；哈佛研究生一年后，1934 转入哥伦比亚大学内外科医师学院（College of Physicians and Surgeons）生物化学系
- **导师**：Hans Thacher Clarke（哥伦比亚生物化学系主任，彼时正广揽后来成为 20 世纪早期杰出生物化学家的研究生）
- **博士**：1937 完成弹性蛋白（elastin）氨基酸组成论文（infobox 论文年份标 1938——口径见 §5），《The Composition of Elastin》
- **师承/博士后环境**：经 Max Bergmann（1934 年因纳粹威胁从德国流亡美国、在洛克菲勒研究所实验室工作的德裔犹太生物化学家）介绍获知钾三草酸铬酸铵与硫氰酸铵两种沉淀剂，分别分离甘氨酸与脯氨酸；博士毕业后入 Bergmann 门下工作
- **研究领域**：生物化学——核糖核酸酶序列、氨基酸层析、蛋白质结构与催化活性

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **纽约犹太家庭（1911）**：商人父亲与儿童权益活动家母亲的公益家风——生命科学志趣的源头。
2. **进步主义学校（1920s）**：Lincoln School 的田野与项目式学习；16 岁入 Phillips Exeter。
3. **哈佛→哥大转折（1929–1934）**：哈佛化学本科 + 一年研究生，1934 转入哥伦比亚 P&S 生物化学系——从化学走向生命。
4. **Clarke 的天才班（1934–1937）**：系主任 Hans Thacher Clarke 广揽英才；斯坦以钾三草酸铬酸盐与硫氰酸铵沉淀剂分别分离甘氨酸、脯氨酸，完成弹性蛋白氨基酸组成论文。
5. **Bergmann 门下（1937–1944）**：博士毕业后入洛克菲勒研究所 Bergmann 实验室；1939 Stanford Moore 加入，两人建立"持续一生的合作体系"（Moore 原话，见 §5 引语口径）。
6. **战时分离与接棒（1942–1944）**：二战中 Stein 留在 Bergmann 身边研究糜烂性毒剂对人体的分子效应；Bergmann 1944 年去世后，所长 Herbert S. Gasser 让两人接续氨基酸研究。
7. **淀粉柱层析定量**：土豆淀粉固定相柱层析 + 新研自动收集器 + 茚三酮显色定量——氨基酸定量分析的方法学起点。
8. **离子交换层析提速（2 周 → 5 天）**：引入离子交换层析，把单蛋白分析从约两周缩至 5 天；再与 Daryl Spackman 合作进一步压缩——催生第一台自动氨基酸分析仪。
9. **分析仪的副产品**：自动氨基酸分析仪还用于 Stein 对人体尿液与血浆氨基酸的研究。
10. **RNase 全序列（1950s 初–1960）**：1950 年代初启动牛胰核糖核酸酶整分子结构测定，1960 年完成全部序列——结合晶体 X 射线分析确定活性部位。
11. **1972 诺贝尔化学奖**：与 Moore、Christian Boehmer Anfinsen 共享，理由 "for their contribution to the understanding of the connection between chemical structure and catalytic activity of the ribonuclease molecule."；诺奖演讲 1972-12-11《The Chemical Structures of Pancreatic Ribonuclease and Deoxyribonuclease》。
12. **轮椅上的坚守（1969–1980）**：1969 年哥本哈根研讨会期间发热数日后突发瘫痪，诊为 Guillain–Barré 综合征；此后四肢瘫痪，但同事称其精神与幽默感未减，仍以导师身份指引洛克菲勒后辈的 RNase 研究。
13. **终章（1980）**：68 岁猝发心力衰竭，1980-02-02 逝于纽约市——诺奖后仅七年余；与妻子周游世界、在家中接待各国科学家的"沙龙"人生收束。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（紫罗兰紫 violet） | `#5B2A86` | 弹性蛋白与序列的深邃紫——生物化学的沉静（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（层析方法 badgeChrom） | `#1E4E79` | 蓝淀粉柱 / 离子交换 |
| 分类色 2（自动分析仪 badgeAuto） | `#1B7A43` | 绿分析仪 / Spackman |
| 分类色 3（RNase 序列 badgeRNase） | `#D97B29` | 琥珀 1960 全序列 / 活性部位 |
| 分类色 4（生命意志 badgeWill） | `#A63A2B` | 砖红 Guillain–Barré / 轮椅坚守 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「洗脱峰 / 氨基酸逐一析出」的层析意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Ascension** — Cold Cinema（文件 `20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav`）
- **风格**：史诗 / 渐强上升 / 预告片式弦乐
- **匹配理由**：
  - "Ascension"（攀升）匹配从淀粉柱到自动分析仪再到 RNase 全序列的三级跳
  - 渐强结构匹配 1969 年后「轮椅上的坚守」——身体沉坠而精神上升的叙事张力
  - 预告片式弦乐匹配 1972 诺奖时刻与洛克菲勒学派的集体史诗
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 核糖核酸酶的读谱人 / William Howard Stein 1911–1980 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍/教育/博士/师承/家庭/领域/荣誉）
03  斯坦的一生 — Sanger 式时间线（10 节点：1911→1929→1934→1937→1939→1944→1958→1960→1969→1972/1980）
04  纽约少年：进步主义教育 (1911–1929) — 表格「时间|事件|结果」（Lincoln School / Exeter）
05  哈佛到哥大：Clarke 的天才班 (1929–1937) — 表格「阶段|导师|成果」+ 公式框：沉淀剂分离 Gly/Pro
06  Bergmann 门下与战时 (1937–1944) — 表格「人物|事件|结果」（Bergmann / Moore 1939 / 糜烂性毒剂研究）
07  淀粉柱与离子交换 — 表格「问题|方法|结果」+ 公式框：2 周 → 5 天
08  自动氨基酸分析仪 — 表格「协作|工程|影响」（Moore / Spackman / 尿液血浆应用）
09  RNase 全序列 (1950s–1960) — 表格「挑战|方法|结果」+ 公式框：ribonuclease 完整序列
10  结构与催化活性 — 表格「证据|方法|结论」（序列 + X 射线 → 活性部位）
11  1972 诺贝尔化学奖 — 三人共享（Anfinsen / Moore / Stein）+ 授奖理由英文原文框
12  轮椅上的坚守 (1969–1980) — Guillain–Barré 时间线表格 + 精神与幽默的传承
13  荣誉与学会 — Sanger 式「类别|代表|意义」表格（Richards Medal / NAS 1960 / DSc 等）
14  结尾 — 「序列即结构，结构即功能——读懂一个酶，就读懂了催化本身。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1972 诺奖口径 | 三人共享：Christian B. Anfinsen、Stanford Moore、William Howard Stein；授奖理由英文原句 "for their contribution to the understanding of the connection between chemical structure and catalytic activity of the ribonuclease molecule."——本页 page.md 未载份额比例，**勿编 1/2·1/4·1/4** |
| 博士年份双值 | infobox 论文年份 1938 vs 正文 "In 1937, Stein completed his thesis"——立传采用**正文 1937**并加注记（以正文叙事为准） |
| 姓名混淆 | 与同批 Stanford Moore 的导师 Karl Paul Link 勿混；Stein 导师是 **Hans Thacher Clarke**（正文作 Hans Thatcher Clarke 两处拼写并存，立传统一取 infobox 形式 Hans Thacher Clarke） |
| Anfinsen 规范名 | 正文两处分别作 Christian B. Anfinsen / Christian Boehmer Anfinsen——立传与入库统一取 **Christian B. Anfinsen**（metadata.json name 形式） |
| 引语红线 | 本页直接引语仅一条：Moore 回忆 "During the early years of our cooperation, Stein and I worked out a system of collaboration that lasted for a lifetime."（Stein 篇正文实载，属 Moore 语，引用须注明）——其余一律间接转述 |
| 1969 病情 | 哥本哈根研讨会发热数日后**突发瘫痪**，诊断 Guillain–Barré 综合征，此后四肢瘫痪（quadriplegic）——勿写成中风或渐冻症；1980-02-02 死因**心力衰竭**（unexpected heart failure），勿写并发症 |
| 1960 口径 | "They determined the entire sequence of ribonuclease by 1960"——Moore 篇正文作 1959 announced；两篇各忠于本人页面，Stein 篇写 by 1960，Moore 篇写 1959 宣布 |
| 战时研究 | Stein 战时研究**糜烂性毒剂（blister agents）对人体的分子尺度效应**——表述克制、勿渲染细节 |
| 同名区分 | William Howard Stein（1911–1980，生物化学家）≠ Karl Paul Link 的学生 Moore ≠ 数值分析家 J. H. Wilkinson；本批另有 Geoffrey Wilkinson——立传中勿混淆 |
| 家庭 | 妻 Phoebe Hockstader（1936 结婚，卒 1989）、三子名字实载可写——除此之外无载家庭成员禁止扩写 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q156492 | ✅ |
| name_zh | 威廉·霍华德·斯坦 | ✅ |
| name_en | William Howard Stein | ✅ |
| birth_date | 1911-06-25 | ✅ |
| death_date | 1980-02-02 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分见下表，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | biochemistry | 生物化学 |
| 1 | chromatography | 色谱法 |
| 2 | protein sequencing | 蛋白质测序 |
| 3 | ribonuclease | 核糖核酸酶 |

## 7. 社会关系入库清单

**红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hans Thacher Clarke | 师→生（direction=advisor） | 哥伦比亚大学生物化学博士导师（1934 入其系，1937 论文） |
| advisor-student | Max Bergmann | 师→生（direction=advisor） | 博士后加入其洛克菲勒研究所实验室；由其介绍沉淀剂方法 |
| colleague | Stanford Moore | 无向 | 1939 加入 Bergmann 实验室后终生合作；分析仪与 RNase 序列 |
| colleague | Daryl Spackman | 无向 | 自动氨基酸分析仪共同研制 |
| colleague | Herbert S. Gasser | 无向 | 洛克菲勒研究所所长，Bergmann 1944 去世后准予接续氨基酸研究 |
| spouse | Phoebe Hockstader | 无向 | 1936 结婚，三子 |
| co-honored | Christian B. Anfinsen | 无向 | 1972 诺贝尔化学奖共同得主 |
| co-honored | Stanford Moore | 无向 | 1972 诺贝尔化学奖共同得主 |

> 禁入库名单：无（正文与 infobox 之外，metadata.json 未提供额外可入库关系；奖学会成员资格不产生关系）。

## 8. 奖项清单

- American Chemical Society Award in Chromatography and Electrophoresis（1964，与 Stanford Moore）
- Richards Medal of the American Chemical Society（1972，与 Stanford Moore）
- Kaj Linderstrøm-Lang Award，Copenhagen（1972，与 Stanford Moore）
- Nobel Prize in Chemistry（1972，与 Moore、Anfinsen 共享）
- D.Sc. honoris causa，Columbia University（1973）
- D.Sc. honoris causa，Albert Einstein College of Medicine of Yeshiva University（1973）
- Award of Excellence Medal，Columbia University Graduate Faculty and Alumni Association（1973）
- National Academy of Sciences 院士（1960 当选）；American Academy of Arts and Sciences 院士（1960 当选）
- 学会会员：American Society of Biological Chemists、Biochemical Society of London、American Chemical Society、AAAS、Harvey Society of New York

## 9. 机构清单

- 教育：Lincoln School（哥大师范学院）、Phillips Exeter Academy（16 岁起）、Harvard University（1929 本科化学 + 一年研究生）、Columbia University College of Physicians and Surgeons 生物化学系（1934–1937，PhD）
- 任职：Rockefeller Institute（Bergmann 实验室起步，此后长期教授生涯；1965 后为 Rockefeller University）；访问教授：University of Chicago（1961）、Harvard University（1964）；讲学：Washington University in St. Louis、Haverford College

## 10. 终审清单

- [ ] 生卒 1911-06-25 / 1980-02-02，享年 68；生卒地均为纽约市
- [ ] 1972 三人共享表述准确；授奖理由英文原句与 Moore 篇一致
- [ ] 博士年份采用正文 1937 并注记 infobox 1938 双值
- [ ] 1969 Guillain–Barré / 1980 心力衰竭表述准确
- [ ] 唯一直接引语（Moore 语）注明出处页，其余无杜撰引号原话
- [ ] "first determination of the complete amino acid sequence of an enzyme" 表述不扩大为"第一个蛋白质"
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/William_Howard_Stein/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 `images.txt` 核对肖像；无真实肖像用装饰圆占位并如实标注
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：仅 Moore 合作感言一条可引，注明出处页
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批 Moore 篇互查：1972 共享口径、1959/1960 年份口径、引语归属两篇一致
