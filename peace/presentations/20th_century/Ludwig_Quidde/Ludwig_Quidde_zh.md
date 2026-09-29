# 和平奖得主立传提示词（OpenPeace · Ludwig Quidde）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Ludwig Quidde（1927 诺贝尔和平奖，德国和平主义者）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。
> 标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按本人物执行。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享仓库下的 peace 侧）。
- **本实例**：Ludwig Quidde（路德维希·克维德），1927 诺贝尔和平奖得主（与 Ferdinand Buisson 共享）。
- **设计哲学**：和平奖得主多为政治家、活动家与法学家，立传重点不在「研究领域」而在**事业脉络**——历史语境（帝国→魏玛→纳粹流亡）、组织活动、以言论与行动推动和平的轨迹。模板骨架沿用物理学家侧的「身份信息页 + 领域结构化表达」，但领域表换为「事业领域表」。

---

## 二、背景信息 【人物专属】

- **目标人物**：Ludwig Quidde（1858-03-23 ~ 1941-03-04，享年 82 岁）
- **气质关键词**：**批判皇权的史学家、德国和平运动的旗手、流亡不辍的乐观主义者** —— 1927 诺贝尔和平奖获奖理由：
  > "for their contribution to the emergence in France and Germany of a public opinion which favours peaceful international cooperation."（表彰他们为法德两国形成支持和平国际合作的社会舆论做出的贡献）
- **设计母题**：**史笔为刃（the historian's pen）**。Quidde 以一部 17 页的《Caligula》小册子影射德皇，以史学之笔介入现实政治；视觉母题可用「羊皮卷/钢笔与罗马半身像」「书页化作和平鸽」等，呼应「以历史批判捍卫和平」的一生。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Ludwig_Quidde/page.md`（Wikipedia 全文 + frontmatter，已抓取）
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 生卒：1858-03-23 生于不来梅（自由汉萨市，富裕市民商人家庭）~ 1941-03-04 逝于瑞士日内瓦流亡地，享年 82 岁；安葬于慕尼黑。⚠️ frontmatter 死亡日期有 04/05 两个值，以 infobox 正文 **4 March 1941** 为准。
- 国籍：德国（German Reich；1933 起流亡瑞士）。
- 教育：哥廷根大学，1881 年获博士学位（史学；职业生涯起点为历史学家/中世纪史学者）。
- 家庭：page.md 仅载「富裕 bourgeois 商人家庭出身」；Margarethe Quidde 仅出现于 See also 链接，**无载禁写配偶/子女**。
- 政党（三个，均 page.md 明载）：German People's Party（DtVP，1868 年成立，1893 年加入）→ German Democratic Party → Radical Democratic Party。
- 核心事业清单：
  1. 德国和平会（German Peace Society / Deutsche Friedensgesellschaft）活动家——青年时期即参与；
  2. 《Caligula: Eine Studie über römischen Caesarenwahnsinn》（1894，17 页 79 脚注）——表面写罗马帝国，实则影射威廉二世「自大狂」，以真名发表，断送学院生涯；
  3. 因对威廉一世新勋章出言不逊被判「大不敬罪」（lèse majesté）入狱三个月（Stadelheim 监狱）；
  4. 一战后反对《凡尔赛条约》（与军国主义立场不同：1918-11-15 德国和平会宣言主张宽和条件以免埋下新战祸）；
  5. 1933 希特勒上台后流亡瑞士日内瓦，终老于此；
  6. 1934 年 76 岁发表《Landfriede und Weltfriede》，引康德「永久和平论」，主张现代技术的威慑将终结战争。
- 关键荣誉：1927 诺贝尔和平奖（与 Ferdinand Buisson 共享）；1927-12-12 诺奖演讲 "Security and Disarmament"（Nobelprize.org 外链明载）。
- 关键时间线（15 节点）：1858 生于不来梅 → 青年时期读史 + 加入德国和平会 → 1881 哥廷根博士 → 1893 加入 DtVP → 1894 《Caligula》出版 → 学院生涯终结 → 大不敬罪入狱三个月（Stadelheim）→ 1914-1918 一战 → 1918-11-15 和平会宣言 → 反对凡尔赛（和平主义立场）→ 魏玛共和国从政（三党）→ 1927 诺贝尔和平奖 → 1927-12-12 演讲 "Security and Disarmament" → 1933 流亡日内瓦 → 1934 《Landfriede und Weltfriede》→ 1941 逝于日内瓦。

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | pacifism | 和平主义 | 一生主线：德国和平会、反战言论 | 核心页 |
| 1 | medieval history | 中世纪史学 | 博士起点，因《Caligula》中断 | 早年页 |
| 2 | political journalism | 政论写作 | 小册子、时评、批评皇权 | Caligula 页 |
| 3 | international peace movement | 国际和平运动 | 德法舆论与和平国际合作 | 诺奖页 |
| 4 | disarmament | 裁军 | 诺奖演讲 "Security and Disarmament" 主题 | 演讲页 |

- 入库：`person_field` 5 条（rank 0–4），与下方 yaml `fields` 完全一致。

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 一致】

> 只收 page.md 明载关系；metadata-only 一律不入库。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Ferdinand Buisson | 无向 | 1927 诺贝尔和平奖共同得主（共享理由：促成法德两国支持和平国际合作的舆论） |
| controversy | Wilhelm II | 无向 | 《Caligula》(1894) 以罗马皇帝影射德皇「自大狂」，为仕途终结之因 |

- 说明：page.md 明载的批判对象仅 Wilhelm II（影射）；入狱所涉言论针对 Wilhelm I 勋章（见陷阱表），不单独立关系。德国和平会为机构非人物，不入 `person_relation`。
- 入库：`person_relation` 2 条；对手方 Wilhelm II 库内已有记录（id=4954，name_en='Wilhelm II'），Ferdinand Buisson 用 manifest name 字段形式。

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#0E4D64`（深海蓝绿——史学之深邃与流亡之沉静，manifest 预分配，勿改）
- **辅色**：诺奖香槟金 `#C9A227`
- badgeA–D 四分类色（事业领域）：
  - `badgeA` 和平主义 — 鸽青 `#2E7D6E`
  - `badgeB` 史学 — 羊皮褐 `#8C6239`
  - `badgeC` 政论 — 印章红 `#A33B2E`
  - `badgeD` 流亡岁月 — 灰蓝 `#4A6785`
- **背景母题**：稀疏书页/卷轴元素色块，呼应「史笔为刃」。

### 第 6 步：规划幻灯片序列 【人物专属，共 16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 史笔为刃 / Ludwig Quidde 1858–1941 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 生卒、国籍、教育、政党、荣誉、核心事业
03  核心事业概览 — 和平会 / Caligula / 大不敬案 / 和平会宣言 / 流亡著述
04  早年：不来梅商人之家 (1858–1881) — 富裕家庭、读史、反俾斯麦
05  哥廷根博士 (1881) — 史学训练与学术起点
06  《Caligula》(1894) — 17 页 79 脚注的罗马研究、影射之笔
07  因言获罪 — 对威廉一世勋章的评论、大不敬罪、Stadelheim 三个月
08  和平运动与政党 — 德国和平会、DtVP、反军国主义
09  一战与凡尔赛 — 1918-11-15 和平会宣言（引原文两段）
10  魏玛从政 — 三党经历与共和国政治
11  1927 诺贝尔和平奖 — 与 Buisson 共享、官方理由
12  诺奖演讲 "Security and Disarmament" (1927-12-12)
13  流亡日内瓦 (1933–1941) — 纳粹上台后的出走（客观记录）
14  《Landfriede und Weltfriede》(1934) — 康德永久和平、技术威慑论
15  遗产与结尾 — 乐观主义的一生
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 版式：每页 `\newcommand{\xxxslide}` 定义；`make` 后 `pdftoppm` 截图查溢出；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距。
- **Quidde 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 死亡日期 | frontmatter 双值 1941-03-04/05，取 infobox 正文 **1941-03-04** |
| 《Caligula》性质 | 表面「纯罗马帝国研究」，影射是隐含平行（implicit parallel），勿写成「公开点名批判」 |
| 入狱原因 | 判刑因对**威廉一世**新勋章的评论，勿与影射威廉二世的《Caligula》混为一谈 |
| 影射对象 | 《Caligula》指向 Wilhelm II；殿下区分 Wilhelm I / Wilhelm II 同名陷阱 |
| 配偶禁写 | Margarethe Quidde 仅见 See also 链接，page.md 正文无载婚姻，**禁写配偶关系** |
| 共享理由 | 1927 与 Buisson 共享同一句理由（"for their contribution..."），勿写成单独理由 |
| 政党数 | 三个政党（DtVP/DDP/Radical Democratic Party），勿漏也勿与其他党混淆 |
| 引语红线 | 1918-11-15 宣言与 1934 康德段为 page.md 原文可引；其余禁编引语 |
| 政治敏感 | 纳粹上台与流亡只作 page.md 明载客观事实记录，不加评价 |
| 无载禁写 | 学术职称细节、家族成员、领奖行程、晚年社交等 page.md 未载一律不写 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| pacifism | 和平主义 | 贯穿一生主线 |
| pamphlet | 小册子 | 《Caligula》体裁 |
| lèse majesté | 大不敬罪 | 判刑依据，勿译「叛国」 |
| German Peace Society | 德国和平会 | 德文名 Deutsche Friedensgesellschaft |
| megalomania | 自大狂 | 影射的核心指控 |
| German People's Party (1868) | 德意志人民党 | 注意与后来同名党区分（1868 年成立） |
| Weimar Republic | 魏玛共和国 | 1918–1933 |
| disarmament | 裁军 | 诺奖演讲主题 |
| Landfriede und Weltfriede | 《国内和平与世界和平》 | 1934 论文，勿误作书名年份 |
| perpetual peace | 永久和平 | 康德概念，Quidde 引用 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Expedition** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 史诗 / 行进 / 纪录片
- **匹配理由**：Quidde 的一生是一场跨越四个时代的「远征」——从不来梅到哥廷根，从《Caligula》的孤身批判到日内瓦的流亡晚景；"Expedition" 的行进感匹配其和平运动的长途跋涉与不屈乐观。
- **本地路径**：`music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` → 复制到 `peace/presentations/20th_century/Ludwig_Quidde/Expedition.wav`
- **时长**：以实际文件为准，ffmpeg `-shortest` 自动对齐。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Ludwig_Quidde/page.md` | 本地 Wikipedia 正文 + frontmatter（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（一~五节） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改） |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步向我汇报。**
> **红线：无载禁写；引语仅限 page.md 原文；政治内容只作客观记录。**
