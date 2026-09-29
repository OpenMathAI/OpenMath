# 医学家立传提示词（Christian de Duve）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1974 年得主 Christian de Duve（克里斯蒂安·德·迪夫）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Christian_de_Duve/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Christian René Marie Joseph, Viscount de Duve（1917-10-02 生于英国 Thames Ditton ~ 2013-05-04 逝于比利时 Nethen，享年 95 岁），比利时细胞学家与生物化学家，子爵
- **气质关键词**：**溶酶体与过氧化物酶体的发现者、术语铸造师（autophagy/endocytosis/exocytosis）、偶然性的信徒**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1974 条目，de Duve/Claude/Palade 三人共享）：
  > "for their discoveries concerning the structural and functional organization of the cell"（因其关于细胞结构与功能组织的发现）
- **设计母题**：**静置五天的离心管（the latent acid phosphatase）**——酶活性"迟到"五日回升，膜包围的囊泡就此现形；用「静置离心管与浮出的囊泡」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Christian_de_Duve/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Christian_de_Duve/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Christian_de_Duve_zh`、`VIDEO_NAME=Christian_de_Duve_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**de Duve 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | cell biology | 细胞生物学 | 1974 诺奖学科；细胞器发现 | 核心页 |
| 1 | biochemistry | 生物化学（亚细胞生化） | 酶分布与分级分离 | 核心页 |
| 2 | endocrinology | 内分泌学 | 胰岛素/胰高血糖素，学术起点 | 早年页 |
| 3 | cytology | 细胞学 | cytologist 身份；细胞起源研究 | 晚年页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Joseph P. Bouckaert | 对方 → 导师 | 卢文大学其实验室专攻内分泌学，胰岛素研究起点 |
| advisor-student | Hugo Theorell | 对方 → 进修导师 | 卡罗林斯卡研究所 18 个月（1946-47；库内 id=4015） |
| advisor-student | Carl Ferdinand Cori | 对方 → 进修导师 | 洛克菲勒基金会资助华盛顿大学六个月（1947） |
| advisor-student | Gerty Cori | 对方 → 进修导师 | Cori 夫妇实验室研修（1947 联合诺奖夫妇） |
| colleague | Earl W. Sutherland Jr. | 无向 | 共同发现 HG 因子即胰高血糖素并使其定名（1971 诺奖得主） |
| colleague | Alex B. Novikoff | 无向 | 1955 到访以电镜首次给出溶酶体可视证据 |
| colleague | Albert Claude | 无向 | 同事与挚友，1972 支持其任卢万天主教大学教授 |
| co-honored | Albert Claude | 无向 | 1974 诺贝尔生理学或医学奖三人共享 |
| co-honored | George Emil Palade | 无向 | 1974 诺贝尔生理学或医学奖三人共享 |
| spouse | Janine Herman | 无向 | 1943-09-30 结婚，二子二女，2008 年去世 |
| parent-child | Thierry de Duve | 无向 | 之子，著名艺术学者 |

**不入库但提示词可叙述**：Detlev Bronk（1960 邀其任洛克菲勒教授的所长，招募事件）；Kimball 与 Murlin（1923 年胰高血糖素最初发现者——"再发现"叙事的背景）；W. Bernhard 与 C. Rouillier（microbodies 先行描述者，文献渊源）；L'Oréal-UNESCO 奖创办人身份。

## 五、配色方案 【人物专属】

- **气质**：静置离心管的耐心、鲁汶大学的学术深青、临终选择的澄明
- **主色**：`#0F5257`（溶酶体深青——酶液与膜性囊泡）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeLyso` 溶酶体 — 深青 `#0F5257`
  - `badgePerox` 过氧化物酶体 — 荧光青 `#0E7490`
  - `badgeWord` 术语铸造 — 赭金 `#B07D2B`
  - `badgeOrigin` 细胞与生命起源 — 深紫 `#4A2A6A`
- **背景母题**：静置离心管与膜包围囊泡，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 溶酶体的发现者 / Christian de Duve 1917–2013 + 四色 badge + 右上头像 + 国籍行（Belgium）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、泰晤士迪顿出身（比利时难民之子）、
    鲁汶天主教大学 MD 1941、鲁汶/洛克菲勒双聘、1974 创 ICP（今 de Duve 研究所）、诺奖 1974、核心领域）
03  核心贡献概览 — 胰高血糖素再发现 / 溶酶体 1955 / 过氧化物酶体 1966 / autophagy 等术语
04  难民之子与鲁汶 (1917–1941) — 一战避难英国出生、耶稣会教育、primus perpetuus、
    1940 应征入伍被俘又"比英雄更滑稽"地逃回、MD 1941
05  胰岛素与胰高血糖素（核心贡献页）— Bouckaert 实验室起点、1944 发现 Lilly 胰岛素杂质、
    与 Sutherland 确认 HG 因子=glucagon（1951 复名）、alpha 细胞假说证实、1953 纯化
06  进修之旅 (1946–1947) — Theorell 卡罗林斯卡 18 个月、Cori 夫妇实验室六个月
07  鲁汶与洛克菲勒双聘 (1947–1969) — 1947 教职、1951 正教授、1960 Bronk 邀约、
    校长晚宴折中：1962 两校双聘
08  1955：溶酶体的偶然发现（核心贡献页）— 酸性磷酸酶活性"迟到"之谜、静置五天回升、
    膜性"囊样结构"假说、命名 lysosome
09  Novikoff 的电镜证据 — 1955 到访给出溶酶体首个可视证据、酸性水解酶定位确认
10  1966：过氧化物酶体 — 尿酸氧化酶的困惑、catalase 等三酶同分布、microbodies 之辨、
    命名 peroxisome、1968 大规模制备
11  术语铸造师 — 1963 Ciba 研讨会"在造词的情绪中"一次写下 autophagy/endocytosis/exocytosis
12  1974 诺奖与 ICP — 与 Claude/Palade 共享、同年在布鲁塞尔创办国际细胞与分子病理学研究所
13  荣誉与认可 — Francqui 1960、Gairdner 1967、Heineken 1973、E.B. Wilson 1989、
    1989 子爵爵位、ForMemRS 1988、NAS 外籍院士 1975
14  遗产与结尾 — 内共生理论贡献、生命起源的思辨晚年、2013 合法安乐死（四子女在场）+ 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生地与国籍 | 生于英国泰晤士迪顿（一战比利时难民之子），1920 年三岁返比——**国籍只入 Belgium**（Nobel/citation json 口径），出生地叙述保留 |
| frontmatter 导师噪声 | metadata doctoral_advisor=[Albert Claude, Hugo Theorell]——**正文无载 Claude 为其导师**（两人是挚友同事），博士（agrégation）在鲁汶自胰岛素研究来——Claude 边不建 advisor，建 colleague；Theorell 为进修导师（正文明载） |
| Bouckaert 边 | "wanted to specialize in endocrinology and joined the laboratory of Joseph P. Bouckaert"——研究院系导师边（胰岛素起点） |
| 胰高血糖素口径 | 1923 由 Kimball 与 Murlin 首次发现后被遗忘——de Duve 是**再发现并定名**（1951 复名、1953 纯化）——勿写成"发现胰高血糖素" |
| 溶酶体因果链 | G6P 酶纯化失败→改用酸性磷酸酶标准酶测活性→活性异常低→静置五天活性回升→膜屏障假说→1955 命名 lysosome——逻辑链完整呈现，"serendipitous" 是 page.md 明文定性 |
| 三个造词同刻 | autophagy、endocytosis、exocytosis 均造于 1963-02 伦敦 Ciba 溶酶体研讨会，原话 "in a word-coining mood"（page.md 明载可引） |
| 过氧化物酶体年份 | 1955 年会报告、1966 正式命名发表、1968 首次大规模制备——三段年份勿混；与 Bernhard/Rouillier 的 microbodies 之辨要交代 |
| 死亡口径 | 2013-05-04 于 Nethen 家中经两名医生执行**合法安乐死**，四子女在场；长期癌症+房颤——客观写，安乐死是其公开立场选择，勿渲染；"I'm not afraid of what comes after" 引语 page.md 明载（Le Soir 访谈）可引 |
| 宗教与演化立场 | 晚年趋向不可知论；坚定支持演化论、联署废除 Louisiana 科学教育法——可客观一句，避免宗教论战展开 |
| 荣誉年份链 | Francqui 1960、Gairdner 1967、Heineken 1973、Nobel 1974、NAS 外籍 1975、Harden 1978、E.B. Wilson 1989、子爵 1989（国王博杜安）、ForMemRS 1988——勿串 |
| 机构沿革 | 鲁汶天主教大学 1969 语言分裂→de Duve 选法语侧 UCL；ICP 1974 创立→1997 八十寿更名→2005 简称 de Duve Institute——沿革勿串 |
| 引语清单 | "more comical than heroic"（越狱）、"a sort of glorified PhD"（学位）、"word-coining mood"（造词）、Le Soir 两句（死亡观）——均 page.md 明载可引 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| lysosome | 溶酶体 | 1955 命名，酸性水解酶仓库 |
| peroxisome | 过氧化物酶体 | 1966 命名，过氧化物酶反应 |
| autophagy | 细胞自噬 | 其造词（1963），注意与 Ohsumi 篇呼应 |
| endocytosis / exocytosis | 胞吞/胞吐 | 同一occasion 所造 |
| glucagon | 胰高血糖素 | 再发现并定名（1951） |
| acid phosphatase | 酸性磷酸酶 | 溶酶体发现的示踪酶 |
| latent period | 潜伏期（酶活性） | 静置五天活性回升之谜 |
| microbody | 微体 | Bernhard/Rouillier 先行描述，de Duve 慎重不沿用 |
| beta cells / alpha cells | 胰岛 β/α 细胞 | 胰岛素/胰高血糖素来源 |
| de Duve Institute | de Duve 研究所 | 1974 创 ICP 演化而来 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**With Me**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：de Duve 的一生总有同行者——Theorell 与 Cori 夫妇的引路、Sutherland 的并肩解谜、Novikoff 的关键一瞥、Claude 的挚友情义、直到临终四名子女在场；With Me 的陪伴感对应这份"偶然从不独行"的生命观，也对应他把 autophagy（自我吞食）讲成细胞与己同在的诗意。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Christian_de_Duve/WithMe.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
