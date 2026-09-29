# Demis Hassabis（德米斯·哈萨比斯）立传提示词

> qid=Q3022141 · 1976-07-27 生于伦敦（在世） · 英国人工智能研究者与企业家 · 21 世纪 · 诺贝尔化学奖（2024，与 John M. Jumper 共享另一半——蛋白质结构预测 AlphaFold；Baker 独得另一半）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Demis_Hassabis/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**对齐 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。肖像用 `images.txt` 实照 `Demis_Hassabis,_2024_Nobel_Prize_Laureate_in_Chemistry_6.jpg`（2024 诺贝尔周单人照，250px 改 500px 下载，`curl -A "Mozilla/5.0"` + `file` 验证；另一张 PhotonQ 2014 与 Agüera y Arcas 合照不用）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{brain}\enspace` 从游戏到生命的智能求索者`\enspace·\enspace` 英国），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Sir Demis Hassabis CBE FRS FREng FRSA）、国籍、出生地、教育（Cambridge/UCL）、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「神经网络 / 棋盘」母题——错落圆点即神经元连接或棋盘上的落子。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——核心页呈现 AlphaFold 的 CASP14 战绩（GDT 87.0 / 误差 < 1 Å / 2 亿蛋白结构库）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Sir Demis Hassabis（CBE FRS FREng FRSA；中文惯称：德米斯·哈萨比斯；原姓 Hassapis，希腊文 Χασάπης，意为"屠夫"，后按 Ingo Althöfer 的说法"执行了一个点突变"把 p 改成 b）
- **生卒**：1976-07-27 生于伦敦（在世，页面无卒日）
- **国籍**：United Kingdom（英国）
- **身份**：AI 研究者与企业家；Google DeepMind 联合创始人兼董事长、Alphabet 首席科学家（2026 起）、Isomorphic Labs 联合创始人兼 CEO；英国政府 AI 顾问；2024 诺贝尔化学奖得主（与 Jumper 共享另一半）
- **家庭**：父 Costas（希腊塞浦路斯裔，家中第一个上大学的人，波西米亚自由灵魂，卖玩具为生的唱作人）；母 Angela（新加坡华裔，幼年孤儿，学护理，做零售与兼职清洁）；北伦敦长大；弟弟中仍有一人保留原姓 Hassapis；家人现居北伦敦；利物浦 FC 终身球迷；懂一些希腊语并以此自豪
- **教育轨迹**：
  - Queen Elizabeth's School, Barnet（1988–1990）；父母家庭教育一年；Christ's College, Finchley（16 岁提前两年考完 A-level）
  - Queens' College, Cambridge：Computer Science Tripos，1997 双一等（double first）毕业
  - UCL Queen Square Institute of Neurology：认知神经科学 PhD（2009），论文 Neural Processes Underpinning Episodic Memory
- **导师**：Eleanor Maguire（博士导师）
- **研究领域**：artificial intelligence / machine learning / neuroscience / computer science

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **国际象棋神童（4 岁–13 岁）**：4 岁看父亲与舅舅对弈学会下棋；13 岁达大师标准（Elo 2300），多次率英格兰少年队；剑桥 1995–1997 三度出战牛津-剑桥对抗赛。
2. **ZX Spectrum 与自学编程（1984）**：用棋赛奖金买下第一台电脑，照书自学编程；在 Amiga 上写出第一个 AI 程序（下黑白棋 reversi）。
3. **Bullfrog 与 Theme Park（gap year）**：凭 Amiga Power 比赛赢得工作，17 岁与 Peter Molyneux 共同设计并主写 1994 年《Theme Park》——数百万销量；拒绝七位数挽留，gap year 挣足大学学费。
4. **剑桥双一等（1997）**：Queens' College 计算机科学 Tripos 双一等毕业。
5. **Lionhead 与 Elixir（1998–2005）**：Lionhead 主写《Black & White》AI；1998 创办 Elixir Studios（《Republic: The Revolution》Metacritic 62、《Evil Genius》75，两获 BAFTA 配乐提名），2005 年 4 月出售 IP 关闭工作室。
6. **重返学院：认知神经科学 PhD（2005–2009）**：UCL Queen Square 神经病学研究所，师从 Eleanor Maguire——想从人脑为新算法找灵感。
7. **海马与想象（PNAS 首作，★关键）**：首次系统证明海马损伤（失忆）患者同样无法想象新经历——建立想象的建构过程与情景记忆重构过程的联系；提出 scene construction（场景构建）理论；入选 Science 年度十大科学突破（2007）。
8. **MIT/哈佛访问科学家与 Gatsby 博士后（2009）**：MIT Tomaso Poggio 实验室与哈佛联合访问；Henry Wellcome 博士后奖学金入 UCL Gatsby 计算神经科学单元，与 Peter Dayan 共事。
9. **创办 DeepMind（2010）**：与 Shane Legg（Gatsby 博士后同事）、Mustafa Suleyman（家族世交）共同创立；使命是 "solve intelligence" 再用它 "to solve everything else"；招入大学同窗 David Silver；2013 年 12 月 DQN 以原始像素超人类玩 Atari。
10. **谷歌收购与 AlphaGo（2014–2017）**：2014 Google 以 4 亿英镑收购；AlphaGo 2015-10 5–0 胜欧洲冠军 Fan Hui、2016-03 4–1 胜李世石、2017 3–0 胜当时世界第一柯洁。
11. **AlphaFold：50 年大挑战（2016–2021，★核心）**：CASP13（2018）43 题中 25 题最准；CASP14（2020-11）自由建模类中位 GDT 87.0、整体误差小于一个原子宽度（<1 Å），主办方宣布问题基本解决；次年折叠科学界已知全部 2 亿蛋白并联合 EMBL-EBI 开放 AlphaFold 蛋白结构数据库；"This is a lighthouse project..."（对 The Guardian）。
12. **Isomorphic Labs 与 2026 转岗**：2021 创办 Isomorphic Labs 任 CEO；2024–2026 由 DeepMind CEO 转任 Alphabet 首席科学家（页面：served as CEO until 2026）。
13. **荣誉大满贯与 2024 诺贝尔化学奖**：与 John M. Jumper 共享 2024 化学奖另一半（"AI 对蛋白质结构预测的研究贡献"口径）；2024 因 AI 服务获封 Knight Bachelor；2017 CBE；FRS（2018）；Lasker/Gairdner/Breakthrough/BBVA（2022，与 Bengio/Hinton/LeCun 共享）/Asturias 等；Science 年度十大突破四次上榜（2007/2016/2020/2021，2021 为年度之冠）；2025 入选 Time 100 并以 "Architects of AI" 群体当选 Time 年度人物。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（钢蓝 steelblue） | `#37548D` | DeepMind 深度网络的冷静钢蓝（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（游戏与棋 badgeGame） | `#B3462E` | 橙红棋盘落子 / Theme Park |
| 分类色 2（神经科学 badgeNeuro） | `#2E7D4F` | 绿海马体 / 场景构建 |
| 分类色 3（AlphaGo badgeGo） | `#1E5E8C` | 青蓝 19 路棋盘上的搜索树 |
| 分类色 4（AlphaFold badgeFold） | `#8C2F5B` | 玫红蛋白折叠 / CASP14 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「神经网络」——层层连接的神经元圆点。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions（源文件 `music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav`，执行时软链/复制至本目录，不复制 wav 入库）
- **风格**：时间流动 / 钢琴弦乐 / 多幕剧式推进
- **匹配理由**：
  - "时间之流" 匹配其四幕人生——棋童 → 游戏天才少年 → 神经科学家 → AI 领航员，每一幕都是"换赛道重新伟大"
  - 多幕剧推进匹配叙事结构——从 ZX Spectrum 到 AlphaFold 的四十年压缩在 15 页里
  - 收束感匹配化学奖的"跨界认证"——时间最终把游戏少年送进了诺贝尔化学奖的殿堂
- **时长**：执行时用 ffprobe 核对 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 从游戏到生命的智能求索者 / Demis Hassabis 1976– + 四色 badge + 右上头像 + 国籍行（英国）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名与头衔/国籍/出生地/教育/博士导师/领域/荣誉）
03  哈萨比斯的一生 — 时间线（10 节点：1976→1984→1994→1997→1998→2009→2010→2014→2020→2024/2026）
04  神童岁月：棋盘与 ZX Spectrum (1976–1997) — 表格「时间|事件|结果」
05  游戏业双子星：Theme Park 与 Black & White — 表格「作品|角色|结果」
06  Elixir 创业与关闭 (1998–2005) — 表格「决策|作品|结果」（拒绝七位数→创业→关闭→转身）
07  神经科学：海马与想象 (2005–2009) — 表格「问题|发现|结果」+ 公式框：情景记忆 ↔ 想象（scene construction）；Science 2007 十大突破
08  创办 DeepMind (2010) — 表格「人物|角色|结果」（Legg/Suleyman/Silver）；使命 "solve intelligence"
09  AlphaGo 三战 (2015–2017) — 表格「对手|比分|意义」（Fan Hui 5-0 / 李世石 4-1 / 柯洁 3-0）
10  AlphaFold：50 年大挑战 (2016–2021，★核心) — 表格「赛事|成绩|意义」+ 公式框：CASP14 GDT 87.0 / <1 Å / 2 亿结构
11  2024 诺贝尔化学奖 — 流程图：Baker（设计，一半）‖ Hassabis+Jumper（AlphaFold，一半）
12  荣誉清单 — 「类别|代表|意义」表格 + itemize（CBE 2017→FRS 2018→Lasker/Gairdner 2023→Nobel 2024→爵士 2024→Time POTY 2025）
13  Isomorphic Labs 与 AGI 议程 — 表格「方向|内容|结果」（AI 安全声明照实写 / "lighthouse project" 引语）
14  结尾 — 「先求解智能，再用智能求解一切。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2024 诺奖结构 | Hassabis 与 **John M. Jumper 共享另一半**（AlphaFold/蛋白质结构预测）；**Baker 独得另一半**（计算蛋白质设计）——勿写"三人平分"或"与 Baker 共享" |
| 获奖理由口径 | 页面口径 "for their AI research contributions to protein structure prediction"（对蛋白质结构预测的 AI 研究贡献）；官方理由（主控任务单）"for protein structure prediction"（与 Jumper 同一理由）——全篇统一"蛋白质结构预测"，勿写"计算蛋白质设计"（那是 Baker 的一半） |
| 姓氏变更 | 原姓 Hassapis → Hassabis（"point mutation" p→b，系 Ingo Althöfer 说法的转述）——按页面口径写并注明出处人；勿写"改姓原因"之外的脑补 |
| 头衔年份 | CBE 授予名单是 **2018 New Year Honours**（页面 list 作 2017 行）；Knight Bachelor 在 **2024**（"services to artificial intelligence"）——两处勿混 |
| CEO 转岗 | DeepMind CEO "until 2026"，2026 成为 Alphabet 首席科学家——如按 2026 年口径写需注明"2026 起" |
| AlphaGo 比分 | Fan Hui 5–0（2015-10）、Lee Sedol 4–1（2016-03）、Ke Jie 3–0（2017）——比分与顺序勿颠倒 |
| CASP14 数字 | 中位 GDT **87.0**（自由建模类）、2018 CASP13 中位 GDT <60、误差 <1 Å、2 亿蛋白结构、与 EMBL-EBI 合作开放数据库——数字照页面，勿夸大 |
| 引语白名单 | 仅可引页面明载："solve intelligence" / "to solve everything else"（DeepMind 使命）、"This is a lighthouse project, our first major investment..."（对 The Guardian）、灭绝风险声明 "Mitigating the risk of extinction from AI should be a global priority alongside other societal-scale risks such as pandemics and nuclear war"（2023 签署）、"one of the most beneficial technologies of mankind ever"（预测）——其余一律间接转述 |
| AI 风险口径 | 签署灭绝风险声明、主张 AI 安全研究、但认为暂停 AI 进步难以执行且收益值得继续——三句照页面并置，勿只取一面 |
| Elixir 结局 | 2005-04 出售 IP 并关闭工作室、Republic 评分 62/Evil Genius 75——照实写，不美化 |
| 母亲背景 | 新加坡华裔、幼年孤儿、学护理做零售——页面明载可写，但注意措辞客观简洁，不加渲染 |
| 页面无载禁写 | 页面无其配偶/婚姻记录（Personal life 无配偶信息）——**禁写配偶关系**；无子女；无 Jumper 相识过程细节 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q3022141 | ✅ |
| name_zh | 德米斯·哈萨比斯 | ✅ |
| name_en | Demis Hassabis | ✅ |
| birth_date | 1976-07-27 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | artificial intelligence researcher | ✅ |
| field_of_work | artificial intelligence（person_field 细分：artificial intelligence / machine learning / neuroscience / computer science / protein structure prediction，带 rank） | ✅ |
| has_biography | false（Beamer 立传完成后再置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 学术同事**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Eleanor Maguire | 师→生（博士导师） | UCL Queen Square 认知神经科学博士导师（2009） |
| advisor-student | Peter Dayan | 师→生（博士后导师） | UCL Gatsby 计算神经科学单元博士后（Henry Wellcome Fellowship） |
| colleague | Tomaso Poggio | 无向 | MIT 实验室访问科学家（与哈佛联合） |

**DeepMind 创业伙伴**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Shane Legg | 无向 | DeepMind 联合创始人；Gatsby 博士后时期结识 |
| colleague | Mustafa Suleyman | 无向 | DeepMind 联合创始人；家族世交 |
| colleague | David Silver | 无向 | 剑桥大学同窗与 Elixir 合伙人，后招入 DeepMind；AlphaGo 核心人物；库内已有记录（id=1871，Sutton 博士生） |

**共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | John M. Jumper | 无向 | 2024 诺贝尔化学奖共同得主（AlphaFold，共享另一半）；规范名 John M. Jumper（下一批入库时回填 QID） |
| co-honored | Yoshua Bengio | 无向 | 2022 Princess of Asturias Award（Technical and Scientific Research）共同得主；库内已有记录（id=279） |
| co-honored | Geoffrey Hinton | 无向 | 2022 Princess of Asturias Award 共同得主；库内已有记录（id=280） |
| co-honored | Yann LeCun | 无向 | 2022 Princess of Asturias Award 共同得主；库内已有记录（id=281） |

> metadata.json `doctoral_advisor` 与正文一致（Maguire）；occupations 字段极长（chess player/poker player 等）——**从严不入库**（不建 other 关系）。
> 无配偶/子女载录——禁写。Lee Sedol/Fan Hui/Ke Jie 是对弈对手，非社会关系——禁写。
> 注：Maguire/Dayan/Poggio/Legg/Suleyman/Jumper 均为库内新建 stub，按本表规范全名建；Bengio/Hinton/LeCun/Silver 复用库内既有记录。

## 8. 奖项清单（择要，全清单见页面 Awards and honours 节）

- Nobel Prize in Chemistry（2024，与 John M. Jumper 共享另一半，蛋白质结构预测）
- Mullard Award（2014，Royal Society）；Royal Academy of Engineering Silver Medal（2016）；Nature's 10（2016）
- CBE（2018 New Year Honours 名单，"services to Science and Technology"）；FRS（2018）；FREng（2017）；FRSA（2009）
- Dan David Prize – Future Award（2020）
- BBVA Foundation Frontiers of Knowledge Award（2022，"Biology and Biomedicine"）
- Princess of Asturias Award for Technical and Scientific Research（2022，与 Bengio/Hinton/LeCun 共享）
- Wiley Prize in Biomedical Sciences（2022）
- BCS Lovelace Medal（2023）；Albert Lasker Award for Basic Medical Research（2023）；Canada Gairdner International Award（2023）；Breakthrough Prize in Life Sciences（2023，AlphaFold）
- Clarivate Citation Laureates（2024）；Keio Medical Science Prize（2024）；Knight Bachelor（2024，"services to artificial intelligence"）
- Time 100（2017、2025）；Time 年度人物 "Architects of AI" 群体（2025）；NAE 国际院士（2026）；RSA Albert Medal（2026）
- Science 年度十大突破：2007/2016/2020 上榜、2021 年度之冠（AlphaFold v2）；DeepMind 九登 Nature 封面、一登 Science 封面

## 9. 机构清单

- 教育：Queen Elizabeth's School, Barnet（1988–1990）；家庭教育一年；Christ's College, Finchley（A-level 16 岁）；Queens' College, Cambridge（CS Tripos，1997 double first）；UCL Queen Square Institute of Neurology（PhD 2009）
- 任职：Bullfrog Productions（gap year）；Lionhead Studios（–1998）；Elixir Studios（1998–2005，创始人）；UCL（2009–2012，Gatsby 博士后与访学）；MIT/哈佛（联合访问科学家）；DeepMind（2010–，联合创始人；2014 被 Google 4 亿英镑收购后保留伦敦主体；CEO until 2026）；Isomorphic Labs（2021–，联合创始人兼 CEO）；Alphabet 首席科学家（2026 起）；UK Government AI Adviser；Francis Crick Institute 科学顾问委员会（2016）
- 荣誉学位：Imperial College London（2018）、EPFL（2023）、University of Oxford（2024）等

## 10. 终审清单

- [ ] 生卒 1976-07-27 伦敦（在世）；父母背景照实、措辞客观
- [ ] 姓氏 Hassapis→Hassabis 按 Althöfer 转述口径写
- [ ] 博士导师 Maguire / 博士后 Dayan / MIT 访学 Poggio 三轨清晰
- [ ] AlphaGo 三战比分与时间顺序准确；CASP14 数字（GDT 87.0 / <1 Å / 2 亿）无误
- [ ] 2024 诺奖"与 Jumper 共享另一半"口径准确；Baker 独得另一半
- [ ] 引语全部在引语白名单内（使命/灯塔/灭绝风险/受益技术四条）；无编造引语
- [ ] CBE 名单年份（2018 New Year Honours）与骑士册封（2024）不混
- [ ] `make distclean && make` 编译通过，0 错误，vbox≤10pt / hbox≤50pt

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Demis_Hassabis/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：下载 images.txt 的 2024 诺贝尔周单人照（勿用 2014 合照）
- [ ] 国籍：封面明示"英国"
- [ ] 引语核对：四条引语须在页面原文找到，其余为间接转述
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox≤10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；头衔缩写（CBE FRS FREng FRSA）与 Sir 称谓的呈现层级
- [ ] 与化学家侧既有格式对齐；结尾品牌 OpenMathAI

---

> **名单状态**：`chemist/generate_21th_century_list.py` 更新由主控统一收尾，本文件不改动生成器。
