# 医学家立传提示词（Martin Evans）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2007 年得主（三人共享之一） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Martin John Evans（1941-01-01 生于格洛斯特郡 Stroud，在世）
- **气质关键词**：**胚胎干细胞的首次培养者、基因敲除小鼠的奠基人之一** —— 2007 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，三人共享同一句）：
  > "for their discoveries of principles for introducing specific gene modifications in mice by the use of embryonic stem cells ."
  > （因他们发现利用胚胎干细胞向小鼠引入特定基因修饰的原理）
- **设计母题**：**胚泡与克隆环（blastocyst & cloning ring）**。小鼠胚泡的内细胞团、培养皿中的克隆环与传代路径——"一个细胞长成一只小鼠"的视觉隐喻。
- **本地 Wikipedia 路径**：medic/presentations/pages/21th_century/Martin_Evans/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/21th_century/Martin_Evans/page.md`；目录 `medic/presentations/21th_century/Martin_Evans/`；Makefile 改 `MAIN=Martin_Evans_zh`；肖像优先 images.txt 所列 Commons 图（Evans in October 2007），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Martin_Evans.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | developmental biology | 发育生物学 |  vertebrate 发育的遗传调控，诺奖核心 | 核心页 |
| 1 | embryology | 胚胎学 | 胚泡/胚胎干细胞分离培养 | 干细胞页 |
| 2 | genetics | 遗传学 | 基因打靶与转基因小鼠 | 敲除页 |
| 3 | stem cell biology | 干细胞生物学 | 1981 与 Kaufman 首建小鼠 ESC 培养 | 干细胞页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| collaborator | Matthew Kaufman | 无向 | 1981 共同首建小鼠胚胎干细胞培养 |
| influence | Elizabeth Deuchar | 无向 | UCL 研究助理阶段实验室技能指导 |
| influence | Jacques Monod | 无向 | 剑桥听其讲座；metadata 误列博士导师 |
| advisor-student | Allan Bradley | 本人→学生 | infobox Doctoral students 明载 |
| advisor-student | Elizabeth Robertson | 本人→学生 | infobox Doctoral students 明载 |
| spouse | Judith Clare Williams | 无向 | 1966 结婚，护士，1993 获 MBE |
| co-honored | Mario Capecchi | 无向 | 2007 诺贝尔生理学或医学奖三人共享（胚胎干细胞基因修饰） |
| co-honored | Oliver Smithies | 无向 | 2007 诺贝尔生理学或医学奖三人共享（胚胎干细胞基因修饰） |
| co-honored | Richard Gardner | 无向 | 1999 March of Dimes 发育生物学奖共享 |

> 对手方规范名：`Oliver Smithies` 沿用库内既有记录（id=4407，本批 yaml UPD 回填）；其余按 page.md 形式新建 stub；`Mario Capecchi` stub 由本批先建（Capecchi 本人批次写镜像边）。

## 五、配色方案

- **气质**：英伦实验生物学的沉稳 + 干细胞研究的开创感 + 绅士学者的克制
- **主色**：剑桥干细胞蓝 `#175873`（胚泡悬浮的培养液色）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` 胚胎干细胞 — 干细胞青 `#2E86AB`
  - `badgeB` 基因敲除小鼠 — 敲除红 `#B23A48`
  - `badgeC` 发育遗传学 — 胚层紫 `#5E4B8B`
  - `badgeD` Cardiff 建制与产业 — 威尔士绿 `#3E6B4F`
- **背景母题**：稀疏同心克隆环 + 小簇细胞圆点（低透明度），自中心向外传代扩散。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 胚胎干细胞之父之一 / Martin Evans 1941– + 三人共享 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生年 Stroud、Christ's College 奖学金、UCL PhD 1969、剑桥、Cardiff、诺奖 2007）
03  核心贡献概览 — 胚胎干细胞培养 / 基因打靶 / 敲除小鼠 / 再生医学公司
04  早年与剑桥 (1941–1963) — 机械车间里学会用车床、St Dunstan's、Christ's College 大奖学金（遗传学黄金期）、因腺热免考毕业
05  UCL 博士 (1963–1969) — Deuchar 指导下练就实验室技能、目标"分离发育调控的 m-RNA"、1969 博士（两栖类早期胚胎 RNA）
06  剑桥遗传系与 Kaufman (1978–1981) — 1980 合作启动、用胚泡分离胚胎干细胞的构想
07  1981：小鼠胚胎干细胞首次培养 — 与 Kaufman 发表；同一年 Gail R. Martin 独立达成（注记）；Kaufman 赴爱丁堡后独力推进
08  从干细胞到敲除小鼠 — 基因修饰 ESC → 嵌合胚胎 → 配子传递 → HPRT 突变小鼠的完整链条；Smithies/Capecchi 实验室实现同源重组打靶（呼应诺奖三人分工）
09  2007 诺贝尔奖 — 三人共享；官方理由全句；2001 Lasker 已同三人预演
10  Cardiff 岁月与荣誉 — 1999 哺乳动物遗传学教授/生物科学院长、2004 爵士（New Year Honours）、2009 校长、2012 Chancellor、Copley Medal 2009、FRS 1993
11  产业与临床 — 2009 与 Ajan Reginald 共同创办 Celixir（原 Cell Therapy Ltd）
12  临床争议（客观一页）— 希腊 2012-2015 试验未获监管授权、期刊 Editorial Expression of Concern、Evans 不同意该 editorial；数据差异与 UKHRA 审查（仅 page.md 实载，平衡呈现）
13  家庭 — 妻 Judith Clare Williams（护士 MBE、乳腺癌康复后投身慈善）、Evans 任 Breakthrough Breast Cancer 信托人；两子一女
14  遗产：敲除小鼠改变医学 — 转基因小鼠成为现代医学研究基石
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 2007 三人共享（Evans/Capecchi/Smithies）同一句官方理由；勿写成 Evans 独得或"一半" |
| Evans 的诺奖分工 | 三人中 Evans 贡献是**胚胎干细胞系**（ESC 载体），同源重组技术实现主要在 Smithies/Capecchi 实验室——分工表述勿混 |
| Monod 师承 | metadata 列 Jacques Monod 为 doctoral_advisor，但 page.md 只载"听其讲座"——入库用 influence，**勿写博士导师**（其 PhD 系 UCL 1969，导师未具名） |
| 1981 双雄 | Gail R. Martin 同年独立培养小鼠 ESC——注记独立发现，勿写成 Evans 独家或含 Martin |
| Kaufman 角色 | 1981 论文 Evans 与 Kaufman 合作；Kaufman 离开后 Evans 独力续推——先后勿倒置 |
| 在世留白 | 在世者：无卒日，生卒行写"1941– "；relations 偏少为诚实值，勿为凑数入边 |
| 争议页 | Celixir 希腊试验争议仅写 page.md 实载四点（未授权/EoC/不同意/数据差异+UKHRA），措辞客观，勿加"造假"定性 |
| 妻子 | Judith Clare Williams 1966 结婚（剑桥求学时相识、曾赴加拿大一年后复合）——叙事线勿简化成"婚后即迁剑桥" |
| 骑士头衔 | 2004 Knight Bachelor（New Year Honours，"for services to medical science"，查尔斯王子授勋 06-25）；勿写"诺贝尔奖封爵" |
| 引语红线 | page.md 直接引语极少（"drawn into a number of fascinating fields"、"to isolate developmentally controlled m-RNA"）——只引实载，其余转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| embryonic stem cell (ESC) | 胚胎干细胞 | 与成体干细胞/IPS 区分 |
| blastocyst | 胚泡 | ESC 分离来源 |
| gene targeting | 基因打靶 | 同源重组定点修饰 |
| knockout mouse | 基因敲除小鼠 | 2007 诺奖应用成果 |
| homologous recombination | 同源重组 | 打靶的分子机制 |
| chimeric embryo | 嵌合胚胎 | ESC 参与生殖系的途径 |
| HPRT | 次黄嘌呤-鸟嘌呤磷酸核糖转移酶 | 首个 ESC 突变模型基因 |
| March of Dimes Prize | 行军硬币奖（发育生物学） | 1999 与 Gardner 共享 |

## 九、背景音乐选择

- **选定曲目**：**The Invisible Light** — Alex-Productions（manifest 预分配）
- **匹配理由**："不可见之光"贴合胚胎干细胞"肉眼不可见却可孕育完整个体"的开创感——从培养皿中的一个细胞到改变医学的小鼠模型，是无声处的惊雷；曲风沉静中带推进，匹配英伦实验生物学的克制叙事。
- **本地路径**：music_audio/ 下 Alex-Productions The Invisible Light 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
