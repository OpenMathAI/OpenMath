# 经济学家立传提示词（Theodore Schultz）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1979 年得主 Theodore Schultz（西奥多·舒尔茨）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Theodore_Schultz/page.md`，与其冲突时以 page.md 为准。

## 0. 背景信息 【人物专属】

- **目标经济学家**：Theodore William Schultz（1902-04-30 生于南达科他州 Badger 东南十英里的小镇、560 英亩农场 ~ 1998-02-26 逝于伊利诺伊州埃文斯顿，享年 95 岁，安葬于 Badger Cemetery）
- **气质关键词**：**人力资本之父、农业经济学的旗手、从农田走向讲台的穷孩子** —— 1979 诺贝尔经济学奖（与 Arthur Lewis 共享）获奖理由：
  > "for their pioneering research into economic development research with particular consideration of the problems of developing countries"（表彰他们对经济发展的开创性研究，尤其着重考虑了发展中国家的问题）
- **设计母题**：**从土地到头脑（farm to mind）**——舒尔茨的核心洞见是「知识与技能是一种资本」：麦穗、书本与储蓄曲线并置，农田的投入产出逻辑映射到人的教育与健康投资，构成背景母题（错落的麦田几何 + 上升的人力资本曲线）。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Theodore_Schultz/page.md`（同目录 `metadata.json` 仅作结构化参考，冲突以 page.md 为准）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 一、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Theodore_Schultz/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Theodore_Schultz_zh`、`VIDEO_NAME=Theodore_Schultz_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库（见下二、三节），无需重复执行；第 5 步起按本文第四至八节执行。

## 二、研究领域梳理 + 入库 【人物专属】

**Schultz 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | human capital theory | 人力资本理论 | 知识与技能是一种资本；诺奖核心贡献之一 | 核心页 |
| 1 | development economics | 发展经济学 | 1979 获奖理由明示领域（经济发展） | 核心页 |
| 2 | agricultural economics | 农业经济学 | infobox Discipline；威斯康星博士专业 | 早年/农业页 |
| 3 | economics of education | 教育经济学 | 教育投资的产出与回报；educational capital | 人力资本页 |

## 三、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Benjamin H. Hibbard | 师→生（本人受教） | 威斯康星大学农经博士（1930）导师，正文明载 |
| advisor-student | D. Gale Johnson | 本人→学生 | 昔日学生，移居芝加哥后亲自招募进经济系 |
| collaborator | Gary Becker | 无向 | 人力资本理论在其协助下形成 |
| collaborator | Jacob Mincer | 无向 | 人力资本理论在其协助下形成 |
| spouse | Esther Florence Werth | 无向 | 1930 结婚（1905–1991），其著作的主要编辑 |
| co-honored | Arthur Lewis | 无向 | 1979 诺贝尔经济学奖共享（经济发展研究） |

**不入库但提示词可叙述**（防 Review 误判）：
- Clifford Hardin、Zvi Griliches、Marc Nerlove、George S. Tolley：正文仅说「1940-50 年代与 Schultz-Johnson 两人关联的研究生与教师」，群体叙述非直接师生，不入库。
- 三个子女（两女一子）：page.md 未具名，不入库。
- Rockefeller Foundation：资助机构非人物，不建边。
- Ernest Lawrence：仅作「南达科他州第二位诺奖得主」对比叙述，无直接关系。
- page.md 的 Chicago school 导航侧栏（Friedman、Coase、Stigler 等数十人）系站内导航框，**非传记内容，一律不得据此建关系边**。

## 四、配色方案 【人物专属】

- **气质**：朴实、务实、大器晚成的中西部农人学者
- **主色**：`#2A3468`（manifest 预分配，深蓝紫——农田暮色与学术深度的叠合）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeHC` 人力资本 — 深蓝紫 `#2A3468`
  - `badgeDev` 发展经济学 — 麦金 `#C8922A`
  - `badgeAgri` 农业经济 — 田野绿 `#3E6B48`
  - `badgeEdu` 教育经济 — 砖红 `#9E4A2B`
- **背景母题**：错落的麦田几何块与一条上升的「人力资本积累曲线」，呼应「从土地到头脑」的视觉隐喻。

## 五、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover 路径按 economics 执行）
01  封面 — 人力资本之父 / Theodore Schultz 1902–1998 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地南达科他农场、教育 SDSU 1927 /
    威斯康星博士 1930、任职 Iowa State 1930–43 与芝加哥大学 1946 起、诺奖 1979、核心领域）
03  核心贡献概览 — 人力资本理论 / 改造传统农业 / 农业与经济发展 / 教育资本
04  农场少年的辍学岁月 (1902–1927) — 八年级被父亲 Henry 留在家务农；南达科他州立农学院
    冬季学期制；1927 农学+经济学学士
05  威斯康星与 Hibbard 门下 (1927–1930) — 农经博士；关税与粗饲料谷物论文
06  艾奥瓦州立学院岁月 (1930–1943) — 农经系执教；人造黄油风波（oleomargarine controversy）离校
07  芝加哥大学经济系主任 (1946–1961) — 招募 D. Gale Johnson；洛克菲勒基金会资助农经项目
08  人力资本理论（核心贡献页）— 战后德日复苏之谜；教育与健康即投资；
    Investment in Human Capital；Becker 与 Mincer 的协助
09  争议与回应 — 「把人当资本」的批评（奴隶制类比、民权运动背景）；舒尔茨的辩护理路
10  改造传统农业 (1964) — 穷国农民是理性经济人；新要素投入；市场化路径
11  发展经济学与国际援助反思 — 粮食与金钱援助之弊；教育与技术投资之利；IMF/世行的回响
12  荣誉与认可 — Nobel 1979 · Francis A. Walker Medal 1972 · AEA 主席 1960 · 三院院士
    （AAAS 1958 / APS 1962 / NAS 1974）· 八个荣誉学位
13  遗产 — 首位 SDSU 毕业生诺奖得主、南达科他州第二位诺奖得主（Lawrence 之后）；
    Schultz Hall（2012–13 落成）
14  遗产与结尾 — 人力资本成为现代经济学的基石概念 + 结尾页
```

## 六、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 早年辍学 | 八年级时父亲让他离开 Kingsbury County Schoolhouse 务农（父认为继续上学就不愿留农场），此后一段时间「没有任何正规中学后教育」——勿写成连续求学经历 |
| 出生地两说 | infobox 作 Arlington, South Dakota；正文作「Badger 东南十英里的小镇、560 英亩农场」。照录正文叙述为主，可注 infobox 口径 |
| 诺奖理由措辞 | 官方理由强调 economic development + developing countries（their/they 复数，与 Lewis 共享）；官方措辞**不含** human capital 字样，人力资本是 page.md 对其获奖工作的叙述 |
| 人力资本归属 | 与 Gary Becker、Jacob Mincer「在其协助下形成」（formulated with the help of），勿写成独自创立；「投资人」思想源自其 Investment in Human Capital 一书 |
| 「把人当资本」争议 | 许多经济学家因奴隶制类比拒绝该理论（民权运动背景下可理解的批评）；舒尔茨自辩理论不否定人性、反而鼓励自我投资——按 page.md 客观转述双方 |
| Chicago school 侧栏 | page.md 顶部芝加哥学派导航框列 Alchian、Becker、Coase、Friedman、Stigler 等数十人，系站内导航**非传记内容**，严禁据此建关系边或写成交往 |
| 援助之弊表述 | 「美援粮食/金钱不仅无益反而有害（农民无法与免费价格竞争）」是 page.md 转述其研究结论，措辞照录其理论视角，勿写成普遍事实断言 |
| 名字署名噪声 | page.md 1981 引语署名误拼 "Theodore W. Shhultz"，系页面噪声；引用引语时署名改正为 Schultz |
| 引语红线 | page.md 载三条英文原话（1977/1980/1981），引用须原文+中译；1980 农夫「精打细算的企业家」句是其最有名的表述 |
| 卒地与安葬 | 逝于伊利诺伊州埃文斯顿（Evanston），安葬于南达科他州 Badger Cemetery；勿混淆 |
| metadata 冲突 | metadata.json 与 page.md 冲突时（如生卒、荣誉列表）一律以 page.md 为准 |

## 七、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| human capital | 人力资本 | 核心概念，勿译「人力资产」；与「人力资源」层次不同 |
| investment in human capital | 人力资本投资 | 1961 AER 论文与 1971 书名 |
| educational capital | 教育资本 | 人力资本的教育分支概念 |
| agricultural economics | 农业经济学 | 其博士专业与第一身份 |
| development economics | 发展经济学 | 获奖理由明示领域 |
| Transforming Traditional Agriculture | 改造传统农业 | 1964 专著，穷国农民理性命题 |
| oleomargarine controversy | 人造黄油风波 | 1943 离开艾奥瓦的导火索 |
| Francis A. Walker Medal | 弗朗西斯·沃克奖章 | AEA 最高奖（1972），勿与诺奖混 |
| economic development | 经济发展 | 获奖理由关键词，勿写「经济增长」 |
| calculating economic agents | 精打细算的经济主体 | 1980 引语核心词，指穷国农民 |

## 八、背景音乐选择 【人物专属】

- **选定曲目**：**Tragedy**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：曲目名的沉郁底色贴合其人生前半的困顿叙事——八年级辍学务农、大萧条年代的农业危机、人造黄油风波出走；而诺贝尔领奖（1979，从瑞典国王 Carl XVI Gustaf 手中接奖）是漫长的悲剧底色后终获承认的高点，音乐张力支撑这条「迟来的承认」弧线。
- **本地路径**：复制 `music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav` 到 `economics/presentations/20th_century/Theodore_Schultz/Tragedy.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 九、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/20th_century/Theodore_Schultz/page.md` | ★ 事实基准 |
| `economics/presentations/pages/20th_century/Theodore_Schultz/metadata.json` | 结构化参考（冲突以 page.md 为准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` | 任务流程第三章 |
| `MySQL/data/Theodore_Schultz.yaml` | 已入库 yaml 存档 |
| `economics/PROMPTS_WORKFLOW.md` | 批量作业手册 |

## 十、执行清单 【模板通用】

1. 建目录 `economics/presentations/20th_century/Theodore_Schultz/`（`images/` 子目录）。
2. 肖像：images.txt 有 URL 直接用（250px 改 500px）；无 URL 用 Commons `Special:FilePath`（curl 加 `-A "Mozilla/5.0"`，`file` 验证），404 则装饰圆占位。page.md 有 1979 领奖照（与 Carl XVI Gustaf），可作插图页。
3. 复制参照 Makefile，设 `MAIN=Theodore_Schultz_zh`、`VIDEO_NAME=Theodore_Schultz_zh`。
4. 按 §五 写 15 帧；每帧 `make` 编译，`pdftoppm` 截图目检。
5. 编译达标：0 error、vbox ≤ 10pt、hbox ≤ 50pt。
6. `make images && make video` 出 mp4；核对 BGM 时长。
7. Review-1 修正写回本提示词。

## 十一、版式补遗 【模板通用】

- 表格页安全负间距：顶部 `-0.35cm`、`arraystretch 0.78–0.82`；公式框/引语框前 `-0.35 ~ -0.55cm`。
- itemize 挤页：`\itemsep -2.5pt` + `\topsep 0pt` + 顶部 `-0.55cm`（勿超 `-0.65cm`，会遮副标题）。
- 引语框（三条 Quotes）用 `beamercolorbox` 或 tcolorbox，中英对照各一行，字号 `\small`。
- 带圈数字 ①-④ 需 `\xeCJKDeclareCharClass{CJK}{"2460->"2473}`；★号 U+2605 在 lmsans-oblique 缺字，避免在 sans 斜体环境使用。
- 文本模式希腊字母须转数学模式。

## 十二、生平时间线节点 【人物专属】

> 供时间线页/身份信息页取材（全部出自 page.md，勿外加）：

| 年份 | 事件 |
|------|------|
| 1902-04-30 | 生于南达科他州 Badger 东南十英里小镇，560 英亩农场 |
| 约 1915 | 八年级时被父亲 Henry 留在家务农，离开 Kingsbury County Schoolhouse |
| 1920s | 入南达科他州立农学院（冬季学期制：一年四个月、三年制） |
| 1927 | 获农学+经济学学士；同年 Esther Werth 毕业于同校商业科学 |
| 1930 | 威斯康星大学农经博士（导师 Hibbard）；同年与 Esther 结婚；入职艾奥瓦州立学院 |
| 1943 | 因人造黄油风波离开艾奥瓦州立 |
| 1946 | 出任芝加哥大学经济系主任（至 1961） |
| 1946 | 招募昔日学生 D. Gale Johnson；获洛克菲勒基金会资助农经项目 |
| 1958 | 当选美国艺术与科学院院士 |
| 1959 | 获母校荣誉理学博士 |
| 1960 | 出任美国经济学会（AEA）主席 |
| 1962 | 当选美国哲学会会员 |
| 1964 | 出版《改造传统农业》 |
| 1970 | 退休（此后仍活跃于芝加哥至 90 多岁） |
| 1972 | 获 Francis A. Walker Medal（AEA 最高奖） |
| 1974 | 当选美国国家科学院院士 |
| 1979 | 与 Arthur Lewis 共享诺贝尔经济学奖；从瑞典国王 Carl XVI Gustaf 手中领奖 |
| 1998-02-26 | 逝于伊利诺伊州埃文斯顿，享年 95；安葬 Badger Cemetery |
| 2012–13 | 南达科他州立大学建成 Theodore W. Schultz Hall 宿舍楼 |

## 十三、肖像与图像素材指引 【人物专属】

- **优先**：`images.txt` 列出的 infobox 肖像 URL（250px 改 500px 下载）。
- **备用**：Commons `Special:FilePath/<文件名>?width=600`（curl 加 `-A "Mozilla/5.0"`，`file` 验证为真图）。
- **正文插图**：page.md 载 1979 领奖照（Theodore Schultz receiving the Nobel Prize from King Carl XVI Gustaf），可作诺奖页插图，图注照录。
- **404 兜底**：装饰圆占位（姓名首字母 + 主色），图注注明「肖像暂缺」。
- **禁用**：Chicago school 侧栏任何头像链接；无版权把握的第三方图。
- **图注规范**：所有插图图注必须照录 page.md 原文语义（如领奖照注「1979 年从瑞典国王 Carl XVI Gustaf 手中领取诺贝尔经济学奖」）。
- **插画母题**：麦田几何块 + 人力资本上升曲线为背景装饰（tcolorbox/tikz），不与照片混排。
- **分辨纪律**：照片统一 500px 宽；装饰圆直径与照片栏位对齐（约 2.6cm），避免版面跳动。

## 十四、获奖理由引用规则 【模板通用】

- **1979 为共享年份**：manifest 的 `citation_en`/`citation_zh` 已给出整句（their/they 复数），封面与诺奖页**逐字引用**，不拆分、不改单数。
- 官方理由不含 human capital 字样；人力资本是 page.md 对其获奖工作的叙述，两者勿混排进引语框。
- 引语框内英文用半角引号 `" "`；中译独立成行，不套引号冒号结构。


