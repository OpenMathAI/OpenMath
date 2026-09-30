# 经济学家立传提示词（George Stigler）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1982 年得主 George Stigler（乔治·斯蒂格勒）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/George_Stigler/page.md`，与其冲突时以 page.md 为准。

## 0. 背景信息 【人物专属】

- **目标经济学家**：George Joseph Stigler（1911-01-17 生于华盛顿州西雅图 ~ 1991-12-01 逝于伊利诺伊州芝加哥，享年 80 岁）
- **气质关键词**：**信息经济学的开创者、规制俘获理论的奠基人、芝加哥学派的旗手与幽默家** —— 1982 诺贝尔经济学奖获奖理由：
  > "for his seminal studies of industrial structures, functioning of markets and causes and effects of public regulation"（表彰他对产业结构、市场运作以及公共监管的成因与效果的开创性研究）
- **设计母题**：**信息的搜寻成本（search cost）**——分散的价格标签散落在市场网格上，一只放大镜在不同标价间移动，寻价路径的折线构成背景母题：1961《信息经济学》「知识就是力量，但它在经济学城里住着贫民窟」的意象化。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/George_Stigler/page.md`（同目录 `metadata.json` 仅作结构化参考，冲突以 page.md 为准）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 一、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/George_Stigler/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=George_Stigler_zh`、`VIDEO_NAME=George_Stigler_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库（见下二、三节），无需重复执行；第 5 步起按本文第四至八节执行。

## 二、研究领域梳理 + 入库 【人物专属】

**Stigler 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | economics of information | 信息经济学 | 1961《信息经济学》开创性论文，Friedman 称其开创新研究领域 | 核心页 |
| 1 | industrial organization | 产业组织 | infobox Notable ideas；获奖理由「产业结构」 | 核心页 |
| 2 | economic regulation / public choice | 经济规制与公共选择 | 1971 规制俘获理论 | 规制页 |
| 3 | history of economic thought | 经济思想史 | 大量论文、1965 结集《经济思想史论文集》 | 思想史页 |

## 三、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Frank Knight | 师→生（本人受教） | 芝加哥博士（1938）论文导师 |
| influence | Jacob Viner | 无向 | page.md 明载的影响者之一 |
| influence | Henry Simons | 无向 | page.md 明载的影响者之一 |
| influence | Milton Friedman | 无向 | infobox Influences 明载 |
| colleague | Milton Friedman | 无向 | 50 余年挚友，芝加哥同门 |
| colleague | W. Allen Wallis | 无向 | 芝加哥同门同学 |
| advisor-student | Jacob Mincer | 本人→学生 | 博士生（infobox 明载） |
| advisor-student | Thomas Sowell | 本人→学生 | 博士生（infobox 明载） |
| collaborator | Claire Friedland | 无向 | 1962 合著 What Can Regulators Regulate |
| collaborator | Paul Samuelson | 无向 | 1963 合著《国家经济作用对话》 |
| collaborator | J.K. Kindahl | 无向 | 1970 合著 The Behavior of Industrial Prices |
| parent-child | Stephen Stigler | 本人→子 | 统计学家，page.md See also 明载 his son |

**入库备注**：Friedman 一人两行（influence + colleague，note 区分）；Samuelson 复用本批次 Klein 篇所建 stub #7778（防分裂）。

**不入库但提示词可叙述**（防 Review 误判）：
- Deirdre McCloskey：批评其把 Adam Smith 描述为「贪婪即善」学派之父是对这位苏格兰哲学家的糟糕解读——单向评论非对等争议，不入库仅叙述。
- Charles Rowley 与「Virginia School」：公共选择内部的学派性反对——学派集体非个人关系，不入库。
- W. Allen Wallis 之外的「同门」仅 Friedman/Wallis 两人 page.md 点名。
- Antal Koppány（伯外叔祖，与 Bobby Fischer 弈和的棋手）：远亲趣闻（Trivia 节），不入库。
- Manhattan Project：二战期间在哥伦比亚大学为曼哈顿计划做数学统计研究——项目非人物。
- 学会会员（APS 1955 / AAAS 1959 / NAS 1975 / ASA Fellow 1963）与 National Medal of Science 1987：荣誉非关系。
- page.md 的 Chicago school 导航侧栏数十人：站内导航非传记内容，严禁据此建边。

## 四、配色方案 【人物专属】

- **气质**：锋利、幽默、怀疑监管的实证主义者
- **主色**：`#175E54`（manifest 预分配，深松绿——学术传统的厚重与芝加哥学派的沉着）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeInfo` 信息经济 — 深松绿 `#175E54`
  - `badgeIO` 产业组织 — 钢青蓝 `#37548D`
  - `badgeReg` 规制俘获 — 砖红 `#9E4A2B`
  - `badgeHist` 思想史 — 麦金 `#C8922A`
- **背景母题**：市场网格上散落的高低价格标签 + 一条放大镜寻价折线；可点缀「Stigler diet」极简食谱表意象（其 1945 最低成本饮食线性规划）。

## 五、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover 路径按 economics 执行）
01  封面 — 信息经济学之父 / George Stigler 1911–1991 + 四色 badge + 右上头像 + 国籍行
    （United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地西雅图、教育华盛顿大学 1931/
    西北 MBA 1932/芝加哥博士 1938、任职 Columbia 1947–58 与芝加哥大学、诺奖 1982、核心领域）
03  核心贡献概览 — 信息经济学 / 搜寻失业理论 / 规制俘获 / 经济思想史
04  西雅图与德裔匈裔家庭 (1911–1933) — 父巴伐利亚裔母匈牙利裔（Erzsébet Hungler），
    童年讲德语；华盛顿大学 1931 BA、西北 1932 MBA（在西北决意从学）
05  芝加哥与 Knight 门下 (1933–1938) — Knight 的博士导师；Friedman 后评「Knight 在芝加哥
    28 年只有三四名学生通过论文答辩」——Stigler 是其中之一
06  早年教职与曼哈顿计划 (1936–1947) — 艾奥瓦州立学院 1936–38；二战在哥伦比亚大学为
    曼哈顿计划做数学统计研究；Brown 一年；1947 入哥伦比亚
07  1961《信息经济学》（核心贡献页）— 搜寻成本；「信息是有价值的资源：知识就是力量，
    然而它在经济学城里住在贫民窟」（原文引用）
08  搜寻失业与信息经济学延伸 — 1962 Information in the Labor Market；
    1963 当选 ASA Fellow
09  规制俘获理论 (1971) — 利益集团用政府规制权力为自身谋利；公共选择分支；
    Virginia School 的反对（学派叙述）
10  经济思想史 — 大量论文、1965 结集；AER 评价「明晰的文笔、穿透性的逻辑、
    睿智的幽默已成作者商标」；McCloskey 的 Smith 解读批评（客观并列）
11  幽默与 spoof 文章 — Stigler's Law of Demand and Supply Elasticities（戏作）；
    《知识分子与市场》；Stigler diet 的由来（1945 最低成本饮食）
12  芝加哥学派旗手 — 1977 创立经济与国家研究中心（Center for the Study of the Economy
    and the State）；1991 身后冠名 Stigler Center
13  荣誉与认可 — Nobel 1982 · National Medal of Science 1987 · 三院院士
    （APS 1955/AAAS 1959/NAS 1975）· Guggenheim Fellow
14  遗产与结尾 — 信息经济学与规制经济学的现代格局 + 结尾页
```

## 六、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由拆解 | 三个并列对象：industrial structures / functioning of markets / causes and effects of public regulation——勿只写「规制」一项；理由为个人独得（1982 单人） |
| Knight 师承轶事 | Friedman 评「Knight 28 年只让三四名学生通过答辩」系 Friedman 的评论转述，标注归属（Friedman, 1992 Biographical Memoirs），勿写成客观统计 |
| Friedman 两行 | influence（infobox Influences）与 colleague（50 余年挚友+同门）分两行入库，note 区分；Friedman 称 Stigler「开创了经济学家的一个新研究领域」指 1961 论文 |
| 引语红线 | page.md 载 Stigler 原文两处：1961「information is a valuable resource: knowledge is power...slum dwelling in the town of economics」与 spoof 定律「all demand curves are inelastic...」——引用须英文原文+中译；AER 对其思想史文集的评价是机构评语，注明出处 |
| 注意含冒号引语 | 「knowledge is power」原句含冒号，中文 note 若转述含「: 」须单引号包裹（yaml 已按规则处理） |
| Manhattan Project 定位 | 是在哥伦比亚大学「为曼哈顿计划进行数学与统计研究」，勿写成「参与研制原子弹」的工程叙述 |
| 规制俘获表述 | 1971 Economic Theory of Regulation：利益集团利用政府规制与强制权力塑造利于自己的法规——照录理论内容；「public choice 的组成部分但遭 Virginia School 深切反对」客观转述 |
| Stigler diet | 得名于其 1945 论文 The Cost of Subsistence（最低成本饮食的线性规划），是运筹学梗非营养学主张 |
| Trivia 不入正文 | 伯外叔祖 Antal Koppány 与 Bobby Fischer 弈和——趣闻仅可作脚注/侧边彩蛋，勿入主线 |
| 儿子 Stephen Stigler | 统计学家（科学史统计著名），page.md See also 明载 his son，入库 parent-child |
| metadata 冲突 | metadata.json 与 page.md 冲突时以 page.md 为准 |

## 七、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| economics of information | 信息经济学 | 1961 开创领域，勿与「信息不对称」（Akerlof）混为同一贡献 |
| search unemployment | 搜寻失业 | 1962 论文提出，与摩擦性失业相关 |
| regulatory capture | 规制俘获 | 1971 理论核心词，勿译「监管捕获」失准 |
| public choice | 公共选择 | 规制俘获所属领域 |
| Stigler diet | 斯蒂格勒饮食 | 1945 线性规划最低成本食谱，趣闻背景 |
| Stigler's Law of Demand and Supply Elasticities | 斯蒂格勒弹性定律 | spoof 戏作，勿当严肃理论 |
| history of economic thought | 经济思想史 | 其研究主干之一 |
| The Economics of Information | 《信息经济学》 | 1961 JPE 论文 |
| What Can Regulators Regulate | 《规制者能规制什么》 | 1962 与 Friedland 合著实证 |
| Memoirs of an Unregulated Economist | 《一个不受规制经济学家的回忆录》 | 1985 自传 |

## 八、背景音乐选择 【人物专属】

- **选定曲目**：**Cinematic Experience**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：电影感的大开大合贴合 Stigler 的智识锋芒与戏剧性人生切面——从西雅图德语童年到 Knight 门下惊险过关、从曼哈顿计划的秘密统计到 1961 年凭一篇论文开创一个领域；幽默家的一生本身即是一部雅致的传记电影。
- **本地路径**：复制 `music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav` 到 `economics/presentations/20th_century/George_Stigler/CinematicExperience.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 九、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/20th_century/George_Stigler/page.md` | ★ 事实基准 |
| `economics/presentations/pages/20th_century/George_Stigler/metadata.json` | 结构化参考（冲突以 page.md 为准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` | 任务流程第三章 |
| `MySQL/data/George_Stigler.yaml` | 已入库 yaml 存档 |
| `economics/PROMPTS_WORKFLOW.md` | 批量作业手册 |

## 十、执行清单 【模板通用】

1. 建目录 `economics/presentations/20th_century/George_Stigler/`（`images/` 子目录）。
2. 肖像：images.txt 有 URL 直接用（250px 改 500px）；无 URL 用 Commons `Special:FilePath`（curl 加 `-A "Mozilla/5.0"`，`file` 验证），404 则装饰圆占位。
3. 复制参照 Makefile，设 `MAIN=George_Stigler_zh`、`VIDEO_NAME=George_Stigler_zh`。
4. 按 §五 写 15 帧；每帧 `make` 编译，`pdftoppm` 截图目检。
5. 编译达标：0 error、vbox ≤ 10pt、hbox ≤ 50pt。
6. `make images && make video` 出 mp4；核对 BGM 时长。
7. Review-1 修正写回本提示词。

## 十一、版式补遗 【模板通用】

- 表格页安全负间距：顶部 `-0.35cm`、`arraystretch 0.78–0.82`；公式框/引语框前 `-0.35 ~ -0.55cm`。
- 引语页（1961 信息经济学名句）含冒号与斜体书名，英文行 `\itshape`、中译行 `\small`；冒号在 CJK 上下文注意半角。
- 幽默页三条 spoof 条目用 itemize 压缩（`\itemsep -2.5pt` + 顶部 `-0.55cm`）；勿超过 `-0.65cm` 遮副标题。
- 价格标签母题 tikz：标签节点 ≤7 个、`inner sep` ≤2pt 防溢出；`\foreach` 分隔符 ASCII 逗号。
- 宏名禁数字；文本模式希腊字母转数学模式；★/① 等符号注意字体缺字（①-④ 需 `\xeCJKDeclareCharClass{CJK}{"2460->"2473}`）。

## 十二、生平时间线节点 【人物专属】

> 供时间线页/身份信息页取材（全部出自 page.md，勿外加）：

| 年份 | 事件 |
|------|------|
| 1911-01-17 | 生于华盛顿州西雅图；母匈牙利裔（Erzsébet Hungler，生于 Bakonypéterd）、父巴伐利亚裔 |
| 童年 | 家中讲德语（德匈后裔） |
| 1931 | 华盛顿大学文学学士（BA） |
| 1932 | 西北大学 MBA——在校期间对经济学产生兴趣、决意学术道路 |
| 1933 | 获芝加哥大学学费奖学金，入芝加哥攻读经济学 |
| 1936–38 | 任教艾奥瓦州立学院 |
| 1938 | 芝加哥大学经济学博士（Knight 指导） |
| 二战 | 大部分时间在哥伦比亚大学为曼哈顿计划做数学与统计研究 |
| 1946–47 | Brown 大学一年 |
| 1947–58 | 哥伦比亚大学教职 |
| 1955 | 当选美国哲学会会员 |
| 1959 | 当选美国艺术与科学院院士 |
| 1961 | 《信息经济学》（JPE）——Friedman 称其「开创了经济学家的一个新研究领域」 |
| 1962 | Information in the Labor Market（搜寻失业）；与 Friedland 合著 What Can Regulators Regulate；当选 ASA Fellow |
| 1963 | 与 Samuelson 合著《国家经济作用对话》；Capital and Rates of Return 出版 |
| 1965 | 《经济思想史论文集》结集出版 |
| 1971 | 《规制的经济理论》（规制俘获） |
| 1975 | 当选美国国家科学院院士 |
| 1977 | 创立经济与国家研究中心（芝加哥商学院）；与 Hayek 等的学圈往来见各人页面 |
| 1982 | 获诺贝尔经济学奖；诺奖演讲 The Process and Progress of Economics（12-08） |
| 1985 | 出版自传 Memoirs of an Unregulated Economist |
| 1987 | 获美国国家科学奖章（National Medal of Science） |
| 1991-12-01 | 逝于伊利诺伊州芝加哥，享年 80；研究中心身后冠名 George J. Stigler Center |

## 十三、肖像与图像素材指引 【人物专属】

- **优先**：`images.txt` 列出的 infobox 肖像（250px 改 500px 下载）。
- **备用**：Commons `Special:FilePath/<文件名>?width=600`（curl 加 `-A "Mozilla/5.0"`，`file` 验证为真图）。
- **404 兜底**：装饰圆占位（姓名首字母 + 主色），图注注明「肖像暂缺」。
- **禁用**：Chicago school 侧栏任何头像链接；与儿子 Stephen Stigler（统计学家）混淆的照片；Trivia 节的 Bobby Fischer 相关图像。

