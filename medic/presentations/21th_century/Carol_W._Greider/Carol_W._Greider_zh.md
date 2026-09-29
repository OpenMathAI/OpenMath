# 医学家立传提示词（Carol W. Greider）

> OpenMedic 项目、21 世纪诺贝尔生理学或医学奖 2009 年得主（卡罗尔·格雷德，端粒酶的发现者）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Carolyn Widney Greider（1961-04-15 生于加州圣地亚哥，在世）
- **气质关键词**：**端粒酶的亲手发现者、从阅读障碍到诺奖的坚韧学者、端粒-衰老-癌症轴的开拓者** —— 2009 获奖理由（与 Elizabeth Blackburn、Jack W. Szostak 三人共享）：
  > "for the discovery of how chromosomes are protected by telomeres and the enzyme telomerase"（因发现染色体如何受端粒和端粒酶保护）
- **设计母题**：**圣诞夜的凝胶**。1984-12-25，Greider 在放射自显影胶片上看到端粒酶活动的规律条带——"一个有规律的模式在发光"。视觉隐喻：暗室中发光的凝胶条带，渐次点亮染色体末端。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Carol_W._Greider/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/21th_century/Carol_W._Greider/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/21th_century/Carol_W._Greider/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Carol_W._Greider_zh`、`VIDEO_NAME=Carol_W._Greider_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/21th_century/Carol_W._Greider/images.txt`（2021 照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Carol_W._Greider.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | telomere biology | 端粒生物学 | 端粒酶发现者，2009 诺奖核心 | 核心页 |
| 1 | molecular biology | 分子生物学 | infobox Fields；端粒酶生化机制 | 核心页 |
| 2 | genetics | 遗传学 | 敲除小鼠与酵母端粒维持 | 研究页 |
| 3 | cellular senescence | 细胞衰老 | 与 Harley 证明端粒缩短是衰老基础 | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Elizabeth Blackburn | 导师 | Berkeley 博士导师（1987 PhD），1984-12-25 得到端粒酶活性关键结果 |
| co-honored | Elizabeth Blackburn | 无向 | 2009 诺贝尔生理学或医学奖三人共享（端粒与端粒酶保护染色体） |
| co-honored | Jack W. Szostak | 无向 | 2009 诺贝尔生理学或医学奖三人共享（端粒与端粒酶保护染色体） |
| collaborator | Ronald A. DePinho | 无向 | 合作产生首只端粒酶敲除小鼠（端粒缩短致早衰表型） |
| collaborator | Calvin Harley | 无向 | 1990 合作证明端粒缩短是细胞衰老的基础 |
| spouse | Nathaniel C. Comfort | 无向 | 结婚（正文作 1992，infobox 作 1993），2011 离异，育二子 |

> 在世者、page.md 篇幅所限，**relations=6 为诚实值**（师生 + 同享 + 2 合作 + 配偶），Review 勿误判缺漏。
> 不入库：infobox "Other academic advisors"（Beatrice M. Sweeney / David J. Asai / Leslie Wilson，红链或无正文语境，防弱关系噪声）；Michael D. West（招募其入 Geron 顾问委员会，商业关系）；实验室学生与博后未具名。
> 库内既有 Jennifer Doudna（#4248, Q56068）规范记录可查；Blackburn（#1130）与 Szostak 由其本人 yaml 规范化，本 yaml 以 manifest 全名引用。

## 五、配色方案 【人物专属】

- **气质**：暗室凝胶的荧光 + 加州阳光的通透 + 阅读障碍者的直觉力
- **主色**：荧光紫红 `#7A3E6E`（放射自显影条带的荧光感，亦含"非典型路径"的独特性）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 端粒酶发现 — 荧光紫红 `#7A3E6E`
  - `badgeB` 生化机制（RNA 模板） — 深青 `#0E7C7B`
  - `badgeC` 敲除小鼠与衰老 — 暗红 `#8C2F1B`
  - `badgeD` 酵母与四膜虫 — 琥珀 `#A0722D`
- **背景母题**：横向排布的发光条带（凝胶电泳意象），四色交替，隐喻"规律在噪声中显现"。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 端粒酶的发现者 / Carol W. Greider 1961– + 四色 badge + 右上头像 + 国籍行 USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生 San Diego、教育 UCSB BA 1983/Göttingen/
    Berkeley PhD 1987、导师 Blackburn、任职 Cold Spring Harbor/Johns Hopkins/UCSC、
    荣誉 Nobel 2009/Lasker 2006、核心领域）
03  核心贡献概览 — 端粒酶的发现 / 端粒酶的生化机制 / 敲除小鼠与衰老 / 酵母端粒维持
04  圣地亚哥与阅读障碍 (1961–1983) — 双亲为学者（父为物理学教授）、Davis 高中、
    一年级发现读写倒错、死记拼写与"补偿性直觉"自我叙述、UCSB College of Creative Studies、
    哥廷根交换；GRE 低分的代价——13 所研究生院只录 2 所
05  选择 Berkeley (1984) — Caltech 与 Berkeley 二选一、加入 Blackburn 实验室（1984-04）、
    寻找假想的"给染色体末端加碱基"的酶、选用非常规模型四膜虫
06  1984-12-25：圣诞夜的凝胶 — 放射自显影上的规律条带、六个月补验、
    1985-12 Cell 论文（telomere terminal transferase → telomerase）
07  RNA 模板的证明 — RNA 降解酶使端粒停止延伸、酶含 RNA+蛋白双组分、
    RNA 部分为添加重复序列的模板
08  Cold Spring Harbor 岁月 (1987–1997) — Fellow 起步、克隆四膜虫端粒酶 RNA 基因（1989）、
    证明端粒酶持续性（1991）、体外重组（1994）、模板利用机制（1995）、
    与 Harley 证明端粒缩短是衰老基础（1990）
09  敲除小鼠：端粒酶并非生存必需 — 与 DePinho 合作首只端粒酶敲除小鼠、
    端粒渐短致早衰表型、第六代全不育、与对照交配可再生端粒
10  Johns Hopkins 时代 (1997–2020) — 1997 入 Hopkney、2004 Daniel Nathans 教授、
    脊椎动物端粒酶 RNA 二级结构（2000）与模板边界（2003）、人类端粒酶 RNA 假结（2005）、
    酵母重组型端粒维持与 DNA 损伤应答、2014 Bloomberg 讲席
11  2006 Lasker → 2009 Nobel — Lasker 三人共享为诺奖前奏、2009 三人共享诺奖、
    获奖序列 Lounsbery 2003/Lasker 2006/Horwitz 2007/Greengard 2008/Nobel 2009
12  回到加州：UC Santa Cruz — 2021 起 Distinguished Professor、
    实验室用酵母/小鼠/生化探究端粒渐短与肿瘤再现、未来聚焦端粒加工与调控
13  阅读障碍者的科学 — 自述"补偿性技能帮助直觉统筹并行线索"、
    选择非常规生物（四膜虫）的非常规决策、AWIS Pinnacle Award（2019）
14  遗产 — 从圣诞夜凝胶到衰老医学、端粒酶的临床想象（癌症/早衰）、
    端粒生物学成为教科书章节、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for the discovery of how chromosomes are protected by telomeres and the enzyme telomerase"；三人共享 |
| 发现年份 | infobox/正文：1984-04 加入实验室、1984-12-25 关键结果、六个月补验、1985-12 Cell 发表——勿写成"1987 发现"（1987 是 PhD 年份） |
| 酶的旧名 | 原名 "telomere terminal transferase"，后称 telomerase——两个名都要出现 |
| 结婚年份双值 ★ | 正文 "married ... in 1992"，infobox "(m. 1993; div. 2011)"——以正文 1992 为准并注记 infobox 差异 |
| 阅读障碍叙事 | Greider 自述补偿性技能帮助科学直觉（page.md 有自述引语，可引原文）——励志叙事须出自其自述，勿渲染成"缺陷成就天才" |
| 择校细节 | 因 GRE 低分被 13 所拒 11 所、录 Caltech+Berkeley——精确数字勿错；"在哥廷根做出重要发现"仅此一句，勿展开 |
| Other academic advisors | infobox 列 Sweeney/Asai/Wilson——**不入库**（无正文语境，防噪声），在本表记录裁定 |
| 端粒酶敲除小鼠 | 端粒酶 dispensable for life（非生存必需）但短端粒致多表型——两面都要说，勿写成"端粒酶决定寿命"的简化版 |
| 任职终点 | 2021 起在 **UC Santa Cruz**（Distinguished Professor），勿误写"现仍在 Johns Hopkins"；1997-2021 在 Hopkins |
| 在世者关系 | relations=6 为诚实值；Blackburn 师生+同享双边、Szostak 仅同享边——照实 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| telomerase | 端粒酶 | 原"端粒末端转移酶" |
| telomere terminal transferase | 端粒末端转移酶 | 1985 论文旧名 |
| autoradiogram | 放射自显影 | 圣诞夜凝胶的关键技术 |
| knockout mouse | 敲除小鼠 | mTERT 缺失模型 |
| processive | 持续性（酶学） | 1991 年证明的酶学性质 |
| pseudoknot | 假结 | 人类端粒酶 RNA 结构（2005） |
| template boundary | 模板边界 | 2003 年定义 |
| senescence | 细胞衰老 | 与 Harley 1990 论证 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Mirage**（manifest 预分配）
- **风格**：迷离 / 内省 / 氛围渐显
- **匹配理由**：暗室中"看似噪声却规律发光"的凝胶，正是海市蜃楼的反面——幻象中辨出真实；Mirage 的渐显氛围匹配其"非常规直觉从噪声中拎出信号"的发现叙事与阅读障碍者的非常规路径。
- **本地路径**：`music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav` → 复制为 `presentations/21th_century/Carol_W._Greider/Mirage.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；励志叙事须出自其自述，勿过度渲染。**
