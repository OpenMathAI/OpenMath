# 医学家立传提示词（Hugo Theorell）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1955 年得主（胡戈·特奥雷尔，氧化酶性质与作用方式的阐明者）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Axel Hugo Theodor Theorell（1903-07-06 生于瑞典林雪平 ~ 1982-08-15 卒于斯德哥尔摩，享年 79 岁）
- **气质关键词**：**毕生献给酶研究的酶学之父、氧化还原酶性质的阐明者、诺贝尔医学研究所首任诺奖得主** —— 1955 获奖理由（独享）：
  > "for his discoveries concerning the nature and mode of action of oxidation enzymes"（因发现氧化酶的性质与作用方式）
- **设计母题**：**发光的酶**。氧化还原酶催化电子转移——"分子世界里静默的呼吸"。视觉隐喻：一条被荧光标记的酶链在试管中明灭，辅以 Karolinska 的沉稳轮廓。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Hugo_Theorell/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/Hugo_Theorell/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/Hugo_Theorell/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Hugo_Theorell_zh`、`VIDEO_NAME=Hugo_Theorell_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/Hugo_Theorell/images.txt`；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Hugo_Theorell.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 毕生事业，1955 诺奖核心 | 核心页 |
| 1 | enzymology | 酶学 | 氧化还原酶的性质与作用方式 | 核心页 |
| 2 | alcohol dehydrogenase | 乙醇脱氢酶 | 分解酒精的酶，开创性进展 | 核心页 |
| 3 | physiological chemistry | 生理化学 | Karolinska 生理化学教授（1930 受聘） | 身份页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Albert Calmette | 导师 | 1924 巴斯德研究所随其学习细菌学三个月 |
| spouse | Elin Margit Elisabeth Theorell | 无向 | 妻（née Alenius），著名钢琴家与羽管键琴家，2002 年去世，合葬斯德哥尔摩北墓园 |

> **relations=2 为诚实值**——page.md 极短（仅 Life 一节），除 Calmette 短期游学与妻子外无任何师承/学生/同事记载，**Review 勿误判缺漏，勿从 Nobel 官网传记补料建边**。
> 不入库：父母 Thure Theorell 与 Armida Bill（背景叙事）；各国荣誉学位授予机构。
> 库内已有 Hugo Theorell stub（#4015，并行批次预建），本 yaml UPD 回填 Q156480；Albert Calmette / Elin Margit Elisabeth Theorell 由本 yaml 新建 stub。

## 五、配色方案 【人物专属】

- **气质**：北欧的极夜蓝 + 酶分子的荧光绿 + 卡罗林斯卡的克制
- **主色**：极夜蓝 `#173F5F`（瑞典冬夜的深邃与酶学的沉潜）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 氧化还原酶 — 极夜蓝 `#173F5F`
  - `badgeB` 乙醇脱氢酶 — 琥珀 `#A0722D`
  - `badgeC` 巴斯德研究所游学 — 灰紫 `#5C5470`
  - `badgeD` 诺贝尔医学研究所 — 深青 `#0E7C7B`
- **背景母题**：一条水平荧光酶链（明暗交替的圆点）横贯版面，badge 圆点如辅基嵌于其上。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 氧化酶的阐明者 / Hugo Theorell 1903–1982 + 四色 badge + 右上头像 + 国籍行 Sweden
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生 Linköping、教育 Katedralskolan/
    Karolinska（1924 医学士、1930 MD）、巴黎巴斯德研究所游学、
    任职 Karolinska 生理化学教授/诺贝尔医学研究所生化部主任、荣誉 Nobel 1955、核心领域）
03  核心贡献概览 — 氧化还原酶 / 乙醇脱氢酶 / 氟化物毒理与辅因子 / 诺贝尔医学研究所首奖
04  林雪平少年 (1903–1921) — 父 Thure Theorell、母 Armida Bill、
    Katedralskolan 中学、1921-05-23 通过会考
05  Karolinska 与巴黎游学 (1921–1924) — 1921-09 入卡罗林斯卡学医、
    1924 医学士毕业、巴斯德研究所随 Albert Calmette 学习细菌学三个月
06  MD 与教职 (1930) — 血浆脂质理论的 MD 学位、受聘 Karolinska 生理化学教授
07  1936：诺贝尔医学研究所生化部 — 新设生化部主任、
    该研究所第一位获诺贝尔奖的研究者
08  氧化还原酶的性质与作用方式 — 1955 诺奖核心工作、
    Nobel Lecture "The Nature and Mode of Action of Oxidation Enzymes"（1955-12-12）
09  乙醇脱氢酶 — 分解肝与其他组织中酒精的酶、开创性进展
10  氟化物毒理 — 氟化钠对关键人类酶辅因子毒作用的理论贡献
11  荣誉与认可 — 皇家学会外籍会员（ForMemRS）、Björkén Prize、
    法国/比利时/巴西/美国多校荣誉学位、美国艺术与科学院/NAS/美国哲学会
12  个人生活与身后 — 妻 Elin Margit Elisabeth（née Alenius），
    著名钢琴家与羽管键琴家（2002 逝）、1982-08-15 卒于斯德哥尔摩、
    合葬北墓园（Norra begravningsplatsen）
13  遗产（一）— 酶学作为现代生物化学的骨架、氧化酶研究通向呼吸链与代谢图谱
14  遗产（二）与结尾 — 乙醇脱氢酶与酒精代谢医学、诺贝尔医学研究所的"首奖"象征意义、
    北欧基础科学的沉潜气质、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for his discoveries concerning the nature and mode of action of oxidation enzymes"（**独享**，his）；与 Nobel Lecture 标题 "The Nature and Mode of Action of Oxidation Enzymes" 几乎同文——两处引用各自照抄 |
| 全名 | Axel Hugo Theodor Theorell——正文通称 Hugo Theorell；yaml/库内用 manifest 形式 `Hugo Theorell` |
| 页面极简 ★ | page.md 仅一节 Life——**宁少勿造**：无博士生、无争议内容可写；relations=2 诚实值须在 §4 注明 |
| Calmette 游学 | 仅 1924 年**三个月**细菌学学习——advisor-student 边 note 务必写"三个月"，勿拔高为长期博士训练 |
| "首位" | 诺贝尔医学研究所（Nobel Medical Institute，1936 新设生化部）**首位获诺奖的研究者**——page.md 明载 first，勿弱化 |
| 氟化物贡献 | "氟化钠对关键人类酶辅因子毒作用的理论"——是获奖贡献的组成部分（page.md 口径），可写但勿夸大为主线 |
| 荣誉学位 | 法国/比利时/巴西/美国多校荣誉学位——page.md 未列校名，勿杜撰具体大学 |
| 妻子职业 | Elin Margit Elisabeth（née Alenius）Theorell 为著名钢琴家与羽管键琴家、2002 年去世——死后 20 年合葬细节可入个人页 |
| 军旅/战争 | page.md 无二战内容——勿从外部来源补写其战时行为 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| oxidoreductase | 氧化还原酶 | 获奖理由核心词 |
| mode of action | 作用方式 | 官方理由用语 |
| alcohol dehydrogenase | 乙醇脱氢酶 | 肝与组织中分解酒精 |
| sodium fluoride | 氟化钠 | 毒作用理论对象 |
| cofactor | 辅因子 | 毒作用靶点 |
| plasma lipids | 血浆脂质 | 其 MD 学位论文主题 |
| Karolinska Institute | 卡罗林斯卡研究所 | 母校与教职 |
| Pasteur Institute | 巴斯德研究所 | 1924 短期游学 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Shine Like The Sun**（manifest 预分配）
- **风格**：明亮 / 辉光 / 大气
- **匹配理由**：氧化还原酶是细胞里静默的"电子之光"——Shine Like The Sun 的辉光感匹配"让不可见的分子反应显形"的酶学叙事，也呼应诺贝尔医学研究所第一缕诺奖之光。
- **本地路径**：`music_audio/` 下 Shine Like The Sun 对应文件（执行时以 `find music_audio -iname "*Shine*"` 实际定位）→ 复制为 `presentations/20th_century/Hugo_Theorell/Shine_Like_The_Sun.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；page.md 极简，宁少勿造、诚实值注明。**
