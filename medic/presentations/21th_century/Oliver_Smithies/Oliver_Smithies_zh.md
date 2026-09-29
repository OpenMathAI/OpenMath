# 医学家立传提示词（Oliver Smithies）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2007 年得主（三人共享之一） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Oliver Smithies（1925-06-23 生于西约克郡 Halifax ~ 2017-01-10 逝于北卡教堂山，享年 91 岁）
- **气质关键词**：**淀粉凝胶电泳的发明者、基因打靶技术的共同奠基人、91 岁仍每天进实验室的"工匠科学家"** —— 2007 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，三人共享同一句）：
  > "for their discoveries of principles for introducing specific gene modifications in mice by the use of embryonic stem cells ."
  > （因他们发现利用胚胎干细胞向小鼠引入特定基因修饰的原理）
- **设计母题**：**凝胶上的条带（bands on the gel）**。淀粉凝胶电泳的分离条带、DNA 同源重组的交叉图式——"把蛋白质与基因分开来看"的视觉隐喻。
- **本地 Wikipedia 路径**：medic/presentations/pages/21th_century/Oliver_Smithies/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/21th_century/Oliver_Smithies/page.md`；目录 `medic/presentations/21th_century/Oliver_Smithies/`；Makefile 改 `MAIN=Oliver_Smithies_zh`；肖像优先 images.txt 所列 Commons 图（AIC Gold Medal 2009 照、与小布什合影等），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Oliver_Smithies.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | genetics | 遗传学 | 基因打靶/敲除小鼠，2007 诺奖核心 | 打靶页 |
| 1 | biochemistry | 生物化学 | 物理生化出身（Ogston 门下） | 早年页 |
| 2 | molecular genetics | 分子遗传学 | 同源重组修饰动物基因组 | 打靶页 |
| 3 | cardiovascular genetics | 心血管遗传学 | 晚年与 Maeda 用改造小鼠研究高血压 | 研究页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Alexander G. Ogston | 师→本人 | Oxford 博士导师（1951，物理生物化学） |
| influence | J. W. Williams | 无向 | 威斯康星博士后东家（Commonwealth Fund 奖学金） |
| influence | Norma Ford Walker | 无向 | 从其学习医学遗传学；合作证明血浆蛋白变异可遗传 |
| co-honored | Mario Capecchi | 无向 | 2007 诺贝尔生理学或医学奖三人共享（胚胎干细胞基因修饰） |
| co-honored | Martin Evans | 无向 | 2007 诺贝尔生理学或医学奖三人共享（胚胎干细胞基因修饰） |
| co-honored | Ralph L. Brinster | 无向 | 2002/03 Wolf 医学奖共享（与 Capecchi） |
| spouse | Nobuyo Maeda | 无向 | 第二任妻子，UNC 病理学教授 |
| collaborator | Nobuyo Maeda | 无向 | 2002 合作用基因改造小鼠研究高血压 |
| spouse | Lois Kitze | 无向 | 第一任妻子，1950s 结婚，1978 分居 |

> 对手方规范名：`Oliver Smithies` 本人记录为库内既有 stub id=4407（本 yaml UPD 回填）；`Martin Evans` 与本批 Evans 篇同形式镜像 co-honored 边幂等合并；其余按 page.md 形式新建 stub。

## 五、配色方案

- **气质**：约克郡工程师之子的朴拙 + 凝胶条带的秩序美 + 九旬仍在飞滑翔机的赤子
- **主色**：淀粉凝胶棕 `#7A5C2E`（电泳凝胶与木质实验台的暖棕）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` 凝胶电泳 — 条带蓝 `#3D6B8C`
  - `badgeB` 基因打靶 — 打靶红 `#A63A2B`
  - `badgeC` 医学遗传学 — 遗传紫 `#5E4B8B`
  - `badgeD` UNC 岁月 — 卡罗来纳蓝 `#2E5E9E`
- **背景母题**：低透明度纵向条带组（电泳泳道）+ 交叉重组图式细线。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 基因打靶的共同奠基人 / Oliver Smithies 1925–2017 + 三人共享 badge + 右上头像 + 国籍行（United States，生于英国）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Halifax、Oxford Balliol 1946/1951、Toronto→Wisconsin→UNC、诺奖 2007）
03  核心贡献概览 — 淀粉凝胶电泳 / 同源重组基因打靶 / 敲除小鼠 / 高血压小鼠模型
04  约克郡少年 (1925–1943) — 保险推销员之子、双胞胎兄弟、无线电与望远镜点燃科学兴趣、Heath Grammar School
05  Oxford：从医学到化学 (1943–1951) — Brackenbury 奖学金入 Balliol、解剖学获奖、Ogston 物理化学教程点拨转轨、1948 与 Ogston 合写首篇论文、1951 DPhil
06  多伦多 Connaught (1953–1960) — 签证问题被迫离美、胰岛素前体研究的"副产物"：1955 淀粉凝胶电泳；Otto Hiller 技术协助；与 Norma Ford Walker 合作证明血浆蛋白变异遗传
07  威斯康星 (1960–1988) — 遗传学系助教→正教授（Leon J. Cole/Hilldale 讲席）、1980s 基因打靶问世
08  基因打靶与敲除小鼠（核心页）— 同源重组替换单个小鼠基因；Capecchi 独立平行发展（注记）；癌症/囊性纤维化/糖尿病研究的全球方法学基础
09  2007 诺贝尔奖 — 与 Capecchi、Evans 共享；官方理由全句；2001 Lasker 三人预演
10  荣誉矩阵 — Lasker 2001、Wolf 2002/03（与 Capecchi、Brinster）、Thomas Hunt Morgan Medal 2007、NAS 1971、ForMemRS 1998、两度 Gairdner（1990/1993）、AIC Gold Medal 2009
11  UNC 与晚年 (1988–2017) — Excellence Professor of Pathology、八旬仍每日进实验室、350+ 论文横跨 1948-2016
12  家庭与业余 — 两任妻子（Lois Kitze 分居 1978；Nobuyo Maeda 合作+伴侣）、色盲却持照飞行爱滑翔、自述无神论者
13  告别 — 2017-01-10 逝于教堂山；Halifax 蓝牌纪念
14  遗产：从条带到基因组 — 电泳是蛋白时代的钥匙，打靶是基因组时代的钥匙
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 2007 三人共享同一句理由；Smithies 的独特贡献点=**在动物细胞中实现同源重组打靶**（与 Capecchi 同时、独立）；Evans 提供 ESC 载体 |
| 独立发现 | page.md 明载 Capecchi "also developed the technique independently"——勿写"师承"或"谁先谁后"定论 |
| 国籍口径 | manifest/citation 主国别 United States（归化入籍），metadata 双国籍 [US, UK]；yaml 按 US(0)+UK(1) 双行，正文写"英裔美国人" |
| 诺奖表述 | 诺奖是"for his genetics work"（正文转述），官方全句是三人共享句——引用统一用 json 版本 |
| 电泳发明年份 | 淀粉凝胶电泳 **1955**（多伦多时期、胰岛素前体研究的"副产物"）；勿写成威斯康星时期 |
| 两任妻子 | Lois Kitze（1950s 结婚、1978 分居——page.md 用 separated，勿写"离婚"）；Nobuyo Maeda（第二任，spouse+collaborator 双行） |
| Wolf 奖三人 | 2002/03 Wolf 医学奖与 Capecchi、Ralph L. Brinster 三人共享（Brinster 非 2007 诺奖得主，勿混入） |
| 在世者亲属 | 父 William（保险推销）、母 Doris née Sykes（Halifax 技术学院英语教师）——page.md 有载可写；不入库（非科研关系，纪律以科研与家庭核心边为准） |
| 死亡地点 | 2017-01-10 逝于北卡教堂山（Chapel Hill），享年 91 |
| 引语红线 | page.md 无整句直接引语——全部转述，中文引号内不得出现"原话" |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| gel electrophoresis | 凝胶电泳 | Smithies 1955 引入淀粉介质 |
| starch gel | 淀粉凝胶 | 首个高分辨蛋白分离介质 |
| homologous recombination | 同源重组 | 打靶分子机制 |
| gene targeting | 基因打靶 | 定点替换单基因 |
| knockout mice | 敲除小鼠 | 2007 诺奖应用 |
| Connaught Laboratory | 康诺特医学研究实验室 | 多伦多时期东家 |
| Brackenbury Scholarship | 布拉肯伯里奖学金 | 入读 Balliol |
| March of Dimes Prize | 发育生物学奖 | 2005 与 Capecchi 共享 |

## 九、背景音乐选择

- **选定曲目**：**Shine Like The Sun** — Alex-Productions（manifest 预分配）
- **匹配理由**："如日生辉"贴合其 60 余年不间断的科学生命力——从 1955 凝胶条带到 82 岁诺奖、91 岁仍每日进实验室；明亮而不燥的曲式匹配这位"快乐工匠"的赤子气质。
- **本地路径**：music_audio/ 下 Alex-Productions Shine Like The Sun 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
