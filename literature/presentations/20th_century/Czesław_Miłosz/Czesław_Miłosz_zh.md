# 文学家立传提示词（OpenLiterature：Czesław Miłosz）

> **本文件是 OpenLiterature 的人物专属立传提示词**，以 Kenneth G. Wilson（OpenPhysicist 模板标杆）为骨架，适配文学家。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分为 Miłosz 定制内容。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist/OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合 OpenPhysicist 标杆（Kenneth G. Wilson 提示词 + tex 结构）与文学家侧实战经验。
- **本实例**：Czesław Miłosz（切斯瓦夫·米沃什），1980 诺贝尔文学奖得主，二十世纪流亡良知的证言者。
- **设计哲学**：文学家立传**没有公式框——以代表作书影 / 名句引文框 / 意象图式替代**；仍须保留「身份信息页」与「文学领域」的结构化表达。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Czesław Miłosz（1911-06-30 ~ 2004-08-14，享年 93 岁）
- **气质关键词**：**被俘心灵的解缚者、历史的见证诗人、立陶宛-波兰-美国的三重边界行走者** —— 1980 诺贝尔文学奖获奖理由：
  > "who with uncompromising clear-sightedness voices man's exposed condition in a world of severe conflicts"
  > （表彰其以毫不妥协的清明，道出人在严酷冲突的世界中毫无遮蔽的境况）
- **设计母题**：**见证与边界（witness and borders）**。生于俄帝国考纳斯省的波兰贵族之家，历经两次大战、纳粹占领、华沙起义、斯大林主义与麦卡锡主义，最终在伯克利与克拉科夫之间安放晚年——版式语言宜用界线、地图轮廓与灰暗底色上的光斑，呼应「在严酷冲突的世界中道出无遮蔽境况」的诗学。
- **本地数据源**：`literature/presentations/pages/20th_century/Czesław_Miłosz/page.md` + 同目录 `metadata.json`、`images.txt`
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Czesław_Miłosz （肖像第 0 步标「待下载」，infobox 有 1999 年照与 mid-career 照）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 页面四件套已下载
- 肖像：**待下载**（infobox "Miłosz in 1999"；404 回退 Commons Special:FilePath / REST API，再失败装饰圆占位）
- **事实基准（正文优先；metadata 生年有双值噪声 1911-06-30 / 1911-11-30，取正文与 infobox 的 1911-06-30）**：
  - 生卒：1911-06-30 生于俄帝国考纳斯省 Šeteniai（今立陶宛凯达伊奈县）~ 2004-08-14 逝于克拉科夫家中，享年 93 岁；国葬于克拉科夫圣玛丽教堂，葬于 Skałka 教堂（波兰先贤安葬地）
  - 家庭：父 Aleksander Miłosz（波兰土木工程师，1863 一月起义者之孙）；母 Weronika（Kunat）；弟 Andrzej（1917–2002，记者/译者/纪录片制片人，二战中同为救助犹太人者）；子 Anthony（1947 生于华盛顿，作曲家）、John Peter（1951 生于华盛顿）
  - 国籍变迁（infobox Citizenship）：立陶宛（1918–）→ 波兰（–1951）→ 无国籍（1951–1970）→ 美国（1970–）→ 波兰（1995 起双重国籍）
  - 教育：维尔纽斯西吉斯蒙德·奥古斯都中学 → 1929 入斯捷潘·巴托里大学（维尔纽斯）法学部，1934 获法学学位；学生诗歌团体 **Żagary**（「维尔纽斯流浪者与知识分子学社」）
  - 1931 巴黎初访：遇远房表亲 **Oscar Milosz**（法语诗人、斯威登堡主义者），成为其导师与灵感来源
  - 早期职业：1936–37 维尔纽斯波兰电台文艺节目 → 因左翼同情指控与高层举报被解职 → 1937 移华沙波兰电台
  - 二战：华沙围城后辗转立陶宛/布加勒斯特，1940 夏徒步潜回德占华沙；参加地下讲座（Tatarkiewicz）；译莎剧《皆大欢喜》与艾略特《荒原》；以假名「Jan Syruć」地下出版第三部诗集《诗》（1940，可能是占领区华沙第一本地下出版物）；1942 地下出版战时波兰诗选《不可征服之歌》
  - 救助犹太人：经地下组织 Freedom 协助华沙犹太人；收留并资助 Tross 夫妇（弟 Andrzej 自维尔纽斯运出；二人均死于华沙起义）；另助 Felicja Wołkomińska 及其兄妹——1989 获 Yad Vashem「国际义人」（Righteous Among the Nations）
  - 未参加 Home Army 与华沙起义之筹划（自述自保本能+视其领导层右翼独裁；后亦批评红军未支援起义）
  - 外交官：1945–1951 任波兰人民共和国文化参赞（纽约→华盛顿→巴黎）；非共产党党员；1947 长子生；1948 促成哥伦比亚大学 Mickiewicz 波兰学部（遭波兰裔美侨抗议，1954 因停拨款终止）；1949 回国目睹恐惧氛围，曾向 Einstein 请教去留；1950 底护照被扣、经外长 Modzelewski 干预归还；1951 年 1 月出走巴黎
  - 巴黎流亡：1951 政治避难；美国因麦卡锡主义拒签；在《Kultura》发表《不》宣布决裂（**铁幕国家首位公开陈述与政府决裂理由的知名作家**）；1953 与家人团聚并出版《被禁锢的头脑》；1956 与 Janina 结婚
  - 伯克利：1960 受邀访学加州大学伯克利分校，两月后获终身教职（无 PhD、无执教经验），斯拉夫语言文学教授；1965 英译选编《战后波兰诗》；1969《波兰文学史》；1978 退休（Berkeley Citation），因妻子病复返讲堂
  - 1980-10-09 获诺贝尔奖：当日开完记者会照常去上陀思妥耶夫斯基课；获奖演说致敬表亲 Oscar；波兰解禁三十年禁令
  - 1981 哈佛诺顿诗歌教授（诺顿讲座成书《诗的见证》1983）；1981 会见 Wałęsa 与教宗若望·保禄二世
  - 晚年：1986 Janina 去世；1992 与 Carol Thigpen（Emory 大学学者）结婚（2002 卒）；1991 立陶宛独立后重访；2000 移居克拉科夫
  - 关键荣誉：Polish PEN 翻译奖 1974 · Guggenheim 1976 · Neustadt 国际文学奖 1978 · **Nobel 1980** · 美国国家艺术勋章 1989 · 白鹰勋章 1994 · Nike 奖 1998（Piesek przydrożny）；美国艺术与科学院/艺术与文学院/塞尔维亚科学院院士；哈佛/密歇根/伯克利/雅盖隆/卢布林/维陶塔斯·马格努斯等荣誉博士
  - 核心作品（4–6 条）：《救援》（Ocalenie, 1945，含 Campo dei Fiori、一个可怜的基督徒看犹太区）；《被禁锢的头脑》（1953）；《诗论》（Traktat poetycki, 1957，Franaszek 称之 magnum opus，Vendler 比之《荒原》）；《伊萨谷》（1955）与《故土》（1959）；《冬日的钟》（Bells in Winter, 1978）；《路边狗》（1997，Nike 奖）
  - 关键时间线（18 节点）：1911 生于 Šeteniai → 1914–18 随父随俄军战线流徙西伯利亚/俄国 → 1921 定居维尔纽斯 → 1929 入巴托里大学法学部 → 1930 首诗刊于学生杂志 → 1931 巴黎初遇 Oscar Milosz → 1933《关于凝冻时间的诗》→ 1934 法学毕业 → 1936–37 电台被解职·迁华沙 → 1939–40 围城·辗转·徒步回华沙 → 1940 地下出版《诗》→ 1943–44 救助犹太人·华沙起义·被俘获释 → 1945《救援》·任文化参赞 → 1951 出走巴黎《不》→ 1953《被禁锢的头脑》·1956 与 Janina 成婚 → 1957《诗论》→ 1960 伯克利 → 1978 Neustadt 奖·退休 → 1980 诺贝尔奖 → 1981 哈佛诺顿教授 → 1986 Janina 去世 → 1989 国际义人·国家艺术勋章 → 1992 与 Carol 成婚 → 2000 移居克拉科夫 → 2004 去世·国葬

### 第 1 步：建立目录 【模板通用】

- 已在 `literature/presentations/20th_century/Czesław_Miłosz/`（本提示词所在目录）

### 第 2 步：复制 Makefile 【模板通用】

- 设置 `MAIN=Czesław_Miłosz_zh`、`VIDEO_NAME=Czesław_Miłosz_zh`

### 第 3 步：收集图片 【人物专属】

- 下载肖像到 `images/Miłosz.jpg`（infobox 1999 年照），`curl -A "Mozilla/5.0"` + `file` 验证；失败装饰圆占位

### 第 4 步：文学领域梳理 + 入库 【模板通用，人物专属内容】

**Miłosz 的文学领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | Polish poetry | 波兰诗歌 | 「灾难派」出身，形式纵贯史诗到两行诗 | 封面、核心页 |
| 1 | witness poetry | 见证诗歌 | 战时经验与幸存者负罪（Campo dei Fiori 等） | 核心页 |
| 2 | literary criticism | 文学批评/思想论著 | 《被禁锢的头脑》——极权研究经典 | 论著页 |
| 3 | poetry translation | 诗歌翻译 | 译莎剧/《荒原》入波兰语；反向把波兰诗引入英语世界 | 翻译页 |
| 4 | literary history | 文学史 | 《波兰文学史》(1969)，在西方推广斯拉夫文学 | 学院页 |

#### 4.1 入库操作

- `python3 seed_person.py data/Czesław_Miłosz.yaml`（幂等；主记录 `primary_occupation='writer'`、`has_social_data=1`）
- 职业关联：writer（rank 0）、poet（rank 1）、translator（rank 2）
- 校验 person_field / person_relation 计数

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Oscar Milosz | 单向 | 远房表亲兼导师，1931 年巴黎初遇，引其入形而上之思 |
| influence | Simone Weil | 单向 | 思想影响者，其著作为 Miłosz 译入波兰语 |
| influence | Fyodor Dostoevsky | 单向 | 明载重要思想影响者 |
| influence | Thomas Stearns Eliot | 单向 | 明载重要思想影响者 |
| influence | Joseph Brodsky | 单向 | 影响其写作；1978 年称 Miłosz 为「我们时代最伟大的诗人」 |
| influence | Seamus Heaney | 单向 | 学界明载 Miłosz 影响其写作 |
| influence | Robert Hass | 单向 | 受 Miłosz 影响的诗人，亦为其 frequent translator |
| colleague | Jerzy Andrzejewski | 无向 | 友人小说家，1940 年合谋以假名地下出版《诗》 |
| colleague | Albert Camus | 无向 | 1951 年流亡巴黎时来访支持 |
| controversy | Pablo Neruda | 无向 | 1951 年 Miłosz 出走后，Neruda 在共产党报纸撰文攻击其为「逃跑的人」 |
| spouse | Janina Dłuska | 无向 | 1956 年成婚（1986 年卒） |
| spouse | Carol Thigpen | 无向 | 1992 年成婚（2002 年卒） |
| parent-child | Anthony Miłosz | — | 长子（1947 生），作曲家，译父诗入英 |
| parent-child | John Peter Miłosz | — | 次子（1951 生） |

> **不入库说明**：Jeanne Hersch（短暂恋情+支持者）与 Jane Zielonko（短暂关系、《被禁锢的头脑》译者）不入库；Einstein 仅「就任内职务见面请教」；Żagary 同社诗人（Zagórski/Bujnicki 等）为群体活动，逐一入库噪声大，仅以文学领域表与正文呈现；被 Miłosz 选集引入英语世界的 Szymborska/Herbert/Różewicz 无直接互动明载，禁写。

#### 4.5.1 入库操作

- 以 `name_en='Czesław Miłosz'`（Q45970）为中心写入 `person_relation`
- 对手方沿用库内记录：Albert Camus(4897)、Thomas Stearns Eliot(5154)、Pablo Neruda(5296)、Simone Weil(377)、Seamus Heaney(5173)、Joseph Brodsky(5382)；其余自动建 stub
- parent-child 不写 direction；influence 用 note 注明影响方向

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：灰暗史页上的清明、铁幕与自由之间的张力
- **配色**：石墨青灰（主色 `#37474F`）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `badgeWitness` 见证诗歌 — 深红 `#8B1A1A`
  - `badgeCaptive` 被禁锢的头脑 — 铁灰蓝 `#2E3B45`
  - `badgeBorder` 立陶宛-波兰边界 — 琥珀 `#B07B2A`
  - `badgeBerkeley` 伯克利岁月 — 加州蓝 `#1B5E8C`
- **背景母题**：地图轮廓线与界线网格，光斑刺破灰暗底色（见证与边界）

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. 封面右上肖像 + 细边框 + 姓名小字注。
2. 封面明示国籍（Poland，立陶宛出生）；底部状态栏 `国籍 | 语言 | 主要奖项`。
3. **必须有身份信息页**：左头像 + 右信息网格（生卒、本名、国籍变迁、教育、任职、荣誉、核心领域）。
4. **无公式框**：用《被禁锢的头脑》书影 /《救援》名句引文框（如 "A Song on the End of the World" 页面明载篇名，引文须用 page.md 英文原文）/ Gdańsk 造船厂纪念碑意象图式替代。
5. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页
01  封面 — 见证的诗人 / Czesław Miłosz 1911–2004 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含国籍变迁五段、教育、任职、荣誉）
03  核心贡献概览 — 《救援》/《被禁锢的头脑》/《诗论》/ 译介桥梁
04  童年与维尔纽斯 (1911–1934) — 贵族庄园、语言天赋、Żagary 诗社
05  巴黎与 Oscar Milosz (1931–1935) — 表亲导师、斯威登堡、奖学金再访
06  战火中的华沙 (1939–1944) — 地下出版、翻译《荒原》、华沙起义
07  国际义人 — 救助犹太人（Tross 夫妇等）、1989 Yad Vashem
08  文化参赞与出走 (1945–1951) — 纽约/华盛顿/巴黎、护照风波、《不》
09  巴黎流亡岁月 (1951–1960) — 《被禁锢的头脑》(核心页·书影)、Camus 支持、Neruda 攻击
10  《诗论》(1957) — magnum opus，Vendler 比之《荒原》
11  伯克利讲席 (1960–1978) — 两个月终身教职、《战后波兰诗》、《波兰文学史》
12  诺贝尔奖 (1980) — 当日照常上课、波兰解禁、凯旋与诺顿讲座
13  晚年：伯克利与克拉科夫之间 — 再婚、重返立陶宛、2000 移居克拉科夫
14  荣誉与认可 — Nobel 1980 · Neustadt 1978 · 国际义人 1989 · 白鹰勋章 1994
15  遗产：毫不妥协的清明
16  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；宏名禁数字；`\foreach` 分隔符 ASCII 逗号；tex 文件名含 Ł/ś 等非 ASCII 字符须注意 xelatex 与 shell 兼容（建议 tex 文件名用 `Czeslaw_Milosz_zh.tex` 转写，目录名保持原文）。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，`pdftoppm` 截图检查溢出/重叠；单遍取日志后须重新 `make pdf`。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Miłosz 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生日噪声 | frontmatter 有 1911-06-30 / 1911-11-30 双值，**取 06-30**（正文与 infobox 一致） |
| 国籍口径 | 名录标 Poland；正文五段 Citizenship 变迁须完整呈现；诺奖演说自认「波兰诗人，非立陶宛诗人」，但 2000 年又自称「大公国最后的公民」——两说并存，勿裁断 |
| 婚期 | 与 Janina 有 1944 华沙民事婚证的争议记载（注 4），**正式教会婚礼为 1956 年法国**；infobox 记 m. 1956；两说按 page.md 注脚处理 |
| 弟与子 | 弟 Andrzej 是记者/救助犹太人同役者（非亲子）；子 Anthony/John Peter 生于华盛顿（1947/1951） |
| 与 Żagary | 「灾难派」（catastrophist）标签是评论界对其诗社的称呼，后逐渐演变，勿写成终身标签 |
| 出走叙事 | 1951 年出走是「政治避难+《不》公开声明」，铁幕国家首位公开决裂理由的知名作家；Neruda 攻击与 Camus 支持须并列呈现，不作政治站队评价 |
| 救助犹太人 | 自己经组织 Freedom 协助+收留 Tross 夫妇（弟运出）；至少另助三人；「国际义人」1989 年追授 |
| 引语红线 | 《被禁锢的头脑》前言段（"I do not regret those years..."）与接受外交官任命的段落在 page.md 有英文原文可引；中文「原话」不得杜撰 |
| 政治内容 | 苏联/斯大林主义/麦卡锡主义/团结工会关联均按 page.md 客观事实简述，**不作政治评价、不展开政治叙事**；"You Who Wronged" 与纪念碑、Solidarity 仅一句客观带过 |
| 荣誉年份 | Neustadt 1978、Nobel 1980、国家艺术勋章 1989、白鹰勋章 1994、Nike 1998——勿混淆 |
| 身后 | 2004-08-14 国葬；Skałka 教堂墓志拉丁文 "May you rest well"、波兰文「治学亦是爱」；葬礼风波（抗议者与教宗确认领圣事）客观一笔带过 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| The Captive Mind | 《被禁锢的头脑》 | 通行译名；勿写「被奴役的心灵」 |
| Żagary | 扎加里诗社 | 维尔纽斯学生诗社，灾难派源头 |
| catastrophism | 灾难派 | 评论界标签，非自我定位 |
| A Treatise on Poetry | 《诗论》 | magnum opus 口径 |
| Righteous Among the Nations | 国际义人 | Yad Vashem 授予 |
| Kultura | 《文化》杂志 | 巴黎波兰流亡出版社刊物（Instytut Literacki） |
| Norton Lectures | 诺顿讲座 | 哈佛 1981，成书《诗的见证》 |
| The Issa Valley | 《伊萨谷》 | 童年庄园回忆小说 |
| Native Realm | 《故土》 | 1959 回忆录 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Expedition** — Alex-Productions
- **风格**: 坚毅 / 行进感 / 远行
- **匹配理由**:
  - "远行" 对应 Miłosz 一生的地理轨迹——Šeteniai → 维尔纽斯 → 华沙 → 巴黎 → 伯克利 → 克拉科夫，流亡与归返的完整弧线
  - "坚毅" 匹配「毫不妥协的清明」——在严酷冲突世界中直言的道德韧性
  - "行进感" 匹配从战时地下到诺奖讲台的漫长证言之路
- **本地路径**: `music_audio/alex-productions/` 下 Expedition 曲目 → `presentations/20th_century/Czesław_Miłosz/Expedition.wav`
- **时长**: 以实际曲目为准，`ffmpeg -shortest` 自动对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：无载禁写；涉政内容只客观简述，不作评价。**
