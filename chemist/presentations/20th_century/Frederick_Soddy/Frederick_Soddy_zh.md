# Frederick Soddy（弗雷德里克·索迪）立传提示词

> qid=Q102830 · 1877-09-02 – 1956-09-22 · 英国放射化学家 · 20 世纪 · 诺贝尔化学奖（1921，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Frederick_Soddy/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页 + 气泡背景。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 就位后使用；无真实肖像则用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 同位素的命名者\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）——紫色圆点暗示「蜕变链上的原子」母题。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（现象 | 规则 | 意义）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——位移定律（α 衰减 Z−2 / β 衰减 Z+1）是天然公式框素材。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Frederick Soddy（中文惯称：弗雷德里克·索迪；FRS）
- **生卒**：1877-09-02 生于英格兰 Eastbourne（Sussex，6 Bolton Road）→ 1956-09-22 逝于英格兰 Brighton（Sussex），享年 79（79 岁生日后 20 天）
- **国籍**：United Kingdom（英国）
- **身份**：放射化学家（radiochemist；通才——化学、核物理、统计力学、金融、经济）
- **家庭**：父 Benjamin Soddy 为谷物商人，母 Hannah Green。1908 年娶 Winifred Moller Beilby（1885–1936，工业化学家 Sir George Beilby 之女），夫妇合作并于 1910 年合著镭 γ 射线吸收论文
- **教育轨迹**：Eastbourne College → University College of Wales, Aberystwyth → Merton College, Oxford（1898 年化学一等荣誉毕业；1898–1900 留校研究）
- **导师**：无博士学位（Oxford 本科毕业）；学术合作起点为 McGill 时期与 Ernest Rutherford 共事（frontmatter 列 Rutherford 为 doctoral advisor，但正文口径为"demonstrator 与 Rutherford 共事"，入库按 colleague 处理）
- **博士**：无
- **研究领域**：放射化学——放射性嬗变、同位素、位移定律；后期经济学（热经济学）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **东伯恩谷物商人之家（1877）**：商人之子，牛津 Merton 学院化学一等荣誉。
2. **麦吉尔与卢瑟福（1900–1903）**：任蒙特利尔 McGill 大学化学示教员（demonstrator），与 Rutherford 合作研究放射性——证明放射性是元素蜕变（transmutation）所致，原子嬗变确实发生，并伴随 α/β/γ 辐射。
3. **镭产生氦（1903）**：与 Sir William Ramsay 在 UCL 证明镭衰变产生氦气（薄壁玻璃封壳 + 真空球 + 光谱分析）——1907 年 Rutherford 与 Royds 进一步证明氦即 α 粒子（He²⁺）。
4. **格拉斯哥讲师（1904–1914）**：与助手 Ada Hitchins 在格拉斯哥与阿伯丁的工作证明铀衰变为镭。
5. **FRS（1910-05）**：当选皇家学会会士。
6. **位移定律（1913）**：α 发射使原子序数下移两位、β 发射上移一位；Kazimierz Fajans 几乎同时独立发现——合称 Fajans and Soddy displacement law。
7. **同位素的命名（1913）**：描述同一元素可有多个原子质量而化学性质相同的现象，命名为 isotope（"同一位置"）——词由 Margaret Todd 建议给索迪。
8. **镤的发现（1918）**：与苏格兰科学家 John Arnold Cranston 宣布发现后来命名为 protactinium（镤）的同位素——略晚于德国 Lise Meitner 与 Otto Hahn 的发现（后者 1915 年已发现但因 Cranston 战时笔记被锁而延迟公布）。
9. **《放射性释义》（1909）**：普及放射性新理解，成为 H. G. Wells 科幻小说 *The World Set Free*（1914，描绘原子弹轰炸的未来战争）的主要灵感来源——Wells 将小说题献给该书。
10. **牛津 Dr. Lee 化学教授（1919–1936）**：任首位 Dr. Lee's Professor of Chemistry，重组牛津实验室与化学教学大纲。
11. **1921 诺贝尔化学奖**：官方理由 "for his contributions to our knowledge of the chemistry of radioactive substances, and his investigations into the origin and nature of isotopes"；同年当选国际原子量委员会委员；诺奖演讲 1922-12-12 *The Origins of the Conception of Isotopes*。
12. **货币改革者（1921–1934）**：四部经济学著作主张以热力学定律审视经济——债务按复利指数增长而实体经济依赖不可再生的化石燃料存量；"货币改革"主张部分成为今天常规（放弃金本位、浮动汇率、财政工具、经济统计局），对部分准备金银行的批评则仍处主流之外，近年 IMF 论文重新激活其提案；《新帕尔格雷夫经济学词典》称其为"改革者"。
13. **业余几何与身后（1936）**：重新发现笛卡尔定理并以诗 "The Kiss Precise" 发表（相切圆称 Soddy circles）；另有 Soddy's hexlet；月球背面 Soddy 环形山与铀矿物 soddyite 以其命名；1956 年逝于 Brighton。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深紫 plumviolet） | `#46356B` | 蜕变链上的原子紫（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（嬗变 badgeTransmute） | `#2E5A9E` | 蓝放射性嬗变 / 与 Rutherford |
| 分类色 2（同位素 badgeIsotope） | `#1B7A43` | 绿同位素命名 / 位移定律 |
| 分类色 3（镤 badgePa） | `#D97B29` | 琥珀 protactinium / 铀→镭 |
| 分类色 4（经济学 badgeEcon） | `#C0395B` | 玫瑰货币改革 / 热经济学 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落）——紫色系圆点链状排布暗示「放射衰变链」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Daylight** — Alex-Productions（文件 `music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav`，勿复制 wav）
- **风格**：明亮 / 理性 / 略带人文温度
- **匹配理由**：
  - "明亮" 匹配"Daylight"与其揭示隐藏原子世界的意象——同位素让看不见的蜕变现形
  - "理性" 匹配其双栖气质——实验室的严谨与经济学的思辨
  - "人文温度" 匹配通才底色——从原子到货币，关怀始终是人
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 同位素的命名者 / Frederick Soddy 1877–1956 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  索迪的一生 — Sanger 式时间线（10 节点：1877→1898→1900→1903→1910→1913→1918→1919→1921→1956）
04  早年：东伯恩与牛津 (1877–1900) — 表格「时间|事件|结果」
05  麦吉尔与卢瑟福：放射性即嬗变 (1900–1903) — 表格「现象|证明|意义」+ 公式框：放射性 = 元素蜕变
06  镭产生氦 (1903) — 表格「合作|方法|结论」（薄壁封壳 + 光谱分析）
07  铀衰变为镭 (1904–1914) — 表格「地点|助手|成果」（Ada Hitchins）
08  位移定律 (1913) — 表格「发射|位移|独立发现」+ 公式框：α: Z−2 · β: Z+1（Fajans and Soddy law）
09  同位素命名 (1913) — 表格「现象|命名|词源」（isotope = "same place"；Margaret Todd）
10  镤的发现 (1918) — 表格「合作|对手|波折」（Cranston；Meitner & Hahn 优先；战时笔记）
11  1921 诺贝尔化学奖 — 表格「理由|演讲|同年」（官方英文理由原文；1922-12-12）
12  牛津与经济学 (1919–1936) — 表格「讲席|著作|主张」（Dr. Lee Professor；四部货币著作）
13  遗产：从原子到货币 — 四分类遗产盒（嬗变 / 同位素 / 镤 / 热经济学）+ Soddy circles + 月坑 soddyite
14  结尾 — 「同一种元素，不同的重量；同一位科学家，两个世界。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1921 诺奖口径 | 官方英文理由原文："for his contributions to our knowledge of the chemistry of radioactive substances, and his investigations into the origin and nature of isotopes"——**独享**；勿缩写或改写；诺奖演讲 1922-12-12 |
| 与 Rutherford 关系 | 正文口径：McGill 任**化学示教员与 Rutherford 共事**（worked with）；frontmatter 虽列 Rutherford 为 doctoral advisor，但索迪无博士学位——入库按 **colleague**，勿写成博士师承 |
| 镤优先权 | 索迪与 Cranston 1918 宣布**略晚于** Meitner 与 Hahn（后者 1915 已发现、公布延迟）——勿写索迪"首先发现镤" |
| 同位素词源 | isotope 一词由 **Margaret Todd** 建议给索迪——命名者是索迪、词源建议者是 Todd，勿混 |
| 镭产氦 1903 | 与 **Ramsay** 在 UCL 合作；1907 年 Rutherford 与 Royds 证明氦即 α 粒子——两步勿混 |
| 助手分工 | Ada Hitchins（多处明载，铀→镭证明，See also 专条）入库；Ruth Pirret 仅一句提及不入库 |
| 经济学表述 | 四部著作（1921–1934）主张与"当时被视为怪人"（roundly dismissed as a crank）的评价如实并置；IMF 论文"重新激活其提案"是近年事件 |
| 政治敏感（红线） | *Wealth, Virtual Wealth and Debt* 曾引用《锡安长老会纪要》、"有人指其反犹但亦有犹太友人/student 持正面看法"——立传中**一律不展开政治观点节**，货币改革主张仅作经济学内容客观简述；Ezra Pound 引语禁用 |
| "第一次/唯一" | 勿写"第一个证明嬗变""唯一"类断言；嬗变证明是 Soddy 与 Rutherford 的共同工作 |
| 阿伯丁与一战 | 1914 任阿伯丁教席，做与一战相关研究——一笔带过即可 |
| 引语红线 | 中文引号内不得出现无源"原话"；Wells 题献、诺奖理由为可溯源项 |
| 品牌口径 | 结尾页品牌写 `OpenMathAI`；引号半角 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q102830 | ✅ |
| name_zh | 弗雷德里克·索迪 | ✅ |
| name_en | Frederick Soddy | ✅ |
| birth_date | 1877-09-02 | ✅ |
| death_date | 1956-09-22 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | radiochemistry（person_field 细分见下表） | ✅ |

**person_field 细分（rank 表）**：

| name_en | rank | name_zh |
|---|---|---|
| radiochemistry | 0 | 放射化学 |
| isotope chemistry | 1 | 同位素化学 |
| nuclear physics | 2 | 核物理 |
| economics | 3 | 经济学 |

## 7. 社会关系入库清单

**同事 / 合作者 / 家人 / 影响对象**（★红线：只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Ernest Rutherford | 无向 | McGill 共事（1900–1903），共同证明放射性是元素嬗变；frontmatter 列其为博士导师但索迪无博士学位，按正文以 colleague 入库 |
| colleague | William Ramsay | 无向 | 1903 在 UCL 共同证明镭衰变产生氦 |
| colleague | Kazimierz Fajans | 无向 | 位移定律几乎同时独立发现（Fajans and Soddy law） |
| colleague | Ada Hitchins | 无向 | 格拉斯哥/阿伯丁研究助手，共同证明铀衰变为镭 |
| colleague | John Arnold Cranston | 无向 | 1918 共同宣布发现镤的同位素 |
| influence | H. G. Wells | 无向 | 索迪《放射性释义》(1909) 启发 Wells《The World Set Free》(1914) 并获题献 |
| other | Margaret Todd | 无向 | isotope（"同一位置"）一词的建议者 |
| spouse | Winifred Beilby | 无向 | 1908 结婚；1910 合著镭 γ 射线吸收论文；1936 年妻子去世 |

> 禁入库名单（metadata-only / 噪声防入）：Ruth Pirret（格拉斯哥研究助手，仅一句提及）、Lise Meitner 与 Otto Hahn（镤发现优先权叙事中的对手方，无直接社会关系）、J. J. Thomson（非放射性元素同位素的后续证明者，仅一句提及）、Thomas Royds（Rutherford 团队成员）、Henry Ford / Ezra Pound（政治节引用链，不入库）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1921，独享）
- Fellow of the Royal Society（1910-05 当选）
- International Atomic Weights Committee 委员（1921）
- 月球背面 Soddy 环形山、铀矿物 soddyite 以其命名
- 《新帕尔格雷夫经济学词典》收录为货币"改革者"

## 9. 机构清单

- 教育：Eastbourne College → University College of Wales, Aberystwyth → Merton College, Oxford（1898 化学一等荣誉；1898–1900 校内研究）
- 任职：McGill University 化学示教员（1900–1903）→ University College London（1903，与 Ramsay）→ University of Glasgow 讲师（1904–1914）→ University of Aberdeen 教席（1914–1919）→ University of Oxford 首任 Dr. Lee's Professor of Chemistry（1919–1936）
- 身后：Frederick Soddy Trust（soddy.org）

## 10. 终审清单

- [ ] 生卒 1877-09-02 / 1956-09-22，享年 79，出生地 Eastbourne、去世地 Brighton
- [ ] 1921 独享；获奖理由英文原文完整引用；诺奖演讲 1922-12-12
- [ ] 与 Rutherford 按 colleague 口径（无博士学位）；与 Ramsay 1903 合作
- [ ] 位移定律（α: Z−2 / β: Z+1）与 Fajans 独立发现；同位素命名与 Margaret Todd 词源
- [ ] 镤 1918 与 Meitner/Hahn 优先权表述准确
- [ ] 政治节红线：货币改革客观简述、政治引用一律不展开
- [ ] 引语全部可在 page.md 溯源，无源处一律间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Frederick_Soddy/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像就位（page.md 实载 "Soddy in 1921" 照片）或装饰圆占位
- [ ] **国籍**：封面顶部明示英国
- [ ] **引语核对**：引语必须在 page.md 原文找到，否则改间接转述
- [ ] **敏感项**：政治节红线逐字复核
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox<10pt、hbox<50pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger）对齐

---

> **名单状态**：本提示词由 chem-batch-02 批次生成；`chemist/generate_20th_century_list.py` 由主控统一收尾，勿改动。
