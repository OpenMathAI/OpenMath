# Friedrich Bergius（弗里德里希·贝尔吉乌斯）立传提示词

> qid=Q76614 · 1884-10-11 – 1949-03-30 · 德国化学家 · 诺贝尔化学奖（1931，与 Carl Bosch 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Friedrich_Bergius/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**严格对齐 Frederick Sanger 立传模板**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金色公式框 + 气泡背景。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 images.txt 仅有 `Friedrich_Bergius_with_wife_1931.jpg`（1931 斯德哥尔摩与妻子合影）：主肖像先查 page.html infobox 原图名，再试 Commons `Special:FilePath/Friedrich Bergius.jpg?width=600` 与 REST API `page/summary`；合影可裁左半身作临时肖像或作插图，注明裁切；全部失败用装饰圆占位，并在 §11 Review 注明。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{industry}\enspace 把煤变成油的化学家\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Friedrich Karl Rudolf Bergius）、国籍、出生地/去世地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「煤的氢化 / 高压釜」母题——离散圆点暗示高压反应中的氢分子。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 褐煤 + H₂ →（高压高温）→ 液态烃。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Friedrich Karl Rudolf Bergius（中文惯称：弗里德里希·贝尔吉乌斯）
- **生卒**：1884-10-11 生于德意志帝国 Breslau（今波兰 Wrocław）附近 → 1949-03-30 逝于阿根廷布宜诺斯艾利斯，享年 64（frontmatter 死亡日期噪声 03-30/03-31 双值，以 infobox 正文 30 March 1949 为准）
- **国籍**：Germany（德国）
- **身份**：化学家（chemist；1931 诺贝尔化学奖共同得主；Bergius 工艺发明人）
- **家庭**：page.md 未载父母姓名；女儿 Renate Burgess（page.md 明载 "Bergius was the father of Renate Burgess"）；1931 年与妻子同赴斯德哥尔摩领奖（合影图证实有妻子，**姓名 page.md 无载——禁写**）
- **教育轨迹**：
  - 入大学前曾在 Mülheim 的 Friedrich Wilhelms 钢铁厂劳动 6 个月
  - 1903 年入 Breslau 大学；1907 年仅用 4 年在莱比锡大学获化学博士（论文：硫酸作溶剂）
- **导师**：Arthur Rudolf Hantzsch（莱比锡博士导师，infobox）；Richard Abegg 为 Other academic advisors
- **研究领域**：化学——高压化学、煤的氢化液化、木材糖化、水热碳化（hydrothermal carbonization）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **布劳斯劳之子（1884）**：生于德意志帝国西里西亚 Breslau（今波兰弗罗茨瓦夫）附近——德国工业心脏地带的一代工程师化学家。
2. **钢铁厂预科（入大学前）**：进大学前在 Mülheim 钢铁厂劳动半年——工业一线的最初体验。
3. **四年速成博士（1903–1907）**：Breslau 起步、莱比锡收官，以「硫酸作溶剂」论文在 Hantzsch 指导下获博士。
4. **卡尔斯鲁厄的洗礼（1909）**：用一学期跟随 Fritz Haber 与 Carl Bosch 参与 Haber–Bosch 工艺开发——高压化学的第一课。
5. **汉诺威与化学动力学（1909）**：同年受邀赴 Leibniz University Hannover 与 Max Bodenstein（化学动力学概念的发展者）共事。
6. **Bergius 工艺专利（1913）**：在授课资格（habilitation）研究期间发展出含碳底物的高压高温化学，取得褐煤氢化制液态烃（合成燃料）的专利——早于闻名的 Fischer–Tropsch 工艺。
7. **Goldschmidt 工厂（1914–1919）**：Theodor Goldschmidt 邀其在 Th. Goldschmidt AG 建工业装置；生产迟至 1919 年（一战结束后燃料需求已回落）才启动。
8. **批评与转折**：Franz Joseph Emil Fischer 的持续批评拖慢进度——一次当面演示后转为支持；技术问题与通胀之下，Bergius 把专利卖给 BASF，由 Carl Bosch 继续推进。
9. **工业规模（二战前）**：多座工厂建成，合成燃料年产能达 400 万吨。
10. **木材糖化与破产边缘**：移居 Heidelberg 改进木材水解制糖工艺，筹划工业规模生产；高成本与技术难题几乎令其破产——执行吏一路追到斯德哥尔摩索取 1931 年诺贝尔奖金。
11. **1931 诺贝尔化学奖**：与 Carl Bosch 共享，官方口径 "in recognition of their contributions to the invention and development of chemical high pressure methods"；诺奖演讲 1932-05-21《Chemical Reactions under High Pressure》。
12. **战火与流亡**：自给自足运动推动建厂，他本人迁居柏林仅边缘参与；在 Bad Gastein 期间实验室与住宅毁于空袭；战后因 IG Farben 合作经历公民权受质疑，先后赴意大利、土耳其、瑞士、西班牙任顾问，最终移居阿根廷任工业部顾问。
13. **终局布宜诺斯艾利斯（1949）**：1949-03-30 逝于布宜诺斯艾利斯，安葬于 La Chacarita 公墓旁的 Cementerio Alemán——一位诺奖得主流亡终老的罕见结局。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深绯红 darkcrimson） | `#8A1E2D` | 煤与火焰、流亡晚景的深沉（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（煤氢化 badgeCoal） | `#5A4632` | 棕褐褐煤氢化 / Bergius 工艺 |
| 分类色 2（高压化学 badgeHighP） | `#8A5A1E` | 赭金高压釜 / Haber–Bosch 洗礼 |
| 分类色 3（木材糖化 badgeWood） | `#2E6B4A` | 绿木材水解 / 水热碳化 |
| 分类色 4（流亡晚年 badgeExile） | `#31456E` | 藏青阿根廷 / 流亡顾问岁月 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「高压氢化 / 反应釜气泡」的意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Ascension** — Cold Cinema（文件 `music_audio/inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav`，不要复制 wav 文件）
- **风格**：史诗 / 管弦 / 升华与跌落的张力
- **匹配理由**：
  - "升华" 与其命运的巨大落差对位——从专利发明到诺奖巅峰，再到破产、流亡、客死他乡
  - "史诗管弦" 匹配煤氢化工业化的宏大尺度（二战前 400 万吨/年产能）
  - 与同批 Bosch 的 Empire Collapse（同为 Cold Cinema 系列）构成 1931 共享得主的姊妹配乐，曲风同源而情绪各异
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐（15 页 × 7 秒 ≈ 105 秒）

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 把煤变成油的化学家 / Friedrich Bergius 1884–1949 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/出生地/去世地/领域/荣誉）
03  贝尔吉乌斯的一生 — 时间线（10 节点：1884→1903→1907→1909→1913→1919→1931→1932→1945→1949）
04  早年：钢铁厂与速成博士 (1884–1907) — 表格「时间|事件|结果」
05  卡尔斯鲁厄与汉诺威 (1909) — 表格「地点|师从|结果」（Haber+Bosch / Bodenstein）
06  Bergius 工艺 (1913) — 表格「问题|方法|结果」+ 公式框：褐煤 + H₂ →（高压高温）→ 液态烃
07  工业化之路 (1914–1919) — 表格「事件|人物|结果」（Goldschmidt 建厂 / F.J.E. Fischer 批评→支持 / 专利售 BASF）
08  木材糖化与破产边缘 — 表格「问题|方法|结果」+ 执行吏追至斯德哥尔摩的细节
09  1931 诺贝尔化学奖 — 表格「人物|贡献|结果」+ 官方获奖理由英文原句
10  战时与空袭 (1939–1945) — 表格「事件|损失|结果」（柏林边缘参与 / Bad Gastein 实验室被毁）
11  流亡与终局 (1946–1949) — 表格「国家|角色|结果」（意/土/瑞/西 → 阿根廷工业部顾问 → 1949 逝世）
12  荣誉与遗产 — 高斯式「类别|代表|意义」表格（Melchett Medal 1934 / Wilhelm Exner Medal 1937 / Liebig Medal / 早于 Fischer–Tropsch）
13  遗产：高压化学的百年回声 — 四分类遗产盒 + 公式框：Bergius 工艺 → 合成燃料 → 水热碳化的现代回声
14  结尾 — 「他在高压之下锻造燃料，也在命运的重压之下走完了后半程。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1931 获奖口径 | 官方措辞 "in recognition of their contributions to the invention and development of chemical high pressure methods"；与 Bosch **共享**——勿写独享 |
| 博士导师冲突 | frontmatter `doctoral_advisor` 写 Richard Abegg，但正文 infobox **Doctoral advisor = Arthur Rudolf Hantzsch**、Abegg 在 **Other academic advisors**——以 infobox 为准 |
| 死亡日期噪声 | frontmatter 死亡日期 1949-03-30 / 03-31 双值——**以 infobox 正文 30 March 1949 为准** |
| Fischer 同名 | 批评其工艺的是 **Franz Joseph Emil Fischer**（Fuel 化学家），**不是** Hermann Emil Fischer / Hans Fischer / Ernst Otto Fischer——勿混 |
| 专利去向 | Bergius 把**煤氢化专利卖给 BASF**，由 Bosch 继续——勿写成卖给 IG Farben 或被抢夺 |
| Fischer–Tropsch | Bergius 工艺发展**早于** Fischer–Tropsch 工艺——可写先后，勿写"竞争失败" |
| 破产与奖金 | 执行吏（bailiff）追至斯德哥尔摩索取诺奖奖金——正文实载，可写；勿扩写金额 |
| 妻子 | 1931 年与妻子同赴斯德哥尔摩（合影证实），**妻子姓名 page.md 无载——禁写**；女儿 Renate Burgess 是唯一明载子女 |
| IG Farben 与战后 | 因战时与 IG Farben 的合作，战后公民权受质疑——客观陈述；他1942 年起在 Bad Gastein、实验室毁于空袭，未直接参与战时生产管理（正文口径 "only marginally involved"） |
| 国籍口径 | 全程 Germany；流亡阿根廷仅是居住与顾问身份——勿写"入籍阿根廷" |
| 出生地 | 生于 Breslau（今 Wrocław，波兰）附近——写「布雷斯劳（今弗罗茨瓦夫）」，勿写成波兰籍 |
| 引语红线 | page.md 无直接引语——全文用间接转述，不得杜撰引号原话 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76614 | ✅ |
| name_zh | 弗里德里希·贝尔吉乌斯 | ✅ |
| name_en | Friedrich Bergius | ✅ |
| birth_date | 1884-10-11 | ✅ |
| death_date | 1949-03-30 | ✅（frontmatter 双值取 infobox） |
| nationality | Germany | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分：chemistry / high-pressure chemistry / coal hydrogenation / hydrothermal carbonization，带 rank） | ✅ |
| has_biography | false（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作者 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Arthur Rudolf Hantzsch | 师→生（莱比锡博士导师） | 1907 年硫酸溶剂论文 |
| colleague | Fritz Haber | 无向 | 1909 年在卡尔斯鲁厄大学随其与 Bosch 参与合成氨开发一学期 |
| colleague | Carl Bosch | 无向 | 卡尔斯鲁厄共事；1931 共享诺奖；煤氢化专利售 BASF 后由其推进 |
| colleague | Max Bodenstein | 无向 | 1909 年起在汉诺威与其共事（化学动力学） |
| colleague | Theodor Goldschmidt | 无向 | 邀请在其 Th. Goldschmidt AG 工厂建煤氢化装置 |
| co-honored | Carl Bosch | 无向 | 1931 诺贝尔化学奖共同得主 |

**子女**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Renate Burgess | Bergius → 女 | page.md 明载 "father of Renate Burgess" |

> **禁入库名单（叙事/图注 only）**：Fritz Haber 的导师性关系不存在（1909 仅一学期共事，作 colleague）；Franz Joseph Emil Fischer（批评者，非合作者，且为同名陷阱人物）；妻子（姓名无载）；Richard Abegg（仅 Other academic advisors 一词，并入 §5 注记不入库——如 Review 认为应入可补 influence 行）。

## 8. 奖项清单

- Nobel Prize for Chemistry（1931，与 Carl Bosch 共享）
- Melchett Medal（1934）
- Wilhelm Exner Medal（1937）
- Liebig Medal（frontmatter award_received 明载，年份 page.md 无载——勿标年份）
- honorary member of the Physics Association（Frankfurt am Main；frontmatter 明载）
- 诺奖演讲 1932-05-21《Chemical Reactions under High Pressure》

## 9. 机构清单

- 教育：Friedrich Wilhelms 钢铁厂（Mülheim，入大学前 6 个月）→ University of Breslau（1903–）→ University of Leipzig（PhD 1907，导师 Arthur Rudolf Hantzsch）
- 任职：University of Karlsruhe（1909，随 Haber 与 Bosch 一学期）→ Leibniz University Hannover（1909–，与 Max Bodenstein 共事，habilitation 期间发展高压化学）→ Heidelberg（木材糖化时期）→ Th. Goldschmidt AG 工业装置（1914 邀请，1919 投产）→ 柏林（二战期间边缘参与）→ 战后意大利、土耳其、瑞士、西班牙顾问 → 阿根廷工业部顾问（–1949）
- 安葬：Cementerio Alemán（La Chacarita Cemetery 旁，布宜诺斯艾利斯）

## 10. 终审清单

- [ ] 生卒 1884-10-11 / 1949-03-30（frontmatter 双值已裁定），享年 64，出生地 Breslau、去世地布宜诺斯艾利斯
- [ ] 1931 共享（Bosch）表述准确；官方获奖理由英文原句完整呈现
- [ ] 博士导师 Arthur Rudolf Hantzsch（infobox 为准）；F.J.E. Fischer 与其他 Fischer 区分清楚
- [ ] Bergius 工艺 1913 专利、早于 Fischer–Tropsch；专利售 BASF 表述准确
- [ ] 妻子姓名无载禁写；女儿 Renate Burgess 入库
- [ ] 流亡经历客观陈述，公民权质疑为正文实载
- [ ] 无编造引语——全文用间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Friedrich_Bergius/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：与妻合影可裁切或作插图；检查主肖像获取结果（REST API / 装饰圆占位）并记录
- [ ] **国籍**：封面顶部明示德国
- [ ] **引语核对**：全文不得出现无法在 page.md 溯源的"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Frederick_Sanger_zh.tex）对齐
