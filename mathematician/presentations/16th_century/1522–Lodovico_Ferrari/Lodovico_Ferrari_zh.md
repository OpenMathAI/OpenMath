# Lodovico Ferrari（洛多维科·费拉里）立传提示词

> qid=Q310783 · 1522-02-02 – 1565-10-05 · 意大利数学家 · 16 世纪（三次/四次方程创立时代）
> 本地 Wikipedia 数据源：`mathematician/presentations/16th_century/pages/Lodovico_Ferrari/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（page.md 无 Ferrari 本人肖像——`images.txt` 首图是 Tartaglia 论战檄文《Terza risposta》1547 年小册子封面，**非肖像**；无真肖像则用装饰圆 `\faIcon{user}` 占位，勿误用檄文封面充当头像）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 意大利`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像（装饰圆占位）+ 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应文艺复兴代数「方程之根」的母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Lodovico de Ferrari（中文惯称：洛多维科·费拉里）
- **生卒**：1522-02-02 生于博洛尼亚（Bologna）→ 1565-10-05 逝于博洛尼亚，享年 43
- **国籍**：意大利（page.md 正文作 Italian；metadata **无** nationality 字段——封面与正文一律写「意大利」，**不得据他页（如 Bombelli 页）推定 1522 年博洛尼亚的政权归属**）
- **身份**：数学家（page.md infobox Fields 仅 Mathematics；metadata occupation 仅 mathematician）
- **家庭**：祖父 Bartolomeo Ferrari 被迫离开米兰迁往博洛尼亚；有寡姐 Maddalena（费拉里退休后与其同住博洛尼亚）
- **教育轨迹**：无大学教育记载；少年时是 Gerolamo Cardano 的仆人（servant），因天资聪颖被 Cardano 亲自教授数学
- **导师**：Gerolamo Cardano（主人兼导师；费拉里协助其三四次方程求解）
- **研究领域**：代数（algebra）、数学（mathematics）

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **四次方程一般解法的破解者**：今日最广为人知的成就——求解 quartic（biquadratic）方程；是「主要由费拉里完成、由卡尔达诺发表」的解法。
2. **出身仆役的数学天才**：以 Cardano 仆人身份入门，因「extremely bright」被 Cardano 亲自教数学——文艺复兴仆役逆袭的传奇叙事。
3. **协助 Cardano 攻克三次与四次方程**：Ferrari aided Cardano on his solutions for quartic equations and cubic equations——师徒协作攻克方程论的两大高峰。
4. **少年成名**：还在十几岁（still in his teens）时，因 Cardano 辞去并推荐，获得罗马一个声望卓著的教职。
5. **Cardano–Tartaglia 公式**：1545 年因三次方程解法归属，费拉里与塔尔塔利亚之间爆发著名论战；今数学史界将三次方程解法归名于两人并称「Cardano–Tartaglia 公式」。
6. **为「塔尔塔利亚终生报复说」辟谣**：page.md 明载「Tartaglia devoted the rest of his life to ruining Cardano」的流传故事**系杜撰**（appear to be fabricated）——费拉里篇可承担这一史学澄清。
7. **42 岁功成身退**：年轻而富有地退休（retired, when young at 42 years old, and wealthy）——代数学家中的异数。
8. **博洛尼亚大学教授**：1565 年返回故乡博洛尼亚，出任博洛尼亚大学数学教授，不久去世。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（博洛尼亚深红） | `#6B1F2A` | 文艺复兴砖城博洛尼亚 / 师门传承 |
| 强调色（代数金） | `#C9A227` | 16 世纪方程论解法的尊崇 |
| 分类色 1（四次方程 — 靛蓝） | `#4C5FD5` | quartic / biquadratic 解法 |
| 分类色 2（三次方程 — 青绿） | `#0E7C7B` | 与 Cardano 协作的三次方程 |
| 分类色 3（论战 — 琥珀） | `#E07B30` | 1545 年与 Tartaglia 的论战 |
| 分类色 4（师门 — 玫红） | `#B76E79` | Cardano 之徒 / 仆役逆袭 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「根式塔（radicandi）」层层开方的结构之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **选定曲目**：**Savage**（alex-productions，本地文件 `music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav`）
- **风格定调**：**强推进 / 紧张 / 竞争感**（方程攻克与公开论战交织的一生）
- **匹配理由**：
  - 「难题攻克」标签匹配四次方程一般解法这一 16 世纪代数最硬核的突破；
  - 「竞争、紧张」匹配 1545 年起与 Tartaglia 的著名论战叙事；
  - 「强推进」匹配仆役出身、十几岁成名、42 岁退休的高密度人生节奏。
  - 时长需 ≥ 13 页 × 7 秒 ≈ 91 秒，ffmpeg `-shortest` 自动对齐。

## 4. Slide 规划（统一 14 页制：共享封面 + 人物封面 + 身份信息 + 时间线 + 早年与教育 + 7 贡献页 + 荣誉与传承 + 终章）

> 正文采用 Wilson 式结构 + 表格 + 公式框：核心贡献页用 `tabularx`（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页用 `p{2.2cm}|X|p{3.0cm}` 表格。帧序与 `TEMPLATE_GUIDE.md` §2 完全同构（帧 1 = 共享封面 `\openmathslide`）。

1. **共享封面**（`\openmathslide`）：`\input{../../cover/openmath_page.tex}`，不改
2. **人物封面**（`\titleslide`）：大标题「四次方程的破解者」+ 洛多维科·费拉里 1522–1565 + 右上装饰圆占位（图注「无存世肖像」）+ 国籍行（意大利）+ 底部三要素状态栏（意大利 | 博洛尼亚大学 | 四次方程一般解法 / Cardano 之门 / 1545 论战）+ 四分类 badge
3. **身份信息页**（`\profileslide`，★ 必做）：左装饰圆 + 右信息网格（生卒 / 本名 Lodovico de Ferrari / 国籍 / 出生地 / 师承 Cardano / 教育（无大学记载，Cardano 亲授）/ 荣誉（无载）/ 核心领域）
4. **费拉里的一生：时间线**（`\timelineslide`）：1522-02-02 博洛尼亚出生 → 少年为 Cardano 仆人、习数学 → 协助攻克三四次方程 → 十几岁获罗马教职 → 1545 与 Tartaglia 论战爆发 → 42 岁功成身退 → 1565 任博洛尼亚大学教授 → 1565-10-05 去世（仅写 page.md 有据的节点：1522 / 1545 / 42 岁 / 1565 / 1565-10-05）
5. **早年与出身**（`\earlyslide`）：祖父 Bartolomeo Ferrari 被逐出米兰、迁居博洛尼亚；少年成为 Cardano 的仆人；因天资极为聪颖（"extremely bright"）被 Cardano 亲自教授数学
6. **四次方程的一般解法**（贡献页，表格 + 公式框）：biquadratic / quartic equation 解法，「主要由费拉里完成（mainly responsible）、由 Cardano 发表」的归属口径
7. **师徒协作：三次与四次方程**（贡献页，表格 + 公式框）：Ferrari aided Cardano on cubic & quartic solutions；四次方程解法由 Cardano 署名发表
8. **Cardano–Tartaglia 公式与 1545 论战**（贡献页，表格 + 公式框）：三次方程解法归名 Cardano 与 Tartaglia 二人；**1545 年**论战爆发（page.md 无 1548 与「胜出」记载，禁写）；「塔尔塔利亚终生报复说系杜撰」的史学澄清
9. **少年成名：罗马教职**（贡献页，表格）：十几岁接替 Cardano 辞任并推荐的罗马声望教职（机构名 page.md 无载，勿具名）
10. **功成身退**（贡献页，表格）：42 岁年轻而富有地退休；回到故乡博洛尼亚与寡姐 Maddalena 同住
11. **博洛尼亚大学教授**（贡献页，表格）：1565 年出任博洛尼亚大学数学教授
12. **英年早逝**（贡献页，表格）：1565-10-05 去世、享年 43；白砷（white arsenic）中毒——**page.md 口径为 "according to a legend, by his sister"，传说性质与下毒者其姐之说均须明确标注**，禁写成既定事实
13. **荣誉与传承**（`\honorslide`）：page.md 无载任何奖项——本页写「历史评价与遗产」：四次方程解法的归属、Cardano–Tartaglia 公式的史学共识、辟谣流传故事；**禁杜撰奖项**
14. **终章**（`\closingslide`）：43 岁、四次方程破解者的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **★ 生年享年裁定**：主控任务单写「46 岁去世（砷中毒说存疑）」**有误**——page.md infobox 明载 1522-02-02 生、1565-10-05 卒（aged 43）。按 page.md 取 **43 岁**口径；metadata.json 日期与 page.md 一致。
- **★ 死因口径**：白砷中毒身亡 + 「下毒者为姐姐」均出自 page.md 原句 "he died of white arsenic poisoning, according to a legend, by his sister"——**必须保留 "according to a legend"（传说）限定语**，禁写成既定事实；可表述为「据传说死于白砷中毒、传说下毒者为其姐」。
- **★ 论战年份**：page.md 仅载 **1545 年论战爆发**（"In 1545 a famous dispute erupted"）——任务单所称「1548 公开论战、费拉里胜出」**page.md 无载，禁写 1548 与「胜出」**。
- **「终生报复说」是杜撰**：page.md 明载该流传故事 "appear to be fabricated"——若引用必须带辟谣框定，禁当事实陈述。
- **四次方程归属口径**：写「主要由费拉里完成（mainly responsible）、由卡尔达诺发表」；勿写「费拉里独立发明」或「卡尔达诺发明四次方程解法」。
- **Cardano–Tartaglia 公式**专指**三次方程**解法、两人共享归名——勿与费拉里的四次方程混写。
- **罗马教职**：无年份（仅 "while still in his teens"）；机构名 page.md 无载（metadata employer 的 Scuole Piatti / Ercole Gonzaga 为 metadata-only，不入机构清单）——教职写「罗马一个声望卓著的教职」即可。
- **退休年龄**：42 岁（page.md "retired, when young at 42 years old, and wealthy"）。
- **国籍**：page.md 正文作 Italian；metadata **无** nationality 字段。封面与正文一律用「意大利」；**不得据他页（如 Bombelli 页）推定 1522 年博洛尼亚的政权归属**——若确需 historical 政权口径，由主控另行裁定。
- **家庭红线**：姐姐 Maddalena 仅载「寡姐、退休后同住」与传说下毒者；祖父 Bartolomeo 仅载迁居事——**无 sibling / grandparent 关系类型**，均不入库。
- **肖像红线**：`images.txt` 首图是 Tartaglia《Terza risposta》（1547）论战檄文封面，画的是论战小册子、**不是费拉里肖像**——禁充当头像；无真肖像用装饰圆占位。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q310783 | 待写入 |
| name_zh | 洛多维科·费拉里 | 待写入 |
| name_en | Lodovico Ferrari（metadata label） | 待写入 |
| birth_date | 1522-02-02 | 待写入 |
| death_date | 1565-10-05 | 待写入 |
| nationality | Italy（page.md 口径；metadata 无该字段，勿补 Papal States） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | algebra / mathematics | 待写入 |
| has_biography | false（本次只入库社会关系，Beamer 立传待做） | 待写入 |

## 7. 社会关系入库清单

- **导师**：Gerolamo Cardano（advisor-student, direction: advisor——主人兼导师，亲自教其数学）
- **协作**：Gerolamo Cardano（collaborator——协助三次/四次方程求解，四次方程解法由 Cardano 发表；双行沿用 Hench–Kendall 先例）
- **论战**：Niccolò Tartaglia（controversy——1545 年三次方程解法归属论战；★ Tartaglia 由 A 组负责，其 yaml 侧请同用 controversy + 规范名 "Niccolò Tartaglia"，INSERT IGNORE 自动去重）
- **不入库**（page.md 无载或无对应类型）：姐姐 Maddalena（寡姐，无 sibling 类型）、祖父 Bartolomeo Ferrari（无 grandparent 类型）、metadata employer Scuole Piatti / Ercole Gonzaga（metadata-only）

## 8. 奖项清单

- 无（page.md 无任何奖项记载；images.txt 檄文封面图仅供叙事插图，非荣誉）

## 9. 机构清单

- 任职：University of Bologna（博洛尼亚大学，1565 年数学教授；metadata employer 明载，page.md 正文 "a professorship of mathematics at the University of Bologna in 1565"）
- 不入库：罗马教职（机构名无载）、Scuole Piatti / Ercole Gonzaga（metadata-only）

## 10. 终审清单

- [ ] 生卒 1522-02-02 / 1565-10-05，享年 **43**（非 46），出生地与卒地均 Bologna
- [ ] 死因带 "according to a legend" 传说限定语，禁写成事实
- [ ] 论战仅写 1545 年爆发，禁写 1548 / 「胜出」
- [ ] 「塔尔塔利亚终生报复说」引用时必须带辟谣框定
- [ ] 四次方程「费拉里主责、Cardano 发表」表述准确
- [ ] Cardano–Tartaglia 公式专指三次方程、两人共享
- [ ] 退休 42 岁且富有；1565 博洛尼亚大学教授
- [ ] 檄文封面图不当头像，无真肖像用装饰圆
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像位 + 国籍行 + 气泡背景 + 品牌 OpenMathAI

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Lodovico_Ferrari/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：确认装饰圆占位并写图注「无存世肖像」（PORTRAITS.md 结论：无）；`images.txt` 的《Terza risposta》(1547) 檄文封面只能在正文作插图，不得顶替头像
- [ ] **国籍**：封面顶部徽章明示意大利（page.md 口径；metadata 无 nationality 字段，勿补 Papal States）
- [ ] **引语核对**：page.md 仅零星短语可引——"extremely bright"、"according to a legend, by his sister"、"while still in his teens"、"retired, when young at 42 years old, and wealthy"；其余一律转述，禁编造
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Cardano / Bombelli / Tartaglia 篇）格式对齐，论战叙事口径一致

## 12. Review-1 事实终审记录（2026-09-29）

- 核对基准：`pages/Lodovico_Ferrari/page.md`（+ metadata.json / images.txt）
- 生卒 / 享年：page.md infobox 「2 February 1522 – 5 October 1565 (aged 43)」，出生地与卒地均 Bologna——与提示词一致（正文与 metadata 亦一致）；享年 43，**非 46**
- 国籍口径：page.md 正文作 Italian；metadata **无** nationality 字段。原 §1/§5/§6 据 Bombelli 页推定 1522 年博洛尼亚属教宗国的链条已删除——立传统一写「意大利」，不超出本人 page.md
- 肖像结论：**无存世肖像**（PORTRAITS.md 依据：唯一图为 Tartaglia《Terza risposta data a messer Hieronimo Cardano et a messer Lodovico Ferraro》(1547) 论战檄文封面，非肖像）——用装饰圆 `\faIcon{user}` 占位，图注「无存世肖像」，禁止檄文封面 / 书影冒充头像（提示词原口径已正确，仅补图注与禁项）
- 引语核对：page.md 可引短语四条（"extremely bright"；"according to a legend, by his sister"；"while still in his teens"；"retired, when young at 42 years old, and wealthy"），均逐字可查；§11 原「本篇 page.md 无直接引语，全文转述」表述**不准确**，已改正
- 本轮修正：
  1. §1 / §5 / §6 三处国籍口径改为「意大利 + metadata 无字段」，删除据 Bombelli 页的教宗国推定链（违反「不得超出本人 page.md」）
  2. §4 按统一 14 页制重写（原 13 页扩为 14 帧：共享封面 + 人物封面 + 身份 + 时间线 + 早年 + 7 贡献页 + 荣誉与传承 + 终章）；原「历史评价与遗产」页定为帧 13 `\honorslide`；帧 8 明确「1545 论战爆发、禁写 1548 与胜出」，帧 12 明确白砷传说性质
  3. §11 第 1 轮头像 / 引语两条按 PORTRAITS.md 与 page.md 实况改正
- 遗留不确定项：① 论战年份仅 1545（page.md "In 1545 a famous dispute erupted"），任务单所称 1548 与「胜出」无载禁写；② 死因与下毒者均系 legend；③ 罗马教职、metadata employer 的 Scuole Piatti / Ercole Gonzaga 均 page.md 无载或 metadata-only，不入机构清单；④ 姐姐 Maddalena 与祖父 Bartolomeo 无对应关系类型，不入库

## 13. 立传期执行记录（Beamer，2026-09-29，math16-c）

- 产出：`Lodovico_Ferrari_zh.tex` / `.pdf`，**14 页**（与 §4 一致：共享封面 + 人物封面 + 身份信息 + 时间线 + 早年 + 7 贡献页 + 荣誉与传承 + 终章）；`make distclean && make` **0 error**、**Overfull 全部为 0**、体积 140 KB。
- 肖像：按 PORTRAITS.md 与 §5 用装饰圆 `\faIcon{user}` 占位，图注「无存世肖像」；《Terza risposta》(1547) 檄文封面未作插图（避免读者误当肖像）。
- 引语：仅使用 §11 列出的可引短语（"extremely bright"、"while still in his teens"、"wealthy"、"white arsenic"）；「塔尔塔利亚终生报复说」按 §11「其余一律转述」以中文转述呈现，未引整句英文。
- 硬口径落实：享年 43；论战仅写 1545 年爆发（无 1548、无「胜出」）；死因带「据传说」限定语；四次方程表述为「主要由费拉里完成、由 Cardano 发表」；Cardano–Tartaglia 公式专指三次方程、二人共享。
- 与 `page.md` **无事实冲突**，未产生 §12 之外的修正。
