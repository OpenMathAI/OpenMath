# 和平奖得主立传提示词（OpenPeace 21 世纪批次：Martti Ahtisaari）

> 本文件是 OpenPeace 项目 21 世纪诺贝尔和平奖批次的人物专属立传提示词。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放和平奖得主人物史（OpenMathAI 共享仓库 `peace/` 侧）。
- **模板来源**：综合数学家/物理学家侧标杆（Kenneth G. Wilson 提示词结构）与和平奖侧 20 世纪批次实战经验。
- **本实例**：Martti Oiva Kalevi Ahtisaari（马尔蒂·阿赫蒂萨里，2008 诺贝尔和平奖独得）。
- **设计哲学**：和平奖得主立传同样必须有「身份信息页」（Identity / Bio 速览页），且强调「事业领域」的结构化表达——这两点构成模板骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Martti Oiva Kalevi Ahtisaari（1937-06-23 ~ 2023-10-16，享年 86 岁）
- **官方获奖理由（照抄，禁止改写）**：
  > "for his important efforts, on several continents and over more than three decades, to resolve international conflicts."
  > 表彰他三十多年来在多个大洲为解决国际冲突所做的重要努力
  - ★ 2008 年为**独得**（无共享得主），主语 "his"。
- **气质关键词**：**谈判桌上的芬兰人、跨大洲的调解者、沉默的和解工程师**
- **设计母题**：**跨越大陆的调解航线（mediation routes）**。纳米比亚、科索沃、亚齐、北爱尔兰——把多条「调解航线」画成连接各大洲的弧线，呼应获奖理由中 "on several continents and over more than three decades"。
- **本地数据源**：`peace/presentations/pages/21th_century/Martti_Ahtisaari/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：
  - 和平奖侧成品参照：`peace/presentations/20th_century/` 下已立传目录
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）
  - yaml 字段母本：`MySQL/data/Frederick_Sanger.yaml`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准（第一轮已核对，来源 = 本地 page.md） 【人物专属】

- 生卒：1937-06-23 生于维堡（Viipuri，时属芬兰，今俄罗斯维堡）~ 2023-10-16 逝于赫尔辛基，享年 86 岁；葬于 Hietaniemi 公墓；2023-11-10 国葬（赫尔辛基主教座堂）
- 国籍：芬兰
- 家庭：父 Oiva Ahtisaari（祖父 Julius Marenius Adolfsen 1872 年自挪威 Tistedalen 移居芬兰；Oiva 1929 年入籍芬兰、1935 年把姓氏 Adolfsen 芬兰化为 Ahtisaari）；母 Tyyne；独子 Marko（1969 年生）
- 教育：库奥皮奥 Kuopion Lyseo 中学；1952 迁居奥卢，Oulun Lyseon Lukio（1956 毕业）；奥卢师范学院两年制课程（1959 取得小学教师资格）；1963 起就读赫尔辛基经济学院
- 军衔：芬兰陆军预备役上尉（captain）
- 早年经历：1960 赴巴基斯坦卡拉奇，任瑞典国际开发署体育寄宿学校主任；1965 进入芬兰外交部国际发展援助司（与 Jaakko Iloniemi 共建该办公室）
- 外交生涯：1973–1977 驻坦桑尼亚大使（兼辖赞比亚、索马里、莫桑比克）；1977–1981 联合国纳米比亚专员（接替 Seán MacBride）；1978 起兼任秘书长 Kurt Waldheim 代表；1987–1991 联合国主管管理事务副秘书长；1989-04 任联合国特别代表主持 UNTAG（纳米比亚过渡时期援助团）；1992 荣获纳米比亚荣誉公民；1991 芬兰外交部国务秘书；1992–1993 联合国南斯拉夫会议波黑工作组主席、Cyrus Vance 特别助理
- 芬兰总统（第 10 任，1994-03-01 – 2000-03-01）：1993-05-16 社民党初选取胜（61%），第二轮险胜 Elisabeth Rehn；支持芬兰加入欧盟（1994 公投 57% 赞成）；1999 与 Viktor Chernomyrdin 一道斡旋，与 Milošević 谈判结束科索沃战事；2000-03-01 由 Tarja Halonen 接任
- 卸任后：2000 出任国际危机组织（International Crisis Group）主席；2000 创立危机管理倡议组织（Crisis Management Initiative, CMI）；2000–2001 与 Cyril Ramaphosa 共同视察北爱尔兰 IRA 武器存放点；2000–2009 Interpeace 理事会主席；2005-11 受科菲·安南任命为科索沃地位问题特使（UNOSEK 设于维也纳）；2007 获 UNESCO Félix Houphouët-Boigny 和平奖；2009-09 加入 The Elders（2011 与 Jimmy Carter、Gro Harlem Brundtland、Mary Robinson 赴朝鲜半岛，2012 与 Desmond Tutu 赴南苏丹）
- 亚奇：2005-08 《赫尔辛基谅解备忘录》——印尼政府与自由亚齐运动结束近 30 年冲突（page.md 明载协议 2005 年在赫尔辛基签署）
- 诺贝尔和平奖：2008-10-10 宣布，2008-12-10 于奥斯陆市政厅受奖
- 晚年：2020-03 感染新冠后康复；2021-09-02 宣布确诊阿尔茨海默病并退出公共生活；2023-10-16 因并发症在赫尔辛基去世
- 关键时间线（15–20 节点）：1937 维堡出生 → 1940 随母迁库奥皮奥 → 1952 迁奥卢 → 1956 中学毕业 → 1959 教师资格 → 1960 卡拉奇 → 1963 赫尔辛基经济学院 → 1965 外交部 → 1973 驻坦大使 → 1977 纳米比亚专员 → 1987 联合国副秘书长 → 1989 UNTAG → 1991 国务秘书 → 1994 就任总统 → 1999 科索沃斡旋 → 2000 CMI 创立 → 2001 北爱尔兰武器核查 → 2005 亚奇协议+科索沃特使 → 2008 诺贝尔和平奖 → 2009 The Elders → 2021 退出公共生活 → 2023 去世

### 第 4 步：事业领域梳理 + 入库 【与 yaml fields 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | conflict resolution | 冲突解决 | 纳米比亚/科索沃/亚齐/北爱尔兰，2008 诺奖核心 | 核心页 |
| 1 | diplomacy | 外交 | 驻外大使、联合国副秘书长、芬兰外交部国务秘书 | 履历页 |
| 2 | international peacekeeping | 国际维和 | UNTAG 纳米比亚过渡时期援助团 | 维和页 |
| 3 | crisis management | 危机管理 | CMI 创始人、国际危机组织主席 | 组织页 |
| 4 | development aid | 发展援助 | 外交部起点、卡拉奇体育教师岁月 | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml relations 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Eeva Ahtisaari | 无向 | 1968 成婚（婚前姓 Hyvärinen），赫尔辛基大学历史学出身 |
| parent-child | Marko Ahtisaari | 无向 | 独子，1969 年生 |
| colleague | Seán MacBride | 无向 | 1977 接替其出任联合国纳米比亚专员（库内 id=6992 复用） |
| colleague | Kofi Annan | 无向 | 2005 受其任命出任科索沃地位问题特使（库内 id=7347 复用） |
| colleague | Jimmy Carter | 无向 | The Elders 同侪，2011 同赴朝鲜半岛（库内 id=7114 复用） |
| colleague | Viktor Chernomyrdin | 无向 | 1999 年联合斡旋科索沃停火的俄方搭档 |
| colleague | Cyril Ramaphosa | 无向 | 2000–2001 共同视察北爱尔兰 IRA 武器存放点 |
| colleague | Cyrus Vance | 无向 | 1992–1993 任其南斯拉夫问题特别助理 |

### 第 5 步：设计配色方案 【manifest 预分配，勿改】

- **主色**：`#0B5351`（深青——芬兰湖区的沉静与外交的克制）
- **诺奖香槟金**：`C9A227`
- badge 四分类色（建议）：冲突解决 深绯 `#7E1E23`；外交 深蓝 `#1E4E79`；维和 联合国蓝 `#3B7EA1`；危机管理 琥珀 `#E07B30`
- **背景母题**：连接各大洲的细弧线（调解航线），稀疏圆点为谈判地点

### 第 6 步：规划幻灯片序列 【人物专属，可微调；共 15 页 = 共享封面 + 14 帧】

```
00  OpenPeace 项目首页（\input cover 共享页）
01  封面 — 跨大洲的调解者 / Martti Ahtisaari 1937–2023 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、教育、任职、荣誉、核心领域）
03  核心事业概览 — 冲突解决 / 外交 / 维和 / 危机管理
04  早年：维堡—库奥皮奥—奥卢 (1937–1959) — 战争童年、教师养成
05  卡拉奇与发展援助起点 (1960–1972) — 体育教师、外交部发展援助司
06  大使与纳米比亚专员 (1973–1981) — 接替 MacBride、SWAPO 联络
07  UNTAG 与纳米比亚独立 (1989–1992) — 监督选举、荣誉公民
08  联合国副秘书长与芬兰总统 (1987–2000) — 1994 就任、欧盟公投
09  科索沃斡旋 (1999) — 与 Chernomyrdin 联合调解、 Milošević 谈判
10  亚奇和平协议 (2005) — 赫尔辛基备忘录、近 30 年冲突落幕
11  科索沃地位特使与诺贝尔和平奖 (2005–2008) — UNOSEK、2008-12-10 领奖
12  The Elders 与 CMI — 危机管理倡议、北爱尔兰武器核查、元老团出访
13  荣誉与认可 — Houphouët-Boigny 奖、Fulbright 奖、各国最高勋章
14  遗产：职业调解人的典范 + 结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照已有和平奖成品 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）可整体复用同项目已立传目录骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Ahtisaari 专属陷阱表**：

| 陷阱 | 说明 |
|------|------|
| 出生地口径 | 生于维堡（时属芬兰，今俄罗斯维堡）——勿写成"生于俄罗斯"；正文地名用 Viipuri/Vyborg 双注 |
| 独得奖 | 2008 诺贝尔和平奖**独得**，无共享得主；勿与多人获奖年份混淆 |
| 总统任期 | 1994-03-01 至 2000-03-01 恰好两届六年；接任者是 Tarja Halonen（勿写成别人） |
| 纳米比亚专员 | 1977 年接替 Seán MacBride（1974–1976 和平奖得主）——接任关系是 colleague 边，勿写成师承 |
| 2003 年伊拉克言论 | 其为伊拉克战争辩护引发 Juha Sihvola 批评——**只客观记录一句话**，不作评价 |
| UN 管理调查 | 1987–1991 副秘书长任内内部调查与宽限期延长事件——客观简述或略写，勿渲染 |
| 名言引语 | "There can be no peace without America." 为 page.md 明载原文，可用；其余无原文出处的话禁引 |
| 家庭 | 妻子 Eeva（2020 同感染新冠）；独子 Marko（1969）；勿编造其他子女 |
| 学历 | 奥卢师范学院两年制（1959 教师资格）+ 赫尔辛基经济学院进修——**无博士学位**，勿写"经济学博士" |
| 无载禁写 | page.md 未载的调解细节（如具体谈判内幕）禁写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| UNTAG | 联合国纳米比亚过渡时期援助团 | 1989–1990，勿与纳米比亚专员任期混淆 |
| UN Commissioner for Namibia | 联合国纳米比亚专员 | 1977–1981 |
| Crisis Management Initiative (CMI) | 危机管理倡议组织 | 2000 年创立，勿与国际危机组织（ICG）混淆 |
| International Crisis Group | 国际危机组织 | 2000 年起任主席（非创始人） |
| Helsinki Memorandum | 赫尔辛基谅解备忘录 | 2005 亚奇和平协议 |
| Kosovo status process | 科索沃地位问题谈判 | 2005–2007 特使任内 |
| UNOSEK | 联合国科索沃特使办公室 | 设于维也纳 |
| The Elders | 元老团 | 2009 加入，勿写成创始人 |
| Interpeace | 国际和平建设组织 | 2000–2009 理事会主席 |
| Aceh | 亚奇 | 印尼苏门答腊，近 30 年冲突 |

---

## 四、背景音乐选择 【manifest 预分配，勿改】

- **选定曲目**：**Ascension** — Cold Cinema（inspiring-electronic 曲库）
- **风格**: 上扬 / 史诗 / 收束感
- **匹配理由**：
  - "Ascension（攀升）" 匹配其履历弧线——乡村教师之子→大使→联合国副秘书长→总统→诺奖得主，一级一级的谈判桌攀升
  - 收束感匹配其事业的完成度：纳米比亚独立、亚齐停火、科索沃谈判——每一段冲突的"落幕"都是一次 Ascension
  - 上扬气质匹配其名言式外交风格："The one who dares, can"（其家训铭文 Se pystyy ken uskaltaa）
- **本地路径**: `music_audio/inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav`
- **时长**：以实际文件为准，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Martti_Ahtisaari/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步向我汇报。**
