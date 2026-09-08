# George Boole（乔治·布尔）立传提示词

> qid=Q134661 · 1815-11-02 – 1864-12-08 · 英国数学家、哲学家、逻辑学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/George_Boole/`（page.md + metadata.json + images.txt）
>
> **立传状态：✅ 已完成（参考高斯基准模板）**——tex（14 页）+ Makefile + 头像就位，`make distclean && make` 编译通过、Overfull = 0；头像采用 Illustrated London News 1865 版画肖像（`images/boole_portrait.jpg`）。

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「二进制 / 布尔格」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：George Boole（中文惯称：布尔）
- **生卒**：1815-11-02 生于林肯（Lincoln，英格兰）→ 1864-12-08 逝于 Ballintemple（科克，爱尔兰），享年 49（肺炎→胸膜积液）
- **国籍**：United Kingdom of Great Britain and Ireland（英国）
- **身份**：数学家、哲学家、逻辑学家（布尔代数、数理逻辑）
- **家庭**：父 John Boole Snr（鞋匠）、母 Mary Ann Joyce；1855 年娶 Mary Everest（George Everest 之侄女），育 5 女
- **教育轨迹**：
  - 几乎完全自学（鞋匠之子，家境贫寒，小学教育后全靠自学）
  - 自学拉丁语、希腊语及现代语言（曾翻译拉丁诗被学者指控抄袭）
  - 16 岁起教书养家（赡养父母与三个弟妹）
  - 19 岁自办学校（林肯 Free School Lane）
- **研究领域**：数理逻辑、布尔代数、微分方程、概率论

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **布尔代数（最著名贡献）**：1847 年《逻辑的数学分析》（The Mathematical Analysis of Logic）引入符号逻辑；1854 年《思维的规律》（The Laws of Thought）系统阐述布尔代数，把逻辑从"语言哲学研究"转化为"二元值与逻辑算符的代数方程系统"。
2. **信息时代的奠基者**：布尔逻辑是计算机编程的基础，被誉为奠定了信息时代的基础。1937 年 Claude Shannon 用布尔代数优化电磁继电器电路，奠定现代电子数字计算机基础（Victor Shestakov 也独立提出类似理论）。
3. **自学成才的传奇**：鞋匠之子，几乎完全自学成才，16 岁教书养家，19 岁自办学校——是"自学成才"的典范。
4. **《思维的规律》**：1854 年出版，除布尔代数外，还尝试为概率论建立一般方法（从给定事件的概率确定逻辑相关事件的概率）。
5. **布尔不等式（Boole's inequality）**：概率论中的基本不等式。
6. **不变量理论**：1841 年发表早期不变量理论的有影响力论文。
7. **微分方程**：完成两部系统专著《微分方程专论》（1859）与《有限差分微积分专论》（1860）。
8. **布尔恒等式（Boole's identity）**：1857 年在超越数比较与定积分理论中证明的恒等式，其推广在希尔伯特变换理论中重要。
9. **悲剧性的死亡（叙事点）**：1864 年 11 月冒雨步行三英里讲课（穿湿衣），患肺炎；妻子信奉顺势疗法（"以毒攻毒"），用湿毯子包裹他，病情恶化，12 月 8 日去世。
10. **非凡的后代**：5 个女儿中，Alicia Boole Stott 研究四维几何，Lucy Everest 是英国第一位女性化学教授，Ethel Lilian 是小说《牛虻》作者；玄孙 Geoffrey Hinton 是深度学习先驱、2024 年诺贝尔物理学奖得主。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | tex 变量 | 说明 |
|---|---|---|---|
| 主色（英伦蓝） | `#1F3A93` | `englandblue` | 英伦理性 / 表头 |
| 强调色（逻辑金） | `#C9A227` | `logicgold` | 布尔代数 / 尊崇 |
| 分类色 1（布尔代数 — 靛蓝） | `#4C5FD5` | `badgeBoolean` | 布尔代数 / 二进制 |
| 分类色 2（逻辑 — 青绿） | `#0E7C7B` | `badgeLogic` | 数理逻辑 / 思维规律 |
| 分类色 3（概率/分析 — 琥珀） | `#E07B30` | `badgeProb` | 布尔不等式 / 微分方程 |
| 分类色 4（遗产 — 石版灰） | `#4A5568` | `badgeLegacy` | 信息时代 / 遗产 |
| 背景 | `#F7F6F9` | `bgmain` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「二进制 / 布尔格（0 与 1）」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**古典典雅 / 自学成才的坚韧与悲剧**（鞋匠之子自学成才、49 岁早逝）
- **匹配理由**：
  - 布尔是自学成才的典范，其工作奠定信息时代，却 49 岁因悲剧性的误诊早逝——需**典雅、坚韧、略带怅惘**的配乐
  - "典雅" 匹配其英国学者气质
  - "怅惘" 匹配其早逝（湿毯子悲剧）
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/典雅/略带怅惘风格）：
  - 首选：古典 / 典雅 / 坚韧风格曲目（呼应自学成才）
  - 备选：历史感深沉 / 怀旧曲目（呼应 49 岁早逝）
  - 时长需 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（实际 13 页正文 + OpenMath 封面，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「布尔代数与信息时代的奠基者」+ 布尔 1815–1864 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1815 林肯出生 → 1831 执教 → 1834 办学 → 1840 首篇论文 → 1844 金奖 → 1847 《逻辑的数学分析》→ 1849 科克教授 → 1854 《思维的规律》→ 1864 逝世
4. **自学成才的早年**（1815–1849）：鞋匠之子、自学、16 岁教书、19 岁办学（5 行表格）
5. **1847《逻辑的数学分析》**（核心贡献页）：逻辑代数化、亚里士多德、争论背景、论域（表格 + 公式框 `NOT x=1-x` 等）
6. **1854《思维的规律》**（核心贡献页）：二元取值、+ 的部分性、Jevons 之争、概率一般方法（表格 + 核心恒等式公式框）
7. **信息时代的奠基**（核心叙事页）：1847/1854 → 1935/1937 Shestakov/Shannon → 现代计算机（流程图 + 逻辑电路同构公式框）
8. **布尔不等式与概率论**（核心贡献页）：布尔不等式、概率一般方法、Keynes/Hailperin 之争（表格 + 公式框）
9. **微分方程与不变量理论**（核心贡献页）：1840 首篇、1841 不变量、1844 金奖论文、1859/1860 专著、1857 布尔恒等式（5 行表格）
10. **科克教授与家庭**（核心叙事页）：1849 QCC 首任教授、Mary Everest、5 女（表格）
11. **悲剧性死亡与非凡后代**（核心叙事页）：湿毯子悲剧、玄孙 Geoffrey Hinton（表格）
12. **荣誉与传承**（`\honorslide`）：生前荣誉 / 身后纪念 / 学术影响（itemize 表格）
13. **终章**（`\closingslide`）：「他把思维变成了代数，后世把代数变成了计算机。」

## 5. 史实陷阱与敏感点（终审必须检查）

- **布尔代数与信息时代**：布尔逻辑是信息时代的**理论基础**，但布尔本人**并未预见计算机**——是后世（Shannon 1937、Shestakov）把布尔代数应用于电路设计。勿写"布尔发明了计算机"或"布尔预见了数字时代"。
- **布尔代数 ≠ 现代布尔代数**：布尔原始系统中 + 是**部分运算**（对应不相交子集的并），后来作者将其解读为异或（对称差）或非异或（析取）——是"布尔奠基、后人完善"，勿写布尔建立了完整的现代布尔代数。
- **逻辑革命**：布尔把逻辑从"语言哲学研究"转化为"代数系统"——是"转化"，勿写布尔否定亚里士多德逻辑（布尔**无意批判**亚里士多德，而是系统化、奠基、扩展其适用范围）。
- **死亡**：1864 年冒雨讲课患肺炎，妻子因信奉顺势疗法用湿毯子包裹他（"以毒攻毒"），病情恶化死于胸膜积液——是**悲剧性的误诊**，客观表述，勿渲染。
- **自学成才**：鞋匠之子，几乎完全自学（小学教育后靠自学，拉丁语可能是书商 William Brooke 所教）——"自学"是相对而言，勿绝对化。
- **皇家学会金奖**：1844 年论文《论分析的一般方法》获皇家学会**第一个数学金奖**——是"第一个数学金奖"。
- **后代**：Geoffrey Hinton 是 Boole 的玄孙（great-great-grandson），2024 年诺贝尔物理学奖——可作"非凡后代"叙事点，但需确认亲属关系表述准确（经 Mary Ellen → George Hinton → H. E. Hinton → Geoffrey Hinton）。
- **无肖像**：✅ 已解决——本地 `images.txt` 虽无本人肖像，但已从 Wikipedia 下载 Illustrated London News 1865 版画肖像至 `images/boole_portrait.jpg`（392×480），封面与身份页均采用。
- **国籍**：United Kingdom of Great Britain and Ireland，今英国（生于英格兰，逝于爱尔兰）——封面用「英国」。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q134661 | ✅ 已入库（MySQL/data/George_Boole.yaml） |
| name_zh | 布尔（或 乔治·布尔） | ✅ 已入库 |
| name_en | George Boole | ✅ 已入库 |
| birth_date | 1815-11-02 | ✅ 已入库 |
| death_date | 1864-12-08 | ✅ 已入库 |
| nationality | United Kingdom | ✅ 已入库 |
| primary_occupation | mathematician | ✅ 已入库 |
| field_of_work | mathematical logic / algebra | ✅ 已入库 |
| has_biography | true | ✅ 本次置 true |

## 7. 社会关系入库清单（§20）

- **学术合作**：Augustus De Morgan（逻辑学同侪，支持其观点）、Duncan Farquharson Gregory（《剑桥数学杂志》编辑，论文发表后成为朋友）、Edward Bromhead（资助数学书籍）
- **后世发展**：William Stanley Jevons（扩展其工作）、Charles Sanders Peirce（整合其与 De Morgan 工作）、Claude Shannon（1937 应用布尔代数于电路）
- **家族**：妻 Mary Everest（George Everest 之侄女）、5 女（Alicia Boole Stott、Lucy Everest Boole、Ethel Lilian Voynich 等）

## 8. 奖项清单

- Royal Medal（皇家奖章，1844，第一个数学金奖，论文《论分析的一般方法》）
- Keith Medal（基思奖章，1855–1857，爱丁堡皇家学会）
- Fellow of the Royal Society（FRS，1857）
- 都柏林大学、牛津大学荣誉学位（LL.D.）

## 9. 机构清单

- 教育：Bainbridge's Commercial Academy（早期）
- 任职：University College Cork（Queen's College Cork，1849 首任数学教授）、Lincoln Mechanics' Institute、Free School Lane, Lincoln（自办学校）

## 10. 终审清单

- [x] 生卒 1815-11-02 / 1864-12-08，享年 49，出生地林肯
- [x] 布尔代数"信息时代理论基础、Shannon 后应用"表述准确，勿写布尔预见计算机（Slide 7 流程图明确理论 → 应用的传承链）
- [x] 布尔原始系统"部分运算、后人完善"表述准确（Slide 6 表格 + 公式框注明）
- [x] 逻辑"转化、无意批判亚里士多德"表述准确（Slide 5 表格）
- [x] 死亡"湿毯子悲剧"客观表述（Slide 11）
- [x] 自学成才"相对而言"表述准确（Slide 4：拉丁语可能为书商 Brooke 所授）
- [x] 皇家学会"第一个数学金奖"表述准确（Slide 4 / 9 / 12）
- [x] 后代 Geoffrey Hinton 亲属关系表述准确（Slide 11：玄孙，经长女 Mary Ellen 一系）
- [x] 头像确认（✅ Illustrated London News 1865 肖像，`images/boole_portrait.jpg`）
- [x] 国籍用「英国」现代对应
- [x] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误，Overfull = 0

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [x] **结合本地 Wikipedia**：逐页对照 Beamer tex 全部事实（生卒、奖项年份、机构、家庭）
- [x] **头像**：✅ 采用 Illustrated London News 1865 肖像（Wikipedia 下载 → `images/boole_portrait.jpg`）
- [x] **国籍**：封面顶部徽章明示英国
- [x] **引语核对**：未使用直接引语；"universe of discourse" 以间接表述呈现（Slide 5 表格）
- [x] **编译验证**：`make distclean && make` 通过，14 页 PDF，Overfull = 0
- [x] **更新提示词**：Review 修正已写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Sylvester / Kummer / Liouville）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
