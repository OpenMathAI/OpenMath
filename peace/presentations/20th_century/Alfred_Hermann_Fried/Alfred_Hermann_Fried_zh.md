# 和平奖得主立传提示词（OpenPeace 实例：Alfred Fried）

> 本文件是 OpenPeace 项目的「诺贝尔和平奖得主立传提示词」，以 Alfred Hermann Fried（1911 诺贝尔和平奖，和平主义出版人）为完整实例。
> 结构对齐 OpenPhysicist 标杆 `Kenneth_G_Wilson_zh.md`（一~五节）。凡标注【模板通用】可复用，【人物专属】按本人物执行。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Alfred Hermann Fried（阿尔弗雷德·弗里德），1911 诺贝尔和平奖得主（与 Tobias Asser 共享），德国和平运动共同创始人。
- **设计哲学**：和平奖立传以「舆论与组织建设」呈现贡献——Fried 的一生是「办刊 + 建会 + 造语」（Die Waffen nieder!、德国和平学会、世界语教科书），立传以「笔杆子和平主义」为叙事骨架，身份信息页必做。

---

## 二、背景信息 【人物专属】

- **目标人物**：Alfred Hermann Fried（1864-11-11 ~ 1921-05-05，享年 56 岁）
- **气质关键词**：**和平运动的出版家、国际无政府状态的批判者、世界语的推动者**
- **官方获奖理由（英文原文照抄 nobel_peace_citations.json）**：
  > "for his effort to expose and fight what he considers to be the main cause of war, namely, the anarchy in international relations"
  - **中译（照抄名录 OpenPeace_20th_Century_Nobel_Laureates.md，禁止改写）**：表彰他揭露并抗争其所认为的战争主要根源——国际关系中的无政府状态
  - ★ 1911 为共享年份：与 Tobias Asser 同年获奖，两人理由句各自独立，Asser 篇理由不适用于本篇
- **设计母题**：**报刊与火炬（press & torch）**。Fried 以杂志、手册、教科书为武器——视觉语言宜用铅字版面、期刊卷标、燃烧的火炬轮廓。
- **本地数据源**：`peace/presentations/pages/20th_century/Alfred_Hermann_Fried/page.md`（Wikipedia 全文 + frontmatter，事实基准唯一来源）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1864-11-11 生于维也纳（奥地利帝国）~ 1921-05-05 卒于维也纳（享年 56）
- 国籍：奥地利（生于奥地利帝国，卒于奥地利第一共和国时期）
- 家庭：page.md 无载（父母/配偶/子女均无），一律禁写
- 教育：15 岁离开学校，进入书店工作；无大学学历（勿杜撰）
- 任职：书商/出版人/记者（1883 移居柏林，1887 开自己的书店）
- 关键荣誉：Nobel Peace Prize 1911；莱顿大学荣誉博士（frontmatter award_received）
- 核心事业清单：
  1. 1892 与 Bertha von Suttner 共同创办杂志 *Die Waffen nieder!*（《放下武器！》，同名小说 1889 出版后的和平运动机关刊），后继刊为 *Die Friedens-Warte*（《和平瞭望》），在其中阐发其和平主义哲学
  2. 1892 共同创立德国和平学会（Deutsche Friedensgesellschaft）
  3. 现代世界和平组织构想的先驱之一（其主张后体现于国际联盟与二战后的联合国）
  4. 世界语运动 prominent member：1903 出版《国际辅助语世界语教科书》及世界语—德语双向词典（1905 再版）
  5. 1909 与 Paul Otlet、Henri La Fontaine（国际协会联盟中央局）合编 *Annuaire de la Vie Internationale*
  6. 著述：《裁军问题》（1904）、《和平运动手册》（1905/1911）、《泛美》（1910）、《革命和平主义的基础》（1908）、《我的战时日记》四卷（1918–1920）等
- 关键时间线（15–20 节点）：1864 生于维也纳 → 15 岁辍学进书店 → 1883 移居柏林 → 1887 自开书店 → 1889 Suttner《放下武器！》出版 → 1892 共同创办同名杂志 → 1892 共创德国和平学会 → 1903 世界语教科书出版 → 1905 《和平运动手册》 → 1908 《革命和平主义的基础》 → 1909 合编 Annuaire → 1910 《泛美》 → 1911 获诺贝尔和平奖（与 Asser 共享） → 1912 《德皇与世界和平》（Norman Angell 作序） → 一战爆发后移居中立国瑞士，继续倡导国际和平 → 1918–1920 《我的战时日记》四卷 → 1921-05-05 卒于维也纳 → 骨灰葬于 Feuerhalle Simmering

### 第 4 步：研究领域/事业领域表 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | pacifism | 和平主义 | 阐发于 Die Waffen nieder! 与 Die Friedens-Warte 的哲学 | 核心页 |
| 1 | peace movement | 和平运动 | 1892 共创德国和平学会 | 运动页 |
| 2 | journalism | 新闻出版 | 杂志创办人、publicist、战时日记 | 早年页 |
| 3 | Esperanto | 世界语 | 教科书与双向词典作者（1903） | 世界语页 |

### 第 4.5 步：社会关系表（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Tobias Asser | 无向 | 1911 诺贝尔和平奖共同得主 |
| colleague | Bertha von Suttner | 无向 | 1892 共同创办 Die Waffen nieder! 杂志 |
| colleague | Paul Otlet | 无向 | 1909 合编 Annuaire de la Vie Internationale |
| colleague | Henri La Fontaine | 无向 | 1909 合编 Annuaire de la Vie Internationale |
| founder | German Peace Society | 无向 | 1892 共同创立德国和平学会 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：笔锋、警示、乱世中的坚守
- **主色**：深紫 `#52307C`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgePAC` 和平主义 — 靛蓝 `#4C5FD5`
  - `badgeMOV` 和平运动 — 青绿 `#0E7C7B`
  - `badgePRE` 新闻出版 — 琥珀 `#C9821F`
  - `badgeESP` 世界语 — 玫瑰 `#B5495B`
- **背景母题**：铅字颗粒底纹 + 疏朗圆点，呼应「一份和平刊物的年代感」

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 以笔为旗的和平主义者 / Alfred Fried 1864–1921 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/国籍/教育/任职/荣誉/核心领域；家庭栏写「page.md 无载」）
03  核心贡献概览 — 刊物 / 和平学会 / 世界语 / 组织构想
04  维也纳书商少年 (1864–1889) — 辍学、书店、1883 柏林、1887 自开书店
05  Die Waffen nieder!：与 Suttner 同行 (1889–1899) — 1892 杂志、1892 德国和平学会
06  Die Friedens-Warte 与和平主义哲学 — 「无政府状态是战争根源」的论证框架
07  世界语运动 (1903–1905) — 教科书、词典、辅助语理想
08  国际协会网络 (1909) — Otlet、La Fontaine、Annuaire de la Vie Internationale
09  荣誉与认可 — Nobel 1911（共享）、莱顿荣誉博士
10  颁奖时刻 — 理由句原文呈现、与 Asser 共享说明
11  一战与流亡 (1914–1921) — 瑞士岁月、战时日记、《欧洲的复兴》
12  遗产：从和平刊物到国际组织构想
13  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照 OpenPhysicist 成品 `\profileslide`。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Fried 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 卒日两说 | frontmatter 与 infobox 作 1921-05-05，导语句作 4 May 1921——**以 infobox/frontmatter 1921-05-05 为准**，全篇勿混用 |
| 共享年份 | 1911 与 Tobias Asser 共享但理由句独立；Asser 的「国际法」理由禁入本篇 |
| 「其认为的」措辞 | 理由句原文是 "what he considers to be the main cause of war"——这是诺奖委员会对和平主义立场的转述，行文勿删去这一限定、勿写成客观定论 |
| 家庭无载 | 父母/配偶/子女 page.md 无载，一律禁写 |
| 杂志时间线 | *Die Waffen nieder!* 小说（1889，Suttner 著）与同名杂志（1892，两人共办）是两回事，勿混淆 |
| Norman Angell | 仅为其 1912 英译本作序者，非合作关系，禁建关系 |
| 德国和平学会 | 是 Fried 与他人在德国共同创立；勿写成其独自创办，也勿与奥地利和平学会混淆 |
| 骨灰安葬地 | Feuerhalle Simmering（维也纳），勿写成墓地名称即葬礼地点的错误表述 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| pacifism | 和平主义 | 区分 "revolutionary pacifism"（其 1908 书名）译法 |
| anarchy in international relations | 国际关系中的无政府状态 | 获奖理由核心词，直译勿美化 |
| Die Waffen nieder! | 《放下武器！》 | 1889 小说与 1892 杂志同名异物 |
| Die Friedens-Warte | 《和平瞭望》 | 前者的后继刊 |
| German Peace Society / Deutsche Friedensgesellschaft | 德国和平学会 | 1892 共创 |
| Esperanto | 世界语 | 其教科书是早期权威教材 |
| Annuaire de la Vie Internationale | 国际生活年鉴 | 1909 与 Otlet/La Fontaine 合编 |
| publicist | 政论作家/出版人 | 勿误译为「公众人物」 |
| Pan-Amerika | 《泛美》 | 1910 著作，关涉美洲国际组织设想 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Through the Darkness** — Audiomachine（manifest 预分配，勿改）
- **风格**: 戏剧性 / 暗色 / 史诗
- **匹配理由**: Fried 的一生横穿一战深渊——「穿过黑暗」恰是其晚年流亡瑞士、仍执笔呼吁和平的写照；暗色史诗气质匹配其对「国际无政府状态」的长期论战
- **本地路径**: `music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav`
- **时长对齐**: ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Alfred_Hermann_Fried/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `MySQL/seed_person.py` | 研究领域 + 社会关系入库引擎 |

> **开始执行。每完成一步汇报。**
> **最重要的事：每写一页就 make，看到溢出就修；所有事实以 page.md 为准，无载禁写。**
