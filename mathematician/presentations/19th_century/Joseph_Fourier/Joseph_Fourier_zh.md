# Joseph Fourier（约瑟夫·傅里叶）立传提示词

> qid=Q8772 · 1768-03-21 – 1830-05-16 · 法国数学家、物理学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Joseph_Fourier/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「波动 / 叠加」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Jean-Baptiste Joseph Fourier（中文惯称：傅里叶）
- **生卒**：1768-03-21 生于法国欧塞尔（Auxerre，勃艮第，法兰西王国）→ 1830-05-16 逝于巴黎，享年 62
- **国籍**：France（法国，出生时属法兰西王国）
- **身份**：数学家、物理学家（傅里叶级数/变换、热传导方程、温室效应发现者）
- **家庭**：裁缝之子，9 岁父母双亡成为孤儿；终身未婚
- **教育轨迹**：
  - 由欧塞尔主教推荐，入本笃会圣马可修道院（Convent of St. Mark）受教
  - 入读 École Normale Supérieure（高等师范学校）
  - 1795 年任教于 École Normale，后接替拉格朗日在 École Polytechnique 任教
- **导师**：Jean-Baptiste Biot、Joseph-Louis Lagrange
- **研究领域**：数学分析、傅里叶级数、数学物理、热传导

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **傅里叶级数（最著名成果）**：提出任意函数（连续或不连续）可展开为正弦级数——虽未加条件严格化（严格化由 Dirichlet 完成），但"某些不连续函数是无穷级数之和"的洞见是突破性发现，奠定傅里叶分析与调和分析基础。
2. **傅里叶变换**：以他命名的变换，是信号处理、物理、工程的核心工具。
3. **热传导方程 / 《热的解析理论》**：1822 年出版《Théorie analytique de la chaleur》，提出热传导的偏微分方程（最典型的抛物型 PDE），并贡献**量纲分析**（dimensional analysis / 量纲齐次性）思想。
4. **傅里叶热传导定律（Fourier's law of conduction）**：热流与温度梯度成正比。
5. **温室效应的发现**：1824/1827 年计算地球温度应远低于实际，提出大气可能起"绝缘体"作用——被公认为温室效应的首次提出（虽未命名，且误判星际辐射贡献）。
6. **多项式实根定理**：年轻时给出笛卡尔符号法则的归纳证明；傅里叶实根定理（1820），与 Budan 定理互为推论，Sturm 1829 给出完整解。
7. **贝塞尔函数**：在圆柱热扩散讨论中，早于 Bessel 数年系统讨论贝塞尔函数；启发了 Sturm–Liouville 理论。
8. **埃及远征**：1798 年随拿破仑远征埃及，任 Institut d'Égypte 秘书，组织军需工场，参与《Description de l'Égypte》（埃及描述）巨著。
9. **行政生涯**：1801 年拿破仑任命其为伊泽尔省（Isère）省长（格勒诺布尔），在任期间开始热传导实验；1822 年继 Delambre 任法国科学院常务秘书。
10. **身后荣誉**：名字刻于埃菲尔铁塔 72 位法国科学家之一；格勒诺布尔约瑟夫·傅里叶大学以其命名；葬于拉雪兹神父公墓（埃及风格墓碑）。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

> ★ 傅里叶是 19 世纪立传系列中**唯一以"热"为核心主题**的数学家，故破例采用**暖色主色**，与高斯、柯西、伽罗瓦、阿贝尔、魏尔斯特拉斯的深蓝系形成鲜明区分，呼应其热传导 / 温度 / 波动叠加的气质。

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（热力绛红） | `#8C2F39` | 热 / 温度 / 法兰西古典 |
| 强调色（热力琥珀） | `#E07B30` | 热传导 / 温度 |
| 分类色 1（傅里叶级数 — 靛蓝） | `#4C5FD5` | 级数 / 变换 |
| 分类色 2（热传导方程 — 橙红） | `#C9481C` | 热方程 / 热传导定律 |
| 分类色 3（温室效应 — 青绿） | `#0E7C7B` | 温室效应 / 地球温度 |
| 分类色 4（生平 / 遗产 — 石板灰） | `#55606E` | 埃及远征 / 行政生涯 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「正弦波的叠加 / 周期格」的视觉语言（傅里叶级数即正弦波叠加）。
- **tex 配色变量命名建议**：`heatred`（主色）、`heatamber`（强调色）、`badgeSeries` / `badgeHeat` / `badgeClimate` / `badgeLegacy`（分类色）、`seriespanel` / `heatpanel` / `climatepanel` 等面板底色。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **风格定调**：**古典庄重 / 宏大**（法国大革命前后学者的严谨与宏大）
- **匹配理由**：
  - 傅里叶横跨数学、物理、行政、埃及远征，人生宏大而理性——需**庄重、古典、宏大**的配乐
  - "波动叠加" 呼应其傅里叶级数——可考虑有起伏、铺陈感强的曲目
  - "热与温度" 呼应其热传导与温室效应——温暖而有厚度的音色
- **已选定曲目（✅ 定稿）**：`Timeless`（沉稳 / 纪录片 / 庄重）
  - 本地源文件：`music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav`
  - 项目当前统一背景音乐风格：高斯、魏尔斯特拉斯、伽罗瓦、阿贝尔均用 Timeless
  - 时长 2 分 8 秒，远 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐
- **接入方式**：软链接到立传目录（不复制大文件）：

  ```bash
  cd presentations/19th_century/Joseph_Fourier
  ln -sf /Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav ./bgm.wav
  ```

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「傅里叶级数 · 热的解析理论」+ 傅里叶 1768–1830 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：傅里叶级数/变换 / 热传导方程 / 温室效应 / 多项式实根 四分类
4. **早年与教育**（1768–1795）：裁缝之子、孤儿、本笃会教育、École Normale、接替拉格朗日
5. **傅里叶级数与傅里叶分析**（核心贡献页）：任意函数展开、Dirichlet 严格化、傅里叶变换
6. **《热的解析理论》与热传导方程**（核心贡献页）：1822 著作、热方程、量纲分析、傅里叶定律
7. **贝塞尔函数与 Sturm–Liouville 理论**：圆柱热扩散、早于 Bessel 的讨论
8. **温室效应的发现**（1824/1827）：地球温度计算、大气绝缘体假说、de Saussure 实验
9. **埃及远征与行政生涯**（1798–1822）：Institut d'Égypte、伊泽尔省长、《埃及描述》
10. **多项式实根定理**：笛卡尔符号法则、傅里叶定理（1820）、Budan、Sturm
11. **荣誉与身后**：埃菲尔塔 72 名、拉雪兹公墓、傅里叶大学、终身未婚
12. **终章**：62 岁、从热到波的遗产与历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **傅里叶级数"任意函数展开"**：傅里叶声称"任意函数（含不连续）可展开为正弦级数"，但**不加条件不严格成立**——严格收敛条件由 **Dirichlet** 首次给出。勿写傅里叶完成了严格证明。
- **导师生卒**：导师 Lagrange、Biot；学生 Dirichlet、Navier、Plana。傅里叶本人未获博士学位（早期法国科学院体系）。
- **傅里叶变换归属**：傅里叶变换是后人以他命名并系统化，傅里叶本人主要贡献是级数展开——勿写"傅里叶发明了现代傅里叶变换的全部理论"。
- **温室效应**：傅里叶是**首次提出大气可能起保温（绝缘）作用**，但未使用"温室效应"一词，且**误判**了星际辐射的贡献（实际差额来自地球内部放射热）——表述为"首次提出温室效应概念，但机制判断有误"。
- **贝塞尔函数**：傅里叶**早于 Bessel 数年**系统讨论（在圆柱热扩散中），但该函数以 Bessel 命名——勿写傅里叶命名了贝塞尔函数。
- **Sturm–Liouville 理论**：傅里叶的圆柱热扩散工作**启发**了 Liouville 与 Sturm 发展 Sturm–Liouville 理论——是"启发"而非"共同创立"。
- **埃及远征**：随拿破仑远征是**科学顾问**身份（Institut d'Égypte 秘书），参与《Description de l'Égypte》——勿夸大其军事角色。
- **行政职务**：伊泽尔省省长是拿破仑任命（原文引用拿破仑的话），虽非数学工作但体现其人生广度——如实写。
- **生卒**：1768-03-21 / 1830-05-16，享年 62；死亡前有心脏动脉瘤，1830-05-04 摔伤加重病情，05-16 去世。
- **国籍表述**：封面顶部用「法国」作为现代对应（出生时属法兰西王国）。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q8772 | 待写入 |
| name_zh | 傅里叶（或 约瑟夫·傅里叶） | 待写入 |
| name_en | Joseph Fourier | 待写入 |
| birth_date | 1768-03-21 | 待写入 |
| death_date | 1830-05-16 | 待写入 |
| nationality | France | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematical analysis / Fourier series / heat conduction | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **导师**：Jean-Baptiste Biot、Joseph-Louis Lagrange
- **学生**：Peter Gustav Lejeune Dirichlet、Claude-Louis Navier、Giovanni Plana
- **学术相关**：Adrien-Marie Legendre（同期法国数学家，1820 Boilly 水彩漫画同框）、Jean Gaston Darboux（1888 重编《热的解析理论》）
- **受其启发**：Joseph Liouville、Jacques Charles François Sturm（Sturm–Liouville 理论）
- **多项式定理相关**：François Budan（Budan 定理独立提出）、Charles Sturm（1829 完整解）
- **同事 / 上级**：Napoleon Bonaparte（任命其为省长）

## 8. 奖项清单

- Grand prix des sciences mathématiques（法国科学院数学大奖）
- Officer of the Legion of Honour（荣誉军团军官）
- Foreign Member of the Royal Society（英国皇家学会外籍会员）
- 1830 年瑞典皇家科学院外籍会员（Foreign Member of the Royal Swedish Academy of Sciences）
- 埃菲尔铁塔 72 位法国科学家刻名之一（身后纪念）

## 9. 机构清单

- 教育：École Normale Supérieure、Fleury Abbey、Royal Abbey of Saint-Germain d'Auxerre（本笃会）
- 任职：École Normale Supérieure、École Polytechnique、Grenoble Alpes University（格勒诺布尔）、Commission des Sciences et des Arts、French Academy of Sciences（1822 起常务秘书）、Lycée Jacques-Amyot d'Auxerre

## 10. 终审清单

- [ ] 生卒 1768-03-21 / 1830-05-16，享年 62，出生地 Auxerre
- [ ] 傅里叶级数"Dirichlet 严格化"表述准确，勿写傅里叶完成严格证明
- [ ] 傅里叶变换为"后人命名系统化"，表述准确
- [ ] 温室效应"首次提出概念、机制判断有误"表述准确
- [ ] 贝塞尔函数"傅里叶早讨论、以 Bessel 命名"表述准确
- [ ] Sturm–Liouville"受傅里叶启发"表述准确
- [ ] 埃及远征"科学顾问"身份表述准确
- [ ] 国籍用「法国」现代对应
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Joseph_Fourier/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：优先 Wikipedia infobox 照片（`images.txt` 第二张 Fourier_in_his_coat_of_prefect 正式肖像，或第一张 Boilly 漫画）；无则用装饰圆占位
- [ ] **国籍**：封面顶部徽章明示法国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如拿破仑任命省长的话）
- [ ] **编译验证**：一律用 `make distclean && make` 编译（**勿用裸 `xelatex` / `latexmk` / `pdflatex` 命令**）
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受；通过 `make` 输出查看，如 `make 2>&1 | grep -iE 'overfull|underfull'`，勿用裸 `xelatex` 单独编译）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Legendre / Abel / Galois）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
