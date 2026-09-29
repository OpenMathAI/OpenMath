# 医学家立传提示词（Haldan Keffer Hartline）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1967 年得主（与 Granit、Wald 三人共享）。
> 本文件是 Hartline 的人物专属立传提示词：事实基准唯一来源为本地 Wikipedia 页面。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Haldan Keffer Hartline（1903-12-22 生于宾州布卢姆斯堡 ~ 1983-03-17 逝于马里兰州福尔斯顿，享年 79）
- **气质关键词**：**单根视神经纤维的第一个记录者、侧抑制机制的揭示者、鲎眼里的对比增强师**
- **诺奖获奖理由（1967，逐字引用 medic/nobel_medicine_citations.json）**：
  > "for their discoveries concerning the primary physiological and chemical visual processes in the eye"
  > （因其关于眼内初级生理与化学视觉过程的发现）——"their"：与 Granit、Wald 三人共享
- **设计母题**：**侧抑制（lateral inhibition）**。一个感受器兴奋、邻位被抑制——轮廓与对比由此而生；
  视觉母题用亮格点亮而四周暗格压低的光斑阵列，象征"视觉清晰度的神经算法"。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Haldan_Keffer_Hartline/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 medic 路径执行：页面读 `medic/presentations/pages/20th_century/{Dir}/page.md`，
> 产出放 `medic/presentations/20th_century/Haldan_Keffer_Hartline/`，数据库写 greatminds 库（MySQL）。
> 第 0 步核对事实基准 → 第 1 步建目录含 images/ → 第 2 步复制 Makefile 设
> `MAIN=Haldan_Keffer_Hartline_zh`、`VIDEO_NAME=Haldan_Keffer_Hartline_zh` → 第 3 步收肖像（Commons 回退，404 装饰圆）→
> 第 4~9 步 tex 编写 → 编译循环（0 error、vbox≤10pt、hbox≤50pt）→ pdftoppm 逐页目检 → make images/video → Review。

## 三、研究领域梳理 + 入库（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | physiology | 生理学 | 视觉的电生理机制（infobox Fields） | 核心页 |
| 1 | neurobiology | 神经生物学 | 视网膜单纤维记录与侧抑制 | 核心页 |
| 2 | biophysics | 生物物理学 | Johns Hopkins 生物物理学系主任（1949） | 职业页 |

## 四、社会关系梳理 + 入库（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Ragnar Granit | 无向 | 1967 诺贝尔生理学或医学奖三人共享（眼内初级生理与化学视觉过程） |
| co-honored | George Wald | 无向 | 1967 诺贝尔生理学或医学奖三人共享（眼内初级生理与化学视觉过程） |
| advisor-student | August Herman Pfund | 师→生（博士导师） | infobox 明载（Johns Hopkins 医学院时期） |
| advisor-student | Paul Greengard | Hartline→学生 | Johns Hopkins 研究生，后亦获诺贝尔奖（page.md 明载） |
| spouse | Elizabeth Kraus Hartline | 无向 | 1936 年结婚；三子 Daniel/Peter/Frederick |

> 说明：relations=5 全部 page.md 明载（诚实值）。Detlev W. Bronk 系宾大 Johnson Foundation 主任（机构关系）不入库；
> Greengard 库内无记录，本侧新建 stub。自查 SQL：`SELECT COUNT(*) FROM person_relation WHERE from_id=<pid> OR to_id=<pid>;` 预期 = 5。

## 五、配色方案

- **气质**：简繁之间、以简驭繁的实验大师
- **主色**：深海军蓝 `#1E4E79`（大西洋鲎的潮间带蓝）+ 香槟金 `#D4AF37`（诺奖色）
- **四分类色 badge**：`badgeLimulus` 鲎眼 — 电光蓝 `#4C5FD5`；`badgeInhibit` 侧抑制 — 冷青 `#0E7C7B`；`badgeFiber` 单纤维记录 — 暖橙 `#E07B30`；`badgeAward` 荣誉 — 皇家紫 `#52307C`
- **背景母题**：中央亮格 + 环暗格的光斑阵列（侧抑制对比图形）

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页
01  封面 — 鲎眼中的对比算法 / Haldan Keffer Hartline 1903–1983 + 四色 badge + 国籍行（United States）
02  身份信息页 — 生卒/布卢姆斯堡出身/Lafayette 1923 + Johns Hopkins MD 1927/宾大→Cornell→Johns Hopkins→洛克菲勒/核心领域
03  核心贡献概览 — 单纤维记录 / 侧抑制 / 简单视觉系统 / 诺奖
04  宾州少年 (1903–1923) — Bloomsburg 出生；Lafayette College 1923 毕业
05  Johns Hopkins (1923–1927) — NRC Fellow 起步视网膜电生理；1927 医学博士（Pfund 门下）
06  德国游学与宾大 (1927–1940) — Eldridge Johnson 旅行学者赴莱比锡大学与慕尼黑大学；归国入宾大 Johnson 医学物理基金会（主任 Bronk）
07  康奈尔一年与重返宾大 (1940–1949) — 1940-41 Cornell Medical College 生理学副教授；重返宾大至 1949
08  Johns Hopkins 生物物理系 (1949–1953) — 生物物理学教授、Jenkins 系主任；研究生 Paul Greengard（后亦获诺奖）
09  鲎眼实验（核心贡献页）— 聚焦鲎（Limulus polyphemus）复眼：微小电极首次记录单根视神经纤维的电脉冲；选择节肢动物/软体动物等"简单视觉系统"的方法论
10  侧抑制的发现 — 感受器互相连接：一个受光兴奋、邻位被抑制——增强光型对比、锐化形状感知；简单视网膜机制=视觉信息整合的关键一步
11  1967 诺贝尔奖 — 理由逐字；与 Granit/Wald 三人共享；ForMemRS 1966（诺奖前一年）
12  荣誉与认可 — NAS 1948 · 美国哲学学会 1952 · AAAS 1957 · 光学学会 (OSA) 首批 Fellow 1959、1980 荣誉会员 · ForMemRS 1966 · Howard Crosby Warren 奖章
13  洛克菲勒岁月 (1953–1983) — 1953 加入洛克菲勒大学任神经生理学教授直至晚年
14  家庭 — 1936 娶 Elizabeth Kraus Hartline；三子 Daniel/Peter/Frederick；1983-03-17 逝于马里兰州 Fallston
15  结尾
```

## 七、特殊陷阱表（★ 执行时必须核对）

| # | 陷阱 | 说明 |
|---|------|------|
| 1 | 获奖理由 | 逐字 "for their discoveries concerning the primary physiological and chemical visual processes in the eye"；三人共享 |
| 2 | 卒日双值 | frontmatter date_of_death 有 ["1983-03-17","1987-03-17"] 两值——**以正文/infobox 1983-03-17（享年 79）为准**，yaml 存 1983，陷阱注明 |
| 3 | 博士导师 | August Herman Pfund 仅 infobox/正文 frontmatter 有载（page.md 正文叙事未展开）——照实入库并注明来源层级 |
| 4 | 学位 | Johns Hopkins **医学博士 (MD) 1927**，NRC Fellow 身份起步视网膜电生理——勿写 PhD |
| 5 | 鲎的选择 | 研究对象含节肢动物/脊椎动物/软体动物，**集中于鲎**（Limulus polyphemus）——勿写成"研究鲎的复眼结构"（其研究是电生理） |
| 6 | 单纤维首次 | "first record of the electrical impulses sent by a single optic nerve fibre"——"首次记录"是 page.md 明载，勿降格为"较早" |
| 7 | Greengard | 系其 Johns Hopkins 研究生、后亦获诺奖——学生边入库；勿写成"洛克菲勒时期学生" |
| 8 | Bronk 不入库 | Detlev W. Bronk 是 Johnson Foundation 主任/机构人物——不建边 |
| 9 | 引语红线 | page.md 无任何直接引语——全篇不得出现"原话"式引语 |
| 10 | 教职年表 | Penn→Cornell(1940-41)→Penn(至1949)→Johns Hopkins(1949-1953)→洛克菲勒(1953–)——Cornell 仅一年，勿写成"任教多年" |

## 八、术语清单

| 英文 | 中文 | 风险点 |
|------|------|--------|
| lateral inhibition | 侧抑制 | 对比增强机制，本篇核心 |
| Limulus polyphemus | 美洲鲎 | 模式生物，"鲎眼" |
| optic nerve fibre | 视神经纤维 | 单纤维记录对象 |
| photoreceptor | 光感受器 | 互连抑制网络单元 |
| microelectrode | 微电极 | 记录工具 |
| biophysics | 生物物理学 | Johns Hopkins 系主任头衔 |
| ForMemRS | 皇家学会外籍院士 | 1966 当选 |
| Howard Crosby Warren Medal | 沃伦奖章 | 认知/实验心理学家奖项 |

## 九、背景音乐选择

- **选定曲目**：**Winds Of Freedom** — Alex-Productions（manifest 预分配）
- **匹配理由**：开阔舒展的旋律对应其研究气质——以最简单的视觉系统回应最普遍的"看清世界"命题；
  海风感贴合潮间带鲎眼的实验意象，也呼应其宾大-霍普金斯-洛克菲勒的从容学术旅程。
- **备选（未采用）**：SEA（海感重叠但 batch-07 已用于 Schekman）、Daylight（明亮感贴合视觉主题但已占用）
- **本地路径**：`music_audio/` 曲库按 curated_tracks.md 复制为 `medic/presentations/20th_century/Haldan_Keffer_Hartline/Winds_Of_Freedom.wav`
