# 经济学家立传提示词（Robert Aumann）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2005 年得主 Robert Aumann（罗伯特·奥曼）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Robert_Aumann/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Robert John Aumann（伊斯拉埃尔·奥曼 ישראל אומן，1930-06-08 生于德国法兰克福，在世）
- **气质关键词**：**重复博弈的大师、共同知识的形式化者、从纽结理论走进博弈论的数学家**
- **诺奖获奖理由**（2005 全年共享理由，manifest `citation_en`/`citation_zh` 已给出；与 `nobel_economics_citations.json` 2005 年本人条目一致）：
  > "for having enhanced our understanding of conflict and cooperation through game-theory analysis"（表彰他们通过博弈论分析增进了我们对冲突与合作的理解）
- **设计母题**：**无限镜像（infinite reflection）**——两面相对的镜面无限反射、层层递归，是「重复博弈的无穷视界、共同知识的递归结构」的视觉隐喻：双方在一次次相遇中学会合作，构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Robert_Aumann/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Robert_Aumann/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Robert_Aumann_zh`、`VIDEO_NAME=Robert_Aumann_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至十二节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Aumann 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | game theory | 博弈论 | infobox Discipline；诺奖核心 | 封面、核心页 |
| 1 | repeated games | 重复博弈 | page.md 明载的最大贡献所在 | 核心页 |
| 2 | mathematical economics | 数理经济学 | infobox Discipline；数学方法进入经济学 | 全篇 |
| 3 | decision theory | 决策理论 | Anscombe–Aumann 框架 | 方法页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | George W. Whitehead | 师→生（博士导师） | MIT 数学博士导师（1955），纽结理论论文《Asphericity of Alternating Linkages》 |
| collaborator | Lloyd Shapley | 无向 | Aumann–Shapley 值；1974 合著《Values of Non-Atomic Games》（库内 id=968） |
| colleague | Michael Maschler | 无向 | 塔木德遗产分配之谜合作者；1995 合著《Repeated Games with Incomplete Information》 |
| co-honored | Thomas Schelling | 无向 | 2005 诺贝尔经济学奖共享（博弈论分析增进对冲突与合作的理解） |
| advisor-student | David Schmeidler | Aumann → 学生 | 博士生（infobox 与正文明载） |
| advisor-student | Sergiu Hart | Aumann → 学生 | 博士生；合编《Handbook of Game Theory》三卷 |
| advisor-student | Abraham Neyman | Aumann → 学生 | 博士生（infobox 与正文明载） |
| advisor-student | Yair Tauman | Aumann → 学生 | 博士生；1981 希伯来文《Game Theory》合著 |
| spouse | Esther Schlesinger | 无向 | 1955-04 于布鲁克林结婚，1998-10 病逝 |
| spouse | Batya Cohn | 无向 | 2005-11 再婚，亡妻 Esther 之妹 |
| parent-child | Shlomo Aumann | 父 → 子 | 长子，1982 黎巴嫩战争阵亡坦克炮手；论文献予他 |

**不入库但提示词可叙述**：其余四子（仅具名不具姓，防臆造）；堂亲 Oliver Sacks（旁系无关系类型可挂）；Machon Shlomo Aumann（以其子命名的机构）；Doron Witztum/Eliyahu Rips/Yoav Rosenberg（圣经密码论文作者，争议事件人物）；1996 委员会成员 Dror Bar-Natan/Hillel Furstenberg 等（一次性事件）。

## 五、配色方案 【人物专属】

- **气质**：深邃、递归、理性与信仰交织
- **主色**：`#37548D`（镜像蓝——重复博弈无穷视界的深遂底色；manifest 预分配）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeRep` 重复博弈 — 镜像蓝 `#37548D`
  - `badgeCorr` 相关均衡 — 青绿 `#0E7C7B`
  - `badgeCK` 共同知识 — 琥珀 `#C07A2A`
  - `badgeTalm` 塔木德与传统 — 砖红 `#6E2B2B`
- **背景母题**：两面相对的镜面无限反射成纵深的金色走廊，愈远愈淡，呼应「重复博弈中合作的幽灵在无穷视界里显形」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 重复博弈的大师 / Robert Aumann 1930– + 四色 badge + 右上头像 + 国籍行（美国 / 以色列）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生地法兰克福、1938 移美、CCNY 学士 1950、
    MIT 硕士 1952/博士 1955、希伯来大学 1956–、Stony Brook 访问、诺奖 2005、核心领域）
03  核心贡献概览 — 重复博弈 / 相关均衡 / 共同知识 / Aumann–Shapley 值
04  法兰克福与出逃 (1930–1938) — 出生两周前之水晶之夜、全家赴美、犹太经学院中学
05  纽约与 MIT (1950–1955) — CCNY 数学学士、MIT 硕博、拓扑学家 Whitehead 门下、纽结理论论文
06  希伯来大学 (1956– ) — 数学系任教、理性研究中心、访学版图（Berkeley/Stanford/Louvain）
07  重复博弈与相关均衡（核心贡献页）— 首次定义相关均衡、比纳什均衡更灵活的均衡概念
08  共同知识：不能同意分歧（核心贡献页）— agreement theorem、共同先验的贝叶斯理性者
09  塔木德与博弈论 — 与 Maschler 破解「分配问题」之谜；论文献予亡子 Shlomo（客观一句）
10  Aumann–Shapley 值 — 与 Shapley 1974《Values of Non-Atomic Games》
11  2005 诺贝尔经济学奖 — 与 Schelling 共享（130 万美元平分）；演讲 War and Peace 三主题（客观）
12  荣誉与认可 — Israel Prize 1994、Nemmers 1998、EMET 2002、Harvey 1983、
    von Neumann Theory Prize、AAAS 外籍荣誉会士 1974、NAS 成员、Yakir Yerushalayim 2006
13  圣经密码争议 — 1996 五人委员会两次检验未证实密码存在；结论引语（英文原文）
14  遗产与结尾 — Stony Brook 博弈论中心创始成员、现代博弈论基石 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| ★ 政治内容红线 | page.md「Political views」整节敏感（PSI 成员、反对 2005 加沙撤离、Blackmailer Paradox、Ahi 政党、Bnei Akiva 演讲）：**一律不进幻灯片**；如需提及仅限一句客观句「其政治立场使获奖决定在欧洲媒体受到批评，并有千人联署请愿」，禁任何评价、演绎与展开 |
| 诺奖演讲口径 | War and Peace 三主题可客观列出（战争并非非理性、可科学研究以图征服 / 重复博弈研究重「后来」轻「现在」 / 简单化媾和可能引发战争而军备竞赛与可信威胁可阻止战争）——系学术内容，保持原义、零引申 |
| 圣经密码争议 | 学术争议可写：1996 年五人委员会（含本人）两次检验均未能证实「密码」存在；结论必须用 page.md 英文原文（"A priori, the thesis of the Codes research seems wildly improbable..."），禁中文化冒充原话 |
| 亡子书写 | Shlomo Aumann 1982 黎巴嫩战争阵亡（装甲兵团坦克炮手）；塔木德论文献予他、Machon Shlomo Aumann 以他命名——**客观、克制、一句带过**，禁渲染 |
| 国籍口径 | manifest country "United States / Israel"（Nobel 口径）；frontmatter 顺序以色列在前系 Wikidata 噪声；yaml 按 manifest 顺序 US rank0/Israel rank1；封面国籍行写「美国 / 以色列」 |
| 博士导师学科 | George W. Whitehead 是 MIT **拓扑学家**、数学博士导师，论文为纽结理论《Asphericity of Alternating Linkages》（1955）；勿写成经济学导师 |
| 库内复用 | Shapley 用库内 Lloyd Shapley（id=968）；本人记录与 Georg Aumann（id=840，数学家）无关，勿混 |
| 与 Schelling 的对手方名 | co-honored 对手方用 manifest 形式 "Thomas Schelling"（其本人批次 econ21th-batch-03 建/回填 Q206460）；本 yaml 预建 stub，对方批次 UPD 回填，零分裂 |
| 在世口径 | 1930 年生在世：封面写 1930–，身份页卒年留白，全文勿写卒年 |
| 奖金口径 | 2005 奖金 130 万美元与 Schelling **平分**（page.md Honours 明载 share），勿写成独得或全数 |
| 名字双形 | Robert John Aumann / 希伯来名 Yisrael Aumann（ישראל אומן）并存，封面可注希伯来名（需希伯来字体族支持，否则省略） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| repeated game | 重复博弈 | 获奖核心场景，勿译「迭代博弈」 |
| correlated equilibrium | 相关均衡 | Aumann 首次定义，比纳什均衡更灵活 |
| common knowledge | 共同知识 | 形式化第一人 |
| agreement theorem | 「不能同意分歧」定理 | 共同先验的贝叶斯理性者 |
| Aumann–Shapley value | Aumann–Shapley 值 | 与 Shapley 合作成果 |
| non-atomic games | 非原子博弈 | 1974 专著主题 |
| folk theorem | 无名氏定理 | 重复博弈经典结果 |
| Anscombe–Aumann framework | Anscombe–Aumann 框架 | 主观期望效用决策框架 |
| bankruptcy problem / division problem | 分配问题（破产问题） | 塔木德遗产分配之谜 |
| Blackmailer Paradox | 勒索者悖论 | **仅术语表收录**，幻灯片禁展开（涉政治敏感） |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Savage**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：「冲突与合作」是一体两面——Savage 的原始张力感贴合博弈论直面战争与和平的勇气，也呼应重复博弈中从对峙走向合作的戏剧弧线；递归渐强的配器与无限镜像母题同构。
- **本地路径**：复制 `music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav` 到 `economics/presentations/21th_century/Robert_Aumann/Savage.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/21th_century/Robert_Aumann/page.md` | 事实基准（唯一事实来源） |
| `economics/presentations/pages/21th_century/Robert_Aumann/metadata.json` | 结构化参考（冲突以 page.md 为准） |
| `economics/presentations/pages/21th_century/Robert_Aumann/images.txt` | 肖像候选 URL |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `economics/presentations/cover/` | OpenEcon 统一封面 |
| `economics/nobel_economics_citations.json` | 2005 年获奖理由原文核对 |

## 十一、执行清单 【模板通用】

1. 通读本提示词与 page.md，建立事实卡（生卒/学位/机构/奖项/关系五组）。
2. 下载肖像（images.txt 或 Commons `Special:FilePath`，500px；404 则装饰圆占位；page.md 内嵌 GPO 2005 年照可作候选）。
3. 复制 Makefile，设 `MAIN=Robert_Aumann_zh`、`VIDEO_NAME=Robert_Aumann_zh`；复制 BGM wav。
4. 按 §六逐页写 Beamer tex；每页 `make` 检查溢出（vbox≤10pt、hbox≤50pt）。
5. `make pdf` 0 error → `pdftoppm` 逐页目检 → `make images && make video` 出 mp4。
6. 数据库已由本批次入库（has_social_data=1），立传完成后由主控将 has_biography 置 1。

## 十二、版式补遗 【模板通用】

- 表格页安全负间距：顶部 −0.35cm、`arraystretch 0.78–0.82`；公式框前 −0.35~−0.55cm。
- 文本模式希腊字母需数学模式；带圈数字需 `\xeCJKDeclareCharClass{CJK}{"2460->"2473}`。
- 引号用半角 `" "`；品牌口径统一 `OpenMathAI`；`\foreach` 分隔符用 ASCII 逗号。
- 若排希伯来文需专用字体族（参照 Adi_Shamir 篇做法）；无把握则省略希伯来名。
- 结尾页底部标注 GitHub 链接由首页模板 `\input` 继承，子 deck 不重复。
