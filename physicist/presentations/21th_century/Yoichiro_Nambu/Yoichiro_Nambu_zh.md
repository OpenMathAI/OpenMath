# 物理学家立传提示词（Yoichiro Nambu）

> 本文件是 OpenPhysicist 21 世纪批次人物专属立传提示词，目标人物：Yoichiro Nambu（2008 诺贝尔物理学奖一半，自发对称性破缺机制）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Yoichiro Nambu / 南部陽一郎。
- **设计哲学**：物理学家立传必须有「身份信息页」+「研究领域」结构化表达，此骨架务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Yoichiro Nambu（1921-01-18 生于东京 ~ 2015-07-05 逝于大阪府丰中市，享年 94 岁）
- **气质关键词**：**自发对称性破缺的开创者、弦论的奠基人之一、永远超前十年的理论家** —— 2008 诺贝尔物理学奖获奖理由（获一半奖金；另一半归小林诚/益川敏英）：
  > "for the discovery of the mechanism of spontaneous broken symmetry in subatomic physics"（因发现亚原子物理中自发对称性破缺机制）
- **设计母题**：**倾斜的旋转伞（the tilted umbrella）**。自发对称性破缺：方程保持对称而基态不再对称——如旋转伞面下凹、伞柄斜立；由此产生的无质量 Nambu–Goldstone 玻色子，是标准模型希格斯机制的原型思想。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Yoichiro_Nambu/page.md`（已有本地）
- **第 0 步素材状态**：`Yoichiro_Nambu.html` 与 `images/` **待下载**；Wikipedia URL：`https://en.wikipedia.org/wiki/Yoichiro_Nambu`
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已有本地（frontmatter + infobox + 正文已核对，事实基准如下）
- 🔲 待下载：`https://en.wikipedia.org/wiki/Yoichiro_Nambu` → `Yoichiro_Nambu.html`；肖像（infobox 照片 Nambu in 2005，另有 1965 朝日新闻采访照、1996 Argonne 合照）→ `images/`
- **事实基准**（全部取自 page.md）：
  - 生卒：1921-01-18 生于东京（大日本帝国）~ 2015-07-05 逝于大阪府丰中市（心力衰竭，享年 94；12 天后公布，仅亲属出席葬礼）
  - 国籍：日本出身，1970 入籍美国（frontmatter 国籍 United States + Japan；表述「日裔美国物理学家」）
  - 家庭：父南部吉郎，福井出身，立命馆中学→早稻田大学文学部（毕业论文论 William Blake），福井女子高中英语教师；1923 关东大地震后全家回福井；妻 Chieko Hida；子 John Nambu；身后由妻 Chieko 与子 John 送终
  - 教育：少年自制矿石收音机听棒球转播；第一高等学校（一高）；在学期间物理吃力（熵概念最难、热力学课不及格）；东京帝国大学（今东京大学），同学中有后来以天体物理基础研究闻名的林忠四郎；毕业前求教汤川秀树与朝永振一郎被拒——「只有天才才能懂粒子物理」
  - 学位：1942 理学学士（东京帝大）；1952 理学博士（DSc）
  - 任职：1942 入伍陆军任技术中尉（挖壕/摆渡，后调短波雷达研究；奉命获取朝永振一郎雷达理论机密文件——直接登门获朝永配合而非间谍手段）；1945–49 东京大学物理学系；1949 大阪市立大学副教授，次年 29 岁升正教授；1952–54 普林斯顿高等研究院（两见爱因斯坦，后者力陈其对量子力学的深刻怀疑）；1954 起芝加哥大学，1958 正教授，1974–77 物理系主任；Henry Pratt Judson 杰出服务荣休教授（物理系 + Enrico Fermi 研究所）；1994 立命馆大学访问教授 + 立命馆亚太大学学术顾问（两校同年设立南部阳一郎研究奖励基金）；1996 大阪大学首个名誉博士，2006 特任教授（丰中校区有研究室）；2011 回日本定居丰中；2017 大阪大学理学研究科 Nambu Hall 启用；2018-11-01 大阪市立大学设立 NITEP（南部阳一郎理论与实验物理研究所）
  - 关键荣誉（含年份）：Heineman 数学物理奖 1970；J. Robert Oppenheimer Memorial Prize 1977；日本文化勋章 + 文化功劳者 1978；福井市名誉市民 1979；美国国家科学奖章 1982；马克斯·普朗克奖章 1985；ICTP 狄拉克奖章 1986；樱井奖 1994；沃尔夫物理学奖 1994/1995；本杰明·富兰克林奖章 2005 + 奥斯卡·克莱因纪念讲座 2005；Pomeranchuk Prize 2007；**Nobel 2008（一半）**；福井县奖 2003、丰中市名誉市民 2011
  - 知名学生：page.md 正文无载（勿写；外部链接中 Madhusree Mukerjee 被标注为 former student，正文未载，不入库）
  - 核心贡献清单（4–6 条）：①1960 提出自发对称性破缺（由 BCS 超导 Bogoliubov–Valatin 方程与狄拉克方程的形式类比悟出）+ 强子弱轴矢部分守恒（PCAC）假说——希格斯机制的理论原型；②1961 与 Jona-Lasinio 两篇合作论文提出 NJL 模型，解释核子质量的手征对称性破缺起源；③1964 给出 Goldstone 定理的一般数学证明（Nambu–Goldstone 玻色子）；④1965 与 Han 提出夸克「色」自由度（整数电荷三重态模型；「color charge」一词由 Gell-Mann/Fritzsch 1971 命名）——QCD 概念地基；⑤1970 年代初独立发现双重共振模型可重释为量子化相对论弦，提出 Nambu–Goto 作用量——弦论奠基人之一；⑥1973 提出 Nambu 力学（多哈密顿量 + Nambu 括号）
  - 其他早期工作：1951 独立提出奇异粒子 associative production；1957 预言矢量 ω 介子、导出 crossing symmetry
  - 关键时间线（15–20 节点）：1921 生于东京 → 1923 关东大地震后迁福井 → 一高（热力学不及格）→ 1942 东京帝大 BS → 1942–45 陆军技术中尉/雷达研究 → 1943 直接向朝永取得雷达文件 → 1945–49 东京大学（受朝永 QED 与久保亮五凝聚态影响）→ 1949 大阪市立大学副教授 → 1950 29 岁正教授 → 1952 DSc + IAS 普林斯顿（两见爱因斯坦）→ 1954 入芝加哥大学 → 1957 预言 ω 介子 + crossing symmetry → 1958 正教授 → 1960 自发对称性破缺 + PCAC → 1961 NJL 模型 → 1964 Goldstone 定理一般证明 → 1965 Han–Nambu 色自由度 → 1970 入籍美国 + Heineman 1970 → 1970 年代初弦论重构 + Nambu–Goto 作用量 → 1973 Nambu 力学 → 1974–77 系主任 → 1978 文化勋章 → 1994 立命馆 + Sakurai + Wolf → 2005 Franklin Medal → 2008 诺贝尔奖（未赴斯德哥尔摩，Jona-Lasinio 代讲）→ 2011 定居丰中 → 2015-07-05 卒
  - 他人评价（引语白名单）：Zumino「他总是比我们超前十年…我花了十年才弄懂他做的东西」；益川敏英「南部先生是日本产生过的最伟大的物理学家，我认为他甚至在汤川和朝永之上」；回忆被拒轶事「Only geniuses can understand particle physics」
  - 轶事：动漫《科学忍者团 Gatchaman》主角之一南部考三郎博士之名受其启发

### 第 0.5 步：事实核对清单（执行立传前逐项打勾，page.md ↔ 本提示词）【人物专属】

- [ ] 1921-01-18 生于东京（大日本帝国）；2015-07-05 卒于大阪府丰中市（心力衰竭，94 岁，12 天后公布）
- [ ] 1923 关东大地震后全家迁福井；父南部吉郎（早稻田文学部、毕业论文论 Blake、福井女子高中英语教师）
- [ ] 一高时代物理吃力：熵概念最难、热力学课不及格；少年自制矿石收音机听棒球转播
- [ ] 东京帝大：同学林忠四郎；求教汤川秀树/朝永振一郎被拒（「只有天才才能懂粒子物理」）
- [ ] 1942 理学学士；1942–45 陆军技术中尉（短波雷达）；1943 直接向朝永取得雷达理论文件
- [ ] 1949 大阪市立大学副教授；1950 29 岁正教授；1952 DSc；1952–54 IAS 普林斯顿（两见爱因斯坦）
- [ ] 1954 入芝加哥大学；1958 正教授；1974–77 物理系主任；1970 入籍美国
- [ ] 1960 自发对称性破缺 + PCAC；1961 NJL（与 Jona-Lasinio）；1964 Goldstone 定理一般证明
- [ ] 1965 与 Han 提出色自由度（整数电荷三重态）；1970s 初弦论重构 + Nambu–Goto 作用量；1973 Nambu 力学
- [ ] 荣誉年份链：Heineman 1970 / Oppenheimer 1977 / 文化勋章+文化功劳者 1978 / NMS 1982 / Planck 1985 / Dirac 1986 / Sakurai 1994 / Wolf 1994-95 / Franklin 2005 / Pomeranchuk 2007 / Nobel 2008 半奖
- [ ] 2008 未赴斯德哥尔摩，Giovanni Jona-Lasinio 代讲诺奖演说
- [ ] 晚年：1994 立命馆；1996 大阪大首个名誉博士；2011 定居丰中；2017 Nambu Hall（大阪大）；2018 NITEP（大阪市立大）

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `Yoichiro_Nambu/` 与 `images/`（第 0 步已建则复用）

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设置 `MAIN=Yoichiro_Nambu_zh`、`VIDEO_NAME=Yoichiro_Nambu_zh`

### 第 3 步：收集图片 【人物专属，待下载】

- 肖像：infobox「Nambu in 2005」照片 → `images/portrait.jpg`；下载后 `file` 验证（JFIF density 异常时 sips 改 72dpi）
- 备选历史照：1965 朝日新闻采访照、1996 Argonne 双重性会议合照（page.md 内嵌 commons 图）
- Commons 直链 404 时回退：Wikipedia REST API `page/summary` 查 infobox 原图名，或 `Special:FilePath/<文件名>?width=600`
- 可选自绘插图：倾斜伞/墨西哥帽 SSB 示意（tikz）/ 弦的世界面示意；Gatchaman 海报有版权，仅文字提及

### 第 9.5 步：交付前自查清单 【模板通用，第 9 步完成后逐项核对】

- [ ] 编译 0 error；vbox ≤ 10pt、hbox ≤ 50pt（取真实 xelatex 日志核对，勿被 latexmk -c 误判）
- [ ] 页数与第 6 步规划一致（pdfinfo 数页数，页数不符 = 可能有帧未渲染或被合并）
- [ ] 逐页 pdftoppm 目检溢出/重叠；修复优先级：删 \plainbar → 缩 inner sep → 缩字号 → 减行距
- [ ] 引语逐条对照白名单（仅 Zumino/益川/被拒三处）；陷阱表「无载禁写」逐条核对
- [ ] 批内主色互查不重复；BGM 曲名批内唯一
- [ ] 术语清单中译逐条核对；结尾页品牌口径 OpenMathAI

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

**Nambu 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | quantum field theory | 量子场论 | 职业主线（诺奖委员会口径 subatomic physics） | 封面、身份页 |
| 1 | spontaneous symmetry breaking | 自发对称性破缺 | 1960 提出，2008 诺奖核心 | 核心贡献页 |
| 2 | quantum chromodynamics | 量子色动力学 | 1965 色自由度先驱，QCD 奠基人之一 | 色荷页 |
| 3 | string theory | 弦论 | Nambu–Goto 作用量，奠基人之一 | 弦论页 |
| 4 | superconductivity | 超导理论 | BCS 类比的灵感来源（研究重心之一） | SSB 缘起页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Makoto Kobayashi | 无向 | 2008 诺贝尔物理学奖共享（Nambu 得一半，小林/益川均分另一半） |
| co-honored | Toshihide Maskawa | 无向 | 2008 诺贝尔物理学奖共享（Nambu 得一半，小林/益川均分另一半） |
| colleague | Giovanni Jona-Lasinio | 无向 | 1961 两篇合作论文提出 NJL 模型；2008 代 Nambu 赴斯德哥尔摩发表诺奖演讲 |
| colleague | Moo-Young Han | 无向 | 1965 合作论文提出夸克色自由度（整数电荷三重态强作用模型） |
| influence | Sin-Itiro Tomonaga | 无向 | 战后东大时期深受其 QED 工作影响；1943 曾直接向其求取雷达理论文件 |
| influence | Ryogo Kubo | 无向 | 战后东大时期深受其凝聚态物理研究影响 |
| spouse | Chieko Hida | 无向 | 妻子（infobox + 讣文明载） |
| parent-child | John Nambu | 亲→子 | 儿子（infobox Children + 讣文明载） |

- 仅收 page.md 明载关系；汤川秀树/朝永振一郎的「求教被拒」不构成师承，不入 advisor-student。

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：深邃、超前、静水流深
- **配色**：暗紫蓝（主色）+ 香槟金（诺奖 `C9A227`）+ 四分类色
  - 主色 `mainclr` 暗紫蓝 `#4E3D6E`
  - `badgeSSB` 自发对称性破缺 — 钢蓝 `#2E5E8C`
  - `badgeNG` Nambu–Goldstone — 琥珀 `#D08A2E`
  - `badgeColor` 色荷 — 玫瑰 `#C2466B`
  - `badgeString` 弦论 — 青绿 `#1F7A6D`
- **批内主色查重**：#4E3D6E 仅本篇使用（Mather #0F3057 / Smoot #8C2F39 / Fert #1B4D3E / Grünberg #2F4F4F）
- **背景母题**：深底上一组从完美圆形渐变到倾斜椭圆的等高线，呼应「对称方程 → 破缺基态」

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 自发对称性破缺的开创者 / 南部陽一郎 1921–2015 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、教育、任职、荣誉、核心领域）
03  核心贡献概览 — SSB / NJL / 色荷 / 弦论 / Nambu 力学
04  少年：东京到福井 (1921–1940) — 大地震、矿石收音机、一高与不及格的热力学
05  东京帝大：被汤川与朝永拒之门外 (1940–1942) — 「只有天才才能懂粒子物理」
06  战时：技术中尉与雷达文件 (1942–1945) — 直接登门见朝永
07  大阪市立大学到普林斯顿 (1949–1954) — 29 岁正教授、两见爱因斯坦
08  芝加哥岁月 (1954–) — 1958 正教授、Enrico Fermi 研究所、系主任
09  1960：自发对称性破缺（核心贡献页一，公式框放 BCS–Dirac 类比示意；Nambu–Goldstone 玻色子）
10  NJL 模型与色荷 (1961/1965) — 与 Jona-Lasinio、与 Han；QCD 概念地基
11  弦论的起点 — 双重共振模型 → 相对论弦、Nambu–Goto 作用量；1973 Nambu 力学
12  2008 诺贝尔奖 — 半奖口径、未赴斯德哥尔摩、Jona-Lasinio 代讲
13  荣誉与评价 — Wolf 1994/95 · 文化勋章 1978 · 益川「日本最伟大的物理学家」· Zumino「超前十年」
14  晚年与遗产 — 立命馆/大阪大学、Nambu Hall、NITEP、Gatchaman 轶事
15  结尾
```

### 第 7–8 步：版式要点 + 该人专属陷阱表 【人物专属】

- 版式复用标杆骨架（`\plainbar` / `\deckbackground` / `\profileslide`）；每写一页 make 并截图查溢出。
- **Nambu 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 半奖口径 | 2008 诺贝尔物理学奖 Nambu 获**一半**，小林诚/益川敏英均分另一半；三方贡献互不相关（SSB vs CP 破缺），勿写成三人合作 |
| 获奖理由 | 官方 "for the discovery of the mechanism of spontaneous broken symmetry in subatomic physics"；勿混入 Kobayashi–Maskawa 的 citation 原句 |
| 求教被拒 | 「只有天才才能懂粒子物理」是被汤川/朝永拒之门外的轶事，**不构成师承关系**，禁写 advisor-student |
| 色荷命名 | Nambu/Han 1965 提出量子数与整数电荷三重态模型；「color charge」一词是 Gell-Mann/Fritzsch 1971 命名；Nambu 模型采用整数电荷，后世标准模型用分数电荷——勿写「Nambu 命名色荷」或「Nambu 创立 QCD」 |
| 弦论归属 | Nambu 独立发现弦重构与提出作用量；「奠基人之一」不是「唯一创始人」；Goto 细节本页未载勿展开 |
| 库内 stub 复用（P0） | 库内 id=2974 'Yoichiro Nambu' 是 batch-5 建小林/益川 co-honored 时的对手方 stub（primary_occupation 误为 mathematician）；yaml 沿用 name_en 'Yoichiro Nambu' UPD 补全并回填 QID Q188120，勿另建别名记录 |
| Tomonaga 规范名 | 库内规范名 **Sin-Itiro Tomonaga**(id=2411, Q184563)，勿用 Shin'ichirō 拼写建 stub；另有 Tomonaga Sanjuro(2552) 为不同人 |
| 在世亲属 | 妻 Chieko Hida、子 John Nambu 仅按 infobox/讣文明载入库，生平细节勿展开 |
| 日本机构译名 | 大阪市立大学（今大阪公立大学）、立命馆大学/亚太大学、大阪大学三组机构勿混淆；Nambu Hall（2017 大阪大）与 NITEP（2018 大阪市立大）归属不同学校 |
| 引语白名单 | Zumino、益川两句 + 「Only geniuses…」共三处可引；其余勿加引号当原话 |
| 战时表述 | 陆军技术中尉、雷达研究、朝永文件均按 page.md 客观表述，勿渲染军国叙事 |
| 名人混淆 | 动漫角色南部考三郎是「名字受启发」，勿写「以他为原型」 |

### 第 9 步：术语审查 【人物专属】

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| spontaneous symmetry breaking | 自发对称性破缺 | 获奖理由核心词，勿译「自发破缺对称」 |
| Nambu–Goldstone boson | 南部–戈德斯通玻色子 | 无质量玻色子，SSB 产物 |
| Goldstone theorem | 戈德斯通定理 | 1964 Nambu 给出一般证明 |
| Nambu–Jona-Lasinio model | NJL 模型 | 核子质量动力学起源 |
| chiral symmetry | 手征对称性 | SSB 在强作用的载体 |
| color charge | 色荷 | 1965 概念先驱 / 1971 命名，两节点 |
| Nambu–Goto action | 南部–后藤作用量 | 弦的世界面面积 |
| dual resonance model | 双重共振模型 | 弦论的前身 |
| Nambu mechanics / bracket | 南部力学 / 南部括号 | 哈密顿力学的高阶推广 |
| Bogoliubov–Valatin equations | 博戈留波夫–瓦拉京方程 | BCS 中的正则变换，SSB 类比来源 |

---

## 四、背景音乐建议 【人物专属】

- **选定曲目**: **Eternals** — Alex-Productions（宏大 / 深远）
- **匹配理由**: 从 SSB 到色荷到弦论，Nambu 的每一项工作都在几十年后成为主流结构的「长期地基」；「宏大/深远/长期影响」标签与 Zumino「超前十年」的评价互为注脚。
- **批内查重**: Eternals 仅本篇使用（Mather=Expedition / Smoot=The Invisible Light / Fert=Through the Darkness / Grünberg=New Lands）
- **本地路径**: `music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Yoichiro_Nambu/page.md` | 本地事实基准 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Yoichiro_Nambu.yaml` | 社会关系入库源 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

