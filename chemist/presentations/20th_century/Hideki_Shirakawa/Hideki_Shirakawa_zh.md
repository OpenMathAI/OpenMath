# Hideki Shirakawa（白川英树）立传提示词

> qid=Q110916 · 1936-08-20 生于日本东京（在世） · 日本化学家 · 20 世纪 · 诺贝尔化学奖（2000，与 Alan J. Heeger、Alan G. MacDiarmid 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Hideki_Shirakawa/`（page.md + metadata.json + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次立传的核心版式语言。

---

## 0. 正文形式说明（参考桑格立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 images.txt 仅有两张**合影**（与森喜朗 2000-10-18 首相官邸；与明仁天皇 2000-11-03 授勋）——**合影不作主肖像**；优先用 Wikipedia REST API `page/summary` 查 infobox 原图（页面注明 "Hideki Shirakawa in 2001"，存在个人照）下载；仍失败则用**装饰圆占位**（主色渐变 + 姓名汉字「白川」），并在 §10 勾选项如实标注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{bolt}\enspace 银色薄膜的发现者\enspace·\enspace 日本`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名白川英樹（Shirakawa Hideki）、国籍、出生地东京、童年轨迹（满洲/台湾/高山市）、教育（东京工业大学本科 1961/博士 1966）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「薄膜/掺杂」母题——大片银色薄膜上零星掺入的碘。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 1977 年碘蒸气掺杂聚乙炔 (CH)x 的导电化（JCS Chem. Commun. 论文实载，作者 Shirakawa/Louis/MacDiarmid/Chiang/Heeger）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Hideki Shirakawa（白川 英樹，Shirakawa Hideki；中文惯称：白川英树）
- **生卒**：1936-08-20 生于日本东京（在世，页面无卒日）
- **国籍**：Japan（日本）
- **身份**：化学家、工程师；筑波大学与浙江大学名誉教授（Professor Emeritus，页面导语明载双校）
- **家庭**：军医的次子；有一兄、一弟一妹（页面原文 "He had one elder and one younger brother and sister"）；童年随家在满洲（Manchukuo）与台湾度过；约小学三年级时迁居母亲的故乡岐阜县高山市。奥运马拉松金牌得主高桥尚子为其远房亲眷（second cousin-niece，正文明载）；早安少女组成员吉泽瞳亦为亲眷（ Relatives 节明载）
- **教育轨迹**：
  - Tokyo Institute of Technology（东京工业大学，页面注现 Institute of Science Tokyo）：1961 年获化学工程学士学位；1966 年获博士学位
  - 毕业后任东工大资源化学研究所（Chemical Resources Laboratory）助手
- **导师**：metadata.json 载 doctoral_advisor "Shū Kanbara"——**page.md 正文与 infobox 均无载，不入库、Beamer 不写**（页面无载禁写）
- **博士**：1966（东京工业大学，页面未载论文题目与导师）
- **研究领域**：导电聚合物——聚乙炔薄膜合成、化学掺杂金属导电性、螺旋聚乙炔、共轭液晶聚合物

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **军医之子与漂泊童年（1936–1940s）**：生于东京、随军医父亲在满洲与台湾度过童年、约三年级迁回母亲故乡岐阜高山市——跨国界的少年时代。
2. **东工大chem engineer（1961）**：化学工程本科毕业，随即进入资源化学研究所任助手——从"造材料"的工程视角进入化学。
3. **银色聚乙炔（1966–1975）**：博士毕业留任助手期间，制出有**金属外观**的聚乙炔——一次意外般的产品日后改写教科书（页面只述 "developed polyacetylene, which has a metallic appearance"，勿添"偶然合成"等无载细节）。
4. **MacDiarmid 到访（1975）**：MacDiarmid 访问东工大时对这一结果产生兴趣——跨国合作的起点。
5. **宾大博士后（1976）**：受邀以博士后研究员身份进入 MacDiarmid 在宾夕法尼亚大学的实验室；与物理学家 Alan Heeger 一起发展聚乙炔的电导率。
6. **碘掺杂突破（1977）**：发现碘蒸气掺杂可大幅提升聚乙炔电导率；1977 年 JCS Chem. Commun. 论文（Shirakawa/Louis/MacDiarmid/Chiang/Heeger 五作者）；导电机制 believed 与孤子（solitons）非线性激发有关（页面原文口径）。
7. **筑波教授（1979–1997）**：1979 年任筑波大学助教授，三年后升正教授；1991 年任大学院理工学研究科长（至 1993-03）与第 3 类群组长（至 1997-03）。
8. **2000 诺贝尔化学奖**：与 Heeger、MacDiarmid 共享，理由 "for the discovery and development of conductive polymers"——**日本第二位**化学诺奖得主、首位非"国立七大学"出身的日本诺奖得主（页面 Recognition 节明载两个"第一/第二"口径，此为可用的排位表述）。
9. **文化勋章（2000-11-03）**：明仁天皇于皇居授予 Order of Culture，并选为 Person of Cultural Merit——与诺贝尔奖同年双喜。
10. **四大研究方向（Research 节）**：①聚乙炔薄膜合成（解决不溶难加工问题，阐明分子与凝固结构）；②微量卤素掺杂产生金属导电性（掺杂剂与 π 电子部分电子转移）；③以液晶为溶剂的乙炔聚合（可控手性的螺旋聚乙炔薄膜）；④侧链接液晶基团的共轭液晶聚合物（电/磁场取向，电学各向异性）。
11. **对媒体过热的低调**：多年表示不希望诺奖受到媒体（尤其日本媒体）过多特殊对待，希望诺奖类别之外的领域也被广泛知晓——谦逊底色。
12. **日本学士院（2001）**：当选日本学士院会员；获日本化学会特别奖（2001）；高分子学会 1983 年奖与 2000 年 SPSJ 杰出成就奖。
13. **浙江大学名誉教授（2006）**：与中国的学术纽带；另，2013 年与物理诺奖得主益川敏英就特定秘密保护法发表共同声明（公共议题——**Beamer 建议略过**，见 §5）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（墨青深蓝 deepteal） | `#0E4D64` | 聚乙炔薄膜的金属光泽与实验室的沉静（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 文化勋章（公式框边线、字段标签） |
| 分类色 1（聚乙炔合成 badgePA） | `#2E7D5B` | 绿银色薄膜 / 薄膜合成 |
| 分类色 2（掺杂导电 badgeDope） | `#B4632C` | 琥珀碘掺杂 / 金属导电性 |
| 分类色 3（螺旋手性 badgeHelix） | `#3E5C94` | 蓝液晶溶剂聚合 / 螺旋聚乙炔 |
| 分类色 4（共轭液晶聚合物 badgeLCP） | `#8E4A6E` | 紫侧链液晶 / 电学各向异性 |
| 背景 | `#F7F6F9` | 浅灰白（与桑格版一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「薄膜上的掺杂位点」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Empire Collapse** — Cold Cinema（源文件 `music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav`；不要复制 wav 文件，Makefile 中引用路径即可）
- **风格**： cinematic / dramatic / drone 长音铺垫，沉郁后展开
- **匹配理由**：
  - "drone 长音" 匹配共轭 π 链的延展意象——长链聚合物如持续低音般铺开
  - "沉郁后展开" 匹配助手时代的沉潜 → 1977 碘掺杂一鸣惊人 → 2000 文化勋章的叙事弧
  - 曲名虽含 "Empire Collapse"，立传叙事不取其字面，仅取其 cinematic 张力（注意在 Beamer 中只写曲名，勿做曲名与内容的过度解读）
- **时长**：以实际曲目时长为准，> 15 页 × 7 秒即可由 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 银色薄膜的发现者 / Hideki Shirakawa 1936– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/童年轨迹/教育/领域/荣誉）
03  白川英树的一生 — 高斯式时间线（10 节点：1936→1961→1966→1975→1976→1977→1979→1983→2000→2006）
04  早年：军医之子与漂泊童年 (1936–1950s) — 表格「时间|事件|结果」
05  东工大：从学生到助手 (1961–1975) — 表格「阶段|方向|结果」+ 公式框：金属外观的聚乙炔 (CH)x
06  宾大合作 (1975–1977) — 表格「问题|方法|结果」（MacDiarmid 到访 → 博士后 → Heeger 三人合作）
07  碘掺杂突破 (1977) — 表格「问题|方法|结果」+ 公式框：I2 掺杂 (CH)x 导电化 + soliton 机制（页面口径）
08  2000 诺贝尔化学奖 — 表格「得主|领域|理由」（三人共享标注醒目）+ citation 英文原句 + 「首位非七大出身」
09  文化勋章 (2000) — 表格「日期|事件|意义」（明仁天皇授勋 2000-11-03 + Person of Cultural Merit）
10  四大研究方向 — 高斯式「方向|内容|意义」表格（薄膜合成/掺杂导电/螺旋手性/液晶聚合物）
11  筑波岁月 (1979–1997) — 表格「年份|职务|结果」（助教授→正教授→大学院科长）
12  荣誉清单 — 高斯式「类别|代表|意义」表格（SPSJ 1983/2000、文化勋章、学士院 2001、浙大名誉教授 2006）
13  低调与立场 — 页面实载的媒体过热之谦逊态度（一句话）+ 遗产四盒
14  结尾 — 银色薄膜点亮导电聚合物时代 + 品牌 OpenMathAI
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖口径 | 2000 化学奖为**三人共享**（Heeger、Alan G. MacDiarmid、白川英树）；理由英文以本地页面口径 "for the discovery and development of conductive polymers"；勿写"独享"或"聚合物电子学之父"类无载头衔 |
| 排位表述 | 可用且仅可用页面明载的两个口径：**第二位**日本化学诺奖得主、**首位**非国立七大学出身的日本诺奖得主；"第一/唯一"类断言除此之外一律禁用 |
| 博士导师 | metadata.json 载 "Shū Kanbara"，但 page.md 正文与 infobox **均无载**——数据库不入库，Beamer 身份信息页师承栏留白或写"页面无载" |
| 同名区分 | 白川英树（Shirakawa Hideki）勿与其他 Shirakawa 混淆；共同得主英文写法统一：Alan J. Heeger / **Alan G. MacDiarmid** / Hideki Shirakawa |
| 童年表述 | 满洲（Manchukuo）与台湾为页面原文，客观陈述历史地名即可；勿展开时代背景评价 |
| 亲眷八卦 | 高桥尚子（second cousin-niece）与吉泽瞳（Morning Musume）为页面 Relatives 节实载——最多一句带过或略过；勿渲染 |
| 合影照片 | 与森喜朗、明仁天皇的两张合影**不作主肖像**（他人在画面中心地位敏感）；若用作插图须写明合影性质与日期 |
| 1977 论文口径 | 页面注 3 载 1977 年 JCS Chem. Commun. 论文五作者（Shirakawa, Hideki; Louis, Edwin J.; MacDiarmid, Alan G.; Chiang, Chwan K.; Heeger, Alan J.）——作者顺序照录，勿改 |
| soliton 机制 | 页面原文为 "it is strongly believed that ... solitons play a role"——写成"普遍认为与孤子非线性激发有关"，**勿写成定论** |
| 特定秘密保护法声明（2013） | 与益川敏英的共同声明属政治性公共议题——**Beamer 全篇略过**（本条为敏感点提示，不作叙事内容） |
| 引语红线 | 页面正文无个人中文可引"原话"；媒体态度一段仅可间接转述（不希望诺奖受媒体过多特殊对待）——中文引号内不得出现杜撰引语 |
| 媒体态度出处 | 该态度出自 Japan Times 2016 报道（页面引注 11）——转述即可，勿标注具体日期页码（本地页面未载于正文） |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q110916 | ✅ |
| name_zh | 白川英树 | ✅ |
| name_en | Hideki Shirakawa | ✅（本批新建记录，任务指定此形式） |
| birth_date | 1936-08-20 | ✅（在世，death_date 留空） |
| nationality | Japan | ✅ |
| primary_occupation | chemist | ✅（occupations 另含 engineer） |
| field_of_work | chemistry（person_field 细分见下表，带 rank） | ✅ |

**person_field 细分（rank 表）**：

| name_en | rank | name_zh | 依据 |
|---|---|---|---|
| conductive polymers | 0 | 导电聚合物 | 诺奖理由核心 |
| polyacetylene | 1 | 聚乙炔 | 银色薄膜合成与结构阐明 |
| helical polymers | 2 | 螺旋聚合物 | 可控手性螺旋聚乙炔（Research 节实载） |
| liquid crystalline polymers | 3 | 液晶聚合物 | 共轭液晶聚合物与电学各向异性 |

## 7. 社会关系入库清单（★ 红线：只收 page.md 正文或 infobox 明载者）

**博士后东家 / 共同得主 / 合作**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Alan G. MacDiarmid | MacDiarmid → 白川（博士后东家） | 1976 年以博士后研究员身份受邀进入其宾夕法尼亚大学实验室 |
| colleague | Alan J. Heeger | 无向 | 宾大合作发展聚乙炔电导率，1977 年碘掺杂突破 |
| co-honored | Alan G. MacDiarmid | 无向 | 2000 诺贝尔化学奖共同得主 |
| co-honored | Alan J. Heeger | 无向 | 2000 诺贝尔化学奖共同得主 |

**禁入库名单（metadata-only，页面正文/infobox 无载）**：
- Shū Kanbara（metadata doctoral_advisor，页面无载——红线示例）
- Yoshirō Mori（合影同框，非学术关系）
- Emperor Akihito（授勋仪式同框，授受关系非人物关系）
- Naoko Takahashi / Hitomi Yoshizawa（远房亲眷，家族关系不入库）
- Toshihide Maskawa（2013 共同声明人，一次性公共事件，非稳定学术关系）

## 8. 奖项清单

- Nobel Prize in Chemistry（2000，与 Heeger / MacDiarmid 三人共享）
- Order of Culture 文化勋章（2000，明仁天皇皇居授勋）+ Person of Cultural Merit 文化功劳者（2000）
- The Award of the Society of Polymer Science, Japan（1983）
- SPSJ Award for Outstanding Achievement in Polymer Science and Technology（2000）
- Professor Emeritus of the University of Tsukuba（2000）
- Special Award of the Chemical Society of Japan（2001）
- Member of the Japan Academy 日本学士院会员（2001）
- Professor Emeritus of the Zhejiang University 浙江大学名誉教授（2006）

## 9. 机构清单

- 教育：Tokyo Institute of Technology（1961 学士·化学工程；1966 博士）
- 任职：Tokyo Institute of Technology 资源化学研究所助手（1966–）→ University of Pennsylvania 博士后（1976–，MacDiarmid 实验室）→ University of Tsukuba（1979 助教授，约 1982 正教授；1991–1993 大学院理工学研究科长；至 1997-03 第 3 类群组长）
- 名誉教职：University of Tsukuba（2000）、Zhejiang University（2006）

## 10. 终审清单

- [ ] 生卒：1936-08-20 生于东京；**在世**（全篇无卒日、无享年表述）
- [ ] 2000 化学奖三人共享表述准确；citation 用本地页面英文原句
- [ ] 「第二位日本化学诺奖得主」「首位非七大出身」两个排位表述准确且未越界
- [ ] 博士导师栏不出现 Shū Kanbara（页面无载红线守住）
- [ ] 1977 论文五作者顺序照录；soliton 机制为"普遍认为"而非定论
- [ ] 合影不作主肖像；媒体态度段为间接转述、无杜撰引语
- [ ] 特定秘密保护法声明已略过；亲眷八卦最多一句
- [ ] 肖像：REST API 成功则用 2001 个人照，否则装饰圆占位并在本清单如实勾选
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Hideki_Shirakawa/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：真实照片或装饰圆占位，图注与来源一致
- [ ] 国籍：封面顶部明示日本
- [ ] 引语核对：全篇无中文引号内的"原话"；媒体态度为间接转述
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与桑格模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Frederick_Sanger_zh.tex）对齐

---

> **名单状态**：chem-batch-25（2000 三人组之一）；`chemist/generate_20th_century_list.py` 由主控统一收尾，本文件不负责改总表。
