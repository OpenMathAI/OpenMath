# 和平奖得主立传提示词（OpenPeace 模板实例：Klas Pontus Arnoldson）

> **本文件是 OpenPeace 的「人物专属立传提示词」**，以 Kenneth_G_Wilson_zh.md（0–11 节结构母本）为结构标杆，
> 以 Frederick_Sanger.yaml 为 yaml 字段母本，为 Klas Pontus Arnoldson（1908 诺贝尔和平奖）定制。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分为 Arnoldson 专属内容。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位 【模板通用】

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 体系，与 OpenPhysicist / OpenChemist / OpenMedic 平级）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的任务流程骨架 + 诺贝尔奖立传通用版式。
- **本实例**：Klas Pontus Arnoldson（克拉斯·蓬图斯·阿诺尔德松，1908 诺贝尔和平奖得主之一）。
- **设计哲学**：和平奖得主立传强调「事业与机构」的结构化表达——人物以政治家/记者/和平组织领导人三重身份推动和平，须以身份信息页与事业领域表呈现；体裁上比科学家立传更贴近「公共生活史」。

---

## 二、背景信息 【人物专属】

- **目标人物**：Klas Pontus Arnoldson（1844-10-27 ~ 1916-02-20，享年 71 岁）
- **姓名**：英文 Klas Pontus Arnoldson；中文 克拉斯·蓬图斯·阿诺尔德松
- **国籍**：瑞典（Sweden）
- **诺奖年份**：1908（与丹麦的 Fredrik Bajer 共享）
- **官方获奖理由英文原文**（照抄 nobel_peace_citations.json，禁止改写）：
  > "for their long time work for the cause of peace as politicians, peace society leaders, orators and authors."
- **官方获奖理由中译**（照抄名录 OpenPeace_20th_Century_Nobel_Laureates.md，禁止改写）：
  > 表彰他们以政治家、和平团体领导人、演说家与作家的身份长期为和平事业工作
- **气质关键词**：**北欧铁路出身的和平议员、挪瑞舆论的调停笔手、世界和平的百年预言者**
- **设计母题**：**铁轨的汇合（converging rails）**。Arnoldson 由铁路职员步入政坛，一生推动挪威与瑞典以和平方式解决争端——两条并行的铁轨最终汇入同一方向，呼应其「以和平方式实现国家间和解」的核心事业；封面与章节过渡页可用铁轨/汇流线条纹母题。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Klas_Pontus_Arnoldson/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/`（OpenPeace 共享封面）
  - yaml 字段母本：`MySQL/data/Frederick_Sanger.yaml`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

> 每完成一步汇报，遇到歧义先征求主控意见再继续。
> **数据库同步要求**：包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准 【人物专属，全部取自 page.md，无载禁补】

- 生卒：1844-10-27 生于瑞典哥德堡（frontmatter 另有 1844-10-21 噪声值，以正文 infobox 10-27 为准）~ 1916-02-20 逝于斯德哥尔摩，享年 71 岁
- 国籍：瑞典
- 家庭：page.md 无载（父母、配偶、子女均禁写）
- 教育：page.md 无载（禁写任何学校）
- 任职机构与经历：
  - 铁路职员起步，1871–1881 年升任站长（stationmaster）
  - 1881 年离开铁路界，全身投入政治；同年当选瑞典国会（riksdag）议员
  - 瑞典国会第二院（Second Chamber）议员，1882–1887
- 核心事业清单：
  1. 瑞典和平与仲裁协会（Swedish Peace and Arbitration Society）创始成员
  2. 以著述与演说塑造挪威、瑞典两国公众舆论，支持以和平方式解决两国争端
  3. 议员任内推动国际仲裁议题
  4. 时评与著述：《Is World Peace Possible?》《Religion in the Light of Research》《The Hope of the Centuries》
- 关键荣誉：1908 年诺贝尔和平奖（与 Fredrik Bajer 共享）
- 诺奖演讲：1908-12-10，题为 *World Referendum*（Nobelprize.org 明载）
- 关键时间线（page.md 明载节点，页面单薄，**其余节点禁补**）：
  1. 1844-10-27 生于哥德堡
  2. 1871–1881 铁路职员 → 站长
  3. 1881 离开铁路界投身政治，当选 riksdag 议员
  4. 1882–1887 第二院议员
  5. 瑞典和平与仲裁协会创始成员（年份无载，时间线不标年份）
  6. 著《Is World Peace Possible?》《Religion in the Light of Research》《The Hope of the Centuries》
  7. 长期为挪瑞和平解决争端塑造舆论
  8. 1908 获诺贝尔和平奖（与 Fredrik Bajer 共享）
  9. 1908-12-10 诺奖演讲 *World Referendum*
  10. 1916-02-20 逝于斯德哥尔摩

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `peace/presentations/20th_century/Klas_Pontus_Arnoldson/` 下建 `images/`
- Makefile 设置 `MAIN=Klas_Pontus_Arnoldson_zh`、`VIDEO_NAME=Klas_Pontus_Arnoldson_zh`
- 肖像：page.md 的 images.txt 有 URL 则直接下载（250px 改 500px）；404 或无肖像用装饰圆占位（带姓名首字母）

### 第 4 步：研究领域/事业领域表 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace movement | 和平运动 | 和平团体创始成员与领导人 | 事业概览页 |
| 1 | international arbitration | 国际仲裁 | 以仲裁方式解决挪瑞争端的舆论推动 | 事业页 |
| 2 | journalism | 新闻/时评 | 时评著述，塑造两国公众舆论 | 著述页 |
| 3 | politics | 政治 | riksdag 第二院议员 1882–1887 | 议员页 |

- yaml `fields` 与上表一致（4 条）；入库 `person_field` 带 rank

### 第 4.5 步：社会关系表 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Fredrik Bajer | 无向 | 1908 诺贝尔和平奖共同得主 |
| founder | Swedish Peace and Arbitration Society | 无向 | 瑞典和平与仲裁协会创始成员 |

- 对方 name_en 用 manifest 规范名 `Fredrik Bajer`；机构 stub `Swedish Peace and Arbitration Society` 为 org 占位（primary_occupation 后续由主控统一矫正）

### 第 5 步：配色方案 【模板通用，人物专属色彩】

- **气质**：北欧的克制、铁路的秩序感、跨越世纪的和平信念
- **配色**：主色 `#283593`（深靛蓝，manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + badgeA–D 四分类色
  - `badgeA` 和平运动 — 靛蓝 `#3F51B5`
  - `badgeB` 国际仲裁 — 青绿 `#0E7C7B`
  - `badgeC` 时评著述 — 琥珀 `#E07B30`
  - `badgeD` 政治生涯 — 玫瑰 `#C4204F`
- **背景母题**：铁轨汇流线条（稀疏斜线自两侧向中央收束），呼应设计母题「铁轨的汇合」

### 第 6 步：规划幻灯片序列 【人物专属，10–12 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 铁路出身的和平议员 / Klas Pontus Arnoldson 1844–1916 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、国籍、职业、议会任期、协会、荣誉、诺奖）
03  事业概览 — 和平运动 / 国际仲裁 / 时评著述 / 议会生涯
04  铁路与转身 (1844–1881) — 铁路职员到站长，1881 弃路从政
05  议会岁月 (1881–1887) — riksdag 当选、第二院任期
06  和平组织 — 瑞典和平与仲裁协会创始成员
07  舆论工程 — 塑造挪威与瑞典两国公众舆论支持和平解决争端
08  笔与书 — Is World Peace Possible? / Religion in the Light of Research / The Hope of the Centuries
09  1908 诺贝尔和平奖 — 与 Fredrik Bajer 共享，官方理由 + 1908-12-10 演讲 World Referendum
10  遗产 — 北欧和平传统的先声
11  结尾
```

### 第 7–8 步：Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照标杆 `\profileslide`
- 每写完一页 `make distclean && make`，`pdftoppm` 截图检查溢出/重叠
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标
- 表格页安全负间距：顶部 −0.35cm、`arraystretch` 0.78–0.82

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Arnoldson 专属陷阱表**：

| 陷阱 | 说明 |
|------|------|
| 生年噪声 | frontmatter 有 1844-10-21 与 1844-10-27 两值，以正文 infobox **10-27** 为准 |
| 议会任期 | 当选 riksdag 是 1881；第二院任期是 1882–1887，两个年份勿混写 |
| 协会年份 | 瑞典和平与仲裁协会的创始年份 page.md 无载，禁写具体年份 |
| 获奖理由口径 | 官方理由是 "their long time work"（二人共享、理由同句）；勿把理由改写成个人专属口径 |
| 诺奖演讲 | 演讲题为 *World Referendum*（1908-12-10），是 page.md 明载的唯一演讲信息 |
| 著述勿混 | 三部作品名是时评/著述清单，勿当「获奖作品」 |
| 无载禁写清单 | 父母、配偶、子女、教育、军旅、死亡原因、协会其他成员、与 Bajer 的私人交往——page.md 均无载，一律禁写 |
| 政治敏感红线 | 挪瑞关系仅按 page.md 客观表述「塑造舆论支持和平解决」，不加任何评价性语句 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| pacifist | 和平主义者 | 勿译「反战分子」 |
| riksdag | 瑞典国会 | 保留原名不意译 |
| Second Chamber | 第二院 | 瑞典两院制下院 |
| stationmaster | 站长 | 铁路职业起点 |
| peace society | 和平团体 | 官方理由用词 |
| arbitration | 仲裁 | 与 mediation（调停）区分 |
| World Referendum | 世界公投 | 诺奖演讲标题，保留英文原名 |
| Swedish Peace and Arbitration Society | 瑞典和平与仲裁协会 | 勿与「国际和平局」混淆 |

---

## 四、背景音乐选择 【人物专属，manifest 预分配，勿改】

- **选定曲目**：**Tragedy** — Alex-Productions
- **bgm_path**：`music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav`
- **匹配理由**：深沉悲悯的弦乐气质，匹配一位在两次大战阴影前离世、一生呼吁世界和平却未能亲见其成的「先知型」人物；克制而绵长的叙事感契合其平静的一生。
- **备选**（未采用，仅存档）：PAST（历史感偏冷战语境）、The Flow of Time（时间感重复用曲）。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Klas_Pontus_Arnoldson/page.md` | 本地 Wikipedia 正文（唯一事实来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节母本） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参考 |
| `peace/presentations/cover/` | OpenPeace 共享封面 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |

> **开始执行。每完成一步汇报。**
