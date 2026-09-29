# 医学家立传提示词（Rodney Robert Porter）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1972 年得主（与 Edelman 共享） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Rodney Robert Porter（1917-10-08 生于兰开夏 Newton-le-Willows ~ 1985-09-06 逝于萨里 Beacon Hill，享年 67 岁）
- **气质关键词**：**用木瓜蛋白酶切开抗体的第一人、Sanger 的首位博士生、补体系统研究的开拓者** —— 1972 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，与 Edelman 共享同一句）：
  > "for their discoveries concerning the chemical structure of antibodies"
  > （因他们关于抗体化学结构的发现）
- **设计母题**：**酶切之力（the enzymatic cut）**。木瓜蛋白酶把 Y 形抗体切成 Fab/Fc 片段——"把解不开的结用剪刀分开"。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Rodney_Robert_Porter/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Rodney_Robert_Porter/page.md`；目录 `medic/presentations/20th_century/Rodney_Robert_Porter/`；Makefile 改 `MAIN=Rodney_Robert_Porter_zh`；肖像优先 images.txt 所列 Commons 图，失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Rodney_Robert_Porter.yaml` 一致，勿重复入库；库内旧分裂 stub `Rodney Porter` id=1129 已按手册流程合并删除）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 职业主领域（infobox Fields） | 封面 |
| 1 | immunology | 免疫学 | 抗体化学结构，诺奖核心 | 诺奖页 |
| 2 | complement system | 补体系统 | 晚年与 Reid/Sim/Campbell 的开拓 | 研究页 |
| 3 | protein chemistry | 蛋白质化学 | Sanger 门下的游离氨基研究起步 | 求学页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Frederick Sanger | 师→本人 | Cambridge 博士导师（1948），Sanger 的首位博士生 |
| colleague | Elizabeth Press | 无向 | NIMR/St Mary's/Oxford 三站长期合作者，诺奖工作贡献卓著 |
| co-honored | Gerald Edelman | 无向 | 1972 诺贝尔生理学或医学奖共享（抗体化学结构） |
| colleague | Kenneth B. M. Reid | 无向 | 补体蛋白研究合作者 |
| colleague | Robert Sim | 无向 | 补体蛋白研究合作者 |
| colleague | Duncan Campbell | 无向 | 补体蛋白研究合作者 |
| spouse | Julia New | 无向 | 1948 结婚，育五子，2025 以 98 岁去世 |

> 对手方规范名：`Frederick Sanger` 沿用库内记录 id=1122（旧分裂边 1343 已随 id=1129 合并清理）；`Gerald Edelman` 沿用库内规范名 id=6158（citation json 作 Gerald M. Edelman，但库内/manifest 规范名为 Gerald Edelman——中间缩写差异会产生分裂 stub，首次入库时已按手册合并清理）；其余按 page.md 形式新建 stub。

## 五、配色方案

- **气质**：兰开夏铁路职员之子的朴实 + 剑桥-牛津的严谨 + 战场归来的沉稳
- **主色**：酶切铜棕 `#7A5230`（木瓜蛋白酶与实验台木色）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` 抗体片段化 — 片段金 `#C9A227`
  - `badgeB` 补体系统 — 补体红 `#A63A2B`
  - `badgeC` 蛋白化学 — 蛋白青 `#2E7D8C`
  - `badgeD` Oxford 建制 — 牛津深蓝 `#1F3A6E`
- **背景母题**：低透明度 Y 形抗体被虚线切成三段、酶剪刀轮廓。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 抗体化学结构的共同破译者 / Rodney Robert Porter 1917–1985 + badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Newton-le-Willows、Liverpool BSc 1939、Cambridge PhD 1948、NIMR/St Mary's/Oxford、诺奖 1972）
03  核心贡献概览 — 木瓜蛋白酶片段化 / Fab 与 Fc / 补体蛋白 / 抗体-细胞表面反应
04  铁路职员之子与二战 (1917–1945) — 车厢厂 chief clerk 之家、Liverpool 生物化学 1939、皇家工兵二尉转 陆军上尉（西西里/北非）、那不勒斯战争部分析员
05  Sanger 的首位博士生 (1945–1948) — Cambridge、蛋白质游离氨基博士论文 1948——Sanger 门下开山弟子
06  NIMR 十一年 (1949–1960) — 国家医学研究所长期任职、抗体研究起步
07  木瓜蛋白酶的胜利（核心页）— 用酶把免疫球蛋白切成易研究的片段（Fab/Fc 之分）；与 Edelman 的还原断链法互为镜像——两条路径会师抗体结构
08  St Mary's 与 Pfizer 讲席 (1960–1967) — 免疫学教授；Betty Press 三站相随、对诺奖工作贡献卓著（page.md 明载）
09  Oxford 岁月 (1967–1985) — Whitley 生物化学教授、Trinity College Fellow
10  1972 诺贝尔奖 — 与 Edelman 共享；官方理由全句；Gairdner 1966、Royal Medal 1973、Copley 1983、FRS 1964
11  补体系统的开拓 — 与 Reid/Sim/Campbell 合作攻关补体蛋白与抗感染防御
12  抗体与细胞表面 — 免疫球蛋白与细胞表面反应研究
13  家庭与身后 — 妻 Julia New（1948 结婚，五子）；1985-09-06 四车相撞事故中去世（赴法度假途中、正式退休前夕）、妻轻伤；Oxford 生化系 Rodney Porter 楼与年度纪念讲座
14  遗产：免疫学的化学基础 — 结构解析开启抗体工程时代
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 1972 两人共享同一句理由；分工：Porter=酶切段（木瓜蛋白酶）、Edelman=化学断链+完整测序——互补勿混写 |
| Sanger 首徒 | page.md 明载 "became Fred Sanger's first PhD student"——advisor-student 边系本篇最硬的师承；库内旧分裂 stub `Rodney Porter`(1129) 及其 1972 诺奖旧边已合并清理，行文勿再引用旧名形式 |
| 名字形式 | yaml/库内规范名 **Rodney Robert Porter**（manifest）；页面标题作 Rodney R. Porter——引用时统一全名 |
| Betty Press | "contributing extensively to the work which led to the Nobel Prize"系 page.md 明载——colleague 边已入，行文给足其贡献，勿写成"助手打杂" |
| 补体三人 | Reid/Sim/Campbell 系 page.md 点名合作者，三条 colleague 边均已入库；行文可合并一句呈现 |
| 事故离世 | 1985-09-06 四车相撞、本人为其中一车司机、妻随行轻伤——客观一句，勿渲染细节 |
| 妻子卒年 | Julia New 2025 年以 98 岁去世——本篇立传时点为事实，如实写 |
| 引语红线 | page.md 无整句直接引语——全部转述；Karolinska 新闻稿引语属 Edelman 篇素材，本篇不借用 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| papain | 木瓜蛋白酶 | 切割抗体的酶 |
| Fab / Fc | 抗原结合片段/可结晶片段 | 酶切片段命名 |
| immunoglobulin | 免疫球蛋白 | 抗体的化学称谓 |
| complement | 补体系统 | 晚年研究方向 |
| free amino groups | 游离氨基 | 博士论文对象 |
| Whitley Professor | 惠特利生物化学讲席 | Oxford 教席 |
| Rodney Porter building | 罗德尼·波特楼 | Oxford 生化系纪念命名 |

## 九、背景音乐选择

- **选定曲目**：**Expedition** — Alex-Productions（manifest 预分配）
- **匹配理由**："探险/远征"贴合其"从战场到实验室"的人生轨迹——北非西西里的军旅、Sanger 门下的开荒、把抗体大分子切开的攻坚；带行进感的曲式匹配结构生物学远征者的形象。
- **本地路径**：music_audio/ 下 Alex-Productions Expedition 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
