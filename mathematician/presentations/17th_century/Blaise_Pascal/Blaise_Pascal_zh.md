# Blaise Pascal（布莱兹·帕斯卡）立传提示词

> qid=Q1290 · 1623-06-19 – 1662-08-19 · 法国数学家/物理学家/哲学家 · 17 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/17th_century/pages/Blaise_Pascal/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。使用 images.txt 中的正装肖像（`Blaise_Pascal_2.jpg`，下载至 `images/pascal_portrait.jpg`）；注意 infobox 肖像标注 "c. 1691" 系**死后绘像**，slide 勿标"生前写实"。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、国籍、出生地、父亲职业、教育（家庭教育）、信仰、核心领域。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），母题呼应「帕斯卡三角 / 算术三角形」的递归之美。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 0.5 模板机制（执行立传前必读）

> 黄金参照 `Johann_Bernoulli/Johann_Bernoulli_zh.tex` 逐帧改写；机械要点（14 帧结构 / 共享封面 `\input{../../cover/openmath_page.tex}` / Makefile 复制改 MAIN / 肖像下载与装饰圆占位 / `make distclean && make` 编译循环 / 已知陷阱）见 **`17th_century/TEMPLATE_GUIDE.md`**。

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Blaise Pascal（布莱兹·帕斯卡）
- **生卒**：1623-06-19 生于 Clermont-Ferrand（奥弗涅，France）→ 1662-08-19 逝于巴黎，享年 39；葬于 Saint-Étienne-du-Mont 教堂墓地
- **国籍**：法国（Kingdom of France）
- **身份**：数学家、物理学家、发明家、哲学家、神学家、作家（"French mathematician, physicist, inventor, philosopher, and Catholic writer"）
- **家庭**：父 Étienne Pascal（鲁昂收税官、穿袍贵族、业余数学家，1631 年卖官得 65,665 里弗尔）；母 Antoinette Begon（帕斯卡 3 岁丧母，父未再娶）；妹 Jacqueline Pascal（后入 Port-Royal 冉森派修道院）、姐 Gilberte Périer；姐夫 Florin Périer（执行 Puy de Dôme 实验）
- **宗教**：天主教徒、1646 年"第一次皈依"后倾向冉森派（Jansenism）；1654-11-23 深夜神秘体验（Memorial 缝入衣襟）
- **教育轨迹**：★ **未上过任何学校/大学**——父 Étienne 亲自在家教育；12 岁以炭条在瓷砖地板上独立重推欧几里得《几何原本》前 32 命题，父亲这才给他一本《几何原本》
- ★ metadata 的 doctoral_advisor: ["Marin Mersenne"] 与 page.md 冲突——page.md 只说帕斯卡把《圆锥曲线论》寄给梅森，**弃用"导师"说法**

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **帕斯卡定理（神秘六边形，1639，16 岁）**：内接于圆锥曲线的六边形，三组对边交点共线（Pascal line）；笛卡尔不肯相信出自少年之手——"René Descartes was convinced that Pascal's father had written it"。
2. **机械计算器 Pascaline（1642）**：为减轻父亲税务计算而造，可做加减法——"one of the first two inventors of the mechanical calculator"；十年造 20 台成品（设计约 50 台）。
3. **概率论共同奠基（1654）**：与费马就分赌注问题通信，"from that collaboration was born the mathematical theory of probability"；期望值概念由此产生。
4. **帕斯卡三角**：《Traité du triangle arithmétique》递归定义 `t_mn = t_{m−1,n} + t_{m,n−1}`，并给出显式公式。
5. **数学归纳法的明确表述**：同一论著中 "Pascal gave an explicit statement of the principle of mathematical induction"。
6. **帕斯卡定律与流体力学**：静水压强只取决于高度差而非液重；发明水压机（hydraulic press）与注射器。
7. **真空研究**：1647 《新真空实验》；1648-09-19 Puy de Dôme 实验（山脚→山顶水银柱下降）证明大气压随高度变化，反驳"自然厌恶真空"。
8. **摆线研究（1658–59）**：以"牙痛消失为上天之兆"八日完成论文；举办摆线竞赛（沃利斯与 Lalouvère 的投稿均未获评通过）。
9. **可证伪思想先声**（致 Étienne Noël）："if it leads to something contrary to a single one of the phenomena, that suffices to establish its falsity."
10. **《省书信》（1656–57）**：笔名 Louis de Montalte，抨击耶稣会道德神学；1660 年被路易十四下令焚书。
11. **帕斯卡赌注**：《思想录》中的信仰概率论证。
12. **公共政策发明**：carrosses à cinq sols（1662）——"credited as the inventor of modern public transportation"（固定线路/票价/无人也发车）。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（冉森灰蓝） | `#465B7A` | 信仰与理性的张力 |
| 强调色（思想金） | `#C9A227` | 《思想录》/ 帕斯卡三角 |
| 分类色 1（概率 — 靛蓝） | `#4C5FD5` | 帕斯卡三角 / 与费马通信 |
| 分类色 2（流体与真空 — 青绿） | `#0E7C7B` | 帕斯卡定律 / Puy de Dôme |
| 分类色 3（计算与几何 — 琥珀） | `#E07B30` | Pascaline / 摆线 |
| 分类色 4（信仰与文学 — 玫红） | `#B76E79` | 《省书信》/ 帕斯卡赌注 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），母题呼应「帕斯卡三角 / 递归数塔」之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**巴洛克典雅 / 深邃忧伤**（39 岁陨落的天才、信仰与理性之交）
- **匹配理由**：
  - 帕斯卡兼具数学冷峻与神秘主义炽热——需**深邃、内敛**的配乐
  - "忧伤" 匹配其常年病痛与 39 岁早逝
  - "典雅" 匹配其法国贵族出身与巴洛克时代
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：沿用系列曲目 **Timeless**（本系列已统一采用，保持一致）
  - 备选：巴洛克 / 法国 17 世纪风格曲目（库普兰气质）
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐梅森/伯努利模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「概率与真空 · 会思考的芦苇」+ 布莱兹·帕斯卡 1623–1662 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 国籍 / 出生地 / 父亲职业 / 教育 / 信仰 / 核心领域）
3. **帕斯卡的一生：时间线**（`\timelineslide`）：1623 出生 → 1631 迁巴黎（家庭教育）→ 1639 神秘六边形 → 1642 Pascaline → 1646 皈依冉森派 → 1648 Puy de Dôme → 1654 与费马通信 / Memorial → 1656–57 《省书信》→ 1658 摆线 → 1662 去世
4. **早年与教育**（`\earlyslide`）：家庭教育、12 岁瓷砖地板上的欧几里得、父 Étienne 的"先几何后拉丁"教学
5. **帕斯卡定理与少年成名**（核心贡献页，表格 + 公式框）：神秘六边形、笛卡尔的质疑、梅森担保
6. **Pascaline**（核心贡献页，表格 + 公式框）：1642 机械计算器、"first two inventors"、商业失败如实写
7. **帕斯卡三角与数学归纳法**（核心贡献页，表格 + 公式框）：`t_mn = t_{m−1,n} + t_{m,n−1}`、归纳原理明确表述
8. **概率论：与费马的通信**（核心贡献页，表格 + 公式框）：1654 分赌注问题、期望值诞生
9. **真空与 Puy de Dôme**（核心贡献页，表格 + 公式框）：1647 新实验、1648 姐夫执行的高山实验
10. **帕斯卡定律与水压机**（核心贡献页，表格 + 公式框）：压强与高度差、水压机/注射器
11. **摆线的八日奇迹**（核心贡献页，表格 + 公式框）：1658 牙痛之兆、摆线竞赛
12. **《省书信》与帕斯卡赌注**（表格）：笔名 Louis de Montalte、焚书令、《思想录》
13. **身后与纪念**（表格）：压强单位 pascal (Pa)、Université Blaise Pascal、Pascal 编程语言 / Nvidia Pascal 微架构、500 法郎纸币、小行星 4500
14. **终章**：39 岁、"人是会思想的芦苇"的历史定位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **向瑞典女王"1632 年"赠计算器**：page.md 原句 "He also presented the first mechanical calculator to Christina, Queen of Sweden in 1632." 是**明显的年代错误**（帕斯卡 1623 年才出生，Pascaline 1642 年才造出）——切勿引用此句。
- **生卒**：1623-06-19 / 1662-08-19，享年 39；遗言 "May God never abandon me"（原文有载，可用）；死因未确证——"speculation focuses on tuberculosis, stomach cancer, or a combination of the two"，勿写死。
- **帕斯卡木桶实验**：原文明确标注 **apocryphal**（真伪存疑）——引用需注明。
- **马车车祸与 Memorial 的因果**："The story of a carriage accident as having led to the experience described in the Memorial is disputed by some scholars."——勿写成定论。
- **《思想录》出版年页内自相矛盾**：正文 1669 / Works 清单 1670——选一并注明。
- **概率论并非由他二人建成**：原文 "Pascal and Fermat, though doing important early work in probability theory, did not develop the field very far. Christiaan Huygens... wrote the first book on the subject."——表述"共同奠基"，勿写"创立了概率论"；惠更斯写第一部概率论著作。
- **Pascaline 商业失败**："failed to be a great commercial success... became little more than a toy, and a status symbol"——如实呈现，勿写"轰动欧洲"。
- **摆线竞赛没有胜者**："neither of the two submissions (by John Wallis and Antoine de Lalouvère) were judged to be adequate"；Roberval 声称早知证明——如实呈现。
- **metadata 冲突**：doctoral_advisor Marin Mersenne **弃用**（page.md 只说寄论文给梅森）。
- **肖像**：infobox 肖像 "c. 1691" 系死后绘像——勿标生前写实。
- **称号**："人是会思想的芦苇"（"Man is only a reed... but he is a thinking reed"，《思想录》No. 200）为 verbatim 引语可用。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q1290 | 待写入 |
| name_zh | 布莱兹·帕斯卡 | 待写入 |
| name_en | Blaise Pascal | 待写入 |
| birth_date | 1623-06-19 | 待写入 |
| death_date | 1662-08-19 | 待写入 |
| nationality | France | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / probability / physics / hydrostatics / philosophy | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **思想引路人**：Gérard Desargues（《圆锥曲线论》的直接启发）
- **学术中介**：Marin Mersenne（第一篇论文的接收人，非导师）
- **合作者**：Pierre de Fermat（1654 概率通信，"joint founders of probability theory"）；Florin Périer（姐夫，Puy de Dôme 实验执行者）
- **承其衣钵**：Christiaan Huygens（"learning of the subject from the correspondence of Pascal and Fermat, wrote the first book on the subject"）
- **论战 / 竞争**：René Descartes（怀疑其少年论文、哲学交锋）、Étienne Noël（真空之争）、耶稣会（《省书信》目标）、Louis XIV（1660 焚书令）、Gilles de Roberval（摆线竞赛评委之争）
- **家庭**：父 Étienne Pascal（收税官/业余数学家）、妹 Jacqueline Pascal（冉森派）、姐 Gilberte Périer

## 8. 奖项清单

- **生前无任何奖项/院士身份记载**（法兰西科学院 1666 年才成立，其逝于 1662）；身后纪念：压强单位 pascal、Université Blaise Pascal、Pascal Chairs、编程语言 Pascal、Nvidia Pascal 微架构、小行星 4500 Pascal、500 法郎纸币、教皇方济各宗座牧函（2023）

## 9. 机构清单

- 教育：无学校/大学——完全由父亲在家教育
- 任职：无正式职务（早年协助父亲鲁昂税务计算；后居巴黎从事研究与写作）
- 关联：Port-Royal 冉森派团体（妹 Jacqueline 入会，帕斯卡与之关系密切但未入会）

## 10. 终审清单

- [ ] 生卒 1623-06-19 / 1662-08-19，享年 39，出生地 Clermont-Ferrand、逝世地 Paris
- [ ] 国籍用「法国」
- [ ] "1632 年赠女王计算器"年代错误勿引用；Pascaline 1642
- [ ] "与费马共同奠基概率论、惠更斯写成第一部概率论著作"表述准确
- [ ] 木桶实验 apocryphal、车祸 Memorial 因果有争议——限定语在位
- [ ] Pascaline 商业失败如实呈现
- [ ] 弃用 metadata 的 doctoral_advisor Mersenne
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Blaise_Pascal/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 images.txt 的 `Blaise_Pascal_2.jpg`（下载至 `images/`），注明约 1691 死后绘像
- [ ] **国籍**：封面顶部徽章明示法国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如 "Man is only a reed..."、"May God never abandon me"）——忠实转述，勿造伪引语
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（笛卡尔 / 费马 / 惠更斯）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
