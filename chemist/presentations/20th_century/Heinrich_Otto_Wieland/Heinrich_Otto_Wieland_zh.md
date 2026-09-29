# Heinrich Otto Wieland（海因里希·奥托·维兰德）立传提示词

> qid=Q76610 · 1877-06-04 – 1957-08-05 · 德国化学家 · 20 世纪 · 诺贝尔化学奖（1927，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Heinrich_Otto_Wieland/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。★ 本人物 images.txt **为空、无任何图片**——封面与身份页用**装饰圆占位**（主色实心圆 + 缩写 HW）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 胆汁酸的解谜者\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：左侧装饰圆 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育、博士导师、博士学生、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡呼应「分子骨架」母题——稠环在暗色中渐显。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：tabularx 三列表格 + 金色边框浅金底公式展示框，如「胆汁酸骨架 = 稠环甾体核 + 侧链」。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Heinrich Otto Wieland（中文惯称：海因里希·奥托·维兰德）
- **生卒**：1877-06-04 生于 Pforzheim, Baden, German Empire → 1957-08-05 逝于 Starnberg, Bavaria, West Germany，享年 80
- **国籍**：Germany（德国；一生历经德意志帝国→魏玛→纳粹→西德四朝）
- **身份**：化学家、大学教师
- **家庭**：父 Theodor Wieland（1846–1928）——持有化学博士学位的药剂师，在 Pforzheim 经营金银精炼厂；堂亲 Helene Boehringer——Boehringer Ingelheim 创始人 Albert Boehringer 之妻；女儿 Eva Wieland 于 1937-05-14 嫁 Feodor Lynen（后为诺奖得主，**页面未载其获奖**）
- **教育轨迹**：Ludwig-Maximilians-Universität München——**1901 博士（师从 Johannes Thiele）、1904 habilitation**
- **博士导师**：Johannes Thiele
- **博士学生**：Rolf Huisgen、Leopold Horner（infobox 明载）；Hans Conrad Leipelt（正文明载"a student of Wieland"）
- **研究领域**：chemistry——胆汁酸（bile acids）、有机化学、毒素（蟾蜍毒/鹅膏毒肽）、生物碱
- **任职轨迹**：TU Munich（1913–1921）→ University of Freiburg（1921–1925）→ LMU München（1925–，接替 Willstätter）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **药剂师之子（1877）**：生于"金匠之城"Pforzheim，父亲是化学博士药剂师，经营金银精炼厂——化学是他家的家业。
2. **慕尼黑师门（1901/1904）**：1901 年在 Johannes Thiele 门下获 LMU 博士，1904 完成 habilitation。
3. **产业咨询（1907–）**：自 1907 年起任 Boehringer Ingelheim 顾问——学术与制药产业的早期联姻（另一口径见 §5）。
4. **慕尼黑工大教授（1913–1921）**：1914 年任特殊专题有机化学副教授，兼慕尼黑国立实验室有机分部主任。
5. **战时服役与毒气研究（1917–1918）**：在 Fritz Haber 领导的 KWI 物理化学与电化学研究所（Dahlem）以研究服替代兵役——参与芥子气新合成路线等武器研究；亦以 Adamsite（亚当氏毒剂）首次合成闻名。
6. **弗莱堡时期（1921–1925）**：接替 Ludwig Gattermann（并接管其著名实验手册）；开启蟾蜍毒与胆汁酸研究；与 Boehringer Ingelheim 合作合成吗啡、士的宁类生物碱。
7. **接掌慕尼黑（1925）**：接替 Richard Willstätter 出任 LMU 化学教授。
8. **1927 诺贝尔化学奖**：表彰其胆汁酸研究；诺奖演讲 1928-12-12《The Chemistry of the Bile Acids》。
9. **α-鹅膏蕈碱（1941）**：分离出世界上最毒蘑菇之一毒鹅膏（Amanita phalloides）的主要活性成分 alpha-amanitin。
10. **以他命名的反应与方法**：Barbier–Wieland 降解、Wieland–Gumlich 醛、Wieland 重排、Wieland 试验（蘑菇毒素鉴定的 Meixner 试验相关）。
11. **黑暗中的守护者**：纽伦堡法案后保护"种族劣等"（racially burdened）学生——被开除者可留在他组里当化学家或"Geheimrats 的客人们"（guests of the privy councillor）；《卫报》2015 年称其"defied the Nazis"。
12. **学生之死**：学生 Hans Conrad Leipelt 因给 Kurt Huber 遗孀 Clara Huber 募捐而被判处死刑——白玫瑰运动阴影下的师门悲剧。
13. **Heinrich Wieland Prize 与身后**：1964 年起每年颁发（脂质研究起步，今表彰生物活性分子研究；2000–2010 由 Boehringer Ingelheim 赞助，2011 起由其基金会颁发，2014 起奖金 10 万欧元）；1957-08-05 逝于 Starnberg，享年 80。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深松绿 deep pine） | `#175E54` | 分子骨架的墨绿与实验室玻璃的冷光（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（胆汁酸 badgeBile） | `#2F5D50` | 墨绿胆汁酸 / 甾体骨架 |
| 分类色 2（毒理学 badgeToxin） | `#7A1E28` | 暗红毒鹅膏 / 蟾蜍毒 |
| 分类色 3（战争与黑暗 badgeWar） | `#4A4A4A` | 铁灰 Dahlem 岁月 / 纳粹时期守护 |
| 分类色 4（产业与传承 badgeLegacy） | `#B8860B` | 暗金 Boehringer / Wieland Prize |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆 + 稠环轮廓线），呼应「甾体四环骨架」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Cinematic Experience** — Alex-Productions（`music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav`；不要复制 wav 文件，Makefile 引用路径即可）
- **风格**：史诗 / 复杂 / 纪录片
- **匹配理由**：
  - "史诗" 匹配其一生的多面性——从胆汁酸到毒气研究、从诺奖到纳粹时期的黑暗守护，是强戏剧张力的世纪人生
  - "复杂" 匹配其争议底色——武器研究的光暗两面、学生之死的悲剧重量，需要电影感的承载
  - "纪录片" 匹配传记叙事——Pforzheim → 慕尼黑 → 弗莱堡 → 慕尼黑 → 1927 诺奖 → 1941 α-鹅膏蕈碱 → Wieland Prize
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 胆汁酸的解谜者 / Heinrich Otto Wieland 1877–1957 + 四色 badge + 右上装饰圆 + 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右 2×2 信息网格（生卒/国籍/教育/博士导师/博士学生/出生地/去世地/领域/荣誉）
03  维兰德的一生 — Sanger 式时间线（10 节点：1877→1901→1904→1913→1917→1921→1925→1927→1941→1957）
04  药剂师之家 (1877–1901) — 表格「人物|身份|意义」（父 Theodor / 金银精炼厂）
05  慕尼黑师门 (1901–1913) — 表格「年份|事件|结果」（Thiele 博士 → habilitation → TU Munich）
06  Dahlem 岁月 (1917–1918) — 表格「背景|工作|结果」（Haber/KWI、芥子气路线、Adamsite 首合成——客观呈现）
07  弗莱堡与接掌慕尼黑 (1921–1925) — 表格「阶段|事件|结果」（Gattermann 继任 / 蟾蜍毒·胆汁酸 / 接替 Willstätter）
08  1927 诺贝尔化学奖 — 公式框：诺奖演讲 The Chemistry of the Bile Acids (1928-12-12)
09  胆汁酸研究 — 表格「问题|方法|结果」+ 公式框：胆汁酸甾体骨架
10  毒理学：从蟾蜍毒到 α-鹅膏蕈碱 — 表格「对象|发现|意义」+ 公式框：alpha-amanitin (1941)
11  以他命名的化学 — 「名称|类型|意义」表格（Barbier–Wieland 降解 / Wieland–Gumlich 醛 / Wieland 重排 / Wieland 试验）
12  黑暗中的守护者 (1933–1945) — 表格「事件|人物|结果」（Nuremberg Laws 下的学生们 / Leipelt 之死）
13  荣誉与 Wieland Prize — 「类别|代表|意义」表格（ForMemRS 1931 / Pour le Mérite 1952 / Otto Hahn Prize 1955 / 1964 起年度奖）
14  结尾 — 「解开胆汁之秘，守护黑暗中的学生。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| Boehringer 年份张力 | Career 节作 "starting in 1907 was a consultant"（顾问），Family 节作 "worked for the company from 1915 to 1920 and established the company's scientific department"——**两口径并存**，页面如实注记（参照 Nygaard/Dahl von Neumann Medal 双口径先例），勿擅自统一 |
| 毒气研究 | Dahlem 时期参与**芥子气合成路线**等武器研究 + **首次合成 Adamsite**——page.md 明载，如实写、不回避也不渲染；其与 Windaus（同批 1928 得主，拒绝毒气研究）对照时各自忠实本页 |
| 女婿 Lynen | 页面仅载 Eva Wieland 于 1937-05-14 嫁 Feodor Felix Konrad Lynen——**勿加 Lynen 诺奖信息**（页面无载禁写） |
| 接任关系 | 1925 接替 Richard Willstätter（慕尼黑）、1921 接替 Ludwig Gattermann（弗莱堡）——是教席继任，勿写成"师承" |
| Leipelt | "a student of Wieland" 明载——入库方向 Wieland→学生；其为 Kurt Huber 遗孀募捐被判死刑——客观陈述，勿加"白玫瑰成员"等页面未载定性 |
| 堂亲线 | Helene Boehringer 是堂亲（cousin）+ Albert Boehringer 是其夫——无对应关系类型，禁入库 |
| 国籍口径 | 一生历经 German Empire → Weimar Republic → Nazi Germany → West Germany——入库用 Germany，正文可注四朝 |
| 获奖理由口径 | page.md 原文 "for his research into the bile acids"——勿泛化成"固醇研究"（那是 Windaus） |
| Goethe Medal | 1942 年（纳粹时期奖项）——如实注记年份与历史语境 |
| 肖像 | images.txt 为空——装饰圆占位，禁编造图注 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76610 | ✅ |
| name_zh | 海因里希·奥托·维兰德 | ✅ |
| name_en | Heinrich Otto Wieland | ✅ |
| birth_date | 1877-06-04 | ✅ |
| death_date | 1957-08-05 | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | biochemistry / organic chemistry（person_field 细分见下表） | ✅ |
| has_biography | 0（待立传后置 1） | ✅ |

**person_field 细分（rank 表）**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | bile acids | 胆汁酸 |
| 1 | organic chemistry | 有机化学 |
| 2 | toxins | 毒素（蟾蜍毒/鹅膏毒肽） |
| 3 | alkaloids | 生物碱 |

## 7. 社会关系入库清单

**★ 红线**：只收 page.md 正文或 infobox 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Johannes Thiele | 师→生（博士导师） | 1901 LMU 博士 |
| advisor-student | Rolf Huisgen | 师→生 | infobox Doctoral students 明载 |
| advisor-student | Leopold Horner | 师→生 | infobox Doctoral students 明载 |
| advisor-student | Hans Conrad Leipelt | 师→生 | 正文明载"a student of Wieland"；因给 Kurt Huber 遗孀募捐被判死刑 |
| colleague | Fritz Haber | 无向 | 1917-18 在其领导的 KWI Dahlem 以研究服替代兵役（沿用库内规范名） |
| colleague | Richard Willstätter | 无向 | 1925 接替其 LMU 化学教授教席 |
| parent-child | Theodor Wieland | 父→子 | 父亲，化学博士药剂师、Pforzheim 金银精炼厂主（1846–1928） |
| other | Feodor Felix Konrad Lynen | 无向 | 女婿，1937-05-14 娶其女 Eva Wieland（页面未载 Lynen 获奖，禁写） |

**禁入库名单（无对应关系类型 / 仅事件性提及）**：

> Helene Boehringer（堂亲）与 Albert Boehringer（其夫、Boehringer Ingelheim 创始人）、Ludwig Gattermann（教席前任）、Elisabeth Dane（仅 See also 一行"Wieland's assistant from 1929"，无正文语境）、Kurt Huber 与 Clara Huber（Leipelt 事件人物）、女儿 Eva Wieland（人物主记录，仅经由 Lynen 关系提及）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1927，独享；诺奖演讲 1928-12-12 The Chemistry of the Bile Acids）
- Foreign Member of the Royal Society，ForMemRS（1931）
- Goethe Medal for Art and Science（1942）
- Pour le Mérite for Sciences and Arts（1952）
- Otto Hahn Prize for Chemistry and Physics（1955）
- Theodor Frerichs Prize（年份页面无载）
- Commander's Cross of the Order of Merit of the Federal Republic of Germany（年份页面无载）
- Silliman Memorial Lectures（frontmatter 载名）
- Heinrich Wieland Prize（1964 起以其名设立；2014 起奖金 10 万欧元）

## 9. 机构清单

- 教育：Ludwig-Maximilians-Universität München（1901 博士、1904 habilitation）
- 任职：Technical University of Munich（1913–1921 教授）、University of Freiburg（1921–1925，Gattermann 继任者）、Ludwig-Maximilians-Universität München（1925– 化学教授，Willstätter 继任者）、KWI Physical Chemistry and Electrochemistry, Dahlem（1917–1918 战时服役）、Organic Division of the State Laboratory, Munich（1914– 主任）
- 产业：Boehringer Ingelheim（1907 起顾问 / 1915–1920 建立其科学部——双口径见 §5）

## 10. 终审清单

- [ ] 生卒 1877-06-04 / 1957-08-05，享年 80，出生地 Pforzheim、去世地 Starnberg
- [ ] 获奖理由忠实 page.md（bile acids）；与 Windaus 甾醇口径区分
- [ ] Boehringer 双口径（1907 顾问 / 1915-1920 建科学部）如实注记
- [ ] Dahlem 武器研究与 Adamsite 首合成客观呈现；与 Windaus 拒绝毒气对照时各自忠实本页
- [ ] Leipelt 关系与悲剧客观陈述；无页面未载定性
- [ ] Thiele/Huisgen/Horner/Leipelt/Haber/Willstätter/父亲/Lynen 八条关系均有 page.md 出处
- [ ] 全篇无编造引语（"defied the Nazis" 为 Guardian 转述句，引用须注明出处）；引号内不出现 page.md 无法溯源的"原话"
- [ ] 封面/身份页装饰圆占位；封面国籍行明示德国
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Heinrich_Otto_Wieland/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **肖像**：确认为装饰圆占位（本地无图）
- [ ] **国籍**：封面顶部明示德国
- [ ] **引语核对**：全篇无直接引语（Guardian 句除外且须注明出处）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger / van 't Hoff 等）对齐
