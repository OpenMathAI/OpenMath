# OpenPeace 人物立传提示词（实例：Ernesto Teodoro Moneta）

> **本文件是 OpenPeace 项目（诺贝尔和平奖得主立传）的人物立传提示词**，
> 以埃内斯托·泰奥多罗·莫内塔（Ernesto Teodoro Moneta，1907 诺贝尔和平奖）为完整实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Ernesto Teodoro Moneta（意大利记者、加里波第旧部、和平主义者）。
- **设计哲学**：本篇是「从战士到和平主义者」的反差型立传——早年军事经历与晚年和平运动的张力是叙事主轴，用「剑与笔」的双重意象组织全篇。

---

## 二、背景信息 【人物专属】

- **目标人物**：Ernesto Teodoro Moneta（1833-09-20 米兰 ~ 1918-02-10 米兰，享年 84 岁）
- **气质关键词**：**千人远征的老兵、《世纪报》主编、多元中的统一先声**
- **诺奖年份与官方获奖理由**：1907 年诺贝尔和平奖（与 Louis Renault 共享）
  > 中文获奖理由（照抄名录 `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md`，禁止改写）：
  > **「表彰他通过新闻与和平集会（无论公开或私下）推动法国与意大利之间的相互理解」**
- **设计母题**：**折剑为犁与报纸油墨（swords to ploughshares & ink）**——加里波第红衫老兵放下步枪拿起钢笔，视觉上以「军刀与报页」的对比贯穿
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Ernesto_Teodoro_Moneta/page.md`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准（人物专属，第一轮已核对）

- 生卒：1833-09-20 生于米兰（伦巴第-威尼西亚王国，奥地利帝国治下）~ 1918-02-10 逝于米兰（意大利王国），享年 84 岁
  - ⚠️ **日期裁定**：frontmatter `date_of_death` 作 1918-01-30，infobox 正文作 **10 February 1918**——以 infobox 正文为准（1918-02-10），提示词与 yaml 均用此，正文中可加注
- 国籍：Kingdom of Italy（出生时为奥地利帝国属伦巴第-威尼西亚）
- 职业：记者（journalist）、民族主义者（nationalist）、军人（military personnel）、和平主义者（pacifist）
- 教育：frontmatter 仅载 educated_at: Milan；15 岁参加 1848 米兰五日起义，后入伊夫雷亚（Ivrea）军事学院
- 任职：1867–1896 任米兰民主派报纸《Il Secolo》主编（发行人 Edoardo Sonzogno）
- 核心事业清单：
  1. 1848 米兰五日起义（15 岁参战，反奥地利统治）
  2. 1859 加入加里波第「千人远征」（Expedition of the Thousand）
  3. 1866 第三次意大利独立战争中对奥作战（意大利陆军序列）
  4. 1867–1896 主编《Il Seculo》，笔战三十年
  5. 1890 创立伦巴第和平与仲裁协会（Unione Lombarda per la Pace e l'Arbitrato），主张裁军、设想国际联盟与常设仲裁法院
  6. 座右铭 *In varietate unitas!*（多元中的统一）——后来启发了欧盟格言
- 关键荣誉：1907 诺贝尔和平奖（与 Louis Renault 共享）
- 关键时间线：1833 生于米兰 → 1848 五日起义（15 岁）→ 伊夫雷亚军事学院 → 1859 千人远征 → 1866 对奥战争 → 1867 主编《Il Secolo》→ 1890 创立伦巴第和平与仲裁协会 → 1907 与 Louis Renault 共享诺贝尔和平奖 → 1918-02-10 卒于米兰
  - ⚠️ 本页 page.md 较短（仅导语级），可补入的信息以 infobox 与导语为限，**禁从诺奖官网或其他外部记忆扩写事实**

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Ernesto_Teodoro_Moneta/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录既有成品的 Makefile，设置 `MAIN=Ernesto_Teodoro_Moneta_zh`、`VIDEO_NAME=Ernesto_Teodoro_Moneta_zh`

### 第 3 步：收集图片 【人物专属】

- page.md 有两图：1907 年肖像（infobox，`Ernestomoneta_milan.jpg`）与米兰 Porta Venezia 花园的纪念碑照片；肖像经 Commons Special:FilePath 取 500px

### 第 4 步：事业领域梳理 + 入库（fields，与 yaml 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace movement | 和平运动 | 伦巴第和平与仲裁协会，获奖核心 | 概览页 |
| 1 | journalism | 新闻工作 | 1867–1896 主编《Il Secolo》，获奖理由核心 | 概览页 |
| 2 | disarmament | 裁军 | 协会主张裁军 | 概览页 |
| 3 | international arbitration | 国际仲裁 | 设想常设仲裁法院 | 概览页 |
| 4 | italian unification | 意大利统一运动 | 1848/1859/1866 三段军事经历 | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Giuseppe Garibaldi | 无向 | 1859 加入其「千人远征」 |
| co-honored | Louis Renault | 无向 | 1907 诺贝尔和平奖共同得主 |

- 本页 page.md 极简，Garibaldi 与 Renault 是仅有的明载关系（relations=2 为诚实值）；Edoardo Sonzogno 仅为报纸发行人，**禁建关系行**
- 对手方 name_en：Garibaldi 用 'Giuseppe Garibaldi'（新建 stub，不编造 qid）；Renault 用 manifest 规范名 'Louis Renault'（本批对手方，先建 stub 待 Renault 本人 yaml UPD 回填）

### 第 5 步：配色方案（manifest 预分配，勿改）

- **主色**：`#0F4C5C`（青碧——亚得里亚海与老兵的沉静）
- **辅色**：诺奖香槟金 `C9A227`
- badgeA–D：badgeA 和平运动（`#1F6B4E`）、badgeB 新闻（`#B08A2E`）、badgeC 仲裁与裁军（`#1F3A5F`）、badgeD 统一运动（`#8C3B2E`）

### 第 6 步：规划幻灯片序列（10–12 页，本篇材料有限宜精不宜长）

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 1907 诺贝尔和平奖 · 埃内斯托·泰奥多罗·莫内塔 1833–1918 + 四色 badge + 右上肖像
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/国籍/职业/任职/荣誉/核心领域）
03  米兰少年与五日 (1833–1848) — 15 岁起义
04  红衫岁月：千人远征 (1859–1866) — 加里波第、第三次独立战争
05  三十年笔政：Il Secolo (1867–1896) — 民主派主编
06  伦巴第和平与仲裁协会 (1890) — 裁军、国联与常设仲裁法院的设想
07  多元中的统一 — In varietate unitas! 与欧盟格言的渊源
08  1907 诺贝尔和平奖 — 与 Louis Renault 共享、官方理由
09  晚年与纪念碑 (1907–1918) — 逝于米兰、Porta Venezia 纪念碑
10  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表

| 陷阱 | 说明 |
|------|------|
| 卒日裁定 | frontmatter 1918-01-30 vs infobox 1918-02-10——**用 1918-02-10**（infobox 正文口径），可在晚年页加注两说 |
| 获奖理由 | 只写「通过新闻与和平集会推动法意相互理解」；莫内塔获奖理由强调法意相互理解，Renault 是海牙/日内瓦会议，**两人理由句不同，勿互相套用** |
| 共享标注 | 1907 为共享奖（Moneta + Renault），封面与诺奖页必须醒目标注 |
| 战士身份 | 1848/1859/1866 三段军事经历是「从战士到和平主义者」叙事基础，勿省略也勿夸大为「军事家」 |
| 材料有限 | page.md 仅导语级内容：时间线只可列上述 8 节点，**禁从外部记忆补写生平**（如具体战役、文章篇目、家庭） |
| 座右铭 | *In varietate unitas!* 与欧盟格言的关系是 page.md 明文「后来启发」，勿写成「直接采纳」 |
| Sonzogno | 《Il Secolo》发行人，仅新闻业背景人物，禁建关系 |
| 政治敏感红线 | 民族主义者（nationalist）身份只按 page.md 客观表述，不加评价 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Five Days of Milan | 米兰五日 | 1848 起义，勿写「米兰五天」 |
| Expedition of the Thousand | 千人远征 | 加里波第 1860...（注意 page.md 作 1859，照 page.md） |
| Il Secolo | 《世纪报》 | 斜体书名 |
| Unione Lombarda per la Pace e l'Arbitrato | 伦巴第和平与仲裁协会 | 1890 创立 |
| Permanent Court of Arbitration | 常设仲裁法院 | 协会设想的对象，勿写成它促成建立 |
| In varietate unitas! | 多元中的统一 | 拉丁语斜体 |
| co-laureate 1907 | 1907 共同得主 | 与 Louis Renault 共享 |

---

## 四、背景音乐 ✅（manifest 预分配，勿改）

- **选定曲目**: **Daylight** — Alex-Productions
- **匹配理由**: 明亮而不失庄重，匹配「老兵暮年转向和平黎明」的叙事弧线——从 1848 的硝烟到 1907 和平奖的曙光
- **本地路径**: `music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav`
- **时长**: 以 ffmpeg `-shortest` 对齐页数

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Ernesto_Teodoro_Moneta/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 0–11 节结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `MySQL/data/Ernesto_Teodoro_Moneta.yaml` | fields + relations 入库母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。最重要的事：page.md 短篇页，禁扩写。**
