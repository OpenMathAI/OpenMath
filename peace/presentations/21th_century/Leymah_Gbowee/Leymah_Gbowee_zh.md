# 和平奖得主立传提示词（OpenPeace 21 世纪批次 4：Leymah Gbowee）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Leymah Gbowee（2011 诺贝尔和平奖得主、利比里亚妇女和平运动领袖）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按目标人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构，移植到和平事业人物。
- **本实例**：Leymah Roberta Gbowee（莱伊曼·罗伯塔·古博薇，在世）。
- **设计哲学**：和平奖得主立传必须有「身份信息页」（Identity / Bio 速览页）与「事业领域」的结构化表达；Gbowee 的一生有「战乱中的母亲 → 组织者 → 和平缔造者」的成长弧线，妇女集体行动的力量是本篇的灵魂。

---

## 二、背景信息 【人物专属】

- **目标人物**：Leymah Gbowee（1972-02-01 生于利比里亚中部，在世）
- **气质关键词**：**妇女非暴力运动的旗手、跨信仰和平的织网者、从创伤中站起来的组织者** —— 2011 诺贝尔和平奖获奖理由：
  > "for their non-violent struggle for the safety of women and for women's rights to full participation in peace-building work"（表彰她们以非暴力方式维护妇女安全、争取妇女充分参与和平建设工作的权利）
- **设计母题**：**白色 T 恤与鱼市祈祷（white shirts and market prayers）**。鱼市里并肩祈祷的基督徒与穆斯林妇女、象征和平的白色衣衫、被"扣留"的谈判大厅——这是比「和平鸽」更贴合 Gbowee 的视觉语言。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/21th_century/Leymah_Gbowee/page.md`（含 frontmatter QID Q107037）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库要求**：研究领域（第 4 步）与社会关系（第 4.5 步）已按本提示词写入 `greatminds` 库（MySQL），Beamer 立传与其并行。

### 第 0 步：核对 Wikipedia 页面与事实基准 【人物专属】

- ✅ 已下载四件套到 `peace/presentations/pages/21th_century/Leymah_Gbowee/`（**事实基准如下**）：
  - 出生（1972-02-01 生于利比里亚中部，在世；全名 Leymah Roberta Gbowee）
  - 国籍（利比里亚）
  - 家庭（六个孩子的母亲：长子 Joshua "Nuku"、长女 Amber、次子 Arthur、次女 Nicole "Pudu"、养女 Lucia "Malou"、幼女 Jaydyn Thelma Abigail，2009-06-02 生于纽约）
  - 教育（Mother Patern College of Health Sciences 社会工作副学士 AA 2001；Eastern Mennonite University 冲突转化硕士 MA 2007；另有联合国训研所/喀麦隆创伤中心等结业证书）
  - 任职（THRP 志愿者 1998；WIPNET/利比里亚协调员；WIPSEN 执行主任（阿克拉）；利比里亚真相与和解委员会提名的专员；Barnard College 社会正义杰出研究员 2013–2015；Oxfam 全球大使 2013；哥伦比亚大学 Earth Institute AC4 妇女和平与安全项目执行主任 2017；Gbowee Peace Foundation Africa 创始人兼主席 2012）
  - 关键荣誉（Nobel Peace Prize 2011；Gruber Women's Rights Prize 2009；JFK Profile in Courage Award 2009；James Parks Morton Interfaith Award 2012；Community of Christ International Peace Award 2016；Golden Plate Award 2019；哈佛肯尼迪学院 Blue Ribbon for Peace 2007；荣誉博士 Rhodes 2012 / American 2018 / Georgetown 2024；Cornell Bartels 世界事务研究员 2022）
  - 核心事业清单（①THRP 创伤疗愈与前童兵康复 ②领导「利比里亚妇女大规模和平行动」2002–2003 ③阿克拉和谈中的妇女施压 ④WIPSEN 与妇女和平网络建设 ⑤回忆录《Mighty Be Our Powers》2011 ⑥Gbowee Peace Foundation Africa 教育赋权）
  - 关键时间线（15–20 节点，见第 6 步幻灯片序列）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/21th_century/` 下创建 `Leymah_Gbowee/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目已有成品的 `Makefile`，设置 `MAIN=Leymah_Gbowee_zh`、`VIDEO_NAME=Leymah_Gbowee_zh`

### 第 3 步：收集图片 【人物专属】

- 查看 `images.txt`；2013 年照（infobox 主图）为首选主肖像；2011 年三人领奖合影可作诺奖页插图
- 无肖像时用装饰圆占位（须在图注写明）

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

> 把事业领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。以下 5 条已入库。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | women's rights | 妇女权利 | 2011 诺奖核心理由 | 核心页、诺奖页 |
| 1 | nonviolent resistance | 非暴力抵抗 | 祈祷、守夜、罢工与静坐 | 运动页 |
| 2 | peacebuilding | 和平建设 | WIPNET/WANEP/WIPSEN 网络建设 | 事业页 |
| 3 | trauma healing | 创伤疗愈 | THRP 起家，前童兵康复 | 早年页 |
| 4 | peace education | 和平教育 | Gbowee Peace Foundation Africa 女童赋权 | 晚近页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 以下 7 条与 yaml 完全一致，已入库（仅收 page.md 明载关系）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Ellen Johnson Sirleaf | 无向 | 2011 诺贝尔和平奖共同得主 |
| co-honored | Tawakkol Karman | 无向 | 2011 诺贝尔和平奖共同得主 |
| colleague | Ellen Johnson Sirleaf | 无向 | 合作者，共同推动利比里亚和平，2011 年为其竞选连任背书 |
| colleague | Thelma Ekiyor | 无向 | WIPNET 培训者与朋友，后共同创建 WIPSEN |
| colleague | Samuel Gbaydee Doe | 无向 | WANEP 联合创始人兼执行主任，引其进入和平建设领域 |
| advisor-student | Hizkias Assefa | 对方为师 | EMU 和平建设暑期学院授课教师 |
| founder | Gbowee Peace Foundation Africa | 人→机构 | 2012 年创立并任主席 |

- 方向约定：founder 人→机构有向；co-honored/colleague 无向自动 from<to 归一
- 对手方 name_en 用 manifest 规范名（Sirleaf/Karman 为并行批次对象，由本 yaml 先建 stub、对方本人 yaml 回填 QID）

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：坚韧、织网、白色中的力量
- **配色**：深紫（manifest 预分配主色 `#46356B`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeWomen` 妇女与和平 — 玫紫 `#8E4585`
  - `badgeNonviol` 非暴力行动 — 青绿 `#0E7C7B`
  - `badgeInterfaith` 跨信仰协作 — 琥珀 `#E07B30`
  - `badgeNobel` 2011 诺奖 — 香槟金 `#C9A227`
- **背景母题**：柔和气泡 + 细密编织网格意象（低饱和），呼应「妇女织网成和平」的设计母题

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍（Liberia），底部状态栏给出 `国籍 | 事业 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：出生、全名、国籍、家庭（子女数）、教育、任职、主要荣誉、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 妇女和平运动旗手 / Leymah Gbowee 1972– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（全名、家庭、教育、任职、荣誉、核心领域）
03  核心贡献概览 — 创伤疗愈 / 妇女和平运动 / 阿克拉和谈 / WIPSEN / 基金会
04  早年：战火中的年轻母亲 (1972–1998) — 17 岁遭遇第一次内战、加纳难民营、六个孩子
05  创伤疗愈之路 (1998–2001) — THRP 志愿者、前童兵康复、AA 学位 2001
06  运动的诞生 (2002) — 鱼市祈祷、清真寺与教堂双线动员、白色 T 恤
07  非暴力方法 — 守夜、罢工、"性罢工"的媒体价值（她自述仅数月且收效有限）、Tubman 大道旁足球场静坐占领
08  阿克拉和谈 (2003) — 率妇女代表团赴加纳、酒店静坐、"和平大厅被古博薇将军占领"、对 Abubakar 的施压
09  和平与选举 (2003–2005) — 08-18 阿克拉全面和平协议、14 年内战结束、2005 Sirleaf 当选非洲首位民选女总统
10  网络与学位 (2004–2007) — WIPSEN 从 WANEP 分立、EMU 冲突转化硕士 2007
11  纪录片与回忆录 — Pray the Devil Back to Hell（2008 Tribeca 最佳纪录片）+ Mighty Be Our Powers（2011）
12  2011 诺贝尔和平奖 — 与 Sirleaf/Karman 三人共享、颁奖日 12-10 三人合影
13  晚近事业 (2012–) — Gbowee Peace Foundation Africa、Barnard/Columbia、Oxfam 大使、2022 Cornell 讲座
14  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【模板通用 + 人物专属】

**版式**：每页 `\newcommand{\xxxslide}{...}`；每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

**Gbowee 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 姓名拼写 | 通名 Leymah Gbowee；Wikipedia 页内对手方拼写 Tawakkul/Tawakel Karman 与 manifest 规范名 Tawakkol Karman 不一致——提示词与 yaml 一律用 manifest 形式 |
| 诺奖理由主语 | 官方理由主语是 "their"（三人共享），勿改写成她个人独得；12-10 颁奖日三人合影可引 |
| 三人分工 | Sirleaf 是政治家/总统、Gbowee 是运动组织者、Karman 是也门活动家，三人事业互不隶属，勿写"三人共同领导同一运动" |
| 性罢工 | 她自述 "lasted, on and off, for a few months. It had little or no practical effect, but it was extremely valuable in getting us media attention"——按自述写，勿渲染夸大 |
| 同名区分 | Samuel Gbaydee Doe（WANEP 和平建设者）与利比里亚前总统 Samuel Doe 无关（page.md 明注 no relation），勿混 |
| 内战数据 | 战后创伤段落数字（25 万死亡、35 万流离、75% 基础设施被毁）出自其回忆录引文，引用时注来源；勿与其他来源混算 |
| 个人生活 | 曾有酗酒问题并于 2008 年戒断（回忆录自述）——客观简述一笔即可，不渲染；伴侣 Daniel/Tunde/James 均按回忆录口径，Tunde 与 James 仅具名 |
| 宗教内容 | 基督徒信仰与跨信仰（基督徒+穆斯林）动员是 page.md 大节内容，可写；但引用其讲道式语句仅限 page.md 明载原文，禁自行扩写 |
| 无载禁写 | 不写具体出生城镇（page.md 仅载 central Liberia）；不写其父/母姓名（page.md 未载）；不写 2012 年后未载的活动细节 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Women of Liberia Mass Action for Peace | 利比里亚妇女大规模和平行动 | 2002 年发起，勿与 WIPNET 混同 |
| WIPNET | 妇女参与和平建设网络 | WANEP 之下的妇女项目 |
| WANEP | 西非和平建设网络 | 1998 年创于加纳的区域组织 |
| WIPSEN | 妇女和平与安全网络 | 2006–07 从 WANEP 分立，驻阿克拉 |
| Trauma Healing and Reconciliation Program | 创伤疗愈与和解项目 | 路德会背景，THRP |
| Accra Comprehensive Peace Agreement | 阿克拉全面和平协议 | 2003-08-18 签署 |
| Eastern Mennonite University | 东门诺大学 | EMU，冲突转化硕士 2007 |
| Mighty Be Our Powers | 《愿我们力量强大》 | 2011 回忆录，与 Carol Mithers 合著 |
| Pray the Devil Back to Hell | 《祈祷恶魔退散》 | 2008 纪录片，Tribeca 最佳纪录片 |
| sex strike | 性罢工 | 按自述口径，勿夸大 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Mirage** — Notan Nigres（manifest 预分配，勿改）
- **风格**: 迷离 / 坚韧 / 渐次清晰
- **匹配理由**:
  - "Mirage（海市蜃楼）"暗合和平从"看似遥不可及的幻影"到"被妇女之手变为现实"的叙事弧线
  - 迷离中渐强的气质，匹配从战乱创伤到组织千人的坚韧
- **本地路径**: `music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav` → `presentations/21th_century/Leymah_Gbowee/Mirage.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Leymah_Gbowee/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/pages/21th_century/Leymah_Gbowee/images.txt` | 肖像与插图 URL |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄，勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Leymah_Gbowee.yaml` | 社会关系/领域入库母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
