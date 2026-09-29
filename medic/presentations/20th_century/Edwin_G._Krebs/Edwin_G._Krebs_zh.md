# 医学家立传提示词（Edwin G. Krebs）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1992 年**得主（与 Edmond H. Fischer 共享）。
> 本文件是 Krebs 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Edwin Gerhard Krebs（1918-06-06 ~ 2009-12-21，享年 91 岁），美国生物化学家
- **气质关键词**：**可逆磷酸化的另一半发现者、Cori 夫妇门下的意外生物化学家、听障而不改其志的实验家** —— 1992 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for their discoveries concerning reversible protein phosphorylation as a biological regulatory mechanism"（因其关于可逆蛋白磷酸化作为生物调控机制的发现）
- **设计母题**：**糖原的钥匙（the glycogen key）**。磷酸化酶 b↔a 的互变就是细胞开动糖原分解的钥匙——以「酶分子上挂卸磷酸小锁的往复」作为视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Edwin_G._Krebs/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **同名区分**：与 Hans Adolf Krebs（1953 诺奖，三羧酸循环，本库另有记录）完全无关，行文避免「克雷布斯」裸称

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Edwin_G._Krebs/`；Makefile 复制后设 `MAIN=Edwin_G_Krebs_zh`（宏名禁句点，文件名保持 manifest 原名）；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 1992 诺奖核心：可逆蛋白磷酸化 | 核心页 |
| 1 | enzymology | 酶学 | 磷酸化酶 b/a 互变的酶学机制 | 研究页 |
| 2 | pharmacology | 药理学 | 1977 回华大任药理学系主任 | 任职页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Edmond H. Fischer | 无向 | 1992 诺贝尔生理学或医学奖共享（可逆蛋白磷酸化） |
| co-honored | Alfred G. Gilman | 无向 | 1989 Lasker 基础医学奖与 Louisa Gross Horwitz 奖共享 |
| advisor-student | Carl Ferdinand Cori | 师→生（博士后导师） | 1946 起在华大其实验室作博士后（磷酸鱼精蛋白与兔肌磷酸化酶） |
| advisor-student | Gerty Cori | 师→生（博士后导师） | 同上，Cori 夫妇实验室（1947 诺奖得主） |
| spouse | Virginia Krebs | 无向 | 2018 卒；育三子 |

**方向约定**：`advisor-student` + `direction: advisor` = 对方是导师；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：牧师之子的朴素、军医转科研的偶然、西雅图的沉静
- **主色**：`#8A4A2E`（糖原铜褐，磷酸化酶与代谢）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：`badgePhos` 磷酸化开关 — 磷酸橙 `#D07B2A`；`badgeCori` Cori 门下 — 圣路易斯砖红 `#7E2D26`；`badgeUW` 华盛顿大学 — 常青绿 `#2E5E4E`；`badgeDavis` 加州 Davis 建系 — 加州金 `#A8752F`
- **背景母题**：米白底上酶分子剪影与 b↔a 互变双箭头小图，错落连缀。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 磷酸化开关的另一半 / Edwin G. Krebs 1918–2009 + 四色 badge + 右上肖像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Lansing Iowa、伊利诺伊/华盛顿大学 MD、华大/UC Davis、荣誉）
03  核心贡献概览 — 可逆磷酸化 / 磷酸化酶互变 / 激酶-磷酸酶循环 / 疾病意义
04  牧师之子的漂泊童年 (1918–1936) — 兰辛出生、频繁迁居、1933 丧父、厄巴纳 定居、Urbana 高中
05  医学与海军 (1936–1946) — 伊利诺伊 BS、华盛顿大学医学院奖学金 1943 MD、Barnes 住院医、海军军医
06  命运的岔口 (1946–1948) — 战后无法回临床、听劝改学基础科学、入 Cori 夫妇实验室做博后
07  磷酸鱼精蛋白与兔肌磷酸化酶 — 博后研究起点、1948 华大助理教授
08  Fischer 到来 (1953)（核心贡献页）— 同系同问题会师、磷酸化酶酶学分工、肌型/薯型之异
09  可逆磷酸化的发现 — b→a 激酶上磷酸、磷酸酶卸磷酸、激素与钙触发的代谢开关
10  迟到的承认与疾病意义 — 细胞分裂/形态/运动调控、癌症与糖尿病关键、现代药物基础
11  荣誉前哨 — Horwitz 1989（与 Alfred Gilman）、Lasker 1989、Welch 化学奖 1991
12  1992 诺贝尔奖 — 与 Fischer 共享
13  建系者 (UC Davis 与华大) — Davis 生化系创始主任、1977 回华大任药理学系主任
14  遗产与身后 — 听障而不改其志、2009-12-21 卒于西雅图；妻 Virginia 2018 卒、三子
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒日 | 1918-06-06 生于 Lansing, Iowa；2009-12-21 卒于西雅图，享年 91 |
| 获奖理由 | "for their discoveries concerning reversible protein phosphorylation as a biological regulatory mechanism"——**their**（与 Fischer 共享） |
| 同名区分 | 与 Hans Adolf Krebs（1953 诺奖、三羧酸循环）无任何关系——全篇用「Edwin G. Krebs」全称或「E. G. Krebs」，防混淆 |
| 「偶然的生物化学家」 | 其自传题为 An accidental biochemist：战后无法回临床、听劝转基础科学——转折叙事可用 |
| Cori 双导师 | 博后师从 Carl 与 Gerty Cori 夫妇（1947 诺奖）——两位各建 advisor-student 一行；Carl 库内无记录按 Fischer 页全名 'Carl Ferdinand Cori' 新建，Gerty 沿用库内(3461) |
| Gilman 边 | 1989 Lasker 与 Horwitz 奖与 Alfred G. Gilman 共享——co-honored 一行，note 写明是两奖而非诺奖，防 Review 误改 |
| 听障 | 正文明载 hearing impaired——克制一笔即可 |
| 家庭 | 妻 Virginia 2018 卒、三子在世——spouse 一行；不建 parent-child 边 |
| 无引语 | 本页正文无直接引语——引号内不得出现「原话」 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| reversible protein phosphorylation | 可逆蛋白磷酸化 | 诺奖理由核心词 |
| phosphorylase b / a | 磷酸化酶 b/a 型 | 互变即开关 |
| protein kinase | 蛋白激酶 | 上磷酸 |
| phosphatase | 磷酸酶 | 卸磷酸 |
| glycogen | 糖原 | 代谢底物 |
| protamine | 鱼精蛋白 | 博后研究试剂 |
| Louisa Gross Horwitz Prize | 哥伦布大学 Horwitz 奖 | 1989 与 Gilman 共享 |
| Welch Award in Chemistry | 韦尔奇化学奖 | 1991 |
| UC Davis | 加州大学戴维斯分校 | 生化系创始主任 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Awaken** — Alex-Productions（manifest 预分配）
- **风格**：苏醒 / 明亮 / 启程感
- **匹配理由**：磷酸化循环就是细胞亿万次「苏醒-休眠」的开关——Awaken 的启程感匹配「沉睡的磷酸化酶被唤醒」的核心发现，也匹配战后军医转身科研、1953 与 Fischer 会师后体系被逐渐唤醒的迟来的承认（第二次使用该曲，首用 Veltman/Perl，同为唤醒者）。
- **本地路径**：`music_audio/` 下 Awaken 曲目 → 复制为 `presentations/20th_century/Edwin_G._Krebs/Awaken.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。
