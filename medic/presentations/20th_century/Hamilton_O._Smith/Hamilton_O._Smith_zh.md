# 医学家立传提示词（Hamilton O. Smith）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1978 年**得主（与 Werner Arber、Daniel Nathans 三人共享）。
> 本文件是 Smith 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Hamilton Othanel Smith（1931-08-31 ~ 2025-10-25，享年 94 岁），美国微生物学家
- **气质关键词**：**首个 II 型限制酶的分离者、首个细菌基因组测序的核心、合成生物学的元老** —— 1978 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for the discovery of restriction enzymes and their application to problems of molecular genetics"（因其发现限制性内切酶及其在分子遗传学问题上的应用）
- **设计母题**：**HindII 的第一刀（the first cut of HindII）**。1970 年 Smith 与 Wilcox 从流感嗜血杆菌中分离出第一个在特定位点切割 DNA 的 II 型酶——以「第一刀落下时双链的整齐断口」作为视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Hamilton_O._Smith/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Hamilton_O._Smith/`；Makefile 复制后设 `MAIN=Hamilton_O_Smith_zh`（宏名禁句点，文件名保持 manifest 原名）；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | molecular biology | 分子生物学 | 1978 诺奖核心：II 型限制酶 | 核心页 |
| 1 | microbiology | 微生物学 | 流感嗜血杆菌研究本体 | 研究页 |
| 2 | biochemistry | 生物化学 | 限制酶与甲基化酶的生化分离 | 研究页 |
| 3 | genomics | 基因组学 | 首个细菌基因组测序、人类基因组组装 | 后期页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Werner Arber | 无向 | 1978 诺贝尔生理学或医学奖三人共享（限制酶） |
| co-honored | Daniel Nathans | 无向 | 1978 诺贝尔生理学或医学奖三人共享（限制酶） |
| colleague | Kent W. Wilcox | 无向 | 1970 共同发现首个 II 型限制酶 HindII |
| colleague | Myron M. Levine | 无向 | NIH 资助下在密歇根大学随其研究传染病 |
| colleague | Craig Venter | 无向 | TIGR/塞雷拉/JCVI 长期搭档，合成基因组学 |
| spouse | Liz Smith | 无向 | 育五子；先其而逝 |

**方向约定**：无向关系 from<to 自动归一。

## 五、配色方案 【人物专属】

- **气质**：临床医生转实验室的务实、切酶的锋利、基因组时代的远望
- **主色**：`#34558B`（嗜血杆菌蓝，酶与测序）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：`badgeHind` HindII — 剪刀红 `#A33A2E`；`badgeMethyl` 甲基化酶 — 印章蓝 `#3B4E8C`；`badgeGenome` 基因组测序 — 测序青 `#1B7A6B`；`badgeSynbio` 合成生物学 — 生命橙 `#C0722E`
- **背景母题**：深蓝底上双链被整齐切断的断口序列 + 断口旁的小段序列标签，错落成谱。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 第一刀的落下者 / Hamilton O. Smith 1931–2025 + 四色 badge + 右上肖像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、纽约/厄巴纳、伯克利/约翰霍普金斯医学院、TIGR/Celera、荣誉）
03  核心贡献概览 — HindII / 甲基化酶 / 首个细菌基因组 / 合成生物学
04  伊利诺伊少年 (1931–1952) — 厄巴纳-香槟长大、UIUC 起步、1950 转伯克利、1952 数学 BA
05  医学之路 (1952–1957) — 约翰霍普金斯医学院 1956 MD、华盛顿大学 Medical Service、海军服役
06  密歇根的传染病岁月 — NIH 资助、Levine 处研究、Henry Ford 医院住院医
07  1970 HindII（核心贡献页）— 与 Wilcox 自流感嗜血杆菌分离首个 II 型限制酶、特异位点切割
08  补全另一半 — 发现 DNA 甲基化酶、证实 Arber 的限制-修饰系统假说
09  1978 诺贝尔奖 — 与 Arber/Nathans 三人共享、1975 古根海姆（苏黎世）
10  基因组时代 (1995) — TIGR 测序首个细菌基因组 H. influenzae——恰是当年发现限制酶的同一菌种
11  人类基因组与 Celera (1998–) — 加入塞雷拉参与人类基因组组装
12  合成生物学 (2003–) — Phi X 174 病毒基因组合成、Mycoplasma laboratorium、Synthetic Genomics
13  家庭与晚年 — 妻 Liz 先逝、五子 12 孙 15 曾孙；2016 淋巴瘤；2025-10-25 卒于 Ellicott City
14  遗产：从第一刀到合成生命 — 重组 DNA/基因组学/合成生物学的三段接力
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生日双值 | frontmatter 1931-08-23 vs 正文 "born... on August 31, 1931"——**以正文 08-31 为准**（yaml 已按正文），此处注明 |
| 卒日 | 2025-10-25 卒于 Ellicott City, Maryland 自宅，享年 94；2016 确诊淋巴瘤——近年事实可写 |
| 获奖理由 | "for the discovery of restriction enzymes and their application to problems of molecular genetics"——**their**（与 Arber/Nathans 共享） |
| 三人分工 | **Smith 是 II 型限制酶的实际分离者**（HindII，1970 与 Wilcox）；Arber 理论化、Nathans 作图——本篇强调「分离」一侧 |
| 全名与文件名 | 全名 Hamilton Othanel Smith；yaml name_en 用 manifest 形式 'Hamilton O. Smith'；LaTeX 宏名禁句点故 MAIN 用下划线 |
| 同菌种闭环 | H. influenzae 既是 1960s 发现限制酶的菌种、又是 1995 首个被测序的细菌基因组——叙事闭环亮点 |
| 菌名拼写 | 正文末段误拼 H. influenza——术语表用正确 H. influenzae |
| Venter 关系 | TIGR/Celera/Synthetic Genomics/JCVI 长期协作——colleague 一边即可，note 概括三段机构 |
| 家庭 | 妻 Liz 先逝、五子（一子先逝）、12 孙 15 曾孙——正文有载；不建 parent-child 边 |
| 页面 workplace 口径 | infobox Workplaces 仅列华盛顿大学医学院，正文主线在霍普金斯/TIGR——以正文为准 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| restriction enzyme (type II) | II 型限制酶 | HindII 为首个 |
| HindII | HindII 酶 | 1970 与 Wilcox 共同发现 |
| DNA methylase | DNA 甲基化酶 | 限制-修饰系统的另一半 |
| Haemophilus influenzae | 流感嗜血杆菌 | 酶的来源菌与首个测序细菌 |
| bacterial genome sequencing | 细菌基因组测序 | 1995 TIGR 首例 |
| human genome assembly | 人类基因组组装 | Celera 时期 |
| Phi X 174 | Phi X 174 噬菌体 | 2003 合成基因组对象 |
| Mycoplasma laboratorium | 实验室支原体 | 半合成细菌计划 |
| synthetic biology | 合成生物学 | 晚年方向 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Through the Darkness** — Alex-Productions（manifest 预分配）
- **风格**：暗夜穿行 / 坚定 / 曙光前奏
- **匹配理由**：从临床病房到「第一刀」再到黑暗中拼接第一个基因组——Through the Darkness 的穿行感匹配其 60 年从酶切暗夜走向合成生命曙光的科研长旅（第二次使用该曲，首用 Akasaki，同为暗夜点灯者）。
- **本地路径**：`music_audio/` 下 Through the Darkness 曲目 → 复制为 `presentations/20th_century/Hamilton_O._Smith/Through_the_Darkness.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。

