# Frédéric Joliot-Curie（弗雷德里克·约里奥-居里）立传提示词

> qid=Q150989 · 1900-03-19 – 1958-08-14 · 法国化学家/物理学家 · 20 世纪 · 诺贝尔化学奖（1935，与妻子 Irène Joliot-Curie 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Frédéric_Joliot-Curie/`（page.md + metadata.json + page.html + images.txt）

---

## 0. 正文形式说明（参考 Frederick Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。**本地 images.txt 有真图**：单人照为罗马尼亚纪念邮票照 `Frederic_Juliot-Curie1.jpg`（图注注明"邮票"，执行时优先 REST API 查 1935 年照）；夫妻合影 `Frederic_and_Irene_Joliot-Curie.jpg`（1940s）可裁剪并加注——**两人独立立传须用不同源**：Frédéric 用单人/邮票照，Irène 用 Harcourt 照（见其篇）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{radiation}\enspace 人工放射性的发现者\enspace·\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Jean Frédéric Joliot，婚后改姓 Joliot-Curie）、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「链式反应」母题——一个母圆点裂生出多个子圆点，暗示核裂变与人工放射性的传递。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——人工放射性页写 α 轰击铝生成磷-30 的核反应式（参照 Irène 篇 ²⁷Al + ⁴He → ³⁰P + n），链式反应页写临界条件示意。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Jean Frédéric Joliot-Curie（出生名 Jean Frédéric Joliot；1926 婚后夫妻同改复合姓 Joliot-Curie；女儿转述：签署科学论文时仍用 Irène Curie 与 Frédéric Joliot）
- **生卒**：1900-03-19 生于巴黎（法兰西第三共和国）→ 1958-08-14 逝于巴黎（第四共和国），享年 58；死因为肝病，与其妻一样被归因于长期过量辐射暴露
- **国籍**：France（法国）
- **身份**：化学家、物理学家；法兰西公学院教授；法国抵抗运动领袖、法国共产党中央委员（1956）；战后首任法国原子能高级专员
- **家庭**：1926-10-04 在巴黎娶 Irène Curie（居里夫妇长女，其导师 Marie Curie 之女），婚后改姓；子女 Hélène Langevin-Joliot（1927，核物理学家）与 Pierre Joliot（1932，CNRS 生物化学家）；夫妻 1948 年矿工罢工期间收养两名女孩（经 Irène 倡议寄养煤矿工子女）
- **教育轨迹**：Lycée Lakanal → ESPCI Paris（巴黎高等物理化学学院）毕业 → 在 Marie Curie 坚持下再考 baccalauréat、读学士、攻博士学位（放射元素电化学）
- **博士**：1930，论文《Etude électrochimique des radioéléments: Applications diverses》（放射元素的电化学研究）
- **导师**：Marie Curie（博士导师；1925 年起任其镭研究所助手）
- **研究领域**：核物理、放射化学、核反应堆、放射生物学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **工程师入居里门下（1900–1925）**：ESPCI 工程师出身，1925 年成为 Marie Curie 在镭研究所的助手——由此遇见 Irène；在 Marie 坚持下补齐学士与博士的全部正规训练。
2. ** marriage 与改姓（1926）**：1926-10-04 婚后夫妻同改复合姓 Joliot-Curie——科学史上最著名的"双姓实验室"由此成立。
3. **核反冲实验（1928–1932）**：巴黎理学院任讲师期间与妻子合作研究原子核结构，尤其是被粒子击中核的反冲（projection/recoil of nuclei）——这一工作成为 Chadwick 1932 年发现中子的必要一步。
4. **与正电子、中子擦肩（1932）**：用 γ 射线鉴别正电子的实验同样识别出了正电子与中子，但未能解读其意义——发现分别被 Carl David Anderson 与 James Chadwick 取得（"错过的诺奖"叙事，须克制客观）。
5. **首次精确计算中子质量（1933）**：夫妻二人 first to calculate accurately the mass of the neutron。
6. **质子-中子-正电子假说与索尔维受挫（1933-10）**：α 轰击铝只测到质子，据此提出质子转化为中子+正电子的新理论；在第七届索尔维会议上被 46 位与会科学家中的多数批评——但后续实验证明其方向正确。
7. **人工放射性（1934）**：用 α 粒子轰击硼、镁、铝，制造出放射性氮、磷、硅同位素（²⁷Al + ⁴He → ³⁰P + n，衰变放出正电子）——**人工放射性**（induced/artificial radioactivity）正式诞生；使医用放射性材料得以快速、廉价、大量生产。
8. **1935 诺贝尔化学奖**：与妻子共享，理由为发现人工放射性——继岳父母之后**第二对**诺贝尔奖夫妻（居里家族诺奖增至 4/5 座）；诺奖演讲（1935-12-12）*Chemical Evidence of the Transmutation of Elements*。
9. **法兰西公学院与核链式反应（1937–1939）**：1937 离镭研究所任法兰西公学院教授；1939-01 致信苏联同事 Abram Ioffe 通报德国发现铀核裂变；随后专攻链式反应与可控核反应堆条件；被 Einstein–Szilárd 致罗斯福信列为链式反应方向的核心科学家之一。
10. **战时：文件转移与抵抗运动（1940–1944）**：1940 纳粹入侵前与 Hans von Halban、Lew Kowarski、Moshe Feldenkrais 把研究文件与材料转移英国；1941-06 参与创建抵抗组织 National Front 并任主席；1942 春加入法国共产党；1944-08 巴黎起义期间在警察局为起义者制造燃烧瓶；战后受 Alsos Mission 讯问并向英方提供德国科学家情报。
11. **法国核计划的缔造者（1945–1950）**：1945 受戴高乐任命出任首任原子能高级专员（CEA）并任 CNRS 主任；1948 监督建成法国第一座核反应堆 Zoé；确保博士生 Toshiko Yuasa 战后重返法国 CNRS。
12. **和平斗士（1950–1958）**：1950 因共产党员身份被清洗免去原子能职务（保留公学院教席）；1945-06 访莫斯科纪念俄国科学院 220 周年；World Council of Peace 主席（1950–1958），获首届斯大林和平奖（1950-04-06 颁发）；1955 年为 Russell–Einstein Manifesto 十一位签署人之一。
13. **Orsay 与身后（1956–1958）**：1956 妻子病逝后接任索邦核物理讲席；生命最后几年倾力创建 Orsay 理学部与核物理中心（今巴黎-萨克雷大学）；1958-08-14 因肝病去世；月球 Joliot 陨石坑、索菲亚地铁 Joliot-Curie 站等以之命名；Transfermium Wars 中 102/105 号元素曾拟名 "joliotium"（Jl）。

## 3. 配色方案（主色 + 强调 + 分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深酒红 burgundy） | `#7E1E23` | 抵抗运动的旗帜红与镭的幽光（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（人工放射性 badgeInduced） | `#2E5A9E` | 蓝诱导放射性 / 放射性同位素 |
| 分类色 2（核物理 badgeNuclei） | `#8E44AD` | 紫核反冲 / 中子质量 / 正电子 |
| 分类色 3（核能与反应堆 badgeReactor） | `#1B7A43` | 绿链式反应 / Zoé / CEA |
| 分类色 4（抵抗与和平 badgePeace） | `#D97B29` | 琥珀 National Front / 斯大林和平奖 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（一母多子的裂生圆点，四档大小错落），呼应「链式反应」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Falling Apart** — Michael FK & Andy Leech（路径 `music_audio/inspiring-electronic/03-qtNSLNUd1VE-...Falling Apart.wav`）
- **风格**：情绪 / 沉郁 / 张力
- **匹配理由**：
  - "沉郁" 匹配其一生底色——发现之光与战争阴影交替（入侵、抵抗、清洗、辐射早逝）
  - "张力" 匹配其身份冲突——科学家/抵抗领袖/共产党员/和平使者的多重张力
  - 曲名暗合其晚年：身体的崩解与事业的不朽并存（克制使用，不做悲情渲染）
- **时长**：执行时核对，不足 15 页 × 7 秒则循环或 ffmpeg 对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 人工放射性的发现者 / Frédéric Joliot-Curie 1900–1958 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  约里奥-居里的一生 — 高斯式时间线（10 节点：1900→1925→1926→1934→1935→1937→1941→1945→1950→1958）
04  早年：从 ESPCI 到镭研究所 (1900–1926) — 表格「时间|事件|结果」（含 Marie 坚持补学位）
05  核反冲与错过的发现 (1928–1932) — 表格「对象|方法|结果」+ 正电子/中子两行擦肩注记
06  人工放射性 (1934) — 表格「靶核|轰击|产物」+ 公式框：²⁷Al + ⁴He → ³⁰P + n（正电子衰变）
07  1935 诺贝尔化学奖 — 共享标注醒目（与 Irène）+ 官方理由 + 第二对诺奖夫妻 + 居里家族 4/5 座
08  链式反应的先声 (1937–1939) — 表格「事件|人物|结果」（Ioffe 信 / Einstein–Szilárd 信提及）+ 公式框：链式反应示意
09  战时：抵抗运动 (1940–1944) — 表格「时间|行动|风险」（文件转移 / National Front / 燃烧瓶）
10  法国核计划 (1945–1950) — 高斯 FFT 页式流程图（CEA 1945 → CNRS 主任 → Zoé 1948 → 1950 被清洗）
11  和平斗士 (1950–1958) — 表格「角色|平台|荣誉」（World Council of Peace / 斯大林和平奖 / Russell–Einstein Manifesto）
12  Orsay 与身后 (1956–1958) — 表格「时间|事件|结果」+ 命名遗产（Joliot 陨石坑 / joliotium 提案）
13  遗产：从实验室到原子时代 — 四分类遗产盒（人工放射性/核物理/核能/和平运动）
14  结尾 — 「他们把放射性，从自然的馈赠变成了人类的造物。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1935 诺奖理由 | 与妻子 **共享**，理由为发现人工放射性（induced radioactivity）；诺奖演讲标题 *Chemical Evidence of the Transmutation of Elements*（1935-12-12）——勿写"独享"或"物理学奖" |
| 第二对诺奖夫妻 | 继岳父母 Pierre & Marie Curie 之后第二对；居里家族诺奖总数 Frédéric 篇口径为 **4** 座（Irène 篇口径为 5 座，含 Marie 双奖）——两篇各忠于本人页面，勿跨篇统一 |
| 本名与署名 | 出生名 Jean Frédéric Joliot；女儿转述"论文署名 Irène Curie 与 Frédéric Joliot"——引语照录，勿改写为"夫妇一直用复合姓" |
| 错过的发现 | 1932 年实验识别出正电子与中子但未解读，分属 Anderson（正电子）与 Chadwick（中子）——客观陈述，勿写"被抢诺奖" |
| 中子质量 | 1933 夫妻 first to calculate accurately the mass of the neutron——"精确计算"勿写成"发现中子" |
| Chadwick 关系 | 夫妻反冲实验是 Chadwick 发现中子的 essential step——是"工作被引用"而非"合作"，入库用 other 类型 |
| 政党与清洗 | 1942 加入法共、1956 入中央委员会；1950 被清洗去 CEA 职务（保留公学院教席）——史实陈述，不加褒贬；斯大林和平奖客观写（1950 奖 / 1951-04-06 颁发） |
| 抵抗细节 | 燃烧瓶一段出自 Collins & LaPierre《Is Paris Burning?》（page.md 明引）——注明出处性质；1944-08 时间勿写错 |
| Toshiko Yuasa | 博士生，战后因尤里奥确保得以返法继续 CNRS 研究——一句客观叙述 |
| 火化/葬礼 | 本页无载国葬细节（Irène 篇有国葬记载）——Frédéric 篇勿写"国葬" |
| 同名区分 | 与 Frédéric Joliot-Curie Metro Station（索菲亚）、月球 Joliot 陨石坑、元素 joliotium 提案各为独立条目；与 Irène Joliot-Curie 独立立传，勿在封面混排两人 |
| 引语红线 | 中文引号内不得出现 page.md 无法溯源的"原话"；可用原句仅诺奖演讲标题与女儿转述署名句；其余全部间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q150989 | ✅（回填至既有 stub #2823） |
| name_zh | 弗雷德里克·约里奥-居里 | ✅ |
| name_en | Frédéric Joliot-Curie | ✅（用 db_name_en 精确形式） |
| birth_date | 1900-03-19 | ✅ |
| death_date | 1958-08-14 | ✅ |
| nationality | France | ✅ |
| primary_occupation | chemist | ✅（infobox Fields：Chemistry, Physics） |
| field_of_work | nuclear physics（person_field 细分：nuclear physics / radiochemistry / electrochemistry，带 rank） | ✅ |
| has_biography | false（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作者 / 门生**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Marie Curie | 师→生（博士导师） | 1925 起镭研究所助手；1930 放射元素电化学博士 |
| advisor-student | Georges Charpak | 约里奥→学生 | infobox doctoral students；1965 诺贝尔物理学奖 |
| advisor-student | Toshiko Yuasa | 约里奥→学生 | 战后由其确保重返法国 CNRS |
| colleague | Hans von Halban | 无向 | 1940 文件转移；链式反应合作 |
| colleague | Lew Kowarski | 无向 | 1940 文件转移；链式反应合作 |
| colleague | Moshe Feldenkrais | 无向 | 1940 文件转移同行 |
| colleague | Abram Ioffe | 无向 | 1939-01 致信通报德国铀裂变发现 |
| colleague | Albert Einstein | 无向 | 1939 Einstein–Szilárd 信中被列为链式反应核心科学家；1955 Russell–Einstein Manifesto 共同签署人 |
| other | James Chadwick | 无向 | 约里奥夫妇核反冲实验是 Chadwick 1932 发现中子的必要一步（工作被引用，非合作） |

**家庭**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Irène Joliot-Curie | 无向 | 1926-10-04 巴黎成婚，夫妻同改姓 Joliot-Curie |
| co-honored | Irène Joliot-Curie | 无向 | 1935 诺贝尔化学奖共同得主（人工放射性） |
| parent-child | Hélène Langevin-Joliot | 约里奥→孩子 | 长女，核物理学家 |
| parent-child | Pierre Joliot | 约里奥→孩子 | 次子，CNRS 生物化学家 |

> **禁入库名单**（metadata.json-only 或页面仅提及、无实质关系载述）：Marie Curie（岳母/博士导师之外的社会关系不再单列）、Irène 之外家族成员 Ève Curie（仅家族背景）、Winston Churchill / Charles de Gaulle（任命关系非社会关系）、Collins & LaPierre（著作作者）、Bernard Vonnegut（无）、Pierre Biquard（合影图注出现，正文无实质载述）、Ouang 家族（合影图注）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1935，与 Irène Joliot-Curie 共享）
- Matteucci Medal（1932）
- Hughes Medal（1947）
- Barnard Medal for Meritorious Service to Science（与 Irène 共同；Irène 篇作 1940）
- Stalin Peace Prize（1950 奖，1951-04-06 颁发；首届）
- French Academy of Sciences 与 Academy of Medicine 成员
- ForMemRS（1946）；荷兰皇家艺术与科学院外籍院士（1946）
- Légion d'honneur：Knight → Officer → Commander（指挥官级，表彰抵抗运动）
- Croix de guerre 1939–1945；Order of the Cross of Grunwald 3rd class；Polonia Restituta 指挥官星章；Work Flag Order 1st class
- 荣誉博士：Jagiellonian University（克拉科夫）、Maria Curie-Skłodowska University、University of Warsaw、University of Łódź

## 9. 机构清单

- 教育：Lycée Lakanal、ESPCI Paris、Science Faculty of Paris（博士 1930）
- 任职：Radium Institute（Curie Institute, Paris，1925 助手起）→ Paris Faculty of Science 讲师 → Collège de France 教授（1937–）→ CNRS 主任 → 法国原子能高级专员（1945–1950 被清洗）→ Sorbonne 核物理讲席（1956，继 Irène）→ Orsay 理学部创建（今 Paris-Saclay University）
- 命名遗产：月球 Joliot 陨石坑；索菲亚 Joliot-Curie 地铁站；法/德/波兰/罗马尼亚/斯洛伐克/加拿大多地街道；元素 102/105 拟名 "joliotium"（Transfermium Wars，未采用）

## 10. 终审清单

- [ ] 生卒 1900-03-19 / 1958-08-14，享年 58，出生地巴黎、去世地巴黎
- [ ] 1935 共享（Irène）、人工放射性理由原句表述准确；"第二对诺奖夫妻"与居里家族 4 座口径准确
- [ ] 博士导师 Marie Curie、1930 电化学博士表述准确
- [ ] 1932 擦肩（Anderson/Chadwick）与 1933 中子质量表述准确
- [ ] 抵抗运动时间线（1940 转移 / 1941-06 National Front / 1942 法共 / 1944-08 燃烧瓶）准确
- [ ] 1950 清洗与 1950 斯大林和平奖、1955 Manifesto 签署表述客观准确
- [ ] 与 Irène 篇互指一致（spouse + co-honored + parent-child 三类全覆盖）
- [ ] 引语仅两条白名单且可在 page.md 溯源
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Frédéric_Joliot-Curie/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：优先 REST API 查 1935 年照；退用邮票照（图注注明"罗马尼亚纪念邮票"）或夫妻合影裁剪加注
- [ ] **国籍**：封面顶部明示法国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 Irène 篇及化学家侧既有格式（Frederick_Sanger_zh.tex）对齐
