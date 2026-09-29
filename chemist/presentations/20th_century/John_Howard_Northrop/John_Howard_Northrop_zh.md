# John Howard Northrop（约翰·霍华德·诺思罗普）立传提示词

> qid=Q106399 · 1891-07-05 – 1987-05-27 · 美国生物化学家 · 20 世纪 · 诺贝尔化学奖（1946，与 Sumner/Stanley 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/John_Howard_Northrop/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景，是本次重写的核心版式语言。

---

## 0. 正文形式说明（参考化学家桑格立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像按 images.txt 装载；页面信息框本无肖像行，404 则装饰圆占位，图注如实标注）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{virus}\enspace 让酶与病毒现出原形的化学家\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育（Columbia BA 1912 / PhD 1915）、师承（metadata 口径注记）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「蛋白质结晶析出」母题——离散圆点暗示胃蛋白酶晶体在溶液中缓缓析出。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（对象 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如「胃蛋白酶提纯 → 结晶 → 蛋白质判据」「噬菌体 = 核蛋白」等具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：John Howard Northrop（中文惯称：约翰·霍华德·诺思罗普）
- **生卒**：1891-07-05 生于纽约州扬克斯（Yonkers）→ 1987-05-27 逝于亚利桑那州威肯伯格（Wickenburg），享年 95
- **国籍**：United States（美国）
- **身份**：生物化学家（biochemist；1946 年诺贝尔化学奖得主之一；酶、病毒蛋白质的分离与结晶研究先驱）
- **家庭**：父 John Isaiah Northrop 为哥伦比亚大学动物学讲师（Havemeyer 家族成员）——在诺思罗普出生前两周死于实验室爆炸；母 Alice Rich Northrop 为亨特学院植物学教师。1917 年娶 Louise Walker（1891–1975），育两子女：John（海洋学家）、Alice（嫁 1954 年诺贝尔生理学或医学奖得主 Frederick C. Robbins）。一家先住纽约州弗农山郊外，后迁马萨诸塞州 Cotuit（缩短其赴新泽西州普林斯顿实验室的通勤）
- **教育轨迹**：Yonkers High School → Columbia University（**1912 年 BA；1915 年化学 PhD**）
- **导师**：metadata 载 Jacques Loeb、Thomas Hunt Morgan——正文与 infobox **无载**（如实注记，不入库）
- **博士**：1915，哥伦比亚大学，化学
- **研究领域**：生物化学、酶学、病毒蛋白质（infobox Fields: Biochemistry）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **遗腹子（1891）**：动物学家父亲死于实验室爆炸，两周后他出生——由植物学家母亲抚养长大。
2. **哥伦比亚博士（1912–1915）**：BA（1912）与化学 PhD（1915）一路连读。
3. **一战与发酵（1914–1918）**：为美国化学战部队研究发酵法生产丙酮与乙醇——这段工作把他引向**酶**的研究。
4. **洛克菲勒研究所（1916–1961）**：入职洛克菲勒医学研究所，一待 45 年直到退休——一生只换过一次东家。
5. **胃蛋白酶结晶（1929）**：分离并结晶胃蛋白酶（pepsin），并证明它是**蛋白质**——以与萨姆纳互证的方法把「酶是蛋白质」推向定论；1934 年因此当选美国国家科学院院士。
6. **消化酶家族全谱（1930s）**：相继分离结晶胃蛋白酶原（pepsinogen，胃蛋白酶前体）、胰蛋白酶（trypsin）、糜蛋白酶（chymotrypsin）、羧肽酶（carboxypeptidase）。
7. **首个噬菌体结晶（1938）**：分离并结晶**第一个噬菌体**（攻击细菌的小病毒），判定其为**核蛋白**——病毒研究的化学转折点；同年当选美国哲学学会会士。
8. **《Crystalline Enzymes》（1939）**：专著《Crystalline Enzymes: The Chemistry of Pepsin, Trypsin, and Bacteriophage》——同年获国家科学院 **Daniel Giraud Elliot Medal**。
9. **Berkeley 双聘（1949）**：加盟加州大学伯克利分校任细菌学教授，后改任生物物理学教授——退休后仍为 Berkeley 细菌学与医学物理荣休教授。
10. **1946 诺贝尔化学奖（三人共享）**：与 James Batcheller Sumner、Wendell Meredith Stanley 共享——页面口径 "The award was given for these scientists' isolation, crystallization, and study of enzymes, proteins, and viruses."（页面未载官方 citation 整句，**勿杜撰**）；1946-12-12 诺奖演讲 *The Preparation of Pure Enzymes and Virus Proteins*。
11. **AAAS Fellow（1949）**：当选美国艺术与科学院 Fellow。
12. **平凡家庭生活**：弗农山小屋 → Cotuit 海滨—— commute 普林斯顿实验室，亲近他钟爱的荒野。
13. **结局与身后（1961–1987）**：1961 年从洛克菲勒研究所退休；1987-05-27 在亚利桑那州威肯伯格**自杀身亡**，享年 95——按页面如实，克制一笔。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深蓝紫 navyviolet） | `#2A3468` | 消化酶与病毒蛋白质的冷冽 precision（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（胃蛋白酶 badgePepsin） | `#1E5A8A` | 蓝 1929 结晶 / 蛋白质判据 |
| 分类色 2（消化酶全谱 badgeEnzymes） | `#1B7A6B` | 青 trypsin / chymotrypsin / carboxypeptidase |
| 分类色 3（噬菌体结晶 badgePhage） | `#8A2E5A` | 玫瑰 1938 首个噬菌体结晶 / 核蛋白 |
| 分类色 4（共同得主 badgeCoLaureate） | `#7A4A1E` | 赭 Sumner / Stanley 三人共享 |
| 背景 | `#F7F6F9` | 浅灰白（与桑格版一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「蛋白质溶液中缓缓析出的晶体」——从透明到晶簇的过程感。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Daylight** — Alex-Productions（文件 `44-JoyIRE5k2Yo-Daylight.wav`；不要复制 wav 到本目录，Makefile 由主控预置）
- **风格**：白昼 / 澄澈 / 真相大白的开阔感
- **匹配理由**：
  - "白昼" 匹配其科学功绩——结晶让看不见的酶与病毒第一次「现出原形」，晦暗处天亮
  - "澄澈" 匹配实验美学——一份晶体，就是一份纯净与确定的宣言
  - "开阔" 匹配其一生跨度——从遗腹子到 95 岁高龄，横跨酶学从争议到定论的整个时代
- **时长**：以曲目实际时长为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 让酶与病毒现出原形的化学家 / John Howard Northrop 1891–1987 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍/教育/博士/师承（metadata 口径注记）/出生地/去世地/领域/荣誉）
03  诺思罗普的一生 — 高斯式时间线（10 节点：1891→1912→1915→1916→1929→1934→1938→1946→1949→1987）
04  早年：遗腹子与哥伦比亚 (1891–1915) — 表格「时间|事件|结果」
05  一战发酵与转向酶学 (1914–1918) — 表格「任务|技术|去向」（丙酮/乙醇发酵 → 酶）
06  胃蛋白酶结晶 (1929) — 表格「问题|方法|结果」+ 公式框：胃蛋白酶提纯 → 结晶 → 蛋白质判据
07  消化酶全谱 (1930s) — 表格「酶|状态|意义」（pepsinogen/trypsin/chymotrypsin/carboxypeptidase）
08  首个噬菌体结晶 (1938) — 表格「对象|方法|结果」+ 公式框：噬菌体 = 核蛋白
09  《Crystalline Enzymes》与 Elliot Medal (1939) — 表格「著作|内容|荣誉」
10  1946 诺贝尔化学奖 — 表格「人物|方向|结果」（三人共享，页面口径原句；1946-12-12 演讲标题）
11  荣誉与机构 — 高斯式「类别|代表|意义」表格（NAS 1934 / 美国哲学学会 1938 / AAAS Fellow 1949 / Rockefeller 45 年 / Berkeley 1949）
12  家庭与晚景 — 高斯式时间线（Louise Walker 1917 → 两子女 → Cotuit → 1961 退休 → 1987 威肯伯格）
13  遗产：结晶术统一酶与病毒 — 四分类遗产盒 + 公式框：酶·蛋白质·病毒的统一化学观
14  结尾 — 「一份晶体，把生命化学拉进白昼。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1946 诺奖理由 | 页面口径 "The award was given for these scientists' isolation, crystallization, and study of enzymes, proteins, and viruses."（**页面未载官方 citation 整句，勿杜撰**）；**三人共享**：Sumner + Northrop + Stanley——勿写共享两人或独享 |
| 分工表述 | Northrop：胃蛋白酶等消化酶 + 噬菌体结晶；Sumner：尿素酶结晶 + 酶=蛋白质双首创；Stanley：病毒（以其本人篇为准）——首创归属**勿抢**：Sumner 页面明载两大首创属 Sumner |
| 父亲之死 | 父 John Isaiah Northrop 死于**实验室爆炸**、时在诺思罗普出生前两周——勿写成「早年丧父」模糊表述 |
| 噬菌体表述 | 1938 年结晶的是**第一个噬菌体**（a small virus that attacks bacteria），判定为核蛋白——勿写成「结晶第一个病毒（泛称）」或「发现噬菌体」 |
| 师承口径 | 正文与 infobox 无载；metadata 载 Jacques Loeb、Thomas Hunt Morgan——身份信息页如实注「metadata 口径」，**不入库** |
| 自杀结局 | 1987-05-27 在威肯伯格自杀——页面明载，仅此一句客观陈述，勿渲染细节 |
| 通勤地点 | 洛克菲勒研究所laboratory 在**普林斯顿（新泽西）**、家在纽约州弗农山/Cotuit——「在纽约市工作 45 年」的表述要与 Princeton 实验室细节区分 |
| 女婿 | 女儿 Alice 嫁 **Frederick C. Robbins**（1954 诺贝尔生理学或医学奖得主）——姻亲关系，勿计入本人直接社会关系库 |
| Delbrück 论战 | 页面仅在 Further reading 文献标题中出现 "The controversy between John H. Northrop and Max Delbrück on the formation of bacteriophage"——正文未载论战内容，**不入库**、正文勿展开 |
| 引用红线 | 全篇页面无直接引语——一律间接转述，**不得出现引号内"原话"**（演讲标题、著作名、诺奖口径句可原样呈现） |
| 同名区分 | 儿子 John（海洋学家）与其本人近似同名——家庭叙事中如提及须写全称「其子 John（海洋学家）」，**禁止**单独以 "John Northrop" 入库（防 stub 分裂/自环） |
| NMS 陷阱 | metadata 载 National Medal of Science，正文与 infobox 无载——奖项清单**不收**，如需提及注明 metadata 口径 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q106399 | ✅ |
| name_zh | 约翰·霍华德·诺思罗普 | ✅ |
| name_en | John Howard Northrop（新建记录） | ✅ |
| birth_date | 1891-07-05 | ✅ |
| death_date | 1987-05-27 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：enzymology / biochemistry / virology，带 rank） | ✅ |
| has_biography | false（Beamer 立传完成后由主控置 1） | ✅ |

## 7. 社会关系入库清单

**家人 / 共同得主**（仅收 page.md 正文或 infobox 明载）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Louise Walker | 无向 | 1917 年结婚；1891–1975 |
| co-honored | James B. Sumner | 无向 | 1946 年诺贝尔化学奖共同得主 |
| co-honored | Wendell Meredith Stanley | 无向 | 1946 年诺贝尔化学奖共同得主 |

> **禁入库名单**：Jacques Loeb、Thomas Hunt Morgan（metadata doctoral_advisor，正文与 infobox 无载）；其子 John（海洋学家，近同名防分裂）；女儿 Alice 与其夫 Frederick C. Robbins（姻亲）；Max Delbrück（论战仅见于 Further reading 文献标题，正文无载）——均**不入库**。

## 8. 奖项清单

- Nobel Prize in Chemistry（1946，与 Sumner / Stanley 共享；1946-12-12 诺奖演讲 *The Preparation of Pure Enzymes and Virus Proteins*）
- Daniel Giraud Elliot Medal（1939，国家科学院；因 1939 年专著 *Crystalline Enzymes: The Chemistry of Pepsin, Trypsin, and Bacteriophage*）
- Member of the National Academy of Sciences（1934）
- Member of the American Philosophical Society（1938）
- Fellow of the American Academy of Arts and Sciences（1949）

## 9. 机构清单

- 教育：Yonkers High School → Columbia University（BA 1912；化学 PhD 1915）
- 任职：U.S. Chemical Warfare Service（一战，发酵法产丙酮/乙醇）→ Rockefeller Institute for Medical Research（1916–1961，45 年；实验室在新泽西州普林斯顿）→ University of California, Berkeley（1949 起细菌学教授，后任生物物理学教授；退休后为细菌学与医学物理荣休教授）
- 家庭居所：纽约州弗农山郊外 → 马萨诸塞州 Cotuit

## 10. 终审清单

- [ ] 生卒 1891-07-05 / 1987-05-27，享年 95，出生地扬克斯、去世地威肯伯格
- [ ] 父亲实验室爆炸身亡（出生前两周）；母 Alice Rich Northrop 亨特学院植物学教师
- [ ] 1929 胃蛋白酶结晶 + 蛋白质判据；1938 首个噬菌体结晶=核蛋白
- [ ] 1946 三人共享（Sumner、Stanley），理由用页面口径句，勿编官方 citation
- [ ] 师承页面无载如实注（Loeb/Morgan 仅 metadata 口径）
- [ ] 自杀结局一句客观陈述；Delbrück 论战不展开
- [ ] 全篇无直接引语——不得出现引号内"原话"
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/John_Howard_Northrop/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 images.txt 装载（页面 infobox 本无肖像行，404 则装饰圆占位并如实标注）
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：全篇不得出现引号内"原话"（页面无直接引语）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与桑格模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐
