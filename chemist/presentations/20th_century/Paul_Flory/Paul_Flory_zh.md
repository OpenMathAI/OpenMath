# Paul Flory（保罗·弗洛里）立传提示词

> qid=Q176351 · 1910-06-19 – 1985-09-09 · 美国化学家 · 诺贝尔化学奖（1974，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Paul_Flory/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 公式展示框。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像按 `images.txt` 就位；page.md 页首有 "Flory in 1973" 照片，如已下载则用真实肖像；否则装饰圆占位并如实标注）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{link}\enspace 高分子链的统计学家\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育（Manchester/Ohio State）、博士（导师/论文）、家庭（妻 Emily Tabor）、核心领域、机构、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「无规线团 / 高分子链段」母题——大小错落的圆点暗示链段的随机行走。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如「Flory–Huggins 溶液理论」「theta 点：排除体积效应被中和」。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Paul John Flory（中文惯称：保罗·约翰·弗洛里）
- **生卒**：1910-06-19 生于伊利诺伊州 Sterling → 1985-09-09 逝于加州 Big Sur（心梗后离世），享年 75
- **国籍**：United States（美国）
- **身份**：化学家（chemist；高分子物理化学奠基人之一；1974 诺贝尔化学奖独享得主）
- **家庭**：父 Ezra Flory 为牧师-教育者（clergyman-educator），母 Martha Brumbaugh（娘家姓）为学校教师；先祖为德裔胡格诺派，可追溯至阿尔萨斯。1936 年娶 Emily Catherine Tabor，三子女：Susan Springer、Melinda Groom、Paul John Flory, Jr.；妻 Emily 2006 年去世，享年 94
- **教育轨迹**：
  - 1927 Elgin High School 毕业
  - 1931 Manchester College（印第安纳，今 Manchester University）学士——化学系教授 Carl W Holl 点燃科学兴趣
  - 俄亥俄州立大学：先在 Cecil E Boord 指导下读一年有机化学硕士，后转物理化学
- **导师**：Herrick L. Johnston（俄亥俄州立大学博士导师）
- **博士**：1934，一氧化氮光化学（photochemistry of nitric oxide）
- **研究领域**：高分子物理化学（physical chemistry of polymers）——溶液理论、排除体积、凝胶化、链构象

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **牧师之家与胡格诺血统（1910）**：Sterling 小城，牧师-教育者父亲与教师母亲——教育气质的底色。
2. **Manchester 学院（1927–1931）**：Carl W Holl 的化学课点燃志向——小学院的起点。
3. **俄亥俄州立：转向物理化学（1931–1934）**：Boord 门下一年有机化学硕士，后师从 Johnston 做一氧化氮光化学，1934 获 PhD。
4. **DuPont 与 Carothers（1934–1937）**：加入杜邦中央研究部，与尼龙发明人 Wallace Carothers 共事——聚合动力学的起点。
5. **缩聚动力学革命**：挑战"链增长末端基团反应性随分子变大而降低"的假设，论证**反应性与链长无关**，推出链数随尺寸指数下降——聚合动力学的定量基础。
6. **链转移概念**：在加聚中引入 chain transfer，修正动力学方程、厘清聚合度分布的难题。
7. **辛辛那提与凝胶化理论（1937–1940）**：Carothers 1937 年去世后转 Basic Science Research Laboratory；发展多官能度化合物聚合的数学理论与聚合物网络/凝胶理论——**Flory–Stockmayer 凝胶化理论**，等价于 Bethe 格上的渗流（percolation），是该领域**第一篇论文**。
8. **Standard Oil 与合成橡胶（1940–1943）**：入 Standard Oil Development 公司 Linden 实验室，发展聚合物混合物的统计力学理论；二战合成橡胶需求下效力 Esso 实验室。
9. **固特异岁月（1943–1948）**：任 Goodyear 聚合物基础研究组组长。
10. **Cornell 与《Principles of Polymer Chemistry》（1948–1953）**：1948 年春应 Peter Debye 邀请主讲 George Fisher Baker 讲座，同年秋入职康奈尔；把 Baker 讲座提炼成 1953 年康奈尔大学出版社《Principles of Polymer Chemistry》——领域标准教科书，沿用至今。
11. **排除体积与 theta 点**：把 Kuhn（1934）提出的 excluded volume 概念引入高分子——长链分子两端平均距离因此变远；提出 theta 点（theta solvent）使排除体积效应被中和、链回归理想链行为——概念性突破。
12. **理论与方程的命名性成果**：Flory–Huggins 溶液理论、Flory 指数、Flory convention（笛卡尔→广义坐标转换）、Flory–Fox 方程、Flory–Rehner 方程、Flory–Schulz 分布、Flory–Stockmayer 理论、星形聚合物、自避行走——命名性成果贯穿高分子科学。
13. **Stanford 晚年与 1974 诺奖（1961–1985）**：1957 迁匹兹堡任 Mellon Institute 研究执行总监，1961 就任斯坦福化学系教授；退休后仍在斯坦福与 IBM 主持实验室。1974 诺贝尔化学奖独享，理由 "for his fundamental achievements, both theoretical and experimental, in the physical chemistry of macromolecules"；同年获 National Medal of Science（福特总统颁）与 Priestley Medal。1985-09-09 心梗后逝于 Big Sur；2002 年追授入 Alpha Chi Sigma 名人堂。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深青 teal） | `#0E4D64` | 高分子溶液的深青——统计力学的沉静（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（聚合动力学 badgeKinet） | `#1B7A43` | 绿缩聚 / 链转移 |
| 分类色 2（凝胶化理论 badgeGel） | `#D97B29` | 琥珀 Flory–Stockmayer / 渗流 |
| 分类色 3（溶液理论 badgeSolution） | `#1E4E79` | 蓝排除体积 / theta 点 / Flory–Huggins |
| 分类色 4（教科书遗产 badgeBook） | `#C0395B` | 玫瑰《Principles of Polymer Chemistry》 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「无规线团 / 链段随机行走」的统计意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Falling Apart** — Michael FK & Andy Leech（文件 `03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav`）
- **风格**：情感钢琴 / 弦乐渐入 / 内省
- **匹配理由**：
  - "Falling Apart" 的标题反向借用——Flory 的全部工作正是回答"链与凝胶何时散架、何时成形"（凝胶点即"散架/交联"的临界）
  - 内省钢琴匹配其理论家的沉静气质——从工业实验室走出的数学化化学
  - 渐入弦乐匹配从 DuPont 车间到 1974 诺奖的漫长积累
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 高分子链的统计学家 / Paul Flory 1910–1985 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍/教育/博士/导师/家庭/领域/荣誉）
03  弗洛里的一生 — Sanger 式时间线（10 节点：1910→1931→1934→1937→1940→1943→1948→1953→1961→1974/1985）
04  牧师之家与 Manchester (1910–1931) — 表格「时间|事件|结果」（Holl 的化学课）
05  俄亥俄州立：光化学博士 (1931–1934) — 表格「阶段|导师|成果」+ 公式框：NO 光化学
06  DuPont：与 Carothers 共事 (1934–1937) — 表格「问题|方法|结果」+ 公式框：反应性与链长无关 → 指数分布
07  链转移与凝胶化理论 (1937–1943) — 表格「对象|理论|意义」+ 公式框：Flory–Stockmayer = Bethe 格渗流
08  战时工业化学 (1940–1948) — 表格「机构|课题|贡献」（Standard Oil / Goodyear）
09  Cornell 与《Principles》(1948–1953) — 表格「契机|著作|影响」（Debye 邀请 / Baker 讲座）
10  排除体积与 theta 点 — 表格「概念|机制|意义」+ 公式框：theta 点 = 排除体积被中和
11  命名性方程墙 — Flory–Huggins / Flory 指数 / Flory convention / Flory–Fox / Flory–Rehner / Flory–Schulz
12  Stanford 与 1974 诺贝尔化学奖 — 独享 + 授奖理由英文原文框 + National Medal of Science
13  荣誉清单 — Sanger 式「类别|代表|意义」表格（Priestley 1974 / NAS 1953 / AAAS 1957 等）
14  结尾 — 「链有多长、如何蜷曲、何时结网——统计力学给出了高分子的语法。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 死亡日期双值 | frontmatter date_of_death = ["1985-09-09", "1985-09-08"]；**infobox 与正文均作 September 9, 1985**——取 1985-09-09，勿取 09-08 |
| 1974 诺奖理由 | 官方原句（page.md 两处实载）"for his fundamental achievements, both theoretical and experimental, in the physical chemistry of macromolecules"——**1974 独享**，勿写共享 |
| National Medal of Science 理由 | 因 "formation and structure of polymeric substances" 研究、由福特总统颁发、物理科学类——年份 1974 与诺奖同年，勿混淆两者理由 |
| 排除体积归属 | excluded volume 概念由 **Werner Kuhn 于 1934 提出**，Flory 是将其**引入高分子领域**——勿写"Flory 发明排除体积" |
| 渗流地位 | Flory–Stockmayer 理论"等价于 Bethe 格上的渗流，是渗流领域第一篇论文"（page.md 明载）——表述限定在 Bethe 格，勿写成"发明渗流理论" |
| Carothers 关系 | Flory 1934 入 DuPont "working with Wallace Carothers"；Carothers 1937 去世后 Flory 转辛辛那提——同事关系，勿写师承（Carothers 非 infobox 导师） |
| 博士前史 | 俄亥俄州立先在 **Cecil E Boord** 门下读一年有机化学硕士，后转物理化学师从 **Herrick L. Johnston**——两位导师角色勿混（infobox 只列 Johnston 为 doctoral advisor） |
| 教科书年份 | 《Principles of Polymer Chemistry》1953 年康奈尔大学出版社；《Statistical Mechanics of Chain Molecules》1969；《Selected Works》1985——书单照录勿提前 |
| 机构口径 | workplaces（infobox）：DuPont、Stanford、Carnegie Mellon、Cornell；正文另有 Mellon Institute（1957–1961，executive director of research）与 Standard Oil/Goodyear——infobox 与正文合并叙述，勿漏 Mellon 阶段 |
| 妻子去世 | Emily Catherine Tabor 2006 年去世（享年 94）——"posthumously inducted" 指 Flory 2002 年追授 Alpha Chi Sigma 名人堂，勿张冠李戴 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q176351 | ✅ |
| name_zh | 保罗·弗洛里 | ✅ |
| name_en | Paul Flory | ✅ |
| birth_date | 1910-06-19 | ✅ |
| death_date | 1985-09-09（双值取 infobox/正文） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | polymer science / physical chemistry（person_field 细分见下表，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | polymer chemistry | 高分子化学 |
| 1 | polymer physics | 高分子物理 |
| 2 | physical chemistry | 物理化学 |
| 3 | solution theory | 溶液理论 |

## 7. 社会关系入库清单

**红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Herrick L. Johnston | 师→生（direction=advisor） | 俄亥俄州立博士导师，1934 一氧化氮光化学论文 |
| advisor-student | Cecil E Boord | 师→生（direction=advisor） | 俄亥俄州立硕士阶段有机化学指导（正文实载） |
| colleague | Wallace Carothers | 无向 | 1934–1937 DuPont 共事，聚合动力学起点 |
| colleague | Peter Debye | 无向 | 1948 受其邀请主讲康奈尔 Baker 讲座，同年入职康奈尔 |
| influence | Werner Kuhn | 无向 | 排除体积概念由 Kuhn 1934 提出，Flory 将其引入高分子领域 |
| spouse | Emily Catherine Tabor | 无向 | 1936 结婚，三子女 |

> 禁入库名单：Carl W Holl（本科启发者，非白名单关系类型）、Ezra Flory / Martha Brumbaugh（父母——正文实载，如需可补 parent-child 两行；本表默认不收以控制噪声）、Gerald Ford（仅颁奖礼仪场合）、Alpha Chi Sigma（组织非人）——均不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1974，独享）
- National Medal of Science（1974，物理科学类，福特总统颁发；理由 "formation and structure of polymeric substances"）
- Priestley Medal（1974）；Golden Plate Award of the American Academy of Achievement（1974）
- William H. Nichols Medal（1962）；Colwyn medal（1954）
- Charles Goodyear Medal（1968）；Elliott Cresson Medal（1971）
- Peter Debye Award in Physical Chemistry（1969）
- Perkin Medal（1977）；Carl-Dietrich-Harries-Medal（1977）
- Willard Gibbs Award；Polymer Physics Prize；Chemical Pioneer Award；Herman Mark Award in Polymer Chemistry（metadata.json 明载）
- 院士：United States National Academy of Sciences（1953 当选）；American Academy of Arts and Sciences（1957 当选）；Fellow of the American Physical Society（metadata.json 明载）
- 追授：Alpha Chi Sigma Hall of Fame（2002）

## 9. 机构清单

- 教育：Elgin High School（至 1927）、Manchester College（1931 学士）、Ohio State University（1934 PhD）
- 任职：DuPont 中央研究部（1934–1937，Carothers 组）→ University of Cincinnati Basic Science Research Laboratory（1937–约1939/1940）→ Standard Oil Development Company Linden 实验室（1940–1943；战时 Esso 合成橡胶）→ Goodyear Tire and Rubber Company（1943–1948，聚合物基础组负责人）→ Cornell University（1948–1956 教授；1948 Baker Lectures）→ Mellon Institute of Industrial Research（1957–1961，研究执行总监，匹兹堡）→ Stanford University 化学系教授（1961 起；退休后仍主持斯坦福与 IBM 实验室）

## 10. 终审清单

- [ ] 生卒 1910-06-19 / 1985-09-09（双值裁定），享年 75；出生地 Sterling、去世地 Big Sur
- [ ] 1974 独享表述准确；授奖理由英文原句照录
- [ ] 排除体积归 Kuhn 提出、Flory 引入高分子——归属正确
- [ ] Flory–Stockmayer = Bethe 格渗流、渗流领域第一篇论文——表述限定正确
- [ ] Boord（硕士有机）/ Johnston（博士物理化学）两导师角色不混
- [ ] Carothers=同事非导师
- [ ] 引语全部可在本地 Wikipedia 原文找到；无直接引语时不出现引号原话
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Paul_Flory/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 `images.txt` 核对肖像（页首 "Flory in 1973" 照片）；无真实肖像用装饰圆占位并如实标注
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：授奖理由两条英文原句外，本页无其他直接引语，一律间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐；命名性方程墙页公式排版专项检查
