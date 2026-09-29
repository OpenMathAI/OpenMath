# 和平奖得主立传提示词（OpenPeace · Nicholas Murray Butler）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Nicholas Murray Butler（1931 诺贝尔和平奖，哥伦比亚大学校长、卡内基国际和平基金会主席）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。
> 标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按本人物执行。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享仓库下的 peace 侧）。
- **本实例**：Nicholas Murray Butler（尼古拉斯·默里·巴特勒），1931 诺贝尔和平奖得主（与 Jane Addams 共享），哥伦比亚大学第 12 任校长（1902–1945，43 年任期）。
- **设计哲学**：Butler 代表美国和平运动的「建制派」——通过大学、基金会与国际教育网络推动和平；立传以哥伦比亚校长任期与卡内基国际和平基金会双主线展开。模板骨架沿用「身份信息页 + 领域结构化表达」，领域表换为「事业领域表」。

---

## 二、背景信息 【人物专属】

- **目标人物**：Nicholas Murray Butler（1862-04-02 ~ 1947-12-07，享年 85 岁）
- **气质关键词**：**"Nicholas Miraculous"、43 年校长任期的教育家、和平运动的建制派领袖** —— 1931 诺贝尔和平奖获奖理由（与 Addams 共享同一句；正文补充口径见陷阱表）：
  > "for their assiduous effort to revive the ideal of peace and to rekindle the spirit of peace in their own nation and in the whole of mankind."（表彰他们不懈努力重振和平理想，在本国乃至全人类心中重新点燃和平精神）
- **设计母题**：**学院与讲坛（the academy and the rostrum）**。Butler 的和平事业由大学讲台、基金会圆桌与国际教育网络织成；视觉母题可用「常春藤拱门与地球仪」「讲坛与条约桌」，呼应「以教育涵养国际心智（the international mind）」。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Nicholas_Murray_Butler/page.md`（Wikipedia 全文 + frontmatter，已抓取）
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 生卒：1862-04-02 生于新泽西州伊丽莎白 ~ 1947-12-07 逝于纽约市，享年 85 岁；1945 年 83 岁时几乎完全失明，辞去所有职务，两年后去世；葬于新泽西州帕特森 Cedar Lawn 公墓。⚠️ frontmatter 生卒均有噪声值（1862-01-01、1947-01-01），以 infobox 正文 **04-02 / 12-07** 为准。
- 国籍：美国；共和党人。曾祖父 Morgan John Rhys（威尔士激进派牧师）。
- 教育：哥伦比亚大学（Columbia College）学士 1882、硕士 1883、博士 1884；1885 赴巴黎与柏林游学；在校加入 Peithologian Society。
- 家庭：父 Henry Butler（制造业工人）、母 Mary Butler；1887 娶 Susanna Edwards Schuyler（1863–1903，育有一女），1903 年丧妻；1907 续娶 Kate La Montagne（纽约地产商 Thomas E. Davis 外孙女）。
- 任职轨迹（全部 page.md 明载）：
  1. 1885 秋加入哥伦比亚哲学系教员；
  2. 1887 与 Grace Hoadley Dodge 共同创立纽约教师培训学校（后并入哥大为 Teachers College, Columbia University）并任校长；其附属实验单元后成 Horace Mann School；
  3. 1890–1891 约翰斯·霍普金斯大学讲师；
  4. 1890 年代新泽西州教育委员会成员，协助组建大学入学考试委员会（College Board）；为 Charles Scribner's Sons 主编 The Great Educators 书系；
  5. 1901 哥大代理校长、1902-01-06 正式就任第 12 任校长，任期 43 年（校史最长），1945-10-01 卸任；任内大规模扩建校园，创建哥伦比亚—长老会医学中心（世界首个学术医学中心）。
- 和平与国际事业：
  1. 1907–1912 任莫霍克湖国际仲裁会议（Lake Mohonk Conference on International Arbitration）主席；
  2. 说服 Andrew Carnegie 出资 1000 万美元创办卡内基国际和平基金会（CEIP）；
  3. 主持基金会国际教育与传播板块，创建驻巴黎欧洲分部；1925–1945 任 CEIP 主席；
  4. 1931 与 Jane Addams 共享诺贝尔和平奖——page.md 补充口径：表彰其对《凯洛格—白里安公约》的推动及作为美国和平运动「更趋建制一翼」领袖的工作；
  5. 一战期间主持美国「修复鲁汶大学」全国委员会（图书馆焚毁后重建）；
  6. 1916-12 与老罗斯福等共同购下拉法耶特侯爵故居 Château de Chavaniac 作为纪念基金总部；
  7. Pilgrims Society 主席（1928–1946，促进英美友谊）；美国艺术暨文学学会主席（1928–1941）。
- 政治活动：1888–1936 历届共和党全国大会代表；1912 年副总统 Sherman 于大选前六天去世，Butler 被指定接收其选举人票（共和党仅得犹他/佛蒙特 8 票，列第三）；1916 助 Elihu Root 竞争共和党提名未果；1920 自行争取提名未果；认为禁酒令（Prohibition）是错误，1933 积极参与废除运动；其共和党原则的哲学基础归于 John W. Burgess 与 Alexander Hamilton。
- 关键荣誉：1931 诺贝尔和平奖；意大利王冠大十字、救世主勋章骑士大十字、圣萨瓦勋章、白狮大十字（1926-07-14）、利奥波德大绶、红鹰指挥官、圣毛里求斯与拉撒路骑士大十字等多国勋章；塞格德大学名誉博士（1931）；1938 美国哲学学会会员；哥大哲学图书馆以其命名，身后主图书馆更名 Butler Library。
- 著作要目：*True and False Democracy* (1907)、*The International Mind* (1912)、*The Basis of Durable Peace* (1918)、自传 *Across the Busy Years*（卷一 1939、卷二 1940）等。
- 关键时间线（16 节点）：1862 生于伊丽莎白 → 1882 哥大学士 → 1884 博士 → 1885 巴黎柏林游学 + 入哥大哲学系 → 1887 创立教师培训学校 → 1890–91 霍普金斯讲师 → 1890s College Board → 1902 哥大校长 → 1907–12 莫霍克湖仲裁会议主席 → 1912 替补副总统候选人（指定接收选举人票）→ 一战鲁汶修复委员会 → 1920 争取总统提名 → 1925–45 CEIP 主席 → 1928 艺术暨文学学会主席 + Pilgrims 主席 → 1931 诺贝尔和平奖 → 1945 失明辞职 → 1947-12-07 逝世。

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international peace movement | 国际和平运动 | CEIP 主席 1925–1945、建制派领袖 | 核心页 |
| 1 | higher education administration | 高等教育管理 | 哥大校长 43 年、Teachers College | 校长页 |
| 2 | international arbitration | 国际仲裁 | 莫霍克湖会议主席 1907–1912 | 仲裁页 |
| 3 | philosophy | 哲学 | 哥大哲学系出身与教员 | 早年页 |
| 4 | diplomacy | 外交 | 「教育家兼外交家」的公众角色 | 导语页 |

- 入库：`person_field` 5 条（rank 0–4），与下方 yaml `fields` 完全一致。

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 一致】

> 只收 page.md 明载关系；metadata-only 一律不入库。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Jane Addams | 无向 | 1931 诺贝尔和平奖共同得主 |
| colleague | Elihu Root | 无向 | 1885 游学结识的终身挚友，1916 助其竞争共和党提名 |
| colleague | Theodore Roosevelt | 无向 | 1912 年大选搭档关联与 1916 拉法耶特故居共同购藏者 |
| colleague | Andrew Carnegie | 无向 | Butler 说服其出资 1000 万美元创办卡内基国际和平基金会 |
| colleague | Grace Hoadley Dodge | 无向 | 1887 共同创立纽约教师培训学校（后为哥大 Teachers College） |
| influence | John W. Burgess | 无向 | Butler 自认其共和党原则的哲学基础来源之一 |
| spouse | Susanna Edwards Schuyler | 无向 | 1887 年成婚（1863–1903），育有一女 |
| spouse | Kate La Montagne | 无向 | 1907 年续弦 |

- 说明：Roosevelt 关系为 page.md 明载的多重交集（"Nicholas Miraculous" 称号的由来、1912 指定接收选举人票、1916 故居共同购藏），以 colleague 概括；Taft/Hoover 为政务任命关系不入库；Burgess 与 Hamilton 并提，但 Hamilton 为历史人物思想资源，仅 Burgess 建关系。
- 入库：`person_relation` 8 条；Addams 本批并行入库，按 manifest name 字段形式匹配。

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#283593`（哥大靛蓝——常春藤学院与建制和平的庄重，manifest 预分配，勿改）
- **辅色**：诺奖香槟金 `#C9A227`
- badgeA–D 四分类色（事业领域）：
  - `badgeA` 和平运动 — 基金会金 `#B08D3E`
  - `badgeB` 教育管理 — 常春藤绿 `#2E6E4E`
  - `badgeC` 国际仲裁 — 石板蓝 `#3E5F8C`
  - `badgeD` 政治活动 — 缎带红 `#8C3B4E`
- **背景母题**：常春藤拱门与圆桌细线纹理，呼应「学院与讲坛」。

### 第 6 步：规划幻灯片序列 【人物专属，共 16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 学院与讲坛 / Nicholas Murray Butler 1862–1947 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 生卒、家庭（两任妻子）、教育、荣誉、核心事业
03  核心事业概览 — 哥大校长 / Teachers College / CEIP / 仲裁会议 / 政治活动
04  早年与求学 (1862–1885) — 哥大三级学位、巴黎柏林游学、Elihu Root 挚友
05  创立 Teachers College (1887) — 与 Dodge、Horace Mann School 渊源
06  教育改革者 (1890–1901) — 霍普金斯讲师、College Board、书系主编
07  哥大校长 (1902–1945) — 43 年校史最长任期、医学中心扩建（核心页）
08  莫霍克湖仲裁会议 (1907–1912) — 国际仲裁讲坛
09  卡内基国际和平基金会 — 说服 Carnegie 千万美金、巴黎分部、1925–45 主席
10  政治活动 (1888–1936) — 1912 替补选举人票、1920 提名未果、禁酒令废除
11  战时与国际教育 — 鲁汶修复、Château de Chavaniac、Pilgrims Society
12  1931 诺贝尔和平奖 — 与 Addams 共享、建制派口径
13  "The International Mind" — 著述与思想（1912 同名书）
14  晚年与遗产 (1939–1947) — 自传、失明辞职、Butler Library 命名
15  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 版式：每页 `\newcommand{\xxxslide}` 定义；`make` 后 `pdftoppm` 截图查溢出；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距。
- **Butler 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 日期噪声 | frontmatter 生卒各有 1862-01-01 / 1947-01-01 噪声值，取 infobox **1862-04-02 / 1947-12-07** |
| 共享理由 | 1931 与 Addams 共享同一句官方理由；page.md 另载补充口径（推动《非战公约》+ 建制派领袖），两种口径分开呈现、勿混写进同一引语框 |
| 校长任期 | 1902-01-06 就任、1945-10-01 卸任，共 43 年（校史最长），勿写「1901–1945」（1901 仅为代理校长） |
| 1912 角色 | Sherman 去世后 Butler 被指定**接收选举人票**（8 票，列第三），勿写成「继任副总统候选人获提名」 |
| 争议内容 | 犹太配额（1919）、对极权体制言论（1931）、法西斯与纳粹态度、Pulitzer 否决（1941）等均 page.md 明载——立传可作客观时间线记录，**不加评价、不展开、不引申**；若版面有限可整体略去 |
| 称号归属 | "Nicholas Miraculous" 是老罗斯福的评语（Theodore Roosevelt），勿写错归属人 |
| Hamilton 禁挂 | Alexander Hamilton 只是思想资源（page.md 与 Burgess 并提），**不建关系**；仅 Burgess 入 influence |
| 两任妻子 | Susanna（1887，1903 逝）与 Kate（1907）分别建 spouse，note 注明年份 |
| 引语红线 | 官方获奖理由、totalitarian 言论等仅引 page.md 原文；圣诞贺词仅作事实提及 |
| 无载禁写 | 一女之姓名、Kate 生卒年、领奖行程等 page.md 未载一律不写 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Carnegie Endowment for International Peace | 卡内基国际和平基金会（CEIP） | 简称 CEIP |
| the international mind | 国际心智 | 其 1912 年著作核心概念 |
| Lake Mohonk Conference | 莫霍克湖会议 | 国际仲裁年度会议 |
| Teachers College | 哥大教育学院 | 前身为纽约教师培训学校 |
| electoral votes | 选举人票 | 1912 指定接收，勿误作「获得提名」 |
| Pilgrims Society | 朝圣者协会 | 英美友好组织 |
| College Board | 大学入学考试委员会 | 1890 年代协助组建 |
| Château de Chavaniac | 沙瓦尼亚克城堡 | 拉法耶特故居 |
| Butler Library | 巴特勒图书馆 | 身后由 South Hall 更名 |
| Across the Busy Years | 《忙碌岁月之间》 | 两卷自传 1939/1940 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Tragedy** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 深沉 / 悲怆 / 历史感
- **匹配理由**：Butler 的一生终章带着深沉的挽歌气质——83 岁失明、辞去一切职务、两年后辞世；而其争议缠身的晚年评价亦如低音铺陈。"Tragedy" 的历史纵深感匹配这位建制派和平主义者辉煌与争议并存的一生。
- **本地路径**：`music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav` → 复制到 `peace/presentations/20th_century/Nicholas_Murray_Butler/Tragedy.wav`
- **时长**：以实际文件为准，ffmpeg `-shortest` 自动对齐。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Nicholas_Murray_Butler/page.md` | 本地 Wikipedia 正文 + frontmatter（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（一~五节） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改） |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步向我汇报。**
> **红线：无载禁写；引语仅限 page.md 原文；政治敏感内容只作客观记录、不评价。**
