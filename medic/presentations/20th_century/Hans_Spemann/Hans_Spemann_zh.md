# 医学家立传提示词（Hans Spemann）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Hans Spemann（1935 年诺贝尔生理学或医学奖得主，德国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Hans_Spemann/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Hans Spemann（汉斯·施佩曼，1869-06-27 斯图加特 ~ 1941-09-12 弗莱堡，享年 72 岁）
- **气质关键词**：**实验胚胎学之父、组织者（Organiser）的发现者、显微外科的祖师** —— 1935 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json；注意本条 citation 为叙述长句，见第七节陷阱 1）：
  > "was awarded a Nobel Prize in Physiology or Medicine in 1935 for his student Hilde Mangold 's discovery of the effect now known as embryonic induction , an influence, exercised by various parts of the embryo , that directs the development of groups of cells into particular tissues and organs, the start of artificial cloning of organisms. Spemann added his name as an author to Hilde Mangold's dissertation (although she objected)."
  > （因胚胎诱导效应——胚胎各部分行使的影响，引导细胞群发育为特定组织与器官，人工克隆生物的起点；该效应由其学生希尔德·曼戈尔德发现）
- **设计母题**：**「一块移植的胚孔」**。把一枚原结（primitive knot）移植到另一胚胎，便指挥出第二套体轴——视觉隐喻：两枚重叠的胚胎轮廓与从一点辐射的诱导波纹。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Hans_Spemann/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Hans_Spemann/`，成目录 `medic/presentations/20th_century/Hans_Spemann/`，Makefile 复制后设 `MAIN=Hans_Spemann_zh`、`VIDEO_NAME=Hans_Spemann_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | embryology | 胚胎学 | 胚胎诱导与组织者，1935 诺奖核心 | 诱导页 |
| 1 | developmental biology | 发育生物学 | 形态发生场、整体论进路 | 场论页 |
| 2 | zoology | 动物学 | 罗斯托克/弗莱堡动物学教授 | 生涯页 |
| 3 | microsurgery | 显微外科 | 婴发结扎环分切细胞，被誉为显微外科真正创始人 | 技法页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Hans_Spemann.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Theodor Boveri | 师 | 维尔茨堡博士导师，寄生线虫细胞谱系论文 |
| advisor-student | Hilde Mangold | 生 | 弗莱堡博士生，1924 组织者实验完成人 |
| controversy | Hilde Mangold | — | 诺奖成果署名争议，其 dissertation 被添名且本人反对 |
| advisor-student | Otto Mangold | 生 | 最早的门生之一，1937 年接替其弗莱堡教席 |
| influence | August Weismann | — | 结核疗养期间读其种质论，转向实验胚胎学 |
| influence | Warren Harmon Lewis | — | 移植实验借鉴其近期工作 |
| influence | Ethel Browne Harvey | — | 移植实验借鉴其近期工作 |
| influence | Paul Alfred Weiss | — | 形态发生场概念受其启发 |
| influence | Julius von Sachs | — | 维尔茨堡求学期间受教 |
| influence | Wilhelm Conrad Röntgen | — | 维尔茨堡求学期间受教 |
| spouse | Klara Binder | — | 1892 年成婚 |
| parent-child | Wilhelm Spemann | 父 | 出版商 |
| parent-child | Lisinka Hoffman | 母 | — |

> 说明：Röntgen 对手方用库内规范名 Wilhelm Conrad Röntgen（id 1057）；Paul Alfred Weiss 用全名新建 stub，避开库内身份不明的 Paul Weiss(853)；四名子女仅以名字提及（Margaret/Fritz/Rudolph/Ulrich，无姓氏叙事）不入库防造名；Hans Driesch/Wilhelm Roux/Oscar Hertwig/T.H.Morgan 为领域史背景人物（Roux-Driesch 实验之争）、Holtfreter/Needham 夫妇/Waddington 为后续证伪者，均无个人交往明载，不入库；Gustav Wolff 仅「相识」，其蝶螈晶体再生实验与本篇工作平行，不入库。

## 五、配色方案 【人物专属】

- **气质**：微观手术的极简克制、德意志学统、整体论的暗流
- **主色**：胚轴青绿 `#245C4C`（两栖类胚胎的冷调）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 胚胎学 — 诱导紫 `#5B4E8E`
  - `badgeB` 发育生物学 — 场论青 `#1F7A6D`
  - `badgeC` 动物学 — 蝶螈褐 `#7A5230`
  - `badgeD` 显微外科 — 发丝银灰 `#8A8F98`
- **背景母题**：两枚半透明胚胎剪影错位叠加 + 发丝环弧线（其分切器械），低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 实验胚胎学之父 / Hans Spemann 1869–1941 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、教育、任职、家庭、荣誉、核心领域）
03  核心贡献概览 — 胚胎诱导 / 组织者 / 显微分切 / 核移植先声
04  早年斯图加特 (1869–1891) — 出版商长子、从商从军卖书、1891 入海德堡学医
05  维尔茨堡：Boveri 门下 (1893–1908) — 1895 学位、寄生线虫细胞谱系博士论文、中耳发育教职论文
06  发丝环与半个胚胎 — 婴发结扎环分切两栖类卵、分裂平面决定命运、破预成论
07  罗斯托克与凯撒威廉研究所 (1908–1919) — 1908 教授、1914 达勒姆副所长
08  组织者实验 (1924)（核心页）— Hilde Mangold 的胚孔移植、次级胚体诱导、organiser 命名
09  1935 诺贝尔奖（核心页）— citation 叙述长句、1935-12-12 诺奖演讲 The Organizer-Effect in Embryonic Development
10  Mangold 之争 — 署名添列与她本人的反对；1923 意外身亡与 1924 全文发表；Spemann-Mangold organizer 命名
11  1928：体细胞核移植先声 — 两栖类胚核转移，克隆技术的最早一步
12  学说的黄昏 — 活力论场分析的坚持；煮沸/冻死组织者仍可诱导 → 分子信号的最终裁定
13  门生与传承 — Otto Mangold 接席；1925 NAS 外籍院士、1933 AAAS、1937 美国哲学学会
14  遗产：从组织者到发育生物学 — Embryonic Development and Induction (1938)；诱导基因与克隆史前史
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | citation 特殊性 | 本批 nobel_medicine_citations.json 的 1935 条目是叙述长句（含 Mangold 归属与署名争议），须逐字引用；官方短句 "for his discovery of the organiser effect in embryonic development" 仅可在陷阱页作对照说明，幻灯片主理由以 json 文本为准 |
| 2 | 死亡日期双值 | infobox 1941-09-09 vs 正文 1941-09-12（heart failure）——取正文 1941-09-12，yaml 已按此填写 |
| 3 | Mangold 归属 | 诺奖成果（组织者效应）是学生 Hilde Mangold 的发现——行文必须保留这一归属；她 1923 年（实验后）死于爆炸意外、1924 年论文全文发表，年份勿错置 |
| 4 | 署名争议 | Spemann 在她反对的情况下把名字添列论文作者——如实记载（controversy 边），既不美化也不加贬斥定性 |
| 5 | 纳粹关联 | 1923 弗莱堡 Schlageter 纪念活动带队献花圈、1935 诺奖演说结尾行纳粹礼——page.md 明载，须以克制史实口径在「争议与暗面」帧如实记载，不渲染不辩护，不建任何人物关系边 |
| 6 | 「克隆起点」 | 1928 两栖类体细胞核移植是「最早的步骤之一」（one of the first moves）——勿写成「克隆之父」 |
| 7 | 引语红线 | 自传中读 Weismann 种质论的感言有英文原文可引；其余叙事无直接引语，禁编造 |
| 8 | 求学三师 | 1895 学位「followed study under Boveri, Sachs and Röntgen」——Boveri 是博士导师（正文+infobox 双载），Sachs/Röntgen 仅求学受教，建 influence 不建师生边 |
| 9 | 全职衔链 | Heidelberg 医学预考（1893）→ München 临床（1893-94）→ Würzburg 动物所（至 1908）→ Rostock 教授（1908）→ KWI Dahlem 副所长（1914）→ Freiburg 教授（1919），勿错置 |
| 10 | metadata 冲突 | frontmatter 与 infobox 一致（Boveri 导师）；仅死亡日双值见陷阱 2 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| embryonic induction | 胚胎诱导 | 诺奖核心概念 |
| organiser / organizer centre | 组织者（组织中心） | 德文 Organisator，两拼写并存 |
| primitive knot | 原结 | 移植取材部位 |
| gastrula | 原肠胚 | 移植实验的胚胎期 |
| blastomere | 卵裂球 | Roux/Driesch 之争语境 |
| morphogenetic field | 形态发生场 | 概念源自 Weiss |
| epigenesis vs preformation | 渐成论 vs 预成论 | 分切实验解决的百年之争 |
| somatic cell nuclear transfer | 体细胞核移植 | 1928 年先声，勿写成现代克隆 |
| Spemann-Mangold organizer | 施佩曼-曼戈尔德组织者 | 双人命名，勿只写 Spemann |
| vitalism | 活力论 | 其晚年立场，如实记载 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**With Me** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「同行」气质双关：与发丝环相伴一生的显微手艺，以及组织者发现中学生 Mangold 的必要在场——本篇叙事绕不开「成果与人共享」的伦理张力
  - 温和内敛的曲风压得住署名争议帧的沉重，不喧宾夺主
- **备选**（未采用）：Tragedy（本批 Murphy 已用）、Lonesome（本批 Szent-Györgyi 已用，且其晚年学术孤旅意象偏弱）
- **本地路径**：按 music_audio/ 内 Alex-Productions With Me 曲目复制至 `medic/presentations/20th_century/Hans_Spemann/With_Me.wav`，ffmpeg `-shortest` 对齐
