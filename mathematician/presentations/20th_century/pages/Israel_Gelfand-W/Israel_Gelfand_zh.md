# Israel Moiseevich Gelfand（伊斯雷尔·盖尔范德）立传提示词

> qid=Q315414 · 1913-09-02 – 2009-10-05 · 苏联/美国数学家 · 20 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/20th_century/pages/Israel_Gelfand-W/`（page.md + metadata.json + images.txt）
> （注：本项目 Gelfand 的 page.md/metadata.json 尚未落盘，事实以已有提示词 Review 记录 + Wikipedia 条目为准）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 苏联 → 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「算子代数格点 / 表示论」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Israel Moiseevich Gelfand（俄语 Изра́иль Моисе́евич Гельфа́нд，中文惯称：盖尔范德/盖尔方德）
- **生卒**：1913-09-02 生于 Okny（Kherson Governorate，俄罗斯帝国，今乌克兰敖德萨州）→ 2009-10-05 逝于美国新泽西州 New Brunswick，享年 96（距 96 岁生日仅 5 周）
- **国籍**：俄罗斯帝国 → 苏联 → 美国（1989 年 76 岁移民美国）
- **身份**：数学家（泛函分析、表示论、积分几何、广义函数、自守形式）
- **家庭**：出生于乌克兰犹太家庭，父亲是磨坊主（苏联体制下成为其被中学开除的理由）
- **教育轨迹**：
  - 约 1927 因父亲是磨坊主被苏联高中开除，此后自学成才
  - 无高中文凭、无大学学位
  - 1932 年 19 岁跳过高中学历，直接进入莫斯科大学读研，导师 Kolmogorov
  - 1935 年 22 岁获博士学位（Candidate of Sciences，苏联副博士）
- **导师**：Andrey Kolmogorov（苏联数学泰斗，概率论/拓扑学/动力学奠基人）
- **研究领域**：泛函分析、算子代数、表示论、积分几何、广义函数、微分方程、自守形式、变分法

## 2. 核心叙事亮点（用于 Slide 4-12）

1. **被开除的犹太少年**：约 1927 年因父亲是磨坊主被苏联中学开除，没有高中文凭和大学学位，完全自学成才——20 世纪数学史上最著名的"体制外天才"叙事。
2. **19 岁被 Kolmogorov 收为研究生**（1932）：苏联数学泰斗 Kolmogorov 的慧眼识珠，改变了 Gelfand 的命运。
3. **22 岁获博士**（1935）：仅用 3 年完成博士论文（Candidate of Sciences）。
4. **Gelfand–Mazur 定理**（1938）：任何复可除 Banach 代数同构于复数域 ℂ，奠定 Banach 代数理论近一个世纪的方向。
5. **Gelfand 表示**（1941）：交换 Banach 代数 ↔ 紧 Hausdorff 空间上的连续函数——深刻的"几何化"对应，Grothendieck 概形理论的精神先声。
6. **Gelfand–Naimark 定理**（1943）：C*-代数的基本表示定理；**GNS 构造**（Gelfand–Naimark–Segal）是量子力学数学基础的核心工具。
7. **Gelfand–Tsetlin 基**（1950）：酉群表示的显式基，理论物理中处理角动量耦合的标准工具。
8. **Gelfand–Levitan–Marchenko 方程**（1950s）：逆散射理论与 soliton 理论的数学基石（KdV 可积性基于此）。
9. **广义函数五卷**（1958–1966，与 Shilov/Vilenkin/Graev 合著）：该领域的经典圣经。
10. **BGG 对应**（1976，Bernstein–Gelfand–Gelfand）：半单李代数范畴 𝒪 的里程碑，统一 Verma 模奇点与 Weyl 群作用。
11. **Gelfand Seminar**（1943–2009）：每周一晚、持续 46 年、培养 27 位博士（含 Szemerédi）——苏联数学黄金时代的"冶炼炉"。
12. **自守形式与表示论的联系**（与 Fomin、Piatetski-Shapiro）：Langlands 纲领的苏联先声。
13. **荣誉**：首届 Wolf Prize（1978，与 Siegel 共享）、Kyoto Prize（1989）、MacArthur Fellowship（1994）、Steele Prize 终身成就（2005）、ForMemRS（1977）、Wigner Medal（1980）、Order of Lenin ×3。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（苏联深红） | `#8B1E3F` | 苏联 / 莫斯科 / 十月革命红 |
| 强调色（数学金） | `#C9A227` | Wolf Prize 首届 / 尊崇 |
| 分类色 1（泛函分析 — 靛蓝） | `#4C5FD5` | Gelfand 表示 / Banach 代数 |
| 分类色 2（表示论 — 青绿） | `#0E7C7B` | BGG 对应 / Tsetlin 基 |
| 分类色 3（分析与几何 — 琥珀） | `#E07B30` | 广义函数 / 积分几何 / GLM |
| 分类色 4（传承 — 玫红） | `#B76E79` | Gelfand Seminar / 27 位博士 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「算子代数格点 / 表示论」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**深沉庄重 / 苏俄宏大**（"苏联数学的灵魂"的深沉与辽阔）
- **匹配理由**：
  - Gelfand 是 20 世纪苏联数学学派的灵魂人物，出身乌克兰犹太村庄、历经苏联体制——需**深沉、庄重**的配乐
  - "宏大" 匹配其贡献的广度（泛函分析到表示论到积分几何）
  - "苏俄气质" 匹配其莫斯科学术生涯与 96 岁的世纪跨越
- **候选方向**（执行时从音乐库核对具体曲目，优先深沉/庄重/苏俄风格）：
  - 首选：肖斯塔科维奇式深沉的古典风格
  - 备选：宏大弦乐 / 历史感深沉曲目
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「苏联数学的灵魂 · 泛函分析与表示论的奠基者」+ 盖尔范德 1913–2009 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **盖尔范德的一生：时间线**（`\timelineslide`）：1913 出生 → 1932 Kolmogorov 研究生 → 1935 博士 → 1938 G–Mazur → 1943 Gelfand Seminar → 1978 Wolf 首届 → 1989 移民美国 → 2009 去世
4. **早年：被开除的犹太少年**（`\earlyslide`，表格）：Okny → 被开除 → Kolmogorov → 22 岁博士
5. **Banach 代数与 Gelfand 表示**（核心贡献页，表格 + 公式框）：G–Mazur 定理、Gelfand 表示
6. **C*-代数与 GNS 构造**（核心贡献页，表格 + 公式框）：Gelfand–Naimark 定理、GNS 构造
7. **表示论**（核心贡献页，表格 + 公式框）：BGG 对应、Gelfand–Tsetlin 基、Verma 模
8. **广义函数与积分几何**（核心贡献页，表格 + 公式框）：广义函数五卷、GLM 方程
9. **Gelfand Seminar**（表格）：46 年每周一晚、27 位博士
10. **自守形式与 Langlands 先声**（表格）：与 Fomin、Piatetski-Shapiro
11. **Wolf Prize 与荣誉**（表格）：Wolf 1978 首届、Kyoto、MacArthur、Steele
12. **传承**（表格）：Szemerédi（Abel 2012）等学生
13. **终章**：96 岁、苏联数学灵魂的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **学历**：⚠️ 被苏联中学开除，**没有高中文凭、没有大学学位**，19 岁直接读研——勿写"大学本科毕业"。
- **博士学位**：1935 年获的是苏联 **Candidate of Sciences（副博士）**，不是西方的 Ph.D.——表述时写"博士（Candidate of Sciences）"。
- **国籍**：俄罗斯帝国 → 苏联 → 美国，1989 年 76 岁移民美国——封面用「苏联 → 美国」。
- **GNS 构造**：Gelfand–Naimark–Segal，Segal 是 Irving Segal（数学家），勿混淆。
- **首届 Wolf Prize**：1978 年首届数学奖，**与 Carl Ludwig Siegel 共享**——勿写"独自获得"。
- **Szemerédi**：Gelfand 的博士生，2012 年获 Abel 奖——学生成就，非 Gelfand 本人 Abel 奖。
- **广义函数**：5 卷 + 1 卷（2015 AMS 再版），与 Shilov、Vilenkin、Graev 等合著——勿写"独自撰写"。
- **逝世**：2009-10-05 于 New Brunswick, NJ，96 岁，距生日仅 5 周。
- **出生地**：Okny 今属乌克兰，但 1913 年属俄罗斯帝国——表述"俄罗斯帝国 Okny（今乌克兰）"。
- **Gelfand Seminar 时间**：1943–1989 在 MSU，1990–2009 迁至 Rutgers——勿写"只在莫斯科"。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q315414 | 待写入 |
| name_zh | 伊斯雷尔·盖尔范德 | 待写入 |
| name_en | Israel Gelfand | 待写入 |
| birth_date | 1913-09-02 | 待写入 |
| death_date | 2009-10-05 | 待写入 |
| nationality | Soviet Union / United States | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | functional analysis / representation theory / integral geometry | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **博士导师**：Andrey Kolmogorov
- **学生**：Endre Szemerédi（Abel 2012）、Alexandre Kirillov、Joseph Bernstein、David Kazhdan、Edward Frenkel、Andrei Zelevinsky 等 27 位博士生
- **合作者**：Mark Naimark（Gelfand–Naimark 定理）、Georgiy Shilov（广义函数）、Naum Vilenkin（广义函数）、Mark Graev（积分几何）、Sergei Fomin（变分法）、Ilya Piatetski-Shapiro（自守形式）、Mikhail Kapranov（判别式）、Andrei Zelevinsky（判别式/丛代数）
- **竞争/共享**：Carl Ludwig Siegel（Wolf 1978 共享）

## 8. 奖项清单

- Wolf Prize（1978，首届数学奖，与 Carl Ludwig Siegel 共享）
- Kyoto Prize（1989，稻盛财团）
- MacArthur Fellowship（1994，天才奖）
- Leroy P. Steele Prize 终身成就（2005，AMS）
- Foreign Member of the Royal Society（ForMemRS，1977）
- Wigner Medal（1980）
- Order of Lenin ×3（苏联最高平民荣誉）
- Stalin Prize、Lenin Prize

## 9. 机构清单

- 教育：Moscow State University（1935 年获 Candidate of Sciences）
- 任职：Moscow State University（1935–1989）；Rutgers University（1989–2009）
- 学术活动：Gelfand Seminar（1943–2009，MSU 与 Rutgers）

## 10. 终审清单

- [ ] 生卒 1913-09-02 / 2009-10-05，享年 96，出生地 Okny（今乌克兰）
- [ ] 学历"被中学开除、无高中文凭、无大学学位、19 岁直读研"表述准确
- [ ] 博士"1935 Candidate of Sciences"表述准确
- [ ] 国籍"苏联 → 美国"表述准确
- [ ] Wolf Prize"1978 首届、与 Siegel 共享"表述准确
- [ ] GNS 构造"Gelfand–Naimark–Segal"表述准确
- [ ] 广义函数"5 卷 + 合著"表述准确
- [ ] Gelfand Seminar"1943–2009、46 年、27 位博士"表述准确
- [ ] 学生 Szemerédi"Abel 2012"表述准确
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合 Wikipedia**：核对生卒、博导、奖项年代、核心定理命名
- [ ] **头像**：使用 `images/Israel_Gelfand.jpg`（284×400 竖版肖像）
- [ ] **国籍**：封面顶部徽章明示「苏联 → 美国」
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如 NYT "among the greatest mathematicians of the 20th century"）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Harish-Chandra / Grothendieck）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
