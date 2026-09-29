# 文学家立传提示词（OpenLiterature：Dario Fo）

> **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist / OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Dario Fo（达里奥·福），1997 年诺贝尔文学奖得主。
> **设计哲学**：文学家立传延续物理学家模板骨架（身份信息页 + 结构化领域表），以**剧作书影 / 引文框 / 意象图式**替代公式框——对达里奥·福，即「中世纪弄臣的当代还魂」：以即兴喜剧、闹剧与独角戏复兴 giullare（游方艺人）传统，以笑声鞭笞权威；其一生大量涉政（左翼运动、与贝卢斯科尼的长期对立、五星级运动）——**全部客观简述、不作政治评价、不展开政治叙事**。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史。
- **本实例**：Dario Luigi Angelo Fo（达里奥·福，1926-03-24 ~ 2016-10-13），意大利剧作家、演员、导演、舞台设计师、歌曲作者、政治活动家，1997 年诺贝尔文学奖得主；生前「堪称世界上演出最广泛的当代剧作家」。
- **设计哲学**：以「弄臣的鞭子」为核心叙事——瑞典学院表彰其「效仿中世纪的弄臣，鞭笞权威，维护受压迫者的尊严」；*Mistero Buffo* 三十年巡演欧美亚拉美，被红衣主教 Poletti 斥为「电视史上最亵渎的演出」——反讽与生命力的并存是其视觉母题：面具、铃铛与即兴姿态。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Dario Luigi Angelo Fo（达里奥·福，1926-03-24 ~ 2016-10-13，享年 90 岁）
- **官方获奖理由（Nobel 1997，禁止改写）**：
  > "who emulates the jesters of the Middle Ages in scourging authority and upholding the dignity of the downtrodden"
  > （表彰其效仿中世纪的弄臣，鞭笞权威，维护受压迫者的尊严）
- **气质关键词**：**弄臣的还魂者、即兴喜剧的当代大师、笑声中的愤怒**
- **设计母题**：**弄臣与面具（the jester & the mask）**。giullare 的铃铛帽、commedia dell'arte 的即兴面具、Harlequin 的彩衣与《一个无政府主义者的意外死亡》的审讯室——以马戏帐篷红金与修道院灰构成对位。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Dario_Fo/page.md`
- **Wikipedia**：https://en.wikipedia.org/wiki/Dario_Fo
- **肖像**：第 0 步优先用 page.md 内嵌图 `Dario_Fo,_Franca_Rame,_Jacopo_Fo.jpg`（与妻儿合影）或 `Dario_Fo2.jpg`（1976）；404 则用装饰圆占位。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）、`literature/presentations/cover/`（统一封面 `\input`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1926-03-24 生于 Lombardy 瓦雷泽省 Sangiano（马焦雷湖东岸，时为意大利王国）~ 2016-10-13 逝于米兰（重症肺病），享年 90 岁。
- **家庭与童年**：长子；父 Felice 为国铁站长（社会主义者、业余演员，演过易卜生剧目），随调职沿瑞士边境频繁搬家；母 Pina Rota Fo 出农家，1978 著回忆录《青蛙之国》；弟 Fulvio 后为剧场管理者、妹 Bianca 为作家；从外祖父与伦巴第渔民、玻璃匠学得讲故事的本领。
- **战时（客观简述）**：1942 迁米兰入 Brera 美术学院；16 岁被强征入墨索里尼社会共和国军队；家人参加反法西斯抵抗，他暗中帮父把难民与盟军士兵伪装成农民送往瑞士，后两度从军中出逃；其自述被游击队员与战友的证词及 1979-02-15 瓦雷塞法院判决质疑——**两说并陈、不下结论**。
- **战后教育**：回 Brera 学画，兼在米兰理工学建筑，因厌倦战后建筑业的机械劳动弃考；神经衰弱后听医嘱「做让自己快乐的事」，开始作画并投身 piccoli teatri（小剧场）运动。
- **婚姻与家庭**：1954-06-24 与出身剧场世家的 Franca Rame 结婚；1955-03-31 生独子 Jacopo（后亦为作家）。
- **起点（1950s）**：1950 与 Franco Parenti 合作综艺四年；1951 RAI 独角喜剧系列 Poer nano（18 个改编圣经与史话的童话独白），因丑化圣经人物被停播；1953 与 Parenti、Giustino Durano 组 I Dritti；1953 起与作曲家 Fiorenzo Carpi 合作（1967 前所有剧作配乐）；1958 返米兰创建 Compagnia Fo-Rame；1959 起六季连续推出全本剧，《大天使们不玩弹球机》获全国与国际声誉（首部走出意大利的福剧作）。
- **RAI 封杀与体制外（客观简述）**：1962 执导 RAI 综艺 Canzonissima，因涉及建筑工人危险工作条件与制作方决裂（1962-11-29 率 Rame 撤出）；RAI 起诉并销毁全部录像，两人被电视界实际封杀 14 年（1977 重返 Rai 2）；1968 建 Associazione Nuova Scena；1970 建 Collettivo Teatrale La Comune；1974 占领废弃市场修缮为 Palazzina Liberty。
- **代表作与里程碑（5 条）**：
  1. 《Mistero Buffo》（1969 起）——独角戏巅峰，三十年巡演四大洲；被红衣主教 Poletti 斥为「电视史上最亵渎的演出」；
  2. 《一个无政府主义者的意外死亡》（1970-12 首演）——取材 1969 米兰丰塔纳广场银行爆炸案，自称「关于一桩悲剧性闹剧的怪诞闹剧」；
  3. 《不付钱！不付钱！》（1974）——写 autoriduzione（自我减价）运动，1990 年前已在 35 国上演，剧名进入英语；
  4. 《Tutta casa, letto e chiesa》（1977，五独白，Rame 主演）与《The Pope and the Witch》（1989）；
  5. 《Johan Padan and the Discovery of the Americas》（1992）——哥伦布 500 周年的反叙事独角戏。
- **Rame 绑架事件（客观简述，一句带过）**：1973-03 Rame 被五名法西斯分子劫持施暴，福与 Rame 当年即恢复巡演。
- **美国禁入（客观简述）**：1980/1983 美国当局两度拒绝福与 Rame 入境；1980-05 纽约举办声援晚会（Miller、Malamud、Scorsese 等出席）；后对国务院诉讼。
- **诺奖与晚年**：1975 首次获提名时自称「这诺贝尔买卖是出真喜剧」；1995-07-17 中风、1996 前康复；**1997 获诺贝尔文学奖**；2001 任 Collège de 'Pataphysique Satrap；2005 竞选米兰市长（初选第二）；2010s 成为五星级运动的「主心骨」（其成员称之）；2016 最后著作《Razza di Zingaro》写遭纳粹杀害的辛提拳击手 Trollmann，同年 Brera 展出系列画作；2016-10-13 逝世。
- **关键时间线（15 节点）**：1926 生于 Sangiano → 1942 入 Brera、战时两度出逃 → 战后 Brera + 米兰理工 → 1950 与 Parenti 合作 → 1951 Poer nano → 1953 I Dritti、遇 Carpi → **1954 与 Franca Rame 结婚** → 1955 子 Jacopo 出生 → 1958 Compagnia Fo-Rame → 1959《大天使们不玩弹球机》→ 1962 Canzonissima 决裂、电视封杀 → 1968/1970 Nuova Scena 与 La Comune → **1970《一个无政府主义者的意外死亡》** → 1974《不付钱！不付钱！》→ 1995 中风 → **1997 诺贝尔文学奖** → 2016 逝世。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | political theatre | 政治剧场 | La Comune 集体、社区剧场与工人题材 | 核心页 |
| 1 | commedia dell'arte | 即兴喜剧 | 古意大利传统的当代复兴 | 核心页 |
| 2 | farce | 闹剧 | 「怪诞闹剧」的自称与笑声的批判力 | 代表作页 |
| 3 | solo theatre | 独角戏 | giullare 传统还魂；Mistero Buffo 三十年巡演 | 独角戏页 |
| 4 | scenography | 舞台美术 | 自写自导自演自设计；画家出身 | 美术页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Franca Rame | 无向 | 1954 年结婚，终身舞台与事业搭档 |
| colleague | Franca Rame | 无向 | Compagnia Fo-Rame 与 La Comune 共同创办者 |
| parent-child | Jacopo Fo | 无向 | 独子，作家兼剧作家 |
| colleague | Franco Parenti | 无向 | 1950 起四年综艺合作的起点 |
| colleague | Giustino Durano | 无向 | I Dritti 综艺团伙伴 |
| colleague | Fiorenzo Carpi | 无向 | 长期作曲搭档，1967 年前所有剧作配乐 |
| influence | Angelo Beolco 等九人 | 自认影响 | 见 yaml：Beolco、Brecht、Chekhov、De Filippo、Gramsci、Mayakovsky、Molière、Shaw、Strehler——page.md 明载「considered his artistic influences」 |

> 贝卢斯科尼等政界对手一律**不入库**（涉政红线）；Rossellini/Bergman 仅系邻居**不入库**；Tati/Keaton/Chaplin 仅系电影风格参照**不入库**。

### 第 5 步：设计配色 【人物专属】

- **主色**：剧场靛蓝 `#16324F`（米兰夜幕与政治剧场的冷峻）
- **诺奖香槟金**：`#C9A227`
- badge 四分类色：
  - `badgeJester` 弄臣 — 马戏红 `#A63A2B`
  - `badgeMask` 即兴喜剧 — 琥珀 `#C97B30`
  - `badgeFarce` 闹剧 — 玫瑰 `#A34A6B`
  - `badgeStudio` 舞台美术 — 青灰 `#4A6B75`
- **背景母题**：柔和气泡 + 铃铛帽轮廓与即兴面具剪影；1997 诺奖页后加入瑞典学院金色印章。

### 第 6 步：规划幻灯片序列 【人物专属，16 页】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 弄臣的还魂 / Dario Fo 1926–2016 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（全名、生卒、出生地、婚姻、剧团谱系、荣誉、核心领域）
03  核心贡献概览 — 政治剧场 / 即兴喜剧 / 闹剧 / 独角戏 / 舞台美术
04  湖畔童年与战时 (1926–1945) — 站长之家、玻璃匠聚落的故事课、两度出逃（客观简述）
05  Brera 与小剧场 (1945–1950) — 弃建筑从画、piccoli teatri 即兴独白
06  Poer nano 与 I Dritti (1951–1954) — 广播独角戏、停播风波、与 Rame 结婚
07  Compagnia Fo-Rame (1958–1962) — 夫妻剧团、大天使们不玩弹球机
08  电视封杀与体制外 (1962–1970) — Canzonissima 决裂、Nuova Scena、La Comune（客观简述）
09  一个无政府主义者的意外死亡 (1970) — 丰塔纳广场案与怪诞闹剧（引文框①：剧名自称）
10  不付钱！不付钱！与 Rame 的独白 (1974–1977) — autoriduzione、Tutta casa letto e chiesa
11  1997 诺贝尔奖 — 弄臣的授勋（引文框②：获奖理由 EN 原文 + 1975 年「喜剧」自嘲对照）
12  Mistero Buffo 与独角戏宇宙 — 三十年巡演、亵渎之争（客观简述）
13  晚年行动 (2001–2016) — 米兰市长竞选、五星级运动、Razza di Zingaro（客观简述）
14  遗产 — 「演出最广泛的当代剧作家」、剧名进入英语、三十种语言的笑声
15  结尾 — 鞭笞权威，维护受压迫者的尊严
```

> 文学家无公式框：第 9/11/12 页用**剧作书影框 / 面具意象图式 / 获奖理由原文引文框**替代。

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 剧名引用 | Accidental Death of an Anarchist / Can't Pay? Won't Pay! / Mistero Buffo——一律官方英译名 + 意大利原名并列 |
| 获奖理由措辞 | 官方 "who emulates the jesters of the Middle Ages in scourging authority and upholding the dignity of the downtrodden"，勿改写 |
| 涉政内容 | 与 PCI 的冲突、RAI 封杀、美国禁入、贝卢斯科尼对立、五星级运动——客观一句带过，**不作政治评价** |
| Rame 绑架 | 1973-03 一句客观带过（Rame 独白 The Rape 1983 受其启发），不展开暴力细节 |
| 战时自述争议 | 抵抗叙事被证词与 1979 法院判决质疑——**两说并陈**，不下结论 |
| 影响者清单 | 九人系 page.md 明载，全部入库（防 Review 误删） |
| 中风年份 | 1995-07-17，1996 七十岁生日前康复——勿与 2016 逝世混淆 |
| Carpi 分界 | 1967 前所有剧作配乐均 Carpi；1975-76 与 1997 两度回归——勿写「终身唯一配乐师」 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| giullare | 游方艺人（中世纪弄臣） | 获奖理由核心意象 |
| commedia dell'arte | 即兴喜剧 | 面具与定型角色 |
| farce | 闹剧 | 「grotesque farce about a tragic farce」自称 |
| Mistero Buffo | 喜剧神秘剧 | 独角戏代表作 |
| Accidental Death of an Anarchist | 一个无政府主义者的意外死亡 | 1970；丰塔纳广场案 |
| Can't Pay? Won't Pay! | 不付钱！不付钱！ | 剧名进入英语 |
| autoriduzione | 自我减价运动 | 1974 剧作的社会背景 |
| Compagnia Fo-Rame | 福-拉梅剧团 | 1958 创建 |
| La Comune | 「公社」剧场集体 | 1970 创建 |
| Palazzina Liberty | 自由宫 | 1974 占据的 Milan 场地 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Savage** — Alex-Productions
- **匹配理由**:
  - "狂放/原始" 匹配即兴喜剧的能量 —— 面具、铃铛与即兴身体的粗粝活力，恰是 giullare 传统的当代还魂
  - "锋利" 匹配其笑声的批判性 —— 以闹剧鞭笞权威，Savage 的压迫感节奏与审讯室戏码同构
  - "戏剧性" 匹配其一生剧场性 —— 从 Poer nano 停播到诺贝尔授勋，福的人生本身是一场长演
- **本地路径**: `music_audio/alex-productions/…/Savage.wav`（对照 `music_audio/curated_tracks.md` 取实际编号）→ `presentations/20th_century/Dario_Fo/Savage.wav`
- **时长**: 约 140 秒 > 16 页 × 7 秒 ≈ 112 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Dario_Fo/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `literature/presentations/cover/` | 项目首页模板（统一 `\input`） |
| `MySQL/seed_person.py` | 人物主记录 + 研究领域 + 社会关系入库 |
| `MySQL/data/Dario_Fo.yaml` | 入库 yaml |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
