# Arno Allan Penzias（阿尔诺·彭齐亚斯）立传提示词

> qid=Q172877 · 1933-04-26 – 2024-01-22 · 美国物理学家与射电天文学家（生于德国慕尼黑） · 20 世纪 · 1978 诺贝尔物理学奖（与 R. W. Wilson 共享一半）
> 本地 Wikipedia 数据源：`physicist/presentations/20th_century/20th_century/Arno_Allan_Penzias/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家标杆 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**。物理学家立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**本人物 images.txt 无本人肖像（仅 Holmdel 喇叭天线照片与 WMAP 图）→ 封面可用 Holmdel Horn Antenna 照片作场景图替代头像（注明"发现地天线"），身份页头像用装饰圆占位。**
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`；infobox 国籍序列为 德国（至 1935，纽伦堡法案）→ 无国籍（1935–1946）→ 美国（1946 起）——正文身份页可完整呈现这一序列），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像（占位）+ 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、去世地、教育、师承、任职、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色（诺奖金）+ 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「宇宙微波背景的各向同性涨落」母题。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Arno Allan Penzias（阿尔诺·彭齐亚斯）
- **生卒**：1933-04-26 生于德国慕尼黑（Munich, Bavaria）→ 2024-01-22 逝于旧金山（San Francisco, California），享年 90（阿尔茨海默病并发症）
- **国籍序列**：德国（至 1935，纽伦堡法案）→ 无国籍（1935–1946）→ 美国（1946 年入籍）
- **身份**：物理学家、射电天文学家
- **家庭**：父 Karl Penzias、母 Justine（née Eisenreich），慕尼黑经营皮革生意；祖父母自波兰来慕尼黑，是 Reichenbachstrasse 犹太会堂的领袖之一；1939 年（六岁）与弟弟 Gunther 作为犹太儿童经 **Kindertransport（儿童救援行动）撤至英国**；父母随后逃离纳粹德国（先英国后美国），1940 年全家定居纽约布朗克斯
- **婚姻**：1954 年娶 Anne Barras（育 David、Mindy、Laurie 三子女，后离异）；1996 年娶硅谷高管 Sherry Levit（成为其子 Carson、女 Victoria 的继父）
- **教育轨迹**：
  - Brooklyn Technical High School（布鲁克林技术高中，1951 年毕业）
  - 纽约市立学院（CCNY）：入学习化学，后转物理，1954 年毕业（成绩居班级前列）
  - 哥伦比亚大学：M.A. 与 Ph.D.（1962），师从 Charles H. Townes（微波激射器 maser 的发明者）
  - 博士论文：*A tunable maser radiometer and the measurement of 21 cm line emission from free hydrogen in the Pegasus I cluster of galaxies*（1962）
- **军旅**：CCNY 毕业后在美国陆军通信兵（Signal Corps）任雷达军官两年
- **研究领域**：物理、宇宙学（known for：cosmic microwave background）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **Kindertransport 少年（1939）**：六岁与弟弟 Gunther 经儿童救援行动撤至英国——从纳粹德国到纽约布朗克斯的完整流亡线（1933 慕尼黑 → 1939 英国 → 1940 美国 → 1946 入籍）。
2. **从化学到物理**：CCNY 先读化学后转物理；通信兵雷达军官经历把他带进哥伦比亚辐射实验室——雷达是他的命运主线（逃离 → 通信兵雷达 → 哥大微波 → Holmdel 天线）。
3. **Townes 门下（1956–1962）**：在哥伦比亚辐射实验室师从 Charles H. Townes（后发明 maser）；博士论文造可调 maser 射电计并测飞马座 I 星系团自由氢的 21 cm 发射。
4. **Holmdel 喇叭天线（1964）**：在贝尔实验室 Holmdel 园区与 Robert Woodrow Wilson 研制超灵敏低温微波接收机（原为射电天文观测用）；1964 年建成最灵敏的天线/接收系统。
5. **无法解释的噪声（1964）**：遭遇不明射电噪声——能量远低于银河系辐射、**各向同性**；先假设地面干扰，尝试并排除了"来自纽约市"的假设。
6. **鸽子粪与"白色电介质"**：检查喇叭天线发现其内积满蝙蝠与鸽子排泄物——彭齐亚斯称之为"白色电介质材料"（"white dielectric material"，page.md 有原文可加引号）；**清除积粪后噪声依然存在**。
7. **与 Dicke 的对接**：排除一切干扰源后，Penzias 联系普林斯顿的 Robert H. Dicke——Dicke 提出这可能正是某些宇宙学理论预言的背景辐射；双方同意在《Astrophysical Journal》**背靠背发表两封信**：Penzias 与 Wilson 描述观测、Dicke 给出宇宙微波背景（CMB）解释——大爆炸的射电遗迹。
8. **里程碑意义**：这一发现成为大爆炸理论的里程碑证据，并对 Alpher、Herman 与 Gamow 在 1940s–1950s 的预言给出实质性证实。
9. **理论与实验相遇的叙事**：先是"多余的天线噪声"的工程排查，后是普林斯顿理论组的对接——"发现先于理解"的经典案例；后续两人合作发表 4080 MHz 各向同性测量（1967，《Science》）。
10. **贝尔实验室生涯**：长期任职 Bell Labs（Holmdel），从工程师出身的研究者到诺奖得主；1990 年代居新泽西 Highland Park。
11. **荣誉**：美国艺术与科学院院士（1975）、美国国家科学院院士（1975）；Henry Draper Medal（1977，与 Wilson）；1978 诺贝尔物理学奖（与 Wilson 共享另一半，另一半为 Kapitsa）；Golden Plate Award（1979）；Harold Pender Award（1991）；IRI Medal（1998）；Karl G. Jansky Lectureship。
12. **身后的纪念**：2019-04-26（86 岁生日）纽伦堡天文协会在 Regiomontanus-Sternwarte 启用 3 米射电望远镜并献予 Penzias；2023-09-11 美国无线电俱乐部设立 "Dr. Arno A. Penzias Award"（无线电科学基础研究贡献奖）。
13. **晚年**：2024-01-22 因阿尔茨海默病并发症逝于旧金山一家辅助生活机构，享年 90。

## 3. 配色方案

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深空靛） | `#2A3468` | 深空与宇宙微波 / 来自时间起点的信号 |
| 强调色（诺奖金） | `#C9A227` | 诺贝尔奖 / 尊崇 |
| 分类色 1（CMB — 天青） | `#2E8BA8` | 宇宙微波背景 / 各向同性 |
| 分类色 2（射电天文 — 蓝绿） | `#3E8E6B` | 21 cm 氢线 / maser 射电计 |
| 分类色 3（贝尔实验室工程 — 琥珀） | `#C0862E` | 喇叭天线 / 低温接收机 / 排噪排查 |
| 分类色 4（大爆炸宇宙论 — 玫瑰） | `#A8404F` | Dicke 对接 / Alpher-Herman-Gamow 预言 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「宇宙微波背景的各向同性涨落」——均匀分布的圆点隐喻无所不在、各向同性的背景辐射，微小的亮度差即宇宙结构的种子。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：纪录片 / 稳重 / "看不见的微光"（工程排查的耐心与宇宙学的升华）
- **选定曲目**：Infraction **The Invisible Light**（纪录片 / 电影 / 稳重），曲目意象与 CMB——"来自宇宙起点、肉眼不可见的微光"——直接对应。
- **落地文件**：`physicist/presentations/20th_century/Arno_Penzias/The_Invisible_Light.wav`（复制自音乐库，不入 git）。
- **匹配理由**：彭齐亚斯的故事是"把噪声听到宇宙里去"——前半段是工程式的沉稳排查，后半段是宇宙尺度的升华；The Invisible Light 的纪录片气质同时容纳两者。

## 4. Slide 规划（约 15 页，Wilson 式结构）

1. **封面**（`\titleslide`）：顶部标签「宇宙学 · 美国」+ 彭齐亚斯 1933–2024 + 右上 Holmdel 天线照片（场景图，注明"发现地"）+ 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像（占位）+ 右 2×2 信息网格（生卒 / 本名 / 国籍（含序列）/ 出生地 / 去世地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：CMB 的发现 / 射电天文技术 / 大爆炸的实证 / 贝尔实验室工程
4. **慕尼黑与流亡**（1933–1946）：Kindertransport、布朗克斯、1946 入籍——国籍三段序列
5. **从化学到雷达**：CCNY 转物理、通信兵雷达军官
6. **Townes 门下**（1956–1962）：哥伦比亚辐射实验室、maser 射电计、飞马座 I 的 21 cm
7. **Holmdel 喇叭天线**（1964）：超灵敏低温微波接收机、15 米喇叭天线
8. **无法解释的噪声**：各向同性、远低于银河辐射、排除纽约市
9. **鸽子粪与"白色电介质"**：蝙蝠与鸽子排泄物、清理后噪声依旧
10. **与 Dicke 的对接**：背靠背发表于《Astrophysical Journal》、CMB 解释
11. **大爆炸的实证**：Alpher / Herman / Gamow 预言的证实、宇宙学范式意义
12. **贝尔实验室岁月**：工程师出身、4080 MHz 各向同性测量、生涯轨迹
13. **荣誉与纪念**：1977 Draper Medal、1978 诺奖（份额结构写准）、1975 双院院士
14. **身后的天线**：2019 纽伦堡射电望远镜献名、2023 Penzias Award
15. **结尾**：90 岁、来自时间起点的耳语

## 5. 史实陷阱与敏感点（终审必须检查）

- **诺奖份额表述**：1978 年 **Penzias 与 Wilson 共享一半**（"for their discovery of cosmic microwave background radiation"，中文用总名单表述"表彰他们发现宇宙微波背景辐射"）；**另一半为 Kapitsa 独得**（低温物理，与两人工作"互不相关"，page.md 明载 unrelated）——勿写成"三人共同获奖"。
- **鸽子粪轶事的可写边界**：page.md 实载三点——喇叭天线内"积满蝙蝠与鸽子排泄物"、Penzias 称之为 "white dielectric material"、**清除积粪后噪声仍在**。这三点可写；引号仅用于 "white dielectric material"（有原文）。**勿增添 page.md 无载的流行细节**（如两人爬进天线内清扫的具体情节、"捕捉鸽子驱离"等）。
- **Dicke 的角色**：是 **Penzias 主动联系** Dicke（contacted）；Dicke "建议"这可能是背景辐射（suggested）；发表形式是双方约定的**背靠背通讯**（side-by-side letters）——勿写成"普林斯顿团队领导了发现"或"Dicke 共享荣誉"。
- **发现年份链**：1964 建成天线/接收系统并遭遇噪声；发表为《Astrophysical Journal》通讯（page.md 未给发表年份，**1965 禁写**，以"1964 年发现、随后发表"表述）；4080 MHz 各向同性论文 1967 有载。
- **理论与预言归属**：CMB 证实的是 **Alpher、Herman 与 Gamow** 在 1940s–1950s 的预言——三人并列，勿只写 Gamow。
- **国籍序列**：德国（至 1935，纽伦堡法案）→ 无国籍（1935–1946）→ 美国（1946 起）——身份页按 infobox 序列完整呈现；封面统一「美国」。
- **Kindertransport 时间链**：1939 年六岁赴英（与弟 Gunther）；父母随后出逃先英后美、1940 定居布朗克斯——勿倒置。
- **"工程师出身"表述**：两人研制的是"超灵敏低温微波接收机（原为射电天文观测设计）"——按此表述，勿写"电信工程师偶得诺奖"的过度戏剧化因果。
- **同名的 R. W. Wilson**：搭档全名 Robert Woodrow Wilson——与 Charles T. R. Wilson（1927 诺奖）、Kenneth G. Wilson（1982 诺奖）不同人，篇内提及必须全名或加"贝尔实验室的 Wilson"限定。
- **无本人肖像**：images.txt 仅有天线照片与 WMAP 图——封面用天线照片作场景图（注明"发现地 Holmdel Horn Antenna"），身份页头像装饰圆占位。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q172877 | 待写入 |
| name_zh | 彭齐亚斯（或 阿尔诺·彭齐亚斯） | 待写入 |
| name_en | Arno Allan Penzias | 待写入 |
| birth_date | 1933-04-26 | 待写入 |
| death_date | 2024-01-22 | 待写入 |
| nationality | United States（序列：Germany → statelessness → United States） | 待写入 |
| primary_occupation | physicist / astronomer | 待写入 |
| field_of_work | physics / cosmology | 待写入 |
| notable_work | cosmic microwave background | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Charles Hard Townes（哥伦比亚大学，1962；maser 发明者）
- **co-honored**：Robert Woodrow Wilson（1978 共享一半）、Pyotr Leonidovich Kapitsa（1978 另一半，工作无关）
- **搭档（colleague）**：Robert Woodrow Wilson（Holmdel 喇叭天线发现搭档）
- **理论对接（colleague）**：Robert H. Dicke（普林斯顿，CMB 解释；背靠背发表）
- **博士学生**：Pierre Encrenaz
- **家庭**：第一任妻 Anne Barras（1954，三子女，离异）；第二任妻 Sherry Levit（1996）

## 7.5 术语清单（对齐标杆 §9，8 条）

| 英文 | 中文 | 风险点 |
|------|------|------|
| cosmic microwave background (CMB) | 宇宙微波背景 | 1978 诺奖发现本体，勿写"预言" |
| Holmdel Horn Antenna | 霍姆德尔喇叭天线 | 发现地装置，超灵敏低温微波接收系统 |
| isotropic | 各向同性 | 噪声的关键特征，排除银河系来源的依据 |
| Kindertransport | 儿童救援行动 | 1939 六岁赴英，流亡线勿倒置 |
| maser radiometer | 微波激射器射电计 | 博士论文装置（Townes 门下） |
| 21 cm line | 21 厘米谱线 | 飞马座 I 星系团自由氢测量 |
| white dielectric material | 白色电介质材料 | 鸽子粪轶事唯一可引原话 |
| back-to-back letters | 背靠背通讯 | 与 Dicke 组在 Astrophysical Journal 的发表形式 |

## 8. 奖项清单

- 诺贝尔物理学奖（1978，与 R. W. Wilson 共享一半；另一半为 Kapitsa）
- Henry Draper Medal（1977，美国国家科学院，与 Wilson）
- Harold Pender Award（1991）；IRI Medal（1998，工业研究院）
- Golden Plate Award of the American Academy of Achievement（1979）；纽约 The International Center 卓越奖
- Karl G. Jansky Lectureship；Herschel Medal
- 美国艺术与科学院院士（1975）、美国国家科学院院士（1975）
- 纽伦堡 3 米射电望远镜献名（2019）；Radio Club of America "Dr. Arno A. Penzias Award"（2023 设立）

## 9. 机构清单

- 教育：Brooklyn Technical High School（1951）→ 纽约市立学院 CCNY（B.S. 1954，化学转物理）→ 哥伦比亚大学（M.A.、Ph.D. 1962，辐射实验室）
- 任职：美国陆军通信兵雷达军官（两年）；Bell Labs（Holmdel Township, New Jersey，长期任职）
- 纪念机构：纽伦堡 Regiomontanus-Sternwarte（2019 献名射电望远镜）

## 10. 终审清单

- [ ] 生卒 1933-04-26 / 2024-01-22，享年 90，出生地 Munich，去世地 San Francisco
- [ ] 1978 份额结构"两人共享一半、Kapitsa 另一半、工作无关"表述准确
- [ ] 鸽子粪仅写 page.md 实载三点，引号仅 "white dielectric material"
- [ ] Dicke"被联系、建议解释、背靠背发表"表述准确
- [ ] 通讯发表年份未标 1965（page.md 无载）
- [ ] Alpher / Herman / Gamow 三人并列
- [ ] 国籍三段序列完整（Germany → statelessness → US）
- [ ] 无本人肖像：封面天线场景图 + 身份页装饰圆占位，品牌 OpenMathAI
- [ ] 正文采用 Wilson 式：身份信息页 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `Arno_Allan_Penzias/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：封面天线场景图 + 身份页装饰圆占位（images.txt 无本人肖像）
- [ ] **国籍**：封面顶部徽章明示美国，身份页含国籍序列
- [ ] **引语核对**：仅 "white dielectric material" 一处（page.md 有原文）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 1978 同届（Kapitsa / R. W. Wilson）格式对齐，CMB 叙事口径一致

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
