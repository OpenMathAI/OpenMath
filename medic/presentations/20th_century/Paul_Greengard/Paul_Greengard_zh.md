# 医学家立传提示词（Paul Greengard）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 2000 年得主（与 Carlsson/Kandel 三人共享） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Paul Greengard（1925-12-11 生于纽约 ~ 2019-04-13 逝于纽约，享年 93 岁）
- **气质关键词**：**神经元内部信号转导的开创者、多巴胺与 DARPP-32 的破译者、以诺奖奖金设立女科学家奖的孝子** —— 2000 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，与 Carlsson/Kandel 共享同一句）：
  > "for their discoveries concerning signal transduction in the nervous system"
  > （因他们关于神经系统内信号转导的发现）
- **设计母题**：**磷酸化的瀑布（the phosphorylation cascade）**。多巴胺 docks 受体 → cAMP 升高 → PKA 激活 → 给蛋白装上磷酸开关——"慢速突触传递的第二信使世界"。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Paul_Greengard/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Paul_Greengard/page.md`；目录 `medic/presentations/20th_century/Paul_Greengard/`；Makefile 改 `MAIN=Paul_Greengard_zh`；肖像优先 images.txt 所列 Commons 图（2009 照），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Paul_Greengard.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neuroscience | 神经科学 | 职业主领域（infobox Fields） | 封面 |
| 1 | signal transduction | 信号转导 | 诺奖核心（第二信使级联） | 核心页 |
| 2 | dopamine signaling | 多巴胺信号 | DARPP-32 中央调控蛋白 | 诺奖页 |
| 3 | Alzheimer's disease research | 阿尔茨海默病研究 | Fisher 中心/Michael Stern 基金会 | 晚年页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Haldan Keffer Hartline | 师→本人 | 约翰霍普金斯博士导师（PhD 1953） |
| influence | Alan Lloyd Hodgkin | 无向 | 其一场讲座令其转向神经元的分子与细胞功能 |
| co-honored | Arvid Carlsson | 无向 | 2000 诺贝尔生理学或医学奖三人共享（神经系统信号转导） |
| co-honored | Eric Kandel | 无向 | 2000 诺贝尔生理学或医学奖三人共享（神经系统信号转导） |
| spouse | Ursula von Rydingsvard | 无向 | 雕塑家，1985 年再婚 |

> 对手方规范名：`Alan Lloyd Hodgkin` 沿用库内 id=6068（勿用 'Alan Hodgkin' 短形式）；`Haldan Keffer Hartline`/`Arvid Carlsson`/`Ursula von Rydingsvard` 新建（Carlsson stub 供 med-batch-34 复用镜像合并）；`Eric Kandel` 与本批 Kandel 篇同键。**relations=5 为诚实值**：两位儿子（Claude/Leslie）与首任妻子不入库。1985 诺奖奖金资助设立 Pearl Meister Greengard 奖（纪念难产去世的母亲）系立传亮点。

## 五、配色方案

- **气质**：杂耍艺人家庭的寒门 + 从数学物理转向生物物理的反战选择 + 老年仍执掌洛克菲勒实验室
- **主色**：突触深蓝 `#1F4E79`（神经元与深海电极的冷色）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` DARPP-32 与多巴胺 — 多巴胺橙 `#C97B2D`
  - `badgeB` 第二信使级联 — 信号青 `#2E7D8C`
  - `badgeC` 磷酸化与 PKA — 生化紫 `#5E4B8B`
  - `badgeD` Pearl Meister 女科学家奖 — 公益金 `#C9A227`
- **背景母题**：低透明度突触内磷酸化级联箭头 + cAMP 分子轮廓。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 神经元信号转导的破译者 / Paul Greengard 1925–2019 + badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、纽约、Hamilton 1948 数学物理、约翰霍普金斯 PhD 1953、Geigy/耶鲁/洛克菲勒、诺奖 2000）
03  核心贡献概览 — 多巴胺-cAMP-PKA 级联 / DARPP-32 / 慢突触传递分子机制 / 磷酸化开关
04  杂耍艺人之家 (1925–1948) — 父亲是杂耍喜剧演员、母亲难产去世、姐姐是演员 Irene Kane、犹太家庭随继母按基督教传统长大、二战海军电子技师（MIT 反神风预警系统）
05  弃物理从生物 (1945–1953) — 拒绝战后核武器主导的物理学界转投生物物理、Hamilton 数学物理学士 1948、霍普金斯 Hartline 实验室、Hodgkin 讲座转向神经元、PhD 1953
06  博士后与药厂岁月 (1953–1967) — 伦敦/剑桥/阿姆斯特丹博士后、Geigy 研究实验室生化部主任
07  学界回归 (1967–1983) — 叶史瓦大学爱因斯坦医学院、Vanderbilt、耶鲁药理系教授、1983 入洛克菲勒大学
08  信号转导之舞（核心页）— 多巴胺结合受体→胞内 cAMP 升高→激活 PKA→磷酸化开关其他蛋白：转录新蛋白/受体上膜增敏/离子通道上膜增兴奋性——神经元内部事件的完整链条
09  DARPP-32 与 2000 诺奖 — 中央调控蛋白 DARPP-32 工作；与 Carlsson、Kandel 共享；官方理由全句；NAS 奖 1991/Lashley 1993 等预演
10  洛克菲勒岁月与老年病 — Fisher 阿尔茨海默研究中心代理主席、Michael Stern 帕金森基金会（后并入 Michael J. Fox 基金会）、Bristol-Myers Squibb 神经科学奖
11  Pearl Meister Greengard 奖（亮点页）— 以诺奖奖金资助设立（2004）、纪念难产去世的母亲、年度授予杰出女性生物医学科学家、原话可引（"[women] are not yet receiving awards..."）
12  荣誉长廊 — NAS 1978、美国艺术与科学院 1978、Dickson 1978、NAS 神经科学奖 1991、Lashley 1993、国家科学奖章、Gerard 奖、Metlife 1998、布雷西亚荣誉博士 2007
13  家庭 — 首婚二子：Claude（伯克利数学博士、Foss Hill 创始人）、Leslie（耶鲁 MD+CS 博士、NYU Courant 所长、NAS/NAE 双院士、Steele 奖）；1985 娶雕塑家 Ursula von Rydingsvard
14  一处争议与身后 — 2018 联邦陪审团裁定洛克菲勒大学在其实验室督导下种族与国籍歧视案担责（page.md 明载客观一句）；2019-04-13 逝于纽约
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 三人共享 | 2000 三人共享同一句理由；分工：Carlsson=多巴胺作为神经递质、Greengard=慢突触传递的信号转导机制、Kandel=记忆存储的突触机制——三线并列勿混写 |
| Hodgkin 规范名 | 库内规范名 **Alan Lloyd Hodgkin**(6068)——page.md 作 Alan Hodgkin，勿以短形式建 stub |
| 仅一场讲座 | Hodgkin 系"a lecture"启发——influence，勿升级为师承 |
| 三段博士后 | 伦敦/剑桥/阿姆斯特丹三校博士后一段带过；Geigy 系药企（后诺华）经历勿漏 |
| 子女不入库 | 二子成就显著（Leslie 系 NAS/NAE 双院士）但不入库，家庭页一句 |
| 歧视案（克制）| 2018 洛克菲勒大学歧视案系其督导实验室发生——page.md 明载，客观一句放"争议"页，勿渲染成个人丑闻主角；宗教背景（犹太血统基督教抚养）客观带过 |
| 首任妻子 | page.md 未载姓名——勿虚构；Ursula 系第二任 |
| 无引语红线 | 可引：Pearl Meister 奖缘起原话（women not yet receiving awards...）；其余转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| signal transduction | 信号转导 | 本届诺奖共同领域 |
| second messenger | 第二信使 | cAMP 级联起点 |
| protein kinase A (PKA) | 蛋白激酶 A | cAMP 依赖 |
| DARPP-32 | DARPP-32 蛋白 | 其诺奖级核心发现 |
| phosphorylation | 磷酸化 | 开关机制 |
| dopamine | 多巴胺 | Carlsson 领域交界 |
| slow synaptic transmission | 慢突触传递 | 其研究定性 |
| Aplysia | （海兔）| Kandel 交界注记 |

## 九、背景音乐选择

- **选定曲目**：**Pathfinder** — Alex-Productions（manifest 预分配）
- **匹配理由**："开拓者"贴合其在神经元内部世界开辟信号转导研究路线的一生——从"受体被占据"到"级联被点亮"的新大陆；推进感曲式匹配其从战时电子技师到诺奖讲台的开拓弧线。
- **本地路径**：music_audio/ 下 Alex-Productions Pathfinder 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
