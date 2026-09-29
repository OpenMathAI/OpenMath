# 医学家立传提示词（Otto Loewi）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Otto Loewi（1936 年诺贝尔生理学或医学奖得主，奥地利）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Otto_Loewi/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Otto Loewi（奥托·勒维，1873-06-03 法兰克福 ~ 1961-12-25 纽约，享年 88 岁；德国出生→1905 奥地利籍→1946 美国籍）
- **气质关键词**：**用两颗蛙心证明化学传递的人、梦中得来的诺奖实验、被纳粹洗劫后重启人生的流亡者** —— 1936 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 Henry Hallett Dale 共享）：
  > "for their discoveries relating to chemical transmission of nerve impulses"
  > （因其关于神经冲动化学传递的发现）
- **设计母题**：**「两颗蛙心与一瓶灌流液」**。第一颗心脏的灌流液让第二颗心也慢下来——视觉隐喻：并排的两枚心脏轮廓，其间一列液滴传递，与梦境的星屑底纹叠加。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Otto_Loewi/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Otto_Loewi/`，成目录 `medic/presentations/20th_century/Otto_Loewi/`，Makefile 复制后设 `MAIN=Otto_Loewi_zh`、`VIDEO_NAME=Otto_Loewi_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | pharmacology | 药理学 | 格拉茨药理学讲席教授，迷走神经物质研究 | 总览页 |
| 1 | neuroscience | 神经科学 | 确证乙酰胆碱为内源性神经递质 | 乙酰胆碱页 |
| 2 | neurotransmission | 神经传递 | 1921 蛙心双灌流实验一锤定音 | 蛙心实验页 |
| 3 | psychobiology | 心理生物学 | 其自称的第二研究领域 | 研究页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Otto_Loewi.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hans Horst Meyer | 师 | 1898 年起任其马尔堡助手，师承多年 |
| advisor-student | Ernest Starling | 师 | 1902 年伦敦大学学院其实验室客座研究 |
| co-honored | Henry Hallett Dale | — | 1936 诺奖共享（神经冲动化学传递），终生挚友 |
| spouse | Guida Goldschmiedt | — | 1908 年成婚，1958 年卒 |

> 说明：本篇是全批关系最少的一篇（4 条），以 page.md 为准诚实建边。Schwalbe/Schmiedeberg/Naunyn 仅「听课」（courses），不建边；Schmiedeberg 虽为 frontmatter doctoral_advisor，但正文只载听课、无指导叙事——按 metadata-only 纪律不入库；Martin Freund/Hofmeister/von Noorden 为工作经历提及，不建边；四名子女未具名不入库；小儿子捐勋章是遗物处置叙事，不建边。

## 五、配色方案 【人物专属】

- **气质**：梦境与实验的交界、流亡者的坚韧、中欧药理学的余晖
- **主色**：蛙心青绿 `#4A6B3A`（林格液中的实验台色）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 药理学 — 洋地黄紫 `#6E4B7A`
  - `badgeB` 神经科学 — 乙酰胆碱橙 `#C07A2E`
  - `badgeC` 神经传递 — 突触蓝 `#33637D`
  - `badgeD` 心理生物学 — 梦境夜蓝 `#3A3F66`
- **背景母题**：两枚心脏剪影与连接液滴、叠加废纸片上的梦涂鸦弧线（其床头字条意象），低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 两颗蛙心证明化学传递 / Otto Loewi 1873–1961 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、三重国籍链、任职、荣誉、核心领域）
03  核心贡献概览 — 蛙心双灌流 / Vagusstoff / 乙酰胆碱确证 / 代谢与强心苷研究
04  法兰克福少年 (1873–1891) — 犹太家庭、1891 入斯特拉斯堡学医
05  求学与转向 (1891–1898) — 听课诸师、1896 医学博士、目睹结核肺炎无药可医弃临床从基础
06  马尔堡：Meyer 门下 (1898–1909) — 代谢研究、苯酞葡糖苷、1900 讲师、1902 蛋白合成论文
07  1902 伦敦：Starling 实验室 — 客座研究、结识终生挚友 Dale
08  格拉茨岁月 (1909–1938) — 1909 药理学讲席、1921 前的器官应答与肾上腺素依赖研究
09  复活节之梦 (1921)（核心页）— 两夜同梦、床头字条、次日清晨的「人生最长一天」
10  蛙心双灌流（核心页）— 实验全解：电刺激迷走神经→灌流液转移→第二颗心减速→Vagusstoff→乙酰胆碱
11  1936 诺贝尔奖（核心页）— citation 原文（与 Dale 共享）、1936-12-12 诺奖演讲
12  1938： Anschluss 之夜 — 与两子同时被捕、三个月后「自愿」放弃全部财产获释、经布鲁塞尔牛津流亡
13  重启：纽约大学 (1940–1961) — 1940 赴美、1941 妻辗转团圆、1946 入籍、NYU 研究教授
14  遗产与身后 — 1961 圣诞节辞世；小儿子将金质奖章赠 Royal Society、文凭归格拉茨；Otto Loewi Gasse
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for their discoveries relating to chemical transmission of nerve impulses"（their 与 Dale 共享）；json 中 Loewi 行 country 标 Germany 但 manifest/总表口径为 Austria——国籍一律按 Nobel 官方 Austria |
| 2 | 三重国籍链 | German 出生 → Austrian（1905）→ American（1946）——时间线勿乱；获奖时（1936）国籍为奥地利 |
| 3 | 梦境叙事 | 两夜同梦+床头字条读不出+第二天再梦立即赴实验室——page.md 明载且是「人生最长一天」句出处，可完整叙述；「从那天起 consensus 是诺奖只是时间问题」为转述 |
| 4 | Vagusstoff | 命名逻辑：迷走神经（Vagus）+德语「物质」（Stoff）；后来确认对应乙酰胆碱——勿写成「Loewi 分离出乙酰胆碱」（是确证对应关系） |
| 5 | 与 Dale 的镜像 | Dale 1914 鉴定乙酰胆碱、Loewi 证明其神经作用；「lifelong friend that helped to inspire the neurotransmitter experiment」——本篇采 Loewi 页口径，Dale 篇用 Dale 页口径，两篇措辞已对齐 |
| 6 | 师承裁定 | Meyer（1898 助手）与 Starling（1902 客座）正文明载建师生边；Schmiedeberg 仅 frontmatter 导师行+正文「听课」，按 metadata-only 纪律不入库 |
| 7 | Anschluss 段 | 1938-03-11 与两子被捕、三个月后以「voluntarily」移交全部财产（含研究资料）获释——「自愿」加引号是 page.md 原文标记，须保留；史实克制叙述，不渲染 |
| 8 | 家庭 | 四名子女未具名；妻子 Guida 1941 年才获准赴美团圆；小儿子 1961 年后捐出奖章（Royal Society）与文凭（格拉茨，1983）——遗赠走向两处勿混 |
| 9 | 散瞳试验 | Loewi's mydriatic test（切胰犬肾上腺素瞳孔反应诊断急性胰腺炎）是冷门但明载的成果，可作一帧彩蛋或并入研究概览 |
| 10 | metadata 冲突 | frontmatter nationality 三值，yaml 按 Nobel 口径只填 Austria；death 1961-12-25 一致 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Vagusstoff | 迷走神经物质 | 德语合成词，勿意译「迷走素」 |
| acetylcholine | 乙酰胆碱 | 后被确证为 Vagusstoff 本体 |
| Ringer's solution | 林格液 | 蛙心灌流的生理盐水 |
| vagus nerve | 迷走神经 | 控制心率的脑神经 |
| neurotransmitter | 神经递质 | 其确证的首个为乙酰胆碱 |
| chemical transmission | 化学传递 | 诺奖理由核心词，与电传递相对 |
| phlorhizin | 苯酞葡糖苷 | 其早期代谢研究造糖尿病模型药 |
| digitalis | 洋地黄 | 其强心苷-钙作用研究 |
| mydriasis | 瞳孔散大 | 散瞳试验术语 |
| Anschluss | 德奥合并 | 1938-03-11 流亡叙事起点 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Cinematic Experience** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「电影感」精准匹配其人生剧本的三幕结构——中欧学统的黄金年代、纳粹之夜的家国劫夺、纽约实验室的第二人生，转场极富镜头感
  - 也匹配「梦中实验」的戏剧瞬间：复活节两夜同梦是全篇最具影像性的画面
- **备选**（未采用）：Tragedy（本批 Murphy 已用；且其晚年善终，不宜全篇悲剧底色）、Awaken（「觉醒」意象贴梦但受众偏低）
- **本地路径**：按 music_audio/ 内 Alex-Productions Cinematic Experience 曲目复制至 `medic/presentations/20th_century/Otto_Loewi/Cinematic_Experience.wav`，ffmpeg `-shortest` 对齐
