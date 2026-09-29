# 和平奖得主立传提示词（OpenPeace：Sir Norman Angell）

> **本文件是 OpenPeace 项目的人物专属立传提示词**，以 Sir Norman Angell（1933 诺贝尔和平奖，《大幻影》作者）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节 + 第 0–9 步）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenPhysicist / OpenMedic 同属 OpenMathAI 共享仓库）。
- **模板来源**：综合物理学家标杆（Kenneth G. Wilson 提示词 + Beamer 结构）与医学/化学侧批量立传经验。
- **本实例**：Sir Ralph Norman Angell（诺曼·安吉尔爵士）。
- **设计哲学**：和平奖得主立传与科学家立传的核心差异，在于**没有「研究领域」而有「事业领域」**，且叙事主线是「理念—论战—影响」而非「实验—理论—应用」；身份信息页（Identity / Bio 速览页）与结构化的领域表达两点构成骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Sir Ralph Norman Angell（1872-12-26 ~ 1967-10-07，享年 94 岁）
- **气质关键词**：**《大幻影》的作者、战争非理性的论者、以笔为剑的新闻人** —— 1933 诺贝尔和平奖获奖理由：
  > "for having exposed by his pen the illusion of war and presented a convincing plea for international cooperation and peace."（表彰他以笔揭露战争的幻象，并为国际合作与和平提出令人信服的呼吁）
- **设计母题**：**幻影的破灭（the optical illusion）**。其核心论点是「欧洲经济一体化已使战争全然徒劳、军国主义过时」——视觉上可用「被戳破的幻象/雾中地图/信用的网络」呼应「战争的幻影」这一母题。
- **本地 Wikipedia**：`peace/presentations/pages/20th_century/Norman_Angell/page.md`（含 frontmatter QID Q272224 与 infobox）
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）
  - 名录（官方理由照抄源）：`peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准（据本地 page.md，无载禁写） 【人物专属】

- 生卒：1872-12-26 生于林肯郡 Holbeach（本名 Ralph Norman Angell Lane，后以 Angell 为姓氏）~ 1967-10-07 逝于 Surrey 郡 Croydon，享年 94 岁
- 国籍：英国（United Kingdom）
- 家庭：Thomas Angell Lane 与 Mary（née Brittain）的第六个孩子；1899 与 Beatrice Cuvellier 结婚，后分居，独居最后 55 年；购入 Essex 郡 Northey Island（仅退潮时与本土相连）独居
- 教育：英国多所学校 → 法国 Saint-Omer 的 Lycée Alexandre Ribot → 日内瓦大学（同时在日内瓦编辑一份英文报纸）
- 17 岁移民美国西海岸：葡萄园工、灌渠挖掘工、牛仔、宅地法移民（曾申请美国国籍）、邮差、探矿者，后任《St. Louis Globe-Democrat》与《San Francisco Chronicle》记者
- 1898 返英，随后赴巴黎：《Daily Messenger》副编辑、《Éclair》撰稿人、多家美国报纸驻法记者（德雷福斯事件通讯）；1905–12 任《Daily Mail》巴黎主编
- 任职/身份：1914 共同创立 Union of Democratic Control；1920 加入工党；1929–31 Bradford North 选区下院议员；Royal Institute of International Affairs 理事、World Committee against War and Fascism 执委、League of Nations Union 执委、Abyssinia Association 会长
- 关键荣誉：Knight Bachelor（1931 新年授勋）；Nobel Peace Prize 1933（1935-06-12 发表诺奖演讲 Peace and the Public Mind）
- 核心事业清单（4–6 条）：
  1. 《Europe's Optical Illusion》（1909 小册子）→《The Great Illusion》（1910 成书）：经济一体化使征服在经济上徒劳
  2. 一战期间集体安全与国际组织的倡导（Union of Democratic Control）
  3. 议员生涯（1922/1923/1935 三度参选失利，1929–31 在任）
  4. 经济教育：《The Money Game》（1928）用游戏教儿童金融与银行基础
  5. 1930 年代中后期倡导对德意日侵略政策的集体国际反对；1940 赴美演讲支持援英
- 关键时间线（15–20 节点）：1872 出生 → 1889 前后赴法求学/日内瓦 → 17 岁移民美国 → 1898 返英 → 1899 结婚 → 巴黎新闻生涯 → 1905–12 Daily Mail 巴黎主编 → 1909 小册子 → 1910《The Great Illusion》→ 1914 UDC 共同创立 → 1920 入工党 → 1929–31 议员 → 1931 受封爵士 → 1933 诺奖 → 1935 诺奖演讲 → 1940 赴美 → 1951 自传 After All → 1967 去世

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

**Angell 的事业领域（按 rank 排序，已入库 person_field，与 yaml fields 一致）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace advocacy | 和平倡导 | 1933 诺奖核心理由 | 核心页 |
| 1 | political economy | 政治经济学 | 战争的经济非理性论证 | 大幻影页 |
| 2 | international relations | 国际关系 | 国际合作与国际组织主张 | 核心页 |
| 3 | journalism | 新闻事业 | Daily Mail 巴黎主编、战地通讯 | 早年页 |
| 4 | economic education | 经济教育 | The Money Game 经济教学法 | 晚年页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 与 `MySQL/data/Norman_Angell.yaml` 完全一致；只收 page.md 明载关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Beatrice Cuvellier | 无向 | 1899 结婚，后分居 |
| influence | F. R. Leavis | 无向 | 其 The Press and the Organisation of Society 被 Leavis 1930 小册子引为来源 |
| influence | Vera Brittain | 无向 | Brittain 多次引用其「智识的道德义务」论断 |
| colleague | Harold Wright | 无向 | 1931 合著 Can Governments Cure Unemployment? |
| controversy | G. G. Coulton | 无向 | 一战期间撰文自称驳斥其小册子 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：清醒、论辩、纸上和平
- **配色**：深青绿（理性与经济论证，manifest 预分配 `#145C54`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeIllusion` 战争幻影 — 玫瑰 `#C4204F`
  - `badgeEcon` 经济论证 — 琥珀 `#E07B30`
  - `badgeIntl` 国际合作 — 靛蓝 `#4C5FD5`
  - `badgePress` 新闻生涯 — 青绿 `#0E7C7B`
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），以「雾中被戳破的圆」呼应幻影母题

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover 共享封面）
01  封面 — 以笔揭露战争幻象 / Sir Norman Angell 1872–1967 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像/装饰圆 + 右信息网格（生卒、本名、国籍、教育、任职、荣誉、核心领域）
03  核心事业概览 — 大幻影 / 国际合作 / 议员生涯 / 经济教育
04  早年：从林肯郡到美国西部 (1872–1898) — 六个孩子、日内瓦大学、17 岁移民、多份底层职业
05  巴黎新闻人 (1898–1914) — Daily Messenger、Éclair、德雷福斯事件通讯、Daily Mail 巴黎主编
06  The Great Illusion（核心贡献页）— 1909 小册子→1910 成书、经济一体化论点、1913 版 Synopsis 引文
07  被误读的预言 — 「战争不可能」之误解、一战后的嘲讽与平反
08  和平组织者 — UDC 1914、国联协会执委、Abyssinia Association 会长
09  议员岁月 (1920–1935) — 工党、Bradford North、1931 爵士、三度落选
10  The Money Game：经济教育实验 (1928)
11  1933 诺贝尔和平奖 — 获奖理由 + 1935 演讲 Peace and the Public Mind
12  荣誉与遗产 — 奖章 1983 拍卖、帝国战争博物馆收藏、Northey Island 隐居
13  遗产：从大幻影到相互依赖的世界
14  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照物理学家标杆 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）可整体复用标杆 tex 骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Angell 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 姓名口径 | 本名 Ralph Norman Angell Lane，后以 Angell 为唯一姓氏；正文统一用 Norman Angell，封面可加 Sir |
| 生年噪声 | frontmatter date_of_birth 有 1872-12-26 / 1874-12-26 / 1874-01-01 三值，以正文与 infobox 的 **1872-12-26** 为准 |
| 「战争不可能」误解 | 他从未主张大战不可能；是「战争徒劳/自我伤害」论。被广泛误读并遭学界与舆论嘲讽——须写明这是误解，勿把误解写成其主张 |
| 小册子与成书 | 1909 年《Europe's Optical Illusion》是小册子，1910 年《The Great Illusion》是成书；电影《La Grande Illusion》片名取自其小册子 |
| 1913 版引文 | 仅 1913 年版 Synopsis 段有 page.md 载英文原文，可入引文框；其余著作仅列书名勿引 |
| 分居而非离异 | 1899 结婚后「separated（分居）」，独居最后 55 年——勿写成离婚 |
| 奖章去向 | 1983 伦敦 Sotheby's 拍出 £8,000，买家是其侄 Eric Angell Lane，现藏 Imperial War Museum——勿写「下落不明」 |
| 议会席位 | 1929–31 MP for Bradford North；1931-09-24 宣布不再寻求连任；1922/1923/1935 三次参选均落败——勿混淆年份 |
| 无载禁写 | 无博士导师/门生可写；与国联官员个人互动 page.md 无载禁写；诺奖是否有共享者——1933 为独得 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| The Great Illusion | 《大幻影》 | 勿译作「伟大的幻觉」 |
| economic interdependence | 经济相互依赖 | 论点核心词 |
| Union of Democratic Control | 民主控制联盟 | 一战时英国压力团体 |
| League of Nations Union | 国际联盟协会 | 与国联本体区分 |
| optical illusion | 视错觉/幻象 | 母题词汇 |
| militarism | 军国主义 | 勿泛化为「军备」 |
| collective security | 集体安全 | 1930 年代主张 |
| homesteader | 宅地法移民 | 美国早年经历 |
| sub-editor | 副编辑 | 巴黎报业职务 |
| Knight Bachelor | 下级勋位爵士 | 1931 获封 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **With Me** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 沉静 / 陪伴感 / 纪录片
- **匹配理由**:
  - 「陪伴感」呼应其孤而不独的一生——与 Beatrice 分居后独居 Northey Island 五十五年，以笔与世界为伴
  - 「沉静」匹配其论证型人格——不诉诸激情而诉诸经济学算术
- **本地路径**: `music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav`
- **时长**: 以 ffmpeg `-shortest` 对齐视频长度

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Norman_Angell/page.md` | 本地 Wikipedia 正文（唯一事实源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `MySQL/data/Norman_Angell.yaml` | 入库数据（fields/relations 与本文件一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步向我汇报。**
