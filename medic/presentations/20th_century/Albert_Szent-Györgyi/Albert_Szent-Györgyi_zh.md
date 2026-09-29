# 医学家立传提示词（Albert Szent-Györgyi）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Albert Szent-Györgyi（1937 年诺贝尔生理学或医学奖得主，匈牙利）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Albert_Szent-Györgyi/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Albert Imre Szent-Györgyi de Nagyrápolt（阿尔伯特·圣捷尔吉，1893-09-16 布达佩斯 ~ 1986-10-22 美国马萨诸塞州伍兹霍尔，享年 93 岁）
- **气质关键词**：**维生素 C 的分离者、柠檬酸循环组分的先行者、从辣椒里拧出抗坏血酸的「快乐的匈牙利人」** —— 1937 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json）：
  > "for his discoveries in connection with the biological combustion processes , with special reference to vitamin C and the catalysis of fumaric acid"
  > （因其关于生物燃烧过程的发现，特别是维生素 C 与延胡索酸的催化）
- **设计母题**：**「一枚辣椒的化学」**。塞格德市场买来的青椒被拧出抗坏血酸——视觉隐喻：辣椒剖面与分子六元环并置，热力学「燃烧」火苗作底纹。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Albert_Szent-Györgyi/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Albert_Szent-Györgyi/`，成目录 `medic/presentations/20th_century/Albert_Szent-Györgyi/`，Makefile 复制后设 `MAIN=Albert_Szent-Györgyi_zh`、`VIDEO_NAME=Albert_Szent-Györgyi_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库：本人复用库内既有记录 id=3316（yaml seed 幂等回填 QID Q180468），已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 细胞呼吸/生物氧化主线，1937 诺奖核心 | 总览页 |
| 1 | vitamin research | 维生素研究 | 分离「六碳酸」并证其为维生素 C（抗坏血酸） | 维生素 C 页 |
| 2 | cellular respiration | 细胞呼吸 | 鉴定延胡索酸等柠檬酸（Krebs）循环组分 | 循环页 |
| 3 | muscle physiology | 肌肉生理学 | 肌动蛋白-肌球蛋白-ATP 收缩机制与伍兹霍尔肌肉研究所 | 肌肉页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Albert_Szent-Györgyi.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Frederick Gowland Hopkins | 师 | 剑桥博士导师（infobox 载），1929 年获 PhD |
| collaborator | Joseph Svirbely | — | 塞格德研究同侪，共证六碳酸为维生素 C |
| collaborator | Zoltán Bay | — | 塞格德相识，生物物理研究伙伴 |
| spouse | Kornélia Demény | — | 1917 年成婚，1941 年离异 |
| spouse | Márta Borbíró | — | 1941 年成婚，1963 年病逝 |
| spouse | June Susan Wichterman | — | 1965 年成婚，1968 年离异 |
| spouse | Marcia Houston | — | 1975 年成婚 |
| parent-child | Cornelia Szent-Györgyi | 女 | 1918 年生，1969 年卒 |
| parent-child | Lola von Szent-Györgyi | 养女 | — |
| parent-child | Miklós Szent-Györgyi | 父 | 特兰西瓦尼亚地主 |
| parent-child | Jozefina Lenhossék | 母 | 解剖学世家之女 |

> 说明：本人记录复用库内 id=3316（QID 回填 Q180468），无分裂。Hopkins 用 infobox 口径（frontmatter 的 Hartog Jacob Hamburger 与 infobox 冲突，沿 Urey/Genzel 先例取 infobox，已标注待 Review 核）。★ 跨批协作现状：Hopkins 的 advisor-student 边已由 Hopkins 所在批次先建（库内 10046，本批同键边幂等跳过、不重复）；Haworth 的 colleague 边（提供维生素 C 参考样品并共同命名 ascorbic acid）已由化学侧建边（库内 8018）——本篇不再重复建边，正文可照常叙述两者关系。其余不入库者：Stephen Rath（赞助商人）、Franklin Salisbury（基金会律师）、Ralph Moss（门生兼传记作者，仅 bibliography 提及）；兄 Pál（小提琴家）无兄弟关系类型不入库；舅公辈 Mihály Lenhossék 等解剖学家族不入库。

## 五、配色方案 【人物专属】

- **气质**： Hungarian 热情、直觉型的「酒神型」科学家、永不熄灭的好奇
- **主色**：辣椒橙红 `#B0521E`（塞格德市场的那枚青椒）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 生物化学 — 燃烧火橙 `#C25B2E`
  - `badgeB` 维生素研究 — 抗坏血酸黄绿 `#8FA82E`
  - `badgeC` 细胞呼吸 — 循环青 `#2E7A6E`
  - `badgeD` 肌肉生理学 — 肌纤维红 `#A83A4A`
- **背景母题**：辣椒剖面弧线与分子六元环交叠、稀疏「生物燃烧」小火苗，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 从辣椒到生命之火 / Albert Szent-Györgyi 1893–1986 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、贵族纹章、四段婚姻、荣誉、核心领域）
03  核心贡献概览 — 维生素 C / 细胞呼吸与循环组分 / 肌肉收缩 / 癌与自由基的晚年转向
04  布达佩斯与一战 (1893–1917) — 解剖学世家、1914 从军医、1916 自伤避战归家、1917 M.D. 并成婚
05  漂泊的求学期 (1917–1930) — 布拉迪斯拉发起步、格罗宁根细胞呼吸、洛克菲勒奖学金入剑桥
06  剑桥 PhD (1929) — Hopkins 门下、肾上腺组织「六碳酸」（hexuronic acid）的分离
07  塞格德：维生素 C 的确证 (1930–1937)（核心页）— Svirbely 生物测定、辣椒来源、Haworth 定结构命名 L-抗坏血酸
08  延胡索酸与循环的拼图 — 生物燃烧过程、Krebs 循环前身组分的鉴定
09  1937 诺贝尔奖（核心页）— citation 原文、1940 年诺奖奖金全部捐予芬兰（冬季战争语境一句）
10  肌肉里的引擎 (1938–1947) — 肌动蛋白+肌球蛋白+ATP、伍兹霍尔肌肉研究所 (1947)
11  乱世孤旅 — 帮犹太友人出逃、参加抵抗运动、1944 伊斯坦布尔密使、希特勒通缉令与盖世太保追捕、战后被提名总统传闻、1947 移美
12  晚年转向：电子与癌 — 量子生物学构想、自由基、NFCR 的创立（1971 访谈引出）、syntropy 提法 (1974)
13  科学观 — Apollonian vs Dionysian 两分、发现定义引语（英文原文+译文）、对拨款制度的批评
14  遗产 — Lasker 1954 · NAS 1956 · Google Doodle 2011；抗氧化/红ox 信号的前驱
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文（biological combustion processes + vitamin C + catalysis of fumaric acid 三要素）；page.md 正文引用句无 "special reference" 的 the——以 json 版本为准 |
| 2 | 维生素 C 归属链 | Szent-Györgyi 分离「六碳酸」并（与 Svirbely）证其为抗坏血酸因子；Haworth 测定结构并命名 L-ascorbic acid——「分离/确证」与「定结构/命名」两段功劳勿混 |
| 3 | 博士导师冲突 | frontmatter doctoral_advisor=Hartog Jacob Hamburger vs infobox=Frederick Gowland Hopkins（剑桥 1929 PhD）——取 infobox 口径入库并在 yaml note 标注，Review 时复核 |
| 4 | 生卒 | 1893-09-16 / 1986-10-22（frontmatter 有 10-21 噪声，正文/infobox 均为 10-22）；1911 入塞梅尔维斯大学，1917 获 M.D. |
| 5 | 四段婚姻 | Kornélia/Cornelia 两拼写并存（infobox vs 正文）——yaml 用 infobox 的 Kornélia Demény；June Wichterman 时年 25 岁、是伍兹霍尔生物学家 Ralph Wichterman 之女；Marcia Houston 收养 Lola——四段均建 spouse 边 |
| 6 | 政治叙事 | 帮犹太友人出逃、参加抵抗运动、1944 密使伊斯坦布尔、盖世太保通缉、1967 越战抗税、世界宪法大会——均 page.md 明载；以克制史实口径集中在「乱世孤旅」一帧，一句带过不渲染，不建任何政治人物关系边 |
| 7 | 引语红线 | "a discovery must be, by definition, at variance with existing knowledge" 与 Apollonian/Dionysian 段有英文原文可引；Weismann 式自传感言本篇无；禁编造「辣椒灵感」类口头禅 |
| 8 | 奖金去向 | 1940 年诺奖奖金全数提供给芬兰（苏芬冬季战争语境）——page.md 明载可写，政治背景一句带过 |
| 9 | Krebs 循环措辞 | 其鉴定的是延胡索酸等组分，循环完成后才以 Krebs 命名——勿写成「发现 Krebs 循环」 |
| 10 | metadata 冲突 | nationalities frontmatter 有 Hungary+United States 两值——yaml 按 Nobel 官方口径只填 Hungary，美国籍（1955）在正文叙述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| hexuronic acid | 「六碳酸」（早期命名） | 后被确认为维生素 C |
| L-ascorbic acid | L-抗坏血酸 | Haworth 定结构后命名 |
| antiscorbutic factor | 抗坏血病因子 | 维生素 C 的功能名 |
| citric acid cycle / Krebs cycle | 柠檬酸循环 / Krebs 循环 | 同物两名 |
| fumaric acid | 延胡索酸 | 诺奖理由要素 |
| biological combustion | 生物燃烧（氧化） | 诺奖理由核心词 |
| actin / myosin / ATP | 肌动蛋白 / 肌球蛋白 / 三磷酸腺苷 | 收缩三要素 |
| glycerol storage | 甘油冷贮法 | 伍兹霍尔技术成果 |
| syntropy | 「合熵」（其新造词） | 替代 negentropy 的提议 |
| Apollonian / Dionysian | 日神型 / 酒神型科学家 | 其科学观二分 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Lonesome** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「孤独的自由灵魂」匹配其底色——战壕里自伤归乡的学生、乱世中的孤身密使、拒写刻板标书的倔强老头，始终与主流保持一步距离
  - 幽缓曲式也贴合其晚年「孤独先行者」的量子生物学远景：同时代的同行多半跟不上他
- **备选**（未采用）：Tragedy（本批 Murphy 已用）、New Lands（开拓感贴切但物理侧高频占用）
- **本地路径**：按 music_audio/ 内 Alex-Productions Lonesome 曲目复制至 `medic/presentations/20th_century/Albert_Szent-Györgyi/Lonesome.wav`，ffmpeg `-shortest` 对齐
