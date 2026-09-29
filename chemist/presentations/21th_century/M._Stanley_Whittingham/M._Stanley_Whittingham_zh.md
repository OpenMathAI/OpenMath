# M. Stanley Whittingham（斯坦利·惠廷厄姆）立传提示词

> qid=Q285062 · 1941-12-22 –（在世）· 英国/美国 · 诺贝尔化学奖（2019，与 John B. Goodenough、Akira Yoshino 共享）· 本地数据源：`chemist/presentations/21th_century/pages/M._Stanley_Whittingham/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：对齐 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}` 高斯式骨架——表格语义化 tabularx + 公式展示框 + 时间线页 + 气泡背景。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像用本地 `images.txt` 首图 Whittingham in 2026 照；下载失败则装饰圆占位并在 Review 注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{bolt}\enspace 锂电池的奠基人\enspace·\enspace 英国 / 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Michael Stanley Whittingham）、国籍（英国出生美国工作）、教育（Stamford School / New College, Oxford）、博士导师（Peter Dickens）、博士后导师（Robert Huggins）、配偶（Georgina Whittingham）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「层间夹入」母题——离散圆点暗示锂离子嵌入二硫化钛层间的三明治意象。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配金色边框浅金底公式展示框（`\fcolorbox` + minipage），如 TiS₂ 嵌入反应式或 "jam in a sandwich" 三明治比喻示意（文字示意，非引语）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Sir Michael Stanley Whittingham（中文惯称：斯坦利·惠廷厄姆；2024 年受封 Knight Bachelor）
- **生卒**：1941-12-22 生于英格兰诺丁汉 Carlton 郊区（在世，卒日留白）
- **国籍**：英国出生、美国工作（British-American；frontmatter nationality: United States + United Kingdom）
- **身份**：化学家；Binghamton 大学（纽约州立大学）化学与材料科学系杰出教授；材料研究所与材料科学与工程项目的创始主任（past founding director）；美国能源部 NECCES（东北化学储能中心）主任
- **家庭**：父为土木工程师（家族第一位上大学者）；母 Dorothy Mary（娘家姓 Findley）婚前为化学家；妻 Georgina Whittingham 博士（SUNY Oswego 西班牙语教授）；子女二人：Michael Whittingham、Jenniffer Whittingham-Bras
- **教育轨迹**：
  - Stamford School（1951–1960）
  - New College, Oxford 攻读化学：BA（1964）、MA（1967）、DPhil（1968），论文《Microbalance studies of some oxide systems》
  - 斯坦福大学博士后
- **博士导师**：Peter Dickens；**博士后导师**：Robert Huggins（Stanford，infobox Other academic advisors）
- **研究领域**：化学——嵌入化学（intercalation chemistry）、电化学储能材料、多电子嵌入反应

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **诺丁汉起步（1941）**：生于英格兰诺丁 Carlton 郊区；父为家族首位大学生（土木工程师），母婚前是化学家。
2. **牛津训练（1960–1968）**：Stamford School 后入 New College, Oxford 读化学，十年内完成 BA/MA/DPhil（1968，氧化物体系微量天平研究）。
3. **斯坦福博士后（1968–）**：师从 Robert Huggins，转向固态离子学与电化学储能方向。
4. **嵌入电极的诞生（1970s）**：在 Fred Gamble 领导的跨学科小组中**发明嵌入电极（intercalation electrode）概念**——离子可逆地嵌入晶格而结构保持不变。
5. **第一个可充锂电池（1977 专利）**：LiAl 阳极 + TiS₂（二硫化钛）嵌入型阴极——高能量密度、锂离子扩散可逆，可充电；专利 1977 年授权 Exxon 商业化（小设备与电动车方向）。
6. **Exxon 时代（16 年）**：Exxon 投入资源推动 Li/LiBX/TiS₂ 电池商业化；因市场太小，Exxon 终止项目，技术授权给美、日、德各一家公司；团队继续在电化学与固态物理期刊发表。
7. **"三明治"比喻**：页面明载惠廷厄姆原话——"All these batteries are called intercalation batteries. It's like putting jam in a sandwich..."（嵌入前后晶体结构完全不变，所以能循环那么久）——本篇唯一可用引语。
8. **转战 Schlumberger（1984–1988）**：随 Gamble 离开 Exxon，任管理者 4 年；1988 年出任 Binghamton 大学化学系教授重返学术。
9. **多电子嵌入（当代研究）**：单电子氧化还原中心限制容量；向多电子嵌入反应推进（LiVOPO4/VOPO4，V³⁺↔V⁵⁺ 多价钒），提升储能密度。
10. **储能建制化**：2007 年联合主持美国能源部化学储能研究；任 NECCES 主任——2014 年获 DOE 1280 万美元、2018 年再获 300 万美元；1994–2000 任 Binghamton 科研副校长（vice provost）。
11. **2015 预言成真**：与 Goodenough 同列 Thomson Reuters Clarivate Citation Laureates（预测诺贝尔化学奖）——四年后成真。
12. **2019 诺贝尔化学奖**："for the development of lithium-ion batteries"（官方理由原句页面明载）——与 John B. Goodenough、Akira Yoshino 共享；诺奖演讲《The Origins of the Lithium Battery》（2019-12-08）；被称"锂离子电池之父"（页面明载 "he is called the founding father of lithium-ion batteries"）。
13. **晚年荣誉**：2018 入选美国国家工程院（表彰"嵌入化学在储能材料中的开创性应用"）；2020 Carnegie Corporation Great Immigrants Award；2023 VinFuture Grand Prize（与 Martin Green、Rachid Yazami、Yoshino 共享）；**2024 年 King's Birthday Honours 受封 Knight Bachelor**（"for services to chemistry"）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（紫罗兰深蓝 violetblue） | `#5B2A86` | 层状晶格与嵌入化学的深邃（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（嵌入化学 badgeInt） | `#1E5631` | 绿——TiS₂ 层间 / 可逆嵌入 |
| 分类色 2（初代锂电 badgeLMB） | `#16324F` | 藏青——LiAl/TiS₂ 电池 / 1977 专利 |
| 分类色 3（储能建制 badgeNEC） | `#B26A00` | 琥珀——NECCES / DOE 储能研究 |
| 分类色 4（荣誉 badgeHonor） | `#8C1F28` | 绯红——NAE 2018 / Knight 2024 / Nobel |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「锂离子嵌入层间的三明治结构」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Winds Of Freedom** — Really Slow Motion & Giant Apes（文件 `music_audio/inspiring-electronic/25-l3Fsk4R6eys-...Winds Of Freedom (Epic Heroic Orchestral).wav`，不要复制 wav）
- **风格**：史诗管弦 / 开拓 / 雄壮上行
- **匹配理由**：
  - "自由之风"匹配 1970s 石油危机背景下的能源突围叙事——以电化学为时代寻找出路；
  - 管弦的上行推进匹配从 TiS₂ 实验室电池到全球锂电产业的奠基性一跃；
  - 沉稳的鼓点匹配"奠基人"二字——为后来者（Goodenough/Yoshino）铺路的第一块基石。
- **时长**：以曲目实际时长为准，ffmpeg `-shortest` 自动对齐 15 页 ≈ 105 秒。

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 锂电池的奠基人 / M. Stanley Whittingham 1941– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/博士导师/博士后导师/配偶/领域/荣誉）
03  惠廷厄姆的一生 — 高斯式时间线（10 节点：1941→1960→1964→1968→1972→1976→1977→1984→1988→2019）
04  诺丁汉与牛津 (1941–1968) — 表格「时间|事件|结果」（Stamford School→New College BA/MA/DPhil→Dickens 指导）
05  斯坦福与嵌入概念 (1968–1972) — 表格「导师|思想|结果」+ 公式框：嵌入反应示意 LixTiS2
06  第一个可充锂电池 (1976–1977) — 表格「问题|方法|结果」+ 公式框：LiAl | LiBX | TiS2 电池构型；1976 Science 论文
07  Exxon 的豪赌与退场 (1970s–1984) — 表格「投入|转折|结果」（商业化→市场太小→授权三家→Gamble 离开）
08  三明治比喻 — 页面明载引语页：嵌入前后晶格不变 → 长循环寿命（唯一引语，全页支撑）
09  重返学术 (1988–) — 表格「机构|职务|研究」（Binghamton 教授→vice provost→NECCES/DOE）
10  多电子嵌入的前沿 — 表格「瓶颈|思路|材料」+ 公式框：LiVOPO4/VOPO4 多价钒多电子反应
11  荣誉与奠基人 — 高斯式「类别|代表|意义」表格（Young Author 1971 / NAE 2018 / Knight 2024 / founding father）
12  2019 诺贝尔化学奖 — 共享结构图解：Whittingham（TiS2 初代）× Goodenough（LixCoO2 正极）× Yoshino（商用化）；理由原句
13  遗产：口袋里的革命 — 四分类遗产盒 + 公式框：从移动电话到电动车（页面 intro 口径）
14  结尾 — 「把离子夹进晶格，为世界储能。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖理由原句 | 官方英文原句 **"for the development of lithium-ion batteries"** 页面明载（Research 节末）——本篇可原句引用；Goodenough/Yoshino 两篇引用时注明口径来源 |
| 2019 三人结构 | 三人**平等共享**同一理由（与 2018 年"一半/另一半"结构不同）——勿套用 Winter 篇的"共享一半"表述 |
| 电池角色分工 | 惠廷厄姆：TiS₂ 嵌入型阴极 + LiAl 阳极初代可充锂电池（1977 专利，Exxon）；Goodenough：LixCoO2 氧化物正极；Yoshino：碳阳极商用化——三者勿混 |
| 双重荣誉混淆 | 2015 Clarivate Citation Laureates（与 Goodenough 同列）是**预测名单**非获奖；2023 VinFuture Grand Prize（与 Martin Green/Rachid Yazami/Yoshino）是另一奖项——两者勿与诺奖混写 |
| 博士导师 | **Peter Dickens**（infobox）；frontmatter `educated_at` 无导师信息；博士后导师 **Robert Huggins**（Stanford，infobox Other academic advisors）——两人分开写 |
| Exxon 年限 | Exxon 16 年 + Schlumberger 4 年（页面明载）——勿写反或合并成"产业界 20 年"；1984 离开 Exxon 是"following Gamble" |
| Knight Bachelor | **2024 King's Birthday Honours**（"for services to chemistry"）；infobox Awards 列表只写 Nobel——爵位年份以 Recognition 节为准 |
| 国籍口径 | British-American；出生地英格兰诺丁汉；nationalities 入库 United Kingdom（rank 0，出生）+ United States（rank 1，工作）——"英国出生美国工作"口径 |
| 引语红线 | 全篇**唯一**可用引语是 "jam in a sandwich" 段（页面明载）；其余一律间接转述；"founding father of lithium-ion batteries" 是页面叙述口径，作称号引用不作引语 |
| Fred Gamble | 页面仅载 "a multidisciplinary group led by Fred Gamble, PhD" 与 "1984 离开 Exxon following Gamble to Schlumberger"——colleague 关系可入，勿拔高为导师 |
| metadata-only 禁入 | frontmatter `award_received` 中 Fellow of the Royal Society 无正文对应叙述——**不入 §8 奖项清单正文**（或仅列且注明 infobox 口径）；子女 Michael/Jenniffer 仅家庭背景，**禁入库** |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q285062 | ✅ |
| name_zh | 斯坦利·惠廷厄姆 | ✅ |
| name_en | M. Stanley Whittingham | ✅（页面标题规范名；清单 db_id 为空） |
| birth_date | 1941-12-22 | ✅ |
| death_date | （空，在世） | ✅ |
| nationality | United Kingdom（rank 0）+ United States（rank 1） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分：chemistry / electrochemistry / intercalation chemistry / lithium-ion battery，带 rank） | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**★红线：只收 page.md 正文或 infobox 明载的关系；metadata-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Peter Dickens | 师→生（博士导师） | 牛津 DPhil（1968，氧化物体系微量天平研究） |
| advisor-student | Robert Huggins | 师→生（博士后导师） | 斯坦福博士后（infobox Other academic advisors） |
| spouse | Georgina Whittingham | 无向 | SUNY Oswego 西班牙语教授 |
| colleague | Fred Gamble | 无向 | Exxon 时期跨学科小组负责人（嵌入电极概念）；1984 随其转投 Schlumberger |
| co-honored | John B. Goodenough | 无向 | 2019 诺贝尔化学奖共同得主；2015 同列 Clarivate Citation Laureates |
| co-honored | Akira Yoshino | 无向 | 2019 诺贝尔化学奖共同得主；2023 VinFuture Grand Prize 共同得主 |
| co-honored | Martin Green | 无向 | 2023 VinFuture Grand Prize 共同得主 |
| co-honored | Rachid Yazami | 无向 | 2023 VinFuture Grand Prize 共同得主 |

> 子女 Michael/Jenniffer、父母：仅家庭背景叙述，**禁入库**。对手方规范名 "John B. Goodenough"、"Akira Yoshino" 与本批两人互指一致；"Martin Green"（页面链接 Martin Green (professor)）与 "Rachid Yazami" 首次入库将由本 yaml 建 stub——用页面全名防分裂。

## 8. 奖项清单

- Nobel Prize in Chemistry（2019，与 Goodenough/Yoshino 共享，"for the development of lithium-ion batteries"）
- Norman Hackerman Young Author Award，The Electrochemical Society（1971）
- Battery Research Award（2003）；ECS Fellow（2004）
- 美国化学会终身贡献奖（2010）；Greentech Media 绿色技术 Top 40 创新者（2010）
- IBA Yeager Award（2012，锂电池材料研究终身贡献）；MRS Fellow（2013）；Turnbull Award（2018）
- Clarivate Citation Laureates（2015，与 Goodenough 同列）
- NAE 成员（2018，"for pioneering the application of intercalation chemistry for energy storage materials"——页面明载引文）
- Great Immigrants Award，Carnegie Corporation（2020）
- VinFuture Grand Prize（2023，与 Martin Green/Rachid Yazami/Akira Yoshino）
- Knight Bachelor（2024 King's Birthday Honours，"for services to chemistry"）
- SUNY Chancellor's Award for Excellence 与 Outstanding Research Award（2007）

## 9. 机构清单

- 教育：Stamford School（1951–1960）；New College, University of Oxford（BA 1964 / MA 1967 / DPhil 1968）
- 博士后：Stanford University
- 产业：Exxon Research & Engineering Company（16 年）；Schlumberger（4 年，管理者）
- 学术：Binghamton University, SUNY（1988– 教授；Distinguished Professor；1994–2000 vice provost for research；材料研究所与 MSE 项目创始主任；NECCES 主任）；NAATBatt International 首席科学官（2017）

## 10. 终审清单

- [x] 生卒 1941-12-22 / 在世留白；出生地 Nottingham（Carlton 郊区）
- [x] 博士导师 Peter Dickens / 博士后导师 Robert Huggins 分写正确
- [x] 2019 三人平等共享；理由原句 "for the development of lithium-ion batteries" 页面明载
- [x] TiS₂ 阴极 + LiAl 阳极初代锂电、1977 专利、Exxon 16 年 / Schlumberger 4 年数字无误
- [x] "jam in a sandwich" 为唯一引语；"founding father" 作页面叙述口径
- [x] Clarivate 2015（预测名单）与 VinFuture 2023 不与诺奖混写；Knight Bachelor 2024
- [x] nationalities UK rank0 + US rank1 口径
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/M._Stanley_Whittingham/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：优先本地 `images.txt` 中 2026 年照片；404 则装饰圆占位
- [ ] 国籍：封面顶部明示 英国/美国 双国籍行
- [ ] 引语核对：全文仅 "jam in a sandwich" 一处引号原话（页面明载）
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；化学式（TiS₂、LiAl、LiVOPO4）一律数学模式
- [ ] 与 Sanger 及 21 世纪批次既有格式对齐；与 Goodenough/Yoshino 两篇共享页口径互查
