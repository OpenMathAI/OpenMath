# 经济学家立传提示词（Gunnar Myrdal）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1974 年得主 Gunnar Myrdal（贡纳尔·缪尔达尔）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Gunnar_Myrdal/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Karl Gunnar Myrdal（1898-12-06 生于瑞典 Skattungbyn ~ 1987-05-17 逝于瑞典 Trångsund，享年 88 岁）
- **气质关键词**：**斯德哥尔摩学派的旗手、循环累积因果的提出者、夫妻双诺奖的另一半**
- **诺奖获奖理由**（1974，与 Friedrich Hayek 共享，逐字引自 manifest）：
  > "for their pioneering work in the theory of money and economic fluctuations and for their penetrating analysis of the interdependence of economic, social and institutional phenomena"（表彰他们在货币理论与经济波动理论方面的开创性工作，以及对经济、社会与制度现象相互依存关系的深刻分析）
- **设计母题**：**循环累积因果（circular cumulative causation）**——变量互为因果、逐轮放大的多因链条，是「回旋上升的水流」的视觉隐喻：螺旋环线与渐变色阶构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Gunnar_Myrdal/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Gunnar_Myrdal/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Gunnar_Myrdal_zh`、`VIDEO_NAME=Gunnar_Myrdal_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Myrdal 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | monetary theory | 货币理论 | Monetary Equilibrium（1931）、事前/事后分析，诺奖核心理由 | 核心页 |
| 1 | macroeconomics | 宏观经济学 | 斯德哥尔摩学派；先于 Keynes 的财政调节主张 | 核心页 |
| 2 | development economics | 发展经济学 | Asian Drama、Rich Lands and Poor、循环累积因果 | 应用页 |
| 3 | sociology | 社会学 | An American Dilemma 种族关系研究、社会政策 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Gustav Cassel | Cassel → 师 | 斯德哥尔摩大学博士导师（1927 博士论文价格形成与预期） |
| influence | Knut Wicksell | 无向 | 建立在 Wicksell 内生货币累积过程理论上（正文明载） |
| co-honored | Friedrich Hayek | 无向 | 1974 诺贝尔经济学奖共享（库内 id=7821，本批先建） |
| spouse | Alva Myrdal | 无向 | 1924-10 结婚（复用库内 id=7035，和平奖侧已有 spouse 边幂等） |
| collaborator | Alva Myrdal | 无向 | 合著《人口问题危机》1934 与 Contact with America 1941 |
| advisor-student | Rudolf Meidner | Myrdal → 学生 | infobox Doctoral students 明载 |
| advisor-student | Leo Törnqvist | Myrdal → 学生 | infobox Doctoral students 明载 |
| parent-child | Jan Myrdal | Myrdal → 子 | 1927 年生（复用库内 id=7436） |
| parent-child | Sissela Bok | Myrdal → 女 | 1934 年生（复用库内 id=7065） |

**不入库但提示词可叙述**：infobox Influences 另列 John R. Commons 与 Raúl Prebisch（仅 infobox 级，防噪声不入库）；三女 Kaj Fölster 无维基链接不入库（其子 Stefan Fölster 系隔代亦不入库）；Keynes 关系系"早期支持者+优先权之争"（自称 1932 Monetary Economics 先于凯恩斯四年的基本思路）无稳定关系类型、仅叙述；William Barber/Shackle 的学术评价系他人转述不入库；Ralph Bunche→Myrdal colleague 边（1940《美国困境》首席研究助理）已由和平奖侧入库无需重复。

## 五、配色方案 【人物专属】

- **气质**：社会工程的热忱、北欧的清朗、制度关怀
- **主色**：`#14324F`（制度深蓝——与共享得主 Hayek 同色为 manifest 预分配，共同体现 1974 届「经济社会制度相互依存」主题）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeMon` 货币与波动 — 深蓝 `#14324F`
  - `badgeDev` 发展与亚洲 — 琥珀 `#C07A2A`
  - `badgeSoc` 社会学与种族研究 — 青绿 `#0E7C7B`
  - `badgeFam` 夫妻双诺奖 — 灰紫 `#52307C`
- **背景母题**：螺旋环线与渐变色阶（循环累积因果抽象），呼应设计母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 斯德哥尔摩学派旗手 / Gunnar Myrdal 1898–1987 + 四色 badge + 右上头像 + 国籍行（Sweden）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地 Skattungbyn、斯德哥尔摩大学法学 1923/经济学博士 1927、
    师承 Cassel、任职 Stockholm/NYU/Geneva、诺奖 1974、核心领域）
03  核心贡献概览 — 货币均衡与事前事后 / 循环累积因果 / An American Dilemma / 亚洲戏剧
04  早年与 Cassel 门下 (1898–1927) — 本姓 Pettersson、1914 改姓 Myrdal、Cassel 轶事（写讣告的对答）
05  货币均衡与事前事后 (1931) — Monetary Equilibrium、Knightian 不确定性、ex ante/ex post 概念
06  斯德哥尔摩学派 (1930) — The Political Element 批判老一代瑞典经济学家、创办计量经济学会、后转批判
07  与 Alva 的合作 (1934) — 合著《人口问题危机》推动社会政策、1941 Contact with America
08  An American Dilemma (1944) — Carnegie 资助、American Creed 与现实落差、1954 Brown v. Board 援引
09  政治生涯与 UNECE (1933–1957) — 社民党议员、1945–47 商工大臣、联合国欧洲经济委员会执行秘书十年
10  亚洲戏剧 (1968) — 二十世纪基金会南亚研究三卷本、1970 The Challenge of World Poverty
11  1974 诺贝尔奖 — 与 Hayek 共享、主张废除经济学奖（经济学是"软"科学）、获奖演讲 1975-03-17
12  夫妻双诺奖 (1982) — Alva 与 García Robles 获诺贝尔和平奖、史上第四对且首对独立获奖的诺奖夫妇
13  荣誉与晚年 — Malinowski Award 1975、Veblen-Commons Award 1975、帕金森病、1987 逝于 Trångsund
14  遗产与结尾 — 福利国家到 welfare world、非均衡经济学与制度主义回响 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 共享奖张力 | 与 Hayek 政治光谱对立（Hayek 自认配对为平衡、Myrdal 抱怨与"空想家"同奖）；两人 co-honored 双向客观呈现，禁单侧叙事 |
| 废奖主张 | Myrdal 领奖后**主张废除经济学奖**（认为经济学是"软"科学）——page.md 明载，必须写且勿回避 |
| 妻子双边关系 | Alva 既有 spouse（1924）又有 collaborator（合著两书）两条边；spouse 边与和平奖侧（id=7035 写入）幂等去重，勿删对方行 |
| 优先权之争 | 自称财政调节基本思路先于 Keynes《通论》四年（1932 Monetary Economics）；William Barber 的"Myrdalian"评论系他人转述，引用须注明 |
| 越战内容红线 | 反对越战、瑞典越南委员会、印支战争罪调查委员会联席主席等均按 page.md 客观记录，禁展开政治评价 |
| 1947 争议 | 与苏联的金融协议遭批评 + 1947 瑞典货币危机被指负责——按正文客观一句，勿下断语 |
| 学生防噪声 | infobox 博士生仅 Meidner/Törnqvist 两人，全收入库；别处出现的瑞典经济学家勿强挂师生 |
| 家族两代 | 子 Jan Myrdal、女 Sissela Bok 入库（库内已有 id）；女 Kaj Fölster 与孙 Stefan Fölster/Janken Myrdal 无类型或无链接不入库 |
| 改姓细节 | 本姓 Karl Adolf Pettersson 之子、1914 按祖地农场改姓 Myrdal——人物页常被漏写，身份信息页补上 |
| Cassel 轶事 | Cassel"要尊敬长者"与"我们写你们的讣告"对答，page.md 明言 possibly apocryphal——引用必须带"据传" |
| metadata 噪声 | metadata.json 曾误连 Gunnar Myrdal 分裂记录（家族 stub 误删事件）——本篇一律以 page.md 与库内规范记录 7062 为准 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| monetary equilibrium | 货币均衡 | 1931 书名，勿译"货币平衡" |
| ex ante / ex post | 事前 / 事后 | 预期分析的核心区分 |
| circular cumulative causation | 循环累积因果 | 多因互馈，勿译"循环因果"简化 |
| Stockholm school | 斯德哥尔摩学派 | 与凯恩斯主义平行而非隶属 |
| An American Dilemma | 《美国的困境》 | 1944，书名定译 |
| Asian Drama | 《亚洲的戏剧》 | 1968 三卷本，书名定译 |
| American Creed | 美国信条 | An American Dilemma 核心概念 |
| Folkhemmet | 人民之家 | 瑞典福利国家理念，其工作有影响（正文明载） |
| welfare world | 福利世界 | Beyond the Welfare State 的扩展主张 |
| UNECE | 联合国欧洲经济委员会 | 1947–1957 执行秘书 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**SEA**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`；与同届 Hayek 同曲，立传出片阶段若撞曲约束可另行协调，本阶段忠于 manifest）
- **匹配理由**：深海的洋流互馈正合「循环累积因果」的多因链条意象；辽阔与冷峻也贴合其横跨经济学、社会学与世界事务的广阔一生。
- **本地路径**：复制 `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav` 到 `economics/presentations/20th_century/Gunnar_Myrdal/SEA.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/20th_century/Gunnar_Myrdal/page.md` | 事实基准（唯一事实来源） |
| `economics/PROMPTS_WORKFLOW.md` | 批量作业手册 |
| `MySQL/data/Gunnar_Myrdal.yaml` | 入库 yaml（与本文第三、四节一致） |
| `economics/economics_list_data.py` / `nobel_economics_citations.json` | 获奖理由中文对照 |

## 十一、执行清单 【模板通用】

1. 读 page.md 建立事实基准（本文件已沉淀，直接核对即可）
2. 下载肖像（images.txt 有 URL 直接用 500px；404 用 Commons `Special:FilePath`，再 404 装饰圆占位）
3. 复制 BGM wav 到人物目录
4. 写 tex（配色按第五节、Slide 序列按第六节）
5. 编译循环：0 error、vbox ≤ 10pt、hbox ≤ 50pt
6. pdftoppm + read_file 逐页目检
7. make images/video；Review-1 修正写回本文件
