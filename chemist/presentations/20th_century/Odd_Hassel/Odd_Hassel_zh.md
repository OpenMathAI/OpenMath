# Odd Hassel（奥德·哈塞尔）立传提示词

> qid=Q157212 · 1897-05-17 – 1981-05-11 · 挪威物理化学家 · 20 世纪 · 诺贝尔化学奖（1969，与 Derek Barton 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Odd_Hassel/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页 + 气泡背景，是本次重写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从 `images.txt` / Commons 下载；404 则用装饰圆占位并在 Review 记录）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 环己烷的立体真相\enspace·\enspace 挪威`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「环己烷椅式构象」母题——离散圆点暗示原子在三维空间中的排布。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Odd Hassel（中文惯称：奥德·哈塞尔；"Odd" 是挪威常见男名，勿意译）
- **生卒**：1897-05-17 生于挪威 Kristiania（今奥斯陆）→ 1981-05-11 逝于奥斯陆，享年 83
- **国籍**：Norway（挪威）
- **身份**：物理化学家（physical chemist）、1969 年诺贝尔化学奖得主
- **家庭**：父 Ernst Hassel（1848–1905）为妇科医生，母 Mathilde Klaveness（1860–1955）；父早逝时哈塞尔 8 岁
- **教育轨迹**：
  - 1915 入 University of Oslo，修数学、物理与化学，1920 毕业
  - 慕尼黑 Kasimir Fajans 实验室工作（发现吸附指示剂）
  - 柏林 Kaiser Wilhelm Institute 从事 X 射线晶体学研究（洛克菲勒奖学金，得 Fritz Haber 之助）
  - 1924 获 Humboldt University of Berlin PhD
- **博士导师**：Heinrich Jacob Goldschmidt（柏林时期论文导师；其子 Victor Goldschmidt 是哈塞尔在奥斯陆求学初期的 tutor）
- **研究领域**：物理化学——分子结构、环己烷及其衍生物构象、电偶极矩、电子衍射

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **克里斯蒂安尼亚之子（1897）**：生于 Kristiania（今奥斯陆）；妇科医生之家，8 岁丧父。
2. **双 Goldschmidt 的引路（1915–1920）**：Victor Goldschmidt 是其入学初期的 tutor；Victor 之父 Heinrich Jacob Goldschmidt 后来成为其论文导师——父子二人是哈塞尔一生的重要人物与朋友。
3. **慕尼黑与吸附指示剂（1920s 初）**：在 Kasimir Fajans 实验室工作，成果导向**吸附指示剂**的发现。
4. **柏林与 X 射线晶体学（1920s）**：Kaiser Wilhelm Institute 开始 X 射线晶体学研究；靠 Fritz Haber 帮助获得洛克菲勒奖学金；1924 年获柏林洪堡 PhD。
5. **回归奥斯陆（1925–1964）**：母校执教近四十年，1934 年升教授。
6. **转向分子结构（1930 起）**：从无机化学转向分子结构问题，聚焦**环己烷及其衍生物**。
7. **把新方法带回挪威**：将**电偶极矩**与**电子衍射**概念引入挪威科学界。
8. **三维分子几何（★ 核心贡献）**：当时通行的信念是环状碳分子躺在平面上；哈塞尔用碳氢键数目证明分子**不可能只存在于一个平面**——确立分子几何的三维性，奠定 1969 诺奖。
9. **二战囚禁（1943–1944）**：1943 年 10 月与奥斯陆大学同事被 Nasjonal Samling 逮捕并移交占领当局，辗转多个拘留营，1944 年 11 月获释。
10. **1969 诺贝尔化学奖**：与英国化学家 Derek Barton 共享——巴顿正是基于哈塞尔积累的实验结果创立构象分析。
11. **挪威双奖章（1964）**：挪威化学学会 Guldberg-Waage Medal 与皇家科学与文学院 Gunnerus Medal 同年颁发。
12. **国际荣誉**：哥本哈根大学（1950）与斯德哥尔摩大学（1960）荣誉博士；1960 年获 St. Olav 骑士勋章；伦敦化学会、挪威科学与文学院、丹麦与瑞典皇家科学院等荣誉会士；奥斯陆大学设年度 Hassel 讲座。
13. **诺奖演讲（1970-06-09）**：题目 *Structural Aspects of Interatomic Charge-Transfer Bonding*——从环己烷构象延伸到原子间电荷转移键。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（勃艮第红 burgundy） | `#7A1E28` | 北欧冬夜与分子刚性的深沉（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（分子结构 badgeMol） | `#1E4E79` | 蓝环己烷 / 三维几何 |
| 分类色 2（衍射方法 badgeDiffr） | `#2E7D4F` | 绿电子衍射 / X 射线晶体学 |
| 分类色 3（战时岁月 badgeWar） | `#6E4A1E` | 暗金拘留营 / 1943–1944 |
| 分类色 4（荣誉与传承 badgeHonor） | `#5B2A6E` | 紫 St. Olav / 双奖章 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「环己烷椅式构象的原子排布」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Lonesome** — AShamaluevMusic（文件：`music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav`；不要复制 wav 到人物目录，video 阶段按路径引用）
- **风格**：忧伤 / 情感 / 纪录片
- **匹配理由**：
  - "忧伤" 匹配其人生底色——8 岁丧父、二战中被囚一年、一生僻居奥斯陆一校
  - "情感" 匹配孤勇者的科学坚守——在纳粹占领下的挪威仍守住了实验室的火种
  - "纪录片" 匹配传记叙事——Kristiania → 慕尼黑 → 柏林 → 奥斯陆 → 诺奖
- **时长核对**：video 阶段用 ffmpeg `-shortest` 自动对齐 15 页 × 7 秒 ≈ 105 秒

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 环己烷的立体真相 / Odd Hassel 1897–1981 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍/教育/博士导师/出生地/去世地/领域/荣誉）
03  哈塞尔的一生 — Sanger 式时间线（10 节点：1897→1915→1920→1924→1925→1934→1943→1964→1969→1981）
04  早年与双 Goldschmidt (1897–1920) — 表格「时间|事件|结果」
05  慕尼黑与柏林 (1920–1924) — 表格「地点|方法|结果」（吸附指示剂 / X 射线晶体学 / PhD）
06  奥斯陆四十年 (1925–1964) — 表格「时间|职务|结果」
07  三维分子几何（★ 核心页）— 表格「问题|方法|结果」+ 公式框：环己烷 C6H12 非平面论证
08  二战囚禁 (1943–1944) — 表格「时间|事件|结果」
09  1969 诺贝尔化学奖 — 表格「人物|贡献|理由」+ 公式框：与 Barton 共享
10  方法论遗产 — 表格「方法|引入挪威|意义」（偶极矩 / 电子衍射 / X 射线）
11  荣誉与骑士 — Sanger 式「类别|代表|意义」表格（Guldberg-Waage / Gunnerus / St. Olav / 荣誉博士）
12  传承：Hassel 讲座 — 表格「形式|内容|意义」+ 1970 诺奖演讲题目
13  遗产：把环立起来 — 四分类遗产盒 + 公式框：构象概念 → Barton 构象分析
14  结尾 — 「分子从不躺平，它们以三维的姿态存在。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1969 获奖口径 | 与 Derek Barton **共享**（非独享）；page.md 措辞 "awarded the Nobel Prize in Chemistry for 1969 / shared with English chemist Derek Barton" |
| 双 Goldschmidt 角色 | Victor Goldschmidt 是**入学初期 tutor**（勿写成博士导师）；Heinrich Jacob Goldschmidt 是**论文导师**——两人是父子，勿混淆 |
| 博士授予机构 | 1924 年 PhD 由**柏林洪堡大学**授予——勿写奥斯陆 |
| 慕尼黑成果 | 在 Fajans 实验室导向**吸附指示剂**的发现——勿写成哈塞尔独立"发明"指示剂 |
| Haber 角色 | Fritz Haber 只是**帮助他获得洛克菲勒奖学金**——勿写成师承或合作者 |
| 囚禁细节 | 1943-10 被 Nasjonal Samling 逮捕移交**占领当局**，辗转多个拘留营，1944-11 获释——勿写"集中营"或具体营名（页面无载） |
| 获奖研究 | 诺奖基于**环状碳分子三维性**的证明——勿泛化为"发现环己烷" |
| 无配偶子女 | page.md 无婚姻/子女记载——身份页留白，不得杜撰 |
| 引语红线 | page.md 正文无哈塞尔直接引语——全篇不得杜撰"哈塞尔说过"，改间接转述 |
| 诺奖演讲日期 | 1970-06-09（page.md 外链明载）——勿写 1969 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q157212 | ✅ |
| name_zh | 奥德·哈塞尔 | ✅ |
| name_en | Odd Hassel | ✅ |
| birth_date | 1897-05-17 | ✅ |
| death_date | 1981-05-11 | ✅ |
| nationality | Norway | ✅ |
| primary_occupation | physical chemist | ✅ |
| field_of_work | physical chemistry（person_field 细分：physical chemistry / molecular structure / X-ray crystallography / electron diffraction，带 rank） | ✅ |
| has_biography | 0（Beamer 立传完成后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Heinrich Jacob Goldschmidt | 师→生（论文导师） | 柏林时期，Victor Goldschmidt 之父 |
| advisor-student | Victor Goldschmidt | 师→生（求学初期导师） | 奥斯陆入学初期的 tutor（非博士导师，note 已限定） |
| colleague | Kasimir Fajans | 无向 | 慕尼黑在其实验室工作，导向吸附指示剂发现 |
| other | Fritz Haber | 无向 | 帮助获得洛克菲勒奖学金（柏林时期） |
| co-honored | Derek Barton | 无向 | 1969 诺贝尔化学奖共同得主 |

> metadata.json-only 的关系一律不入库；page.md 无配偶/子女/门生记载。

## 8. 奖项清单

- Nobel Prize in Chemistry（1969，与 Derek Barton 共享）
- Guldberg-Waage Medal（挪威化学学会，1964）
- Gunnerus Medal（皇家挪威科学与文学院，1964）
- Fridtjof Nansen Award of Excellence（数学自然科学类；frontmatter 明载）
- Centenary Prize（frontmatter 明载）
- Knight of the Order of St. Olav（1960）
- 荣誉博士：University of Copenhagen（1950）、Stockholm University（1960）
- 荣誉会士：挪威化学会、伦敦化学会（Chemical Society of London）、挪威科学与文学院、丹麦皇家科学与文学院、瑞典皇家科学院

## 9. 机构清单

- 教育：University of Oslo（1915–1920）、慕尼黑 Fajans 实验室、柏林 Kaiser Wilhelm Institute、Humboldt University of Berlin（PhD 1924）
- 任职：University of Oslo（1925–1964，1934 年升教授）
- 命名机构：奥斯陆大学年度 Hassel 讲座

## 10. 终审清单

- [x] 生卒 1897-05-17 / 1981-05-11，享年 83，出生地 Kristiania、去世地奥斯陆
- [x] 1969 与 Barton 共享；获奖研究为环状碳分子三维性
- [x] 双 Goldschmidt 角色区分（tutor vs 论文导师）；博士由柏林洪堡授予
- [x] 二战囚禁 1943-10 至 1944-11，表述不夸大
- [x] 无配偶/子女记载、正文无直接引语、全篇不杜撰
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Odd_Hassel/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：从 images.txt / Commons 下载；404 用装饰圆占位并记录
- [ ] **国籍**：封面顶部明示挪威
- [ ] **引语核对**：全篇不得出现无法在 page.md 溯源的"原话"
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
