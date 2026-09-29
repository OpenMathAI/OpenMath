# 医学家立传提示词（Frank Macfarlane Burnet）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1960 年得主（与 Medawar 共享） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Frank Macfarlane Burnet（1899-09-03 生于维多利亚州 Traralgon ~ 1985-08-31 逝于 Port Fairy，享年 85 岁）
- **气质关键词**：**获得性免疫耐受的预言者、克隆选择理论的提出者、澳大利亚免疫学之父** —— 1960 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，与 Medawar 共享同一句）：
  > "for discovery of acquired immunological tolerance"
  > （因发现获得性免疫耐受）
- **设计母题**：**自我与非我的边界（self & non-self）**。克隆选择的扇形展开、被清除的自反应淋巴细胞——"免疫系统如何学会不上演手足相残"。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Frank_Macfarlane_Burnet/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Frank_Macfarlane_Burnet/page.md`；目录 `medic/presentations/20th_century/Frank_Macfarlane_Burnet/`；Makefile 改 `MAIN=Frank_Macfarlane_Burnet_zh`；肖像优先 images.txt 所列 Commons 图（1960 斯德哥尔摩照、与妻女合照等），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Frank_Macfarlane_Burnet.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | immunology | 免疫学 | 耐受/克隆选择/自身免疫，诺奖核心 | 免疫页 |
| 1 | virology | 病毒学 | Q 热/鹦鹉热/流感噬菌体 | 病毒页 |
| 2 | bacteriophage research | 噬菌体研究 | 溶原性先驱描述 | 早期页 |
| 3 | public health policy | 公共卫生政策 | 澳洲科学建制与 WHO 顾问 | 政策页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | John Charles Grant Ledingham | 师→本人 | 伦敦大学博士导师（1928，噬菌体） |
| influence | Charles Kellaway | 无向 | Hall 研究所所长，视其为最优秀青年并送其赴英 |
| influence | Henry Hallett Dale | 无向 | 伦敦国家医学研究所 fellowship 东家（1932-33） |
| collaborator | Frank Fenner | 无向 | 《抗体的产生》1949 再版合著者 |
| influence | Niels Kaj Jerne | 无向 | 自然选择假说为克隆选择理论前身 |
| colleague | E. H. Derrick | 无向 | Q 热合作研究（Coxiella burnetii 以其命名） |
| co-honored | Peter Medawar | 无向 | 1960 诺贝尔生理学或医学奖共享（获得性免疫耐受） |
| spouse | Edith Linda Marston Druce | 无向 | 1928 结婚，1973 因淋巴系白血病去世 |
| spouse | Hazel G. Jenkins | 无向 | 1976 结婚，微生物系图书馆员 |

> 对手方规范名：`Henry Hallett Dale` 沿用库内记录 id=3588；`Peter Medawar` 沿用库内记录 id=5868（本批 Medawar 篇 yaml 镜像）；其余按 page.md 形式新建 stub。

## 五、配色方案

- **气质**：澳州的孤高 + 理论家的冷峻直觉 + "独狼式"研究所掌门
- **主色**：桉树绿 `#4A6B3A`（澳大利亚丛林与免疫生态）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` 克隆选择 — 克隆金 `#C9A227`
  - `badgeB` 免疫耐受/自我非我 — 耐受蓝 `#2E6E9E`
  - `badgeC` 病毒学（Q 热/流感/噬菌体） — 病毒红 `#A63A2B`
  - `badgeD` 澳洲科学建制 — 桉树绿 `#4A6B3A`
- **背景母题**：低透明度克隆扇形树 + 自我/非我边界的盾形分界线。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 克隆选择理论与免疫耐受之父 / Frank Macfarlane Burnet 1899–1985 + badge + 右上头像 + 国籍行（Australia）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Traralgon、墨尔本 MD 1924、伦敦 PhD 1928、Hall 研究所所长 1944-65、诺奖 1960）
03  核心贡献概览 — 获得性免疫耐受假说 / 克隆选择 / 自我-非我概念 / 病毒学成就
04  "Mac" 的孤僻童年 (1899–1916) — 苏格兰移民银行经理之家七兄妹、长姐残疾的家庭阴影、甲虫收集与达尔文、Geelong College 全额奖学金
05  墨尔本与转折 (1918–1925) — 医学以避战、临床神经学志向被劝转实验室、伤寒凝集反应首篇论文、MD 考试遥遥领先
06  伦敦与噬菌体 (1925–1928) — 搭船做船医抵英、Lister 研究所、Beit Fellowship、Ledingham 门下 PhD 1928、溶原性先驱假说（与 McKie 1929，迟至多年后被接受，奠定 Delbrück/Hershey/Luria 1969 诺奖的工作基础）
07  Bundaberg 悲剧与免疫学起点 — 12 名儿童死于污染白喉疫苗、查明金葡菌污染、毒素-抗毒素兴趣转向
08  黄金岁月：病毒学 (1932–1944) — 伦敦 NIMR（Dale 东家）流感病毒分离传代、鸡胚测定法、Q 热（Coxiella burnetii 以其命名）与鹦鹉热、Dora Lush 感染殉职的悲剧、流感疫苗试验失败（两万人）仍获国际声誉
09  掌舵 Hall 研究所 (1944–1965) — 拒哈佛讲席回澳、"黄金时代的病毒学"、1957 单方面转向免疫学、孤狼式管理与批评
10  1949：自我-非我与耐受假说（核心页）—《抗体的产生》（与 Fenner 合著）引入 self/non-self；胚胎期植入异源细胞将不产生抗体的预言；"无法自证实验"
11  Medawar 的实验证明与 1960 诺奖 — Medawar/Billingham/Brent 1953 脾细胞宫内注入实验证实；两人性格迥异（寡言 vs 圆融）却相互敬重；官方理由全句
12  克隆选择（核心页二）— 扩展 Jerne 自然选择假说；1958 Nossal+Lederberg 一个 B 细胞一种抗体；1959 专著；Talmage 优先权争议注记；Lederberg 1959 中枢耐受修正其假说
13  公共政策与争议（客观一页）— 首位澳大利亚年度人物 1960、AAS 主席 1965-69、WHO 专家小组；降级的分子生物学论战（Genes, Dreams and Realities）与 Endurance of Life 争议、生物武器建议档案——仅 page.md 实载，克制呈现
14  晚年与身后 — 两任妻子；1978 退休又著 16 部；1985-08-31 逝于 Port Fairy（结直肠癌）、国葬；Burnet 研究所更名、Macfarlane Burnet 奖章
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 1960 两人共享同一句理由；分工：Burnet=理论预言（假说）、Medawar=实验证明——Burnet 自述"my part was a very minor one—it was the formulation of an hypothesis"（英文原句可引） |
| 理论归属链 | 克隆选择：Ehrlich 侧源→Jerne 自然选择假说→Burnet 扩展；Talmage 同期论文优先权争议 + Lederberg 的遗传学概念化——"Burnet's clonal selection theory"之名掩盖了多人贡献，页面明载须注记 |
| 假说被修正 | 后续研究表明胚胎期移植亦可被排斥；Lederberg 1959 提出"淋巴细胞年龄"决定耐受（中枢耐受）——Burnet 原假说解释被取代，诚实呈现 |
| 生物武器建议 | 解密档案显示其 1947-52 曾建议澳洲发展针对东南亚"人口过剩"国家的生化武器——涉政治敏感，立传**不展开**，仅陷阱表留存 |
| 争议言论 | Endurance of Life 的安乐死/淘汰主张引发与希特勒类比的风暴、Genes Dreams 攻击分子生物学——page.md 有载但争议性强，立传以一句客观带过或不写 |
| 政治立场 | 反核/反烟草/批评越战/支持 Whitlam 等——**政治敏感一律禁写**，仅限科学政策语境 |
| 实验室群像 | Isaacs/Ada/Cairns/Fazekas/Fenner 等门下群星仅 Fenner 入库（合著明载）；McKie（溶原性合著）与 Holmes（NZ 黑鼠）不入库；Dora Lush 殉职作叙事细节不入库 |
| Nossal 关系 | Nossal 系其继任者且 1958 实验在其所内完成，但 page.md 未明写师生关系——不入库 |
| 两任妻子 | Edith Druce（1928 结婚，1973 白血病去世，一子二女）；Hazel Jenkins（1976 结婚，寡居歌手出身的图书馆员）——双 spouse 行 |
| 引语红线 | 可引：tolerance 假说英文原句、"very minor one"自评、"an effort to believe what common sense tells you isn't true"（宗教观）；其余转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| acquired immunological tolerance | 获得性免疫耐受 | 1960 诺奖理由 |
| clonal selection | 克隆选择 | Burnet 命名并扩展 Jerne |
| self / non-self | 自我/非我 | Burnet 引入免疫学的概念 |
| lysogeny | 溶原性 | 1929 与 McKie 先驱描述 |
| Coxiella burnetii | 伯内特柯克斯体 | Q 热病原，以其命名 |
| hemagglutination assay | 血凝测定 | 流感研究技术 |
| graft-versus-host | 移植物抗宿主反应 | 与 Simonsen 合作系统 |
| immunological surveillance | 免疫监视 | 晚年理论方向 |

## 九、背景音乐选择

- **选定曲目**：**PAST** — Alex-Productions（manifest 预分配）
- **匹配理由**："历史感/深沉"贴合其跨越两次大战、从噬菌体到免疫学理论的世纪纵深；理论家孤身在澳洲远离欧美中心的执守，需要沉稳而略带孤寂的曲式承载。
- **本地路径**：music_audio/ 下 Alex-Productions PAST 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
