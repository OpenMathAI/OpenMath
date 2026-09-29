# Carl Bosch（卡尔·博施）立传提示词

> qid=Q76606 · 1874-08-27 – 1940-04-26 · 德国化学家与工程师 · 诺贝尔化学奖（1931，与 Friedrich Bergius 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Carl_Bosch/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**严格对齐 Frederick Sanger 立传模板**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金色公式框 + 气泡背景。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 images.txt 仅有签名与 IG Farben 图（无独照）：主肖像先查 page.html infobox 原图名（c. 1929 肖像未被抓取），再试 Commons `Special:FilePath/Carl Bosch.jpg?width=600` 与 REST API `page/summary`；`IGFarbenGoetterrat.jpg`（Groeber 油画，Bosch 坐于前排）可作插图；全部失败用装饰圆占位，并在 §11 Review 注明。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{industry}\enspace 把空气变成面包的工程师\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「高压反应釜 / 工业塔群」母题——离散圆点暗示合成塔中的高压分子。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 N₂ + 3H₂ → 2NH₃（Haber–Bosch）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Carl Bosch（中文惯称：卡尔·博施；与 Robert Bosch GmbH 创始人 Robert Bosch 是叔侄关系）
- **生卒**：1874-08-27 生于德意志帝国 Cologne → 1940-04-26 逝于 Heidelberg，享年 65
- **国籍**：Germany（德国；frontmatter 作 German Reich）
- **身份**：化学家与工程师（chemist, engineer；高压工业化学先驱；IG Farben 创始人与首任领袖）
- **家庭**：父 Carl Friedrich Alexander Bosch（1843–1904）为成功的燃气与管道供应商；叔父 Robert Bosch（火花塞先驱、Bosch 公司创始人）；1902 年娶 Else Schilbach，育有一子一女
- **教育轨迹**：在冶金与化学之间抉择，1892–1898 就读柏林 Charlottenburg 王立技术学院（今 TU Berlin）与莱比锡大学
- **导师**：Johannes Wislicenus（莱比锡）
- **博士**：1898 年莱比锡大学，有机化学方向
- **研究领域**：化学——高压化学、催化、合成氨工业、合成燃料

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **科隆商人世家（1874）**：燃气与管道供应商之子，叔父是创办 Bosch 公司的 Robert Bosch——工程与产业的基因深植家庭。
2. **从冶金到化学（1892–1898）**：Charlottenburg 技术学院 + 莱比锡大学；1898 年在 Wislicenus 指导下获有机化学博士。
3. **BASF 起步（1899）**：以初级职位进入当时德国最大的化工与染料公司 BASF。
4. **哈伯的桌面实验 → 世界工厂（1909–1913）**：把 Fritz Haber 的合成氮桌面演示，经 Haber–Bosch 工艺放大为工业规模的合成硝酸盐生产——「把空气变成面包」的工程奇迹。
5. **工程师的攻坚清单**：耐高压高温的设备与工厂设计、大型压缩机、安全高压炉、廉价纯净氢气原料、氨的纯化与加工；Oppau 建成第一座全套 Haber–Bosch 工厂。
6. **催化剂突破**：为哈伯工艺找到比稀缺的 osmium 与昂贵的 uranium 更实用的催化剂。
7. **Bosch 反应与 Bosch–Meiser 尿素工艺**：以己名留世的两个工业化学过程。
8. **战后高压版图**：一战后把高压技术扩展到 Bergius 工艺合成燃料与甲醇生产。
9. **IG Farben（1925）**：协助创建当时世界最大的化工公司 IG Farben 并任首任领袖；1926 年 9 月公司股票以其主席身份签署（配图 I.G. Farbenindustrie AG）。
10. **1931 诺贝尔化学奖**：与 Friedrich Bergius 共享，官方口径 "in recognition of their contributions to the invention and development of chemical high pressure methods"。
11. **与纳粹的周旋（1932–1935）**：1932 年中派两位 IG Farben 高管面见 Hitler，试图阻止纳粹对合成燃料项目的政治攻击；1933 年 12 月纳粹政府给予 Leuna 合成油扩产价格与收购保障；1933 年起公开反对纳粹的自给自足与压制政策，渐被边缘化；1935 年起任监事会主席，实权旁落。
12. **科学公益领袖**：1937 年任 Kaiser Wilhelm Society（威廉皇帝学会）主席；1924 年获 Siemens-Ring 以表彰其应用研究贡献与对基础研究的支持。
13. **陨落与身后（1940）**：因许多纳粹政策（包括反犹主义）受抨击而被逐步解除高位，陷入抑郁与酗酒，1940-04-26 逝于 Heidelberg；小行星 7414 Bosch 以其命名；陨石与矿物标本先借展 Yale、后由 Smithsonian 收购。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（勃艮第红 burgundy） | `#7A1E28` | 高压钢铁与工业时代的厚重（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（合成氨 badgeAmmonia） | `#2E5A9E` | 蓝 Haber–Bosch / 合成氨 |
| 分类色 2（高压化学 badgeHighP） | `#8A5A1E` | 赭金高压釜 / 催化剂 |
| 分类色 3（工业帝国 badgeIGFarben） | `#4A3A6E` | 紫 IG Farben / 巴斯夫 |
| 分类色 4（合成燃料 badgeFuel） | `#2E6B4A` | 绿 Bergius 工艺放大 / 甲醇 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「高压反应 / 工业塔群」的意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Empire Collapse** — Cold Cinema（文件 `music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav`，不要复制 wav 文件）
- **风格**：史诗 / 管弦 / 帝国兴衰的戏剧张力
- **匹配理由**：
  - "帝国崩塌" 直接呼应 IG Farben 帝国的兴衰与其个人结局——从世界最大化工公司首任领袖到被纳粹边缘化、抑郁而终
  - "史诗管弦" 匹配 Haber–Bosch 工业化的宏大尺度——今日供养全球约三分之一人口
  - 与批次内其他曲目（Bergius=Ascension 同属 Cold Cinema 系列）为姊妹篇，两人共享 1931 诺奖，曲风同源而主题各异
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐（15 页 × 7 秒 ≈ 105 秒）

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 把空气变成面包的工程师 / Carl Bosch 1874–1940 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/出生地/去世地/领域/荣誉）
03  博施的一生 — 时间线（10 节点：1874→1898→1899→1909→1919→1925→1931→1935→1937→1940）
04  早年：科隆与莱比锡 (1874–1898) — 表格「时间|事件|结果」
05  BASF 起步 (1899–1908) — 表格「阶段|职责|结果」
06  Haber–Bosch 工艺 (1909–1913) — 表格「问题|方法|结果」+ 公式框：N₂ + 3H₂ → 2NH₃
07  工程攻坚：高压世界 — 表格「障碍|方案|结果」（压缩机/高压炉/氢源/催化剂替代 Os、U）
08  战后高压版图：合成燃料与甲醇 — 表格「工艺|原料|结果」（Bergius 工艺放大 / Bosch–Meiser 尿素）
09  IG Farben (1925–1935) — 表格「年份|事件|结果」+ Groeber 油画插图（IGFarbenGoetterrat.jpg）
10  1931 诺贝尔化学奖 — 表格「人物|贡献|结果」+ 官方获奖理由英文原句
11  与纳粹的周旋 (1932–1940) — 表格「年份|事件|结果」——事实陈述页（1932 面见 Hitler 未遂 / 1933 Leuna 保障 / 1933 起反对与边缘化 / 1937 KWS 主席）
12  荣誉与遗产 — 高斯式「类别|代表|意义」表格（Siemens-Ring 1924 / Liebig Medal 1919 / Exner Medal 1932 / Goethe Prize 1939 / 小行星 7414 Bosch）
13  遗产：供养世界的氮 — 四分类遗产盒 + 公式框：今日 1 亿吨氮肥/年 · 人类能源产出 >1% · 人体一半氮来自合成固氮
14  结尾 — 「他把大气中的氮，变成了餐桌上的粮食。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1931 获奖口径 | 官方措辞 "in recognition of their contributions to the invention and development of chemical high pressure methods"（正文引言作 "introduction of high pressure chemistry"）——与 Bergius **共享**，勿写独享 |
| Haber 与 Bosch 分工 | **Haber** 是桌面演示与方法发明，**Bosch** 是工业化放大（设备、高压、催化剂）——功劳勿互换；勿写博施"发明"合成氨 |
| 催化剂归属 | 博施负责找到比 **osmium、uranium** 更实用的催化剂——勿写他发明了最初催化剂 |
| Bosch 反应 ≠ Haber–Bosch | Bosch reaction（CO₂+H₂ → C+H₂O）与 Haber–Bosch（合成氨）是**两个不同反应**，勿混 |
| 叔侄关系 | Robert Bosch 是**叔父**（spark plug 先驱、Bosch 公司创始人）——叙述可写，**不入库**（非父子关系类型） |
| 纳粹段落口径 | 1932 派高管面见 Hitler「试图阻止纳粹攻击合成燃料项目」、1933 反对 autarky 与镇压政策、渐被边缘化——按正文客观陈述；1933-12 Leuna 保障是纳粹政府的决定，勿写成博施促成 |
| 职务表述 | 1925「helped found IG Farben, first head」；1935 起董事长角色「largely ceremonial」——勿写成 1935 年才创建或一直掌权 |
| 死因 | 抑郁与酗酒（正文明载）后逝于 Heidelberg——客观陈述，勿扩写医学细节 |
| 配偶 | Else Schilbach（1902 结婚），一子一女——无载之名禁写 |
| 遗产数字 | 「今日生产 1 亿吨氮肥/年」「消耗人类能源产出 >1%」「供养约 1/3 人口」「人体约一半氮为合成固氮来源」——四个数字均正文实载，勿夸大或混用 |
| IChemE 评选 | Haber 与 Bosch 被 Institution of Chemical Engineers 会员评为**史上最具影响力化学工程师**——勿写"最伟大化学家" |
| 页面无载禁写 | page.md **未载**其具体学历成绩、更多子嗣细节——勿补写 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76606 | ✅ |
| name_zh | 卡尔·博施 | ✅ |
| name_en | Carl Bosch | ✅ |
| birth_date | 1874-08-27 | ✅ |
| death_date | 1940-04-26 | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分：chemistry / high-pressure chemistry / chemical engineering / industrial chemistry，带 rank） | ✅ |
| has_biography | false（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作者 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Johannes Wislicenus | 师→生（莱比锡博士导师） | 1898 年有机化学博士 |
| colleague | Fritz Haber | 无向 | Haber–Bosch 工艺：Haber 发明方法，Bosch 完成工业放大 |
| colleague | Friedrich Bergius | 无向 | 一战后博施将高压技术扩展至 Bergius 工艺合成燃料；Bergius 专利后售予 BASF 由其继续 |
| co-honored | Friedrich Bergius | 无向 | 1931 诺贝尔化学奖共同得主 |

**配偶**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Else Schilbach | 无向 | 1902 年结婚，育有一子一女 |

> **禁入库名单（叙事/图注 only）**：Robert Bosch（叔父，非直系亲子）、Carl Duisberg（仅 Groeber 油画同框，无明载关系）、Edmund ter Meer（同上）、Adolf Hitler（1932 会见为政治事件，非科学关系）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1931，与 Friedrich Bergius 共享）
- Liebig Medal of German Chemists Association（1919）
- Werner von Siemens Ring（1924）
- Honorary doctorate, Technische Hochschule Karlsruhe（1918）
- Wilhelm Exner Medal of Austrian Trade Association（1932）
- Bunsen Medal of the German Bunsen Society
- Golden Grashof Memorial Medal of the VDI
- Carl Lueg Memorial Medal
- Goethe Prize of the City of Frankfurt（1939）
- National Inventors Hall of Fame（frontmatter 明载）
- 小行星 7414 Bosch 命名；月球无载勿写

## 9. 机构清单

- 教育：Königliche Technische Hochschule Charlottenburg（今 TU Berlin，1892–）+ University of Leipzig（–1898，PhD 1898，导师 Johannes Wislicenus）
- 任职：BASF（1899 入职，1919 Liebig Medal 时期已是核心）→ Haber–Bosch Oppau 工厂（1909–1913 建成）→ IG Farben 首任领袖（1925 协助创建）→ 监事会主席（1935–，礼仪性）→ Kaiser Wilhelm Society 主席（1937）
- 身后：陨石/矿物收藏 → 借展 Yale → Smithsonian 收购；安葬 Heidelberg Bergfriedhof

## 10. 终审清单

- [ ] 生卒 1874-08-27 / 1940-04-26，享年 65，出生地 Cologne、去世地 Heidelberg
- [ ] 1931 共享（Bergius）表述准确；官方获奖理由英文原句完整呈现
- [ ] Haber/Bosch 分工准确；催化剂替代 Os/U 归属正确；Bosch reaction 与 Haber–Bosch 勿混
- [ ] 纳粹段落客观陈述：1932 会见意图、1933 起反对与边缘化、1935 礼仪性主席
- [ ] 遗产四个数字（1 亿吨/年、>1% 能源、1/3 人口、人体一半氮）全部正文实载
- [ ] 叔父 Robert Bosch 仅叙述不入库
- [ ] 无编造引语——全文用间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Carl_Bosch/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：检查主肖像获取结果（REST API / 装饰圆占位）并记录；Groeber 油画仅作插图
- [ ] **国籍**：封面顶部明示德国
- [ ] **引语核对**：全文不得出现无法在 page.md 溯源的"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Frederick_Sanger_zh.tex）对齐
