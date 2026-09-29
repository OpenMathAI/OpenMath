# 医学家立传提示词（Élie Metchnikoff）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1908 年**得主（与 Paul Ehrlich 共享）。
> 本文件是 Metchnikoff 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Élie Metchnikoff（Илья Ильич Мечников；1845-05-15 [俄历 5-03] ~ 1916-07-15，享年 71 岁），俄罗斯帝国动物学家、免疫学家
- **气质关键词**：**吞噬作用的发现者、先天免疫之父、老年学的命名者、酸奶长寿说的布道者** —— 1908 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "in recognition of their work on immunity"（因其对免疫的研究）
- **设计母题**：**海星幼虫旁的哨卫（sentinels around the starfish larva）**。1882 年梅西纳，Metchnikoff 把柑橘刺插入海星幼虫，次日看见细胞聚集环刺——以「刺与环聚的守卫细胞」作为先天免疫的视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Élie_Metchnikoff/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Élie_Metchnikoff/`；Makefile 复制后设 `MAIN=Elie_Metchnikoff_zh`（LaTeX 宏名禁用非 ASCII 重音，文件名保持 manifest 原名）；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | immunology | 免疫学 | 1908 诺奖核心：吞噬作用与细胞免疫 | 核心页 |
| 1 | microbiology | 微生物学 | 霍乱自体实验、肠道菌群学说 | 微生物页 |
| 2 | gerontology | 老年学 | 1903 命名 gerontology、酸奶长寿说 | 老年页 |
| 3 | zoology | 动物学 | 本业出身；比较胚胎研究 | 早年页 |
| 4 | embryology | 胚胎学 | 与 Kovalevsky 共获 von Baer 奖 | 早年页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Rudolf Leuckart | 师→生（实验室导师） | 吉森大学实验室导师，在此作出首项发现（线虫世代交替） |
| co-honored | Alexander Kovalevsky | 无向 | 1867 与其共享 Karl Ernst von Baer 奖（胚层发育研究） |
| influence | Charles Darwin | 无向 | 深受进化论影响，支持自然选择与生物发生律 |
| spouse | Ludmila Feodorovitch | 无向 | 1869 结婚，1873-04-20 死于肺结核 |
| spouse | Olga Belokopytova | 无向 | 1875 娶其学生 Olga，1944 卒于巴黎 |
| advisor-student | Isaak Krasilschik | 生（Metchnikoff→学生） | 学生，合作以绿僵菌生物防治害虫 |
| colleague | Émile Roux | 无向 | 巴斯德研究所同事，合作甘汞软膏预防梅毒 |
| colleague | Carl Friedrich Wilhelm Claus | 无向 | 维也纳动物学教授，建议 phagocyte 一词 |
| colleague | Louis Pasteur | 无向 | 1888 应邀入巴斯德研究所，终老于此 |
| colleague | Rudolf Virchow | 无向 | 主要支持者，在其 Archiv 刊发其吞噬细胞论文 |
| co-honored | Paul Ehrlich | 无向 | 1908 诺贝尔生理学或医学奖共享（免疫研究） |

**方向约定**：`advisor-student` + `direction: advisor` = 对方是导师；`direction: student` = 对方是学生；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：乐观的怀疑论者、海边的博物学家、生命延长赛的鼓手
- **主色**：`#175873`（地中海海蓝，梅西纳的海与巴斯德研究所）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：
  - `badgePhago` 吞噬作用 — 珊瑚橙 `#C4622D`
  - `badgeImmune` 细胞免疫 — 免疫青 `#1E7A6B`
  - `badgeGero` 老年学 — 暖褐金 `#9A7B3F`
  - `badgeRussia` 俄罗斯岁月 — 冷灰蓝 `#4E6478`
- **背景母题**：浅海蓝底上散布海星剪影与环刺聚集的小圆细胞群（大小错落），呼应梅西纳实验。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 先天免疫之父 / Élie Metchnikoff 1845–1916 + 四色 badge + 右上肖像 + 国籍行（Russia）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、伊万诺夫卡、哈尔科夫/吉森/圣彼得堡、巴斯德研究所、荣誉）
03  核心贡献概览 — 吞噬作用 / 细胞免疫 / 益生菌观念 / 老年学命名
04  伊万诺夫卡的少年 (1845–1862) — 摩尔达维亚贵族父 + 乌克兰犹太母、母亲力主自然科学、哈尔科夫大学两年修完四年
05  德国求学线 (1864–1867) — Heligoland 海岛、Cohn 引荐 Leuckart、线虫世代交替首发现、吉森发现扁虫胞内消化
06  博士与敖德萨讲席 (1867–1882) — 与 Kovalevsky 共获 von Baer 奖、22 岁任敖德萨讲师、1870 动物学正教授
07  梅西纳的海星幼虫之夜 (1882)（核心贡献页）— 辞职赴西西里、柑橘刺实验、吞噬现象发现
08  phagocyte 命名与论战 — Claus 建议 phagocyte 一词、1883 敖德萨报告、Pasteur/Behring 等怀疑、Virchow 力挺刊文
09  细胞免疫 vs 体液免疫 — Metchnikoff 细胞派 vs Ehrlich 体液派、opsonin 调理素汇合（Wright 1903 后）
10  巴斯德研究所岁月 (1888–1916) — 敖德萨疫苗站长遇挫、Pasteur 面谈聘任、与 Roux 合作梅毒预防、终老研究所
11  霍乱自体实验 (1892) — 自饮霍乱菌而不病、志愿者一安一危、肠道菌群决定易感性假说
12  酸奶与 orthobiosis — 保加利亚乳杆菌、1903《人性研究》/1907《延寿乐观研究》、probiotics 观念先声
13  1908 诺贝尔奖 — 与 Ehrlich 共享 "work on immunity"、细胞+体液两派同台加冕、1906 Copley 奖章、1916 Albert 奖章
14  遗产：以 Mechnikov 命名的机构 — 敖德萨国立大学、圣彼得堡西北医科大学、乌克兰微生物学研究所；5-15 Metchnikoff Day
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒双值 | 生：正文 infobox 作 **15 May [O.S. 3 May] 1845**；frontmatter 有 05-03/05-15/05-16 三值——正文 05-15 为准；explanatory note 明载 16 May 系其本人换算错误（诺奖委员会裁定）。卒：正文 infobox **15 July 1916**（frontmatter 07-02/07-16 为噪声） |
| 姓名形式 | 本名 Ilya Ilyich Mechnikov，西文名 Élie Metchnikoff；动物学作者缩写 Metschnikoff/Mechnikov；yaml name_en 用 manifest 形式 Élie Metchnikoff |
| 国籍口径 | manifest/Nobel 官方为 **Russia**；正文强调生于今乌克兰境内的俄国帝国，五个民族都宣称他——表述用「俄罗斯帝国」 |
| 获奖理由 | "in recognition of their work on immunity"——**their**（与 Ehrlich 共享） |
| 博士导师裁定 | frontmatter doctoral_advisor 列 Leon Cienkowski 与 Louis Pasteur，但正文均无载——**不入库**；正文明载的导师线索是 Leuckart 实验室（师承）与圣彼得堡获博士（with Kovalevsky），据此入库 |
| Pasteur 关系 | 先是怀疑其学说者、后是聘任他的东家——colleague 一行 note 需兼顾；勿写成 Pasteur 学生 |
| 论战对象 | Behring 与多数细菌学家怀疑吞噬说；Ehrlich 是学术对手但同台获奖（正文明载 Metchnikoff 曾"尖锐攻击"Ehrlich）——争议表述对事不对人 |
| 妻子两位 | 第一任 Ludmila 1869、1873-04-20 卒于肺结核（其死引发第一次服鸦片自杀未遂）；第二任 Olga 是其学生，1880 斑疹伤寒引发第二次自杀未遂（注射回归热螺旋体）——自杀经历正文明载可写，但表述克制 |
| Darwin 批评 | 他批评 Darwin 对 Malthus 人口论的盲从——影响关系是「深受影响但有批评」，勿写成全盘接受 |
| 遗体 | 依遗嘱遗体供医学研究后在拉雪兹公墓火化，骨灰坛存巴斯德研究所图书馆——可写 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| phagocytosis | 吞噬作用 | 1882 发现；细胞免疫基础 |
| phagocyte / macrophage | 吞噬细胞 / 巨噬细胞 | 命名由 Claus 建议 |
| innate immunity | 先天免疫 | 「先天免疫之父」称号 |
| humoral immunity | 体液免疫 | Ehrlich 一侧，与细胞免疫互补勿对立 |
| gerontology | 老年学 | 1903 由其命名 |
| orthobiosis | 正生（正常生活之道） | 其益生菌观念的自创术语 |
| Lactobacillus delbrueckii subsp. bulgaricus | 保加利亚乳杆菌 | 酸奶长寿说核心菌 |
| opsonin | 调理素 | Wright 1903 后调和两派的关键概念 |
| biogenetic law | 生物发生律 | Haeckel 重演论，其支持 |
| Copley Medal | 科普利奖章 | 1906 皇家学会授予 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Daylight** — Alex-Productions（manifest 预分配）
- **风格**：明亮 / 温暖 / 乐观
- **匹配理由**：Metchnikoff 的底色是乐观主义者——《 optimistic studies》《人性研究》都以乐观为题；Daylight 的明亮温暖匹配他从丧妻自毁走向科学乐观的人生转折，也匹配「白血球是身体的守卫者」这一带来光明的发现。
- **本地路径**：`music_audio/` 下 Daylight 曲目 → 复制为 `presentations/20th_century/Élie_Metchnikoff/Daylight.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。
