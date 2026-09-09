# Evangelista Torricelli（埃万杰利斯塔·托里拆利）立传提示词

> qid=Q102490 · 1608-10-15 – 1647-10-25 · 意大利数学家/物理学家 · 17 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/17th_century/pages/Evangelista_Torricelli/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**注意：本地 images.txt 无标准肖像**（仅有《Lezioni》扉页肖像、雕像照等）；执行时从 Wikimedia Commons 下载 **Lorenzo Lippi 约 1647 年画像**（infobox 所用）至 `images/torricelli_portrait.jpg`；失败则用《Lezioni》扉页肖像或装饰圆 `\faIcon{user}` 占位。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 意大利`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、国籍、出生地、师承、教育、核心领域。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），母题呼应「水银柱 / 空气之洋涟漪」之美。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Evangelista Torricelli（埃万杰利斯塔·托里拆利）
- **生卒**：1608-10-15 生于罗马（教皇国）→ 1647-10-25 逝于佛罗伦萨（托斯卡纳大公国），39 岁生日后第 10 天去世，享年 39
- **国籍**：metadata 记 Grand Duchy of Tuscany（按事业归属），实际生于教皇国（罗马）、家庭来自 Faenza——现代对应意大利
- **身份**：数学家、物理学家、发明家
- **家庭**：父 Gaspare Ruberti（纺织工人，家境贫寒）；母亲 page.md 自相矛盾（Giacoma Torricelli vs Caterina Angetti）——身份信息页写"母亲（史料记载有出入）"或略去；长子；养子 Alessandro（继承其全部遗物）
- **教育轨迹**：
  - 早年 Faenza，由舅舅（Camaldolese 修士）抚养教育
  - 1624–1626 耶稣会学院学数学与哲学（page.md 推测在 Faenza）
  - 1626 赴罗马，1626–1632 担任 Benedetto Castelli（伽利略的学生、罗马 Sapienza 数学教授）的秘书与弟子——原文 "There is no actual evidence that Torricelli was enrolled at the university. It is almost certain that Torricelli was taught by Castelli."
- **师承**：Benedetto Castelli（直接导师）；1641 年赴 Arcetri 任伽利略口述秘书三个月（直至伽利略 1642-01-08 去世）；亦曾为卡瓦列里的学生与挚友

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **气压计的发明（1643）**：一端封闭约 1 米长管装满水银倒立水银槽，水银柱降至约 76 cm，管顶留出**托里拆利真空**——"the first recorded incident of creating permanent vacuum"（有记录的第一次造出持久真空）。
2. **"空气之海"假说**：我们生活在"air sea"的底部，气压如水压——首次科学解释抽水泵只能把水抽到约 10 米；奠定现代大气压概念与气压计/高度计。
3. **"我们沉溺于空气之洋的底部"**：1644-06-11 致 Michelangelo Ricci 信 "Noi viviamo sommersi nel fondo d'un pelago d'aria."——本传主引语。
4. **托里拆利定律**：容器底部小孔出水速度正比于水深平方根（page.md 形式 dy/dt = −k√y），后成为伯努利原理特例。
5. **托里拆利小号（Gabriel 号角）**：`y = 1/x` 绕轴旋转体——**表面积无穷而体积有限**的"不可思议"悖论，引发关于无穷本质的大论战（含霍布斯）。
6. **无穷级数先驱**：《De dimensione parabolae》(1644) 用伸缩级数证明几何级数求和。
7. **不可分法的传播者**：表述比卡瓦列里更易读，"Many 17th century mathematicians learned of the method through Torricelli"。
8. **摆线求积**：求出摆线面积与重心；与 Roberval 爆发优先权争议。
9. **"安全抛物线"与包络概念**：首次建立**包络（envelope）**概念。
10. **托里拆利原理（虚功原理）**：重心不能升降则平衡——后被惠更斯用于摆的研究。
11. **风的科学解释**：风由两地温差与密度差产生——首次科学解释。
12. **透镜研磨**：发明灯焊玻璃制显微透镜方法，制望远镜与显微镜；佛罗伦萨存有多片刻有其名字的大透镜。
13. **继承伽利略衣钵**：1642 年伽利略去世后继任**大公数学家**及比萨大学数学讲席（Ferdinando II 任命）。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（佛罗伦萨酒红） | `#7E2A33` | 托斯卡纳 / 伽利略学脉 |
| 强调色（水银金） | `#C9A227` | 气压计 / 大公数学家 |
| 分类色 1（气压与真空 — 青绿） | `#0E7C7B` | 托里拆利真空 / 空气之海 |
| 分类色 2（几何 — 靛蓝） | `#4C5FD5` | 托里拆利小号 / 摆线 / 包络 |
| 分类色 3（流体与力学 — 琥珀） | `#E07B30` | 托里拆利定律 / 虚功原理 |
| 分类色 4（光学 — 玫红） | `#B76E79` | 透镜研磨 / 望远镜 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），母题呼应「水银柱涟漪 / 空气之洋」之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**巴洛克典雅 / 灵动清澈**（伽利略传人、实验科学的早晨）
- **匹配理由**：
  - 托里拆利是实验物理学黎明期人物——需**清澈、灵动**的配乐
  - "清澈" 匹配其真空实验与透明透镜的意象
  - "典雅" 匹配其美第奇宫廷数学家身份
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：沿用系列曲目 **Timeless**（本系列已统一采用，保持一致）
  - 备选：巴洛克 / 17 世纪意大利风格曲目
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐梅森/伯努利模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「气压计之父 · 托里拆利小号」+ 埃万杰利斯塔·托里拆利 1608–1647 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 国籍 / 出生地 / 师承 / 教育 / 核心领域）
3. **托里拆利的一生：时间线**（`\timelineslide`）：1608 罗马出生 → 1626 罗马师从 Castelli → 1641 任伽利略秘书 → 1642 继任大公数学家 → 1643 气压计实验 → 1644 《Opera geometrica》→ 1647 去世
4. **早年与教育**（`\earlyslide`）：Faenza、耶稣会学院、罗马师从 Castelli（无注册入学证据）、伽利略称许的罗马"三头同盟"
5. **气压计与托里拆利真空**（核心贡献页，表格 + 公式框）：1643 水银实验、"第一次造出持久真空"
6. **空气之海与大气压**（核心贡献页，表格 + 公式框）：假说内容、解释 10 米泵极限、"We live submerged..."
7. **托里拆利小号**（核心贡献页，表格 + 公式框）：`y=1/x` 旋转体、体积有限表面积无穷、无穷悖论之争
8. **托里拆利定律**（核心贡献页，表格 + 公式框）：`dy/dt = −k√y`、伯努利原理特例
9. **摆线与包络**（核心贡献页，表格 + 公式框）：摆线面积重心、安全抛物线、与 Roberval 的争议
10. **虚功原理与风的解释**（核心贡献页，表格 + 公式框）：托里拆利原理、风的温差成因
11. **光学与透镜**（核心贡献页，表格 + 公式框）：灯焊透镜、望远镜显微镜、佛罗伦萨藏镜
12. **不可分法的传播与学界网络**（表格）：比卡瓦列里更易读、与 Ricci 通信、Viviani 学生、伽利略/卡瓦列里学脉
13. **荣誉与传承**（表格）：压强单位 torr、月球环形山、Torricelli 山脉、"En virescit Galileus alter"
14. **终章**：39 岁、英年早逝的"另一个伽利略"的历史定位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **出生地**：page.md 明言 "born on 15 October 1608 in Rome"，家庭来自 Faenza；metadata 的 place_of_birth 同时列 "Rome" 与 "Faenza"——写"生于罗马，祖籍 Faenza"；逝世地仅 Florence（metadata 多出的 Rome 弃用）。
- **母亲姓名自相矛盾**：Giacoma Torricelli vs Caterina Angetti——slide 勿写死任一名字。
- **无大学注册证据**：原文 "There is no actual evidence that Torricelli was enrolled at the university."——勿写"毕业于罗马 Sapienza 大学"，只写"师从 Castelli"；metadata 的 "Roman College" 与 page.md（"possibly the one in Faenza"）冲突，弃用。
- **气压计优先权限定**：笛卡尔 1631 年已描述原理但未建造仪器（原文 "although there is no evidence that Descartes ever built such an instrument"）；海拔升高水银柱下降是**帕斯卡**的预测与证明；假说与实验的先后原文承认不确定——均需限定语。
- **托里拆利定律公式形式**：page.md 给的是 dy/dt = −k√y 与"速度 ∝ √深度"；常用 v=√(2gh) **未在原文出现**——若使用需另注来源。
- **摆线争议**：Roberval 指控抄袭，原文定性 "Although it appears that Torricelli reached his solution independently, the matter was still in dispute up to his death."——写"独立完成（似是）、争议至死未决"。
- **公开支持哥白尼仅一次**：1632 年致伽利略信是其唯一公开表态——勿夸大。
- **死因**："fever, most likely typhoid"（发热，最可能伤寒）——勿写疟疾。
- **小号命名**：Torricelli's trumpet 也更常被称为 **Gabriel's Horn**——两名皆可。
- **无院士记录**：page.md/metadata 均无林琴学院等院士身份——不得虚构。
- **称号**："气压计之父"为通行称号可用；"En virescit Galileus alter"（又一个伽利略开花了）为 1715 年遗著卷首字谜，注明出处。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q102490 | 待写入 |
| name_zh | 埃万杰利斯塔·托里拆利 | 待写入 |
| name_en | Evangelista Torricelli | 待写入 |
| birth_date | 1608-10-15 | 待写入 |
| death_date | 1647-10-25 | 待写入 |
| nationality | Italy（Grand Duchy of Tuscany / Papal States） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / physics / hydrodynamics / optics | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **导师**：Benedetto Castelli（1626–1632）；Bonaventura Cavalieri（学生兼挚友，page.md 明载）
- **学术追随**：Galileo Galilei（1641 任其口述秘书三个月；间接师承）
- **学生**：Vincenzo Viviani
- **通信 / 学术**：Michelangelo Ricci（1644 著名信件）、Raffaello Magiotti、Antonio Nardi（罗马"三头同盟"）
- **论战 / 竞争**：Gilles de Roberval（摆线优先权）；小号无穷悖论之争牵涉 Hobbes
- **雇主/赞助**：托斯卡纳大公 Ferdinando II de' Medici；教皇 Urban VIII（水利实验）
- **家庭**：父 Gaspare Ruberti（纺织工人）、养子 Alessandro

## 8. 奖项清单

- 无奖项/院士身份记载；荣誉体现为：压强单位 torr、月球环形山 Torricelli、小行星 7437、Torricelli 山脉、植物属 Torricellia、Faenza 雕像（1868）

## 9. 机构清单

- 教育：Jesuit College（1624–1626，可能在 Faenza）；罗马师从 Benedetto Castelli（无大学注册证据）
- 任职：大公数学家 + 比萨大学数学讲席（1642–1647，Ferdinando II de' Medici 任命，接续伽利略）

## 10. 终审清单

- [ ] 生卒 1608-10-15 / 1647-10-25，享年 39，出生地 Rome（祖籍 Faenza）、逝世地 Florence
- [ ] 国籍用「意大利」，历史政权注明教皇国/托斯卡纳大公国
- [ ] "师从 Castelli、无大学注册证据"表述准确，弃用 Roman College
- [ ] 气压计"首次造出持久真空"表述准确，笛卡尔/帕斯卡相关限定语在位
- [ ] 托里拆利定律用 page.md 形式或注明 v=√(2gh) 另有来源
- [ ] 摆线争议"独立完成（似是）、争议至死未决"表述准确
- [ ] 死因"发热，最可能伤寒"表述准确
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Evangelista_Torricelli/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：从 Wikimedia Commons 下载 Lorenzo Lippi c.1647 肖像，失败则用《Lezioni》扉页肖像/装饰圆占位
- [ ] **国籍**：封面顶部徽章明示意大利
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如 "Noi viviamo sommersi nel fondo d'un pelago d'aria"）——忠实转述，勿造伪引语
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（卡瓦列里 / 梅森）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
