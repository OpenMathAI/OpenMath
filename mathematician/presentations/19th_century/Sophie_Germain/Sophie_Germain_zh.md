# Sophie Germain（玛丽-索菲·热尔曼）立传提示词

> qid=Q7103 · 1776-04-01 – 1831-06-27 · 法国数学家、物理学家、哲学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Sophie_Germain/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「曲面 / 弹性」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Marie-Sophie Germain（中文惯称：热尔曼，或索菲·热尔曼）
- **生卒**：1776-04-01 生于巴黎 → 1831-06-27 逝于巴黎（rue de Savoie），享年 55（乳腺癌）
- **国籍**：France（法国）
- **身份**：数学家、物理学家、哲学家（数论、弹性理论、费马大定理部分结果）
- **家庭**：资产阶级家庭；父亲 Ambroise-François Germain（富有的丝绸商，一说金匠，1789 年当选三级会议资产阶级代表）；有一姐 Marie-Madeline、一妹 Angélique-Ambroise
- **教育轨迹**：
  - 13 岁因法国大革命（巴士底狱陷落）禁足家中，在父亲书房读到 Montucla《数学史》，受阿基米德之死故事吸引，自学数学
  - 自学拉丁语、希腊语以读牛顿、欧拉著作；读 Bézout、Cousin 著作
  - 1794 年 École Polytechnique 创办，作为女性被禁止入学，但取得讲义并以化名 Antoine-Auguste Le Blanc 提交作业给拉格朗日
- **导师 / 通信对象**：Carl Friedrich Gauss（epistolary correspondent，通信导师）；实际引路人 Joseph-Louis Lagrange
- **研究领域**：数论、弹性理论、力学、哲学

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **化名求学（最动人叙事）**：以男性化名「Monsieur Antoine-Auguste Le Blanc」与 Lagrange、Legendre、Gauss 通信，掩盖女性身份以躲避对女性科学家的嘲讽。Lagrange 见其才华要求见面，她才坦白真实身份，Lagrange 成为其导师与朋友。
2. **与 Gauss 的通信与友谊**：三年研读《算术研究》后以 Le Blanc 化名致信 Gauss；1807 年拿破仑战争期间担心 Gauss 遭阿基米德式厄运，写信请求 Pernety 将军保护 Gauss 安全。身份揭晓后，Gauss 赞叹「……她无疑拥有最高贵的勇气、非凡的才华与卓越的天才」。两人始终未曾谋面。
3. **费马大定理的贡献（Sophie Germain 定理）**：提出 Sophie Germain 定理，证明费马大定理第一情形对所有奇素数 p<100 成立（实际已证明 p<197）；L.E. Dickson 后用其定理证明 p<1700 的第一情形。为后世探索费马大定理奠定基础。
4. **弹性理论（第一位获巴黎科学院奖的女性）**：1816 年以《Recherches sur la théorie des surfaces élastiques》成为**第一位获得巴黎科学院奖的女性**（针对 Chladni 振动板实验的悬赏）。其推导的偏微分方程是 Kirchhoff–Love 板方程的特例。
5. **平均曲率（mean curvature）**：在《Mémoire sur la courbure des surfaces》（1831）中引入平均曲率概念（亦称 Germain curvature）。
6. **Sophie Germain 素数**：若 p 与 2p+1 皆为素数，则 p 为 Sophie Germain 素数。
7. **Sophie Germain 恒等式**：x⁴+4y⁴ = (x²+2xy+2y²)(x²−2xy+2y²)。
8. **哲学著作**：《Pensées diverses》《Considérations générales sur l'état des sciences et des lettres》（后者获孔德高度赞赏，主张科学与人文无本质区别），皆身后出版。
9. **身后荣誉**：高斯临终前六年（1837）为她在哥廷根大学争取荣誉学位（未果）；巴黎有 Sophie Germain 街、Lycée Sophie Germain；法国科学院 2003 年设立 Sophie Germain 奖（每年 8000 欧元）；2026 年计划将她的名字加入埃菲尔铁塔 72 位女性科学家名单（其弹性理论支撑了铁塔建造，但因性别曾被排除在原有 72 人名单外）。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（法国深蓝） | `#1F3A93` | 法兰西理性 |
| 强调色（玫瑰金） | `#B76E79` | 女性先驱 / 打破偏见 |
| 分类色 1（数论 — 靛蓝） | `#4C5FD5` | 费马大定理 / Sophie Germain 素数 |
| 分类色 2（弹性理论 — 青绿） | `#0E7C7B` | 弹性曲面 / 平均曲率 |
| 分类色 3（哲学 — 琥珀） | `#E07B30` | 哲学 / 科学人文统一 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「弹性曲面的曲率 / 振动板」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**抒情坚毅 / 女性力量**（在性别偏见中坚持自学成才的坚毅与优雅）
- **匹配理由**：
  - 热尔曼以化名求学、深夜裹被读书、冲破性别偏见的经历——需**抒情、坚毅而不悲怆**的配乐，呼应其"在偏见中坚持"的勇气
  - "优雅" 匹配其法国资产阶级出身与哲学修养
  - "坚毅" 匹配其一生独立研究、55 岁病逝仍笔耕不辍的精神
- **已选定曲目（✅ 定稿）**：Alex-Productions「Awaken」（鼓舞 / 明亮 / 突破，呼应女性先驱的坚毅与打破偏见）
  - 本地源文件：`music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav`
  - 复制到成品目录并重命名为：`awaken.wav`
  - 时长约 2 分钟，≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「化名求学的数学先驱 · 弹性理论与费马大定理」+ 热尔曼 1776–1831 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：数论 / 弹性理论 / 哲学 / 化名求学 四分类
4. **早年与自学**（1776–1794）：资产阶级家庭、大革命禁足、Montucla 与阿基米德、自学拉丁希腊文
5. **化名 Le Blanc 与 Lagrange**（核心叙事页）：École Polytechnique、化名投稿、身份揭晓
6. **与 Gauss 的通信与友谊**（核心叙事页）：Disquisitiones、Le Blanc 化名、1807 保护 Gauss、Gauss 的赞叹
7. **费马大定理与 Sophie Germain 定理**（核心贡献页）：第一情形、p<197、Dickson 的推广
8. **弹性理论与科学院大奖**（核心贡献页）：Chladni 振动板、1816 获奖、Kirchhoff–Love 方程特例
9. **平均曲率与曲面理论**：Mémoire sur la courbure、Germain curvature
10. **哲学著作与晚年**：Pensées、Considérations、乳腺癌、Crelle's Journal
11. **荣誉与身后**：Gauss 争取荣誉学位、Sophie Germain 奖、埃菲尔塔 72 女性名单、街道与学校
12. **终章**：55 岁、打破性别偏见的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **【最重要】无生前肖像**：Germain **没有任何生前画像或照片**，也没有同时代的容貌描述。现有"素描"是基于 Zacharie Astruc 的半身像（该半身像又基于死亡面具）绘制的。**封面与身份信息页头像必须用装饰圆 `\faIcon{user}` 占位，或使用 Astruc 半身像素描并明确标注"非生前肖像"**——切勿误用他人照片，也勿把死亡面具照片当真人肖像。
- **化名 Le Blanc**：Germain 使用男性化名「Antoine-Auguste Le Blanc」通信，是**主动隐瞒女性身份**以躲避嘲讽——勿写成"冒名顶替真实学生"（该名字确曾是一名前学生，但她只是借用）。
- **导师关系**：Gauss 是**通信导师（epistolary correspondent）**，非正式博士导师；Lagrange 是实际引路人——勿写成 Germain 在 Gauss 门下正式攻读。
- **弹性理论获奖的缺陷**：1816 年获奖，但她的方程依赖了 **Euler 的一个错误方程**，导致边界条件错误，方法未精确预测实验结果——如实写"获奖但存在缺陷"，勿写成完美理论。她的方程是 Kirchhoff–Love 板方程的特例。
- **费马大定理贡献范围**：Germain 证明第一情形对 p<100 成立（实际 p<197），Dickson 后用其定理推到 p<1700——勿写成"证明了费马大定理"。
- **Poisson 争议**：Poisson 1814 年发表弹性理论时**未致谢 Germain 的帮助**（虽曾与她合作且作为评委接触过她的工作）——客观表述为"优先权争议"。
- **死亡**：死于乳腺癌（1829 年确诊，1831-06-27 去世），非其他原因。
- **死亡证明身份**：死亡证明上登记为"rentière-annuitant（财产持有人）"而非"数学家"——体现当时对女性科学家的偏见，可作叙事点。
- **埃菲尔铁塔**：Germain 的弹性理论支撑了铁塔建造，但**未被列入原有 72 位科学家名单**（Mozans 1913 年指出是性别歧视）；2026 年计划将她加入 72 位女性科学家名单——勿写成她已刻名于铁塔。
- **荣誉学位**：Gauss 1837 年（她死后六年）为她争取哥廷根荣誉学位但未果——勿写成她获得了荣誉学位。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q7103 | 待写入 |
| name_zh | 热尔曼（或 索菲·热尔曼） | 待写入 |
| name_en | Sophie Germain | 待写入 |
| birth_date | 1776-04-01 | 待写入 |
| death_date | 1831-06-27 | 待写入 |
| nationality | France | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | number theory / elasticity theory / mechanics | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **通信导师**：Carl Friedrich Gauss（epistolary correspondent）
- **引路人 / 导师**：Joseph-Louis Lagrange
- **通信 / 合作**：Adrien-Marie Legendre（数论与弹性理论通信，其《数论》第二版补充收录 Germain 工作并称"非常巧妙"）
- **优先权争议**：Siméon Denis Poisson（1814 发表弹性理论未致谢）
- **学术帮助**：Joseph Fourier（科学院秘书，为她争取参加科学院会议的入场券）、Augustin-Louis Cauchy（1826 审稿并建议她发表）
- **评奖相关**：Ernst Chladni（振动板实验，激发弹性理论竞赛）
- **哲学欣赏者**：Auguste Comte（高度赞赏其哲学）
- **家族**：父 Ambroise-François Germain、姐 Marie-Madeline、妹 Angélique-Ambroise、外甥 Armand-Jacques Lherbette（整理出版其哲学著作）

## 8. 奖项清单

- Grand prix des sciences mathématiques（法国科学院数学大奖，1816 年弹性理论，**第一位获此奖的女性**）
- 72 scientist women names on the Eiffel Tower（2026 年计划加入埃菲尔塔 72 位女性科学家名单，身后纪念）
- （Sophie Germain Prize 为 2003 年设立的纪念性奖项，非其生前所获）

## 9. 机构清单

- 教育：University of Göttingen（荣誉学位推荐，未获授；educated_at 字段标注，需谨慎——她未正式就读，是 Gauss 推荐荣誉学位）
- 自学为主，无正式任职（因性别被排斥在学术职位之外）

## 10. 终审清单

- [ ] 生卒 1776-04-01 / 1831-06-27，享年 55，出生地巴黎
- [ ] 【无生前肖像】封面/身份信息页头像用装饰圆或 Astruc 半身像素描（标注非生前肖像），勿用死亡面具当真人像
- [ ] 化名 Le Blanc"主动隐瞒女性身份"表述准确
- [ ] Gauss 为"通信导师"、Lagrange 为"引路人"，表述准确
- [ ] 弹性理论"获奖但依赖 Euler 错误方程、边界条件有误"表述准确
- [ ] 费马大定理"第一情形 p<197、Dickson 推至 p<1700"表述准确，勿写成证明费马大定理
- [ ] Poisson 优先权争议客观表述
- [ ] 死于乳腺癌，死亡证明身份为"财产持有人"（可作叙事点）
- [ ] 埃菲尔塔"未被列入原名单、2026 计划加入"表述准确
- [ ] 荣誉学位"Gauss 争取未果"表述准确
- [ ] 国籍用「法国」现代对应
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Sophie_Germain/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：无生前肖像，用装饰圆占位或 Astruc 半身像素描（标注非生前肖像）
- [ ] **国籍**：封面顶部徽章明示法国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如 Gauss 的赞叹、Cauchy/Navier 的评价）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Fourier / Legendre / Abel）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
