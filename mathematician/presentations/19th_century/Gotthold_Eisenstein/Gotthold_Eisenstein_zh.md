# Gotthold Eisenstein（戈特霍尔德·艾森斯坦）立传提示词

> qid=Q61047 · 1823-04-16 – 1852-10-11 · 德国数学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Gotthold_Eisenstein/`（page.md + metadata.json + images.txt）
>
> **立传状态：✅ 已完成（参考高斯基准模板）**——tex（13 页正文）+ Makefile + 头像就位，`make distclean && make` 编译通过、Overfull = 0；头像经 Wikipedia API 查得条目主图（`images/eisenstein_portrait.jpg`，524×689）；BGM 已选 **Lonesome**（AShamaluevMusic，悲伤/电影感，契合 29 岁天才早逝），视频 `make video` 已生成。

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「三次单位根 / 格点」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Ferdinand Gotthold Max Eisenstein（中文惯称：艾森斯坦）
- **生卒**：1823-04-16 生于柏林（普鲁士王国）→ 1852-10-11 逝于柏林，享年 29（肺结核）
- **国籍**：Kingdom of Prussia（普鲁士王国，今德国）
- **身份**：数学家（数论、分析、椭圆函数）
- **家庭**：犹太裔父母在他出生前皈依新教
- **教育轨迹**：
  - 自幼体弱多病（曾患脑膜炎），但学业优异
  - 14 岁入 Friedrich Werder Gymnasium，15 岁已掌握中学数学课程（老师评价"他的数学知识远超中学课程范围"）
  - 自学 Euler、Lagrange 的微分学
  - 学生时代即旁听 Dirichlet 等人在柏林大学的讲座
- **导师**：Ernst Kummer、Nikolaus Wolfgang Fischer（博士导师）
- **研究领域**：数论、分析、椭圆函数

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **艾森斯坦判别法（最著名贡献）**：判断多项式不可约性的著名判别法（Eisenstein's criterion），是抽象代数中的基本工具。
2. **艾森斯坦整数与艾森斯坦素数**：三次单位根整环中的整数（Eisenstein integer）与素数（Eisenstein prime）。
3. **三次与四次互反律**：在 Crelle's Journal 发表四次互反律的两个证明，以及三次、四次互反律的类似定律。
4. **艾森斯坦级数（Eisenstein series）**：模形式理论中的基本对象（Eisenstein series）。
5. **艾森斯坦互反律（Eisenstein reciprocity）**：数论中的互反律。
6. **天才早逝的传奇**：29 岁死于肺结核，是数学史上英年早逝的天才之一。Alexander von Humboldt 终生资助他，并**亲自护送其灵柩到墓地**。
7. **与 Hamilton 的相遇**：1843 年在都柏林见 William Rowan Hamilton，被介绍 Abel 五次方程不可解证明，激发其研究兴趣。
8. **获 Gauss 赏识**：拜访高斯，获布雷斯劳大学荣誉博士。
9. **荣誉**：1851/1852 年分别当选哥廷根科学院、柏林科学院院士；布雷斯劳大学荣誉博士。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（普鲁士深蓝） | `#1F3A93` | 德意志理性 |
| 强调色（数学金） | `#C9A227` | 天才 / 尊崇 |
| 分类色 1（判别法/整数 — 靛蓝） | `#4C5FD5` | 判别法 / 艾森斯坦整数 |
| 分类色 2（互反律 — 青绿） | `#0E7C7B` | 三次/四次互反律 |
| 分类色 3（级数/椭圆函数 — 琥珀） | `#E07B30` | 艾森斯坦级数 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「三次单位根 / 格点」的视觉语言。

### 3.5 背景音乐选择 ✅ 【已选定】

- **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
- **选定曲目**：**Lonesome**（AShamaluevMusic，优先级 1，`music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav`，3:17，已软链为 `bgm.wav`）
- **匹配理由**：标签"悲伤 / 电影感 / 情感"，适用场景"悲剧人物、逆境、孤独钻研"——完美契合艾森斯坦 29 岁肺结核早逝的天才陨落叙事
- （避免与他片重复：Poncelet 用 The Flow of Time，Cayley 用 Timeless，Hermite 用 Eroica）

## 4. Slide 规划（实际 13 页正文 + OpenMath 封面，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「艾森斯坦」+ 副题「柏林大学讲师 · 29 岁陨落的数论天才」+ 右上头像 + 国籍行 + 底部三要素状态栏 + 4 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1823 出生 → 1837 入 Gymnasium → 1843 都柏林 → 1844 科学院首篇+Crelle 爆发 → 1847 执教 → 1848 革命入狱 → 1851/52 两院院士 → 1852 逝世+洪堡扶灵
4. **神童早年**（1823–1843）：柏林、犹太裔皈依新教、脑膜炎、15 岁掌握中学课程、自学 Euler/Lagrange、老师评价引语、旁听 Dirichlet（4 行表格）
5. **艾森斯坦判别法**（核心贡献页）：判什么/怎么判/为什么常用（表格 + 公式框 $p\mid a_0,\dots,a_{n-1},\ p\nmid a_n,\ p^2\nmid a_0$）
6. **艾森斯坦整数与素数**（核心贡献页）：$\mathbb{Z}[\omega]$、素元、三角格点几何直观（呼应气泡母题；表格 + 公式框）
7. **三次与四次互反律**（核心贡献页）：Gauss 遗产、Crelle 两个证明、艾森斯坦互反律（表格 + 谱系公式框；明确"Gauss 已研究、Eisenstein 首次系统发表证明"）
8. **艾森斯坦级数**（核心贡献页）：定义 $G_{2k}$、椭圆函数来源、现代模形式地位（表格 + 公式框）
9. **都柏林与格廷根**（核心叙事页）：Hamilton 点火、回柏林一年首篇、拜访 Gauss、布雷斯劳荣誉博士（表格）
10. **洪堡的资助与 1848 革命**（核心叙事页）：补助金庇护、1847 habilitation、1848 短暂入狱、两院院士（表格）
11. **天才早逝**（核心叙事页）：1852-10-11 肺结核 29 岁、洪堡扶灵、与 Abel/Galois 并列、1975 AMS 全集（表格）
12. **荣誉与遗产**（`\honorslide`）：生前荣誉 / 以他命名 / 身后影响（itemize 表格）
13. **终章**（`\closingslide`）：「29 年的寿命，不朽的数论基石。」

## 5. 史实陷阱与敏感点（终审必须检查）

- **艾森斯坦判别法**：是"判断多项式不可约性的判据"——是 Eisenstein 的贡献，但需注意该判别法是抽象代数中的工具，勿写"艾森斯坦发明了整环理论"。
- **艾森斯坦整数**：三次单位根整环中的整数——是"定义并研究"，勿夸大。
- **三次与四次互反律**：Eisenstein 发表四次互反律的**两个证明**及三次、四次互反律——是"证明"，勿写他首次提出（高斯已研究过这些定律）。
- **神童评价**：老师评价"他的数学知识远超中学课程范围……有朝一日将为科学的发展与扩展做出重要贡献"——是老师预言，可引用。
- **死亡**：1852-10-11 死于肺结核，年仅 29 岁——是"肺结核"，勿误写其他死因。
- **洪堡护送灵柩**：Alexander von Humboldt 是**终生资助者**，并亲自护送其灵柩到墓地——体现其受敬重，可作叙事点。
- **无肖像**：✅ 已解决——本地 `images.txt` 仅含 Wikiquote logo，但经 Wikipedia API（`prop=pageimages`）查得条目主图 `Gotthold_Eisenstein.jpeg`（Commons c/c0，524×689 竖版肖像），下载至 `images/eisenstein_portrait.jpg`，封面与身份页均采用。
- **国籍**：Kingdom of Prussia（普鲁士王国），今属德国——封面用「德国（普鲁士王国）」。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q61047 | ✅ 已入库（MySQL/data/Gotthold_Eisenstein.yaml） |
| name_zh | 艾森斯坦（或 戈特霍尔德·艾森斯坦） | ✅ 已入库 |
| name_en | Gotthold Eisenstein | ✅ 已入库 |
| birth_date | 1823-04-16 | ✅ 已入库 |
| death_date | 1852-10-11 | ✅ 已入库 |
| nationality | Germany（普鲁士王国） | ✅ 已入库 |
| primary_occupation | mathematician | ✅ 已入库 |
| field_of_work | number theory / elliptic function | ✅ 已入库 |
| has_biography | true | ✅ 本次置 true；另修正 relations 中 Gauss 备注（"学生"→"拜访并受赏识（非正式师承）"） |

## 7. 社会关系入库清单（§20）

- **博士导师**：Ernst Kummer、Nikolaus Wolfgang Fischer
- **师承 / 旁听**：Peter Gustav Lejeune Dirichlet（学生时代旁听其讲座）
- **学术相关**：William Rowan Hamilton（1843 都柏林相遇，介绍 Abel 证明）、Carl Friedrich Gauss（拜访并获赏识）
- **资助者**：Alexander von Humboldt（终生资助、护送灵柩）

## 8. 奖项清单

- 布雷斯劳大学（University of Wrocław）荣誉博士
- 1851 年哥廷根科学院院士、1852 年柏林科学院院士

## 9. 机构清单

- 教育：Frederick William University Berlin（柏林大学）、University of Wrocław（荣誉博士）、Ludwig Cauer primary school、Friedrich-Wilhelms-Gymnasium、Friedrichswerder Gymnasium
- 任职：Frederick William University Berlin（1847 起任教）

## 10. 终审清单

- [x] 生卒 1823-04-16 / 1852-10-11，享年 29，出生地柏林
- [x] 艾森斯坦判别法"多项式不可约性判据"表述准确（Slide 5：判什么/怎么判/为什么常用，公式框完整）
- [x] 艾森斯坦整数"三次单位根整环"表述准确（Slide 6：$\mathbb{Z}[\omega]$ 定义 + 三角格点几何直观，勿夸大）
- [x] 三次/四次互反律"证明、高斯先行"表述准确（Slide 7：明确"Gauss 已研究，Eisenstein 在 Crelle 发表两个证明及类似定律"，谱系图注明）
- [x] 神童评价引用准确（Slide 4：老师评价按 page.md 原文直译引用）
- [x] 死亡"肺结核 29 岁"表述准确（Slide 11：1852-10-11 肺结核，与 Abel/Galois 并列）
- [x] 洪堡"终生资助、护送灵柩"表述准确（Slide 10 / 11）
- [x] 头像确认（✅ Wikipedia API 查得条目主图，`images/eisenstein_portrait.jpg`）
- [x] 国籍用「德国（普鲁士王国）」表述准确
- [x] **引语红线**：封面与 Slide 9 金句原为"高斯曾说三个划时代数学家"（不在 Wikipedia 原文，来自外部流传）——已改为忠实转述「获 Gauss 赏识、受洪堡庇护」
- [x] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景（三次单位根/格点母题）+ 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误，Overfull = 0（一次通过）；`make images && make video` 完成（BGM: Lonesome）

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [x] **结合本地 Wikipedia**：逐页对照 Beamer tex 全部事实（生卒、Gymnasium、都柏林 1843、Crelle 发表、habilitation 1847、入狱 1848、两院院士 1851/52、死因均与 page.md 一致）
- [x] **头像**：✅ 经 Wikipedia API 查得条目主图并下载（`images/eisenstein_portrait.jpg`），封面与身份页均采用
- [x] **国籍**：封面顶部徽章明示德国（普鲁士王国）
- [x] **引语核对**：老师评价按 page.md 原文引用；"高斯三个划时代数学家"名言不在原文，已从封面与 Slide 9 移除并改为忠实转述
- [x] **编译验证**：`make distclean && make` 一次通过，14 页 PDF，Overfull = 0；`make images && make video` 完成（BGM: Lonesome）
- [x] **更新提示词**：Review 修正已写回本文件

### 第 2 轮（Review-2）：结构优化
- [x] 检查 Overfull/Underfull 告警：Overfull = 0（一次通过）
- [x] 身份信息页布局与 Wilson 模板对齐（左肖像 2.95×3.9 + 右 2×2 网格）
- [x] 中文标点 / 断行 / 间距统一（引语用半角 " "）
- [x] 与同世纪数学家（Boole / Poncelet / Cayley / Hermite）格式对齐（同模板、同结构、同收尾页式样）

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
