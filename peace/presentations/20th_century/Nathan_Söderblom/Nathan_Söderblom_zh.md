# 和平奖得主立传提示词（OpenPeace · Nathan Söderblom）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Nathan Söderblom（1930 诺贝尔和平奖，乌普萨拉大主教、普世教会合一运动奠基人之一）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。
> 标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按本人物执行。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享仓库下的 peace 侧）。
- **本实例**：Nathan Söderblom（纳坦·瑟德布卢姆），1930 诺贝尔和平奖得主，瑞典信义宗乌普萨拉大主教（1914–1931）。
- **设计哲学**：Söderblom 是本批唯一的神职人员——立传重点在**教会合一与和平的交汇**：巴黎牧师生涯、乌普萨拉教席、大主教任上的战时人道工作，以及 1925 斯德哥尔摩「Life and Work」大会。模板骨架沿用「身份信息页 + 领域结构化表达」，领域表换为「事业领域表」。

---

## 二、背景信息 【人物专属】

- **目标人物**：Lars Olof Jonathan Söderblom（1866-01-15 ~ 1931-07-12，享年 65 岁）
- **气质关键词**：**普世合一运动的奠基人、战时人道的牧者、以合一促和平的大主教** —— 1930 诺贝尔和平奖获奖理由：
  > "for promoting Christian unity and helping create 'that new attitude of mind which is necessary if peace between nations is to become reality'."（表彰他推动基督教会的合一，并帮助培育“若要国家间和平成为现实所必需的那种新心态”）
- **设计母题**：**合一的拱顶（the arch of unity）**。教会拱顶由多根立柱共同支撑——恰如 Söderblom 毕生推动的教派合一；视觉母题可用「大教堂拱顶与多色立柱」「烛光汇聚」，呼应「教会合一承载国家间和平」。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Nathan_Söderblom/page.md`（Wikipedia 全文 + frontmatter，已抓取）
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 本名：Lars Olof Jonathan Söderblom（"Nathan" 为惯用名）。
- 生卒：1866-01-15 生于瑞典 Trönö（Söderhamn 市，Gävleborg 县）~ 1931-07-12 逝于乌普萨拉，享年 65 岁；信义宗圣历 7 月 12 日纪念日（Calendar of Saints）。
- 国籍：瑞典。
- 家庭：父 Jonas Söderblom 为教区牧师（Söderblom 子承父业）；母 Nikolina Sophie Blûme；娶 Anna Forsell（Anna Söderblom，1870–1955）；育有 12 名子女，其中包括 Staffan Söderblom。
- 教育：1883 年入乌普萨拉大学；1893 年回国后按立牧师（由 Gottfrid Billing 按立）。
- 任职轨迹（全部 page.md 明载）：
  1. 1892–1893 乌普萨拉学生会副主席、主席；
  2. 1894–1901 瑞典驻巴黎使馆牧师——教区会众包括 Alfred Nobel（1833–1896）与 August Strindberg（1849–1919）；1897 年主持诺贝尔纪念礼拜；
  3. 1901–1914 乌普萨拉大学神学院教席教授；
  4. 1912–1914 兼任莱比锡大学宗教学教授；
  5. 1914-05-20 当选乌普萨拉大主教（瑞典信义宗首座），1914-11-08 由 Gottfrid Billing 坚振就任，在任至 1931。
- 关键荣誉：1930 诺贝尔和平奖（独享）；frontmatter 载 Tartu/Oslo/Berlin/Oxford/St Andrews/Umeå/Geneva 等名誉博士与法国荣誉军团骑士（仅 frontmatter 有载，正文未展开，立传可列名录）。
- 核心事业清单：
  1. 一战期间呼吁全体基督教领袖为和平与正义工作，并致力于改善战俘与难民境遇；
  2. 1920 年代领导基督教「Life and Work」运动，被视为普世教会合一运动（ecumenical movement）主要奠基人之一；
  3. 开启瑞典国教会与英格兰教会之间的互领圣餐（intercommunion）运动；
  4. 1925 年主持斯德哥尔摩「Life and Work」世界大会（World Conference of Life and Work）；
  5. 与英格兰普世运动家 George Bell（坎特伯雷座堂主任、奇切斯特主教）为紧密同工。
- 著作（Selected works）：*Den enskilde och kyrkan* (1909)、*Helighet och kultur* (1913)、*Gudstrons uppkomst* (1914)。
- 关键时间线（15 节点）：1866 生于 Trönö → 1883 入乌普萨拉大学 → 1892–93 学生会主席 → 1893 按立牧师 → 1894–1901 巴黎使馆牧师（Nobel/Strindberg 会众）→ 1897 主持诺贝尔纪念礼拜 → 1901 乌普萨拉教席 → 1912–14 兼莱比锡教授 → 1914-05 当选大主教 → 1914-11 就任 → 一战和平呼吁 + 战俘难民救济 → 1920s Life and Work 运动 → 1925 斯德哥尔摩世界大会 → 1930 诺贝尔和平奖 → 1931-07-12 逝世。

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | ecumenism | 普世教会合一运动 | Life and Work 运动、主要奠基人之一 | 核心页 |
| 1 | peace advocacy | 和平倡导 | 一战和平呼吁、1930 和平奖 | 诺奖页 |
| 2 | theology | 神学 | 信义宗神学家、教会合一的教理基础 | 教席页 |
| 3 | religious studies | 宗教学 | 1912–1914 莱比锡大学宗教学教授 | 莱比锡页 |
| 4 | pastoral ministry | 牧养事工 | 巴黎使馆牧师、大主教牧职 | 巴黎页 |

- 入库：`person_field` 5 条（rank 0–4），与下方 yaml `fields` 完全一致。

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 一致】

> 只收 page.md 明载关系；metadata-only 一律不入库。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Jonas Söderblom | 无向 | 父亲，教区牧师，Söderblom 子承父业 |
| spouse | Anna Söderblom | 无向 | 本姓 Forsell（1870–1955），育有 12 名子女 |
| parent-child | Staffan Söderblom | 无向 | 十二名子女中 page.md 具名者 |
| colleague | George Bell | 无向 | 英格兰普世运动家（坎特伯雷座堂主任/奇切斯特主教），紧密同工 |

- 说明：Alfred Nobel / August Strindberg 为巴黎教区会众关系（牧养对象），非合作或影响关系，不入库；Gottfrid Billing 为按立礼主持者，非师承，不入库。
- 入库：`person_relation` 4 条；parent-child 按库内惯例不写 direction（自动 from<to 归一，note 注明父子/父子关系）。

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#0F4C5C`（大教堂深青——北欧教会的庄重与和平愿景，manifest 预分配，勿改）
- **辅色**：诺奖香槟金 `#C9A227`
- badgeA–D 四分类色（事业领域）：
  - `badgeA` 普世合一 — 拱顶金 `#B08D3E`
  - `badgeB` 和平倡导 — 鸽青 `#2E7D6E`
  - `badgeC` 神学与宗教学 — 经卷紫 `#5B4A78`
  - `badgeD` 牧养事工 — 牧野蓝 `#3E6E8C`
- **背景母题**：稀疏烛光与拱顶线条色块，呼应「合一的拱顶」。

### 第 6 步：规划幻灯片序列 【人物专属，共 16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 合一的拱顶 / Nathan Söderblom 1866–1931 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 本名、生卒、家庭、教育、圣职轨迹、荣誉
03  核心事业概览 — 巴黎牧师 / 乌普萨拉教席 / 大主教 / Life and Work / 斯德哥尔摩大会
04  早年：牧师之子 (1866–1883) — Trönö 村、父业启蒙
05  乌普萨拉求学 (1883–1893) — 学生会主席、1893 按立
06  巴黎使馆牧师 (1894–1901) — Nobel 与 Strindberg 的牧者、1897 纪念礼拜
07  神学教席 (1901–1914) — 乌普萨拉神学院
08  莱比锡教授 (1912–1914) — 宗教学讲席
09  乌普萨拉大主教 (1914) — 当选与就任
10  战时牧者 (1914–1918) — 和平呼吁、战俘与难民救济
11  Life and Work 运动 — 合一运动的主要奠基人（核心页）
12  1925 斯德哥尔摩世界大会 — 主持 Life and Work 世界会议
13  1930 诺贝尔和平奖 — 官方理由（独享）＋「新心态」引文
14  遗产：从斯德哥尔摩到普世教会 — 圣历纪念日与合一运动传承
15  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 版式：每页 `\newcommand{\xxxslide}` 定义；`make` 后 `pdftoppm` 截图查溢出；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距。
- **Söderblom 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 本名与惯用名 | 本名 Lars Olof Jonathan Söderblom，惯用 Nathan；封面与正文统一用 Nathan，身份页注本名 |
| Strindberg 生卒 | page.md 内联写 1849–1911，导语段写 1849–1919（原页面即两说）；立传引 Strindberg 年份时以 1849 为准，卒年两说并存或回避 |
| Nobel 关系 | Nobel/Strindberg 是其巴黎教区会众，**牧养关系非合作/影响关系**，禁写「好友/合作者」 |
| 按立者 | Gottfrid Billing 主持 1893 按立与 1914 坚振，非博士导师，禁挂 advisor-student |
| 大主教就任 | 1914-05-20 当选、1914-11-08 就任，两个日期勿混 |
| 合一运动定位 | 「主要奠基人之一」（one of the principal founders），勿写成「唯一创始人」 |
| 获奖理由 | 1930 为 Söderblom 独享；理由内嵌单引号引文 'that new attitude of mind...' 为官方原文，须保留原样 |
| 名誉博士 | 仅 frontmatter 有载（Tartu/Oslo/Berlin/Oxford/St Andrews/Umeå/Geneva），立传列名录即可，勿展开叙事 |
| 政治敏感 | 一战交战国、教会与国家关系只作 page.md 明载客观记录，不加评价 |
| 无载禁写 | 12 名子女仅 Staffan 具名，其余不写；Anna 生平细节 page.md 未载不写 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| ecumenism | 普世教会合一运动 | 亦译「普世运动」 |
| Archbishop of Uppsala | 乌普萨拉大主教 | 瑞典信义宗首座 |
| Primate of Sweden | 瑞典首席主教 | 大主教的另一头衔 |
| Life and Work | 「生活与工作」运动 | 1920s 基督教和平与社会行动运动 |
| intercommunion | 互领圣餐 | 与英格兰教会的开启性进展 |
| Church of Sweden | 瑞典国教会 | 信义宗 |
| Calendar of Saints | 圣徒历 | 信义宗 7 月 12 日纪念日 |
| ordination | 按立（圣职） | 1893，勿译「授圣餐」 |
| consecration | 坚振/祝圣 | 1914-11-08 就任礼 |
| World Conference of Life and Work | 生活与工作世界大会 | 1925 斯德哥尔摩 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Daylight** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 明亮 / 晨光 / 磅礴
- **匹配理由**：从战壕年代的黑暗呼吁到 1925 斯德哥尔摩的烛光汇聚，Söderblom 的工作是把教派分裂的「长夜」引向合一的「天光」；"Daylight" 的明亮气质匹配其合一愿景与 1930 年的和平荣誉。
- **本地路径**：`music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav` → 复制到 `peace/presentations/20th_century/Nathan_Söderblom/Daylight.wav`
- **时长**：以实际文件为准，ffmpeg `-shortest` 自动对齐。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Nathan_Söderblom/page.md` | 本地 Wikipedia 正文 + frontmatter（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（一~五节） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改） |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步向我汇报。**
> **红线：无载禁写；引语仅限 page.md 原文；政治与宗教内容只作客观记录。**
