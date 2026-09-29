# Pedro Nunes（佩德罗·努内斯）立传提示词

> qid=Q435718 · 1502 – 1578-08-11 · 葡萄牙数学家 · 16 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/16th_century/pages/Pedro_Nunes/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**使用 `PORTRAITS.md` 指定的肖像文件** `nunes_portrait.png`（已下载到本目录 `images/`；文件名与图注以 `PORTRAITS.md` 为准），图注 `Pedro Nunes 像（1843 年 Panorama 杂志所刊）`。**不得改用装饰圆占位**；落地前须核验文件为 PNG/JPEG 且 >5KB。备选：里斯本发现者纪念碑雕像局部（`Pedro_Nunes_April_2009-1a.jpg`）**只能作正文插图，不得当头像**；`Assinatura_Pedro_Nunes.svg` 签名图可作版式元素。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 葡萄牙`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名（拉丁名 Petrus Nonius）、国籍、出生地、教育、任职、核心领域。事实取自 Wikipedia infobox 与正文，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），呼应「大航海时代的球面与航线」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Pedro Nunes（葡萄牙语读音 [ˈpeðɾu ˈnunɨʃ]；拉丁名 Petrus Nonius——其发明 nonius 即由此而来；中文惯称：佩德罗·努内斯）
- **生卒**：1502 生于 Alcácer do Sal（葡萄牙）→ 1578-08-11 逝于科英布拉（Coimbra），享年 76
- **国籍**：葡萄牙（出生时属 Kingdom of Portugal，历史政权）
- **身份**：数学家、宇宙志学家（cosmographer）、教授；很可能出身 New Christian（改宗基督教的犹太人后裔）家庭
- **家庭**：page.md 明载极少——仅知其孙辈数人曾被葡萄牙宗教裁判所指控信奉并秘密信犹太教而入狱数年；父母、配偶均无载，**禁写**
- **教育轨迹**：
  - 早年教育几乎无载；约 1517–1522 年就读萨拉曼卡大学（University of Salamanca）
  - 约 1529 年回里斯本开始任教，继续医学学业，同时在里斯本大学讲授伦理学、哲学、逻辑学与形而上学
  - 1532 年获医学博士（doctorate in medicine）
- **任职轨迹**：
  - 1529 年任 Royal Cosmographer（王家宇宙志学家）；1547 年升任 Chief Royal Cosmographer，任至去世
  - 1537 年葡萄牙大学由里斯本迁回科英布拉，随迁至重建的科英布拉大学任数学教授至 1562 年——这是科英布拉大学新设的教席（1544 年起数学成为独立教席），设立初衷或为满足航海技术训练之需
- **导师**：page.md 无载，**禁写**
- **研究领域**：数学、航海术、制图学、球面三角学、宇宙志、天文学、力学

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **用数学工具处理航海与制图的第一人**：被视为当时最伟大的数学家之一，首次以数学工具系统处理航海与海图问题。
2. **loxodrome（等角航线 / rhumb line）的首创者**：第一个指出恒向行驶的船不走大圆（两点间最短路），而是沿与经线保持固定夹角的螺旋线（loxodrome）航行——Nunes connection（navigator connection）即与等角航线直接相关。
3. **海图论战**：在 *Tratado em defensam da carta de marear*（1537）中主张海图的纬线与经线应画成直线，但他未能解决由此产生的投影问题——直到墨卡托（Mercator）发明其投影法才告解决，且沿用至今。
4. **nonius 测微装置发明人**：以同心圆逐圈内缩刻度提高象限仪等仪器的读数精度；第谷·布拉赫曾使用但嫌其复杂；启发了 Clavius 与 Jacob Curtius 的改进，最终由 Pierre Vernier（1631）化为游标卡尺（Vernier scale）——Vernier 自称其发明是「 perfected nonius」，很长时间里它就叫 nonius，瑞典语至今称 nonieskala。
5. **最短暮光问题**：求任一地点白昼最短暮光日及其时长——以微分几何眼光看极值问题，早于约翰与雅各布·伯努利一个多世纪独立攻克此题且更完整（伯努利兄弟只解出最短日、未能确定时长）；努内斯因而是极值问题的先驱。
6. **托勒密体系的最后一位重要改进者**：可能是最后一位对托勒密地心体系做出重要数学改进的大数学家；他了解哥白尼的著作，但在出版作品中仅略作提及、以纠正其中若干数学错误。
7. **球面三角学大师**：多数成就源于其对球面三角学的深刻理解，以及把托勒密对欧几里得几何的改造移植到球面三角上的能力。
8. **「最后的伟大评注家」与知识普及**：身处「评注古人」到「实验数据」的科学转型期；首作 *Tratado da sphera*（1537）评注 Sacrobosco/Purbach/托勒密；主张知识应共同而普遍地传播，故除拉丁文外兼用葡萄牙语与西班牙语（*Livro de Algebra*）出版。
9. **王室教师**：1531 年受若昂三世之命教育国王幼弟 Luís 与 Henry；后又受命教育王孙、未来的国王 Sebastian。
10. **国际影响**：对 John Dee 与 Edward Wright 的工作有明确影响；Clavius（格里高利历的推动者、罗马学院的核心人物）可能听过他的课并受其著作影响，称他为 supreme mathematical genius（至高无上的数学天才）。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海航海蓝） | `#0F4C81` | 大航海时代 / 葡萄牙 |
| 强调色（罗盘金） | `#C9A227` | 浑天仪与航海仪器的黄铜质感 |
| 分类色 1（等角航线 — 青绿） | `#0E7C7B` | loxodrome / 航海数学 |
| 分类色 2（制图学 — 靛蓝） | `#4C5FD5` | 海图 / 墨卡托投影前史 |
| 分类色 3（仪器 — 琥珀） | `#E07B30` | nonius / 游标卡尺前身 |
| 分类色 4（古典传承 — 玫红） | `#B76E79` | 托勒密评注 / 球面三角 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「球面、航线与浑天仪」的圆之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **选定曲目**：**Expedition**（alex-productions，`music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`）
- **风格定调**：**探索 / 史诗 / 开阔**（大航海时代远征式叙事）
- **匹配理由**：
  - 努内斯是「航海数学化」的第一人，生在葡萄牙垄断海洋贸易的黄金时代——"远征 / 探索"气质与其航海数学主题严丝合缝（curated_tracks.md 对 Expedition 的场景标注即「几何、拓扑、远征式叙事」）
  - 曲目的开阔感匹配「海图、球面、等角航线」的空间意象
  - 本组三人 BGM 互不重复：Nunes=Expedition、Commandino=PAST、Recorde=Awaken
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（统一 14 页制：共享封面 + 人物封面 + 身份信息 + 时间线 + 早年与教育 + 7 贡献页 + 荣誉与传承 + 终章）

> 正文采用 Wilson 式结构 + 表格 + 公式框：核心贡献页用 `tabularx`（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页用 `p{2.2cm}|X|p{3.0cm}` 表格。帧序与 `TEMPLATE_GUIDE.md` §2 完全同构（帧 1 = 共享封面 `\openmathslide`）。

1. **共享封面**（`\openmathslide`）：`\input{../../cover/openmath_page.tex}`，不改
2. **人物封面**（`\titleslide`）：大标题「航海数学之父 · 等角航线首创者」+ Pedro Nunes 1502–1578 + 右上肖像（`images/nunes_portrait.png`，图注见 PORTRAITS.md）+ 国籍行（葡萄牙）+ 底部三要素状态栏（葡萄牙 | 科英布拉大学 / 王家宇宙志学家 | 等角航线 / nonius / 海图数学化）+ 四分类 badge
3. **身份信息页**（`\profileslide`，★ 必做）：左肖像 + 右信息网格（生卒 / 拉丁名 Petrus Nonius / 国籍 / 出生地 Alcácer do Sal / 教育 / 任职 / 核心领域）
4. **佩德罗·努内斯的一生：时间线**（`\timelineslide`）：1502 Alcácer do Sal 出生 → c.1517–1522 萨拉曼卡 → c.1529 回里斯本任教 / 王家宇宙志学家 → 1532 医学博士 → 1537 科英布拉数学教授 → 1547 首席王家宇宙志学家 → 1562 卸任教席 → 1578-08-11 科英布拉去世
5. **早年与教育**（`\earlyslide`）：Alcácer do Sal、萨拉曼卡（约 1517–1522）、里斯本任教（伦理 / 哲学 / 逻辑 / 形而上学）、1532 医学博士
6. **等角航线 loxodrome**（贡献页，表格 + 公式框）：恒向航行的螺旋轨迹、与经线保持定角、非大圆（两点间最短路）——航海数学第一课
7. **海图论战与墨卡托前史**（贡献页，表格 + 公式框）：*Tratado em defensam da carta de marear*（1537）主张纬线经线皆画成直线、投影难题未解而留给墨卡托（**勿写努内斯影响墨卡托**）
8. **nonius 与测量仪器**（贡献页，表格 + 公式框）：同心圆逐圈内缩刻度原理、第谷使用而嫌其复杂、Clavius 与 Jacob Curtius 改进、Pierre Vernier 1631 化为游标
9. **最短暮光问题**（贡献页，表格 + 公式框）：任一定点的最短暮光日及其时长、极值问题先驱、伯努利兄弟一个多世纪后独立重解而「less success」（只解出最短日、未定时长）
10. **托勒密体系的最后改进者与球面三角**（贡献页，表格 + 公式框）：地心体系的数学改进、对哥白尼仅略作引述纠错；球面三角学的深刻理解与托勒密-欧几里得方法移植
11. **著作与多语出版**（贡献页，表格）：*Tratado da sphera*(1537)、*De crepusculis*(1542)、*De erratis Orontii Finaei*(1546)、*Petri Nonii Salaciensis Opera*(1566)、*Livro de Algebra*(1567)；拉丁 / 葡 / 西多语出版的普及主张
12. **王室教师与学术影响**（贡献页，表格）：Luís / Henry / Sebastian 三位王室学生；Clavius 的 "supreme mathematical genius" 评价（听课系 possible，见 §5）；John Dee / Edward Wright 受其影响
13. **荣誉与传承**（`\honorslide`）：page.md 无载任何奖项——本页写「身后纪念」：发现者纪念碑雕像、里斯本 Pedro Nunes 中学、Instituto Pedro Nunes、100 escudos 硬币、小行星 5313 Nunes、TAP 航空 A330 命名；**禁杜撰奖项**
14. **终章**（`\closingslide`）：76 岁辞世于科英布拉；「以数学工具驾驭海洋的第一人」的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **生卒裁定**：metadata.json 的 date_of_birth 有三个噪声值 `1492 / 1497 / 1502-01-01`，date_of_death 有 `1577 / 1578-08-11` 两个值——**以 page.md 正文与 infobox 为准：1502 生、1578-08-11 卒（享年 76）**；birth 具体日 page.md 无载，只写年份 1502，**勿写 1502-01-01**。
- **国籍**：metadata 国籍为 Kingdom of Portugal（历史政权）——封面用现代对应「葡萄牙」，入库时 Kingdom of Portugal 加 `era_note: historical`。
- **犹太血统表述**：page.md 措辞为 "probably from a New Christian (of Jewish origin) family"——**必须保留 probably（可能）限定**；孙辈被宗教裁判所指控入狱为明载，可客观简述，但勿渲染宗教冲突细节。
- **loxodrome 与墨卡托的关系**：page.md 实载是「努内斯主张海图经纬线画直线但**未能解决**由此产生的问题，局面持续到墨卡托发明投影法」——**禁写努内斯影响了墨卡托 / 二人有师承或通信**；表述为「提出问题在先、墨卡托解决在后」的客观承接即可。
- **Clavius 关系**：page.md 原文为 "It is possible that ... Clavius attended Pedro Nunes' classes"——听课是**可能（possible）**表述；但 Clavius 称其 "supreme mathematical genius" 为明载可引。入库建 influence 关系时 note 必须注明页面作 possible 推测。
- **伯努利兄弟的对比**：page.md 明载约翰与雅各布·伯努利一个多世纪后重解最短暮光问题且"less success"（只解出最短日、未定时长）——可写，但**勿写伯努利兄弟"失败"的贬低性总结**，忠实转述即可。
- **Nunes connection**：现代微分几何以 Nunes connection（navigator connection）命名相关联络，Cartan 1922 年访巴黎时曾向爱因斯坦展示——脚注级事实，可作花絮，勿展开成「努内斯对现代微分几何的贡献」。
- **第谷 / Vernier**：第谷用过 nonius 但嫌复杂、Vernier 1631 年改良为游标——属**装置传承**而非人际关系，勿建入库关系。
- **引语红线**：可用引语仅两条——Clavius 的 "supreme mathematical genius"；努内斯知识普及主张 «o bem, quanto mais comum e universal, tanto é mais excelente»（善愈共同愈普遍则愈卓越，脚注 10 载，注明转引自 Calafate）。其余一律转述，勿编造。
- **家庭**：父母、配偶、子女 page.md 均无载，**禁写**；孙辈入狱仅客观一句。
- **机构口径**：葡萄牙大学 1537 年「由里斯本迁回科英布拉」——表述为随迁/转任科英布拉大学，勿写「考取」；数学教席 1544 年成为独立教席为明载。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q435718 | 待写入 |
| name_zh | 佩德罗·努内斯 | 待写入 |
| name_en | Pedro Nunes | 待写入 |
| birth_date | 1502 | 待写入（仅年份，page.md 无月日） |
| death_date | 1578-08-11 | 待写入 |
| nationality | Portugal / Kingdom of Portugal（historical） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / navigation / cartography / astronomy / mechanics | 待写入 |
| has_biography | false | 本次只入库社会关系，立传未做 |

## 7. 社会关系入库清单（§20）

- **王室学生**：Luís of Portugal, Duke of Beja（国王幼弟）、Henry, King of Portugal（国王幼弟、后为国王）、Sebastian of Portugal（王孙、未来国王）——advisor-student
- **思想影响**：John Dee（其数学纲领受努内斯著作影响）、Edward Wright（其航海制图工作受努内斯影响）、Christopher Clavius（可能听过课并受著作影响，note 注明 possible）
- **争议**：Oronce Fine（1546 年 *De erratis Orontii Finaei* 专书指其错误）——controversy
- **不入库**：墨卡托（仅问题承接无直接关系）、第谷/Vernier（装置传承非人际）、Calafate（引语转引者）、纪念碑上并立的航海家们

## 8. 奖项清单

- page.md 无载任何奖项；**本页留空，禁编造**。身后纪念（小行星 5313 Nunes、100 escudos 硬币、中学与研究所命名、TAP 航机命名）归入荣誉叙事页而非奖项。

## 9. 机构清单

- 教育：University of Salamanca（萨拉曼卡大学，约 1517–1522）
- 任职：University of Lisbon（里斯本大学，约 1529–1537 任教，1532 医学博士）；University of Coimbra（科英布拉大学，1537–1562 数学教授）
- 王职（无机构条目，正文叙述）：Royal Cosmographer（1529）、Chief Royal Cosmographer（1547–1578）

## 10. 终审清单

- [ ] 生卒 1502 / 1578-08-11，享年 76，出生地 Alcácer do Sal、卒地科英布拉
- [ ] 国籍用「葡萄牙」现代对应，入库 Kingdom of Portugal 加 historical
- [ ] 犹太血统表述保留 probably 限定
- [ ] loxodrome「首创提出」、墨卡托「问题承接」表述准确，无师承/影响虚线
- [ ] nonius → Clavius/Curtius 改进 → Vernier 1631 游标 的装置链表述准确
- [ ] 最短暮光问题「早于伯努利兄弟一个多世纪且更完整」表述忠实
- [ ] 引语仅两条（Clavius 评价 + 脚注 10 葡语主张），均有出处
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Pedro_Nunes/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `PORTRAITS.md` 指定的 `nunes_portrait.png`（1843 年刊像；纪念碑雕像只能作插图，禁止当头像）
- [ ] **国籍**：封面顶部徽章明示葡萄牙
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 16 世纪组其他数学家（Recorde / Commandino）格式对齐

## 12. Review-1 事实终审记录（2026-09-29）

- 核对基准：`pages/Pedro_Nunes/page.md`（+ metadata.json / images.txt）
- 生卒 / 享年：page.md infobox 「Born 1502 Alcácer do Sal; Died 11 August 1578 (aged 76)」，卒地 Coimbra——与提示词一致；出生仅年份（无月日），metadata 出生三噪声值（`1492 / 1497 / 1502-01-01`）与死亡噪声值 `1577` 均已弃用
- 国籍口径：page.md / metadata 作 Kingdom of Portugal（历史政权）；封面写现代对应「葡萄牙」——与提示词一致
- 肖像结论：**有肖像**，`PORTRAITS.md` 指定 `nunes_portrait.png`（本目录 `images/`，480 KB，>5KB 合格），图注 `Pedro Nunes 像（1843 年 Panorama 杂志所刊）`；纪念碑雕像（`Pedro_Nunes_April_2009-1a.jpg`）按 PORTRAITS.md 只能作插图。§0.1 与 §11 旧口径（「纪念碑雕像可作封面图」「失败则装饰圆占位」）已删改
- 引语核对：两条均可在 page.md 查到——① Clavius 评语 "supreme mathematical genius"（line 39）；② 脚注 10 葡语 «o bem, quanto mais comum e universal, tanto é mais excelente»（转引自 Calafate，须注明转引）。其余无引号内容为转述
- 本轮修正：
  1. §0.1 第 1 条与 §11 头像行改为 PORTRAITS.md 口径（指定 `nunes_portrait.png` + 图注；纪念碑雕像降为插图、禁止当头像、禁止装饰圆顶替）
  2. §4 按统一 14 页制重写（共享封面 + 人物封面 + 身份 + 时间线 + 早年 + 7 贡献页 + 荣誉与传承 + 终章）；原「托勒密体系」与「球面三角学」两页合并为帧 10，原「身后纪念」升为帧 13 `\honorslide`；帧 7 补明「勿写努内斯影响墨卡托」、帧 8 补 Clavius / Curtius 中间环节
- 遗留不确定项：① 生年无月日，正文只写 1502；② 犹太血统须保留 page.md 的 "probably" 限定；③ Clavius 听课系 "It is possible that..."，入库须注 possible；④ `De crepusculis` 的成书年份与 Nunes connection 条目为脚注级花絮，勿展开

## 13. 立传期记录（2026-09-29，math16-b）

- 产出：`Pedro_Nunes_zh.tex`（14 页：共享封面 + 人物封面 + 身份信息 + 时间线 + 早年 + 7 贡献页 + 荣誉与传承 + 终章）、`Makefile`（仅改 `MAIN`/`VIDEO_NAME`）。
- 编译：`make distclean && make` 0 error；Overfull 1 处 4.75pt（<10pt 达标）。
- 肖像落地：`nunes_portrait.png`（1843 年 Panorama 杂志所刊像）。标题页图注取简写「1843 年刊像」，身份信息页图注用全称「Pedro Nunes 像（1843 年 Panorama 杂志所刊）」——标题页图注缩短以避免越出右边界。
- 事实与 page.md 无冲突：生年只写 1502（无月日）、卒 1578-08-11、享年 76；犹太血统保留「probably」限定；loxodrome 首创、墨卡托「问题承接」无师承；nonius 装置链（第谷 → Clavius/Curtius → Vernier 1631）表述为装置传承、不入库；导师 / 父母 / 配偶按 page.md 无载禁写。
- 引语：仅用 Clavius "supreme mathematical genius"；脚注 10 葡语主张因版面取舍未入正文（未编造任何引语）。
- 未做 mp4（按主控统一安排）。

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
