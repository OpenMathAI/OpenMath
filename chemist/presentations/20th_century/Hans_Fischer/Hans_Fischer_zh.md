# Hans Fischer（汉斯·费歇尔）立传提示词

> qid=Q76604 · 1881-07-27 – 1945-03-31 · 德国有机化学家 · 诺贝尔化学奖（1930，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Hans_Fischer/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**严格对齐 Frederick Sanger 立传模板**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金色公式框 + 气泡背景。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 images.txt 仅有 `Nobel_ceremony_1930.jpg`（授奖典礼合影，可作插图**非主肖像**）：主肖像先查 page.html infobox 原图名（1930 年肖像图未被抓取），再试 Commons `Special:FilePath/Hans Fischer (chemist).jpg?width=600` 与 REST API `page/summary`；全部失败用装饰圆占位（主色渐变 + 姓名首字母），并在 §11 Review 注明。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 血红素与叶绿素的合成者\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育（化学+医学双科）、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「卟啉环 / 色素分子」母题——离散圆点暗示血红素与叶绿素共有的四吡咯大环。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如血红素 = 卟啉环 + 中心铁原子。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Hans Fischer（中文惯称：汉斯·费歇尔；与 Emil Fischer / Otto Fischer / Ernst Otto Fischer 均非同一人）
- **生卒**：1881-07-27 生于普鲁士王国黑森-拿骚 Höchst am Main（今法兰克福市区）→ 1945-03-31（复活节星期日）逝于慕尼黑（自杀），享年 63
- **国籍**：Germany（德国）
- **身份**：有机化学家（organic chemist；1930 诺贝尔化学奖独享得主；兼具医学训练）
- **家庭**：父 Dr. Eugen Fischer 为 Kalle & Co.（Wiesbaden）董事、Stuttgart 技术学院 Privatdozent；母 Anna Herdegen；1935 年（约 50 多岁）娶 Wiltrud Haufe
- **教育轨迹**：
  - Stuttgart 读小学；Wiesbaden「Humanistisches Gymnasium」1899 年毕业
  - 读化学与医学：先 Lausanne 大学，后 Marburg 大学；1904 年化学毕业
  - 1906 年获行医执照；1908 年获 M.D.；此后申请进入慕尼黑大学（LMU München）
- **导师**：Theodor Zincke（infobox 博士导师，Marburg）；Emil Fischer 为 Other academic advisors（柏林第一化学研究所）
- **研究领域**：有机化学——吡咯化学、血红素与叶绿素、胆汁色素、临床化学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **化学工业之家（1881）**：Kalle & Co. 董事之子，Wiesbaden 文理中学出身——化工与学术的双重家风。
2. **化学 + 医学双科（1899–1908）**：Lausanne 与 Marburg 攻读化学与医学，1904 化学、1906 行医执照、1908 M.D.——双学位塑造了他贯穿一生的「医学化学」视角。
3. **慕尼黑临床起点**：先在慕尼黑 Medical Clinic 工作；1910 年受 von Müller 教授（其兴趣所在即吡咯色素）邀请加入著名的慕尼黑第二 Medical Clinic——胆色素 bilirubin 组成研究由此起步，并延续数十年。
4. **柏林淬炼**：进入柏林第一化学研究所，在 Emil Fischer 指导下工作。
5. **回归慕尼黑（1911–1916）**：1911 回 LMU；1912 任内科学讲师；1913 任生理学研究所生理学讲师——临床与基础双线并行。
6. **教授之路（1916–1921）**：1916 任 Innsbruck 大学医学化学教授；1918 转 Vienna 大学；1921 年起任慕尼黑工业大学有机化学教授直至去世。
7. **吡咯王国**：毕生工作围绕血液、胆汁色素与叶绿素，以及这些色素共同的化学母核——吡咯。
8. **血红素合成（1929）**：成功合成 haemin 并证明其环中心是铁原子——1930 年诺奖的直接前奏。
9. **1930 诺贝尔化学奖（独享）**：官方理由 "for his researches into the constitution of haemin and chlorophyll and especially for his synthesis of haemin"；诺奖演讲 1930-12-11。
10. **胆色素双璧**：阐明 biliverdin（瘀伤青黄之色）与 bilirubin（黄疸之黄）的组成，并于 **1942、1944 年先后合成**两者。
11. **60,000 次微量分析**：一生完成超过 60,000 种化学物质的微量分析——数字本身即是实验强度的证词。
12. **荣誉轨迹**：Leopoldina 院士（1919）、Geheimrat（1925）、Liebig Medal（1929）、哈佛荣誉博士（1936）、Davy Medal（1937）。
13. **毁灭与终局（1945）**：实验室与毕生工作毁于二战末期慕尼黑大轰炸；1945-03-31 复活节星期日自杀身亡——德国科学史上最沉痛的一页（事实陈述，勿渲染细节）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深松绿 darkpine） | `#2F5D50` | 色素化学的深沉底色（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（血红素 badgeHaem） | `#8A2A2A` | 深红血红素 / 铁 |
| 分类色 2（叶绿素 badgeChloro） | `#2E7D3E` | 绿叶绿素 / 光合作用 |
| 分类色 3（胆色素 badgeBile） | `#B8860B` | 暗金 bilirubin / biliverdin |
| 分类色 4（吡咯化学 badgePyrrole） | `#4A3A6E` | 紫吡咯母核 / 卟啉环 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「卟啉大环 / 色素分子」的意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Last Hope** — Victor Cooper（文件 `music_audio/inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav`，不要复制 wav 文件）
- **风格**：戏剧性 / 悲壮 / 强大的史诗感
- **匹配理由**：
  - "最后的希望" 直接呼应其终局——毕生工作毁于轰炸后的 1945 年复活节，作品标题与人物命运形成克制而有力的对位
  - "戏剧性史诗" 匹配血红素合成这一 20 余年攻坚的宏大叙事
  - 与批次内其他曲目（Harden=Nostalgy、Euler-Chelpin=Through the Darkness）不重复
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐（15 页 × 7 秒 ≈ 105 秒）

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 血红素与叶绿素的合成者 / Hans Fischer 1881–1945 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育双科/博士导师/出生地/去世地/领域/荣誉）
03  费歇尔的一生 — 时间线（10 节点：1881→1899→1904→1908→1910→1916→1921→1929→1930→1945）
04  早年：化工之家与双科学业 (1881–1908) — 表格「时间|事件|结果」
05  慕尼黑与柏林 (1908–1916) — 表格「阶段|导师|结果」（von Müller / Emil Fischer）
06  教授之路：因斯布鲁克→维也纳→慕尼黑工大 (1916–1921) — 表格「年份|大学|职位」
07  吡咯与色素王国 — 表格「色素|问题|结果」+ 公式框：卟啉大环 = 四吡咯 + 金属中心
08  血红素合成 (1929) — 表格「问题|方法|结果」+ 公式框：haemin = 卟啉环 + 中心 Fe
09  1930 诺贝尔化学奖（独享） — 表格「理由|演讲|意义」+ 官方获奖理由英文原句
10  胆色素：biliverdin 与 bilirubin — 表格「色素|颜色|合成年份」（1942 / 1944）
11  荣誉与学术地位 — 高斯式「类别|代表|意义」表格（Leopoldina / Liebig Medal / Harvard / Davy Medal）
12  毁灭：慕尼黑大轰炸 (1944–1945) — 表格「事件|损失|结局」——事实陈述页，克制笔法
13  遗产：色素化学的奠基者 — 四分类遗产盒 + 公式框：60,000 次微量分析 + 月球环形山 Fischer（1976，与 Emil Fischer 同名纪念）
14  结尾 — 「他把血液的颜色，还原成了化学的语言。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| Fischer 同名大迷宫 | 本篇是 **Hans Fischer**（1930 化学奖）；博士导师 **Theodor Zincke**；柏林老师 **Hermann Emil Fischer**；批评 Bergius 的是 **Franz Joseph Emil Fischer**（另一人）；1973 得主是 **Ernst Otto Fischer**；Harden 导师是 **Otto Fischer**——五组名字严禁互串 |
| 博士导师冲突 | frontmatter `doctoral_advisor` 写 Hermann Emil Fischer，但正文 infobox **Doctoral advisor = Theodor Zincke**、Emil Fischer 在 **Other academic advisors**——以 infobox 为准 |
| 1930 获奖口径 | 官方措辞 "for his researches into the constitution of haemin and chlorophyll and especially for his synthesis of haemin"；**独享**——勿写共享 |
| 胆色素合成年份 | bilirubin 合成 **1942**、biliverdin 合成 **1944**（正文顺序 "synthesized them in 1942 and 1944, successively" 对应 biliverdin→bilirubin 叙述在前、合成在后）——表述以正文为准勿对调年份归属 |
| 60,000 分析 | "microanalyses of more than 60,000 chemical substance(s)"——表述为"超过 60,000 种化学物质的微量分析"，勿写成 6,000 |
| von Müller 角色 | von Müller 是"激发其兴趣的前教授与主管"，1910 邀其加入慕尼黑第二 Medical Clinic——勿与博士导师混淆 |
| 婚姻 | 1935 年娶 Wiltrud Haufe（约 50 多岁）——正文仅此，勿扩写子女 |
| 死亡表述 | 1945-03-31 复活节星期日自杀；直接原因是实验室与毕生工作毁于慕尼黑轰炸——客观陈述，**不渲染方法细节**、不写心理推断 |
| 肖像 | 本地仅 Nobel_ceremony_1930.jpg（典礼合影）——作插图可以，**主肖像须另行获取或装饰圆占位**，勿把合影裁切冒充独照 |
| 月球环形山 | Fischer 环形山（1976）纪念的是 Hans Fischer **与** Hermann Emil Fischer 两人——勿写只纪念一人 |
| 页面无载禁写 | page.md **未载**其兄弟姐妹、具体炸毁日期、纳粹时期政治立场——一律不写 |
| 引语红线 | page.md 无直接引语（"exclusively" 一词带引号仅指其专注工作）——全文用间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76604 | ✅ |
| name_zh | 汉斯·费歇尔 | ✅ |
| name_en | Hans Fischer | ✅ |
| birth_date | 1881-07-27 | ✅ |
| death_date | 1945-03-31 | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分：organic chemistry / biochemistry / porphyrin chemistry / clinical chemistry，带 rank） | ✅ |
| has_biography | false（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Theodor Zincke | 师→生（Marburg 博士导师） | infobox 明载博士导师 |
| advisor-student | Hermann Emil Fischer | 师→生（柏林第一化学研究所） | Other academic advisors；柏林时期在其所工作 |
| advisor-student | Hans von Müller | 师→生（前教授与主管） | 激发其色素研究兴趣，1910 邀其入慕尼黑第二 Medical Clinic |

**门生（Hans Fischer → 学生，源自本地 Wikipedia 正文 infobox，5 人）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Alfred E. Treibs | Hans Fischer → 学生 | infobox 明载博士生 |
| advisor-student | Werner Zerweck | Hans Fischer → 学生 | infobox 明载博士生 |
| advisor-student | Costin Nenițescu | Hans Fischer → 学生 | infobox 明载博士生 |
| advisor-student | Adolf Stachel | Hans Fischer → 学生 | infobox 明载博士生 |
| advisor-student | Heinz Gibian | Hans Fischer → 学生 | infobox 明载博士生 |

**配偶**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Wiltrud Haufe | 无向 | 1935 年结婚 |

> **禁入库名单（literature/正文提及 only）**：Heinrich Wieland（仅 1950 年悼念文章作者，正文未明载同事关系）、Otto Hönigschmid（同上，悼念文章标题中提及）。

## 8. 奖项清单

- Nobel Prize for Chemistry（1930，独享）
- Fellow of the Academy of Sciences Leopoldina（1919）
- Privy Councillor / Geheimrat（1925）
- Liebig Memorial Medal（1929）
- Honorary doctorate, Harvard University（1936）
- Davy Medal, Royal Society of London（1937）
- 月球环形山 Fischer（1976，与 Hermann Emil Fischer 共同纪念）

## 9. 机构清单

- 教育：Stuttgart 小学 → Humanistisches Gymnasium Wiesbaden（–1899）→ University of Lausanne → Marburg University（1904 化学毕业；1906 行医执照；1908 M.D.）→ LMU München（1908 申请进入）
- 任职：慕尼黑 Medical Clinic → 柏林第一化学研究所（Emil Fischer 处）→ LMU München（1911；1912 内科学讲师；1913 生理学讲师）→ Innsbruck 大学医学化学教授（1916）→ Vienna 大学（1918）→ 慕尼黑工业大学有机化学教授（1921–1945，直至去世）

## 10. 终审清单

- [ ] 生卒 1881-07-27 / 1945-03-31，享年 63，出生地 Höchst am Main、去世地慕尼黑
- [ ] 1930 独享表述准确；官方获奖理由英文原句完整呈现
- [ ] 博士导师 Theodor Zincke（infobox 为准）；von Müller 与 Emil Fischer 角色区分清楚
- [ ] 血红素 1929 合成、bilirubin 1942 / biliverdin 1944 年份准确
- [ ] 五位博士生全部入库；Wieland / Hönigschmid 不入库
- [ ] 1945 年结局客观陈述，无渲染
- [ ] 无编造引语——全文用间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Hans_Fischer/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：Nobel_ceremony_1930.jpg 仅作插图；检查主肖像获取结果（REST API / 装饰圆占位）并记录
- [ ] **国籍**：封面顶部明示德国
- [ ] **引语核对**：全文不得出现无法在 page.md 溯源的"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Frederick_Sanger_zh.tex）对齐
