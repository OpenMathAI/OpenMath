# Isaac Newton（艾萨克·牛顿）立传提示词

> qid=Q935 · 1643-01-04（新历；旧历 1642-12-25）– 1727-03-31（新历）· 英国数学家/物理学家 · 17 世纪（核心贡献 1665–1687）
> 本地 Wikipedia 数据源：`mathematician/presentations/17th_century/pages/Isaac_Newton/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。images.txt 有肖像可用：**Godfrey Kneller 1702 年肖像**，下载至 `images/newton_portrait.jpg`。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒（注新旧历）、国籍、出生地、家庭（遗腹子）、教育、核心领域。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），母题呼应「苹果下落的抛物线 / 棱镜色散光谱」之美。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Sir Isaac Newton（FRS，中文：艾萨克·牛顿）
- **生卒**：**1643-01-04**（新历；旧历 1642-12-25 圣诞节，英格兰当时用儒略历）生于 Woolsthorpe Manor（林肯郡）→ **1727-03-31**（新历；旧历 1727-03-20）逝于肯辛顿，享年 84；国葬，安葬 Westminster Abbey 中殿——**第一位葬入该教堂的科学家**。★ infobox 新历在前、旧历括注；metadata 旧历在前——统一用新历为主口径
- **国籍**：Kingdom of England / Kingdom of Great Britain，现代对应英国
- **身份**：数学家、物理学家、天文学家、炼金术士、神学家、作家、发明家（"an English polymath"）
- **家庭**：父（同名 Isaac Newton）在牛顿**出生前三个月**去世；早产儿——母亲说他"能装进一夸脱杯里"；3 岁时母亲 Hannah Ayscough 改嫁 Reverend Barnabas Smith，把他留给外祖母抚养；**终身未婚**（"Although it was claimed that he was once engaged, Newton never married."）；无遗嘱去世，遗产分给亲属
- **教育轨迹**：约 12–17 岁 The King's School, Grantham（1659 年曾被母亲接回务农，校长 Stokes 与舅舅劝说返校）→ **Trinity College, Cambridge**（1661 年 6 月入学，初为 subsizar，1664 获奖学金）：BA 1665、MA 1668、1667 fellow；1669 年（获 MA 仅一年后，26 岁）接任 Lucasian 教授（经 Charles II 特许免于受圣职）
- **导师**：Isaac Barrow（1669 让出卢卡斯教席）、Benjamin Pulleyn

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **广义二项式定理（1664–65）**：推广到任意指数，`(1+x)^n = Σ C(n,k)x^k`——"one of the most powerful and significant in the whole of mathematics"。
2. **微积分（流数法，1665–1666 瘟疫年）**：剑桥停课回伍尔索普的"奇迹年"，"his private studies... have been described as 'the richest and most productive ever experienced by a scientist'"；点记号 `ẋ` 沿用至今。
3. **万有引力与《原理》（1687）**：`F = G·m₁m₂/r²` 推导开普勒定律、解释潮汐/彗星/岁差——"the first great unification in physics"；Halley 鼓励并自费出版。
4. **运动三定律（Principia 1687）**：奠定经典力学，"not improved upon for more than 200 years"。
5. **反射望远镜（1668）**：造出第一台真正可用的反射望远镜（Newtonian telescope），避免色差。
6. **光学与棱镜分光（1666）**：白光可分解与复合、"颜色是光本身内在属性"；光的微粒说，但在《光学》中承认光兼具波动性。
7. **《光学》Opticks（1704）**：微粒说 + Queries（Query 30："Are not gross Bodies and Light convertible into one another...?"）。
8. **牛顿冷却定律（1701）**：`dT/dt = −k(T − T_env)`——第一个热传导公式。
9. **牛顿法**：`x_{n+1} = x_n − f(x_n)/f'(x_n)` 迭代求零点。
10. **其他数学**：牛顿恒等式、Newton polygon、Newton–Cotes 公式、最早明确表述一般 Taylor 级数（1691–92 草稿）、变分法开创者（1685 最小阻力问题）。
11. **皇家铸币厂**：Warden 1696–99、Master 1699–1727；主持 1696 大重铸、追缉造假者（William Chaloner 绞死）；铸币周产量 15,000 → 100,000 英镑。
12. **皇家学会主席（1703–1727）**：第 12 任；FRS 1672；1705 年 Queen Anne 册封爵士（"likely to have been motivated by political considerations"）。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（皇家深蓝） | `#16305C` | 皇家学会主席 / 英国 |
| 强调色（苹果金） | `#C9A227` | 苹果树 / 万有引力 |
| 分类色 1（微积分 — 靛蓝） | `#4C5FD5` | 流数法 / 二项式定理 |
| 分类色 2（力学与引力 — 青绿） | `#0E7C7B` | 《原理》/ 三定律 / 万有引力 |
| 分类色 3（光学 — 琥珀） | `#E07B30` | 棱镜光谱 / 反射望远镜 / 微粒说 |
| 分类色 4（铸币与治理 — 玫红） | `#B76E79` | 皇家铸币厂 / 皇家学会主席 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），母题呼应「苹果下落轨迹 / 棱镜色散光谱」之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**庄严恢弘 / 理性之光**（近代科学之巅的英国国葬级人物）
- **匹配理由**：
  - 牛顿是"第一次伟大统一"的完成者——需**恢弘、庄严**的配乐
  - "理性之光" 匹配《原理》照亮宇宙秩序的意象
  - "庄严" 匹配其国葬与"英国之荣光"的历史地位
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：沿用系列曲目 **Timeless**（本系列已统一采用，保持一致）
  - 备选：巴洛克 / 亨德尔式英国庄重风格曲目
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐梅森/伯努利模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「万有引力 · 《自然哲学的数学原理》」+ 艾萨克·牛顿 1643–1727 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒含新旧历 / 国籍 / 出生地 / 家庭 / 教育 / 核心领域）
3. **牛顿的一生：时间线**（`\timelineslide`）：1643-01-04 新历出生（旧历 1642-12-25）→ 1661 三一学院 → 1665–66 瘟疫年奇迹（微积分/光谱/引力萌芽）→ 1669 卢卡斯教授 → 1672 FRS/反射望远镜 → 1687 《原理》→ 1696 铸币厂 → 1703 皇家学会主席 → 1705 封爵 → 1727 国葬
4. **早年与教育**（`\earlyslide`）：遗腹子、一夸脱杯的早产儿、Grantham 的风车与日晷、三一学院 subsizar
5. **瘟疫年的奇迹：微积分**（核心贡献页，表格 + 公式框）：流数法、`(1+x)^n` 广义二项式、`ẋ` 记号
6. **《自然哲学的数学原理》**（核心贡献页，表格 + 公式框）：`F = G·m₁m₂/r²`、三定律、开普勒定律的推导、"first great unification"
7. **光学与反射望远镜**（核心贡献页，表格 + 公式框）：棱镜分光、1668 反射望远镜、微粒说
8. **《光学》与冷却定律**（核心贡献页，表格 + 公式框）：Opticks 1704、`dT/dt = −k(T − T_env)`、Queries
9. **牛顿法与代数**（核心贡献页，表格 + 公式框）：`x_{n+1} = x_n − f(x_n)/f'(x_n)`、牛顿恒等式、变分法雏形
10. **皇家铸币厂厂长**（表格）：大重铸、追缉 Chaloner、周产量 15,000→100,000 英镑
11. **皇家学会主席与封爵**（表格）：FRS 1672、主席 1703–1727、1705 封爵（政治动机注记）
12. **优先权之争**（表格）：与莱布尼茨各自独立发明微积分、符号体系不同、1711 调查黑幕（牛顿自写结论）、英国 1820 后才改用莱布尼茨记号
13. **身后与国葬**（表格）：Westminster Abbey 第一位科学家、Pope 拟墓志铭、1 英镑纸币、力的单位 newton、Trinity 门外苹果树后代
14. **终章**：84 岁、"站在巨人肩上 / 海滩拾贝的孩子"的历史定位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **新旧历双日期**：infobox "4 January 1643 [O.S. 25 December 1642]"、卒 "31 March 1727 [O.S. 20 March 1727]"——封面用新历 1643–1727 并注明旧历；墓碑铭文用旧历（1726）是旧历新年始于 3 月 25 日的缘故，可作趣味注记。
- **苹果落地故事**：故事出自牛顿本人讲述（经 Catherine Barton → Voltaire 流传）；**"苹果砸中脑袋"是后世讹传**（"though not the apocryphal version that the apple actually hit Newton's head"）；Woolsthorpe 树为真树（DNA 支持，约 1816 年风暴吹倒后从根再生）——可讲但分寸要准。
- **微积分优先权之争（安全口径，照录原文）**："Both are now credited with independently developing calculus, though with very different mathematical notations. However, it is established that Newton came to develop calculus much earlier than Leibniz."；"the notation of Leibniz is recognised as the more convenient notation... and after 1820, by British mathematicians."——**双方各自独立、牛顿更早、莱布尼茨记号最终通行**；1711 皇家学会调查"it was later found that Newton wrote the study's concluding remarks"（牛顿自写结论）。
- **谁先发表**：莱布尼茨 1684 年发表在先；牛顿 1665–66 手稿在先但出版极迟（De analysi 1711、Method of Fluxions 1736）——两条必须同时陈述。
- **"Standing on the shoulders of giants"**：1675 年 2 月致 Hooke 信；Wikipedia 明示真伪存疑（"Some historians argued that this... was an oblique attack on Hooke"；谚语已见于 Herbert 1651）——引用须加注，勿作纯谦辞。
- **晚年神学与炼金术**：约一千万字手稿中约一百万字涉炼金术；私下的反三一立场（Arian）但 "never made a public declaration"；Keynes 定性 "He was the last of the magicians"——引用此定性最稳妥。
- **封爵动机**："likely to have been motivated by political considerations"——注记政治因素。
- **遗言**：page.md **未收录任何临终遗言**——勿杜撰。
- **metadata 噪声**：occupation 含 "astrologer"（星象家）——Wikidata 噪声，弃用。
- **教学趣闻**："his classes were almost always empty"（对墙讲课）——可作趣味点勿拔高。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q935 | 待写入 |
| name_zh | 艾萨克·牛顿 | 待写入 |
| name_en | Isaac Newton | 待写入 |
| birth_date | 1643-01-04（旧历 1642-12-25） | 待写入 |
| death_date | 1727-03-31（旧历 1727-03-20） | 待写入 |
| nationality | United Kingdom（Kingdom of England / Great Britain） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / physics / astronomy / optics / alchemy / theology | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **导师**：Isaac Barrow（1669 卢卡斯教席交接）、Benjamin Pulleyn
- **学生**：Roger Cotes、William Whiston（卢卡斯教席继任者）
- **合作/资助**：Edmond Halley（《原理》的鼓励者与出资人）、John Conduitt（晚年助手与遗产执行）、Nicolas Fatio de Duillier（密友，1693 决裂）
- **通信 / 学术**：Robert Hooke（1679–80 通信促其证明椭圆轨道）、Henry Oldenburg、John Locke、Samuel Pepys（Newton–Pepys 问题）、John Flamsteed（交恶，提前出版其星表）
- **论战 / 竞争**：Gottfried Wilhelm Leibniz（微积分优先权之争，英国皇家学会 1711 裁决、牛顿自写结论）、Robert Hooke（光学之争）、追随者 Samuel Clarke（Leibniz–Clarke 通信为其辩护）
- **家庭**：父（遗腹）、母 Hannah Ayscough（改嫁）；终身未婚

## 8. 奖项清单

- FRS（1672）；皇家学会主席（1703–1727，第 12 任）；Knight Bachelor（1705，Queen Anne）；法国科学院外籍联系院士；死后：国葬、Westminster Abbey 中殿（第一位科学家）、力的 SI 单位 newton、1 英镑纸币头像（1978–88）

## 9. 机构清单

- 教育：The King's School, Grantham；Trinity College, Cambridge（BA 1665 / MA 1668 / fellow 1667）
- 任职：Lucasian Professor of Mathematics, Cambridge（1669–1702）；皇家铸币厂 Warden（1696–99）/ Master（1699–1727）；皇家学会主席（1703–1727）；两度剑桥选区议员（1689–90、1701–02）

## 10. 终审清单

- [ ] 生卒 1643-01-04（O.S. 1642-12-25）/ 1727-03-31（O.S. 1727-03-20），享年 84，出生地 Woolsthorpe、逝世地 Kensington
- [ ] 国籍用「英国」；新旧历口径统一（新历为主）
- [ ] 苹果故事"出自本人讲述、砸头是讹传"表述准确
- [ ] 微积分优先权"各自独立、牛顿更早、莱布尼茨 1684 先发表"双陈述
- [ ] "standing on the shoulders of giants"加注出处争议
- [ ] 神学/炼金术用 Keynes "last of the magicians" 口径
- [ ] 封爵"政治动机"注记在位
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Isaac_Newton/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 Kneller 1702 肖像（images.txt 已有链接）
- [ ] **国籍**：封面顶部徽章明示英国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如海滩拾贝句、Pope 拟墓志铭）——忠实转述，勿造伪引语
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（莱布尼茨 / 巴罗 / 惠更斯）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
