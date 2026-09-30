# 经济学家立传提示词（James M. Buchanan）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1986 年得主 James M. Buchanan（詹姆斯·布坎南）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/James_M._Buchanan/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：James McGill Buchanan Jr.（1919-10-03 生于田纳西州默弗里斯伯勒 ~ 2013-01-09 逝于弗吉尼亚州布莱克斯堡，享年 93 岁）
- **气质关键词**：**公共选择理论的总设计师、没有浪漫的政治经济学家、宪政经济学的奠基人**
- **诺奖获奖理由**（逐字引用）：
  > "for his development of the contractual and constitutional bases for the theory of economic and political decision-making"（表彰他为经济与政治决策理论奠定了契约与宪制基础）
- **设计母题**：**规则的规则（rules of the game）**——宪法层面定规则、后宪法层面玩游戏，是「政治作为交换」的视觉隐喻：棋盘格线之上再叠一层格线、一枚金色契约印章构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/James_M._Buchanan/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/James_M._Buchanan/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=James_M._Buchanan_zh`、`VIDEO_NAME=James_M._Buchanan_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Buchanan 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | public choice theory | 公共选择理论 | 诺奖核心：经济学方法研究政治行为 | 核心页 |
| 1 | constitutional economics | 宪政经济学 | 契约与宪制基础、规则的规则 | 宪政页 |
| 2 | public finance | 财政学 | 税收、公债与财政公平起点 | 财政页 |
| 3 | public goods theory | 公共物品理论 | Wicksell–Lindahl 传统的再表述 | 公共品页 |
| 4 | political economy | 政治经济学 | 弗吉尼亚学派、政治作为交换 | 学派页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Frank Knight | Buchanan ← 导师 | 芝加哥「de facto」博士导师，六周转向市场秩序（正文+frontmatter 双明载） |
| collaborator | Gordon Tullock | 无向 | 1962《同意的计算》合著、公共选择学会与《Public Choice》期刊共同创办 |
| collaborator | G. Warren Nutter | 无向 | 1956 共创杰斐逊中心、1959 合著《普遍教育的经济学》 |
| advisor-student | Richard E. Wagner | Buchanan → 学生 | 1960s 门下弟子（Wagner 自述），1967/1977 两书合著 |
| collaborator | Geoffrey Brennan | 无向 | 1980《课税的权力》与 1985《规则的理由》合著 |
| colleague | Richard A. Musgrave | 无向 | 布鲁金斯 NBER 财政顾问委员会同席、称其论文 pioneering |
| colleague | Ronald Coase | 无向 | 弗吉尼亚学派同侪（page.md 列名） |
| colleague | George Stigler | 无向 | 弗吉尼亚学派同侪（page.md 列名） |
| colleague | Alexandre Kafka | 无向 | 弗吉尼亚学派同侪（page.md 列名） |
| colleague | Leland B. Yeager | 无向 | 弗吉尼亚学派同侪（page.md 列名） |
| influence | Knut Wicksell | 无向 | 1896 论文 1948 首读并自译，诺奖演讲称其「现代公共选择的重要先行者」 |
| influence | Thomas Hobbes | 无向 | infobox Influences 明载 |
| influence | Friedrich Hayek | 无向 | infobox Influences 明载 |
| influence | Ludwig von Mises | 无向 | 1954 后对照《Human Action》自述深受启发 |
| influence | Maffeo Pantaleoni | 无向 | 富布赖特意大利年所读意大利财政学派，自称思想先祖 |
| influence | Antonio De Viti De Marco | 无向 | 意大利财政学派，「思想先祖」 |
| influence | Vilfredo Pareto | 无向 | 意大利财政学派，「思想先祖」 |
| spouse | Anne Bakke | 无向 | 1945-10-05 旧金山结婚，无子女，2005 妻先逝 |
| controversy | Nancy MacLean | 无向 | 2017《锁链中的民主》引发学界争论（Fleury–Marciano 2018 JEL 评述等回应） |

**不入库但提示词可叙述**：祖父 John P. Buchanan（田纳西州长，1891–93，家族叙述不建 parent-child 隔代边）；James C. Miller III、Charles J. Goetz（中心共事，叙述即可）；1963 夏洛茨维尔会议出席者 Olson/Riker/Ostrom/Downs/Duncan Black/Rawls 等（一次聚会名单，防噪声）；Tyler Cowen/Alexander Tabarrok（GMU 后辈对 Calhoun 渊源的考据，叙述）；Gordon Anderson（远房表亲）。

## 五、配色方案 【人物专属】

- **气质**：契约的冷峻、规则的秩序、田纳西农场的固执
- **主色**：`#2F5D50`（宪章青——规则之上的规则的沉静）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgePC` 公共选择 — 深青 `#2F5D50`
  - `badgeConst` 宪政经济学 — 靛蓝 `#2E3A59`
  - `badgeFin` 财政学 — 琥珀 `#C07A2A`
  - `badgeVS` 弗吉尼亚学派 — 灰紫 `#52307C`
- **背景母题**：棋盘格线之上再叠一层半透明格线、一枚金色契约印章——「宪法层面定规则、后宪法层面玩游戏」的双重结构。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 公共选择理论的总设计师 / James M. Buchanan 1919–2013 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地田纳西、教育 MTSU/田纳西大学/芝加哥 PhD 1948、
    任职 GMU/Virginia Tech/UVA、诺奖 1986、核心领域）
03  核心贡献概览 — 公共选择 / 同意的计算 / 宪政经济学 / 财政与公债
04  田纳西农场与二战 (1919–1945) — genteel poverty、祖父藏书室、Nimitz 司令部作战计划军官
05  芝加哥的六周转向 (1945–1948) — Knight 课程、从社会主义到市场秩序、1948 论文
06  威克塞尔的遗产（核心贡献页）— 1948 首读并自译「正义课税的新原则」、一致性投票、办公室墙上的两张照片
07  1962《同意的计算》（核心贡献页）— 与 Tullock、契约与宪制基础、logrolling
08  弗吉尼亚学派与两个中心 (1956–1983) — 杰斐逊中心、公共选择学会与期刊、CSPC 从 VPI 迁 GMU
09  意大利财政学派的滋养 (1955–1956) — Pantaleoni/De Viti/Pareto、公债观、1960 教科书专章
10  政治作为交换（核心贡献页）— politics without romance、行为对称、方法论个人主义
11  《自由的界限》与乌托邦之争 (1975) — magnum opus、无政府思想实验、遗产税 100% 的意外立场
12  荣誉与认可 — Nobel 1986、MPS 主席 1984–86、2006 国家人文奖章、UFM 荣誉博士
13  争议与回响 — MacLean《锁链中的民主》与学界回应、智利顾问经历一句话客观记录
14  遗产与结尾 — 新政治经济学的奠基 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| Knight 的「de facto」 | 芝加哥正式体制下 Knight 是 **de facto** PhD supervisor——行文保留「实际导师」措辞；同时 Knight 也是 Friedman/Stigler 的老师，勿把 Friedman 写成 Buchanan 同门分支 |
| Tullock 的学位 | Tullock 有法学博士、无经济学训练——「布坎南是哲学家、图洛克是科学家」的互补描述照 page.md 转述，勿写成 Tullock 经济学出身 |
| 政治敏感内容红线 | 智利经历（向 Pinochet 提供政策建议、被指提供军事统治的分析辩护）与 1959 弗吉尼亚择校报告的种族背景均 page.md 明载：**一句话客观记录、多口径并写、零评价**；MacLean 争议与 Fleury–Marciano/Bernstein 的批评回应两面并呈，禁单侧定性 |
| 名言引用 | "politics without romance"、"I want a private sphere..."（1986 Chicago Tribune）等 page.md 有英文原文者可入引文框并标出处；无原文处只转述 |
| 最小工资论战引语 | 1996 WSJ 回应 Card–Krueger 含侮辱性词汇（"camp-following whores"）——引用须完整标注为原文转载，或仅转述其反对立场，避免单独摘出侮辱词 |
| Wicksell 翻译者 | Buchanan 1958 年自德语翻译《A New Principle of Just Taxation》——「翻译者」身份是 page.md 明载事实，勿写成仅读者 |
| 三机构序列 | UVA 1956–68 → UCLA 1968–69 → Virginia Tech 1969–83 → GMU 1983–退休，1998 又回 VTech 任荣休讲座教授——勿漏 UCLA 一年与 1998 回聘 |
| MPS 缩写 | Mont Pelerin Society 主席 1984–86；与 Modigliani 的 MPS 宏观模型是不同 MPS，勿混淆 |
| Arrow 论战 | Buchanan 批评 Arrow 不可能定理、主张轮换与宪政结构——学术分歧入正文叙述，不建 controversy 边（page.md 语境为理论商榷） |
| 无子女 | 与 Anne Bakke 无子女；子女相关 parent-child 边一律不存在，勿据姓氏联想补边 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| public choice theory | 公共选择理论 | 诺奖核心，勿译「公共选择学派」泛称 |
| The Calculus of Consent | 《同意的计算》 | 1962 与 Tullock 合著 |
| constitutional economics | 宪政经济学 | 与宪法学（constitutional law）不同 |
| politics without romance | 没有浪漫的政治 | Buchanan 自创语，须保留英文并列 |
| logrolling | 互投赞成票 | 政治选票交易 |
| unanimity rule | 一致同意规则 | 承自 Wicksell |
| benefit principle | 受益原则 | 税负公平的 Wicksell 机制 |
| Virginia school | 弗吉尼亚学派 | 与芝加哥学派分立 |
| opportunity cost | 机会成本 | 1969《成本与选择》 |
| Samaritan's dilemma | 撒玛利亚人困境 | infobox Notable ideas 之一 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Last Hope**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Buchanan 的终身母题是「为政治寻回制度的约束」——从农场少年的固执到 93 岁的宪政守望，dramatic epic 的曲风承载一个理想主义者把全部赌注押在「规则」上的孤勇，也呼应《自由的界限》中在无政府与利维坦之间寻找最后希望的追问。
- **本地路径**：复制 `music_audio/inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav` 到 `economics/presentations/20th_century/James_M._Buchanan/LastHope.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
