# 经济学家立传提示词（John Forbes Nash Jr.）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1994 年得主 John F. Nash Jr.（小约翰·福布斯·纳什）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/John_Forbes_Nash_Jr./page.md`，与其冲突时以 page.md 为准（同目录 metadata.json 仅作结构化参考）。

## 一、背景信息 【人物专属】

- **目标数学家/经济学家**：John Forbes Nash Jr.（1928-06-13 生于西弗吉尼亚州布鲁菲尔德 ~ 2015-05-23 与妻同日车祸逝于新泽西州门罗镇，享年 86 岁）
- **气质关键词**：**非合作博弈均衡的发现者、浸入嵌入定理的证明者、从精神分裂中「理性归来」的双奖得主（Nobel 1994 + Abel 2015）**
- **诺奖获奖理由**（1994，与 John Harsanyi、Reinhard Selten 三人共享，manifest citation 逐字）：
  > "for their pioneering analysis of equilibria in the theory of non-cooperative games"（表彰他们在非合作博弈理论中关于均衡的开创性分析）
- **设计母题**：**均衡点与对称破缺（equilibrium & symmetry）**——纳什均衡是「没有人能靠单独改变策略而获益」的不动点：以多元策略交汇的不动点网格、彼此制衡的对称线与渐渐重归的轨迹构成背景母题，呼应「博弈、几何、偏微分方程三个世界的同一双手」。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/John_Forbes_Nash_Jr./page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）
- **一句话画像**：卡内基理工 BS+MS 双学位一年拿下（1948），普林斯顿 28 页博士论文定义纳什均衡；MIT 时代证明纳什嵌入定理、与 De Giorgi 各自独立解决 Hilbert 第十九问题的正则性；1959 年起精神分裂症缠身三十年，在普林斯顿数学系的宽容中「用理性驱逐妄想」；1994 获诺贝尔经济学奖、2015 领 Abel 奖数日后与妻车祸同逝。
- **学科身份注记**：Nash 的 primary_occupation 是 **mathematician**（库内既有 stub 同口径），诺奖系经济学奖——立传以「数学家获经济学诺奖」的双冠视角展开，fields 以博弈论为首。

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/John_Forbes_Nash_Jr./`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=John_Forbes_Nash_Jr._zh`、`VIDEO_NAME=John_Forbes_Nash_Jr._zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。
> 布局检查照模板第 8 步：每写完一页 `make distclean && make`，`pdftoppm` 截图逐页目检溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

## 三、研究领域梳理 + 入库 【人物专属】

**Nash 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | game theory | 博弈论 | 1994 诺奖核心：非合作博弈均衡（纳什均衡）与议价解 | 封面、核心页 |
| 1 | differential geometry | 微分几何 | MIT 时代：纳什嵌入定理（1953 C1 / 1956 C∞） | 嵌入页 |
| 2 | partial differential equations | 偏微分方程 | De Giorgi-Nash 定理；Nash inequality；2015 Abel 奖理由 | PDE 页 |
| 3 | real algebraic geometry | 实代数几何 | 研究生时代证明 Nash 流形/Nash 函数定理（1950 ICM 宣布） | 代数页 |

补充说明（供立传 agent 取材）：四大成果群——①博弈论（1950a 议价问题 Econometrica；1950b n 人均衡 PNAS；1951 非合作博弈 Annals；1953 二人合作博弈）；②实代数几何（1950 ICM 宣布、1951 定稿：光滑流形可由多项式零集表示，Michael Artin/Barry Mazur 用于动力系统）；③嵌入定理（第一定理 1953 C1 等距嵌入、Nash-Kuiper 改进；第二定理 1956，1999 获 Steele Prize；Moser 扩展为 Nash-Moser 定理；Gromov 的 convex integration 系其思想的当代延伸）；④PDE（Morrey 二变量结果的推广至多变量+抛物型；Nash inequality 证明归功 Elias Stein；解决 Hilbert 第十九问题的一种形式）。1945-1996 共发表 23 篇论文。1978 von Neumann Theory Prize（与 Carlton Lemke）；1996 NAS 院士；2015 Abel Prize（与 Louis Nirenberg，"for striking and seminal contributions to the theory of nonlinear partial differential equations and its applications to geometric analysis"）。

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Albert W. Tucker | Tucker → 导师 | 普林斯顿博士导师（1950，28 页论文《Non-Cooperative Games》；库内既有边沿用幂等） |
| co-honored | John Harsanyi | 无向 | 1994 经济学奖三人共享（非合作博弈均衡开创性分析） |
| co-honored | Reinhard Selten | 无向 | 1994 经济学奖三人共享（非合作博弈均衡开创性分析） |
| co-honored | Louis Nirenberg | 无向 | 2015 Abel 奖共享（非线性偏微分方程及其几何分析应用） |
| spouse | Alicia Lardé Lopez-Harrison | 无向 | MIT 物理系毕业生、萨尔瓦多裔归化公民；1957 结婚、1963 离异、2001 复婚；2015-05-23 同日车祸双亡 |
| collaborator | Lloyd Shapley | 无向 | 合著《A simple three-person poker game》(1950，收入 von Neumann/Morgenstern 系列卷) |
| influence | Richard Duffin | 无向 | 卡内基理工本科导师，致普林斯顿推荐信原文 "He is a mathematical genius" |
| influence | John Lighton Synge | 无向 | 其教师建议从化工转化学再转数学 |
| colleague | Ennio De Giorgi | 无向 | De Giorgi-Nash 定理独立平行发现（方法几乎无关、纳什的更强可兼抛物型） |
| colleague | Jürgen Moser | 无向 | Moser 把其嵌入思想扩展为 Nash-Moser 定理（天体力学等应用） |

**不入库但提示词可叙述**：John Milnor（库内既有 Milnor→Nash colleague 边由 Milnor 侧维护，本篇不重写；普林斯顿同期+1954 实验博弈论文合作仅文献记载）；Harold W. Kuhn（博弈论文集编者+1950 扑克论文编者身份，无对等关系类型）；Eleanor Stier（伴侣并生长子 John David Stier，无白名单类型）；二子 John David Stier 与 John Charles Martin Nash（后者高中确诊精神分裂、后获 Rutgers 数学 PhD——仅具名叙述，parent-child 不入）；Warren Ambrose（告知嵌入猜想）、Louis Nirenberg 的椭性猜想转告与 Paul Garabedian 的 De Giorgi 情报（一次性学术信息传递）；Peter Lax（"stroke of genius" 评价）、Mikhael Gromov（两段大段评价引文）、Klaus Roth/René Thom（1958 Fields 委员会投票前三，档案史实）；Sylvia Nasar / Ron Howard / Russell Crowe（传记与电影）；Heisuke Hironaka（"Nash blowing-up" 命名者）。

## 五、配色方案 【人物专属】

- **气质**：深邃、天才的孤光、理性与暗流的拉锯
- **主色**：`#1E3A5F`（manifest 预分配，深海蓝——不动点的冷静与普林斯顿夜色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeGame` 博弈论 — 深海蓝 `#1E3A5F`
  - `badgeEmbed` 嵌入定理 — 青绿 `#0E7C7B`
  - `badgePDE` 偏微分方程 — 玫瑰 `#C4204F`
  - `badgeMind` 理性归来 — 琥珀 `#C07A2A`
- **背景母题**：不动点网格与渐归轨迹（策略交汇点发亮、发散轨迹被弧线拉回），呼应纳什均衡与「用理性驱逐妄想」的归来叙事。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex，品牌口径 OpenMathAI）
01  封面 — 均衡的发现者 / John F. Nash Jr. 1928–2015 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格：生卒（1928-06-13 Bluefield ~ 2015-05-23 Monroe Township，
    享年 86）、教育（Carnegie Tech BS+MS 1948 / Princeton PhD 1950）、任职（MIT C.L.E. Moore
    讲师 1951-59 / Princeton 至终老）、双奖（Nobel 1994 + Abel 2015）、核心领域
03  核心贡献概览 — 纳什均衡 / 嵌入定理 / De Giorgi-Nash 定理 / 实代数几何（四 badge 横排）
04  布鲁菲尔德神童 (1928–1945) — 电气工程师之父与教师之母；Bluefield College 先修数学课；
    13 岁书房实验；George Westinghouse 奖学金
05  卡内基与普林斯顿 (1945–1950) — 化工→化学→数学（Synge 建议）一年双学位；
    Duffin 推荐信 "He is a mathematical genius"；Lefschetz 的 Kennedy fellowship；
    在普林斯顿开始均衡理论
06  纳什均衡 (1950–1951)（核心贡献页）— 28 页博士论文《Non-Cooperative Games》（Tucker 门下）；
    1950b PNAS 一页纸定义均衡点；1951 Annals 完整版；议价问题与 Nash bargaining solution
07  合作博弈与扑克 (1950–1953) — 与 Shapley 合著三人扑克；二人合作博弈 (1953)；
    Mayberry-Nash-Shubik 双寡头比较
08  实代数几何 (1949–1952) — 光滑流形=多项式零集（1950 ICM 宣布、1951 定稿）；
    Nash 流形与 Nash 函数；Artin/Mazur 的动力系统应用
09  嵌入定理 (1953–1956)（核心贡献页）— C1 等距嵌入与 Nash-Kuiper 改进；
    C∞ 第二定理：损失正则性的隐函数定理；Steele Prize 1999；
    Gromov 的 convex integration 延伸
10  De Giorgi-Nash 定理 (1957–1958)（核心贡献页）— Nirenberg 的猜想、Hörmander 的讨论；
    多变量+抛物型推广；Hilbert 第十九问题的一种解决；Lax 称 "stroke of genius"；
    1958 Fields 投票第三（Roth/Thom 之后，档案史实）
11  密码学的先声 — 1950 年代致 NSA 的信（2011 解密）：预期了现代密码学的计算困难性概念
12  漫长的暗流 (1959–1970) — 1959 哥伦比亚讲座的失序；McLean 与 Trenton 住院；
    "John Nash, Emperor of Antarctica" 的信件；电影与事实的出入（服药描述）
13  理性归来 (1970–2015) — 普林斯顿数学系的宽容与 Alicia 的收留；"enforced rationality"；
    1994 三十年病期自省；1995 自述未竟潜力；1999 CMU 荣誉博士等
14  双奖与终章 — von Neumann Prize 1978（与 Lemke）/ Nobel 1994（Harsanyi/Selten 共享）/
    NAS 1996 / Steele 1999 / Abel 2015（Nirenberg 共享）——2015-05-19 奥斯陆领奖、
    五日后新泽西 Turnpike 车祸与 Alicia 同逝 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 学科身份 | Nash 是数学家获**经济学**诺奖（与 Harsanyi/Selten 三人共享、同一句理由）；primary_occupation 保持库内 mathematician 口径，勿改成 economist |
| 姓名与库内记录 | 库内既有三条 stub（#205 John F. Nash Jr. / #429 John Nash / #967 John Forbes Nash）：本批次以 manifest 名 **John Forbes Nash**（#967）为准 UPD；Milnor 侧既有 colleague 边由 #429 改指 #967；#205 空壳删除——分裂合并已由本批次完成 |
| 共享奖口径 | 1994 与 Harsanyi、Selten 共享（b08 批对手方，manifest 规范名 John Harsanyi / Reinhard Selten）；2015 Abel 与 Louis Nirenberg 共享——两种 co-honored 边并存，note 分写 |
| 卒日叙事 | 2015-05-23 新泽西 Turnpike 出租车车祸，未系安全带被抛出，与妻 Alicia 同日双逝——领 Abel 奖（2015-05-19 奥斯陆）返程；时间线精确勿散置 |
| 精神分裂叙述 | 客观克制：1959 起病、住院、1970 后不再住院、逐渐康复、「enforced rationality」自我描述；1995 自述因病近 30 年未竟全潜力；不猎奇、不诊断、不评价；1994 写作段 page.md 有英文原文可引 |
| 电影与事实 | 《A Beautiful Mind》服药情节与事实不符（Nash 本人指出）；电影批评（省略 Eleanor Stier 与长子）客观并置；Nasar 1998 书与 2001 电影只作文化背景 |
| Fields 遗珠 | "Nash placed third in the committee's vote for the medal, after Klaus Roth and René Thom"——档案研究史实，措辞「档案研究显示投票第三」，勿写成「因 De Giorgi 同时发现而落选」的因果断言 |
| Nash-Moser vs De Giorgi-Nash | 两个「Nash 定理」完全不同：前者是嵌入思想的隐函数定理推广（Moser 扩展、天体力学应用）；后者是椭圆/抛物方程正则性（Moser 另一路径汇流称 De Giorgi-Nash-Moser 理论）——勿混写 |
| Nash inequality 证明 | page.md 明载 Nash 把证明归功 Elias Stein——勿写成纳什自证 |
| 密码学 | 1950 年代 NSA 信件（2011 解密）显示其「anticipated」基于计算困难性的现代密码学概念——勿写成「发明公钥密码」 |
| RAND 与安全许可 | 1954 Santa Monica 诱捕行动被捕（指控撤销）但被吊销 top-secret 许可并解雇——正文明载，客观一笔，勿渲染 |
| 引语红线 | Duffin 推荐信、Gromov 两段评价、Lax 一句、Nash 1994 自述段、1995 访谈句均 page.md 有英文原文可引；中文引号内不得出现无原文支撑的「原话」 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Nash equilibrium | 纳什均衡 | 无人能靠单独改策略获益的策略组合；1950b 一页纸+1951 完整版 |
| Nash bargaining solution | 纳什议价解 | 1950a Econometrica；合作博弈侧成果 |
| non-cooperative games | 非合作博弈 | 获奖理由核心词；博士论文标题复数 |
| Nash embedding theorems | 纳什嵌入定理 | 两条：C1 (1953) 与 C∞ (1956)；勿与 Nash-Moser 混 |
| Nash-Moser theorem | Nash-Moser 定理 | 处理损失正则性的隐函数定理（Moser 扩展） |
| De Giorgi-Nash theorem | De Giorgi-Nash 定理 | 椭圆/抛物方程解的连续性；与 Moser 路径汇流 |
| Nash inequality | Nash 不等式 | Sobolev 不等式家族；证明归功 Elias Stein |
| Nash blowing-up | Nash 爆破 | 奇点消解变换（Hironaka 命名） |
| real algebraic manifold | 实代数流形 | 光滑流形的多项式零集表示（1952b） |
| ideal money | 理想货币 | 晚年货币思想（自述与 Hayek 平行），2002 论文；一笔即可 |
| Abel Prize | 阿贝尔奖 | 2015 与 Nirenberg 共享；理由句逐字引用 |
| John von Neumann Theory Prize | 冯·诺依曼理论奖 | 1978 与 Carlton Lemke 共享（博弈论贡献） |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Pathfinder**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：「探路者」是纳什一生的双重隐喻——学术上，他在博弈、几何、PDE 三个互不相通的世界里各辟新路（均衡点、嵌入定理、正则性）；人生上，他从精神分裂的暗流中靠「强制理性」一步步走回数学。Pathfinder 的行进感与克制的张力，恰好托住这条从不动点到归来之路的叙事弧线。
- **本地路径**：复制 `music_audio/inspiring-electronic/23-GiwYLGgJw7w-Ghostwriter Music - Pathfinder (Composed by Daniel Beijbom - Recorded in Budapest).wav` 到 `economics/presentations/20th_century/John_Forbes_Nash_Jr./Pathfinder.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
