# Irène Joliot-Curie（伊雷娜·约里奥-居里）立传提示词

> qid=Q7504 · 1897-09-12 – 1956-03-17 · 法国化学家/物理学家 · 20 世纪 · 诺贝尔化学奖（1935，与丈夫 Frédéric Joliot-Curie 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Irène_Joliot-Curie/`（page.md + metadata.json + page.html + images.txt）

---

## 0. 正文形式说明（参考 Frederick Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。**本地 images.txt 有真肖像**：`Irène_Joliot-Curie_Harcourt.jpg`（c. 1920s，Harcourt 摄影室标准肖像）——执行时下载 500px 用作封面与身份页头像；夫妻合影仅作插图勿作头像（与 Frédéric 篇区分）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{radiation}\enspace 镭的女儿\enspace·\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Irène Curie，婚后改姓）、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「家族传承」母题——两代同色的圆点成串，暗示居里—约里奥-居里两代放射科学家。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——人工放射性页必须写 α 轰击铝的核反应式 **²⁷Al + ⁴He → ³⁰P + n**（磷-30 天然不存在，衰变放出正电子）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Irène Joliot-Curie（出生名 Irène Curie；1926 婚后与丈夫同改复合姓 Joliot-Curie）
- **生卒**：1897-09-12 生于巴黎（法兰西第三共和国）→ 1956-03-17 逝于巴黎 Curie Hospital（急性白血病，与钋与 X 射线暴露相关），享年 58
- **国籍**：France（法国）
- **身份**：化学家、物理学家；镭研究所所长（1946）；法国政府科研国务副秘书（1936，首批三位女性政府成员之一）；CEA 六位创始委员之一（1945）
- **家庭**：Marie Curie 与 Pierre Curie 长女；妹 Ève（1904 生）；父 Pierre 1906 因马车事故早逝，由母亲抚养。1926 年娶 Frédéric Joliot（婚后同改姓）；子女 Hélène Langevin-Joliot（婚后 11 个月出生，核物理学家）与 Pierre Joliot（1932，CNRS 生物化学家）；无神论者、反战者，国葬时家属要求省去宗教与军事环节
- **教育轨迹**：巴黎天文台附近学校（1906 数学天赋显现）→ 母亲与 Langevin 等学者组建 "The Cooperative"（九位名学者子女的家庭联合教育，含中文与雕塑课，约两年）→ Collège Sévigné 高中（至 1914）→ 索邦理学院学士 → 一战中断 → 1918 完成数学与物理第二学士学位
- **博士**：1925，Doctor of Science；论文《Recherches sur les rayons α du polonium: oscillation de parcours, vitesse d'émission, pouvoir ionisant》（钋 α 射线研究）
- **导师**：Paul Langevin（infobox 博士导师）
- **研究领域**：化学、放射化学、核物理、放射生物学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **居里家长女（1897）**：生于诺奖之家；1906 丧父，Marie 独力抚养并亲自设计教育——"The Cooperative" 学者共育实验。
2. **一战战地放射师（1914–1918）**：修护理学课程随母上前线做 X 光放射师，后独自驻比利时放射站；教医生用放射定位体内弹片、自学修设备；辗转 Furnes、Ypres、Amiens 等地，获军功奖章（military medal）。
3. **母亲助手与钋博士（1918–1925）**：回索邦完成第二学位后任母亲助手，在父母创建的镭研究所教放射学；博士研究钋 α 衰变——钋即父母发现的、以波兰命名的元素；1925 获科学博士。
4. **教 Frédéric 放射化学（1924）**：博士将成时受命向年轻化学工程师 Frédéric Joliot 传授放射化学精密实验技术——这段师徒相识导向 1926 年婚姻。
5. **夫妻实验室（1928–）**：自 1928 与丈夫合力研究原子核；1932 获得母亲全部钋的支配权。
6. **与正电子、中子擦肩（1932）**：用 γ 射线做实验同时识别出正电子与中子，但未能解读其意义——发现分别由 Carl David Anderson 与 James Chadwick 完成。
7. **首次精确计算中子质量（1933）**：夫妻二人 first to calculate accurately the mass of the neutron。
8. **索尔维受挫（1933-10）**：α 轰击铝实验中只测到质子，据此提出质子→中子+正电子假说；第七届索尔维会议上遭 46 位与会科学家多数批评——随后被证明方向正确。
9. **人工放射性（1934）**：以 α 粒子轰击天然稳定同位素，造出天然不存在的放射性同位素——由硼得放射性氮、由铝得放射性磷、由镁得放射性硅（²⁷Al + ⁴He → ³⁰P + n，衰变放正电子）；使医用放射性材料快速、廉价、大量可得；同年获理学院教授职位。
10. **1935 诺贝尔化学奖**：与丈夫共享，理由为发现人工放射性——继父母之后第二对诺奖夫妻，居里家族诺奖增至 **5** 座（本篇口径），成为迄今诺奖得主最多的家族；亦是唯一诺奖母女对（Marie–Irène）与父女对（Pierre–Irène）。
11. **女性参政与 CEA（1936/1945）**：1936 人民阵线政府任科研国务副秘书（首批三位女性政府成员之一），任内协助创建 CNRS；1945 为 CEA 六委员之一（丈夫任主任）；1946 接掌母亲创建的 Institut Curie。
12. **战争岁月与家庭（1941–1944）**：1941–1943 患肺结核赴瑞士疗养，屡次冒险返法、数度被德军扣留于瑞士边境；1944 判定滞留法国过于危险，携子女赴瑞士，9 月与久无音讯的丈夫重逢；夫妻沿用 Pierre/Marie 惯例公开全部成果，但 1939-10-30 将核裂变文献封存于法国科学院（至 1949）。
13. **辐射之殇与身后（1946–1956）**：1946 年实验室钋密封胶囊爆炸受照；确诊白血病后仍工作，1955 完成 Orsay 新物理实验室规划；1956-03-17 逝于巴黎 Curie 医院；国葬省去宗教与军事环节；名字列入汉堡 *Monument to the X-ray and Radium Martyrs of All Nations*；2026 年与母亲同列拟增补埃菲尔铁塔 72 位女性 STEM 名单（巴黎市长宣布）。

## 3. 配色方案（主色 + 强调 + 分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深紫 royalpurple） | `#5B2A86` | 镭的幽紫辉光与家族传承的庄重（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（人工放射性 badgeInduced） | `#2E5A9E` | 蓝诱导放射性 / 人工同位素 |
| 分类色 2（家族传承 badgeFamily） | `#8E44AD` | 紫居里家族 / 母女诺奖对 |
| 分类色 3（核物理 badgeNuclei） | `#1B7A43` | 绿中子质量 / 正电子 / 核反应 |
| 分类色 4（公共事业 badgePublic） | `#D97B29` | 琥珀 CNRS / CEA / 女性参政 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（两代同色圆点成串，四档大小错落），呼应「家族传承」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Mirage** — Notan Nigres（路径 `music_audio/inspiring-electronic/04-5gcb94jhG1I-...Mirage (Audio).wav`）
- **风格**：空灵 / 冷冽 / 微光感
- **匹配理由**：
  - "空灵" 匹配放射性的"不可见之光"意象与战地 X 光的记忆
  - "冷冽" 匹配其克制坚忍的一生——战地、边境扣留、带病工作
  - "微光" 暗合人工放射性微弱而持久的信号——正是从微弱谱线中读出的新元素
- **时长**：执行时核对，不足 15 页 × 7 秒则循环或 ffmpeg 对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 镭的女儿 / Irène Joliot-Curie 1897–1956 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  约里奥-居里夫人的一生 — 高斯式时间线（10 节点：1897→1906→1914→1918→1925→1926→1934→1935→1936→1956）
04  早年：居里家长女与 The Cooperative (1897–1914) — 表格「时间|事件|结果」
05  战地放射师 (1914–1918) — 表格「任务|地点|结果」（Furnes/Ypres/Amiens + 军功奖章）
06  钋博士与母亲的助手 (1918–1926) — 表格「阶段|内容|结果」+ 遇见 Frédéric
07  人工放射性 (1934) — 表格「靶核|轰击|产物」+ 公式框：²⁷Al + ⁴He → ³⁰P + n
08  1935 诺贝尔化学奖 — 共享标注醒目（与 Frédéric）+ 官方理由 + 母女/父女诺奖对 + 家族 5 座
09  错过的发现与中子质量 (1932–1933) — 表格「对象|方法|结果」+ Anderson/Chadwick 擦肩注记
10  女性参政与 CEA (1936–1946) — 高斯 FFT 页式流程图（副秘书 1936 → CNRS 协创 → CEA 委员 1945 → Institut Curie 所长 1946）
11  战争岁月 (1941–1944) — 表格「时间|事件|结果」（瑞士疗养 / 边境扣留 / 文献封存科学院）
12  辐射之殇 (1946–1956) — 表格「时间|事件|结果」+ X 射线与镭殉难者纪念碑注记
13  遗产：女性与放射科学的路标 — 四分类遗产盒 + 命名遗产（Prix Joliot-Curie 1956 / 埃菲尔铁塔 72 女性 2026 提名）
14  结尾 — 「她生于镭的光里，也把光留给了后来者。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1935 诺奖理由 | 与丈夫 **共享**，理由为发现人工放射性（artificial radioactivity；page.md 亦作 discovery of artificial radioactivity）——勿写"独享"或"物理学奖" |
| 家族诺奖数 | 本篇口径 **5** 座（Irène 篇明文 five Nobel Prizes；Frédéric 篇明文 four）——两篇各忠于本人页面，勿跨篇统一；Review 时对照两篇 §5 交叉注记勿误改 |
| 唯一母女/父女对 | Marie–Irène 唯一诺奖母女对；Pierre–Irène 唯一父女对（"同一 occasion"）——限定语勿省略 |
| 博士导师 | infobox 明载 **Paul Langevin**；Marie Curie 是母亲兼研究上司（"work as her mother's assistant"），**勿写成博士导师** |
| 中子/正电子 | 1932 识别出但未解读，分属 Chadwick（中子）与 Anderson（正电子）——客观陈述，勿写"被抢" |
| 索尔维受挫 | 46 位与会科学家多数批评——史实陈述，勿添"性别歧视"归因（页面无此载述） |
| 收养 | 1948 矿工罢工期间经巴黎 Newsletters 呼吁寄养并收养两名女孩——一句带过，勿展开 |
| 死因 | 急性白血病，与钋及 X 射线暴露相关（1946 钋胶囊爆炸受照为实载事件）——医学归因按页面措辞 "possibly due to / linked to"，勿写"死于辐射事故"绝对化 |
| Ève Curie | 妹妹，作家（本页未展开其职业）——只作家庭背景 |
| Stefania Maracineanu | 仅 See also 链接（人工放射性优先权争议人物）——本页正文无载，**不写不库** |
| 埃菲尔铁塔 | 2026 年"拟增补 72 位女性"名单为提议（announced/proposed）——勿写"已刻上铁塔" |
| 引语红线 | 本页正文无直接引语白名单——中文引号内一律间接转述；诺奖演讲标题 *Artificial Production of Radioactive Elements*（1935-12-12）可引用 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q7504 | ✅（回填至既有 stub #2929） |
| name_zh | 伊雷娜·约里奥-居里 | ✅ |
| name_en | Irène Joliot-Curie | ✅（用 db_name_en 精确形式） |
| birth_date | 1897-09-12 | ✅ |
| death_date | 1956-03-17 | ✅ |
| nationality | France | ✅ |
| primary_occupation | chemist | ✅（infobox Fields：Chemistry, Physics） |
| field_of_work | radiochemistry（person_field 细分：radiochemistry / nuclear physics / radiobiology，带 rank） | ✅ |
| has_biography | false（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**家庭（红线：父子/母子关系均 page.md 明载）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Marie Curie | 母→女 | 长女；诺奖史上唯一母女对 |
| parent-child | Pierre Curie | 父→女 | 1906 早逝；唯一父女对 |
| spouse | Frédéric Joliot-Curie | 无向 | 1926 成婚，夫妻同改姓 |
| co-honored | Frédéric Joliot-Curie | 无向 | 1935 诺贝尔化学奖共同得主 |
| parent-child | Hélène Langevin-Joliot | 伊雷娜→孩子 | 长女，核物理学家 |
| parent-child | Pierre Joliot | 伊雷娜→孩子 | 次子，CNRS 生物化学家 |

**师长 / 合作者**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Paul Langevin | 师→生（博士导师） | infobox；The Cooperative 亦为 Langevin 参与 |
| advisor-student | Henriette Mathieu-Faraggi | 伊雷娜→学生 | infobox doctoral students |
| colleague | Marie Curie | 无向 | 镭研究所共事：一战放射助手、战后教放射学 |
| other | James Chadwick | 无向 | 夫妻反冲实验是 Chadwick 1932 发现中子的必要一步（工作被引用，非合作） |
| other | Carl David Anderson | 无向 | 夫妻 γ 射线实验识别出正电子但未解读，发现归 Anderson |
| other | Otto Hahn | 无向 | 伊雷娜实验室的镭核研究助益 Hahn/Strassmann 1938 铀轰击工作（间接，注明"work helped"口径） |

> **禁入库名单**（metadata.json-only 或页面无实质载述）：Lise Meitner（Frisch、Szilárd 同段提及但与 Irène 无直接关系载述）、Fritz Strassmann（同上，与 Otto Hahn 并提）、Leo Szilard（仅 Szilard 理论背景句）、Ève Curie（手足背景）、Henriette Mathieu-Faraggi 之外的 "her children" 泛称学生、Anne Hidalgo / Isabelle Vauglin（2026 提名新闻人物）、Stefania Maracineanu（仅 See also）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1935，与 Frédéric Joliot-Curie 共享）
- Matteucci Medal（1932；Frédéric 篇同年同奖）
- Barnard Gold Medal for Meritorious Service to Science（1940，与 Frédéric 共同）
- Officer of the Legion of Honour（军官级；Frédéric 为 Commander）
- Order of the Cross of Grunwald 3rd class；Polonia Restituta 指挥官星章
- 荣誉博士：Jagiellonian University（克拉科夫）、Maria Curie-Skłodowska University
- 一战军功奖章（military medal，X 光设施服务）
- 命名纪念：Prix Joliot-Curie（法国物理学会 1956 设立）；汉堡 X 射线与镭殉难者纪念碑刻名；2026 埃菲尔铁塔 72 女性 STEM 提名（与母亲同列）

## 9. 机构清单

- 教育：Collège Sévigné（至 1914）、Sorbonne / University of Paris（学士、1925 科学博士）；The Cooperative（约 1906–1908）
- 任职：Radium Institute（母亲助手、放射学讲师）→ University of Paris 理学院教授（1935 诺奖后获聘）→ 法国政府科研国务副秘书（1936）→ CEA 委员（1945）→ Institut Curie 所长（1946）→ Orsay 理学部规划（1955）
- 命名遗产：Prix Joliot-Curie（Société Française de Physique）

## 10. 终审清单

- [ ] 生卒 1897-09-12 / 1956-03-17，享年 58，出生地巴黎、去世地巴黎 Curie Hospital
- [ ] 1935 共享（Frédéric）、人工放射性理由表述准确；家族 5 座 / 母女对 / 父女对限定语准确
- [ ] 博士导师 Paul Langevin（勿写 Marie Curie）表述准确
- [ ] ²⁷Al + ⁴He → ³⁰P + n 公式与"天然不存在的磷-30"表述准确
- [ ] 1936 副秘书（首批三位女性政府成员）与 CNRS 协创、1945 CEA、1946 所长时间线准确
- [ ] 1946 钋胶囊爆炸与 1956 白血病医学归因措辞按页面（possibly/linked）
- [ ] 与 Frédéric 篇互指一致（spouse + co-honored + parent-child 三类全覆盖）；禁入库名单一致
- [ ] 本页无引语白名单——全文无引号内"原话"（除诺奖演讲标题）
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Irène_Joliot-Curie/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/Irène_Joliot-Curie_Harcourt.jpg`（c. 1920s 真肖像，下载 500px）
- [ ] **国籍**：封面顶部明示法国
- [ ] **引语核对**：全文无引语（演讲标题除外）；检查无杜撰引号
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 Frédéric 篇及化学家侧既有格式（Frederick_Sanger_zh.tex）对齐
