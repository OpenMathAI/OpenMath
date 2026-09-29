# 文学家立传提示词（OpenLiterature：Wisława Szymborska）

> **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist / OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Wisława Szymborska（维斯瓦娃·辛波丝卡），1996 年诺贝尔文学奖得主。
> **设计哲学**：文学家立传延续物理学家模板骨架（身份信息页 + 结构化领域表），以**代表作书影 / 引文框 / 意象图式**替代公式框——对辛波丝卡，即「一粒沙中的世界」：以反讽的精确、悖论与轻描淡写照亮哲理主题，以不足 350 首的小体量成就「与散文作家比肩的销量」；其早年官方意识形态阶段的转折**客观简述、不作政治评价**。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史。
- **本实例**：Maria Wisława Anna Szymborska（维斯瓦娃·辛波丝卡，1923-07-02 ~ 2012-02-01），波兰诗人、随笔家、翻译家，1996 年诺贝尔文学奖得主；一生定居克拉科夫。
- **设计哲学**：以「两千人中的两个」为核心叙事——她在《有些人喜欢诗》中写道「也许两千个人中有两个喜欢诗」，而其诗集在波兰的销量却可媲美一流散文作家；反讽的精确与自嘲的谦逊构成其全部气质，视觉母题围绕「一粒沙看世界」（View with a Grain of Sand）展开。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Maria Wisława Anna Szymborska（维斯瓦娃·辛波丝卡，1923-07-02 ~ 2012-02-01，享年 88 岁）
- **官方获奖理由（Nobel 1996，禁止改写）**：
  > "for poetry that with ironic precision allows the historical and biological context to come to light in fragments of human reality"
  > （表彰其诗歌以反讽的精确，让历史与生命的语境在人类现实的碎片中显现）
- **气质关键词**：**反讽的精确、以轻写重的哲人、最小的体量最大的回声**
- **设计母题**：**一粒沙与两千分之一（a grain of sand & two in a thousand）**。空公寓里的猫（Cat in an Empty Apartment）的非人类视角、一见钟情（Love at First Sight）的偶然哲学、「我家里有个垃圾篓」的自嘲——以沙粒、猫与打字纸构成视觉母题。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Wisława_Szymborska/page.md`
- **Wikipedia**：https://en.wikipedia.org/wiki/Wis%C5%82awa_Szymborska
- **肖像**：第 0 步优先用 page.md 内嵌图 `2011-01-17Komorowski+szymborska.jpg`（2011 白鹰勋章授勋照）；404 则用装饰圆占位。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）、`literature/presentations/cover/`（统一封面 `\input`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1923-07-02 生于波兰中西部 Prowent（今属 Kórnik）~ 2012-02-01 于克拉科夫家中睡梦中离世（肺癌），享年 88 岁；一生以克拉科夫为居。
- **家庭与童年**：父 Wincenty Szymborski 时任爱国慈善家 Władysław Zamoyski 伯爵的管家；Zamoyski 1924 去世后家迁 Toruń，1931 迁克拉科夫；母 Anna（娘家姓 Rottermund）。
- **战时与大学**：1939 德军入侵后在地下课堂继续学业；1943 起做铁路雇员躲避强征德国劳工，同时为英语教科书画插图、写故事与应景诗；1945 入雅盖隆大学，先读波兰文学后转社会学，结识并受米沃什影响；1945-03 首诗「Szukam słowa」（寻找词语）刊于《Dziennik Polski》；1948 因家境辍学（未获学位）。
- **婚姻**：1948 嫁诗人 Adam Włodek，1954 离异（无子女），两人保持亲近直至 Włodek 1986 年去世；1967 起与作家 Kornel Filipowicz 相伴（伴侣关系，无库内白名单类型，不入库）。
- **早年官方意识形态阶段（客观简述，不作评价）**：早年拥护波兰人民共和国官方意识形态——1953 在克拉科夫恐怖审判政治请愿书上签名；处女诗集 1949 因「不符合社会主义要求」未过审查；初版《Dlatego żyjemy》含列宁与建设 Nowa Huta 主题诗；随党的路线从斯大林主义转向「民族」共产主义，她与官方意识形态日渐疏离并否定早年政治作品；1966 才正式退党；自 1957 与巴黎流亡刊物 Kultura 主编 Jerzy Giedroyc 结识并长期供稿；1964 反对共产党支持的针对独立知识分子的抗议公开信；1980 年代向地下刊物 Arka 化名供稿。
- **职业轨迹**：1953 加入《Życie Literackie》（文学生活）编辑部至 1981；1968 起开设书评专栏 Lektury Nadobowiązkowe（非必读书）；1981–83 任克拉科夫月刊 NaGlos 编辑；另将法国巴洛克诗歌与胡格诺诗人 Agrippa d'Aubigné 译为波兰语。
- **关键荣誉**：克拉科夫文学奖 1954；波兰文化部奖 1963；Kościelski 奖 1990；歌德奖 1991；赫尔德奖 1995；波兹南密茨凯维奇大学荣誉博士 1995；**诺贝尔文学奖 1996**（波兰笔会奖同年）；文化功勋金奖 2005；白鹰勋章 2011（波兰最高荣誉）；克拉科夫荣誉市民 1997。
- **身后**：2013 设立 Wisława Szymborska 奖；去世时正在写新诗，未及亲自编定最后一部诗集。
- **核心作品与贡献（5 条）**：
  1. 《Dlatego żyjemy》（1952）与《Pytania zadawane sobie》（1954）——官方意识形态时期的起点（客观呈现）；
  2. 《Wołanie do Yeti》（1957）与《Sól》（1962）——摆脱意识形态、确立反讽与哲理声口；
  3. 《Wszelki wypadek》（1972）与《Wielka liczba》（1976）——成熟期：悖论、非人类视角、日常奇迹；
  4. 《Ludzie na moście》（1986）、《Koniec i początek》（1993）、《Widok z ziarnkiem piasku》（1996）——战争、历史与个体命运的对位；
  5. 《Chwila》（2002）、《Dwukropek》（2005，Gazeta Wyborcza 读者年度最佳）、《Tutaj》（2009）——晚期；遗作《Wystarczy》（2012）与《Błysk rewolwru》（2013）。
- **跨界影响**：《一见钟情》启发基斯洛夫斯基《蓝白红三部曲之红》与电影《向左走向右走》；《Nothing Twice》多次被谱写；晚年与小号手 Tomasz Stańko 合作，Stańko 2013 出专辑《Wisława》纪念。
- **关键时间线（15 节点）**：1923 生于 Prowent → 1931 迁克拉科夫 → 1939–44 地下课堂与铁路雇员 → 1945 首诗发表、入雅盖隆大学 → 1948 辍学、嫁 Włodek → 1949 首书未过审查 → 1952 首部诗集出版 → 1953 入《Życie Literackie》→ 1957 与 Giedroyc 结识 → 1966 退党 → 1968 书评专栏 → 1991 歌德奖 → **1996 诺贝尔文学奖** → 2011 白鹰勋章 → 2012-02-01 逝世。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | lyric poetry | 抒情诗 | 不足 350 首的小体量核心 | 核心页 |
| 1 | philosophical poetry | 哲理诗 | 悖论、矛盾与轻描淡写照亮哲理主题 | 主题页 |
| 2 | war poetry | 战争与历史书写 | 诸多诗篇以战争与恐怖为题 | 主题页 |
| 3 | literary criticism | 文学批评 | 非必读书书评专栏（1968–1981） | 专栏页 |
| 4 | literary translation | 文学翻译 | 法国巴洛克诗歌与 d'Aubigné 译介 | 翻译页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Adam Włodek | 无向 | 1948 年结婚、1954 离异，保持亲近至其 1986 年去世 |
| influence | Czesław Miłosz | 受其影响 | 雅盖隆大学文坛相识并受其影响 |
| colleague | Jerzy Giedroyc | 无向 | 巴黎流亡刊物 Kultura 主编，自 1957 起长期供稿 |
| colleague | Karl Dedecius | 无向 | 德语区波兰文学译介者，使其在德语世界广为人知 |
| colleague | Tomasz Stańko | 无向 | 晚年合作爵士小号手，以其名出专辑 Wisława 纪念 |

> Kornel Filipowicz 系长期伴侣（1967 起）无白名单类型**不入库**；基斯洛夫斯基等仅系作品跨界引用**不入库**；Zamoyski 伯爵系父亲雇主**不入库**。

### 第 4.6 步：代表作品年表 【人物专属，取自 page.md】

| 年份 | 波兰语原名 | 英译名 | 备注 |
|------|-----------|--------|------|
| 1952 | Dlatego żyjemy | That's Why We Are All Alive | 首部诗集（官方意识形态时期） |
| 1954 | Pytania zadawane sobie | Questioning Yourself | 克拉科夫文学奖 |
| 1957 | Wołanie do Yeti | Calling Out to Yeti | 转折起点 |
| 1962 | Sól | Salt | 哲理声口确立 |
| 1967 | Sto pociech | No End of Fun | |
| 1972 | Wszelki wypadek | Could Have | 成熟期 |
| 1976 | Wielka liczba | A Large Number | |
| 1986 | Ludzie na moście | People on the Bridge | |
| 1993 | Koniec i początek | The End and the Beginning | 战争与历史 |
| 1996 | Widok z ziarnkiem piasku | View with a Grain of Sand | 诺奖年英译选集 |
| 2002 | Chwila | Moment | |
| 2005 | Dwukropek | Colon | Gazeta Wyborcza 读者年度最佳 |
| 2005 | Monolog psa zaplątanego w dzieje | Monologue of a Dog Ensnared in History | |
| 2009 | Tutaj | Here | |
| 2012 | Wystarczy | Enough | 遗作 |
| 2013 | Błysk rewolwru | The Glimmer of a Revolver | 遗作 |

### 第 5 步：设计配色 【人物专属】

- **主色**：黛紫 `#372A75`（克拉科夫的暮色与哲理的深度）
- **诺奖香槟金**：`#C9A227`
- badge 四分类色：
  - `badgeSand` 一粒沙 — 沙金 `#B08D2E`
  - `badgeIrony` 反讽 — 玫瑰 `#A34A6B`
  - `badgeCat` 空屋之猫 — 青灰 `#4A6B75`
  - `badgeWar` 历史与战争 — 铁灰 `#4A4A55`
- **背景母题**：柔和气泡 + 一粒放大的沙粒与打字纸上的手稿字迹；晚期页面加入克拉科夫钟楼剪影。

### 第 6 步：规划幻灯片序列 【人物专属，16 页】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 一粒沙中的世界 / Wisława Szymborska 1923–2012 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（全名、生卒、出生地、居所、婚姻、荣誉、核心领域）
03  核心贡献概览 — 抒情诗 / 哲理诗 / 战争书写 / 文学批评 / 文学翻译
04  早年：Prowent 与战时克拉科夫 (1923–1945) — 管家之家、地下课堂、铁路雇员
05  雅盖隆大学与文坛起点 (1945–1948) — 米沃什影响、首诗发表、辍学与初婚
06  意识形态的起点与转折 (1949–1957) — 1949 审查、首部诗集、疏离与否定（客观简述）
07  Kultura 与去意识形态化 (1957–1966) — Wołanie do Yeti、Giedroyc、1966 退党
08  成熟期声口 (1962–1976) — Sól、非人类视角（意象图式①：空屋之猫）
09  书评人辛波丝卡 (1968–1981) — 非必读书专栏、NaGlos
10  1980 年代 (1980s) — Arka 化名供稿、历史书写加深（客观简述）
11  1996 诺贝尔奖 — 反讽的精确（引文框①：获奖理由 EN 原文）
12  一见钟情与跨界 — 基斯洛夫斯基之红（意象图式②：两条平行的路）
13  晚期 (1997–2011) — Chwila、Dwukropek、Tutaj；白鹰勋章 2011
14  身后与遗产 — Wisława Szymborska 奖、Stańko 专辑
15  结尾 — 「我家里有个垃圾篓」：最小的体量，最大的回声
```

> 文学家无公式框：第 8/12/11 页用**意象图式 / 书影框 / 获奖理由原文引文框**替代。

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 波兰语名 | Wisława Szymborska（ł 为 L-stroke，tex 侧用 lsslash 或预置字体）；全名 Maria Wisława Anna Szymborska |
| 获奖理由措辞 | 官方 "for poetry that with ironic precision allows the historical and biological context to come to light in fragments of human reality"，勿改写 |
| 早年意识形态 | 1953 请愿书签名、早期官方主题诗、1966 才正式退党——按 page.md 客观并列，**不作评价、不渲染**；「背叛早年立场」之类定性禁写 |
| 诗作数量 | 不足 350 首（reputation rests on a small body of work）；「我家里有个垃圾篓」是自嘲原话 |
| 菲利波维奇 | Kornel Filipowicz 自 1967 起为伴侣关系——无白名单类型不入库 |
| Włodek | 1954 离异后「保持亲近」至 1986 年去世——勿写成「终老」 |
| 荣誉年份 | 歌德奖 1991、赫尔德奖 1995、白鹰勋章 2011——三段勿混 |
| 跨界引用 | 《一见钟情》启发《红》与《向左走向右走》——写「启发/灵感来源」，勿写成合作 |
| 遗作 | 《Wystarczy》2012、《Błysk rewolwru》2013；她去世时未及亲自编定 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| ironic precision | 反讽的精确 | 获奖理由核心词 |
| paradox | 悖论 | 常用手法之一 |
| understatement | 轻描淡写 | 常用手法之一 |
| View with a Grain of Sand | 《一粒沙看世界》 | 1996 诗集（英译名） |
| Cat in an Empty Apartment | 《空房间里的猫》 | 非人类视角代表作 |
| Love at First Sight | 《一见钟情》 | 启发电影《红》 |
| Lektury Nadobowiązkowe | 非必读书 | 书评专栏 |
| Kultura | 《文化》 | 巴黎流亡月刊 |
| Order of the White Eagle | 白鹰勋章 | 2011 波兰最高荣誉 |
| samizdat | 地下出版 | Arka 刊物供稿 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Daylight** — Alex-Productions
- **匹配理由**:
  - "明快/轻盈" 匹配其反讽的精确 —— 辛波丝卡的重量感恰恰来自以轻盈处理沉重（战争、死亡、历史），Daylight 的明亮底色是「在日常现实的碎片中显现」的声音等价物
  - "清晨" 匹配「两千分之一」的谦逊自嘲 —— 不宏大、不悲情，而是清醒与好奇
  - 与 batch 内已分配曲目无重复（Daylight 用于 1996，明快曲库在 1994-1998 区间未被占用）
- **本地路径**: `music_audio/alex-productions/…/Daylight.wav`（对照 `music_audio/curated_tracks.md` 取实际编号）→ `presentations/20th_century/Wisława_Szymborska/Daylight.wav`
- **时长**: 约 135 秒 > 16 页 × 7 秒 ≈ 112 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Wisława_Szymborska/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `literature/presentations/cover/` | 项目首页模板（统一 `\input`） |
| `MySQL/seed_person.py` | 人物主记录 + 研究领域 + 社会关系入库 |
| `MySQL/data/Wisława_Szymborska.yaml` | 入库 yaml |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
