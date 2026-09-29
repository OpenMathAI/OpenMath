# 医学家立传提示词（Tasuku Honjo）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2018 年得主（与 Allison 共享） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Tasuku Honjo（本庶 佑，1942-01-27 生于京都，在世）
- **气质关键词**：**PD-1 的发现者、类别转换重组的概念奠基人、日本免疫学的旗手** —— 2018 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，与 Allison 共享同一句）：
  > "for their discovery of cancer therapy by inhibition of negative immune regulation"
  > （因他们发现通过抑制负向免疫调控来治疗癌症）
- **设计母题**：**免疫闸门（PD-1 gate）**。T 细胞闸门被 PD-1 扣住、抗体松开闸门的意象——"关上的门重新打开"。
- **本地 Wikipedia 路径**：medic/presentations/pages/21th_century/Tasuku_Honjo/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/21th_century/Tasuku_Honjo/page.md`；目录 `medic/presentations/21th_century/Tasuku_Honjo/`；Makefile 改 `MAIN=Tasuku_Honjo_zh`；肖像优先 images.txt 所列 Commons 图（Honjo in 2013、2018 诺奖发布会照），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Tasuku_Honjo.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | immunology | 免疫学 | 职业主领域（infobox Fields 分子免疫学） | 封面 |
| 1 | molecular immunology | 分子免疫学 | 抗体基因重排/AID | 贡献页 |
| 2 | cancer immunotherapy | 肿瘤免疫治疗 | PD-1 阻断原理，诺奖核心 | 核心页 |
| 3 | biochemistry | 生物化学 | 医学化学博士训练 | 求学页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Yasutomi Nishizuka | 师→本人 | 京都大学医学化学博士导师之一（1975） |
| advisor-student | Osamu Hayaishi | 师→本人 | 京都大学医学化学博士导师之一（1975） |
| advisor-student | Shizuo Akira | 本人→学生 | infobox Notable students 明载 |
| co-honored | James P. Allison | 无向 | 2018 诺贝尔生理学或医学奖共享（负向免疫调控抑制） |

> 对手方规范名：`Shizuo Akira` 沿用库内既有记录（id=5022）；`James P. Allison` 与本批 Allison 篇同形式镜像 co-honored 边幂等合并；其余按 page.md 形式新建 stub。**relations=4 为诚实值**（在世者，page.md 无配偶/家庭记载，勿虚构补边）。

## 五、配色方案

- **气质**：京都学派的沉静 + 五十年如一日的免疫学深耕 + 公共发声的担当
- **主色**：京都紫 `#4A235A`（日式优雅与学问的纵深）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` PD-1 — 闸门红 `#B23A48`
  - `badgeB` 抗体类别转换/AID — 抗体蓝 `#2E6E9E`
  - `badgeC` IL-4/IL-5 细胞因子 — 细胞因子青 `#2E7D8C`
  - `badgeD` 京都大学建制 — 京都紫 `#4A235A`
- **背景母题**：低透明度闸门弧线 + Y 型抗体简笔。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — PD-1 的发现者 / Tasuku Honjo（本庶 佑）1942– + badge + 右上头像 + 国籍行（Japan）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生年京都、京都大学 MD 1966/PhD 1975、Carnegie/NIH、大阪/京都教授、诺奖 2018）
03  核心贡献概览 — 类别转换重组框架 / IL-4/IL-5/AID / PD-1 / PD-1 阻断疗法
04  京都求学 (1942–1966) — 山口县立宇部高中、京都大学医学部 1966 MD
05  博士与留美 (1966–1977) — 1975 医学化学博士（Nishizuka/Hayaishi 双导师）；1971-73 华盛顿卡内基胚胎学系访问学者、1973-77 NIH NICHD 研究免疫反应遗传基础
06  三校教授线 — 东京医大助教授 1974-79、大阪大学遗传学教授 1979-84、京都医学化学教授 1984-2005、2005 起京都免疫与基因组医学；2012-17 静冈县立大学理事长；2017 KUIAS 副所长/特任教授
07  类别转换重组的概念框架（核心页一）— 抗体基因重排模型 1980-82 用 DNA 结构验证；class switch recombination 基本概念框架的确立者
08  细胞因子与 AID（核心页二）— 1986 IL-4/IL-5/IL-2 受体 α 链 cDNA 克隆；2000 发现 AID，证明其对类别转换与体细胞高频突变不可或缺
09  1992：PD-1 现身 — 活化 T 淋巴细胞上发现诱导性基因 PD-1；后续证明其阻断可建立癌症免疫疗法原理
10  2018 诺贝尔奖 — 与 Allison 共享；官方理由全句；CTLA-4 与 PD-1 两条刹车线互补
11  荣誉矩阵 — 朝日奖 1981、日本学士院奖 1996、文化勋章 2013（天皇授）、Robert Koch 奖 2012、Tang 奖 2014（与 Allison 同奖同成就）、京都奖 2016、Alpert 奖 2017
12  公共发声（客观一页）— 公开批评日本政府暂停 HPV 疫苗积极推荐（缺乏科学依据、公共健康风险）；支持记者 Riko Muranaka 诉讼中提交书面意见（科学可重复性）——仅 page.md 实载
13  会员与讲席 — 美国 NAS 国际会员 2001、德国 Leopoldina 2003、日本学士院 2005；名誉博士（澳门科大 2020/UBC 2021/台大 2024）
14  遗产：从抗体机制到抗癌武器 — PD-1 抑制剂改变全球肿瘤治疗格局
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 2018 两人共享同一句理由（Honjo=PD-1 线，Allison=CTLA-4 线）；2014 Tang 奖亦二人同享——两次共享勿混年份 |
| 双博士导师 | page.md 明载 "under the supervision of Yasutomi Nishizuka and Osamu Hayaishi"——两条 advisor 边并列，勿只取其一 |
| 生年 | metadata 双值 1942-01-27 / 01-01，**以 page.md 正文 27 January 1942 为准** |
| COVID 谣言 | 网传"本庶佑称病毒系武汉实验室制造"系**虚假信息**，其本人公开否认（BBC 引京都大学声明"greatly saddened"）——涉地缘政治敏感，立传**一律不写**该话题，仅陷阱表留存 |
| HPV 疫苗发声 | 仅写 page.md 两点（批评暂停推荐 + 支持记者诉讼），措辞客观；不扩展日本政策争论 |
| AID 年份 | AID 发现 **2000**；PD-1 鉴定 **1992**——两条时间线勿混 |
| 在世留白 | 在世者：无卒日；relations=4 诚实值（page.md 无家庭记载，勿虚构；除 Akira 外无具名学生） |
| 中文姓名 | 中文写"本庶 佑"，name_en 用 Tasuku Honjo；日文汉字仅封面/身份页点缀 |
| 引语红线 | page.md 无整句直接引语（BBC 转述除外且属禁写话题）——全部转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| PD-1 | 程序性细胞死亡蛋白 1 | 1992 鉴定的诱导性基因 |
| class switch recombination | (抗体)类别转换重组 | Honjo 概念框架 |
| AID | 活化诱导胞苷脱氨酶 | 2000 发现 |
| somatic hypermutation | 体细胞高频突变 | 与 CSR 共需 AID |
| IL-4 / IL-5 | 白细胞介素 4/5 | 1986 cDNA 克隆 |
| CTLA-4 | 细胞毒性 T 淋巴细胞抗原 4 | Allison 线（对照提及） |
| Order of Culture | 日本文化勋章 | 2013 天皇授 |
| Kyoto Prize | 京都奖 | 2016 基础科学 |

## 九、背景音乐选择

- **选定曲目**：**Winds Of Freedom** — Alex-Productions（manifest 预分配）
- **匹配理由**："自由之风"贴合"松开免疫闸门、让 T 细胞自由攻击肿瘤"的治疗哲学；开阔沉静的曲式匹配京都学派五十年如一日的深耕与公共发声的担当。
- **本地路径**：music_audio/ 下 Alex-Productions Winds Of Freedom 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
