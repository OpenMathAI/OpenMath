# Brook Taylor（布鲁克·泰勒）立传提示词

> qid=Q212085 · 1685-08-18 – 1731-12-29 · 英国数学家、律师 · 18 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/18th_century/pages/Brook_Taylor/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 英格兰`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「泰勒级数 / 函数逼近」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Brook Taylor（中文惯称：泰勒，尊称"有限差分法之父 / 泰勒级数的提出者"）
- **生卒**：1685-08-18 生于 Edmonton（米德尔塞克斯，英格兰）→ 1731-12-29 逝于伦敦（Somerset House），享年 46
- **国籍**：英格兰（English，出生时属 Kingdom of England）
- **身份**：数学家、律师（barrister）
- **家庭**：父 John Taylor（肯特郡 Patrixbourne 议员），母 Olivia Tempest（Edmonton 的 John Tempest 之女）；1721 年娶 Miss Brydges（1723 年难产去世，子亦夭折）；1725 年娶 Sabetta Sawbridge（1730 年难产去世，女儿 Elizabeth 幸存）
- **教育轨迹**：
  - 1701 年入剑桥大学圣约翰学院（St John's College，fellow-commoner）
  - 1709 年获法学士（LL.B.）
  - 1714 年获法学博士（LL.D.）
- **导师**：John Machin（约翰·梅钦）、John Keill（约翰·凯尔）
- **研究领域**：数学分析、有限差分、透视学、振动弦

## 2. 核心叙事亮点（用于 Slide 4-14）

1. **泰勒定理（1715）**：给出函数在一点的局部多项式逼近，其重要性直到 1772 年才被拉格朗日充分认识，称其为"微分学的主要基础（the main foundation of differential calculus）"。
2. **泰勒级数**：将函数展开为幂级数，是分析学与无穷小方法的基石，后世麦克劳林级数是其在 $x=0$ 处的特殊情形。
3. **有限差分法**：《Methodus Incrementorum Directa et Inversa》（1715，"正反增量法"）为高等数学新增"有限差分"（calculus of finite differences）这一分支。
4. **振动弦**：用有限差分法确定振动弦的运动形式。
5. **天文折射**：首次给出天文折射（astronomical refraction）令人满意的研究。
6. **分部积分法**：系统化分部积分（integration by parts）技巧。
7. **透视学**：《Linear Perspective》（1715）更清晰地阐述透视原理，后经 Joshua Kirby（1754）、Daniel Fournier（1761）补充。
8. **皇家学会**：1712 年当选院士（FRS）；同年参与牛顿 vs 莱布尼茨优先权之争的裁定委员会；1714–1718 年任学会秘书。
9. **哲学与宗教转向**：1715 年起转向哲学宗教，与 Comte de Montmort 通信讨论马勒布朗士学说；遗稿《On the Jewish Sacrifices》《On the Lawfulness of Eating Blood》。
10. **悲剧人生**：两任妻子均难产去世；健康自 1717 年起恶化；1729 年父亡、继承 Bifrons 庄园；1731 年 46 岁早逝。
11. **后世纪念**：月球环形山 Taylor（Taylor crater）于 1935 年以其名命名。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（英格兰红） | `#9E1B32` | 英格兰 / 剑桥 |
| 强调色（数学金） | `#C9A227` | 18 世纪数学的尊崇 |
| 分类色 1（分析 — 靛蓝） | `#4C5FD5` | 泰勒定理 / 泰勒级数 |
| 分类色 2（有限差分 — 青绿） | `#0E7C7B` | 有限差分 / 增量法 |
| 分类色 3（透视/几何 — 琥珀） | `#E07B30` | 线性透视 |
| 分类色 4（振动弦/物理 — 玫红） | `#B76E79` | 振动弦 / 天文折射 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「泰勒级数 / 函数逼近」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**古典典雅 / 启蒙理性的肃穆**（"泰勒级数之父"的奠基地位与悲剧早逝的沉郁）
- **匹配理由**：
  - 泰勒是 18 世纪英国数学的代表，贡献横跨分析、有限差分、透视学——需**典雅、理性、略含沉郁**的配乐
  - "典雅" 匹配其剑桥出身与启蒙时代气质
  - "沉郁" 匹配其 46 岁早逝、两度丧妻的人生悲剧
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/典雅/理性风格）：
  - 首选：古典 / 典雅 / 理性风格曲目（本系列高斯/黎曼/欧拉/拉格朗日等已用 Timeless，可沿用保持一致）
  - 备选：巴洛克 / 启蒙时代风格曲目（呼应 18 世纪英国）
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐欧拉模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「泰勒级数之父 · 有限差分法的奠基者」+ 泰勒 1685–1731 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **泰勒的一生：时间线**（`\timelineslide`）：1685 Edmonton 出生 → 1701 入圣约翰学院 → 1712 当选皇家学会院士 → 1715 《Methodus Incrementorum》→ 1714–1718 学会秘书 → 1729 继承 Bifrons → 1731 去世
4. **早年与教育**（`\earlyslide`）：Edmonton、剑桥圣约翰学院、Machin 与 Keill 引路、中心振荡问题
5. **泰勒定理**（核心贡献页，表格 + 公式框）：$f(x)=f(a)+f'(a)(x-a)+\cdots$
6. **泰勒级数**（核心贡献页，表格 + 公式框）：幂级数展开、麦克劳林级数
7. **有限差分法**（核心贡献页，表格 + 公式框）：增量法、差分 $\Delta$
8. **振动弦与天文折射**（核心贡献页，表格 + 公式框）：振动弦运动形式、折射
9. **分部积分法**（核心贡献页，表格 + 公式框）：分部积分公式
10. **透视学**（特色页，表格）：《Linear Perspective》、透视原理
11. **皇家学会与微积分之争**（表格）：FRS、牛顿 vs 莱布尼茨裁定、学会秘书
12. **悲剧人生与传承**（表格）：两度丧妻、早逝、Contemplatio Philosophica
13. **荣誉与后世纪念**（表格）：皇家学会会员、月球环形山 Taylor
14. **终章**：46 岁、"泰勒级数之父"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **国籍**：metadata 国籍为 Kingdom of England（英格兰王国）；泰勒生于英格兰、卒于伦敦——封面用「英格兰」，勿写"大不列颠 / 联合王国"（其生前 1707 年英格兰与苏格兰方才合并为大不列颠王国，出生时仍属英格兰王国）。
- **泰勒定理**：1715 年《Methodus Incrementorum》中提出，但重要性直到 1772 年才被拉格朗日认识并称其为"微分学的主要基础"——勿写"泰勒提出即被广泛认可"。
- **泰勒级数 vs 麦克劳林级数**：麦克劳林级数是泰勒级数在 $x=0$ 处的特殊情形，命名在麦克劳林（1698–1746）之后——勿把麦克劳林级数写成泰勒的贡献，也勿混淆两者。
- **分部积分法**：infobox 列为 known for，但分部积分在莱布尼茨时代已有人使用，泰勒作出系统化表述——表述为"系统化"而非"发明"。
- **导师关系**：John Machin 与 John Keill 是 academic advisors（学术指导者），非现代博士导师制——勿写"泰勒在二人门下攻读博士学位"（泰勒的学位是法学 LL.B./LL.D.，非数学）。
- **中心振荡问题**：泰勒解得"center of oscillation"问题，但解直到 1714 年 5 月才发表，且被 Johann Bernoulli 质疑优先权——表述准确，勿写"独自首创"。
- **死亡**：1731-12-29 逝于伦敦 Somerset House，享年 46；metadata 另记 1731-11-30（疑为旧历），以 Wikipedia infobox 1731-12-29 为准。
- **律师身份**：泰勒受过法学训练并从事律师职业（barrister），数学是其主要志业——可写"数学家、律师"，勿忽略其法学背景。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q212085 | 待写入 |
| name_zh | 泰勒（或 布鲁克·泰勒） | 待写入 |
| name_en | Brook Taylor | 待写入 |
| birth_date | 1685-08-18 | 待写入 |
| death_date | 1731-12-29 | 待写入 |
| nationality | Kingdom of England | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematical analysis / mathematics | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **导师**：John Machin（约翰·梅钦）、John Keill（约翰·凯尔）
- **优先权争议**：Johann Bernoulli（约翰·伯努利，中心振荡问题优先权）
- **同代英国数学**：Isaac Newton（牛顿，微积分优先权之争裁定委员会同席）、Roger Cotes（科茨，能与伯努利家族抗衡的少数英国数学家之一）
- **后世评价**：Joseph-Louis Lagrange（拉格朗日，1772 年称泰勒定理为"微分学的主要基础"）
- **父亲**：John Taylor（肯特郡 Patrixbourne 议员）

## 8. 奖项清单

- Fellow of the Royal Society（英国皇家学会会员，1712）

## 9. 机构清单

- 教育：St John's College, Cambridge（剑桥大学圣约翰学院，1701 入、1709 LL.B.、1714 LL.D.）
- 任职：Royal Society（皇家学会，1712 院士，1714–1718 秘书）；St John's College, Cambridge

## 10. 终审清单

- [ ] 生卒 1685-08-18 / 1731-12-29，享年 46，出生地 Edmonton
- [ ] 国籍用「英格兰」，并注明其生前正值英格兰—苏格兰合并
- [ ] 导师 Machin / Keill"学术指导"表述准确（非博士导师）
- [ ] 泰勒定理"1715 提出、1772 拉格朗日认识"表述准确
- [ ] 泰勒级数 vs 麦克劳林级数区分清楚
- [ ] 分部积分"系统化"表述准确（非发明）
- [ ] 中心振荡"1714 发表、Bernoulli 质疑优先权"表述准确
- [ ] 律师身份与法学学位表述准确
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Brook_Taylor/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 Goupy 所作肖像（`images/taylor_portrait.jpg`，624×800）
- [ ] **国籍**：封面顶部徽章明示英格兰
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如拉格朗日"the main foundation of differential calculus"）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（欧拉 / 拉格朗日 / 拉普拉斯）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
