# Alan MacDiarmid（艾伦·G·麦克迪尔米德）立传提示词

> qid=Q110942 · 1927-04-14 生于新西兰马斯特顿 – 2007-02-07 卒于美国宾州 Drexel Hill · 新西兰/美国化学家 · 20 世纪 · 诺贝尔化学奖（2000，与 Alan J. Heeger、Hideki Shirakawa 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Alan_MacDiarmid/`（page.md + metadata.json + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次立传的核心版式语言。

---

## 0. 正文形式说明（参考桑格立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 images.txt 仅有**建筑照**（VUW Alan MacDiarmid building），无人像——优先用 Wikipedia REST API `page/summary` 查 infobox 原图（页面注明 "Alan MacDiarmid in Beijing, China, 2005"，存在真实人像）下载；仍失败则用**装饰圆占位**（主色渐变 + 姓名首字母），并在 §10 勾选项如实标注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{bolt}\enspace 合成金属的推销员\enspace·\enspace 新西兰 \to 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名 Alan Graham MacDiarmid、国籍（新西兰 → 美国公民，infobox Citizenship: American）、出生地 Masterton、去世地 Drexel Hill、教育（VUW / Wisconsin / Cambridge 双博士）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「掺杂/合成金属」母题。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如聚乙炔 (CH)x 掺杂导电化与聚苯胺质子酸掺杂（emeraldine → metallic regime，1978/1986 论文实载）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Alan Graham MacDiarmid，ONZ FRS（中文惯称：艾伦·G·麦克迪尔米德）
- **生卒**：1927-04-14 生于新西兰 Masterton → 2007-02-07 逝于美国宾夕法尼亚州 Drexel Hill（家中跌落楼梯去世，享年 79；去世前患骨髓增生异常综合征 myelodysplastic syndrome）；葬于 Drexel Hill 的 Arlington Cemetery
- **国籍**：新西兰出身、美国公民（infobox Citizenship: American；page 口径 "New Zealand-American chemist"）
- **身份**：化学家（2000 年诺贝尔化学奖三位得主之一）
- **家庭**：五子妹之一（三兄两妹——页面原文 "three brothers and two sisters"，排行未明载勿写"第几子"）；家贫、大萧条中随家迁往 Lower Hutt；十岁左右从父亲一本旧教科书自学入化学之门。第一任妻子 Marian Mathieu（1954 年结婚，1990 年去世），育有四子女（Heather McConnell、Dawn Hazelett、Duncan MacDiarmid、Gail Williams）与九个孙辈；第二任妻子 Gayl Gentile（2005 年结婚）。堂兄 Douglas MacDiarmid 为旅外新西兰画家（诺奖次年为其绘肖像，藏新西兰肖像画廊）
- **教育轨迹**：
  - Hutt Valley High School
  - Victoria University of Wellington：1943 过大学入学考试与医学预科考试；读书期间做兼职 "lab boy"（实验室杂务）；BSc 1947；此后任本科生实验 demonstrator；完成 MSc 后任化学系助理——1949 年在 *Nature* 发表首篇论文；1951 年一等荣誉毕业
  - University of Wisconsin–Madison（Fulbright 奖学金）：无机化学方向，M.S. 1952、PhD 1953
  - Sidney Sussex College, Cambridge（Shell 研究生奖学金）：第二个 PhD 1955，论文 *The chemistry of some new derivatives of the silyl radical*
- **导师**：页面与 infobox **均未载博士导师姓名**——勿编造
- **研究领域**：导电聚合物、硅化学（宾大前二十年主线）、聚苯胺、合成金属

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **大萧条中的少年（1927–1943）**：Masterton 贫困家庭、举家迁 Lower Hutt；约十岁从父亲的旧教科书自学化学——图书馆与旧书是第一位导师。
2. **"lab boy" 勤工俭学（1943–1951）**：VUW 读书期间做实验室杂务与 demonstrator；1949 年以助理身份在 *Nature* 发表首篇论文；1951 一等荣誉毕业并获 Fulbright 奖学金。
3. **双博士学位（1952–1955）**：Wisconsin 无机化学 M.S./PhD（1952/1953）→ Cambridge Sidney Sussex College 第二个 PhD（1955，硅基自由基衍生物化学）——硅化学伏笔在此埋下。
4. **圣安德鲁斯一年 → 宾大四十五年**：苏格兰 St Andrews 初级教职一年后加入宾夕法尼亚大学化学系，1964 年升正教授，前后四十五年。
5. **硅化学二十年**：在宾大前二十年的研究聚焦硅化学；1988 年任 Blanchard Professor of Chemistry。
6. **白川的银色薄膜（1975）**：白川英树在东京工业大学制出有金属光泽的聚乙炔；MacDiarmid 1975 年访问东工大时注意到这一结果——合作的起点（页面明载此因果在 Heeger/白川两侧一致）。
7. **1976-1977 宾大合作**：邀请白川以博士后身份来宾大实验室；与物理学家 Alan Heeger 一起把聚乙炔的导电性做上去——1977 年首次发表成果。
8. **2000 诺贝尔化学奖**：三人共享；诺奖表彰"发现经某些改性后塑料可以导电"，并由此发展出重要应用（页面明载的应用面：感光胶片抗静电剂、可调光的智能窗、发光二极管、太阳能电池、手机显示屏，以及指向分子电子学的未来）。
9. **聚苯胺王国**：1978 JACS 高导电聚乙炔衍生物论文（Chiang/Heeger/MacDiarmid/Park/Shirakawa 等）之后，1986 年起聚苯胺质子酸掺杂系列论文（emeraldine → metallic regime）成为其标签性成果——"synthetic metals"（合成金属）概念（其诺奖演讲即以此为题）。
10. **论文与专利**：600 余篇论文、20 项专利；晚年仍亲授新生研讨课（2001），环球演讲倡导 21 世纪创新的全球化。
11. **祖国的最高礼遇**：2000 年获新西兰皇家学会最高荣誉 Rutherford Medal；2002 年新年荣誉获封 Order of New Zealand（新西兰最高荣誉）；2003 当选 FRS。
12. **中国情缘**：2004 年获中国政府"友谊奖"（外国专家最高荣誉）；吉林大学 2001 年起设有 Alan G. MacDiarmid 研究所；2005 年在北京留影。
13. **身后纪念（2007– ）**：UT Dallas 的 Alan G. MacDiarmid NanoTech Institute 于 2007 年以其命名；VUW 的 Alan MacDiarmid 楼落成、遗孀捐赠其诺贝尔奖章展出；Lower Hutt 的 MacDiarmid Place（2013）——从 "lab boy" 到以名字命名楼与研究所的闭环。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（午夜蓝 midnightblue） | `#16324F` | 合成金属的深邃金属光泽（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（导电聚合物 badgePoly） | `#2E7D5B` | 绿掺杂聚乙炔 (CH)x |
| 分类色 2（聚苯胺 badgeAniline） | `#8C6A1F` | 金聚苯胺 emeraldine 质子酸掺杂 |
| 分类色 3（硅化学 badgeSilicon） | `#4A6B8A` | 蓝灰宾大前二十年主线 |
| 分类色 4（应用与产业 badgeApp） | `#9E4A3A` | 赭抗静电/智能窗/LED/太阳能 |
| 背景 | `#F7F6F9` | 浅灰白（与桑格版一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「掺杂」——少量掺入即点亮全局。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Last Hope** — Victor Cooper（源文件 `music_audio/inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav`；不要复制 wav 文件，Makefile 中引用路径即可）
- **风格**： dramatic / powerful / epic，带希望感的推进
- **匹配理由**：
  - "Last Hope" 的希望感匹配大萧条穷孩子借旧书自学、终至诺贝尔的一生弧线
  - "dramatic powerful" 匹配塑料导电这一颠覆教科书认知的发现的冲击力
  - 史诗感匹配其 600 篇论文 + 20 项专利 + 环球布道的产业推手形象
- **时长**：以实际曲目时长为准，> 15 页 × 7 秒即可由 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 合成金属的推销员 / Alan G. MacDiarmid 1927–2007 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/去世地/教育双博士/领域/荣誉）
03  麦克迪尔米德的一生 — 高斯式时间线（10 节点：1927→1943→1951→1953→1955→1964→1977→1988→2000→2007）
04  早年：大萧条与旧教科书 (1927–1943) — 表格「时间|事件|结果」
05  "lab boy" 到一等荣誉 (1943–1951) — 表格「时间|事件|结果」（含 1949 Nature 首篇论文）
06  双博士：Wisconsin 与 Cambridge (1951–1955) — 表格「阶段|方向|结果」+ 公式框：硅基自由基衍生物
07  宾大四十五年 (1955–2000) — 表格「阶段|方向|结果」（硅化学二十年 → Blanchard 讲席 1988 → UT Dallas 2002）
08  聚乙炔导电 (1975–1977) — 表格「问题|方法|结果」+ 公式框：(CH)x 碘掺杂导电化
09  2000 诺贝尔化学奖 — 表格「得主|领域|理由」（三人共享标注醒目）+ citation 英文原句
10  聚苯胺与合成金属 (1978– ) — 表格「对象|机制|意义」+ 公式框：emeraldine 质子酸掺杂
11  应用图谱 — 高斯式「材料|应用|前景」表格（抗静电/智能窗/LED/太阳能/分子电子学）
12  门生与合作网络 — 表格「人物|方向|结果」（Shirakawa 博士后 1976 / Heeger 长期合作）
13  荣誉与身后纪念 — 高斯式「类别|代表|意义」表格（Rutherford 2000 / ONZ 2002 / FRS 2003 / 友谊奖 2004 / 命名机构）
14  结尾 — 从 Masterton 的旧教科书到导电塑料点亮的世界 + 品牌 OpenMathAI
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖口径 | 2000 化学奖为**三人共享**；理由英文以本地页面口径（诺奖表彰"plastics can, after certain modifications, be made electrically conductive"的发现）；勿写"独享" |
| 姓名规范 | 全名 Alan Graham MacDiarmid；数据库 name_en 统一用 **Alan G. MacDiarmid**（与 Heeger/白川两侧对手方名一致，防分裂）；勿与核物理学家 Ernest MacDiarmid 等同名混淆（页面无此混淆，仅防笔误） |
| 博士导师 | 页面与 infobox **均未载**两位 PhD 的导师姓名——身份信息页与数据库均禁写导师 |
| 双 PhD 年份 | Wisconsin：M.S. 1952、PhD 1953；Cambridge：第二个 PhD 1955——勿合并成"1955 年获双博士" |
| 建筑落成年份 | 页面自相矛盾两处：Legacy 图注 "The Alan MacDiarmid building in 2026" 及正文 "opened in May 2010"，而正文另句 "In 2011 the Alan MacDiarmid building ... was opened"——**写 2011 落成（后句为叙述主体）或回避精确年份**，勿两处并存 |
| 妻子年份 | 第一任 Marian Mathieu 1954 结婚、1990 去世；第二任 Gayl Gentile 2005 结婚、2014 去世——勿写错配对关系 |
| 兄妹数目 | 页面原文 "one of five children – three brothers and two sisters"——只写"五子妹之一"，**勿推断排行** |
| 生计叙事 | "lab boy" or janitor 为页面原文——中文写"实验室杂务/勤杂工"皆可，但勿夸化为"清洁工起家的励志故事"之外的无载细节 |
| 同性/裸体主义者段落 | 页面 Personal life 有 naturist/nudist、sun-worshipper、waterskier 一句——**边缘轶事，Beamer 全篇略过** |
| 政治敏感 | 无政治内容；2005 年北京留影、2004 友谊奖、吉林大学研究所仅作客观事实陈述，不加评价 |
| 引语红线 | 页面正文**无直接引语**（诺奖演讲标题 «Synthetic Metals": A Novel Role for Organic Polymers» 只作标题引用）——中文引号内不得出现任何"原话"，一律间接转述 |
| 门生/导师 | 页面未载任何博士生与导师名单——Slide 12 只写白川 1976 博士后来访合作与 Heeger 合作，勿列"学生清单" |
| 应用边界 | 应用清单以页面实载为限（抗静电、智能窗、LED、太阳能电池、手机显示、分子电子学展望）——勿加电池/传感器等页面未列的展开（其 DOE 报告虽有电池标题，若引用须注明出处年份） |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q110942 | ✅ |
| name_zh | 艾伦·G·麦克迪尔米德 | ✅ |
| name_en | Alan G. MacDiarmid | ✅（本批新建记录；三人侧对手方名统一用此形式） |
| birth_date | 1927-04-14 | ✅ |
| death_date | 2007-02-07 | ✅ |
| nationality | New Zealand（rank 0）+ United States（rank 1） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分见下表，带 rank） | ✅ |

**person_field 细分（rank 表）**：

| name_en | rank | name_zh | 依据 |
|---|---|---|---|
| conductive polymers | 0 | 导电聚合物 | 诺奖理由核心 |
| silicon chemistry | 1 | 硅化学 | 宾大前二十年研究主线（页面明载） |
| polyaniline | 2 | 聚苯胺 | 1986 起系列论文与其标签性成果 |
| synthetic metals | 3 | 合成金属 | 其诺奖演讲主题概念 |

## 7. 社会关系入库清单（★ 红线：只收 page.md 正文或 infobox 明载者）

**共同得主 / 合作 / 博士后**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Alan J. Heeger | 无向 | 2000 诺贝尔化学奖共同得主 |
| co-honored | Hideki Shirakawa | 无向 | 2000 诺贝尔化学奖共同得主 |
| colleague | Alan J. Heeger | 无向 | 宾大长期合作，掺杂聚乙炔系列论文共同作者 |
| advisor-student | Hideki Shirakawa | MacDiarmid → 学生 | 1976 年白川以博士后身份受邀进入其宾大实验室 |
| spouse | Marian Mathieu | 无向 | 第一任妻子，1954 年结婚，1990 年去世 |
| spouse | Gayl Gentile | 无向 | 第二任妻子，2005 年结婚 |

**禁入库名单（metadata-only 或页面明载但按本批惯例不入库）**：
- 堂兄 Douglas MacDiarmid（画家，页面明载但为家族关系，按本批化学家惯例仅收学术关系）
- 四名子女与九名孙辈（页面明载姓名，同上不入库）
- Chiang C.K. 等仅出现在论文作者列表中的合作者（页面无关系叙述，不入库）
- metadata employer 中的 University of Wisconsin–Madison（教育经历而非人物关系）

## 8. 奖项清单

- Nobel Prize in Chemistry（2000，与 Heeger / Shirakawa 三人共享）
- Rutherford Medal（2000，新西兰皇家学会最高荣誉）
- Order of New Zealand，ONZ（2002 新年荣誉，新西兰最高荣誉）
- Fellow of the Royal Society，FRS（2003）；Honorary Fellow of the Royal Society Te Apārangi
- 美国国家科学院院士（2002）
- Friendship Award（2004，中国政府外国专家最高荣誉）
- The Francis J. Clamer Medal（1993，Franklin Institute）；William H. Nichols Medal（2002）
- American Chemical Society Award in Materials Chemistry（1999）；Chemical Pioneer Award；Oesper Award；Centenary Prize；John Scott Award
- Victoria University of Wellington 荣誉博士（1999）

## 9. 机构清单

- 教育：Hutt Valley High School → Victoria University of Wellington（BSc 1947、MSc、一等荣誉 1951）→ University of Wisconsin–Madison（M.S. 1952、PhD 1953）→ Sidney Sussex College, University of Cambridge（PhD 1955）
- 任职：University of St Andrews（初级教职一年）→ University of Pennsylvania（1964 正教授，四十五年，1988 Blanchard Professor of Chemistry）→ University of Texas at Dallas（2002 加入）
- 命名机构：Alan G. MacDiarmid NanoTech Institute（UT Dallas，2007 追命名）；Alan G. MacDiarmid Institute（吉林大学，2001 起）；MacDiarmid Institute for Advanced Materials and Nanotechnology（新西兰）；Alan MacDiarmid Chair in Physical Chemistry（VUW，2001）；Alan MacDiarmid Place（Lower Hutt，2013）

## 10. 终审清单

- [ ] 生卒 1927-04-14 / 2007-02-07，享年 79；去世原因（家中楼梯跌倒、生前患 MDS）与安葬地表述准确
- [ ] 2000 化学奖三人共享表述准确；citation 用本地页面英文口径
- [ ] 双 PhD 年份（1952/1953 Wisconsin；1955 Cambridge）与"页面未载导师"红线守住
- [ ] 白川 1976 博士后来宾大、1975 东工大注意到银色薄膜的因果链准确
- [ ] 建筑落成年份处理一致（2011 或回避精确年份，勿两说并存）
- [ ] 两任妻子配对与年份准确；子女仅一句带过或不出现在 Beamer
- [ ] 全篇无杜撰引语（页面无直接引语）；naturist 段落已略过
- [ ] 肖像：REST API 成功则用 2005 北京照，否则装饰圆占位并在本清单如实勾选
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Alan_MacDiarmid/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：真实照片或装饰圆占位，图注与来源一致（北京 2005）
- [ ] 国籍：封面顶部明示新西兰 → 美国
- [ ] 引语核对：全篇应无中文引号内的"原话"；诺奖演讲标题引用格式正确
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与桑格模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Frederick_Sanger_zh.tex）对齐

---

> **名单状态**：chem-batch-25（2000 三人组之一）；`chemist/generate_20th_century_list.py` 由主控统一收尾，本文件不负责改总表。
