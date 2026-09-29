# 医学家立传提示词（Georg von Békésy）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1961 年得主（独得） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Georg von Békésy（Békésy György，1899-06-03 生于布达佩斯 ~ 1972-06-13 逝于檀香山，享年 73 岁）
- **气质关键词**：**耳蜗行波的发现者、以频闪摄影解剖听觉之谜的物理学家、亚洲艺术收藏家** —— 1961 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，独享）：
  > "for his discoveries of the physical mechanism of stimulation within the cochlea"
  > （因其发现耳蜗内受激的物理机制）
- **设计母题**：**耳蜗行波（the traveling wave）**。频闪摄影下的基底膜波动、沿蜗牛壳盘旋的频率地形图——"声音在螺旋里画出地形"。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Georg_von_Békésy/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Georg_von_Békésy/page.md`；目录 `medic/presentations/20th_century/Georg_von_Békésy/`；Makefile 改 `MAIN=Georg_von_Bekesy_zh`（tex 文件名 ASCII 化）；肖像优先 images.txt 所列 Commons 图（Békésy in 1961、1918 年轻照），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Georg_von_Békésy.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biophysics | 生物物理学 | 职业主领域（infobox Fields） | 封面 |
| 1 | auditory physiology | 听觉生理学 | 耳蜗/基底膜/行波，诺奖核心 | 核心页 |
| 2 | sensory physics | 感觉物理学 | 频闪摄影与银粒标记观测方法 | 方法页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Sándor Békésy | 父→本人 | 父，经济外交官（1860-1923） |

> 对手方规范名：仅 1 条关系（Finsen relations=2 之前的最薄诚实值）。**relations=1 为诚实值**——page.md 无导师/门生/配偶记载；Róbert Bárány 仅载"邀其赴乌普萨拉任职被婉拒"（job offer 非学术关系，裁定不入库）；兄 Miklós（农业生物学家）不入库。立传时勿虚构补边。

## 五、配色方案

- **气质**：奥匈帝国的旧式优雅 + 邮政局工程师的务实 + 檀香山的收藏家晚年
- **主色**：耳蜗铜金 `#8C5A2B`（蜗壳螺纹与银粒标记的金属色）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` 行波与基底膜 — 波动蓝 `#2E6E9E`
  - `badgeB` 频率地形（tonotopy） — 频谱青 `#2E7D8C`
  - `badgeC` 电信工程出身 — 工程灰 `#3A4A6B`
  - `badgeD` 亚洲艺术收藏 — 收藏金 `#C9A227`
- **背景母题**：低透明度螺旋（蜗壳）轮廓 + 沿螺旋渐变的波峰曲线。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 耳蜗行波的发现者 / Georg von Békésy 1899–1972 + badge + 右上头像 + 国籍行（United States，匈牙利裔）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、布达佩斯、伯尔尼化学/布达佩斯物理学博士 1926、匈牙利邮局 23 年、哈佛 1947-66、檀香山 1966、诺奖 1961）
03  核心贡献概览 — 基底膜行波 / 频率位置分布 / 毛细胞响应 / 耳蜗机械模型
04  三都少年的漂移童年 (1899–1919) — 外交官之父（生于克卢日）、母亲克罗地亚出生、布达佩斯-慕尼黑-苏黎世三地求学、兄妹三人（兄 Miklós 后成著名农业生物学家）
05  化学与物理之间 (1919–1928) — 伯尔尼学化学、布达佩斯物理学博士（快速测定分子量法）、工程公司一年、1928 首篇内耳振动论文；婉拒 Bárány 的乌普萨拉职位（畏瑞典寒冬）
06  匈牙利邮局的二十三年 (1923–1946) — 电信信号质量研究引其叩问人耳、邮局实验室里做出诺奖级工作的独特路径
07  解剖学革命：尸体耳蜗部分存活解剖法 — 频闪摄影 + 银屑标记：基底膜以表面波方式运动
08  频率的地形图（核心页）— 高频→蜗底最大振幅、低频→蜗顶；不同频率在基底膜上位置分散后激发不同神经纤维；tonotopy 概念与机械模型验证
09  1961 诺贝尔奖（独得）— 官方理由全句；ASA 金质奖章同年；Denker/Leibniz 银章/Guyot/Shambough 等前史荣誉
10  理论的边界（诚实一页）— 其理论假定全被动机械过程；忽略多种哺乳动物基底膜的不连续解剖证据；Kemp 证明需要主动反馈；2025 Hudspeth 组最终证明哺乳动物内耳频率分析无需行波——行波理论被证伪（page.md 明载，科学自纠的范例）
11  流亡与转场 (1946–1966) — 1946 离匈赴卡罗林斯卡、1947 哈佛、1965 实验室火灾后受邀夏威夷、1966 夏威夷大学教授
12  荣誉与院士 — Leopoldina 院士 1962、七校荣誉博士（Münster/伯尔尼/帕多瓦/布宜诺斯艾利斯/科尔多瓦/夏威夷/森梅威斯）
13  收藏家与捐赠 — 亚洲艺术大藏家、藏品捐赠瑞典诺贝尔基金会；兄 Miklós 留匈获科苏特奖
14  身后 — 1972-06-13 逝于檀香山；Békésy 神经生物学实验室、1985 诺奖研讨会纪念文集
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 独享 | 1961 系**独得**（无共享者）——封面勿写"共享" |
| 理论被证伪 | page.md 明载三段递进：Békésy 忽略解剖不连续证据→Kemp 证明需主动反馈→2025 Hudspeth 组证明哺乳动物频率分析无需行波、其内耳理论"thus disproved"——**必须诚实呈现**，这是本篇最独特的一页；勿把行波理论写成定论 |
| tonotopy 表述 | "each sensory cell (hair cell) responds maximally to a specific frequency"系其理论推断；页面对其与后续毛细胞调谐发现的张力已有交代——表述区分"理论主张"与"后续确立" |
| Bárány 不入库 | Róbert Bárány（诺奖耳科前辈）仅 job offer 且被婉拒——非学术关系，不入库（库内虽有 Robert Bárány id=4602 可复用，但本篇无关系可写） |
| relations=1 | 诚实值：仅 parent-child（父 Sándor）；无配偶/门生/导师记载——立传勿虚构家庭页，以"收藏与孤独"作晚年叙事 |
| 国籍 | citation json "Hungary United States"、页面 Citizenship 仅列 U.S.、metadata [Hungary, US]——yaml 按 US(0)+Hungary(1)，正文写"匈牙利裔美国生物物理学家" |
| 生年月 | 无双值问题（1899-06-03 三处一致），但注意与 Burnet（1899-09-03）同年生——本批两位 1899 年生人勿混生卒 |
| 兄长 | Miklós 留在匈牙利、科苏特奖得主——仅叙事细节不入库 |
| 引语红线 | page.md 无整句直接引语（诺奖演讲标题除外）——全部转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| cochlea | 耳蜗 | 听觉器官螺旋部分 |
| basilar membrane | 基底膜 | 行波载体 |
| traveling wave | 行波 | Békésy 理论核心（后被修正） |
| tonotopy | 位置-频率对应（音调拓扑） | 频率沿蜗管分布 |
| hair cell | 毛细胞 | 感觉细胞 |
| stroboscope | 频闪仪 | 观测方法 |
| passive mechanics | 被动机械过程 | 其理论假定（后被证伪） |
| active feedback | 主动反馈 | Kemp 证明的必要环节 |

## 九、背景音乐选择

- **选定曲目**：**Nostalgia** — Alex-Productions（manifest 预分配）
- **匹配理由**："怀旧/悠长"贴合奥匈旧梦与邮局时代的孤独研究——一位在帝国的余晖里用频闪灯凝视螺旋的工程师；绵长曲式呼应行波沿蜗管缓缓推进的意象。
- **本地路径**：music_audio/ 下 Alex-Productions Nostalgia 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
