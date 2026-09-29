# Kurt Alder（库尔特·阿尔德）立传提示词

> qid=Q76595 · 1902-07-10 – 1958-06-20 · 德国化学家 · 20 世纪 · 诺贝尔化学奖（1950，与 Otto Diels 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Kurt_Alder/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金色公式展示框 + 气泡背景，是本次撰写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。⚠️ 本地 images.txt 仅有墓碑照片（Grab-kurt-alder.jpg），**非肖像禁用**——若无真实肖像则按模板用装饰圆占位，图注写「肖像暂缺·装饰占位」。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 二烯合成的建筑师\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像（或装饰圆）+ 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「双烯体 + 亲双烯体 → 六元环」的环化母题——大小错落的圆点暗示六元环骨架上的原子。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化——Diels–Alder 反应式（环戊二烯 + 顺丁烯二酸酐 → 桥环加成物）是全篇视觉锚点。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Kurt Alder（中文惯称：库尔特·阿尔德）
- **生卒**：1902-07-10 生于上西里西亚 Königshütte（今波兰 Chorzów，时属德意志帝国）→ 1958-06-20 逝于科隆（西德），享年 55
- **国籍**：Germany（德国；生于德意志帝国，逝于西德）
- **身份**：化学家（chemist）、大学教授（university teacher）、诺贝尔化学奖得主
- **家庭**：教师之子（page.md 原文 "as a teacher's son"）；page.md 无载配偶与子女——禁写
- **教育轨迹**：
  - 早年在 Königshütte 当地接受启蒙教育
  - 1922 Königshütte 划归波兰，离开该地区
  - 1922 起柏林大学（University of Berlin / Humboldt-Universität zu Berlin）攻读化学
  - 后转基尔大学（University of Kiel），1926 年获博士学位（导师 Otto Paul Hermann Diels）
- **导师**：Otto Paul Hermann Diels（博士导师；infobox doctoral_advisor）
- **研究领域**：有机化学（organic chemistry）——Diels–Alder 反应、Alder-ene 反应、二烯合成、合成橡胶

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **西里西亚教师之子（1902）**：生于上西里西亚工业区 Königshütte，在家乡完成早期学业——工业区的化工氛围是他职业志向的底色。
2. **边界变迁中的少年（1922）**：Königshütte 划归波兰，20 岁的阿尔德离开故土西行——同年进入柏林大学攻读化学。
3. **柏林→基尔（1922–1926）**：先在柏林大学打下化学根基，后转入基尔大学，1926 年在 Otto Diels 指导下获博士学位——从此与 Diels 的名字永远联系在一起。
4. **1928 年关键论文**：Diels 与 Alder 在《Justus Liebigs Annalen der Chemie》460 卷发表「Synthesen in der hydroaromatischen Reihe」（氢芳香族系列的合成）——Diels–Alder 反应正式诞生：共轭双烯与亲双烯体一步构建六元环。
5. **基尔讲席（1930–1936）**：1930 年任基尔大学化学讲师（reader），1934 年升任 lecturer——在 Diels 身边继续二烯化学的系统研究。
6. **Alder-ene 反应**：以他命名的「烯反应」（ene reaction）——另一个以 Alder 冠名的人名反应，与 Diels–Alder 反应是**两个不同的反应**。
7. **转向工业（1936–1940）**：1936 年离开基尔加入 Leverkusen 的 I G Farben Industrie，从事合成橡胶研究——二烯化学从实验室走向工业。
8. **科隆教授（1940）**：1940 年出任科隆大学实验化学与化学技术教授、化学研究所所长——在战时欧洲研究条件艰难的岁月里仍坚持系统研究。
9. **151 篇论文**：终其一生在这一领域发表超过 151 篇论文——高产而专一。
10. **与 Münz 的合作（1945–1949）**：1945 年起与 EDTA 发明人 Ferdinand Münz 密切合作，1949 年两人共同发表二烯合成与加成论文。
11. **1950 诺贝尔化学奖**：与其导师 Diels 共享，获奖工作即 Diels–Alder 反应——教科书式的「师生同奖」。
12. **以他命名**：月球环形山 Alder 以他命名；经 Diels–Alder 反应制备的杀虫剂 aldrin（艾氏剂）亦以他命名——人名反应、环形山、杀虫剂三重纪念。
13. **骤然离世（1958）**：1958 年 6 月 20 日逝于科隆，享年 55，两周后才在公寓被发现，死因不详；去世前他在致诺贝尔得主会议常务委员会的信中写道（英文原文可溯源）：页载 "The relentless and ever-increasing demands placed on active German university professors by constantly new tasks have, in my case, after years of depleting my strength, led to exhaustion..."——过劳的悲怆注脚。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深松绿 deeppine） | `#1E6B52` | 六元环骨架的有机化学之绿（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（Diels–Alder 反应 badgeDA） | `#2E5A9E` | 蓝双烯加成 / 1928 论文 |
| 分类色 2（Alder-ene 反应 badgeEne） | `#D97B29` | 琥珀烯反应 / 人名反应 |
| 分类色 3（工业应用 badgeInd） | `#C0395B` | 玫瑰合成橡胶 / IG Farben |
| 分类色 4（基尔·科隆 badgeUni） | `#5C3A21` | 褐大学讲席 / 研究所 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「六元环 / 环加成」的环状骨架。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Lonesome** — AShamaluevMusic（文件：`music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav`；**不要复制 wav 文件**，执行阶段按 Makefile 常规软链/引用）
- **风格**：忧伤 / 情感 / 电影感
- **匹配理由**：
  - "Lonesome（孤独）" 匹配其结局——55 岁骤逝、两周后才被发现、死因不详的悲怆尾声
  - "情感" 匹配叙事张力——师生同奖的高光与过劳早逝的暗面对照
  - "电影感" 匹配传记叙事——西里西亚 → 基尔 → 科隆 → 诺贝尔 → 环形山命名
- **时长**：以文件实际时长为准（须 > 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐）

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 二烯合成的建筑师 / Kurt Alder 1902–1958 + 四色 badge + 右上头像（或装饰圆）+ 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/去世地/教育/博士导师/领域/荣誉）
03  阿尔德的一生 — Sanger 式时间线（10 节点：1902→1922→1926→1928→1930→1936→1940→1945→1950→1958）
04  西里西亚与求学 (1902–1926) — 表格「时间|事件|结果」
05  基尔：与 Diels 的师生缘 (1926–1936) — 表格「时间|事件|结果」+ 公式框：Diels–Alder 反应通式
06  1928 关键论文 — 表格「问题|方法|结果」+ 公式框：环戊二烯 + 亲双烯体 → 桥环产物
07  从基尔到工业与科隆 (1936–1940) — 表格「阶段|机构|产出」
08  与 Münz 合作 (1945–1949) — 表格「人物|方向|结果」
09  1950 诺贝尔化学奖 — 表格「理由|口径|意义」+ 公式框：获奖理由（师生同奖）
10  人名反应的版图 — 表格「反应|提出|地位」（Diels–Alder / Alder-ene / aldrin / 环形山）
11  荣誉与纪念 — Sanger 式「类别|代表|意义」表格（含 itemize 荣誉清单：Nobel 1950 / Emil Fischer Medal / Fresenius Prize）
12  骤然离世 — 科隆岁月 + 1958 信件原文框（英文整句引用）+ 两周后才被发现
13  遗产：环加成改变有机合成 — 四分类遗产盒 + 公式框：Diels–Alder 反应的现代地位
14  结尾 — 「一步成环，把六元环写进了合成化学的语法。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 共享口径 | 1950 与导师 Otto Diels **共享**，勿写独享；「师生同奖」表述可保留 |
| 获奖理由 | page.md 实载口径 "shared with his teacher Diels for their work on the Diels–Alder reaction"；官方 citation 口径 "for his discovery and development of the diene synthesis"（此为 Nobel 官网口径、非本地页面实载，仅作表述参考、不作人物引语使用）——两口径不矛盾，勿混写 |
| 出生地口径 | Königshütte（Chorzów），**当时属德意志帝国、今属波兰**——勿写「波兰化学家」；国籍 Germany |
| 卒日 | 1958-06-20（infobox），正文仅载 "June 1958"——两处一致勿写 7 月 |
| 死因 | page.md 明载 **cause unknown**（两周后才在科隆公寓被发现）——严禁编造死因 |
| 两个反应 | **Diels–Alder 反应**（[4+2] 环加成）与 **Alder-ene 反应**（烯反应）是两个不同反应，勿混写 |
| aldrin | 经 Diels–Alder 反应制备的杀虫剂 aldrin 以科学家命名——不是他发明的农药，勿写「他发明杀虫剂」 |
| 家庭 | page.md 无载配偶与子女——禁写 |
| 引语 | 去世前致信为 page.md 实载英文原句（可整句引用原文）；除此之外无直接引语——中文引号内禁编造「原话」 |
| 肖像 | images.txt 仅有墓碑照片 Grab-kurt-alder.jpg——**非肖像禁用作头像**，用装饰圆占位 |
| 151 篇 | "more than 151 papers" 指其合成领域一生的发表总量——勿写成「某一年」 |
| 同名区分 | 伯克利理论化学家 Berni Alder（库内另有记录）与本篇 Kurt Alder 无关，勿混 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76595 | ✅ |
| name_zh | 库尔特·阿尔德 | ✅ |
| name_en | Kurt Alder | ✅ |
| birth_date | 1902-07-10 | ✅ |
| death_date | 1958-06-20 | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分：organic chemistry / Diels–Alder reaction / diene synthesis / synthetic rubber，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 共同得主 / 合作者**（★红线：只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Otto Diels | 师→生（博士导师） | 1926 基尔大学博士导师 |
| co-honored | Otto Diels | 无向 | 1950 诺贝尔化学奖共同得主（Diels–Alder 反应） |
| colleague | Ferdinand Münz | 无向 | 1945 起密切合作，1949 共同发表二烯合成与加成论文；EDTA 发明人 |

> **对手方名规范**：Otto Diels 用 frontmatter 名 `Otto Diels`（Diels 本篇提示词由 chem-batch-10 执行，两批共用同一 frontmatter 名，防分裂 stub）。
> **禁入库名单**：page.md 未载 Alder 的配偶/子女/门生，metadata.json 亦无额外关系——本篇无禁入项。

## 8. 奖项清单

- Nobel Prize in Chemistry（1950，与 Otto Diels 共享）
- Emil Fischer Medal（infobox award_received）
- Fresenius Prize（infobox award_received）
- 若干荣誉学位（page.md：several honorary degrees，具体名目无载——禁列具体大学）

## 9. 机构清单

- 教育：University of Berlin / Humboldt-Universität zu Berlin（1922–）、University of Kiel（PhD 1926）
- 任职：University of Kiel（1930 reader，1934 lecturer）；I G Farben Industrie, Leverkusen（1936–1940，合成橡胶）；University of Cologne（1940 教授 + 化学研究所所长，直至 1958 去世）

## 10. 终审清单

- [ ] 生卒 1902-07-10 / 1958-06-20，享年 55，出生地 Königshütte（今 Chorzów）、去世地科隆
- [ ] 1950 与 Diels 共享表述准确；获奖理由两口径区分清楚
- [ ] Diels–Alder 反应与 Alder-ene 反应未混写；aldrin 命名口径准确
- [ ] 死因「不详」如实表述；去世信英文原句可溯源
- [ ] 家庭信息未杜撰（无配偶/子女）
- [ ] 引语全部可在本地 page.md 原文找到；中文引号内无编造原话
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误、溢出达标

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 page.md 逐页对照 Beamer tex 全部事实
- [ ] 头像：无真实肖像，确认装饰圆占位 + 图注「肖像暂缺」
- [ ] 国籍：封面顶部明示德国
- [ ] 引语核对：去世信原句必须在 page.md 原文找到
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：由 chem-batch-09 执行；`chemist/generate_20th_century_list.py` 由主控统一收尾，本篇不改动。
