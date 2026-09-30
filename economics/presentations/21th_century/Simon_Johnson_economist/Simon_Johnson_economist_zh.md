# 经济学家立传提示词（Simon Johnson）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2024 年得主 Simon Johnson（西蒙·约翰逊）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Simon_Johnson_economist/page.md`，与其冲突时以 page.md 为准（metadata.json 仅作结构化参考）。

## 一、背景信息 【人物专属】

- **目标经济学家**：Simon H. Johnson（1963-01-16 生于英格兰谢菲尔德，英国裔美国人，**在世**，卒年留白）
- **气质关键词**：**IMF 首席经济学家的转身体、金融危机的制度诊断者、技术红利的再分配论者** —— 2024 年诺贝尔经济学奖获奖理由（与 Daron Acemoglu、James A. Robinson 共享，逐字引自 `economics/nobel_economics_citations.json` 2024 年 Simon Johnson 条目）：
  > "for studies of how institutions are formed and affect prosperity"（表彰他们关于制度如何形成并影响繁荣的研究）
- **设计母题**：**金融寡头与制度制衡（financial oligarchy & institutional checks）**——Johnson 的公共写作主线：2001 殖民地起源论文证明制度决定繁荣；IMF 亲历危机后以《13 银行家》《安静的政变》警示金融权力对制度的俘获；与 Acemoglu 合著《权力与进步》追问技术红利流向谁。视觉隐喻：一杆天平，一侧是堆叠的金条（金融权力），另一侧是列柱（制度制衡），支点用诺奖金色高亮。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Simon_Johnson_economist/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Simon_Johnson_economist/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Simon_Johnson_economist_zh`、`VIDEO_NAME=Simon_Johnson_economist_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Johnson 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | political economy | 政治经济学 | infobox Discipline 首位；制度与权力俘获 | 封面、核心页 |
| 1 | development economics | 发展经济学 | infobox Discipline；殖民地起源研究 | 核心页 |
| 2 | international economics | 国际经济学 | IMF 首席经济学家经历；跨国比较 | IMF 页 |
| 3 | financial crises and banking | 金融危机与银行 | 13 银行家/白宫燃烧；系统性风险委员会 | 危机页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 6 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Rudiger Dornbusch | 师→生（博士导师） | MIT 博士导师（1989），论文通胀、中介与经济活动 |
| co-honored | Daron Acemoglu | 无向 | 2024 诺贝尔经济学奖三人共享（制度如何形成并影响繁荣） |
| co-honored | James A. Robinson | 无向 | 2024 诺贝尔经济学奖三人共享（制度如何形成并影响繁荣） |
| collaborator | Daron Acemoglu | 无向 | 合著殖民地起源（2001）与 Power and Progress（2023） |
| collaborator | James Kwak | 无向 | 合著 13 Bankers（2010），共创 Baseline Scenario 博客 |
| collaborator | Jonathan Gruber | 无向 | 合著 Jump-Starting America（2019） |

**不入库但提示词可叙述**：妻子与两个女儿（page.md 未具名，禁造名字）；Fannie Mae 董事会、CFA 系统性风险委员会、Project Syndicate 专栏（机构职务非个人关系）；Raghuram Rajan / Olivier Blanchard（IMF 任上前后任，infobox 表格行非关系）；Rodrigo Rato / Dominique Strauss-Kahn（IMF 总裁上下级，不建边）。

## 五、配色方案 【人物专属】

- **气质**：冷峻、制衡、危机后的反思
- **主色**：`#14324F`（manifest 预分配藏蓝——与 2024 三人组统一色系）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeInst` 制度与繁荣 — 藏蓝 `#14324F`
  - `badgeImf` IMF 岁月 — 青蓝 `#175E73`
  - `badgeBank` 金融与危机 — 铁灰 `#5A5A5A`
  - `badgeNobel` 诺奖荣誉 — 金 `#C9A227`
- **背景母题**：金条与列柱的天平，呼应「金融权力需要制度制衡」的公共写作主线。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 金融危机的制度诊断者 / Simon Johnson 1963– + 四色 badge + 右上头像 + 国籍行（United Kingdom / United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地谢菲尔德、教育 Oxford BA 1984 /
    Manchester MA 1986 / MIT PhD 1989、任职 MIT Sloan、IMF 2007–08、诺奖 2024、核心领域）
03  核心贡献概览 — 殖民地起源 / IMF 危机亲历 / 金融寡头警示 / 技术与进步的再分配
04  谢菲尔德到牛津 (1963–1986) — Abbotsholme 私立学校、Oxford PPE（Corpus Christi 学院）、Manchester MA
05  MIT 博士 (1986–1989) — Rudiger Dornbusch 门下，通胀、中介与经济活动
06  哈佛与杜克 (1989–1997) — 初级学者（俄罗斯研究中心）→ Fuqua 商学院
07  MIT Sloan (1997–) — 2002 终身；Kurtz 创业学讲席；Global Economics 与未来工作倡议
08  IMF 首席经济学家 (2007–2008) — 危机前夕与危机爆发期在任；The Quiet Coup 的由来
09  殖民地起源（核心贡献页）— 2001 三人合著：制度差异解释前殖民地约四分之三人均收入差
10  13 链行家与金融改革 — 2010 与 Kwak；Baseline Scenario 博客；系统性风险委员会
11  权力与进步 (2023) — 与 Acemoglu：技术不自动带来公益；AI 批判与政策清单
12  2024 诺贝尔经济学奖 — 三人共享；2025 Carnegie Great Immigrant Award
13  公共写作与政策 — Project Syndicate 月度专栏（2010–）、CBO 经济顾问小组、2026 UK AI 经济学研究所主席
14  遗产与结尾 — 从 IMF 到制度经济学的公共知识分子 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由表述 | 2024 三人共享**同一句** "for studies of how institutions are formed and affect prosperity"；勿拆分改写；中译统一「表彰他们关于制度如何形成并影响繁荣的研究」 |
| 目录消歧义 | 目录名 `Simon_Johnson_economist`（消歧义后缀），但 yaml/库内 name_en 用 **Simon Johnson**（manifest 口径无后缀）；tex 正文标题勿写「(economist)」 |
| 国籍口径 | 英裔美国人 British-American；frontmatter 仅 United States 系噪声，以 infobox/正文与 manifest（United Kingdom / United States）为准；2025 Carnegie Great Immigrant Award 呼应移民身份 |
| IMF 任期 | 2007-03 至 2008-08-31 任 IMF 首席经济学家（正前任 Rajan、后任 Blanchard）；「危机前夕与爆发期在任」是事实表述，勿写成「应对了危机」 |
| 博士导师 | infobox 作 Rudiger Dornbusch、frontmatter 作 Rudi Dornbusch、正文两形并存；入库统一 **Rudiger Dornbusch** |
| 书名年份 | 13 Bankers 2010 / White House Burning 2013 / Jump-Starting America 2019（与 Gruber）/ Power and Progress 2023（与 Acemoglu），勿串年 |
| The Quiet Coup | 2009 年 Atlantic Monthly 文章，标题可写；内容涉及金融危机权贵叙事，转述保持客观一句，勿渲染 |
| 政治敏感线 | Biden transition 志愿成员、Fannie Mae 董事会等涉美政治机构只客观列职务，不展开政策立场叙述；不写党派评价 |
| 2026 新机构 | 2026-06 英国政府宣布成立 AI Economics Institute、Johnson 任主席（page.md 明载可写）；Acemoglu 2026 新书与其无关，勿混 |
| 家庭 | 仅「已婚、两个女儿」，无姓名——禁造配偶/子女名字，不入库 |
| 在世口径 | 1963 年生、在世，卒年留白，三处口径一致 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| extractive institutions | 汲取型制度 | 三人组共享核心词 |
| Chief Economist of the IMF | IMF 首席经济学家 | 2007–2008 在任，勿写「IMF 总裁」 |
| systemic risk | 系统性风险 | Systemic Risk Council 联合创始人 |
| The Quiet Coup | 安静的政变 | 2009 文章标题，勿意译走样 |
| 13 Bankers | 13 银行家 | 2010 合著书名，副题华尔街接管与下次危机 |
| Power and Progress | 权力与进步 | 2023 合著书名，千年来技术与繁荣之争 |
| baseline scenario | 基线情景 | 博客名 The Baseline Scenario，勿意译 |
| capture | 俘获 | 金融权力俘获制度的公共写作母题 |
| Kurtz Professor | Kurtz 创业学讲席 | MIT Sloan 教席名号 |
| Peterson Institute | 彼得森国际经济研究所 | 2008–2019 高级研究员 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless**（manifest 预分配，`music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav`；2024 三人组同曲，出片阶段若撞曲需主控协调可换备选）
- **匹配理由**：与 Acemoglu/Robinson 篇同曲——制度研究的长时段气质一致；Johnson 侧从 IMF 危机现场到《权力与进步》的千年技术叙事同样需要「超越一时一事的沉稳时间感」。
- **备选**：★ **Tragedy**（危机叙事张力）；★ **The Flow of Time**（时间感直白）。
- **本地路径**：复制 wav 到 `economics/presentations/21th_century/Simon_Johnson_economist/Timeless.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、执行清单 【模板通用】

1. 读本提示词 + `Kenneth_G_Wilson_zh.tex` 骨架，建目录 `economics/presentations/21th_century/Simon_Johnson_economist/`；
2. 从 images.txt / Commons 下载肖像（250px→500px），404 则装饰圆占位；
3. 复制 Makefile 设 `MAIN=Simon_Johnson_economist_zh`、`VIDEO_NAME=Simon_Johnson_economist_zh`；
4. 写 tex（配色按第五节、Slide 序列按第六节），每写一页 `make` 查溢出（0 error、vbox≤10pt、hbox≤50pt）；
5. `make pdf` → `pdftoppm` 逐页目检 → `make images` → `make video` 出 mp4；
6. 全程遵守第七节陷阱表；引语仅限 page.md 载有英文原文者（引原文+译文），无原文不得造「原话」；政治内容零评价。
