# Adolf Butenandt（阿道夫·布特南特）立传提示词

> qid=Q5327 · 1903-03-24 – 1995-01-18 · 德国生物化学家 · 20 世纪 · 诺贝尔化学奖（1939，与 Leopold Ružička 共享；1949 年才受领）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Adolf_Butenandt/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传的 Beamer 格式与提示词结构**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 images.txt 仅有雌酮结构式插图（Estrone_structure.svg，**不可作肖像**，可作核心贡献页插图）；先尝试 Wikipedia REST API `page/summary` 取 infobox 原图（Commons `Special:FilePath` 回退，250px 改 500px）；404 则用**装饰圆占位**（主色渐变圆 + 首字母 AB），并在 Review 时记录。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 性激素化学的奠基人\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名 Adolf Friedrich Johann Butenandt、国籍、出生地 Lehe（今 Bremerhaven）/去世地 Munich、教育（Marburg → Göttingen）、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「甾体四环骨架」母题——错落的圆环暗示甾体 A/B/C/D 四环。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如雌酮结构式 / 甾体激素提取-合成路线。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Adolf Friedrich Johann Butenandt（中文惯称：阿道夫·弗里德里希·约翰·布特南特，通称 Adolf Butenandt）
- **生卒**：1903-03-24 生于普鲁士王国汉诺威省 Lehe（今不莱梅哈芬）→ 1995-01-18 逝于慕尼黑，享年 91
- **国籍**：Germany（德国）
- **身份**：生物化学家（性激素化学；马普学会主席 1960–1972）
- **家庭**：妻 Erika（1906 年生，1995 年与布特南特同年去世，享年 88），育七子
- **教育轨迹**：
  - 起步于 Marburg University
  - 博士阶段加入哥廷根 **Adolf Windaus**（诺贝尔化学奖得主）课题组，1927 年获化学 PhD（infobox 论文条目标注 1928）
  - 博士课题：分离并表征 *Derris elliptica*（鱼藤）根中毒性杀虫成分（鱼藤酮类，rotenone）的化学
  - Habilitation 后 1931 年任哥廷根讲师
- **导师**：Adolf Windaus（博士导师，1928 诺贝尔化学奖得主）
- **研究领域**：有机化学与生物化学——性激素（雌酮、黄体酮、睾酮）、昆虫信息素（蚕蛾醇 bombykol）、甾体化学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **北海之滨的少年（1903）**：生于 Lehe（今 Bremerhaven）——后来该市以他命名荣誉市民（1960）。
2. **马尔堡起步**：大学学业始于 Marburg University。
3. **哥廷根：诺奖得主门下（至 1927）**：加入 Adolf Windaus 课题组，以鱼藤杀虫毒素的化学研究获 PhD——天然产物化学起点。
4. **转向激素：两条建议**：Adolf Windaus 与先灵公司的 Walter Schöller 建议他研究**从卵巢提取的激素**——由此改变其学术方向。
5. **雌酮与女性激素的分离**：从数千升尿液中提取出雌酮（estrone）及其他主要女性性激素——"以吨计原料换毫克级纯品"的提取化学。
6. **但泽教授时期（1933–1936）**：任 Butenandt 但泽工业大学（Technical University of Danzig）正教授；1934 年提取**黄体酮**（progesterone），次年提取**睾酮**（testosterone）。
7. **1939 诺贝尔化学奖**：官方理由 "work on sex hormones"；与 Leopold Ružička（甾体合成）**共享**；因政府政策**最初拒领**，**1949 年**战后才接受。
8. **柏林-达勒姆所长（1936）**：出任威廉皇帝生化研究所（Kaiser Wilhelm Institut，后 Max Planck Institute for Biochemistry）所长——前任所长 Carl Neuberg 因犹太身份被免职；同年 5 月 1 日加入 NSDAP（党员号 3716562）。
9. **战争科研的灰色地带**：鱼藤酮研究被纳粹领导层视为可用于战壕灭虱；申请 "kriegswichtig"（对战争重要）政府资助；1940 年参与为潜艇长途航行研究激素治疗；获战争功绩十字勋章（1942 二等 / 1943 一等）——战后与身后其政治立场始终未获完全澄清（page.md 明载 "never been fully resolved"）。
10. **战后重建**：1945 年研究所迁图宾根，任图宾根大学教授；1948 年曾被考虑巴塞尔大学生理医学讲席，最终被化学工业界说服留在德国；1956 年研究所迁马丁斯里德，任慕尼黑大学（LMU）教授。
11. **马普学会主席（1960–1972）**：接替 Otto Hahn 出任 Max Planck Society 主席十二年。
12. **蚕蛾醇 bombykol（1959）**：**首次**发现并命名家蚕蛾性信息素 bombykul——信息素化学的开山之作。
13. **荣誉的一生**：14 个荣誉博士（图宾根 1949、LMU 1950、格拉茨 1957、利兹 1961、塞萨洛尼基 1961、马德里 1963、维也纳 1965、圣路易斯 1965、洪堡柏林 1966、剑桥 1966、格但斯克工业大学 1994 等）；Pour le Mérite（1962）、巴伐利亚马克西米利安科学与艺术勋章（1981）、联邦大十字级勋章等；1951–1992 年间 31 次参加林道诺奖得主大会（纪录）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（青碧 deep-teal） | `#0F4C5C` | 甾体骨架的沉静（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（女性激素 badgeEstro） | `#8C3A5B` | 玫瑰雌酮 / 黄体酮 |
| 分类色 2（男性激素 badgeAndro） | `#1B6B5A` | 绿睾酮 / 雄甾酮 |
| 分类色 3（信息素 badgePheromone） | `#C9702A` | 橙蚕蛾醇 bombykol |
| 分类色 4（历史之重 badgeShadow） | `#7A2430` | 暗红 NSDAP / 战时科研 / 拒领-受领 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「甾体四环骨架」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**PAST** — Alex-Productions（文件 `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav`；不要复制 wav 文件，Makefile 直接引用该路径）
- **风格**：回望 / 沉思 / 纪录片
- **匹配理由**：
  - "回望" 匹配布特南特需要双重审视的一生——激素化学的辉煌（雌酮→黄体酮→睾酮→bombykol）与纳粹时期的未决争议同页并存
  - "沉思" 匹配"政治立场从未完全澄清"（page.md 原文）的克制叙事基调
  - 恢弘段落匹配马普学会主席 12 年的科学组织者生涯
- **时长对齐**：以实际曲目时长与 15 页 × 7 秒 ≈ 105 秒比较，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 性激素化学的奠基人 / Adolf Butenandt 1903–1995 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/去世地/教育/博士导师/领域/荣誉）
03  布特南特的一生 — 高斯式时间线（10 节点：1903→1927→1931→1933→1934→1936→1939→1945→1960→1995）
04  早年：马尔堡到哥廷根 (1903–1927) — 表格「时间|事件|结果」+ Windaus 门下
05  两条建议：转向卵巢激素 — Windaus 与 Schöller 的建议（表格「人物|角色|影响」）
06  雌酮：数千升尿液的提取 (1931 前后) — 表格「问题|方法|结果」+ 公式框：雌酮结构式
07  但泽岁月：黄体酮与睾酮 (1933–1936) — 表格「年份|激素|意义」
08  1939 诺贝尔化学奖 — 官方获奖理由 + 与 Ružička 共享 + 1949 受领（表格「得主|领域|理由」）
09  柏林-达勒姆：所长与 NSDAP (1936) — Neuberg 被免职 / 1936-05-01 入党 / 战时科研（克制客观一页）
10  战后：图宾根—马丁斯里德 (1945–1956) — 巴塞尔抉择 / LMU 教授
11  马普学会主席 (1960–1972) — 接替 Otto Hahn / 高斯式流程图：KWG→MPG
12  蚕蛾醇 bombykol (1959) — 信息素化学开山（公式框：bombykol 命名）
13  荣誉与纪录 — 14 个荣誉博士 / Pour le Mérite / 林道大会 31 次（表格）
14  结尾 — 「激素把生命的声音放大，历史则要求科学家诚实作答。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1939 共享 | 与 Leopold Ružička **共享**（Ružička 理由为 polymethylenes 与 higher terpenes 含雄性激素首次合成）；获奖理由按官方口径 "work on sex hormones"（page.md 引号原句） |
| 拒领-受领 | 因政府政策**最初拒领**，**1949 年**战后接受——勿写"主动拒绝"或"1945 受领" |
| 博士年份 | 正文 "finished his studies with a PhD in chemistry in 1927"，infobox 论文条目 1928——行文用 **1927**，必要时加注 infobox 差异 |
| 入党事实 | 1936-05-01 加入 NSDAP、党员号 3716562、Neuberg 因犹太身份被免职、"never been fully resolved"——**page.md 明载，如实呈现**，克制客观；"被视为战时重要" 的资助与 1940 潜艇激素研究一句带过，不渲染 |
| Schöller | Walter Schöller（先灵公司）与 Windaus 共同建议其研究卵巢激素——**page.md 明载**，入库用 other 类型 |
| 同名区分 | Adolf Butenandt（本篇）与 Adolf Windaus（导师）、Adolf von Baeyer（1905 化学奖得主）三人勿混 |
| Otto Hahn | 马普学会主席**前任**—— colleague 关系（机构交接），非师生 |
| bombykol | 1959 年**首次**发现并命名家蚕蛾性信息素——page.md 明载（"He was also the first, in 1959"），可写；细节勿扩大 |
| 荣誉十字 | War Merit Cross（1942 二等 / 1943 一等）是纳粹时期德国勋章——只在"历史之重"页客观列出，勿放入荣誉高光清单 |
| 家庭 | 妻 Erika 1906 年生、1995 年去世（同年）；七子——勿写"妻先逝" |
| 无引语 | page.md 无直接引语——禁造引号"原话"；GDCh 类似定性句不存在本篇，政治评价只用 page.md 明载句 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q5327 | ✅（metadata.json） |
| name_zh | 阿道夫·布特南特 | ✅ |
| name_en | Adolf Butenandt | ✅（page.md 规范名，db_id 空） |
| birth_date | 1903-03-24 | ✅ |
| death_date | 1995-01-18 | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：sex hormones / steroid chemistry / pheromones / organic chemistry，带 rank） | ✅ |
| has_biography | false（立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作者 / 共同得主**（仅收 page.md 正文或 infobox 明载）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Adolf Windaus | 师→生（博士导师） | 哥廷根课题组，1927 年化学 PhD |
| spouse | Erika Butenandt | 无向 | 1906 年生，1995 年同年去世，育七子 |
| colleague | Otto Hahn | 无向 | 马普学会主席职务交接（Hahn→Butenandt，1960） |
| co-honored | Leopold Ružička | 无向 | 1939 诺贝尔化学奖共同得主 |
| other | Walter Schöller | 无向 | 先灵公司化学家，与 Windaus 共同建议其研究卵巢激素 |

**门生**：page.md 无 doctoral students 明载——**不设学生关系**。

> **禁入库名单（metadata-only / 背景人物）**：Carl Neuberg（前任所长，仅机构史背景）、七名子女（未具名）、巴塞尔大学等机构（机构非人物）、NSDAP（组织非人物）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1939，与 Leopold Ružička 共享，"work on sex hormones"；1949 受领）
- War Merit Cross（1942 二等；1943 一等）——历史条目，非高光荣誉
- Paul Ehrlich and Ludwig Darmstaedter Prize（1953）
- Knight Commander's Cross（1959）与 Grand Cross（1964）of the Order of Merit of the Federal Republic of Germany
- Honorary Citizen of Bremerhaven（1960）、Honorary Citizen of Munich（1985）
- Wilhelm Normann Medal（1961）
- Pour le Mérite（1962）
- Austrian Decoration for Science and Art（1964）
- Cultural Honor Prize of the City of Munich（1967）
- Legion of Honour, Commander（1969）
- Ordre des Palmes Académiques（1972）
- Bavarian Maximilian Order for Science and Art（1981）
- Grand Cross 1st class of the Order of Merit of the Federal Republic of Germany（1985）
- Grand Gold Decoration for Services to the Republic of Austria（1994）
- Carus Medal、Harnack Medal、Emil Fischer Medal、Fresenius Prize、August Wilhelm von Hofmann Medal（infobox 载）
- 14 个荣誉博士（图宾根 1949、LMU 1950、格拉茨 1957、利兹 1961、塞萨洛尼基 1961、马德里 1963、维也纳 1965、圣路易斯 1965、洪堡柏林 1966、剑桥 1966、格但斯克工业大学 1994 等）
- 林道诺奖得主大会 31 次参加（1951–1992，纪录）

## 9. 机构清单

- 教育：Marburg University、University of Göttingen（PhD 1927，Windaus 组；Habilitation 后 1931 讲师）
- 任职：Technical University of Danzig（1933–1936 正教授）、Kaiser Wilhelm Institut（柏林-达勒姆，1936 所长；后 Max Planck Institute for Biochemistry；1945 迁图宾根；1956 迁马丁斯里德）、University of Tübingen（1945 教授）、Ludwig-Maximilians-Universität München（1956 教授）
- 科学组织：Max Planck Society（President 1960–1972，接替 Otto Hahn）
- 纪念：荣誉市民（Bremerhaven 1960、Munich 1985）

## 10. 终审清单

- [ ] 生卒 1903-03-24 / 1995-01-18，享年 91；出生地 Lehe（今 Bremerhaven）、去世地慕尼黑
- [ ] 1939 与 Ružička 共享；1949 受领；获奖理由口径准确
- [ ] 博士年份 1927（infobox 1928 加注）；导师 Windaus 表述准确
- [ ] NSDAP（1936-05-01、党员号）、Neuberg 被免职、"never been fully resolved" 如实且克制
- [ ] Schöller 建议句、Hahn 主席交接、bombykol 1959 表述准确
- [ ] War Merit Cross 只入"历史之重"页；荣誉清单年份准确
- [ ] 中文引号内无 page.md 无法溯源的"原话"；无"第一次/唯一"类断言（除 bombykol "first" 原文语境外）
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Adolf_Butenandt/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：images.txt 仅结构式——REST API / Special:FilePath 尝试结果与占位方案记录回写本节
- [ ] **国籍**：封面顶部明示德国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到；本篇全文无直接引语，禁造
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 模板）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，执行者不改。
> **最重要的事：每写一页就 make，看到溢出就修。**
