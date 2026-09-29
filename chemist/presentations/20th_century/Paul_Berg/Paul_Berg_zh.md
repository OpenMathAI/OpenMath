# Paul Berg（保罗·伯格）立传提示词

> qid=Q102379 · 1926-06-30 – 2023-02-15 · 美国生物化学家 · 20 世纪 · 诺贝尔化学奖（1980，独得一半；另一半由 Walter Gilbert 与 Frederick Sanger 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Paul_Berg/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传模板**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 内若缺，先按常规流程下载 Wikipedia 肖像，404 则装饰圆占位；page.md 内嵌 1980 年 Berg 照片与 1983 年 Queen Beatrix 合影可用作候选）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace 重组 DNA 之父\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育（Penn State BS / Case Western Reserve PhD）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「基因剪接 / 链条」母题——圆点连缀暗示 DNA 片段的拼接。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如重组 DNA 概念示意：物种 A DNA + 物种 B DNA → 杂合分子。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Paul Berg（中文惯称：保罗·伯格）
- **生卒**：1926-06-30 生于纽约布鲁克林 → 2023-02-15 逝于加州斯坦福，享年 96
- **国籍**：United States（美国）
- **身份**：生物化学家（biochemist；斯坦福大学教授；1980 诺贝尔化学奖得主）
- **家庭**：俄国犹太移民夫妇之子——母 Sarah Brodsky（家庭主妇）、父 Harry Berg（服装制造商）；1947 年娶 Mildred Levy，育有一子
- **教育轨迹**：
  - Abraham Lincoln High School（布鲁克林，1943 毕业）
  - Pennsylvania State University（生物化学 B.S.，1948；犹太兄弟会 ΒΣΡ 成员）
  - Case Western Reserve University（生物化学 PhD，1952）
- **博士论文**：用放射性同位素示踪研究中间代谢——甲酸、甲醛与甲醇转化为甲硫氨酸中完全还原态的甲基；并是最早证明叶酸与 B12 辅因子参与其中的人之一
- **研究领域**：生物化学——核酸生物化学、重组 DNA、基因剪接、分子遗传学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **布鲁克林裁缝之子（1926）**：俄国犹太移民家庭，父亲是服装制造商——大萧条年代的科学梦。
2. **同位素示踪（1952）**：博士论文以放射性同位素追踪中间代谢，厘清「食物如何变成细胞材料」——甲酸/甲醛/甲醇 → 甲硫氨酸甲基的还原路径。
3. **博士后漂泊（1952–1954）**：美国癌症学会博士后，先后在哥本哈根细胞生理学研究所与华盛顿大学医学院；1954 任癌症研究学者（微生物学系）。
4. **遇 Kornberg（1954–1959）**：在华盛顿大学与 **Arthur Kornberg** 共事；1955–1959 任华盛顿大学医学院教授。
5. **斯坦福（1959–2000）**：1959 迁斯坦福，任教生物化学 41 年；1985–2000 任 Beckman 分子与遗传医学中心主任；2000 退休后仍活跃于研究。另曾任剑桥 Clare Hall 十年期研究员。
6. **第一次跨越物种（1970s）**：**第一个造出含两个不同物种 DNA 的分子**——把一个物种的 DNA 插入另一个物种的分子；这一基因剪接技术是现代基因工程的基本步骤。
7. **病毒染色体**：开发基因剪接技术后，Berg 用它研究病毒染色体。
8. **科学家的自我刹车（1974）**：Berg 与其他科学家呼吁**自愿暂停**部分重组 DNA 研究，直到风险评估完成——科学史上罕见的主动减速。
9. **Asilomar 会议（1975）**：作为组织者召集重组 DNA Asilomar 会议——评估潜在危害、为生物技术研究立规矩；被视为**预防原则**的早期应用。
10. **1980 诺贝尔化学奖**：独得**一半**，理由 "for his fundamental studies of the biochemistry of nucleic acids, with particular regard to recombinant-DNA"；另一半由 Gilbert 与 Sanger 共享（碱基测序方法）——**两组贡献不同，勿混**。
11. **公共事务（2000 后）**：涉足重组 DNA 与胚胎干细胞议题的生物医学公共政策；为遗传学家 **George Beadle** 立传著书；《Bulletin of the Atomic Scientists》赞助人委员会成员。
12. **荣誉等身（1982–2006）**：AAAS 科学自由与责任奖（1982）、国家科学奖章（1983，里根颁授）、美国哲学会（1983）、金盘奖（1989）、英国皇家学会外籍院士（1992）、Max Delbrück Medal（1999）、生物技术遗产奖（2005）、Carl Sagan 科普奖（2006）。
13. **谢幕（2023）**：2023-02-15 在斯坦福去世，享年 96——1966 年（36 岁）即当选 NAS 院士与 AAAS Fellow 的早慧一生落幕。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（藏蓝 navyblue） | `#2A3468` | 分子遗传学的严谨与斯坦福的深蓝（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（重组 DNA badgeRDNA） | `#1B7A43` | 绿跨物种基因剪接 |
| 分类色 2（代谢示踪 badgeTrace） | `#2E5A9E` | 蓝同位素示踪 / 中间代谢 |
| 分类色 3（Asilomar badgeAsilo） | `#D97B29` | 琥珀自愿暂停 / 生物技术规范 |
| 分类色 4（公共政策 badgePolicy） | `#C0395B` | 玫瑰科学与社会 / 干细胞议题 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「基因剪接」片段连缀的几何。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Awaken** — Alex-Productions（文件 `music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav`，不复制 wav）
- **风格**：觉醒 / 开创 / 未来感
- **匹配理由**：
  - "觉醒" 匹配重组 DNA 的时代意义——第一次让两个物种的 DNA 在一支试管里相遇，基因工程的大幕由此拉开
  - "开创" 匹配其双重身份——实验室里的第一个剪接者 + 会议桌前的第一个刹车者（Asilomar）
  - "未来感" 匹配其晚年转向——从试管到公共政策，把科学家的责任带进 21 世纪
- **时长**：以实际曲目时长为准，超过 15 页 × 7 秒由 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 重组 DNA 之父 / Paul Berg 1926–2023 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍/教育/博士/出生地/去世地/领域/荣誉）
03  伯格的一生 — 时间线（10 节点：1926→1943→1948→1952→1954→1955→1959→1974/75→1980→2023）
04  早年：布鲁克林与宾州 (1926–1948) — 表格「时间|事件|结果」
05  博士论文：同位素示踪 (1948–1952) — 表格「问题|方法|结果」+ 公式框：甲酸/甲醛/甲醇 → 甲硫氨酸甲基
06  从哥本哈根到斯坦福 (1952–1959) — 表格「阶段|机构|结果」（Kornberg 合作）
07  重组 DNA：第一次跨越物种 — 表格「问题|方法|结果」+ 公式框：物种 A DNA + 物种 B DNA → 杂合分子
08  科学家的刹车 (1974–1975) — 表格「事件|内容|意义」+ 公式框：自愿暂停 → Asilomar 规范
09  1980 诺贝尔化学奖 — 表格「人物|半份|贡献」+ 公式框：Berg=重组 DNA；Gilbert/Sanger=碱基测序
10  公共事务与传承 — 表格「领域|行动|结果」（干细胞政策/Beadle 立传/原子科学家公报）
11  荣誉清单 — 「类别|代表|意义」表格（含 itemize 荣誉清单）
12  Beckman 中心 — 流程图页（1985 创任 → 2000 退休 → 斯坦福 41 年）
13  遗产：基因工程的基石 — 四分类遗产盒 + 公式框：剪接一个基因，唤醒一个时代
14  结尾 — 「他剪接的不只是 DNA，还有科学与社会的边界。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1980 诺奖分配 | Berg **独得一半**（重组 DNA / 核酸生物化学）；Gilbert 与 Sanger **共享另一半**（碱基测序方法）——两组理由不同勿混：Berg 的理由是 "for his fundamental studies of the biochemistry of nucleic acids, with particular regard to recombinant-DNA"，Gilbert/Sanger 是 "for their contributions concerning the determination of base sequences in nucleic acids" |
| 与 Sanger 的关系 | Sanger 是 1980 共享对手方（其 1958 奖独享）——勿写 Berg 与 Sanger "共同发明测序" |
| "第一个"表述 | page.md 明载 "the first scientist to create a molecule containing DNA from two different species"——可写"第一个造出含两个不同物种 DNA 的分子"；勿扩写成"第一个做基因工程的人" |
| 暂停令性质 | 1974 是**自愿暂停**（voluntary moratorium）——勿写"政府禁令"；1975 Asilomar 会议"被视为预防原则的早期应用"是页面原话的转述 |
| 博士年份 | PhD 1952（Case Western Reserve）——勿与 Penn State BS 1948 混 |
| 机构顺序 | 华盛顿大学医学院（1955–1959 教授）→ 斯坦福（1959–2000）——勿颠倒；Kornberg 合作在华盛顿大学 |
| Clare Hall | 剑桥 Clare Hall 是"tenured as a research fellow"——勿写成读博或访学 |
| 家庭 | 妻 Mildred Levy（1947 结婚）、一子——1983 年 Queen Beatrix 合影中"第二对夫妇"可作图注素材 |
| 犹太裔口径 | 俄国犹太移民之子——背景叙述可用，勿衍生政治内容 |
| 宗教/争议 | 《Bulletin of the Atomic Scientists》赞助人身份照实写；无其他敏感内容 |
| frontmatter 噪声 | occupation 含 biologist/researcher 等多条——主职业以 biochemist 为准 |
| 荣誉年份 | Lasker 与 Gairdner 在 frontmatter 有列但 page.md 正文未给年份——照实写"年份未载"或留白，勿编造 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q102379 | ✅（UPD 回填 stub #1128） |
| name_zh | 保罗·伯格 | ✅ |
| name_en | Paul Berg | ✅（与库内 #1128 精确一致） |
| birth_date | 1926-06-30 | ✅ |
| death_date | 2023-02-15 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：recombinant DNA / molecular biology / nucleic acids，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Arthur Kornberg | 无向 | 华盛顿大学圣路易斯医学院共事 |
| co-honored | Walter Gilbert | 无向 | 1980 诺贝尔化学奖，Gilbert 与 Sanger 共享另一半 |
| co-honored | Frederick Sanger | 无向 | 1980 诺贝尔化学奖，Gilbert 与 Sanger 共享另一半 |

**家庭**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Mildred Levy | 无向 | 1947 结婚，育有一子 |

> **禁入库名单**：George Beadle（仅著书立传对象）；Queen Beatrix（仅合影图注）；父母 Harry Berg / Sarah Brodsky（背景叙述）；Harry Hopkins 无涉（那是 Gilbert 篇）。metadata.json 无其他 page.md 未载关系。

## 8. 奖项清单

- Nobel Prize in Chemistry（1980，独得一半；另一半 Gilbert + Sanger）
- Albert Lasker Award for Basic Medical Research（年份未载）
- Canada Gairdner International Award（年份未载）
- NAS 院士 + American Academy of Arts and Sciences Fellow（1966）
- AAAS Award for Scientific Freedom and Responsibility（1982）
- National Medal of Science（1983，里根颁授）
- American Philosophical Society（1983）
- National Library of Medicine Medal（1986）
- Golden Plate Award of the American Academy of Achievement（1989）
- Foreign Member of the Royal Society, ForMemRS（1992）
- Max Delbrück Medal（1999）
- Biotechnology Heritage Award（2005）
- Carl Sagan Prize for Science Popularization（2006，Wonderfest）
- American Institute of Chemists Gold Medal（年份未载）

## 9. 机构清单

- 教育：Abraham Lincoln High School（1943）→ Pennsylvania State University（BS 1948）→ Case Western Reserve University（PhD 1952）
- 任职：哥本哈根细胞生理学研究所 + 华盛顿大学医学院（1952–1954 美国癌症学会博士后）→ 华盛顿大学医学院微生物学系（1954）→ 华盛顿大学医学院教授（1955–1959）→ Stanford University（1959–2000；Beckman 分子与遗传医学中心主任 1985–2000）；剑桥 Clare Hall 十年期研究员
- 会议：Asilomar 重组 DNA 会议（1975，组织者）

## 10. 终审清单

- [ ] 生卒 1926-06-30 / 2023-02-15，享年 96，出生地布鲁克林、去世地斯坦福
- [ ] 1980 诺奖"独得一半 / 另一半 Gilbert+Sanger"表述准确；两条官方理由不混淆
- [ ] "第一个造出含两个不同物种 DNA 的分子"表述与 page.md 原文一致
- [ ] 1974 自愿暂停 / 1975 Asilomar 因果链照原文
- [ ] 华盛顿大学 → 斯坦福年份准确；Kornberg 合作语境准确
- [ ] 引语全部可在本地 Wikipedia 原文溯源（获奖理由英文原文）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Paul_Berg/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：下载 Wikipedia 肖像（250px→500px；404 用 REST API 查 infobox 原图名；仍失败装饰圆占位）
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（1980 官方获奖理由为唯一硬引语）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox≤10pt、hbox≤50pt）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本文件不改动总名单。
> **最重要的事：每写一页就 make，看到溢出就修。**
