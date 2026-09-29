# John B. Goodenough（约翰·古迪纳夫）立传提示词

> qid=Q906529 · 1922-07-25 – 2023-06-25（享年 100）· 美国 · 诺贝尔化学奖（2019，与 M. Stanley Whittingham、Akira Yoshino 共享）· 本地数据源：`chemist/presentations/21th_century/pages/John_B._Goodenough/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：对齐 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}` 高斯式骨架——表格语义化 tabularx + 公式展示框 + 时间线页 + 气泡背景。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像用本地 `images.txt` 中 2010 年照片或 2019 诺奖照；下载失败则装饰圆占位并在 Review 注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{battery-full}\enspace 锂离子电池正极之父\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒（1922-07-25 Jena / 2023-06-25 Austin）、本名（John Bannister Goodenough）、国籍（美国，生于德国）、教育（Yale BS / Chicago MS, PhD）、博士导师（Clarence Zener）、配偶（Irene Wiseman）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「晶格 — 离子」母题——离散圆点暗示锂离子在氧化物品格中的嵌入与脱出。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配金色边框浅金底公式展示框（`\fcolorbox` + minipage），如 $\mathrm{Li_xCoO_2}$ 正极反应式或 Goodenough–Kanamori 规则条目。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：John Bannister Goodenough（中文惯称：约翰·古迪纳夫；读音 /ˈɡʊdɪnʌf/）
- **生卒**：1922-07-25 生于德国耶拿（Jena, Thuringia，魏玛德国；父母为美国人）→ 2023-06-25 逝于得克萨斯州 Austin 的辅助生活机构，享年 100（距 101 岁生日差一个月）
- **国籍**：United States（美国）
- **身份**：材料科学家、固态物理学家、诺贝尔化学奖得主；1986 年起任得克萨斯大学奥斯汀分校材料科学、电气工程与机械工程教授
- **家庭**：学术世家——父 Erwin Ramsdell Goodenough（1893–1965，约翰出生时在牛津读研究生，后任耶鲁宗教史教授）；母 Helen Miriam (Lewis) Goodenough；兄 Ward 后为宾夕法尼亚大学人类学教授；父再婚后有两位同父异母弟妹：Ursula Goodenough（圣路易斯华盛顿大学生物学荣休教授）、Daniel Goodenough（哈佛医学院生物学荣休教授）。1951 年娶芝加哥大学加拿大籍历史学研究生 Irene Wiseman，无子女；Irene 2016 年去世
- **教育轨迹**：
  - 童年患阅读障碍（dyslexia），未被诊断；自学书写考入 Groton School 并获全额奖学金，1940 年以第一名毕业
  - Yale University：两年半修完课程，1944 年 *summa cum laude* 毕业（Skull and Bones 成员）；珍珠港事件后欲参军，数学教授劝其留校修完气象资格课程，后加入美国陆军航空队气象部门
  - University of Chicago：战后获物理学 MS 与 PhD（1952）
- **博士导师**：Clarence Zener（电击穿理论家）；在芝加哥期间亦与 Enrico Fermi、John A. Simpson 共同工作与学习
- **研究领域**：固态物理、磁学（超交换）、材料科学、锂离子电池正极、随机存取磁存储器

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **耶拿出生（1922）**：生于德国耶拿的美国学者家庭；童年阅读障碍未被诊断，被小学视为 "a backward student"，却自学考入 Groton 并以第一名毕业。
2. **战争与气象（1942–1945）**：珍珠港事件后欲参军，被劝留在耶鲁修完课程；战后进入芝加哥大学，师从 Clarence Zener 读物理。
3. **博士与磁性（1952）**：博士论文《A theory of the deviation from close packing in hexagonal metal crystals》（1952，Zener 指导）。
4. **MIT Lincoln Laboratory（24 年）**：任研究科学家与团队负责人，参与开发随机存取磁存储器（RAM）；研究磁学与过渡金属氧化物中的金属—绝缘体转变。
5. **Goodenough–Kanamori 规则**：与合作轨道序（cooperative Jahn–Teller 畸变）概念一道，与金森順次郎（Junjiro Kanamori）共同提出预测材料中磁超交换符号的半经验规则——超交换是高温超导的核心性质。
6. **两部名著**：专著《Magnetism and the Chemical Bond》（1963）与《Les oxydes des metaux de transition》（1973）；一生 550+ 论文、85 书章、5 本专著。
7. **转赴牛津（1970s 末–1980s 初）**：美国政府终止其研究经费后离开美国，出任牛津大学无机化学实验室主任。
8. **Li_xCoO_2 正极（1980）**：在 Whittingham 电池材料工作基础上，1980 年发现用 LixCoO2 作轻质高能量密度正极可使锂电池容量翻倍（与 Koichi Mizushima 等合作发表）。
9. **零专利费（1980s）**：牛津拒绝为其专利付费，转向英国 Harwell 原子能研究机构（AERE）——条款规定发明人 Goodenough 与 Mizushima 零版税；1990 年 AERE 将专利授权给 Sony 等厂商，估计获利超 1000 万英镑。
10. **聚阴离子正极（奥斯汀时期）**：1986 年起任 UT Austin 教授；与 Arumugam Manthiram 发现聚阴离子类正极（如磷酸铁锂，1997 磷橄榄石论文）——聚阴离子的诱导效应使电压高于氧化物。
11. **玻璃电池争议（2017）**：2017-02-28 团队在 Energy and Environmental Science 发表全固态玻璃电解质电池；遭电池学界广泛质疑（数据不全面、机理被认为违反热力学第一定律），后续工作后仍存争议——页面明载，须如实呈现两面。
12. **2019 诺贝尔化学奖**：与 M. Stanley Whittingham、Akira Yoshino 共享（表彰锂离子电池研究）；**97 岁获奖，成为史上最年长的诺贝尔奖得主**（页面明载 "He remains the oldest person ever to have been awarded the prize"）；2021-08-27 起至逝世为在世最年长得主。诺奖演讲《Designing Lithium-ion Battery Cathodes》（2019-12-08）。
13. **终身工作到 98 岁**：2021 年 98 岁仍在 UT Austin 工作，希望再寻电池技术突破；约翰·古迪纳夫奖（ACS 与 ECS 分别以其名设奖）；2023-06-25 于 Austin 去世。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深绯红 crimson） | `#7E1E23` | 氧化物与磁性研究的厚重（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（磁学与 RAM badgeMag） | `#16324F` | 藏青——超交换 / Goodenough–Kanamori / RAM |
| 分类色 2（锂电正极 badgeLi） | `#1B7A43` | 绿——LixCoO2 / LiFePO4 |
| 分类色 3（产业转化 badgeInd） | `#B26A00` | 琥珀——Harwell / Sony 授权 |
| 分类色 4（荣誉 badgeHonor） | `#5B2A86` | 紫——National Medal of Science / Copley / Nobel |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「锂离子在晶格中的嵌入位点」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**The Invisible Light** — Infraction（文件 `music_audio/inspiring-electronic/19-tGxXsgSKPiQ-...The Invisible Light.wav`，不要复制 wav）
- **风格**：纪录片式 / 宽厚 / 微光渐亮
- **匹配理由**：
  - "Invisible Light（不可见之光）"匹配其一生主题——看不见的离子与自旋，最终点亮了每个人的手机与电动车；
  - 纪录片式的宽厚铺底匹配 97 岁最年长得主的沧桑与从容；
  - 渐亮的推进匹配 "阅读障碍男孩 → 100 岁仍在实验室" 的一生弧线。
- **时长**：以曲目实际时长为准，ffmpeg `-shortest` 自动对齐 15 页 ≈ 105 秒。

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 锂离子电池正极之父 / John B. Goodenough 1922–2023 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/博士导师/配偶/领域/荣誉）
03  古迪纳夫的一生 — 高斯式时间线（10 节点：1922→1940→1944→1952→1976→1980→1986→2013→2019→2023）
04  阅读障碍与 Groton (1922–1944) — 表格「时间|事件|结果」（dyslexia 自学→Groton 第一名→Yale summa cum laude→陆军航空队气象）
05  芝加哥与磁学 (1946–1952) — 表格「导师|领域|结果」+ 公式框：Goodenough–Kanamori 超交换规则
06  MIT Lincoln Laboratory (1952–1976) — 表格「问题|方法|结果」（RAM / 金属—绝缘体转变 / 轨道序）
07  牛津与 LixCoO2 (1980) — 表格「问题|方法|结果」+ 公式框：LixCoO2 正极容量翻倍
08  零版税的专利 (1980s–1990) — 表格「机构|条款|结果」（牛津拒付→AERE Harwell 零版税→1990 授权 Sony £10M+）
09  奥斯汀与聚阴离子 (1986–) — 表格「合作|发现|意义」+ 公式框：聚阴离子诱导效应（Manthiram 合作）
10  玻璃电池的争议 (2017–) — 表格「主张|质疑|现状」（两面如实呈现）
11  荣誉与命名 — 高斯式「类别|代表|意义」表格（NAE 1976 / National Medal of Science / Draper 2014 / Copley 2019 / 两机构以其名设奖）
12  2019 诺贝尔化学奖 — 共享结构图解：Whittingham（TiS2 初代）× Goodenough（LixCoO2 正极）× Yoshino（石油焦阳极商用化）；97 岁最年长
13  遗产：一座移动的世界 — 四分类遗产盒 + 公式框：550+ 论文 / 5 部专著 / John B. Goodenough Award
14  结尾 — 「足够好的人生，直到 100 岁。」（Enough——呼应其姓氏的页面向尾句，仅作修辞不作引语）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 出生地与国籍 | **生于德国耶拿**（父母为美国人），国籍美国——勿写成"生于美国"；frontmatter nationality 仅 United States，无 Germany |
| 享年与最年长 | 2023-06-25 逝于 Austin，享年 100；**97 岁获奖、史上最年长得主**为页面两处明载（intro 与 Distinctions 节 "He remains the oldest person ever"）——可写但须注明口径 |
| 获奖年份结构 | 2019 与 Whittingham、Yoshino **三人共享**同一理由（表彰锂离子电池研究）；获奖理由英文原句 "for the development of lithium-ion batteries" 载于本批 Whittingham 本地页面——引用时注明口径来源；古迪纳夫本人页面无引文原句 |
| LixCoO2 论文 | 1980 年 Mater. Res. Bull. 论文作者序为 **Mizushima, Jones, Wiseman, Goodenough**——勿写古迪纳夫独作；发现地点牛津 |
| LiCoO2 发现年份口径 | 本页作 1980 年发表；Yoshino 页面称 LiCoO2 "discovered in 1979 by Godshall et al. at Stanford, and Goodenough and Mizushima at Oxford"——两页口径分别忠实，Beamer 取 "1980 论文发表" 口径，勿混写 "1979 论文" |
| 专利零版税 | 牛津**拒绝**为其申请专利；Harwell AERE 接受但条款**发明人零版税**（Goodenough 与 Mizushima）；AREE 授权获利 £10M+ 归 AERE——三方角色勿混 |
| 聚阴离子合作 | 聚阴离子类正极由 **Manthiram 与 Goodenough** 共同发现；磷酸铁锂 1997 论文作者 Padhi, Nanjundaswamy, Goodenough——勿写"古迪纳夫独发现" |
| 玻璃电池争议 | 页面明载学界质疑（数据不全、解释牵强、被指违反热力学第一定律）——须两面呈现，勿单方面写成"突破"；2020 年 LNEG/Porto/UT 专利仅页面一句 |
| 军旅口径 | 珍珠港事件后欲参军被劝留校；后加入**美国陆军航空队气象部门**——occupation 中的 meteorologist 即源于此；勿写"从军作战" |
| 家庭 | 配偶 Irene Wiseman（1951 结婚，2016 去世，无子女）；兄 Ward（人类学）；同父异母 Ursula/Daniel——parent-child 关系仅页面明载父母名（Erwin/Helen），**infobox Parents 可入库**；兄弟/弟妹无独立关系行必要（见 §7 禁入说明） |
| 引语红线 | 本地 page.md 无第一人称引语——全文不得出现引号内"原话"；"a backward student" 是页面转述小学评语，可作半角引号内的页面原文引用 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q906529 | ✅ |
| name_zh | 约翰·古迪纳夫 | ✅ |
| name_en | John B. Goodenough | ✅（页面标题规范名；清单 db_id 为空） |
| birth_date | 1922-07-25 | ✅ |
| death_date | 2023-06-25 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | physicist | ✅（页面 Fields: Physics；intro 口径 materials scientist / solid-state physicist 入 occupations） |
| field_of_work | solid-state physics（person_field 细分：solid-state physics / materials science / lithium-ion battery / magnetism，带 rank） | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**★红线：只收 page.md 正文或 infobox 明载的关系；metadata-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Clarence Zener | 师→生（博士导师） | 1952 芝加哥大学物理博士 |
| advisor-student | Laura H. Lewis | 生→师（学生） | infobox Doctoral students |
| advisor-student | Arumugam Manthiram | 生→师（博士后） | infobox 其他知名学生（postdoc）；合作发现聚阴离子类正极 |
| advisor-student | Bill David | 生→师（博士后） | infobox 其他知名学生（postdoc） |
| spouse | Irene Wiseman | 无向 | 1951 结婚，2016 去世，无子女 |
| colleague | Koichi Mizushima | 无向 | 1980 LixCoO2 正极论文共同作者、专利共同发明人（零版税条款） |
| colleague | Junjiro Kanamori | 无向 | Goodenough–Kanamori 超交换规则共同提出 |
| colleague | Enrico Fermi | 无向 | 芝加哥大学期间共同工作与学习的物理学家 |
| colleague | John A. Simpson | 无向 | 芝加哥大学期间共同工作与学习的物理学家 |
| co-honored | M. Stanley Whittingham | 无向 | 2019 诺贝尔化学奖共同得主；2015 年同列 Clarivate Citation Laureates |
| co-honored | Akira Yoshino | 无向 | 2019 诺贝尔化学奖共同得主 |

> 兄弟 Ward、同父异母弟妹 Ursula/Daniel、父亲 Erwin/母亲 Helen：页面仅作家庭背景叙述，**不建 parent-child/sibling 行**（避免家族表噪声；Erwin/Helen 若入库仅可经 frontmatter 对应，正文无独立关系叙述——**禁入库**）。Fermi 行沿用库内规范记录 Enrico Fermi（id 1081）。美国能源部长 Steven Chu（2009 Fermi Award 颁奖人）、Obama（2013 National Medal 颁奖人）、Siegfried Hecker（Fermi Award 共同获奖冶金学家）均为颁奖场合人物——**禁入库**。

## 8. 奖项清单

- Japan Prize（2001，轻质高能量密度可充锂电池关键材料）
- Enrico Fermi Award（2009，与冶金学家 Siegfried Hecker 同获）
- National Medal of Science（2011 授奖 infobox 口径 / 2013 由 Obama 颁发——正文两处年份口径并存，Beamer 取 "2013 颁发" 并可注 infobox 2011）
- IEEE Medal for Environmental and Safety Technologies（2012）
- Charles Stark Draper Prize（2014）
- Welch Award in Chemistry（2017）；C.K. Prahalad Award（2017）
- Copley Medal（2019）
- Nobel Prize in Chemistry（2019，与 Whittingham/Yoshino 共享）
- NAE 成员（1976）；NAS 及法国、西班牙、印度对应科学院成员；Foreign Member of the Royal Society（2010）
- Von Hippel Award、Centenary Prize、Olin Palladium Award、Washington Award、Benjamin Franklin Medal、Clarivate Citation Laureates（2015，与 Whittingham 同列）等 frontmatter/正文互证奖项

## 9. 机构清单

- 教育：Groton School（全额奖学金，1940 第一名毕业）；Yale University（BS 1944，summa cum laude，Skull and Bones）；University of Chicago（MS、PhD 1952）
- 任职：MIT Lincoln Laboratory（研究科学家兼团队负责人，24 年）；University of Oxford 无机化学实验室主任（1970s 末–1980s 初）；University of Texas at Austin（1986–2023，Cockrell School of Engineering，Virginia H. Cockrell Centennial Chair）
- 顾问：Enevate 技术顾问委员会（2010）；JCESR 顾问（Argonne 牵头）；Battery500 顾问（2016，PNNL 牵头）

## 10. 终审清单

- [x] 生卒 1922-07-25 Jena / 2023-06-25 Austin，享年 100；国籍美国
- [x] 97 岁获奖 = 史上最年长得主（页面明载两处）；2021-08-27 起在世最年长
- [x] 2019 三人共享；获奖理由英文原句注明取自 Whittingham 页面口径
- [x] LixCoO2 1980 论文作者序（Mizushima/Jones/Wiseman/Goodenough）；牛津拒专利→Harwell 零版税→Sony 授权 £10M+
- [x] 聚阴离子正极记 Manthiram 合作；1997 磷橄榄石论文作者序正确
- [x] 玻璃电池争议两面呈现；National Medal of Science 年份双口径已标注
- [x] 博士生/博士后入库口径与 infobox 一致；Fermi/Simpson 用 colleague 类型
- [x] 引语红线：全文无杜撰第一人称原话
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/John_B._Goodenough/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：优先本地 `images.txt` 中 2010 年照片（2009 Fermi Award 由 Steven Chu 颁发照亦可，图注须写明场合）
- [ ] 国籍：封面顶部明示美国（生于德国耶拿须在身份页注明）
- [ ] 引语核对：全文不得出现无法溯源的引号原话
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；化学式一律数学模式
- [ ] 与 Sanger 及 21 世纪批次既有格式对齐；与 Whittingham/Yoshino 两篇的共享页口径互查
