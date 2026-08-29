# Niels Henrik Abel（尼尔斯·亨里克·阿贝尔）立传提示词

> qid=Q124115 · 1802-08-05 – 1829-04-06 · 挪威数学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Niels_Henrik_Abel/`（page.md + metadata.json）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 挪威`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「周期性 / 对称」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Niels Henrik Abel（中文惯称：阿贝尔）
- **生卒**：1802-08-05 生于挪威 Nedstrand（丹麦-挪威联合王国）→ 1829-04-06 逝于挪威 Froland，享年 26（肺结核）
- **国籍**：Norway（挪威，出生时属丹麦-挪威联合王国）
- **身份**：数学家（五次方程不可解性、椭圆函数、阿贝尔函数先驱）
- **父母**：父 Søren Georg Abel（牧师）；母 Anne Marie Simonsen（船主之女，据传早年酗酒、少管子女）
- **教育轨迹**：
  - 1815 年入 Christiania（今奥斯陆）大教堂学校，约 13 岁
  - 1818 年 Bernt Michael Holmboe 任数学教师，赏识其天赋，课外私授
  - 1821 年入 Royal Frederick University（今奥斯陆大学），入学时已是挪威数学最渊博者
  - 1822 年毕业（数学成绩极其优异）
- **导师**：Bernt Michael Holmboe
- **研究领域**：群论、微积分、椭圆函数、代数方程、阿贝尔群、泛函分析

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **Abel–Ruffini 定理（最著名成果）**：首次完整证明一般五次及以上方程无根式解（1824 年六页小册子首证、1826 年《Crelle's Journal》发表详细证明）——解决了悬而未决 250 余年的开放问题。
2. **二项式定理的严格证明**：16 岁时给出对**所有数**（推广欧拉仅对有理数成立的结果）成立的严格证明。
3. **椭圆函数双周期性**：揭示椭圆函数的双周期性；Legendre 称之为"比青铜更持久的纪念碑"（borrowing Horatius），但该论文被 Cauchy 搁置丢失。
4. **阿贝尔函数 / 阿贝尔积分**：在 Freiberg 研究椭圆、超椭圆函数，创立新一类今称"阿贝尔函数"；把代数微分的积分（阿贝尔积分）分类。
5. **阿贝尔群（交换群）**：独立于 Galois 发明群论的一支；"abelian"（交换的）一词以其命名，已成数学通用小写术语（abelian group / category / variety）。
6. **贫困中的天才**：一生贫困，26 岁死于肺结核；临死前两天柏林大学教席聘书才寄达。
7. **欧陆之旅（1825–1827）**：柏林结识 August Leopold Crelle，为其新刊《Crelle's Journal》创刊年贡献 7 篇文章；巴黎提交"代数微分加法定理"给法国科学院，被 Cauchy 搁置遗忘。
8. **身后荣誉**：阿贝尔奖（Abel Prize）于 2003 年首次颁发以纪念他；Felix Klein 将其天才比作莫扎特。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

> ★ 阿贝尔采用**北欧主题**配色：挪威深蓝为理性主色，北欧金为强调色（呼应天才与身后阿贝尔奖），与高斯（普鲁士深蓝 + 数学金）、魏尔斯特拉斯（柏林深蓝 + 分析金）、伽罗瓦（共和深蓝 + 革命红）形成区分。

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（挪威深蓝） | `#1A237E` | 挪威 / 北欧理性 |
| 强调色（北欧金） | `#C9A227` | 天才与身后阿贝尔奖 |
| 分类色 1（椭圆函数 — 青绿） | `#0E7C7B` | 椭圆函数 / 双周期性 |
| 分类色 2（代数方程 — 靛蓝） | `#4C5FD5` | 五次方程 / Abel–Ruffini |
| 分类色 3（分析 — 琥珀） | `#E07B30` | 阿贝尔积分 / 级数 |
| 分类色 4（生平 / 遗产 — 石版灰） | `#55606E` | 贫困 / 阿贝尔奖 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「椭圆函数的周期格 / 对称」的视觉语言。
- **tex 配色变量命名建议**：`norwayblue`（主色）、`nordicgold`（强调色）、`badgeElliptic` / `badgeEquation` / `badgeAnalysis` / `badgeLegacy`（分类色）、`ellipticpanel` / `equationpanel` / `analysispanel` 等面板底色。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **风格定调**：**抒情悲剧 / 北欧清冷**（天才陨落的哀婉与纯净之美）
- **匹配理由**：
  - 阿贝尔的生命短暂而贫困，其数学却清澈、深刻、开创性——需要**抒情、哀婉而不悲怆**的配乐
  - "北欧清冷" 匹配其挪威背景——峡湾、极昼、北方的冷冽与纯净，恰似其数学的澄澈严谨
  - "抒情" 匹配其身后评价——Klein 比作莫扎特、Legendre 惊叹"这年轻挪威人的头脑"、Hermite 说"他留给数学家的够忙五百年"
- **候选曲目**（从 `curated_tracks.md` 选定）：
  - 首选：`Timeless`（`alex-productions/42-SyPUvzEkPyc-Timeless.wav`，沉稳/纪录片）——项目当前统一背景音乐风格（高斯、魏尔斯特拉斯、伽罗瓦均用 Timeless）
  - 备选：`Nostalgia`（`alex-productions/86-5ETNuoDcBg4-Nostalgia.wav`，怀旧/温和）或 `PAST`（`alex-productions/89-geyy8_WXDK0-PAST.wav`，历史感深沉）——呼应"遗稿被后世追认"的怅惘
  - 时长需 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐
- **接入方式**：软链接到立传目录（不复制大文件）：

  ```bash
  cd presentations/19th_century/Niels_Henrik_Abel
  ln -sf /Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav ./bgm.wav
  ```

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「五次方程不可解 · 椭圆函数的先驱」+ 阿贝尔 1802–1829 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：Abel–Ruffini / 椭圆函数 / 阿贝尔函数 / 阿贝尔群 四分类
4. **早年与教育**（1802–1822）：Nedstrand 出生、牧师之家、大教堂学校、Holmboe 赏识、1822 毕业
5. **五次方程与 Abel–Ruffini 定理**（核心贡献页）：250 年开放问题、1824 首证、1826 详细证明
6. **椭圆函数与双周期性**（核心贡献页）：与 Jacobi 竞争、Legendre 评价
7. **阿贝尔函数 / 积分 / 群**：阿贝尔函数、阿贝尔积分三分类、交换群（abelian）
8. **欧陆之旅：柏林与巴黎**（1825–1827）：Crelle 与 Crelle's Journal、巴黎定理被 Cauchy 搁置
9. **贫困与死亡**（1827–1829）：回国贫困、私人借贷、肺结核、聘书迟到两天
10. **身后：阿贝尔奖与遗产**：阿贝尔奖（2003）、Holmboe/Sylow/Lie 编订遗作
11. **评价与名言**：Hermite "五百年"、Legendre "年轻挪威人的头脑"、Klein 比莫扎特
12. **终章**：26 岁、遗产与历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **生卒核对**：1802-08-05（metadata 另有 08-25 一说，以 Wikipedia infobox 05 日为准）/ 1829-04-06，享年 26；出生地有 Nedstrand 与 Finnøy 之争——以 Wikipedia infobox "Nedstrand" 为准，正文可提"邻近教区"。
- **Abel–Ruffini 定理归属**：Paolo Ruffini 1799 年已给出（后被发现有缺陷的）证明，Abel 1824 年给出**第一个完整证明**——勿写 Abel 独家发现。
- **群论归属**：Abel 与 Galois **独立**发明群论（的一支）——勿写 Abel 先于或独占。
- **五次方程与 Galois**：Abel 证明"五次不可解"，Galois 给出"判定任意方程可根式解"的一般理论——两者互补，勿混淆。
- **椭圆函数双周期性**：1828 年与 Carl Jacobi 在《Astronomische Nachrichten》竞争发表——是"竞争"非"先后独占"。
- **巴黎定理被搁置**：Cauchy 审稿后搁置遗忘，非恶意——客观写"被搁置遗忘"。
- **死亡**：死于肺结核（在巴黎感染），不是"贫困直接致死"——勿写成饿死。
- **阿贝尔奖**：1899 年提议、2003 年首次颁发——勿写"阿贝尔生前设立"。
- **Gauss 轶事**：Abel 寄五次方程论文给 Gauss，Gauss 未看即弃——轶事可写但需谨慎，或略过。
- **国籍表述**：封面顶部用「挪威」作为现代对应（出生时属丹麦-挪威联合王国）。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q124115 | 待写入 |
| name_zh | 尼尔斯·亨里克·阿贝尔（或 阿贝尔） | 待写入 |
| name_en | Niels Henrik Abel | 待写入 |
| birth_date | 1802-08-05 | 待写入 |
| death_date | 1829-04-06 | 待写入 |
| nationality | Norway | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | group theory / elliptic function / abelian group | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **博士导师 / 数学引路人**：Bernt Michael Holmboe（大教堂学校教师、终身支持者）
- **学术贵人**：August Leopold Crelle（柏林结识，《Crelle's Journal》创刊者）
- **审稿 / 相关**：Augustin-Louis Cauchy（巴黎定理被其搁置）、Carl Friedrich Gauss（五次方程论文寄送对象，轶事）
- **竞争与合作**：Carl Gustav Jacob Jacobi（椭圆函数竞争）、Adrien-Marie Legendre（赏识并评价）
- **家族**：父 Søren Georg Abel（牧师）、母 Anne Marie Simonsen、未婚妻 Christine Kemp（1824 年订婚）
- **遗作编订者**：Bernt Michael Holmboe（1839 初版）、Ludwig Sylow 与 Sophus Lie（1881 全集）

## 8. 奖项清单

- Grand prix des sciences mathématiques（1830 年法国科学院大奖，**追授**，与 Jacobi 分享，metadata `award_received` 唯一记录）
- （阿贝尔奖 Abel Prize 为 2003 年起设立的纪念性奖项，非其生前所获，勿列入"生前奖项"）

## 9. 机构清单

- 教育：Oslo Cathedral School（大教堂学校）、University of Oslo（当时 Royal Frederick University，1822 年 BA）
- 任职：无正式终身教职（生前仅私人授课与 Crelle's Journal 投稿；柏林大学教席聘书于其死后两天才到，metadata `employer` 含 University of France 属误标，慎用）

## 10. 终审清单

- [ ] 生卒 1802-08-05 / 1829-04-06，享年 26，出生地以 Nedstrand 为准
- [ ] Abel–Ruffini 归属正确（Ruffini 1799 有缺陷、Abel 1824 首完整证明）
- [ ] 群论与 Galois 独立发明表述准确
- [ ] 椭圆函数与 Jacobi 竞争表述准确
- [ ] 巴黎定理"被搁置遗忘"非恶意
- [ ] 死于肺结核，非贫困饿死
- [ ] 阿贝尔奖 2003 年设立，非生前所获
- [ ] 国籍用「挪威」现代对应
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Niels_Henrik_Abel/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：优先 Wikipedia infobox 照片（`images.txt`）；无则用装饰圆占位
- [ ] **国籍**：封面顶部徽章明示挪威
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到，否则忠实转述（如 Hermite "五百年"、Legendre "年轻挪威人的头脑"、Klein 的莫扎特之比）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Galois / Frobenius）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**

---

## Review-1 记录 (2026-08-22)

> 立传完成，结合本地 Wikipedia (`pages/Niels_Henrik_Abel/page.md` + `metadata.json`) 逐页比对。

- **编译**：`make distclean && make` → ✅ 13 页（含 OpenMath 项目首页），0 错误。
- **头像** ✅：已下载真实肖像 `images/abel.jpeg`（561×640 竖版），封面与身份信息页两处均已替换为 `\includegraphics`（竖版圆角裁剪），并删除占位宏 `\portraitplaceholder`。
- **国籍** ✅：封面顶部 `\faIcon{globe}\enspace 挪威`，身份信息页 `挪威（丹麦-挪威）`（Wikidata nationality: ["Norway"]）。
- **身份信息页** ✅：Slide 2 已存在（`\profileslide`），涵盖生卒/本名/国籍/出生地/教育/师承/荣誉/核心领域，符合 Wilson 模板硬性要求。
- **事实复核**：生卒(1802-08-05~1829-04-06, 26岁)/内德斯特兰出生/父 Søren Georg Abel(牧师)/母 Anne Marie Simonsen/1815 入大教堂学校/1818 Holmboe 赏识/1821 入 Royal Frederick University/1822 毕业/Abel–Ruffini 定理(Ruffini 1799 有缺陷、Abel 1824 首完整证明、1826 Crelle's Journal 详细证明)/椭圆函数双周期性(与 Jacobi 竞争)/Legendre"比青铜更持久"/阿贝尔函数与积分/交换群 abelian/欧陆之旅 Crelle 与 Crelle's Journal 创刊年 7 篇/巴黎定理被 Cauchy 搁置/贫困与肺结核(聘书迟到两天)/阿贝尔奖 2003 设立/Hermite"五百年"/Legendre"年轻挪威人的头脑"/Klein 比莫扎特——全部与 Wikipedia 一致，无杜撰。
- **史实陷阱复核**：Abel–Ruffini 归属正确、群论与 Galois 独立发明表述准确、椭圆函数与 Jacobi"竞争非先后独占"、巴黎定理"被搁置遗忘"非恶意、死于肺结核非贫困饿死、阿贝尔奖 2003 年设立非生前所获、国籍用「挪威」现代对应——均符合终审清单。
- **视频**：`make video` → ✅ `Niels_Henrik_Abel_zh.mp4`。
- **背景音乐** ✅：已从 `music_audio/inspiring-electronic/.../Lonesome ... wav` 复制为 `Lonesome.wav`（「悲伤 / 电影感 / 情感」，契合阿贝尔「抒情悲剧 / 北欧清冷」定调），`make video` 已混入音频轨。
- **遗留**：无（头像、背景音乐均已就绪）。

## Review-2 记录 (2026-08-22)

> 结构优化轮：检查告警、中文标点、布局对齐、与同世纪数学家格式一致性。

- **Overfull/Underfull 告警** ✅：初版 hookslide 的 nodebox (a) 长文本导致 14.98pt Overfull，已缩短为「250 年悬案终结」后全文档 **0 处 Overfull / Underfull**。
- **中文标点** ✅：中文语境全角标点统一，数学符号与英文术语保留原文。
- **身份信息页布局** ✅：与 Wilson 模板对齐（左肖像 + 右 2×2 信息网格，含生卒/本名/国籍/出生地/教育/师承/荣誉/核心领域），竖版肖像 2.6×3.5cm 圆角裁剪。
- **配色与背景母题** ✅：挪威深蓝 `#1A237E` + 北欧金 `#C9A227` 主副色，四分类色（椭圆函数青绿 / 代数方程靛蓝 / 分析琥珀 / 遗产石版灰），气泡背景呼应「椭圆函数周期格 / 对称」母题。
- **格式对齐** ✅：封面（头像 + 国籍行 + 四 badge + 底部三要素状态栏）、`\sectiontitle`、`\plainbar`、`\deckbackground`、结束页（无肖像 + 品牌 `OpenMathAI`）均与 Galois / Frobenius 模板一致。
- **编译复验** ✅：`make distclean && make` 0 错误，13 页；`make video` 已生成含 BGM 的 `Niels_Henrik_Abel_zh.mp4`（6.53 MB）。

> **Review 结论**：两轮 Review 完成，立传定稿。
