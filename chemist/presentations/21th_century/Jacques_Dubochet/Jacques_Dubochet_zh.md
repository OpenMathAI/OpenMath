# Jacques Dubochet（雅克·杜博歇）立传提示词

> qid=Q41585344 · 1942-06-08 –（在世）· 瑞士生物物理学家 · 21 世纪 · 诺贝尔化学奖（2017，与 Joachim Frank、Richard Henderson 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Jacques_Dubochet/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 目录已就位，取 page.md 首图 2017 年斯德哥尔摩诺奖记者会照片；下载失败用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{snowflake}\enspace 把水冻成玻璃的人\enspace·\enspace 瑞士`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「玻璃化冰晶」母题——冷色调离散圆点暗示水分子来不及结晶、被瞬间定格成玻璃态。
5. **表格语义化 + 公式框**（★ 核心版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Jacques Dubochet（中文惯称：雅克·杜博歇）
- **生卒**：1942-06-08 生于瑞士艾格勒（Aigle）→ 在世（2026-09 无卒日，年龄留白处理）
- **国籍**：Switzerland（瑞士）
- **身份**：退休瑞士生物物理学家（retired Swiss biophysicist；frontmatter description 作 "Swiss chemist"，正文口径 biophysicist，以正文为准）；洛桑大学生物物理学荣誉教授
- **家庭**：已婚，育有两名子女（页面未载妻名与子女名，禁杜撰）；有阅读障碍（dyslexia）；1970 年代与未来妻子的第二次约会是同去抗议凯泽劳格斯特核电站建设项目——环保与社会运动的终身底色
- **教育轨迹**：
  - 1962 入洛桑大学理工学院（今 EPFL）学物理，1967 获物理工程学位
  - 1969 于日内瓦大学获分子生物学证书（Certificate of Molecular Biology），开始 DNA 电子显微镜研究
  - 1973 在日内瓦大学与巴塞尔大学完成生物物理学论文（infobox 论文条目标 1974：《Contribution to the use of dark-field electron microscopy in biology》，年份口径见 §5）
- **导师**：Eduard Kellenberger（博士导师，infobox 明载）
- **博士**：1973（正文）/论文条目 1974（infobox），日内瓦大学 + 巴塞尔大学联合
- **研究领域**：生物物理学——冷冻电子显微镜（cryo-EM）、冷冻电子断层扫描、玻璃化切片冷冻电镜、结构生物学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **艾格勒少年（1942）**：生于沃州小城艾格勒；有阅读障碍却走上科学之路——"换一种方式看世界"的一生隐喻（间接转述，无原话引语）。
2. **物理 → 分子生物学的跨界（1962–1969）**：EPFL 物理工程学位打下的仪器功底 + 日内瓦分子生物学证书，恰好是"造显微镜的人去用显微镜"的复合训练。
3. **暗场电镜博士论文（1973）**：《Contribution to the use of dark-field electron microscopy in biology》——从 Day 1 就在跟"电子显微镜看生物样品"这一根本难题较劲。
4. **根本难题：水与真空不兼容**：电镜样品须置高真空，而水会沸腾蒸发；传统做法是干燥/染色——生物分子因此变形失真。让水"既液态又可入镜"是悬置数十年的死结。
5. **玻璃化（vitrification）突破（1980–1981）**：把薄水膜冷却得足够快，晶体来不及形成，水直接凝固成无定形"玻璃态"——1981 与 McDowall 发表纯水玻璃化（J. Microscopy）。
6. **冷冻含水样品电镜（1982）**：与 Lepault、Freeman、Berriman、Homo 发表冻结水与水溶液的电镜观察——生物样品第一次在接近天然含水状态下入镜。
7. **技术三件套**：玻璃化制样 + 冷冻电镜 + 冷冻电子断层扫描 + 玻璃化切片（vitreous sections）——用于成像蛋白质复合物、病毒颗粒等单个生物结构。
8. **EMBL 海德堡组长（1978–1987）**：时属西德；在此完成玻璃化方法学的主干工作。
9. **洛桑大学教授（1987–2007）**：2007 年 65 岁退休、任荣誉教授；在洛桑推动"科学家关注社会议题"的公民科学倡议（Citizen biologists）。
10. **2017 诺贝尔化学奖**：与 Joachim Frank、Richard Henderson 共享，官方理由 "for developing cryo-electron microscopy for the high-resolution structure determination of biomolecules in solution"——他贡献的是**制样环节**：把生物样品玻璃化冻进玻璃态水。
11. **2018 皇家摄影学会 Progress Medal**：与 Frank、Henderson 共同获得——"摄影或成像领域重要进展"，从成像史角度再次确认冷冻电镜的地位。
12. **自行车停车位（2017）**：被问及希望大学如何纪念诺奖时，他只要求一个自行车停车位（他 30 年几乎每天骑车去实验室）——洛桑校园至今保留 "Reserved for Jacques Dubochet" 车位。
13. **公民与社会参与**：瑞士社会民主党党员、莫尔日市政议会成员兼监督委员会席位、Grandparents for Future 气候运动成员；2021 年底以他命名的 Dubochet Center for Imaging（DCI，EPFL+UNIL+UNIGE 合建）落成，数周后即对解析新冠病毒 Omicron 变异株刺突蛋白作出关键贡献。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深绿 deepgreen） | `#1E6B52` | 玻璃化冰水的冷冽与生命结构的沉稳（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（玻璃化制样 badgeVitr） | `#2E7FA8` | 冰蓝玻璃态水膜 / 快速冷却 |
| 分类色 2（冷冻电镜 badgeCryoEM） | `#1B7A43` | 绿电子束下的含水样品 |
| 分类色 3（断层扫描 badgeTomog） | `#D97B29` | 琥珀三维重建 / 玻璃化切片 |
| 分类色 4（公民科学 badgeCitizen） | `#C0395B` | 玫瑰社会参与 / 气候运动 |
| 背景 | `#F5F8F7` | 冷调浅灰白（微绿） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），冷色调为主，呼应「来不及结晶的水分子被定格」的玻璃化意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Lonesome** — AShamaluevMusic（inspiring-electronic 系列，文件 `music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav`；不复制 wav 文件，Makefile 引用路径即可）
- **风格**：忧伤而情感深沉的电影感电子乐
- **匹配理由**：
  - "孤独的长期主义" 匹配杜博歇气质——玻璃化是几十年坐冷板凳的方法学苦功，2017 年 75 岁才等来诺奖，全批五人中获奖时最年长
  - "情感深沉" 匹配其人生底色——阅读障碍少年、反核抗议者、骑车上班的诺奖得主，纪录片式娓娓道来
  - "电影感" 匹配 15 页传记叙事的起承转合
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 把水冻成玻璃的人 / Jacques Dubochet 1942– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/领域/荣誉）
03  杜博歇的一生 — 时间线（10 节点：1942→1962→1967→1969→1973→1978→1981→1987→2017→2021）
04  早年：艾格勒到洛桑 (1942–1969) — 表格「时间|事件|结果」
05  博士：暗场电镜 (1969–1978) — 表格「时间|事件|结果」
06  根本难题：水与真空 (1950s–1980) — 表格「问题|传统做法|代价」
07  玻璃化突破 (1980–1982) — 表格「问题|方法|结果」+ 公式框：玻璃化冷却速率（晶体来不及形成）
08  EMBL 与技术三件套 (1978–1987) — 表格「技术|对象|用途」
09  洛桑岁月与公民科学 (1987–2007) — 表格「时间|事件|结果」
10  2017 诺贝尔化学奖 — 表格「三人|分工|理由」+ 公式框：官方获奖理由英文原句（三人共享同一理由）
11  自行车停车位与幽默 — 轶事页（车位照片位 + Progress Medal 2018）
12  DCI 与 Omicron (2021–) — 流程图：DCI 落成 → 数周后解析 Omicron 刺突蛋白
13  遗产：冷冻电镜改变结构生物学 — 四分类遗产盒
14  结尾 — 「让水来不及结晶，让生命来得及被看见。」（自撰收束句，非引语）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2017 三人分工 | Dubochet＝玻璃化冷冻制样、Frank＝单颗粒重建算法、Henderson＝首张膜蛋白电子密度图/推动技术极限——勿互相混淆；三人共享**同一句**官方理由 |
| 获奖理由 | 官方措辞 "for developing cryo-electron microscopy for the high-resolution structure determination of biomolecules in solution"——勿写成"发明电子显微镜"或"发明冷冻电镜"（是 develop 非 invent） |
| 身份口径 | 正文 "retired Swiss biophysicist"；frontmatter description "Swiss chemist"——**以正文 biophysicist 为准**，DB occupation 用 biophysicist |
| 博士年份 | 正文 "In 1973, he completed his thesis"；infobox 论文条目标 (1974)——正文页写 1973 并加注 infobox 口径，勿只写其一 |
| 教育三校 | EPFL（1967 物理工程学士）→ 日内瓦（1969 分子生物学证书、博士）+ 巴塞尔（博士联合）——勿写成三地各一学位 |
| 妻子与子女 | 仅 "married with two children"，**妻子与子女页面未载姓名**——禁止杜撰人名，人物关系图不出现 |
| 政党与政治 | 社会民主党党员、市政议会、气候运动为页面实载可写；但保持事实陈述、不做政治评价 |
| Progress Medal | 2018 年与 Frank、Henderson **共同**获皇家摄影学会 Progress Medal——勿写成个人奖 |
| Lennart Philipson Award | 2014 年 EMBL 颁发——在诺奖**之前**，勿写成诺奖衍生奖 |
| Gareth Griffiths 引语 | "Jacques had a vision..." 系其 EMBL 同事 Griffiths 2015 年的转述评价——标注说话人，勿当杜博歇自述 |
| 同名区分 | Richard Henderson＝生物学家/结构生物学家（本批合作者），页面上不存在其他 Henderson 干扰，但与物理学家 Arthur Henderson 等无关 |
| DCI 时间 | 2021 年 11 月底启动；Omicron 刺突蛋白解析在其后数周——时间顺序勿倒置 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q41585344 | ✅ |
| name_zh | 雅克·杜博歇 | ✅ |
| name_en | Jacques Dubochet | ✅ |
| birth_date | 1942-06-08 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | Switzerland | ✅ |
| primary_occupation | biophysicist | ✅ |
| field_of_work | structural biology（person_field 细分见下表） | ✅ |

**person_field 细分（rank 表）**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | cryo-electron microscopy | 冷冻电子显微镜 |
| 1 | structural biology | 结构生物学 |
| 2 | biophysics | 生物物理学 |
| 3 | vitrification | 玻璃化制样 |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主**（★红线：只收 page.md 正文或 infobox 明载；metadata-only 一律不入库）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Eduard Kellenberger | 师→生（博士导师） | infobox 明载；日内瓦/巴塞尔 1973 论文 |
| co-honored | Joachim Frank | 无向 | 2017 诺贝尔化学奖共同得主（另含 Henderson 共三人） |
| co-honored | Richard Henderson | 无向 | 2017 诺贝尔化学奖共同得主 |
| colleague | Gareth Griffiths | 无向 | EMBL 同事，2015 年公开回顾其玻璃化历程 |

> **禁入库名单**（页面无具名或仅 metadata 可见）：妻子（页面未载姓名）、两名子女（未具名）、Grandparents for Future 其他成员、DCI 合作机构人物（机构关系不落人）。metadata.json properties 无额外关系字段。

## 8. 奖项清单

- Nobel Prize in Chemistry（2017，与 Frank/Henderson 共享）
- Lennart Philipson Award，EMBL（2014）
- Royal Photographic Society Progress Medal（2018，与 Frank/Henderson 共同）
- honorary doctorate from the University of Strasbourg（frontmatter 载，具体年份页面无载）
- Royal Photographic Society 授奖词口径：'an important advance in the scientific or technological development of photography or imaging in the widest sense'

## 9. 机构清单

- 教育：EPFL（1962–1967，物理工程）、University of Geneva（1969 证书；博士）、University of Basel（博士联合）
- 任职：EMBL Heidelberg 组长（1978–1987）；University of Lausanne 教授（1987–2007）、荣誉教授（2007–）
- 命名机构：Dubochet Center for Imaging（DCI，2021，EPFL + UNIL + UNIGE 合建）；洛桑校园自行车专属车位

## 10. 终审清单

- [ ] 生卒 1942-06-08 / 在世留白；出生地 Aigle
- [ ] 2017 三人共享同一句官方理由；三人分工表述准确
- [ ] 博士年份 1973（正文）+ infobox 1974 双口径注记
- [ ] 身份用 biophysicist（正文口径）；妻子/子女未具名禁写
- [ ] Progress Medal 2018 三人共同；Philipson Award 2014 在诺奖前
- [ ] Griffiths 引语标注说话人；结尾句非引语
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Jacques_Dubochet/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像就位（2017 斯德哥尔摩记者会照片；失败用装饰圆）
- [ ] **国籍**：封面顶部明示瑞士
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（官方获奖理由、Griffiths 评价、Progress Medal 授奖词）；无原文一律间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金参照）对齐
