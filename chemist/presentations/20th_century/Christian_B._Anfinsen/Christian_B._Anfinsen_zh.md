# Christian B. Anfinsen（克里斯蒂安·安芬森）立传提示词

> qid=Q102278 · 1916-03-26 – 1995-05-14 · 美国生物化学家 · 20 世纪 · 诺贝尔化学奖（1972，与 Stanford Moore、William Howard Stein 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Christian_B._Anfinsen/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页 + 气泡背景，是本次重写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从 `images.txt` / Commons 下载；404 则用装饰圆占位并在 Review 记录）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{project-diagram}\enspace 蛋白质折叠的立法者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「多肽链折叠」母题——离散圆点暗示氨基酸残基折叠成天然构象的过程。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Christian Boehmer Anfinsen Jr.（中文惯称：克里斯蒂安·伯默·安芬森；"B." 取自父名 Boehmer）
- **生卒**：1916-03-26 生于宾夕法尼亚州 Monessen → 1995-05-14 逝于马里兰州 Randallstown，享年 79
- **国籍**：United States（美国）
- **身份**：生物化学家（biochemist）、1972 年诺贝尔化学奖得主；1982 年起任 Johns Hopkins 大学生物学与（物理）生物化学教授
- **家庭**：挪威裔移民家庭——父 Christian Boehmer Anfinsen Sr. 为机械工程师，母 Sophie（娘家姓 Rasmussen）；1920 年代举家迁费城。两段婚姻：Florence Kenenger（1941 结婚，1978 离异，育三子女）；Libby Shulman Ely（1979 结婚，4 名继子女；婚后皈依正统犹太教）
- **教育轨迹**：
  - Monessen High School → 1933 入 Swarthmore College（校队橄榄球；1937 化学学士 BA）
  - 1939 获宾夕法尼亚大学有机化学硕士（MS）
  - American-Scandinavian Foundation 奖学金赴哥本哈根 Carlsberg Laboratory（发展复杂蛋白/酶的化学结构分析新方法）
  - 1941 获哈佛医学院生物化学系博士奖学金；1943 获 PhD（论文 *Quantitative histochemical studies of the retina*）
- **博士导师**：Albert Baird Hastings（哈佛医学院，infobox 明载）
- **研究领域**：生物化学——蛋白质结构与功能、核糖核酸酶复性、蛋白质折叠（Anfinsen's dogma）、分子进化

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **挪威移民之子（1916）**：宾州钢铁小镇 Monessen 出生，挪威裔机械工程师家庭；1920 年代迁往费城。
2. **球场与实验室（1933–1937）**：Swarthmore 校队橄榄球员，1937 年化学学士——运动与科研双线起步。
3. **Carlsberg 缘分（1939）**：美斯堪的纳维亚基金会奖学金赴哥本哈根 Carlsberg 实验室；这段缘分 1954 年会再续（洛克菲勒基金会奖学金重返一年）。
4. **哈佛博士（1941–1943）**：哈佛医学院生物化学系，师从 Albert Baird Hastings，论文为视网膜定量组织化学研究。
5. **战时服务（WWII）**：在美国科学研究与发展办公室（OSRD）工作。
6. **NIH 时代（1950）**：出任国家心脏研究所（NIH，Bethesda）细胞生理实验室主任——诺奖级工作正是在 NIH 完成。
7. **周游列国（1954–1959）**：洛克菲勒基金会奖学金重返 Carlsberg 一年；古根海姆奖学金赴以色列 Rehovot 的 Weizmann 科学研究所（1958–59）；1958 当选美国艺术与科学院院士。
8. **1961 年的判决性实验（★ 核心贡献）**：证明**核糖核酸酶（ribonuclease）变性后可以自发复性并恢复酶活**——蛋白质折叠所需的全部信息都编码在氨基酸序列本身（即 Anfinsen's dogma / 序列决定构象）。
9. **Anfinsen's dogma 与 Anfinsen cage**：序列 → 天然构象的原理以他命名；"Anfinsen cage" 描述折叠微环境——见 See also 明载。
10. **1972 诺贝尔化学奖**：与 Stanford Moore、William Howard Stein 共享，表彰核糖核酸酶工作——"氨基酸序列与生物活性构象之间的联系"（page.md 对三人工作的总述口径）。
11. **分子进化的先声（1959）**：出版 *The Molecular Basis of Evolution*，把蛋白质化学与遗传学联系起来；发表 200 余篇原始论文；核酸压缩领域的思想先驱；主编 *Advances in Protein Chemistry*。
12. **晚年转向（1979–1995）**：与 Libby Ely 结婚后皈依正统犹太教；1981 年成为世界文化理事会创始成员；1982 年至去世任教 Johns Hopkins。
13. **身后之名（1996–）**：The Protein Society 设立 Christian B. Anfinsen Award（1996 起，每年授予蛋白质科学杰出贡献者，首任得主 Donald Hunt）——1995-05-14 逝于马里兰州 Randallstown。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深绯红 crimsond） | `#9E2B25` | NIH 白墙与折叠多肽的庄重底色（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（蛋白质折叠 badgeFold） | `#1E5A8A` | 蓝核糖核酸酶复性 / dogma（核心贡献主视觉） |
| 分类色 2（序列决定构象 badgeSeq） | `#1B7A43` | 绿氨基酸序列 / 一级结构 |
| 分类色 3（Carlsberg 缘 badgeCarlsberg） | `#C9A227` 加深版 `#8A6D1E` | 暗金哥本哈根 / Weizmann |
| 分类色 4（分子进化 badgeEvolution） | `#5B2A6E` | 紫 Molecular Basis of Evolution |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「多肽链折叠为天然构象」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Last Hope** — Victor Cooper（文件：`music_audio/inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav`；不要复制 wav 到人物目录，video 阶段按路径引用）
- **风格**：戏剧性 / 强大 / 史诗
- **匹配理由**：
  - "最后的希望" 匹配科学母题——变性蛋白能否复原曾是悬案，复性实验给出了决定性答案：序列即一切
  - "戏剧性" 匹配 1961 年判决性实验的叙事张力
  - "史诗" 匹配从宾州小镇到 NIH 到斯德哥尔摩的上升弧线
- **时长核对**：video 阶段用 ffmpeg `-shortest` 自动对齐 15 页 × 7 秒 ≈ 105 秒

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 蛋白质折叠的立法者 / Christian B. Anfinsen 1916–1995 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/出生地/去世地/领域/荣誉）
03  安芬森的一生 — Sanger 式时间线（10 节点：1916→1937→1939→1943→1950→1954→1961→1972→1982→1995）
04  挪威移民之子 (1916–1937) — 表格「时间|事件|结果」（Monessen / 费城 / Swarthmore 橄榄球）
05  Carlsberg 与哈佛 (1939–1943) — 表格「阶段|地点|结果」（奖学金 / Hastings / PhD 1943）
06  NIH 时代 (1950–1960) — 表格「机构|职位|结果」（国家心脏研究所细胞生理实验室主任 / Weizmann）
07  复性实验（★ 核心页）— 表格「问题|方法|结果」+ 公式框：变性 → 复性 → 活性恢复（1961）
08  Anfinsen's dogma — 表格「命题|证据|意义」+ 公式框：序列 ⇒ 天然构象
09  1972 诺贝尔化学奖 — 表格「人物|贡献|理由」+ 公式框：与 Moore/Stein 共享（三人方向区分）
10  分子进化 (1959) — 表格「著作|内容|意义」+ 200 余篇论文 / Anfinsen cage
11  荣誉与信仰 — Sanger 式「类别|代表|意义」表格（NAS / 丹麦皇家科学院 / AAAS 1958 / 皈依与自述）
12  身后之名 — 表格「形式|内容|意义」（Anfinsen Award 1996 / Papers 入藏国家医学图书馆）
13  遗产：折叠革命 — 四分类遗产盒 + 公式框：从 dogma 到今日蛋白质设计
14  结尾 — 「氨基酸的序列里，写着蛋白质自己的命运。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1972 获奖口径 | 与 Stanford Moore、William Howard Stein **共享**；page.md 只给出对三人工作的总述（核糖核酸酶、序列与活性构象的联系）——**本地页面无三人分别的官方 citation**，勿杜撰 Moore/Stein 的单独获奖理由；Moore/Stein 的方向（活性中心催化活性）由 chem-batch-15 依其本人页面口径处理 |
| dogma 出处 | "序列决定天然构象" 的表述来自 1961 年复性实验结论——勿把 Anfinsen's dogma 与分子生物学中心法则（central dogma）混淆 |
| 1961 实验 | 核糖核酸酶**变性后自发复性并保留酶活**——是"提示/表明"（suggesting）序列编码折叠信息，勿写成"证明信息存在细胞外"之类的引申 |
| 博士导师 | Albert Baird Hastings（哈佛医学院）——infobox 明载；论文题目 *Quantitative histochemical studies of the retina*（1943） |
| 两段婚姻 | Florence Kenenger（1941–1978 离异，3 子女）；Libby Shulman Ely（1979 结婚，4 继子女）——勿写"原配去世"；1979 年**皈依正统犹太教**，1987 年自述（转述）对宗教的感情仍反映"五十年正统不可知论"——须忠实原文引号句 |
| WWII 工作 | Office of Scientific Research and Development（OSRD）——勿写成"参军" |
| 机构衔接 | 1962 年短暂回哈佛医学院任访问教授并受邀任化学系主任，随后出任 NIAMD 化学生物学实验室主任至 1981 年——勿写成"回哈佛任教授" |
| Nobel 讲座 | 1972-12-11 *Studies on the Principles that Govern the Folding of Protein Chains*（page.md 外链明载） |
| 引语红线 | page.md 正文仅有宗教自述一句英文原话——其余一律间接转述；无出处的"原话"禁用 |
| 获奖者名单区分 | Anfinsen Award 历任得主表（Hunt/Hendrickson/Fersht/Karplus/Yonath 等）是奖项页信息——立传正文可略过，勿与本人荣誉混排 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q102278 | ✅ |
| name_zh | 克里斯蒂安·安芬森 | ✅ |
| name_en | Christian B. Anfinsen | ✅ |
| birth_date | 1916-03-26 | ✅ |
| death_date | 1995-05-14 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：biochemistry / protein folding / protein chemistry / molecular evolution，带 rank） | ✅ |
| has_biography | 0（Beamer 立传完成后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 共同得主 / 婚姻**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Albert Baird Hastings | 师→生（博士导师） | 哈佛医学院生物化学系，1943 年 PhD |
| co-honored | Stanford Moore | 无向 | 1972 诺贝尔化学奖共同得主 |
| co-honored | William Howard Stein | 无向 | 1972 诺贝尔化学奖共同得主 |
| spouse | Florence Kenenger | 无向 | 1941 结婚，1978 离异，育三子女 |
| spouse | Libby Shulman Ely | 无向 | 1979 结婚，4 名继子女 |

> metadata.json-only 的关系一律不入库；Anfinsen Award 历任得主不构成本人关系、不入库；page.md 未载其博士生名单。

## 8. 奖项清单

- Nobel Prize in Chemistry（1972，与 Stanford Moore、William Howard Stein 共享）
- American-Scandinavian Foundation fellowship（1939）；Guggenheim Fellowship（1958–59，frontmatter 明载）
- Rockefeller Foundation fellowship（1954，重返 Carlsberg）
- Fellow of the American Academy of Arts and Sciences（1958）
- 院士：美国国家科学院（NAS）、丹麦皇家科学与文学院、American Philosophical Society
- 荣誉博士：University of Las Palmas de Gran Canaria（frontmatter 明载）
- 身后：Christian B. Anfinsen Award（The Protein Society，1996 年设立）

## 9. 机构清单

- 教育：Monessen High School、Swarthmore College（BA 1937）、University of Pennsylvania（MS 1939）、Carlsberg Laboratory（哥本哈根，1939）、Harvard Medical School（PhD 1943）
- 任职：OSRD（二战）→ NIH 国家心脏研究所细胞生理实验室主任（1950，Bethesda）→ Weizmann 科学研究所（1958–59）→ 哈佛医学院访问教授（1962）→ NIAMD 化学生物学实验室主任（至 1981）→ Johns Hopkins 大学生物学与（物理）生物化学教授（1982–1995）
- 命名机构：The Protein Society「Christian B. Anfinsen Award」（1996 起）

## 10. 终审清单

- [x] 生卒 1916-03-26 / 1995-05-14，享年 79，出生地 Monessen（PA）、去世地 Randallstown（MD）
- [x] 1972 与 Moore/Stein 共享；不杜撰三人分别的官方 citation
- [x] 1961 复性实验与 dogma 表述准确；与中心法则区分
- [x] 博士导师 Hastings、论文题目准确；OSRD 勿写成参军
- [x] 两段婚姻与皈依表述忠实原文
- [x] 正文无杜撰引语；Anfinsen Award 得主表不入库、不混排
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Christian_B._Anfinsen/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：从 images.txt / Commons 下载（infobox 为 1969 年照片 / 实验室照）；404 用装饰圆占位并记录
- [ ] **国籍**：封面顶部明示美国（挪威裔作小注）
- [ ] **引语核对**：仅宗教自述一句可引原文，其余转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 骨架）对齐

---

> **名单状态**：本文件由 chem-batch-14 生成；`chemist/generate_20th_century_list.py` 由主控统一更新。
> **最重要的事：每写一页就 make，看到溢出就修。**
