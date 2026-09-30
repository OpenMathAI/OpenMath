# 经济学家立传提示词（Oliver Hart）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2016 年得主 Oliver Hart（奥利弗·哈特）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Oliver_Hart_economist/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Sir Oliver Simon D'Arcy Hart（1948-10-09 生于英国伦敦，在世，卒年留白）
- **气质关键词**：**不完全契约的开创者、产权理论的奠基人、从伦敦到哈佛的契约经济学家**
- **诺奖获奖理由**（2016 与 Bengt Holmström 共享，逐字引自 manifest / `economics/nobel_economics_citations.json`）：
  > "for their contributions to contract theory"（表彰他们对契约理论的贡献）
- **设计母题**：**不完全契约与产权边界（incomplete contracts & ownership）**——契约永远写不完所有或然状态，剩余控制权必须落到"拥有者"手中；以残缺的契约文书边角与栅格边界构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Oliver_Hart_economist/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Oliver_Hart_economist/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Oliver_Hart_economist_zh`、`VIDEO_NAME=Oliver_Hart_economist_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Hart 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | contract theory | 契约理论 | 2016 诺奖核心（与 Holmström 共享） | 封面、核心页 |
| 1 | incomplete contracts | 不完全契约 | 契约无法覆盖所有或然状态的核心思想 | 核心页 |
| 2 | theory of the firm | 企业理论 | 产权/所有权配置与企业边界 | 产权页 |
| 3 | corporate finance | 公司金融 | infobox Fields 明载 | 应用页 |
| 4 | law and economics | 法与经济学 | infobox Fields 明载；曾任美国法与经济学会会长 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 12 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Michael Rothschild | Rothschild → 导师 | Princeton 博士导师（1974），论文 Essays in the economics of uncertainty |
| co-honored | Bengt Holmström | 无向 | 2016 诺贝尔经济学奖共享（契约理论贡献） |
| spouse | Rita B. Goldberg | 无向 | 妻，哈佛文学教授 |
| parent-child | Philip D'Arcy Hart | Hart → 子 | 父，医学研究者 |
| collaborator | Sanford J. Grossman | 无向 | 合著四篇（1980/1983/1986/1988）含 The Costs and Benefits of Ownership |
| collaborator | John Hardman Moore | 无向 | 合著四篇（1988/1990/1994/2008）含 Property Rights and the Nature of the Firm |
| collaborator | Andrei Shleifer | 无向 | 合著 The Proper Scope of Government（1997） |
| collaborator | Robert W. Vishny | 无向 | 同上（1997，与 Shleifer 三人合著） |
| advisor-student | David S. Scharfstein | Hart → 学生 | 博士生（infobox 明载） |
| advisor-student | Jeremy C. Stein | Hart → 学生 | 博士生（infobox 明载） |
| advisor-student | Luigi Zingales | Hart → 学生 | 博士生（infobox 明载） |
| advisor-student | Richard Holden | Hart → 学生 | 博士生（infobox 明载） |

**不入库但提示词可叙述**：母 Ruth Meyer（妇科医生，无维基链接不建边）；曾外祖父 Samuel Montagu（第一代 Swaythling 男爵，隔代不入）；二子 Daniel 与 Benjamin（仅具名不入库）；Mervyn King（同窗叙述，非持续关系）；2023 年封爵（Knight Bachelor，荣誉非关系）。

## 五、配色方案 【人物专属】

- **气质**：严谨、结构化、契约文书的秩序与边界感
- **主色**：`#7E1E23`（契约深红——manifest 预分配，与 Holmström 篇同色呼应 2016 共享）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeInc` 不完全契约 — 深红 `#7E1E23`
  - `badgeProp` 产权与企业 — 靛蓝 `#37474F`
  - `badgeFin` 公司金融 — 深蓝 `#16324F`
  - `badgeLaw` 法与经济学 — 琥珀 `#C07A2A`
- **背景母题**：残缺的契约边角 + 栅格边界线（剩余控制权的归属），呼应「契约写不全，所以产权重要」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 不完全契约的开创者 / Sir Oliver Hart 1948– + 四色 badge + 右上头像 + 国籍行
    （United Kingdom / United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地伦敦、教育 Cambridge BA 1969 /
    Warwick MA 1972 / Princeton PhD 1974、师承 Michael Rothschild、任职 Harvard、诺奖 2016、
    2023 封爵、核心领域）
03  核心贡献概览 — 不完全契约 / 产权与企业理论 / 公司金融 / 法与经济学
04  早年与教育 (1948–1974) — 伦敦出生、犹太家庭（Montagu 家族）、Cambridge 数学 BA 1969、
    Warwick 经济学 MA 1972、Princeton PhD 1974
05  Princeton 博士：Rothschild 门下 (1974) — 论文 Essays in the economics of uncertainty
06  英国任教岁月 — Essex 讲师、Churchill College fellow、LSE 教授；1984 返美
07  MIT 与哈佛 (1984– ) — MIT 任教、1993 起哈佛、1997 首任 Andrew E. Furer 讲席教授、
    2000–03 经济系主任
08  不完全契约（核心贡献页）— 契约不可能覆盖每一或然状态：contractual incompleteness 的含义与后果
09  产权与企业理论（核心贡献页，与 Grossman/Moore）— Grossman–Hart–Moore 产权方法：
    The Costs and Benefits of Ownership (1986)、Property Rights and the Nature of the Firm (1990)
10  契约作为参照点 — Incomplete Contracts and Renegotiation (1988)、Contracts as Reference
    Points (2008)、人力资本不可让渡的债务理论 (1994)
11  从理论到法庭与政策 — Black and Decker / Wells Fargo 税务案政府专家：控制权保留决定税收利益
12  门生与传承 — Scharfstein / Stein / Zingales / Holden 四位博士生
13  荣誉与认可 — Nobel 2016 · Guggenheim · NAS 院士 · 英国科学院 corresponding fellow ·
    美国法与经济学会会长 · AEA 副会长 · 2023 生日授勋封爵（Knight Bachelor）·
    诺奖演讲 Incomplete Contracts and Control
14  遗产与结尾 — 不完全契约理论从企业理论到规制政策的现代格局 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 目录名与规范名 | 目录/yaml 文件名用 `Oliver_Hart_economist`（消歧义后缀），name_en 用 manifest 形式 `Oliver Hart`（label 无消歧义后缀）；全名 Oliver Simon D'Arcy Hart，姓氏属 D'Arcy Hart 双桶姓但通行称 Hart（page.md 注释明载） |
| 国籍口径 | British-American / 持英美双重国籍（page.md Personal life 明载）；manifest country=United Kingdom / United States 拆两条入库 |
| 获奖共享表述 | 2016 与 Holmström 共享，理由同一句；Hart 一侧的侧重点是"所有权应如何配置、何时契约优于所有权"（page.md 获奖段明载） |
| 封爵年份 | 2023 Birthday Honours 封 Knight Bachelor（服务经济理论）；Sir 头衔勿写成"获诺贝尔奖后立即封爵"或误写年份 |
| 三位合著者分工 | Grossman（1980/1983/1986/1988 四篇）、Moore（1988/1990/1994/2008 四篇）、Shleifer+Vishny（1997 一篇三人合著）——篇目年份勿互串 |
| 博士生口径 | infobox "See list" 后列四人（Scharfstein/Stein/Zingales/Holden），全部入库；勿把合著者当学生 |
| 家族关系 | 父 Philip D'Arcy Hart 是医学研究者（parent-child 入库）；母 Ruth Meyer 无维基链接仅叙述；曾外祖父 Samuel Montagu 隔代不入库 |
| 妻子身份 | Rita B. Goldberg 是哈佛文学教授、Holocaust 二代回忆录 Motherland 作者——身份可叙述，入 spouse 边 |
| 政治内容红线 | page.md Political views 节（2024 年 16 位诺奖得主公开信涉美国政治人物）一律不写入幻灯片与提示词叙事，不入库任何关系 |
| metadata 噪声 | metadata.json 与 page.md 无实质冲突；frontmatter nationality 顺序 (US, UK) 与 Nobel 口径 (UK/US) 不一致时以 manifest/page.md 的 UK 在前为准 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| contract theory | 契约理论 | 获奖理由核心词 |
| incomplete contracts | 不完全契约 | 核心概念，勿写成"非完备合同" |
| property rights | 产权 | Grossman–Hart–Moore 框架核心 |
| residual control rights | 剩余控制权 | 所有权的理论基础 |
| theory of the firm | 企业理论 | 与 Coase 传统相接 |
| ownership | 所有权/所有者配置 | 2016 获奖工作侧重点 |
| renegotiation | 再谈判 | 1988 与 Moore 合著主题 |
| Knight Bachelor | 下级勋位爵士 | 2023 封爵类别，勿写成"骑士勋章" |
| law and economics | 法与经济学 | 学会会长身份对应领域 |
| integrated assessment | （非本篇术语） | 勿与 Nordhaus 的 IAM 混淆 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Invisible Light**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：不完全契约研究的是"写不进契约的那部分"——看不见的或然状态决定看得见的产权安排；"不可见之光"隐喻契约文本之外的剩余控制权。与 Holmström 篇同曲，呼应 2016 共享得主的双人叙事。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `economics/presentations/21th_century/Oliver_Hart_economist/TheInvisibleLight.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/21th_century/Oliver_Hart_economist/page.md` | ★ 唯一事实基准 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `economics/presentations/cover/` | OpenEcon 统一首页模板 |
| `MySQL/data/Oliver_Hart_economist.yaml` | 入库 yaml（已执行） |
| `economics/nobel_economics_citations.json` | 获奖理由英文原文 |

## 十一、执行清单 【模板通用】

1. 读本提示词 + page.md 建立事实基准；2. 下载肖像（250px 改 500px，Commons 404 则装饰圆占位）；3. 复制 Makefile 设 `MAIN=Oliver_Hart_economist_zh`；4. 按 §六写 15 页 Beamer；5. `make distclean && make` 编译循环（0 error、vbox≤10pt、hbox≤50pt）；6. pdftoppm 逐页目检；7. 两轮 Review；8. DB `has_biography` 置 1。

## 十二、版式补遗 【模板通用】

- 表格页安全负间距：顶部 -0.35cm、arraystretch 0.78-0.82；公式框前 -0.35~-0.55cm。
- 时间线 `\foreach` 分隔符必须 ASCII 逗号；文本模式希腊字母须数学模式；宏名禁数字。
- 引语框：仅诺奖 citation 原句（英中对照）；半角引号；品牌口径 `OpenMathAI`。
- 国籍徽章写 `United Kingdom / United States`（双国籍）。
