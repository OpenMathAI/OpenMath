# Richard R. Ernst（理查德·恩斯特）立传提示词

> qid=Q122272 · 1933-08-14 – 2021-06-04 · 瑞士物理化学家 · 20 世纪 · 诺贝尔化学奖（1991，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Richard_R._Ernst/`（page.md + metadata.json）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。肖像用 Wikipedia "Ernst in the 1980s" 或 UNESCO 2011 帧；下载失败用装饰圆占位并如实标注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{wave-square}\enspace把谱仪变成万花筒\enspace·\enspace 瑞士`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、全名（Richard Robert Ernst）、国籍、出生地/去世地、教育、博士导师（双导师）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「脉冲 / 频谱」母题——离散圆点如时域脉冲经傅里叶变换铺成频谱。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 时域 FID $\xrightarrow{\text{Fourier}}$ 频域谱；一维 NMR → 二维 NMR。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Richard Robert Ernst（中文惯称：理查德·恩斯特）
- **生卒**：1933-08-14 生于瑞士温特图尔（Winterthur）→ 2021-06-04 逝于温特图尔，享年 87（生于斯逝于斯，同一座城）
- **国籍**：Switzerland（瑞士）
- **身份**：物理化学家；ETH 苏黎世物理化学实验室主任（退休前）；诺奖得主
- **家庭**：Robert Ernst 与 Irma Ernst-Brunner（née Brunner）三个孩子中最年长；祖父是商人，1898 年所建宅邸即其成长之家
- **配偶与子女**：娶 Magdalena Kielholz，直至他去世；三个孩子：Anna Magdalena、Katharina Elisabeth、Hans-Martin Walter
- **爱好**：大提琴（少年时认真考虑过当作曲家）；喜艺术，尤其藏族唐卡——用科学方法分析唐卡颜料的地理来源与年代
- **教育轨迹**：13 岁偶然翻出已故叔父（冶金工程师）的一箱化学品，把能想到的反应都试了一遍，有的爆炸把父母吓坏 → 入 ETH 苏黎世学化学
- **博士**：1962 年 ETH 苏黎世物理化学博士（此前 1957 年获文凭 "Diplomierter Ingenieur Chemiker"，服兵役间隔）；导师**双导师 Hans H. Günthard 与 Hans Primas**；论文《Kernresonanz-Spektroskopie mit stochastischen Hochfrequenzfeldern》（随机高频场下的核磁共振波谱学）
- **研究领域**：物理化学——傅里叶变换 NMR、二维 NMR、脉冲技术、磁共振成像、生物大分子溶液结构

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **叔父的化学品箱（约 1946）**：13 岁翻出已故冶金工程师叔父的化学品箱，把能想到的反应试了个遍——有些爆炸把父母吓坏；化学的第一次触碰是爆炸性的。
2. **大提琴与作曲梦**：少年时代沉醉音乐，一度认真考虑以作曲为业——"工具匠"式的精度与艺术家的感性在他身上并存。
3. **失望的课程与自学（1953–1957）**：对 ETH 课程内容失望，课余自学量子力学与热力学；1957 年以 "Diplomierter Ingenieur Chemiker" 文凭毕业。
4. **随机高频场博士论文（1962）**：在 Günthard 与 Primas 双导师门下做核磁共振波谱学——为日后的脉冲革命埋下伏笔。
5. **Varian 岁月（1963–1968）**：赴美国 Varian Associates 任科学家，**发明傅里叶变换 NMR 与噪声去耦**等一系列方法——把灵敏度和速度都提高几个量级。
6. **回归 ETH（1968–1976）**：1968 年回 ETH 任讲师，1970 助理教授、1972 副教授、1976 起物理化学正教授。
7. **二维 NMR（1970s）**：发展二维核磁共振与一系列新型脉冲技术——把一维谱变成可分辨分子全貌的"万花筒"。
8. **"工具匠"（tool-maker）**：他谦逊地自称"工具匠"而非科学家——为化学与医学锻造最好的观测工具。
9. **物理化学实验室主任**：领导磁共振波谱学研究组，任 ETH 物理化学实验室主任；1998 年退休。
10. **与 Wüthrich 的合作**：与 Kurt Wüthrich 合作进行溶液中生物大分子的 NMR 结构测定；并参与医学磁共振断层成像（MRI）的发展与分子内动力学研究。
11. **万米高空听到诺奖（1991）**：飞越大西洋的航班上得知获奖——受邀进入驾驶舱，用无线电与诺贝尔委员会通话，听到理由 "for his contributions to the development of the methodology of high resolution nuclear magnetic resonance (NMR) spectroscopy"。
12. **荣誉的国际半径**：ForMemRS（1993）；爱沙尼亚科学院（2002）、美国 NAS、伦敦皇家学会、德国利奥波第那、俄罗斯科学院、韩国科学技术翰林院、孟加拉科学院外籍院士/外籍会士；Kirkwood Medal（1989）。
13. **科学与和平**：纪录片《Science Plus Dharma Equals Social Responsibility》（2009 Bel Air 电影节世界首映）记录其家乡与信仰;2022 年温特图尔 Cameo 影院再映其传记纪录片——摄制于去世前数月。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（紫罗兰深紫 deepviolet） | `#372A75` | 频谱深处的秩序——共振与相干（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（FT-NMR badgeFT） | `#2E5A9E` | 蓝傅里叶变换 / 脉冲序列 |
| 分类色 2（2D NMR badge2D） | `#1B7A43` | 绿二维谱 / NOE / ECCO |
| 分类色 3（MRI 与大分子 badgeMRI） | `#B0413E` | 绯红医学成像 / 生物大分子结构 |
| 分类色 4（音乐与唐卡 badgeArt） | `#D97B29` | 琥珀大提琴 / 藏族唐卡科学分析 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「时域脉冲 → 频域谱线」的变换之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Pathfinder** — Ghostwriter Music（Daniel Beijbom，录于布达佩斯；文件：`music_audio/inspiring-electronic/23-GiwYLGgJw7w-Ghostwriter Music - Pathfinder (Composed by Daniel Beijbom - Recorded in Budapest).wav`；不要复制 wav 文件）
- **风格**：开阔行进 / 探路者气质 / 精密而向上
- **匹配理由**：
  - "探路者" 直指其人——FT-NMR、2D NMR、脉冲技术，每一步都是无人走过的路径
  - "精密" 匹配其"工具匠"气质——不标榜理论雄心，只造最好的仪器与方法
  - "开阔行进" 匹配其跨洋轨迹——温特图尔 → 苏黎世 → 加州 Varian → 万米高空接获斯德哥尔摩来电
- **时长**：以曲文件实际时长为准，ffmpeg `-shortest` 自动对齐 15 页

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 把谱仪变成万花筒 / Richard R. Ernst 1933–2021 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/全名/国籍/教育/双博士导师/配偶子女/出生地/去世地/领域/荣誉）
03  恩斯特的一生 — Sanger 式时间线（10 节点：1933→1957→1962→1963→1968→1976→1991→1993→1998→2021）
04  早年：化学品箱与大提琴 (1933–1953) — 表格「时间|事件|结果」
05  ETH 求学与自学 (1953–1962) — 表格「时间|事件|结果」（失望课程→自学量子力学/热力学→随机场博士论文）
06  Varian 与傅里叶变换 NMR (1963–1968) — 表格「问题|方法|结果」+ 公式框：时域 FID →Fourier→ 频域谱
07  二维 NMR 与脉冲技术 (1970s–1980s) — 表格「挑战|方法|结果」+ 公式框：一维 → 二维（演化期 t1 × 检测期 t2）
08  与 Wüthrich 的合作及 MRI — 表格「对象|协作|意义」（生物大分子溶液结构 / 医学磁共振断层成像）
09  1991 诺贝尔化学奖 — 独享；官方理由 "for his contributions to the development of the methodology of high resolution nuclear magnetic resonance (NMR) spectroscopy"；万米高空接奖叙事
10  "工具匠"的谦逊 — 引语框 + 表格「自称|实绩|反差」
11  荣誉与学会 — Sanger 式「类别|代表|意义」表格（Kirkwood 1989 / Marcel Benoist / Nobel+Wolf+Horwitz 1991 / ForMemRS 1993 / Reichstein 2000 / 罗马尼亚之星 2004）
12  音乐、唐卡与和平 — 表格「爱好|科学介入|意义」（作曲梦 / 唐卡颜料科学断代 / 纪录片）
13  遗产：共振改变世界 — 四分类遗产盒（化学谱学 / 医学成像 / 结构生物学 / 仪器哲学）
14  结尾 — 「他给世界造了更好的耳朵，去听分子的振动。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1991 诺奖口径 | **独享**，官方理由 "for his contributions to the development of the methodology of high resolution nuclear magnetic resonance (NMR) spectroscopy"——勿写"发明 MRI"（其贡献是 NMR 方法学，MRI 是应用之一） |
| Marcel Benoist Prize 年份 | **infobox 作 1985、正文作 1986 两说并存**——Beamer 取正文 1986 并加注 "infobox 作 1985"，勿只写其一 |
| FT-NMR 发明地 | 在 **Varian Associates**（1963 年入职后）发明——勿写"在 ETH 发明"；回 ETH（1968）后发展的是 2D NMR 与脉冲技术 |
| 双博士导师 | **Hans H. Günthard 与 Hans Primas 并列**——勿只写一人 |
| 博士论文题目 | 德文题《Kernresonanz-Spektroskopie mit stochastischen Hochfrequenzfeldern》（随机高频场），勿意译成"傅里叶变换 NMR" |
| 学位年份 | 文凭 1957（"Diplomierter Ingenieur Chemiker"）、博士 1962、中间服兵役——年份勿串 |
| Wüthrich 关系 | 页面作 "collaborating with Professor Kurt Wüthrich"——**合作者（colleague）**，非师生；Wüthrich 2002 年诺奖但**本页面未提**，勿写其诺奖信息 |
| 博士生 | infobox Doctoral students 仅 **Marc Baldus** 一人；metadata.json 的 doctoral_student（Christian Radloff 与 Q136681263）页面无载——**按页面口径只入库 Marc Baldus** |
| 获奖场景 | "在飞越大西洋的航班上得知获奖，受邀进驾驶舱用无线电与委员会通话"——页面明载可写；勿加"正在领奖途中"等发挥 |
| "tool-maker" | 他自称 "tool-maker"（工具匠）——页面原文明载，可作直接引语（须半角引号）；勿扩写成"自嘲只会造仪器" |
| 子女名字 | Anna Magdalena、Katharina Elisabeth、Hans-Martin Walter 三人——照页面拼写；妻子 Magdalena Kielholz "until his death"（无离婚表述） |
| 出生/去世同城 | 生于温特图尔、逝于温特图尔（2021-06-04，享年 87）——勿写"逝于苏黎世" |
| 奖项重复 | Nobel、Wolf、Horwitz 三奖同年 **1991**——勿误写 Wolf/Horwitz 为 1989；Kirkwood Medal 1989 |
| 引语红线 | 直接引语仅两处：①获奖理由官方句 ②"tool-maker" 自称；其余一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q122272 | ✅ |
| name_zh | 理查德·恩斯特 | ✅ |
| name_en | Richard R. Ernst | ✅ |
| birth_date | 1933-08-14 | ✅ |
| death_date | 2021-06-04 | ✅ |
| nationality | Switzerland | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | physical chemistry（person_field 细分见下表） | ✅ |
| has_biography | false（立传 Beamer 完成后置 1） | ✅ |

person_field 细分（rank 表）：

| field | rank | 说明 |
|---|---|---|
| physical chemistry | 0 | metadata field_of_work 第二项/主研方向 |
| NMR spectroscopy | 1 | FT-NMR / 2D NMR / 脉冲技术 |
| magnetic resonance imaging | 2 | 医学磁共振断层成像参与发展 |
| structural biology | 3 | 与 Wüthrich 合作溶液大分子结构 |

## 7. 社会关系入库清单

**红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hans H. Günthard | 师→生（博士导师之一） | ETH 苏黎世，1962 博士 |
| advisor-student | Hans Primas | 师→生（博士导师之一） | ETH 苏黎世，双导师并列 |
| colleague | Kurt Wüthrich | 无向 | 合作进行溶液中生物大分子的 NMR 结构测定 |
| spouse | Magdalena Kielholz | 无向 | 结婚直至恩斯特去世；三子女 Anna Magdalena / Katharina Elisabeth / Hans-Martin Walter |
| advisor-student | Marc Baldus | Ernst→学生 | infobox Doctoral students 明载 |

> **禁入库名单**：Christian Radloff 与 Q136681263（仅 metadata.json doctoral_student 有载，页面无载——**禁入**）；Varian Associates、ETH 等机构非人际；纪录片导演 Carlo Burton、Lukas Schwarzenbacher 等不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1991，独享）
- John Gamble Kirkwood Medal（1989）
- Marcel Benoist Prize（正文 1986 / infobox 1985，两说并存须注记）
- Wolf Prize in Chemistry（1991）
- Louisa Gross Horwitz Prize（Columbia，1991）
- Tadeus Reichstein Medal（2000）
- Order of the Star of Romania, Commander（2004）
- Foreign Member of the Royal Society, ForMemRS（1993）
- 外籍会士/院士：美国 NAS、伦敦皇家学会、爱沙尼亚科学院（2002）、德国 Leopoldina、俄罗斯科学院、韩国科学技术翰林院、孟加拉科学院
- 荣誉博士：慕尼黑工业大学、EPF 洛桑、苏黎世大学、安特卫普大学、 Babeș-Bolyai 大学、蒙彼利埃大学

## 9. 机构清单

- 教育：ETH Zurich（1957 文凭；1962 博士，物理化学）
- 任职：Varian Associates（1963–1968，科学家；发明 FT-NMR 与噪声去耦）、ETH Zurich（1968 讲师 → 1970 助理教授 → 1972 副教授 → 1976 物理化学正教授 → 物理化学实验室主任 → 1998 退休）
- 纪录片：Science Plus Dharma Equals Social Responsibility（2009 世界首映）；2022 温特图尔 Cameo 影院传记纪录片

## 10. 终审清单

- [ ] 生卒 1933-08-14 / 2021-06-04，享年 87；温特图尔生于斯逝于斯
- [ ] 1991 独享；获奖理由官方句准确
- [ ] FT-NMR 在 Varian 发明；2D NMR 与脉冲技术在 ETH
- [ ] 双博士导师 Günthard + Primas；博士论文为随机高频场主题
- [ ] Marcel Benoist Prize 1985/1986 两说注记处理
- [ ] Wüthrich=合作者（非师生）；博士生仅 Marc Baldus；Radloff 禁入
- [ ] 荣誉年份逐项对照 infobox 与正文两处清单
- [ ] 引语仅获奖理由句与 "tool-maker"，均可回溯 page.md 原文
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Richard_R._Ernst/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：Wikipedia "Ernst in the 1980s" 或 UNESCO 2011 肖像，或装饰圆占位（如实标注）
- [ ] 国籍：封面顶部明示 瑞士
- [ ] 引语核对：获奖理由句与 "tool-maker" 须在 page.md 原文找到
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger）对齐

---

> **名单状态**：本文件由 chem-batch-21 执行生成；`chemist/generate_20th_century_list.py` 状态列由主控统一收尾，本批次不改动。
