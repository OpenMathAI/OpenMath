# Fritz Haber（弗里茨·哈伯）立传提示词

> qid=Q57075 · 1868-12-09 – 1934-01-29 · 德国化学家 · 20 世纪 · 诺贝尔化学奖（1918，独享；1919 年领取）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Fritz_Haber/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页 + 气泡背景。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 就位后使用；无真实肖像则用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 从空气中制造面包的人\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）——灰蓝圆点暗示「空气中的氮 / 历史的阴影」双重母题。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Fritz Jakob Haber（中文惯称：弗里茨·哈伯）
- **生卒**：1868-12-09 生于普鲁士王国布雷斯劳（Breslau，今波兰弗罗茨瓦夫）→ 1934-01-29 逝于瑞士巴塞尔一间旅馆（心力衰竭，赴巴勒斯坦途中学），享年 65
- **国籍**：Germany（生于普鲁士王国布雷斯劳；犹太家庭出身，1892–1894 在耶拿期间皈依路德宗）
- **身份**：化学家（哈伯法合成氨发明者；化学战组织者——双重身份必须并置）
- **家庭**：父 Siegfried（染料/颜料/药材商人）与母 Paula 是表亲结婚；母亲在 Fritz 出生三周后去世，父子关系长期疏离；父再娶 Hedwig Hamburger，育三女（Else/Helene/Frieda）。1901-08-03 娶 Clara Immerwahr（布雷斯劳大学首位化学女博士），子 Hermann（1902）；1915-05-02 Clara 在花园自杀身亡。1917-10-25 再娶 Charlotte Nathan，育 Eva-Charlotte 与 Ludwig Fritz（1921–2004，英国经济史家，著 *The Poisonous Cloud*），1927-12-06 离婚
- **教育轨迹**：柏林腓特烈·威廉大学（1886–87 冬季学期，师从 A. W. Hofmann）→ 海德堡大学（1887 夏季学期，师从 Robert Bunsen）→ 夏洛滕堡高等技术学校（今 TU Berlin，师从 Carl Liebermann）→ 1891-05 以 *cum laude* 获柏林大学博士学位（夏洛滕堡当时无博士学位授予权）→ 苏黎世联邦理工一学期（师从 Georg Lunge）
- **导师**：Carl Liebermann（博士课题实际指派者，piperonal 衍生物论文）；Robert Bunsen（海德堡从学；frontmatter 列为博士导师）
- **博士**：1891，*Ueber einige Derivate des Piperonals*（柏林大学授位）
- **研究领域**：物理化学——化学热力学、电化学、气体反应、合成氨、表面科学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **布雷斯劳商人家庭（1868）**：犹太同化家庭；父希望他继承染料生意，他却执意学化学；随父跑业务期间经历霍乱疫情囤货失败，父亲断言他"不属于商界"。
2. **求学三城（1886–1891）**：柏林—海德堡—夏洛滕堡；1891 年以 piperonal 衍生物论文获柏林大学博士。
3. **耶拿与改宗（1892–1894）**：在耶拿任 Ludwig Knorr 的独立助手；期间由犹太教皈依路德宗。
4. **卡尔斯鲁厄起飞（1894–1911）**：经 Carl Engler 推荐入 Hans Bunte 门下任助教；烃类热分解的定量研究成为特许任教资格（habilitation）论文；1898 年升 Extraordinarius。
5. **技术电化学奠基（1898）**：专著 *Grundriss der technischen Elektrochemie* 引起广泛注意；对不可逆/可逆电化学还原的研究被视为该领域经典；1906 年接任卡尔斯鲁厄物理化学讲席教授。
6. **哈伯法（1909）**：与助手 Robert Le Rossignol 在 500°C、2900 psi 与催化剂条件下首次实现由氮气与氢气催化合成氨——源自 Le Châtelier 原理的逆向推导。
7. **BASF 工业化（1913）**：与 BASF 的 Carl Bosch 合作放大到工业规模，改用更精炼的铁催化剂——Haber–Bosch 法成为工业化学里程碑；据估算全球每年粮食产量的三分之一依赖该法，支撑近一半世界人口。
8. **1918 诺贝尔化学奖**：表彰合成氨（1919 年实际领取）；获奖演说引语："It may be that this solution is not the final one. Nitrogen bacteria teach us that Nature... still understands and utilizes methods which we do not as yet know how to imitate."
9. **一战化学战（1914–1915）**：任战争部化学处处长（上尉军衔），组织逾 150 名科学家与 1300 名技术人员；1915-04-22 伊普尔第二次战役亲临氯气云释放——"化学战之父"；与法国诺奖得主 Victor Grignard 形成化学家的战争对阵；Franck、Hertz、Hahn 曾在其毒气部队服役。
10. **哈伯规则与辩护（一战）**：低浓度长时间与高浓度短时间暴露等效的剂量-时间关系（Haber's rule）；为毒气战辩护"死亡就是死亡"——需与 Einstein 等人的批评并置。
11. **Clara 之死（1915-05-02）**：伊普尔氯气战后 10 天，妻子 Clara 在花园自杀身亡——自杀原因存推测（部分观点认为与其毒气工作有关），行文必须克制、注明属推测。
12. **魏玛时期（1919–1933）**：任威廉皇帝物理化学与电化学研究所所长（柏林 Dahlem，1911–1933）；海水提金研究（结论：浓度远低于早期报告，不经济）；管理日本"星基金"资助 Willstätter、Planck、Hahn、Szilard 等；1920 年代其研究所开发了杀虫剂 Zyklon A——注意：Zyklon B 是后来在他**无直接参与**的情况下由其成果发展而来（page.md 明载口径）。
13. **辞职、流亡与客死（1933–1934）**：1933-04-30 致函 Rust 与 Planck 辞去一切职务（"作为改宗犹太人我或许可依法留任，但我不再愿意"）；短暂流亡剑桥（Rutherford 拒绝与他握手）；接受 Weizmann 邀请出任雷霍沃特 Sieff 研究所所长，1934-01-29 途中死于巴塞尔；Einstein 悼词："Haber's life was the tragedy of the German Jew – the tragedy of unrequited love"。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（靛蓝 indigo） | `#283593` | 空气与工业的冷峻蓝（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 麦穗金黄（公式框边线、字段标签） |
| 分类色 1（合成氨 badgeAmmonia） | `#1B7A43` | 绿哈伯法 / 化肥养活世界 |
| 分类色 2（化学战 badgeGas） | `#616161` | 灰氯气云 / 战壕——刻意用哑色 |
| 分类色 3（电化学 badgeElectro） | `#D97B29` | 琥珀电化学 / 热力学经典 |
| 分类色 4（流亡 badgeExile） | `#8C1F28` | 暗红 1933 辞职 / 巴塞尔终点 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落）——上部偏绿、下部渐灰，暗示「面包与毒气」的一体两面。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Expedition** — Alex-Productions（文件 `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`，勿复制 wav）
- **风格**：推进感 / 命运感 / 大开大合
- **匹配理由**：
  - "推进感" 匹配哈伯法的技术远征——从实验室克级到养活半个世界的工业奇迹
  - "命运感" 匹配其一生双重性的戏剧张力——诺奖与化学战、荣耀与放逐
  - "大开大合" 匹配传记叙事的跨度——布雷斯劳→卡尔斯鲁厄→柏林→巴塞尔
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 从空气中制造面包的人 / Fritz Haber 1868–1934 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  哈伯的一生 — Sanger 式时间线（10 节点：1868→1891→1894→1898→1909→1913→1915→1918→1933→1934）
04  早年：布雷斯劳商人之家 (1868–1886) — 表格「时间|事件|结果」
05  求学与改宗 (1886–1894) — 表格「城市|师从|收获」+ 公式框：博士论文 piperonal 衍生物
06  卡尔斯鲁厄：技术电化学 (1894–1911) — 表格「对象|方法|结果」
07  哈伯法 (1909–1913) — 表格「问题|条件|结果」+ 公式框：N₂ + 3H₂ ⇌ 2NH₃（500°C · 2900 psi · 催化剂）
08  BASF 工业化与养活世界 — 表格「阶段|人物|规模」+ 1/3 粮食 · 近半人口
09  1918 诺贝尔化学奖 — 表格「理由|领取|演说」（1919 领取；演说引语）
10  一战：化学战与哈伯规则 (1914–1918) — 表格「组织|事件|辩护」（伊普尔 1915-04-22；克制呈现）
11  Clara Immerwahr (1901–1915) — 表格「人物|成就|结局」（克制、注明死因属推测）
12  魏玛时期： Dahlem 与海水提金 (1919–1933) — 表格「方向|内容|结论」+ Zyklon A 口径（无直接参与 B）
13  1933 辞职与流亡 (1933–1934) — 表格「事件|地点|终点」+ Einstein 悼词
14  结尾 — 「他喂饱了世界，也玷污了空气。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 诺奖年份 | **1918 年奖，1919 年实际领取**——两个年份勿混；**独享** |
| 获奖理由 | page.md 口径："for his invention of the Haber process"（发明哈伯法合成氨）；演说引语仅用 page.md 明载那句（Nitrogen bacteria...）——勿杜撰其他原话 |
| 博士导师 | 实际课题指派者为 **Carl Liebermann**（夏洛滕堡，柏林大学授位）；Bunsen 是海德堡从学一学期（frontmatter 列为博士导师）——两人并列并注明差异 |
| 化学战表述 | 客观陈述史实（伊普尔日期、编制规模、"化学战之父"称呼），**不渲染细节**；其团队研制的毒气造成的伤亡数字仅用 page.md 明载的 67,000 casualties 一处 |
| Zyklon 口径 | 研究所开发的是 **Zyklon A**（杀虫熏蒸剂）；**Zyklon B** 是后来在他**无直接参与**（without his direct involvement）下发展而来并用于大屠杀——口径必须严格照此，勿写"他发明了 Zyklon B" |
| MDMA | page.md 明载"他首次合成 MDMA"的说法**不正确**（实为 Merck 的 Anton Köllisch 1912）——立传中不要沿用 |
| Clara 之死 | 1915-05-02 自杀身亡；**死因至今属推测**（"The reasons for her suicide remain the subject of speculation"），与毒气工作的关联是"有人认为"——必须克制并标注推测属性 |
| Rutherford 拒握手 | 剑桥流亡期间 Rutherford 拒绝握手——明载可写，但与 Hartley/Pope/Donnan 帮助他离德并置呈现 |
| 同名区分 | 与血亲中的"Koppel"无亲属关系（Koppel was not actually related to Haber）；儿子 Hermann（与 Clara 所生）与 Ludwig Fritz（与 Charlotte 所生）勿混 |
| 战后秘密武器 | 1919–1923 与 Stoltzenberg 秘密化学武器合作、协助西班牙与俄国——明载，但建议一笔带过、不展开 |
| 政治敏感 | 全篇不出现当代政治类比；引语仅限 page.md 明载英文原句（获奖演说、"during peace time a scientist belongs to the world..."、Einstein 悼词、umbrella 对话） |
| 品牌口径 | 结尾页品牌写 `OpenMathAI`；引号半角 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q57075 | ✅ |
| name_zh | 弗里茨·哈伯 | ✅ |
| name_en | Fritz Haber（库内既有记录 id=2152，精确复用回填 QID） | ✅ |
| birth_date | 1868-12-09 | ✅ |
| death_date | 1934-01-29 | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | physical chemistry（person_field 细分见下表） | ✅ |

**person_field 细分（rank 表）**：

| name_en | rank | name_zh |
|---|---|---|
| physical chemistry | 0 | 物理化学 |
| chemical thermodynamics | 1 | 化学热力学 |
| electrochemistry | 2 | 电化学 |
| industrial chemistry | 3 | 工业化学 |

## 7. 社会关系入库清单

**师长 / 同事 / 对手 / 家人**（★红线：只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Carl Liebermann | 师→生（博士课题指派） | 夏洛滕堡从学；piperonal 论文，柏林大学 1891 授位 |
| advisor-student | Robert Bunsen | 师→生（海德堡从学） | 1887 夏季学期；frontmatter 列为博士导师 |
| colleague | Carl Bosch | 无向 | 与 BASF 合作将哈伯法工业化；1918 同获柏林 Bunsen Medal |
| colleague | Robert Le Rossignol | 无向 | 助手；1909 共同实现合成氨 |
| colleague | Max Born | 无向 | 共同提出 Born–Haber 循环（晶格能） |
| colleague | Albert Einstein | 无向 | 多年挚友与批评者；1933 年后仍相交，致悼词 |
| colleague | Otto Hahn | 无向 | 一战在哈伯毒气部队服役；星基金资助对象 |
| colleague | James Franck | 无向 | 未来诺奖得主，一战在哈伯毒气部队服役 |
| colleague | Gustav Hertz | 无向 | 未来诺奖得主，一战在哈伯毒气部队服役 |
| colleague | Hans Bunte | 无向 | 卡尔斯鲁厄东家；建议其研究烃类热分解（habilitation） |
| competitor | Victor Grignard | 无向 | 一战"化学家的战争"对阵双方（法方诺奖化学家） |
| other | Chaim Weizmann | 无向 | 1933 邀其出任雷霍沃特 Sieff 研究所所长 |
| spouse | Clara Immerwahr | 无向 | 1901 结婚；布雷斯劳大学首位化学女博士；1915 自杀身亡 |
| spouse | Charlotte Nathan | 无向 | 1917 结婚，1927 离婚；育 Eva-Charlotte 与 Ludwig Fritz |

> 禁入库名单（metadata-only / 噪声防入）：Ludwig Knorr（耶拿独立助手期，非学位师承）、Georg Lunge（苏黎世一学期从学）、Hans Luggin（电化学讲座）、Georg Bredig（同行交流）、Joseph Joshua Weiss（剑桥流亡助手，仅一句提及）、Hugo Stoltzenberg（战后秘密合作，敏感且噪声）、Harold Hartley / William Pope / Frederick Donnan（帮助离德的英方人士）、Otto Peterson / Friedrich Kerschbaum（毒气部队指挥序列）、Bernhard Rust / Wilhelm Solf / Hoshi Hajime（行政与资助方）。均 page.md 仅一句提及或非社会关系，不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1918 奖，1919 领取，独享）
- Iron Cross（1915）
- Bunsen Medal of the Bunsen Society of Berlin（1918，与 Carl Bosch 同获）
- Rumford Medal（1932，American Academy of Arts and Sciences）
- Wilhelm Exner Medal（1929）
- Foreign Associate of the National Academy of Sciences, USA（1932）
- Foreign Honorary Member, American Academy of Arts and Sciences（1914）
- Honorary Member：Société Chimique de France（1931）、Chemical Society of England（1931）、Society of Chemical Industry, London（1931）、USSR Academy of Sciences（1932）
- German Chemical Society President（1923）；IUPAC Board of Directors（1929–1933，Vice-President 1931）
- Harnack Medal；Liebig Medal；Goethe-Medaille für Kunst und Wissenschaft

## 9. 机构清单

- 教育：Friedrich Wilhelm University Berlin（1886–87、1891 PhD）→ Heidelberg University（1887 夏）→ Technische Hochschule Charlottenburg（今 TU Berlin）→ ETH Zürich（一学期）
- 任职：Jena（Knorr 组独立助手 1892–1894）→ Karlsruhe 大学（助教 1894–；Privatdozent 1896；Extraordinarius 1898；物理化学讲席教授 1906–1911）→ 威廉皇帝物理化学与电化学研究所所长（柏林 Dahlem，1911–1933；1953 年更名 Fritz Haber Institute）→ 剑桥流亡（1933–34）→ Sieff Research Institute（雷霍沃特，受邀未到任）
- 纪念：Fritz Haber Institute of the MPG（1953 更名）；Fritz Haber Library（Sieff/Weizmann，1936 建立藏其私人图书馆）；Fritz Haber Research Center for Molecular Dynamics（耶路撒冷希伯来大学，1981）

## 10. 终审清单

- [ ] 生卒 1868-12-09 / 1934-01-29，享年 65，出生地布雷斯劳、去世地巴塞尔
- [ ] 1918 奖 / 1919 领取；独享；获奖理由与演说引语口径正确
- [ ] 博士导师 Liebermann + Bunsen 双列并注明口径差异
- [ ] 哈伯法条件（500°C / 2900 psi / 催化剂）与 BASF 工业化（铁催化剂）表述准确
- [ ] 化学战、Zyklon A/B、MDMA 辟谣、Clara 死因推测四项敏感口径全部正确
- [ ] 引语仅限 page.md 明载英文原句（获奖演说 / Einstein 悼词 / "during peace time..." 等）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Fritz_Haber/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像就位或装饰圆占位
- [ ] **国籍**：封面顶部明示德国
- [ ] **引语核对**：引语必须在 page.md 原文找到，否则改间接转述
- [ ] **敏感项**：化学战 / Zyklon / Clara 三处逐字复核 §5 口径
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox<10pt、hbox<50pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger）对齐

---

> **名单状态**：本提示词由 chem-batch-02 批次生成；`chemist/generate_20th_century_list.py` 由主控统一收尾，勿改动。
