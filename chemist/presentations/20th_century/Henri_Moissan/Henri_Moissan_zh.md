# Henri Moissan（亨利·莫瓦桑）立传提示词

> qid=Q102804 · 1852-09-28 – 1907-02-20 · 法国化学家 · 1906 年诺贝尔化学奖
> 诺奖官方理由（总名单措辞）：表彰他研究并分离出元素氟所作出的巨大贡献，以及他为科学服务而采用以他名字命名的电炉
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Henri_Moissan/`（page.md + metadata.json + images.txt）
> 版式基准：**参考数学家 Carl Friedrich Gauss（Q6722）的立传提示词与 Beamer 格式**——表格语义化 tabularx + 公式展示框 + 时间线页 + 身份信息页，是本次立传的核心版式语言。

---

## 0. 正文形式说明（参考数学家高斯立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（images.txt **无肖像 URL**，仅有签名图、氟气颜色对比图、电炉造钻场景图——执行阶段按 §11 Review-1 指引回退下载）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{fire}\enspace 驯服氟的人\enspace·\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色（氟绿）+ 强调色（诺贝尔金）+ 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「炉火 / 晶体」母题——光斑圆点如电弧炉的火色与碳化硅晶面的闪光。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（电解方程、SiC、SF₆ 等）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Ferdinand Frédéric Henri Moissan（中文惯称：亨利·莫瓦桑）
- **生卒**：1852-09-28 生于巴黎 → 1907-02-20 逝于巴黎，享年 54
- **国籍**：France（法国）
- **身份**：化学家、药剂师、大学教师（chemist / pharmacist / pharmacologist / university teacher；1906 年诺贝尔化学奖得主）
- **家庭**：父 Francis Ferdinand Moissan 为东方铁路公司小职员；母 Joséphine Améraldine（娘家姓 Mitel）为缝纫女工。1882 年娶 Léonie Lugan（Marie Léonie Lugan Moissan），1885 年得子 Louis Ferdinand Henri
- **教育轨迹**：
  - 1864 随家迁 Meaux，入当地学校；做过钟表匠学徒
  - 1870 因普法战争随家回巴黎；未取得进入大学所需的 grade universitaire；服一年兵役
  - 入 École Supérieure de Pharmacie de Paris（巴黎高等药剂学校）；1874 通过 baccalauréat（此前一次未过）；1879 取得一级药剂师资格；1880 在此获博士学位
  - 实验室出身：Edmond Frémy 实验室（国立自然史博物馆）→ Pierre Paul Dehérain 实验室（École Pratique des Hautes Études）
- **导师**：博士导师一职存在来源冲突——page.md infobox 作 Henri Debray，metadata 作 Pierre Paul Déhérain；正文叙事中 Dehérain 是其实验室导师并劝其走学术道路（详见 §5）
- **博士论文**：*Sur les oxydes métalliques de la famille du fer*（1880；正文另述其 Ph.D. 工作为氰及其生成氰化物/氰 ure 的反应）
- **研究领域**：化学（无机化学）——氟的分离与氟化学、电弧炉与高温化学、碳化物/硼化物、矿物学（碳化硅）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **钟表匠学徒（1864–1870）**：铁路小职员与缝纫女工之子，在 Meaux 做钟表匠学徒——精密手艺成为日后玻璃真空系统与电极工艺的伏笔。
2. **无大学文凭的学徒（1870–1874）**：普法战争中断学业，没有 grade universitaire 进不了大学；从药剂学徒起步，1874 年第二次尝试才通过 baccalauréat。
3. **一次砷中毒急救（1872）**：在巴黎药房工作时救活一名砷中毒者——由此决心投身化学，先后进入 Frémy、Dehérain 的实验室。
4. **首篇论文（1874）**：与 Dehérain 合发植物二氧化碳与氧代谢论文；随后转向无机化学，发火铁（pyrophoric iron）研究获 Deville 与 Debray 两大法国无机化学家赏识。
5. **氟的世纪难题（1880s 之前）**：元素氟早已为人所知，但历代分离尝试全部失败，有实验者丧命——莫瓦桑接手的是化学史上最危险的元素之一。
6. **借来的实验室（1880s）**：自己没有实验室，借 Charles Friedel 的场地，用 90 个 Bunsen 电池的强电池组电解熔融三氯化砷——观察到气体却被三氯化砷重新吸收，功亏一篑。
7. **1886-06-26 首次分离氟**：电解 KHF₂ 溶于液态 HF 的溶液（HF 不导电，故必须加 KHF₂），铂-铱电极、铂制装置、冷至 −50 °C——阴极氢与阳极氟完全分开；此法至今仍是工业制氟的标准方法。
8. **科学院验证风波（1886）**：法兰西科学院派 Berthelot、Debray、Frémy 三人验证，首次竟无法复现——原因是本次 HF 中缺少此前实验里痕量的氟化钾；解决并多次演示成功后获一万法郎奖金。
9. **氟化学大家族**：此后专注氟的化学表征，发现大量氟化合物——1901 年与 Paul Lebeau 共同发现六氟化硫 SF₆。
10. **电弧炉与高温化学**：发展电弧炉，打开新化合物制备之路——合成多种元素的硼化物与碳化物；碳化钙的合成为乙炔化学铺路。
11. **人造金刚石的尝试**：试图用压力使常见形态的碳转变为金刚石——"尝试"是 page.md 的原文定性（见 §5 红线）。
12. **moissanite（1893–1905）**：研究亚利桑那 Meteor Crater（Canyon Diablo 峡谷）陨石碎片，发现微量新矿物，判定为碳化硅；1905 年该矿物以他命名 moissanite。
13. **荣誉与骤逝（1903–1907）**：1903 年当选国际原子量委员会成员（原始成员，任职至去世）；发表逾三百篇论文；1906 年获诺贝尔化学奖——从斯德哥尔摩领奖归来不久，1907-02-20 在巴黎骤逝，死因定为急性阑尾炎，另有推测认为长期氟与一氧化碳暴露亦有影响。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深氟绿 fluorteal） | `#145C54` | 氟气淡黄绿之深调——毕生母题（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（氟化学 badgeFluorine） | `#1B7A43` | 氟绿 1886 分离 / SF₆ |
| 分类色 2（电炉与高温化学 badgeFurnace） | `#B03A2E` | 炉火红电弧炉 / 碳化物 / 硼化物 |
| 分类色 3（矿物与晶体 badgeMineral） | `#4C5FD5` | 晶蓝moissanite / 陨石 / 金刚石尝试 |
| 分类色 4（药剂师与荣誉 badgePharma） | `#7D5BA6` | 紫药剂师出身 / 原子量委员会 / 荣誉序列 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「炉火 / 晶体」——炉光圆斑与晶体刻面。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Through the Darkness** — Audiomachine（Inspiring Electronic 合辑）
- **风格**：史诗 / 黑暗中推进 / 突破前夕
- **匹配理由**：
  - "黑暗中推进" 匹配氟分离的本质——历代化学家为氟丧命、所有尝试皆失败，莫瓦桑在借来的实验室里用 90 个电池反复试错，直至 1886-06-26 的黑暗尽头
  - "史诗" 匹配科学验证的戏剧性——科学院三人验证团到场却无法复现、痕量氟化钾之谜、一万法郎奖金，一幕完整的攻坚剧
  - 收束于骤逝的悲怆——领奖归来数周即离世，黑暗与光明在一部传记里同时收尾
- **时长**：3:07（187 秒）> 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐
- **注意**：wav 复制在执行立传阶段进行（`music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav`），本阶段不复制任何音频文件

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 驯服氟的人 / Henri Moissan 1852–1907 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  莫瓦桑的一生 — 高斯式时间线（10 节点：1852→1864→1872→1880→1886→1892→1893→1900→1906→1907）
04  早年：钟表匠学徒与药剂学徒 (1852–1874) — 表格「时间|事件|结果」
05  从药房急救到实验室 (1872–1880) — 表格「时间|事件|结果」（Frémy → Dehérain → 博士）
06  氟：世纪难题 (1880s) — 表格「问题|方法|结果」（历代失败 / 三氯化砷电解 / 90 电池）
07  1886-06-26 首次分离氟 — 表格「问题|方法|结果」+ 公式框：KHF2 溶于液态 HF 电解 · 铂-铱电极 · −50 °C
08  科学院验证风波 — 表格「事件|原因|结果」+ 公式框：痕量 KF 之谜 · 一万法郎
09  氟化学大家族 (1886–1907) — 表格「问题|方法|结果」+ 公式框：SF6（与 Lebeau，1901）
10  电弧炉与高温化学 (1892–) — 表格「问题|方法|结果」+ 公式框：碳化物 / 硼化物 / CaC2 → 乙炔化学
11  金刚石尝试与 moissanite (1893–1905) — 表格「问题|方法|结果」+ 公式框：SiC · Canyon Diablo 陨石
12  荣誉与学术任职 — 高斯式「类别|代表|意义」表格（1896 戴维 / 1898 Cresson / 1906 诺贝尔 / 荣誉军团三级 / 原子量委员会）
13  遗产：标准方法与以他命名的矿物 — 四分类遗产盒 + 公式框：工业制氟标准方法 · moissanite · 300+ 论文
14  结尾 — 金句（须与 page.md 事实相容的原创概括，不杜撰引语）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1906 诺奖理由 | 官方措辞（总名单）「表彰他研究并分离出元素氟所作出的巨大贡献，以及他为科学服务而采用以他名字命名的电炉」；1906 **独享**，无共享者；page.md intro 英文为 "for his work in isolating fluorine from its compounds"，电炉部分在 intro 另句——中文理由以总名单为准，勿只写氟 |
| 1 票优势击败门捷列夫 | **page.md 脚注 1 明载** "He defeated Dmitri Mendeleev of Russia by a margin of just one vote"——有载可用，但属脚注单源表述：正文用小字注/正文句呈现，**勿做成标题级断言** |
| 导师冲突（重要） | page.md infobox：doctoral advisor = **Henri Debray**；metadata.json：doctoral_advisor = **Pierre Paul Déhérain**；正文叙事：Dehérain 实验室出身、劝其走学术道路、1874 合发首篇论文，Debray 则是赏识其发火铁研究的无机化学家兼验证团成员。**以 page.md 为准则应从 infobox 作 Debray**，但两处矛盾须在 Beamer 与入库时以 note 标明"来源冲突" |
| 电解质细节 | 电解的是 **KHF₂（potassium hydrogen difluoride）溶于液态 HF 的溶液**——因为 HF 不导电必须加 KHF₂；勿写成"电解熔融 HF""电解氟化钾"。电极铂-铱、装置冷至 −50 °C |
| 三氯化砷不算成功 | 借 Friedel 实验室、90 个 Bunsen 电池电解熔融三氯化砷观察到的气体被**重新吸收**——是观察不是分离；勿写成"曾在三氯化砷中分离出氟" |
| 验证风波因果 | 1886-06-26 首次成功在先；科学院验证团（Berthelot/Debray/Frémy）到场无法复现，原因是本次 HF **缺少此前实验中痕量的氟化钾**——勿把"验证失败"写成"方法错误" |
| 人造金刚石 | page.md 定性为 "attempted to use pressure to produce synthetic diamonds"——是**尝试**，勿写"成功合成人造金刚石"；插图 `Henri_Moissan_making_diamonds.jpg` 图注为"用他发明的电炉尝试造金刚石"，勿写成"成功造钻" |
| moissanite | 1893 年在 Meteor Crater（Canyon Diablo 峡谷，亚利桑那）**陨石碎片**中发现微量新矿物，判定为碳化硅；1905 年以他命名——勿写"他合成了 moissanite"、勿与金刚石尝试混为一谈 |
| 去世表述 | 1907-02-20 逝于巴黎，享年 54，**从斯德哥尔摩领奖归来不久**；死因为急性阑尾炎，另有"氟与 CO 长期暴露亦有影响"是 page.md 原文的 speculation——必须写"有推测认为"，勿写成定论 |
| "1907 年获奖后不久去世" | 诺奖是 **1906 年度**（1906-12 在斯德哥尔摩领奖），1907-02 去世——"获奖后不久去世"表述须精确到月，勿写"1907 年获奖" |
| 任职时间线 | 药学院：1886 年前升到毒理学教授；1899 年任无机化学讲席；1900 年接替 Louis Joseph Troost 出任**索邦**无机化学教授——1899（药学院）与 1900（索邦）勿混 |
| 荣誉军团 | metadata 载 Knight / Officer / Commander 三级并存、正文作 commandeur——年份皆无载，勿编年份 |
| 奖项年份 | Davy Medal **1896**、Elliott Cresson Medal **1898**（infobox 有载）；Hofmann Medal、Prix Lucaze **无年份**——勿编；"first French Nobel prize winner in chemistry" 仅见于参考文献标题（Viel 1999），正文无载，**禁写** |
| 外籍会员表述 | 正文作 "elected fellow of the Royal Society"，metadata 作 Foreign Member of the Royal Society——按正文写"当选皇家学会会士"并 note 差异 |
| 学生仅两人 | Paul Lebeau、Maurice Meslans（infobox 与 metadata 一致）；SF₆ 是 1901 年与 Lebeau 共同发现——勿扩写学生名单 |
| 引语纪律 | page.md 无任何 Moissan 原话引语——**禁止杜撰"莫瓦桑名言"**，全部间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q102804 | ✅ |
| name_zh | 亨利·莫瓦桑 | ✅（与总名单一致） |
| name_en | Henri Moissan | ✅ |
| birth_date | 1852-09-28 | ✅ |
| death_date | 1907-02-20 | ✅ |
| nationality | France | ✅ |
| primary_occupation | chemist（兼 pharmacist / pharmacologist / university teacher） | ✅ |
| field_of_work | chemistry（person_field 细分建议：fluorine chemistry / electric arc furnace / high-temperature chemistry / silicon carbide，带 rank） | ✅ |
| has_biography | 执行立传并入库后置 1 | 🔲 |

## 7. 社会关系入库清单

**师长 / 同事 / 前任 / 竞争者**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Pierre Paul Dehérain | 师→生（实验室导师） | 劝其走学术道路；1874 合发首篇论文——注意 infobox 导师作 Debray 的来源冲突 |
| advisor-student | Henri Debray | 师→生（infobox 所载博士导师） | 亦为 1886 氟验证团成员；入库时 note 冲突 |
| colleague | Edmond Frémy | 无向 | 最早实验室导师（自然史博物馆）；后为科学院验证团成员 |
| colleague | Charles Friedel | 无向 | 1880s 氟攻关时借用其实验室 |
| colleague | Marcellin Berthelot | 无向 | 1886 法兰西科学院验证团成员 |
| other | Henri Étienne Sainte-Claire Deville | 无向 | 与 Debray 同为赏识其发火铁研究的法国无机化学家 |
| other | Louis Joseph Troost | 无向 | 1900 年莫瓦桑接替其索邦无机化学讲席 |
| competitor | Dmitri Mendeleev | 无向 | page.md 脚注：1906 诺奖以一票之差胜出（单源脚注，note 注明） |

**门生（Moissan → 学生）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Paul Lebeau | Moissan → 学生 | 1901 共同发现六氟化硫 SF₆ |
| advisor-student | Maurice Meslans | Moissan → 学生 | infobox 与 metadata 一致 |

> 正文（page.md）无载的关系不虚构任何合作细节；Mendeleev 一票之差仅按脚注入库并注明来源层级。

## 8. 奖项清单

- Nobel Prize in Chemistry（1906，独享）
- Davy Medal（1896）
- Elliott Cresson Medal（1898）
- Prix Lucaze（年份无载）
- Hofmann Medal / August Wilhelm von Hofmann Medal（年份无载）
- Légion d'honneur：Knight、Officer、Commander（commandeur）（三级并存，年份无载）
- Fellow of the Royal Society（正文表述；metadata 作 Foreign Member——note 差异）
- Fellow of the Chemical Society of London
- Honorary member of the Manchester Literary and Philosophical Society（1892）
- Honorary member of the Physics Association (Frankfurt am Main)（仅 metadata）
- International Atomic Weights Committee 成员（1903 当选，原始成员，任职至去世——委员会身份而非奖项，Beamer 归荣誉/任职均可）
- 一万法郎奖金（法兰西科学院，1886 氟验证成功后——奖金非奖章）

## 9. 机构清单

- 教育：Meaux 地方学校（1864–，其间钟表匠学徒）；École Supérieure de Pharmacie de Paris（一级药剂师 1879、博士 1880）；École Pratique des Hautes Études（Dehérain 实验室）；早期 Frémy 实验室（国立自然史博物馆）
- 任职：巴黎高等药剂学校（Assistant Lecturer → Senior Demonstrator → 1886 前升毒理学教授；1899 任无机化学讲席）；Sorbonne / University of Paris 无机化学教授（1900–，接替 Troost）
- 命名矿物：moissanite（碳化硅，1905 年以其名命名）

## 10. 终审清单

- [ ] 生卒 1852-09-28 / 1907-02-20，享年 54，出生地与去世地均为巴黎
- [ ] 1906 诺奖独享，理由中文措辞与总名单一致（氟 + 电炉两部分齐全）
- [ ] 1886-06-26 首次分离氟日期精确；电解质表述为 KHF₂ 溶于液态 HF
- [ ] 验证风波因果正确（痕量 KF 缺失）；一万法郎奖金归属正确
- [ ] 人造金刚石写"尝试"；moissanite 写"陨石中发现、1905 命名"
- [ ] 去世死因：急性阑尾炎为定论，氟/CO 暴露标"有推测认为"
- [ ] 导师 Dehérain/Debray 冲突已在 Beamer 与入库 note 中标明
- [ ] 一票之差击败 Mendeleev 以小字注呈现（脚注单源）
- [ ] 1899（药学院）/1900（索邦）任职时间线不混
- [ ] 引语全部可在本地 Wikipedia 原文找到（预计为零——全部间接转述）
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Henri_Moissan/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：images.txt **无肖像 URL**（仅签名图、氟气颜色对比图 `Moissan_color_images.jpg`、电炉造钻场景图 `Henri_Moissan_making_diamonds.jpg`、站点 logo）——按序回退：① Wikipedia REST API `page/summary` 查 infobox 原图名后用 Commons Special:FilePath 下载（候选文件名如 "Henri Moissan 1906.jpg"、"Moissan.jpg"，逐个试）；② Commons Category "Henri Moissan" 找肖像；③ 全部 404 则装饰圆占位（造钻场景图可作 04/11 页插图而非肖像）
- [ ] **国籍**：封面顶部明示法国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（预计仅诺奖理由英文一句；其余全部间接转述）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox ≤10pt、hbox ≤50pt）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有成品（Frederick Sanger）及数学家侧（高斯）格式对齐

---

> **名单状态**：本提示词已完成；Beamer 立传待执行。`chemist/generate_20th_century_list.py` 的 `BIOGRAPHIES_DONE` **暂不更新**，待 Beamer 完成后再置 ✅。
> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
