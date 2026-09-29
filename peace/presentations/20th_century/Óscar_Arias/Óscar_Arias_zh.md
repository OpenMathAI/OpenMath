# 和平奖得主立传提示词（OpenPeace 实例：Óscar Arias）

> **本文件是 OpenPeace 项目「诺贝尔和平奖得主立传提示词」的批次实例**，
> 以 Óscar Arias（1987 诺贝尔和平奖，哥斯达黎加总统）为对象。
> 结构母本：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Óscar Arias Sánchez（奥斯卡·阿里亚斯）——两度出任哥斯达黎加总统的和平调停者，以《埃斯基普拉斯 II 号协议》为中美洲战争画上句点。
- **设计哲学**：Arias 立传的核心是**「谈判桌上的和平」（peace at the negotiating table）**——版面以协议签署与地区地图为视觉主线，凸显「政治家型和平奖得主」的制度性成就，同时保留身份信息页与领域结构化骨架。

---

## 二、背景信息 【人物专属】

- **目标人物**：Óscar Arias Sánchez（1940-09-13 生于哥斯达黎加埃雷迪亚，在世）
- **诺奖年份与官方获奖理由**：1987 年诺贝尔和平奖（独得）：
  > "for his work for lasting peace in Central America"
  > （表彰他为中美洲持久和平所做的工作）
  > ※ 中译以名录 `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` 为准，禁止改写。
- **气质关键词**：**谈判桌上的调停者、小国的大外交、务实的发展主义者**
- **设计母题**：**地峡与握手（isthmus & handshake）**——中美洲五国地图轮廓 + 协议签署意象；辅助母题为「小国承担大调停」（哥斯达黎加 1948 年废除军队的和平传统背景按 page.md 实载谨慎使用，无载禁写废除军队细节）。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Óscar_Arias/page.md`

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：核对本地页面与事实基准 【人物专属】

- 事实基准（以本地 page.md 为准）：
  - 生卒（1940-09-13 生于埃雷迪亚省 upper-class 家庭；**在世，无卒日**；frontmatter 生年 1941-09-13 为噪声，以 infobox/正文 1940 为准；祖先含卡塔戈被奴役女性 Ana Cardoso）
  - 教育（San José 圣弗朗西斯学院中学；Boston University（初意学医，返国）；University of Costa Rica 法律与经济学位；1967 赴 London School of Economics；1974 University of Essex 政治学博士）
  - 任职履历（国家计划办公室主任 1971–1974（Figueres 任内）；国家计划部长 1974–1977（Oduber 任内）；立法议会议员 1978-05-01–1981-05-02（Heredia 选区）；总统 1986-05-08–1990-05-08（第 40 任）与 2006-05-08–2010-05-08（第 45 任）；党派 National Liberation Party（PLN，社会民主党））
  - 关键荣誉（Nobel Peace Prize 1987；Princess of Asturias Award for International Cooperation；Philadelphia Liberty Medal；Martin Luther King Jr. 和平奖；Albert Schweitzer 人道主义奖；Premio de las Américas；Jackson Ralston 奖；50+ 荣誉学位含 Harvard/Princeton/Dartmouth；2003 当选国际刑事法院受害者信托基金董事会）
  - 核心事业清单（见第 4 步）
  - 关键时间线（15 节点：1940 出生 → 1971 计划办公室主任 → 1974 计划部长 → 1974 Essex 博士 → 1978 议员 → 1986 首任总统 → 1987-08《埃斯基普拉斯 II 号协议》签署（Esquipulas II Accords）→ 1987-12-10 诺贝尔和平奖 → 1989-90 尼加拉瓜与 1990-93 萨尔瓦多和平协议吸收其方案要点 → 1990–2006 在野岁月 → 2000/2003 连任禁令诉讼 → 2006 二度就任（1.2% 险胜 Ottón Solís）→ 2007-06-01 与中华人民共和国建交 → 2008 暂失声（声带囊肿）→ 2009 洪都拉斯宪法危机调停（七点方案）→ 2017/2019 Crucitas 案与性侵指控相继获判不起诉/撤销（仅客观记录）→ 2025 美国撤销其签证（仅客观记录））
- 政治敏感事实的口径：2007 建交换档、劝促达赖喇嘛推迟访问、2009 洪都拉斯危机、2017/2019 司法指控、2025 签证撤销与对特朗普的评论等**一律只作 page.md 明载的客观事实记录，禁加评价，禁大段引用**

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Óscar_Arias/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 设置 `MAIN=Oscar_Arias_zh`（文件系统建议 ASCII 主名，目录保留 Óscar_Arias）并核对 `\input` 路径

### 第 3 步：收集图片 【人物专属】

- 优先从 `images.txt` 选真实肖像（infobox 2018 照或 1980s OscarArias.jpg）
- 下载失败则用装饰圆占位（Commons → REST API 回退）

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

**Arias 的事业领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace mediation | 和平调解 | Esquipulas II 与 2009 洪都拉斯调停，1987 诺奖核心 | 封面、调停页 |
| 1 | democratic governance | 民主治理 | 两任总统、推动中美洲议会 | 总统页 |
| 2 | international diplomacy | 国际外交 | Contadora 支持、建交换档、ICC 信托基金 | 外交页 |
| 3 | economic development | 经济发展 | 非传统农业与旅游转型、计划部长履历 | 总统页 |
| 4 | education reform | 教育改革 | 重设中小学标准化考试 | 总统页 |

#### 4.1 入库操作

- 新建/更新 `people` 主记录（`name_en='Óscar Arias'`，manifest DATA 规范名），`primary_occupation='politician'`、`has_social_data=1`、`has_biography=0`
- 关联职业 `politician`（rank 0）、`activist`（rank 1）；国籍 `Costa Rica`
- 将 5 个领域写入 `person_field`（带 rank），缺失领域先建字典项

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Margarita Penón Góngora | 无向 | 1973 成婚，1993 离异 |
| spouse | Suzanne Fischel Kopper | 无向 | 2012 成婚 |
| colleague | John Biehl | 无向 | 英国求学时期同侪，为诺奖游说出力 |
| colleague | Rodrigo Madrigal Nieto | 无向 | 诺奖游说伙伴 |

#### 4.5.1 入库操作

- 以 `name_en='Óscar Arias'` 为中心写入 `person_relation`；两任 spouse 均入库并注明年份
- 对手方 name_en 先查库沿用库内形式；缺失人物先建占位（`has_biography=0`）
- 无载禁写：Zelaya/Micheletti（调停对象非社会关系）、Solís（竞选对手）、Oduber/Figueres（仅上下级任职）、达赖喇嘛（推迟访问事件）、两名子女（仅具数量未具名）均不入库

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **配色**：manifest 预分配主色 **深绿 `#145C54`** + 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeMed` 和平调解 — 深红 `#A63A2B`
  - `badgeGov` 民主治理 — 青绿 `#0E7C7B`
  - `badgeDip` 国际外交 — 琥珀 `#E07B30`
  - `badgeEco` 经济与教育 — 紫 `#52307C`
- **背景母题**：中美洲地峡轮廓线 + 签署笔触 + 柔和气泡

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 中美洲的调停者 / Óscar Arias 1940– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生年、出生地、教育、两任总统任期、荣誉、核心领域）
03  核心事业概览 — 和平调解 / 民主治理 / 国际外交 / 经济发展 / 教育改革
04  早年与求学 (1940–1974) — 埃雷迪亚、BU 弃医、UCR 法与经济、LSE、Essex 博士
05  政坛阶梯 (1971–1986) — 计划办公室、计划部长、议员、1986 当选
06  中美洲危机 — 萨尔瓦多/危地马拉/尼加拉瓜内战格局（按 page.md 客观陈述）
07  Esquipulas II 与和平方案 — 外国撤出、停止援助游击队、民主原则、社会重建
08  1987 诺贝尔和平奖 — 获奖理由原句 + Biehl/Madrigal 游说 + 方案要点被后续协议吸收
09  第一任总统的经济转型 (1986–1990) — 传统作物→非传统农业与旅游、中美洲议会倡议
10  在野与连任之战 (1990–2006) — 1969 禁令、2003 判决、2006 险胜 1.2%
11  第二任总统 (2006–2010) — 建交换档（仅客观一句）、教育改革、美洲峰会演讲
12  2009 洪都拉斯调停 — 七点方案、双方立场（仅客观记录）
13  争议与司法 — Crucitas 案 2019 撤销、2019–2020 指控与最终撤销（仅客观事实、禁渲染）
14  遗产：小国的和平外交 — 50+ 荣誉学位、ICC 受害者信托基金
15  结尾 — OpenMathAI 品牌口径
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide`

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Arias 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | 官方措辞 "for his work for lasting peace in Central America"，勿写"因 Esquipulas 协议获奖"的因果化表述；1987 为独得年份 |
| 生年 | 正文/infobox 1940-09-13；frontmatter 1941 为噪声，全文统一 1940 |
| 在世 | 无卒日、无享年；身份信息页与时间线终点留"在世" |
| 全名 | Óscar Arias Sánchez；DATA 规范名/封面用 "Óscar Arias"，正文首现给全名 |
| 协议名称 | Esquipulas II Accords（《埃斯基普拉斯 II 号协议》），勿与 Esquipulas I 混写；1987-08 签署细节 page.md 未载日期者禁编 |
| 方案结局 | "其方案未被正式采纳，但关键概念反映在萨尔瓦多（1990–93）与尼加拉瓜（1989–90）的和解协议中"——因果与程度措辞按原文，勿写"他的计划结束了战争" |
| 2006 选举 | 手工重新计票后以 18,169 票（1.2%）险胜 Ottón Solís，恰过 40% 单轮门槛——数字勿错 |
| 建交换档 | 2007-06-01 与中华人民共和国建交、同时终止对台承认（第 167 个国家）——一句客观记录，禁展开两岸评价 |
| 达赖喇嘛事件 | "劝促推迟访问"仅作事实记录，禁任何立场表述 |
| 司法指控 | Crucitas 案（2017 起诉→2019-10 全案释放）与 2019 性侵指控（2020-12 撤销、后因申诉人请求最终撤销）全部只作程序性事实记录， Arias 一贯否认，禁写结论性评价 |
| 2025 签证 | 美国国务院撤销签证、Arias 归因于其任内对华关系——客观记录其本人说法（Facebook 评论引语勿大段引用） |
| 连任禁令 | 1969 宪法修正案禁止前总统再任；2003-04 判决推翻"非连续连任"禁令；Monge 斥为"国家打击"——多方观点并列 |
| 子女 | 仅"2"个、未具名，不入库不展开 |
| 著作 | 《El camino de la paz》(1989) 等西班牙语书名勿意译改写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Esquipulas II Accords | 埃斯基普拉斯 II 号协议 | 1987 中美洲和平协议 |
| Contadora Group | 孔塔多拉集团 | 中美洲斡旋集团 |
| Central American crisis | 中美洲危机 | 冷战背景术语 |
| National Liberation Party | 民族解放党 | 缩写 PLN，社会民主党 |
| Central American Parliament | 中美洲议会 | Parlamento Centroamericano |
| mediator | 调停者 | 2009 洪都拉斯危机身份 |
| Sala IV | 第四庭（宪法法庭） | 哥斯达黎加最高法院宪法庭 |
| non-consecutive re-election | 非连续连任 | 2003 判决关键概念 |
| Trust Fund for Victims | 受害者信托基金 | 国际刑事法院下属，2003 入董事会 |
| Economists for Peace and Security | 和平与安全经济学家组织 | 其受托人身份 |
| cash crop | 经济作物 | 咖啡与香蕉 |
| H1N1 | 甲型 H1N1 流感 | 2009-08-11 确诊（健康页，勿写成新冠） |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **With Me** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 沉稳 / 陪伴感 / 坚定
- **匹配理由**:
  - "With Me"（与我同行）契合调停者气质——和平不是独角戏，而是把对手各方"请到同一张谈判桌"的陪伴与坚持
  - 沉稳而坚定基调匹配两任总统、跨越近四十年的政治生涯韧性
  - 收束于 1987 诺奖与后续和平协议的兑现，留有希望
- **本地路径**: `music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav` → `presentations/20th_century/Óscar_Arias/With_Me.wav`
- **时长**: 以实际文件为准，16 页 × 7 秒 ≈ 112 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Óscar_Arias/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `peace/presentations/cover/openpeace_page.tex` | 项目首页模板 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：无载禁写；政治敏感内容只作客观事实记录。**
