# George Andrew Olah（乔治·安德鲁·奥拉）立传提示词

> qid=Q192603 · 1927-05-22 – 2017-03-08 · 匈牙利裔美国化学家 · 20 世纪 · 诺贝尔化学奖（1994，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/George_Andrew_Olah/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景，是本次撰写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从 `pages/George_Andrew_Olah/images.txt` 下载至 `images/`，404 则用装饰圆占位并在 Review-1 注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 驯服碳正离子的人\enspace·\enspace 匈牙利/美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Oláh András György）、国籍（匈牙利→美国）、出生地/去世地、教育、导师、核心领域、机构、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆），呼应「碳正离子」母题——一个被超酸稳定住的明亮圆点，悬浮于深色场中。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 " "。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：George Andrew Olah，本名 Oláh András György（匈牙利姓名序：姓在前；中文惯称：乔治·安德鲁·奥拉）
- **生卒**：1927-05-22 生于匈牙利布达佩斯 → 2017-03-08 逝于加州 Beverly Hills 自宅，享年 89
- **国籍**：Hungary → United States（1971 入籍美国；1956 事件后经英国、加拿大赴美）；匈牙利裔美国人（Hungarian-American）
- **身份**：化学家（chemist）；碳正离子化学开创者；György Marx 所称 "The Martians（火星人科学家）" 之一
- **家庭**：犹太夫妇 Magda（娘家姓 Krasznai）与律师 Gyula Oláh 之子；1949 年娶 Judit Ágnes Lengyel，二子：György（George，1954 生于匈牙利）、Ronald（1959 生于美国）
- **教育轨迹**：
  - 布达佩斯 Piarist Gimnazium（中学）
  - 布达佩斯技术大学（今 Budapest University of Technology and Economics），有机化学家 Géza Zemplén 门下，获化学工程 MS 与 PhD
- **导师**：Géza Zemplén（布达佩斯技术大学有机化学家）
- **博士**：布达佩斯技术大学化学工程（页面未载具体年份与论文题，禁写）
- **研究领域**：碳正离子化学、超酸化学、烃类化学、甲醇经济

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **布达佩斯少年（1927–1949）**：Piarist 中学 → 技术大学 Zemplén 门下；犹太家庭出身。
2. **双肩教授（1949–1956）**：1949–1954 任母校有机化学教授；1954–1956 任匈牙利科学院研究所有机化学部主任、副科学主任——三十岁前已身居要职。
3. **1956 事件与流亡**：匈牙利事件后携家先避英国、再赴加拿大——命运齿轮的转折点。
4. **Dow 化学的八年（1957–1965）**：与同乡化学家 Stephen J. Kuhn 一同加入 Dow Chemical（安大略 Sarnia）；**碳正离子的开创性工作始于 Dow 的这八年**。
5. **重返学界（1965）**：Case Western Reserve University（Cleveland）化学系主任（1965–1969）；1967–1977 任 C. F. Maybery 杰出研究教授。
6. **入籍与南迁（1971/1977）**：1971 入籍美国；1977 迁往 University of Southern California。
7. **超酸与魔酸（USC）**：任杰出教授、Loker 烃类研究所所长（1980 起 Donald P. and Katherine B. Loker 杰出化学教授）；寻找稳定「非经典碳正离子」导致发现被超酸稳定的质子化甲烷——魔酸 FSO₃H-SbF₅。
8. **公式化的胜利**：CH₄ + H⁺ → CH₅⁺——正离子可被稳定后，红外与 NMR 谱学得以深入研究其结构，并用作有机合成催化剂。
9. **非经典碳正离子论战**：与 Saul Winstein 一道，同 Purdue 的 Herbert C. Brown 进行了持续整个职业生涯的论战；Olah 的 NMR 研究为 Winstein 的「电子在三碳间离域」非经典模型提供更多证据。
10. **1994 诺贝尔化学奖**：**独享**，"for his contribution to carbocation chemistry"（页面原句）。
11. **Olah 基金（1997）**：Olah 家族设立 George A. Olah Endowment，每年颁发烃类/石油化学奖（前身 ACS 石油化学奖），由 ACS 遴选管理。
12. **甲醇经济（晚年）**：研究从烃类转化燃料转向甲醇经济——以可再生与核能从 H₂ 与工业/大气 CO₂ 制甲醇（2005 专文）；与 Robert Zubrin、Anne Korin、James Woolsey 推动灵活燃料动议。
13. **身后评价**：匈牙利政府称「国家失去了一位伟大的爱国者与匈牙利科学生活最杰出的人物之一」；诺奖演讲题为 "My Search for Carbocations and Their Role in Chemistry"（1994-12-08）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（钢蓝 steelblue） | `#37548D` | 超酸的冷冽与碳正离子的电性蓝（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（碳正离子 badgeCation） | `#5B76B8` | 蓝 CH₅⁺ / 魔酸 |
| 分类色 2（流亡与 Dow badgeDow） | `#1B7A43` | 绿 1956 / Sarnia 八年 |
| 分类色 3（论战 badgeDebate） | `#D97B29` | 琥珀非经典离子论战 / NMR 证据 |
| 分类色 4（甲醇经济 badgeMethanol） | `#C0395B` | 玫瑰 CO₂→CH₃OH / 能源愿景 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「被超酸捕获的碳正离子」——深场中的一点亮。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Nostalgia** — Alex-Productions（清单指定 `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav`，不要复制 wav 文件，由 Makefile 侧引用）
- **风格**：怀旧 / 温厚 / 回望
- **匹配理由**：
  - "Nostalgia" 匹配叙事的乡愁线——布达佩斯 → 1956 流亡 → Sarnia → Cleveland → USC，一生横跨三国，回望故乡的旋律底色
  - "温厚" 匹配晚年甲醇经济的愿景——为能源与地球寻找出路的公共情怀
  - "回望" 匹配结尾页——匈牙利政府对他的身后评价，故乡最终以其为荣
- **时长**：以文件实际时长为准（> 15 页 × 7 秒 ≈ 105 秒即可），ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 驯服碳正离子的人 / George A. Olah 1927–2017 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/导师/出生地/去世地/领域/机构/荣誉）
03  奥拉的一生 — 时间线（10 节点：1927→1949→1956→1957→1965→1971→1977→1994→1997→2017）
04  布达佩斯：Piarist 与 Zemplén (1927–1956) — 表格「时间|事件|结果」
05  流亡与 Dow 八年 (1956–1965) — 表格「阶段|地点|工作」
06  Case Western (1965–1977) — 表格「岗位|研究|结果」
07  超酸与魔酸 (USC) — 表格「问题|方法|结果」+ 公式框：CH₄ + H⁺ → CH₅⁺（FSO₃H-SbF₅）
08  非经典碳正离子论战 — 表格「人物|立场|证据」（Winstein 模型 vs H. C. Brown；NMR 证据）
09  1994 诺贝尔化学奖 — 表格「口径|原文|意义」（独享；"for his contribution to carbocation chemistry"）
10  学脉与机构 — 表格「机构|角色|时间」（Loker 研究所所长 / Olah Endowment 1997）
11  甲醇经济 — 表格「原料|路径|愿景」+ 公式框：H₂ + CO₂ → CH₃OH（可再生/核能供能）
12  荣誉之殿 — 表格「类别|代表|意义」（Tolman 1991 / Nobel 1994 / ForMemRS 1997 / Priestley 2005 / 旭日章 2003 / 匈牙利 Pro Merit 2006）
13  遗产 — 四分类遗产盒 + 公式框：碳正离子进入教科书
14  结尾 — 「把最不安分的电子，按进最安静的地基。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖口径 | 1994 **独享**（页面无共同得主）；官方理由为页面原句 "for his contribution to carbocation chemistry"——勿扩写为「创立超酸化学」 |
| 姓名序 | 本名 **Oláh András György**（匈牙利姓前名后）；英文署名 George A. Olah——两形式勿混 |
| Dow 年限 | 碳正离子开创性工作始于 Dow 的 **八年**（1957–1965，页面作 eight years with Dow）——勿写成「长期任教」 |
| 国籍变迁 | 1956 后：英国（短暂）→ 加拿大（Dow Sarnia）→ 1965 赴美 → **1971 入籍**；1956 前为匈牙利——勿写「生于奥地利」或「1977 移美时才到美国」（1965 已抵 Case Western） |
| 论战定位 | 论战双方是 **Olah（与 Winstein 一方）vs Herbert C. Brown**；Winstein 是非经典模型的提出者、Olah 提供光谱证据——勿写「Olah 单挑 Brown」或「Brown 提出 Winstein 模型」 |
| H. C. Brown 同名 | Herbert C. Brown（Purdue，1979 化学诺奖得主）——与 Georg Wittig 同年获奖者、与他人勿混；本库另有条目，note 注明 Purdue |
| 博士年份 | 页面仅载 MS 与 PhD 均在布达佩斯技术大学化学工程，**未载年份与论文题**——禁写 |
| 魔酸 | Magic Acid = **FSO₃H-SbF₅**；质子化甲烷 CH₅⁺ 由超酸稳定——化学式与配比勿写错 |
| 机构时间线 | 1965–1969 化学系主任（Case Western）；1977 迁 USC；1980 起 Loker 教授——勿把「Loker 研究所所长」提前到 Case Western 时期 |
| 奖项年份 | Tolman 1991 / Chemical Pioneer 1993 / Nobel 1994 / F. A. Cotton 1996 / ForMemRS 1997 / Cope 2001 / 旭日章 2003 / Priestley 2005 / 匈牙利 Pro Merit 2006——勿错位 |
| 引语红线 | 可引用（页面原文）：诺奖理由句、匈牙利政府身后评价句、诺奖演讲题名；中文引号内不得出现无法在 page.md 溯源的「原话」；「The Martians」须注明出处为 György Marx 的说法 |
| 宗教背景 | 犹太夫妇之子为页面明载，可客观陈述；页面无载的宗教实践/二战遭遇细节禁写 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q192603 | ✅ |
| name_zh | 乔治·安德鲁·奥拉 | ✅ |
| name_en | George Andrew Olah | ✅ |
| birth_date | 1927-05-22 | ✅ |
| death_date | 2017-03-08 | ✅ |
| nationality | Hungary（rank 0）/ United States（rank 1，1971 入籍） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分：carbocation chemistry / superacid chemistry / hydrocarbon chemistry / methanol economy，带 rank） | ✅ |
| has_biography | false（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 家人 / 同事 / 论战对手**（★ 只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Géza Zemplén | 师→生（大学导师） | 布达佩斯技术大学有机化学家，Olah 的 MS/PhD 导师 |
| spouse | Judit Lengyel | 无向 | 1949 年结婚；二子 György（1954）与 Ronald（1959） |
| colleague | Stephen J. Kuhn | 无向 | 同乡化学家，1956 后一同加入 Dow Chemical（Sarnia） |
| colleague | Saul Winstein | 无向 | 非经典碳正离子模型提出者；Olah 的 NMR 研究为其模型提供证据 |
| competitor | Herbert C. Brown | 无向 | Purdue；非经典碳正离子存在性的职业生涯论战对手（1979 化学诺奖） |

> metadata.json-only 的关系（如各类奖章评审人、未在正文出现的合作者）**不予入库**；1994 诺奖为独享，无 co-honored 关系。

## 8. 奖项清单

- Nobel Prize in Chemistry（1994，独享）
- ACS Henry Morley Medal（1970）；California Scientist of the Year（1989）；Roger Adams Award in Organic Chemistry（1989）
- Tolman Award（1991）；Chemical Pioneer Award, American Institute of Chemists（1993）
- ACS F. A. Cotton Medal（1996）；Golden Plate Award（1996）；Foreign Member of the Royal Society, ForMemRS（1997）
- Arthur C. Cope Award（2001）；American Philosophical Society 成员（2001）；Order of the Rising Sun 旭日章（2003）
- Priestley Medal（2005，ACS 最高荣誉）；Hungarian Order of Pro Merit（2006）
- Széchenyi Prize；Centenary Prize；Guggenheim Fellowship；George A. Olah Award in Hydrocarbon or Petroleum Chemistry（以其命名的 ACS 奖项）

## 9. 机构清单

- 教育：Budapesti Piarist Gimnazium；Budapest University of Technology and Economics（化学工程 MS、PhD）
- 任职：布达佩斯技术大学有机化学教授（1949–1954）；匈牙利科学院研究所有机化学部主任、副科学主任（1954–1956）；Dow Chemical, Sarnia, Ontario（约 1957–1965）；Case Western Reserve University（1965–1977，化学系主任 1965–1969，C. F. Maybery 杰出研究教授 1967–1977）；University of Southern California（1977–，杰出教授、Loker Hydrocarbon Research Institute 所长、1980 起 Loker 杰出化学教授）
- 命名机构：George A. Olah Endowment（1997，ACS 管理的年度烃类/石油化学奖）

## 10. 终审清单

- [ ] 生卒 1927-05-22 / 2017-03-08，享年 89，出生地布达佩斯、去世地 Beverly Hills 自宅
- [ ] 1994 独享表述准确；诺奖理由用页面原句
- [ ] 本名 Oláh András György 与英文署名两形式未混；Dow 八年（Sarnia）与 1965 转学界未混
- [ ] 魔酸 FSO₃H-SbF₅ 与 CH₄ + H⁺ → CH₅⁺ 化学式准确；论战三方角色（Olah / Winstein / Brown）准确
- [ ] 1971 入籍、1977 迁 USC、1980 起 Loker 教授时间线准确
- [ ] 引语全部可在本地 Wikipedia 原文找到；「The Martians」注明出处
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/George_Andrew_Olah/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像已就位或装饰圆占位（注明理由）
- [ ] **国籍**：封面顶部明示匈牙利/美国
- [ ] **引语核对**：诺奖理由句、匈牙利政府评价句须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger、Kary_Mullis 等）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 的更新由主控统一收尾（本提示词不直接改动）。
> **最重要的事：每写一页就 make，看到溢出就修。**
