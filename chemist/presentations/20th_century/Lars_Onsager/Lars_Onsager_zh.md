# Lars Onsager（拉尔斯·翁萨格）立传提示词

> qid=Q107405 · 1903-11-27 – 1976-10-05 · 挪威裔美国物理化学家与理论物理学家 · 20 世纪 · 诺贝尔化学奖（1968，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Lars_Onsager/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**严格对齐 Frederick Sanger 黄金参照**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.md`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 金色公式展示框 + 气泡背景。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。⚠ 肖像说明：本地 `images.txt` 仅含墓碑合照（Kirkwood_onsager.jpg，Onsager 与 Kirkwood 并葬的墓碑照）与公式渲染图——**非个人标准肖像**；回退方案：经 Wikipedia REST API `page/summary` 查 infobox 原图名后用 `Commons Special:FilePath/<文件名>?width=600` 下载（curl -A "Mozilla/5.0" + file 验证）；404 则装饰圆占位，禁用墓碑照充当肖像。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{exchange-alt}\enspace 倒易关系的先知\enspace·\enspace 挪威 / 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「涨落—弛豫—对称」母题——微观涨落与宏观不可逆过程的倒易对称。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。⚠ 公式框内容仅用页面可溯源的量/名称做示意，页面无具体公式的（倒易关系、Ising 配分函数）用名称+示意并注明"示意"。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Lars Onsager（中文惯称：拉尔斯·翁萨格）
- **生卒**：1903-11-27 生于 Kristiania（今奥斯陆），挪威 → 1976-10-05 逝于佛罗里达州 Coral Gables（动脉瘤），享年 72
- **国籍**：Norway → United States（1945 入籍美国；"Norwegian American"）。⚠ metadata.json 另载 Kingdom of the Netherlands——正文无据，为 metadata 噪声，**禁用**
- **身份**：物理化学家与理论物理学家（physical chemist and theoretical physicist；耶鲁 J. Willard Gibbs 理论化学讲席教授）
- **家庭**：父为律师。1933-09-07 娶 Margrethe Arledter（电化学家 Hans Falkenhagen 的姻亲妹），育三子一女；妻昵称 Gretel，1991 年去世安葬后，子女在墓碑 "Nobel Laureate" 后加星号并在右下角补 "*etc."。本页无其他家庭成员记载——禁写
- **教育轨迹**：
  - 奥斯陆完成中学
  - Norwegian Institute of Technology（NTH，特隆赫姆）——1925 年毕业获化学工程师资格；在校精读 Whittaker & Watson 的 *A Course of Modern Analysis*（对其日后工作影响至深）
  - 耶鲁大学 PhD 1935——论题为周期 4π 的 Mathieu 方程之解及其相关函数（此前 NTH 曾认定其倒易关系纲要"过于不完整"不构成博士论文；耶鲁本可让其以已发表论文充当论文，他坚持重做新研究）
- **导师口径**：frontmatter doctoral_advisor 载 **Peter Debye**；正文实载 1925–1928 任 Debye 的 ETH 助手（非正式读博关系；耶鲁 1935 博士未载导师）——PPT 与 yaml 均按此限定表述
- **研究领域**：physical chemistry、统计力学——电解质溶液理论、不可逆过程热力学（倒易关系）、相变（二维 Ising 模型精确解）、超流理论、液晶

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **律师之子（1903）**：Kristiania（今奥斯陆）出生——数学天赋早早指向理论而非实验。
2. **NTH 化学工程师（1925）**：特隆赫姆毕业；把 *A Course of Modern Analysis* 读通——日后解 Mathieu 方程、对角化 Ising 传递矩阵的数学弹药库。
3. **修正 Debye-Hückel（1925–1926）**：对电解质溶液的 Debye-Hückel 理论得出修正（规定溶液中离子的布朗运动），1926 年发表——即 Debye-Hückel-Onsager 方程的方向。
4. **面晤 Debye（1925）**：径直赴苏黎世当面告诉 Debye"他的理论错了"——反而令 Debye 深为折服，邀其任 ETH 助手（至 1928）。
5. **约翰霍普金斯的一学期（1928）**：赴美任 JHU 教职，教大一化学——理论天才、教学无能，一学期即被解聘。
6. **布朗大学与倒易关系（1929/1931）**：教研究生统计力学（课程被学生戏称 "Sadistical Mechanics"）；研究温度梯度对扩散的影响，提出 **Onsager 倒易关系**（1929 年发表、1931 年扩展）——重要多年无人识货；1933 年大萧条中布朗裁员离任。
7. **婚姻（1933）**：赴奥地利访电化学家 Hans Falkenhagen，结识其姻亲妹 Margrethe Arledter，1933-09-07 结婚，三子一女。
8. **没有博士学位的教授（1933–1935）**：以博士后身份被耶鲁聘用，随后被发现从未获得博士学位；坚持重做新研究而非提交旧论文——Mathieu 方程论文化学与物理系看不懂，数学系（研究生院主任 Einar Hille 等）力保，1935 年授化学博士。
9. **耶鲁晋升（1934/1940）**：论文完成前即任助理教授，1940 副教授；两门统计力学课被戏称 "Advanced Norwegian I/II"（高级挪威语 I/II）——"无法指导研究生，除非偶尔遇到出色者"。
10. **介电弛豫（1930s）**：改进 Debye 研究过的电介质偶极理论（Onsager reaction field）——1936 年投稿被 Debye 主编的刊物拒稿，战后 Debye 才接受其想法。
11. **二维 Ising 模型精确解（1944）**：从 2×2 传递矩阵到 64×64 逐级对角化，猜出（后称）Onsager 代数；解用到广义四元数代数与椭圆函数理论——零场二维 Ising 模型精确解，被广泛视为数学物理的神来之笔（tour de force）。他自嘲开战之初研究是因为"二战期间有很多时间"。
12. **战后扩展（1945–1950s）**：1945 入籍美国并获 J. Willard Gibbs 理论化学教授头衔（与 Gibbs 同路——以数学应用物理化学）；1949 提出氦超流的量子涡旋理论（两年后 Feynman 独立提出同一理论）；液晶硬棒模型、冰的电性；Fulbright 奖学金访剑桥研究金属磁性——金属磁通量子化的重要想法。
13. **1968 诺贝尔化学奖与身后**：Lorentz Medal（1958）、Willard Gibbs Award（1962）、Peter Debye Award（1965）之后，倒易关系的价值在战后数十年显现——1968 年获诺贝尔化学奖（页面表述如此；官方 citation 原句页面无载），同年获 National Medal of Science；NAS（1947）、AAAS（1949）、Alpha Chi Sigma（1950）、美国哲学学会（1959）、ForMemRS（1975）；1972 自耶鲁退休赴迈阿密大学理论研究中心任杰出物理学教授；1976-10-05 动脉瘤逝于 Coral Gables；葬 New Haven Grove Street Cemetery——与 John Gamble Kirkwood 并排，墓碑原刻仅 "Nobel Laureate"；身后：NTH 设 Lars Onsager Lecture 与讲席（1993）、美国物理学会设统计物理 Lars Onsager Prize（1993）、手稿捐赠 NTNU 成 The Lars Onsager Archive。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深青绿 deepviridian） | `#1E6B52` | 涨落与对称的深青绿——微观可逆与宏观不可逆的倒易镜像（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（倒易关系 badgeRecip） | `#1E4E79` | 蓝 Onsager reciprocal relations / 不可逆过程热力学 |
| 分类色 2（Ising 精确解 badgeIsing） | `#8B1A1A` | 红 二维 Ising 精确解 / Onsager 代数 |
| 分类色 3（统计力学扩展 badgeStat） | `#6B4C9A` | 紫 超流涡旋 / 液晶硬棒模型 / 冰的电性 |
| 分类色 4（双国人生 badgeLife） | `#1B7A43` | 绿 挪威—美国双轨 / NTH 与耶鲁 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「涨落—弛豫」——宏观输运系数背后成对的微观涨落。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Eternals** — Alex-Productions（`music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`；不要复制 wav 文件，make video 时引用路径）
- **风格**：恒久 / 深沉 / 大尺度时间感
- **匹配理由**：
  - "Eternals" 匹配倒易关系的命运——1929/1931 发表后冷落数十年，战后终成不可逆过程热力学的基石，1968 加冕：迟到的永恒
  - 大尺度时间感匹配二维 Ising 精确解的数学之美——一件超越时代的 work of art
  - 墓碑上只刻 "Nobel Laureate" 的极简，正是这种恒久气质的注脚
- **时长**：以文件实际时长为准，ffmpeg `-shortest` 自动对齐 15 页 × 7 秒

## 4. Slide 规划（15 页，Sanger 同构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 倒易关系的先知 / Lars Onsager 1903–1976 + 四色 badge + 右上头像 + 国籍行（挪威 / 美国）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  翁萨格的一生 — 高斯式时间线（10 节点：1903→1925→1926→1928→1931→1935→1944→1945→1949→1968）
04  挪威岁月与 NTH (1903–1925) — 表格「时间|事件|结果」（律师之子/A Course of Modern Analysis/化学工程师）
05  面晤 Debye (1925–1928) — 表格「行动|反应|结果」+ 公式框：Debye-Hückel-Onsager 方程（名称示意，注明源自 Known for）
06  美国开局 (1928–1933) — 表格（JHU 一学期/布朗/Sadistical Mechanics/大萧条离任）
07  Onsager 倒易关系 (1929/1931) — 表格「问题|方法|结果」+ 公式框：L_ij 与 L_ji 的对称示意（注明"示意"）
08  没有博士学位的教授 (1933–1935) — 表格（NTH 拒稿/Mathieu 方程/数学系力保 PhD 1935）+ Advanced Norwegian 轶事
09  二维 Ising 精确解 (1944) — 表格「问题|方法|结果」+ 公式框：传递矩阵逐级对角化示意（注明"示意"）
10  战后扩展 (1945–1950s) — 表格（Gibbs 教授 1945/超流涡旋 1949 与 Feynman 独立/液晶/冰/Fulbright 剑桥）
11  1968 诺贝尔化学奖 — 独享；页面表述（倒易关系价值显现）+ National Medal of Science 1968；官方原句页面无载
12  教学轶事与人格 — 表格（一学期被解聘/Sadistical Mechanics/Advanced Norwegian I-II/只带得出色者）
13  墓碑与身后 — "Nobel Laureate" + "*etc." 轶事 / 与 Kirkwood 并排长眠 / 1993 双奖设立 / Onsager Archive
14  结尾 — 「微观的每一次涨落里，都藏着宏观的对称。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1968 诺奖理由 | 官方 citation **英文原句本地 page.md 无载**——禁写原句（如 "for the discovery of the reciprocal relations bearing his name…" 之类页外文本一律禁）；用页面表述"倒易关系的价值在战后数十年显现，到 1968 已被认为重要到足以获奖"，并注明"页面无载官方原文" |
| 1968 独享 | 1968 为**独享**，无共同得主——勿造 co-honored |
| 国籍 | Norway + United States（1945 入籍，正文明载）；metadata.json 的 **Kingdom of the Netherlands 为噪声**——禁用 |
| 师承口径 | frontmatter doctoral_advisor=Peter Debye；正文实载为"ETH 助手（1925–1928）+ Debye 曾拒其 1936 投稿"——写"师承 Debye"必须限定为 ETH 助理时期；耶鲁 1935 PhD 未载导师 |
| Debye 拒稿 | 1936 年介电弛豫论文被 Debye 主编刊物拒稿，战后 Debye 才接受——与 1925 年"面晤折服"是两件事，勿混写 |
| 超流涡旋 | 1949 Onsager 提出；**两年后 Feynman 独立提出同一理论**——写"独立提出"，禁写"Feynman 沿用/师承 Onsager" |
| Ising 解范围 | **零场二维** Ising 模型精确解（1944）——勿写三维、勿写含外场 |
| 教学轶事 | JHU 一学期解聘、"Sadistical Mechanics"、"Advanced Norwegian I/II"、"无法指导研究生除偶尔出色者"——均页面原载可用，但保持克制幽默勿丑化 |
| Fuoss | Raymond Fuoss 是其布朗大学**研究生**，后随他加入耶鲁化学系——advisor-student（学生）入库依据即此句 |
| 妻名 | Margrethe Arledter（1933-09-07 结婚；三子一女）；"Gretel" 为同一人的昵称（1991 年去世句用 Gretel）——同一人两写须注明 |
| Kirkwood | 仅"墓碑并排"轶事，**无学术关系记载**——禁入库关系、禁写同事/师承 |
| Falkenhagen | 1933 走访+姻亲——非实质学术合作，禁入库关系 |
| Feynman 关系 | 独立平行工作，无交往记载——禁入库关系 |
| 博士生 | 正文 infobox 仅 Joseph L. McCauley 一人；metadata.json 另载 John Frederick Nagle、Stefan Machlup、John Lester Greenstadt、Joseph F. Malerba——**metadata-only 不予入库** |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q107405 | ✅ |
| name_zh | 拉尔斯·翁萨格 | ✅ |
| name_en | Lars Onsager | ✅ ★必须用库内 db_name_en 精确形式（复用记录 UPD 回填 QID，防分裂） |
| birth_date | 1903-11-27 | ✅ |
| death_date | 1976-10-05 | ✅ |
| nationality | Norway（rank 0）+ United States（rank 1，1945 入籍） | ✅ |
| primary_occupation | physical chemist | ✅ |
| field_of_work | physical chemistry（person_field 细分：irreversible thermodynamics / statistical mechanics / physical chemistry / electrolyte theory，带 rank） | ✅ |
| has_biography | false（立传 Beamer 完成后再置 1） | ✅ |

## 7. 社会关系入库清单

**★红线：只收 page.md 正文或 frontmatter 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Peter Debye | 师→生 | ETH 助理时期导师（frontmatter doctoral_advisor；正文载 1925–1928 任其助手，因当面指错理论反受赏识） |
| advisor-student | Raymond Fuoss | Onsager→学生 | 布朗大学研究生，后随其加入耶鲁化学系 |
| advisor-student | Joseph L. McCauley | Onsager→学生 | 正文 infobox doctoral student |
| spouse | Margrethe Arledter | 无向 | 1933-09-07 结婚，三子一女（昵称 Gretel） |

> **metadata-only 禁入库名单**：John Frederick Nagle、Stefan Machlup、John Lester Greenstadt、Joseph F. Malerba（doctoral_student 仅 metadata.json）；John Gamble Kirkwood（仅墓碑并排轶事）；Richard Feynman（独立平行工作无交往）；Hans Falkenhagen（走访+姻亲非实质合作）——均不予入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1968，独享）
- National Medal of Science（1968）
- Lorentz Medal（1958）
- Willard Gibbs Award（1962）
- Peter Debye Award in Physical Chemistry（1965）
- Rumford Prize（frontmatter 载，页面未给年份——禁编）
- Wilbur Cross Medal（frontmatter 载，页面未给年份——禁编）
- National Academy of Sciences（1947 当选）
- American Academy of Arts and Sciences（1949 当选）
- Alpha Chi Sigma（1950 加入）
- American Philosophical Society（1959 当选）
- Foreign Member of the Royal Society，ForMemRS（1975）
- NTH 荣誉博士 doctor techn. honoris causa（1960）
- Fellow of the American Physical Society（frontmatter 载）

## 9. 机构清单

- 教育：奥斯陆中学；Norwegian Institute of Technology（NTH，特隆赫姆，1925 化学工程师）；Yale University（PhD 1935，Mathieu 方程）
- 任职：ETH Zürich（Debye 助手，1925–1928）；Johns Hopkins University（1928，一学期）；Brown University（–1933）；Yale University（1934 助理教授→1940 副教授→1945 J. Willard Gibbs 理论化学教授→1972 退休）；University of Cambridge（Fulbright 访问）；University of Miami 理论研究中心杰出物理学教授（1972–）
- 身后：葬 New Haven Grove Street Cemetery（与 Kirkwood 并排）；The Lars Onsager Archive（NTNU Gunnerus 图书馆）

## 10. 终审清单

- [ ] 生卒 1903-11-27 / 1976-10-05，享年 72，出生地 Kristiania（今奥斯陆）、去世地 Coral Gables（动脉瘤）
- [ ] 1968 独享表述准确；获奖理由为页面表述+注明"页面无载官方原文"
- [ ] 国籍 Norway+United States（1945 入籍）；Netherlands metadata 噪声未采用
- [ ] 师承 Debye 限定为 ETH 助理时期；耶鲁 PhD 1935（Mathieu 方程、数学系力保）表述准确
- [ ] Feynman"两年后独立提出"未写成沿用；Ising 解=零场二维
- [ ] 教学轶事（Sadistical Mechanics/Advanced Norwegian）如实且不丑化
- [ ] 墓碑轶事（Nobel Laureate + *etc.）与妻 Gretel=Margrethe Arledter 注记准确
- [ ] 引语核对：任何引号文本必须在 page.md 溯源（含 tombstone 用语与课程昵称），否则改间接转述
- [ ] 正文采用 Sanger 同构：身份信息页 + 时间线页 + 表格语义化 + 公式框（示意注明）+ 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误，vbox≤10pt / hbox≤50pt

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Lars_Onsager/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：REST API 回退下载结果核对（禁用墓碑照）；404 则装饰圆占位并在 §0 注记
- [ ] 国籍：封面顶部明示挪威 / 美国
- [ ] 引语核对：任何引号文本必须在 Wikipedia 原文找到
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox<10pt / hbox<50pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger/Fischer 等）对齐；公式框"示意"注记全篇一致
