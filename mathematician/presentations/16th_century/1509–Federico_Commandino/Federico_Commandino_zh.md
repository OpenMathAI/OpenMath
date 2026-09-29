# Federico Commandino（费德里科·科门迪诺）立传提示词

> qid=Q671745 · 1509 – 1575-09-05 · 意大利数学家 · 16 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/16th_century/pages/Federico_Commandino/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**使用 `PORTRAITS.md` 指定的肖像文件** `commandino_portrait.jpg`（已下载到本目录 `images/`，74 KB，合格；文件名与图注以 `PORTRAITS.md` 为准），图注 `Federico Commandino（传世版画像）`。**不得改用装饰圆占位**；落地前核验文件为 JPEG 且 >5KB。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 意大利（乌尔比诺公国）`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、国籍、出生地、师承（Brassavola）、教育、恩主、核心领域。事实取自 Wikipedia infobox 与正文，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），呼应「古希腊手稿与几何原图」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Federico Commandino（中文惯称：费德里科·科门迪诺）
- **生卒**：1509 生于乌尔比诺（Urbino）→ 1575-09-05 逝于乌尔比诺，享年 66
- **国籍**：意大利（出生时属 Duchy of Urbino，乌尔比诺公国，历史政权）
- **身份**：人文主义者、数学家、古希腊数学著作翻译家、出版者、医师
- **家庭**：page.md 无载，**禁写**
- **教育轨迹**：
  - 就读帕多瓦大学（University of Padua）
  - 后赴费拉拉大学（University of Ferrara），师从 Antonio Musa Brassavola 获医学博士（doctorate in medicine）
- **恩主链**（page.md 明载的赞助人序列）：维泰博主教 Grassi → 教宗克莱孟八世（Clement VIII）→ 乌尔比诺公爵 Guidobaldo II della Rovere → 随枢机 Ranuccio Farnese 赴罗马 → 枢机 Cervini（短暂在位为教宗玛策禄二世 Marcellus II）→ 被 Francesco Maria II della Rovere 请回乌尔比诺
- **导师**：Antonio Musa Brassavola（费拉拉，医学博士导师）
- **研究领域**：数学、数学史（古希腊著作整理）、几何学、重心理论

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **古希腊数学的「文艺复兴摆渡人」**：以翻译、校勘、出版古代数学家著作为毕生中心事业——史料以希腊文写本为主、阿拉伯文为次；译文以拉丁文为主、意大利文为次。
2. **阿基米德的再生**：负责阿基米德多部论著的整理出版；1565 年在博洛尼亚出版 *Archimedis De iis quae vehuntur in aqua libri duo*（浮体论二卷，校订并加评注）。
3. **译业版图**：阿里斯塔克斯《论日月的大小与距离》、帕普斯《数学汇编》、希罗《气体力学》、托勒密《平面球体图》与《晷针》、阿波罗尼奥斯《圆锥曲线论》、欧几里得《几何原本》——几乎覆盖希腊几何的正典谱系。
4. **科门迪诺定理（Commandino's theorem）**：四面体过各顶点到对面重心的四线共点——首次出现于其重心理论著作 *Liber de centro gravitatis solidorum*（1565）。
5. **重心的几何理论**：*Liber de centro gravitatis solidorum*（1565）是立体重心理论的系统几何处理，承阿基米德而来、启下世纪力学。
6. **师承一脉**：学生 Guidobaldo del Monte 与 Bernardino Baldi——前者成为力学名家并是伽利略的挚友（此句为延伸语境，**正文只写 page.md 实载的学生身份**）。
7. **欧洲学者通信网**：与 Conrad Dasypodius、Gerolamo Cardano、Francesco Maurolico、Christopher Clavius 保持通信——古典数学复兴的跨国网络节点。
8. **文艺复兴人文主义侧影**：在乌尔比诺可能与 John Dew 会面——page.md 原文 "putatively met John Dee"（据说/推测会面），仅可作存疑花絮。
9. **从医学到数学**：医学博士出身而以数学翻译名世——16 世纪学者「一身多职」的典型样本。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（乌尔比诺赭红） | `#7A3B2E` | 乌尔比诺公国的宫廷赭色 / 古典手稿 |
| 强调色（手稿羊皮金） | `#B98A2F` | 希腊抄本与拉丁译本的书卷感 |
| 分类色 1（翻译事业 — 靛蓝） | `#3D5A80` | 希腊→拉丁的古典摆渡 |
| 分类色 2（阿基米德 — 青绿） | `#0E7C7B` | 浮体论 / 阿基米德正典 |
| 分类色 3（重心理论 — 琥珀） | `#C87F2F` | Commandino 定理 / 立体重心 |
| 分类色 4（师承通信 — 玫红） | `#8E5572` | del Monte / Baldi / 欧洲通信网 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「抄本、书页与几何图形」的静态之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **选定曲目**：**PAST**（alex-productions，`music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav`）
- **风格定调**：**历史感 / 深沉 / 回望古典**
- **匹配理由**：
  - 科门迪诺毕生事业是「向两千年前回望」——把阿基米德、帕普斯、欧几里得从希腊抄本摆渡到拉丁世界；PAST 的"历史感 / 深沉"定调与"古典复兴"主题天然契合（curated_tracks.md 场景标注「人物回顾、数学传统」）
  - 沉稳的节奏匹配其学者型、非论战型的一生（无大起大落，只有默默译述）
  - 本组三人 BGM 互不重复：Nunes=Expedition、Commandino=PAST、Recorde=Awaken
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（统一 14 页制：共享封面 + 人物封面 + 身份信息 + 时间线 + 早年与教育 + 7 贡献页 + 荣誉与传承 + 终章）

> 正文采用 Wilson 式结构 + 表格 + 公式框：核心贡献页用 `tabularx`（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页用 `p{2.2cm}|X|p{3.0cm}` 表格。帧序与 `TEMPLATE_GUIDE.md` §2 完全同构（帧 1 = 共享封面 `\openmathslide`）。

1. **共享封面**（`\openmathslide`）：`\input{../../cover/openmath_page.tex}`，不改
2. **人物封面**（`\titleslide`）：大标题「古希腊数学的摆渡人 · 阿基米德再生」+ Federico Commandino 1509–1575 + 右上肖像（`images/commandino_portrait.jpg`，图注见 PORTRAITS.md）+ 国籍行（意大利 · 乌尔比诺公国）+ 底部三要素状态栏（意大利 | 无固定教职（恩主赞助） | 古希腊数学翻译 / 重心理论 / 阿基米德校勘）+ 四分类 badge
3. **身份信息页**（`\profileslide`，★ 必做）：左肖像 + 右信息网格（生卒 / 国籍 / 出生地 Urbino / 师承 Brassavola / 教育 / 恩主 / 核心领域）
4. **费德里科·科门迪诺的一生：时间线**（`\timelineslide`）：1509 乌尔比诺出生 → 帕多瓦求学 → 费拉拉医学博士（Brassavola 门下）→ Grassi / 克莱孟八世庇护 → Guidobaldo II 庇护 → 罗马（Farnese / Cervini）→ 归乌尔比诺（Francesco Maria II）→ 1565 重心著作 / 阿基米德浮体论 → 1575-09-05 卒于乌尔比诺
5. **早年与教育**（`\earlyslide`）：乌尔比诺、帕多瓦、费拉拉、医学博士、从医学到数学
6. **翻译家的事业版图**（贡献页，表格）：希腊文写本为主、阿拉伯文为次 → 拉丁译文为主、意大利文为次；七位古希腊数学家的译业清单表
7. **阿基米德的再生**（贡献页，表格 + 公式框）：*Archimedis De iis quae vehuntur in aqua libri duo*（1565 博洛尼亚，校订并加评注）——口径为「负责出版阿基米德多部论著」，勿夸大为全部遗作首刊
8. **科门迪诺定理与立体重心理论**（贡献页，表格 + 公式框）：四面体过各顶点到对面重心的四线共点；出自 *Liber de centro gravitatis solidorum*（1565）——定理**首次出现于该重心著作**，勿写成译欧几里得时发现
9. **托勒密 / 阿波罗尼奥斯 / 帕普斯**（贡献页，表格）：《平面球体图》《晷针》《圆锥曲线论》《数学汇编》与阿里斯塔克斯、希罗、欧几里得的翻译意义
10. **师承与通信网**（贡献页，表格）：学生 Guidobaldo del Monte、Bernardino Baldi；通信学者 Dasypodius / Cardano / Maurolico / Clavius（**勿延伸写 del Monte–伽利略关系**）
11. **恩主与文艺复兴宫廷**（贡献页，表格）：Grassi → 克莱孟八世 → Guidobaldo II → Farnese → Cervini → Francesco Maria II 的庇护链（patronage，非学术合作者；克莱孟八世句的年代矛盾按 §5 照录并注存疑）
12. **著作年表**（贡献页，表格）：*Liber de centro gravitatis solidorum*（1565）、*Archimedis De iis quae vehuntur in aqua*（1565）；可附 John Dee「据说会面」之存疑花絮（带限定语）
13. **荣誉与传承**（`\honorslide`）：page.md 无载任何奖项——本页写「译业的历史回响」：为伽利略时代的力学与几何备好文本基础、Commandino 定理至今存名；**禁杜撰奖项**
14. **终章**（`\closingslide`）：66 岁辞世于乌尔比诺；「他把古希腊数学交给了近代」的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **生卒裁定**：metadata.json 的 date_of_birth 有 `1509-01-01 / 1506` 两个值、date_of_death 有 `1575-09-03 / 1575-09-05` 两个值——**以 page.md 正文为准：1509 生、1575-09-05 卒**；birth 具体日 page.md 无载，只写年份 1509，**勿写 1509-01-01**；§5 记录 1506 与 09-03 为 metadata 噪声。
- **国籍**：metadata 国籍为 Duchy of Urbino（乌尔比诺公国，历史政权）——封面用现代对应「意大利」，入库时 Duchy of Urbino 加 `era_note: historical`。
- **克莱孟八世的年代矛盾**：page.md 明载其受克莱孟八世（Clement VIII）庇护，但克莱孟八世 1592 年才即位、晚于其卒年 1575——这是 Wikipedia 条目自身的表述，**行文忠实照录 page.md 并可加小字注记年代存疑，勿擅自改写为其他教宗**；§5 记录此裁定。
- **John Dee 关系**：page.md 原文 "putatively met John Dee"（据说会面）——**推测性表述，不入库关系**；正文若提及必须带「据说/推测」限定。
- **Guidobaldo del Monte 与伽利略**：page.md 只载 del Monte 是其学生——**勿延伸写 del Monte-伽利略关系**，更勿写「科门迪诺影响了伽利略」。
- **译本与「科门迪诺定理」**：定理首次出现于重心著作（1565）——勿写「在翻译欧几里得时发现」；勿把译书与其原创著作混为一谈。
- **恩主≠合作者**：教宗、枢机、公爵是赞助人（patronage），**不是学术合作者**——入库不建任何关系类型，仅正文叙述。
- **引语红线**：page.md 全文无 Commandino 直接引语——**全篇禁引语**，一律转述。
- **卒地**：page.md 正文未明写卒地，metadata place_of_death 为 Urbino——可用「卒于乌尔比诺」，§5 注明此值取自 metadata（与 page.md 无冲突）。
- **「阿基米德翻译家」的准确口径**：page.md 表述为 "responsible for the publication of many treatises of Archimedes"（负责出版阿基米德多部论著）——勿夸大为「全部阿基米德遗作的首次出版」。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q671745 | 待写入 |
| name_zh | 费德里科·科门迪诺 | 待写入 |
| name_en | Federico Commandino | 待写入 |
| birth_date | 1509 | 待写入（仅年份，page.md 无月日） |
| death_date | 1575-09-05 | 待写入 |
| nationality | Italy / Duchy of Urbino（historical） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / geometry / mechanics / history of mathematics | 待写入 |
| has_biography | false | 本次只入库社会关系，立传未做 |

## 7. 社会关系入库清单（§20）

- **博士导师**：Antonio Musa Brassavola（费拉拉大学，医学博士）——advisor-student
- **学生**：Guidobaldo del Monte、Bernardino Baldi——advisor-student
- **通信学者**：Conrad Dasypodius、Gerolamo Cardano、Francesco Maurolico、Christopher Clavius——collaborator
- **不入库**：John Dee（putatively met 推测会面）、诸位恩主（Grassi/克莱孟八世/Guidobaldo II/Farnese/Cervini/Francesco Maria II，patronage 非学术关系）、古希腊诸位作者（阿基米德/欧几里得等，跨两千年禁建关系）

## 8. 奖项清单

- page.md 无载任何奖项；**本页留空，禁编造**。

## 9. 机构清单

- 教育：University of Padua（帕多瓦大学）；University of Ferrara（费拉拉大学，医学博士）
- 任职：page.md 未载任何教职/机构雇佣（一生主要依靠恩主赞助）——**institution 表仅录教育两条，勿编造任职**。

## 10. 终审清单

- [ ] 生卒 1509 / 1575-09-05，享年 66，生卒地均乌尔比诺
- [ ] 国籍用「意大利」现代对应，入库 Duchy of Urbino 加 historical
- [ ] 克莱孟八世年代矛盾按 page.md 照录并注存疑
- [ ] John Dee 仅「据说会面」且不入库
- [ ] 科门迪诺定理出自 1565 重心著作表述准确
- [ ] 译业清单与 page.md 一致（阿基米德/阿里斯塔克斯/帕普斯/希罗/托勒密/阿波罗尼奥斯/欧几里得）
- [ ] 全篇无直接引语
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Federico_Commandino/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `PORTRAITS.md` 指定的 `commandino_portrait.jpg`（禁止改为装饰圆占位）
- [ ] **国籍**：封面顶部徽章明示意大利（乌尔比诺公国）
- [ ] **引语核对**：page.md 无直接引语，全篇应为转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 16 世纪组其他数学家（Nunes / Recorde）格式对齐

## 12. Review-1 事实终审记录（2026-09-29）

- 核对基准：`pages/Federico_Commandino/page.md`（+ metadata.json / images.txt）
- 生卒 / 享年：page.md 「1509 – 5 September 1575」，metadata date_of_death 首选值 `1575-09-05`，两者一致，享年 66；出生仅年份 1509（page.md 无月日，metadata 的 `1509-01-01` 与 `1506-00-00` 均弃用）；卒地 page.md 正文未明写，metadata place_of_death 作 Urbino（与出生地同城，可用）
- 国籍口径：page.md / metadata 作 Duchy of Urbino（历史政权）；封面写「意大利（乌尔比诺公国）」——与提示词一致
- 肖像结论：**有肖像**，`PORTRAITS.md` 指定 `commandino_portrait.jpg`（本目录 `images/`，74 KB，>5KB 合格），图注 `Federico Commandino（传世版画像）`；§0.1 与 §11 旧口径（「失败则装饰圆占位」）已删改
- 引语核对：page.md 全篇无 Commandino 直接引语——**本篇禁引语**，一律转述；§4/§10 已同步此口径
- 本轮修正：
  1. §0.1 第 1 条与 §11 头像行改为 PORTRAITS.md 口径（指定 `commandino_portrait.jpg` + 图注 + 禁止装饰圆顶替）
  2. §4 按统一 14 页制重写（共享封面 + 人物封面 + 身份 + 时间线 + 早年 + 7 贡献页 + 荣誉与传承 + 终章）；原「科门迪诺定理」与「立体重心理论」两页合并为帧 8，原「译业的历史回响」升为帧 13 `\honorslide`、原「著作年表」定为帧 12；帧 7/8/10/11 分别补入「勿夸大阿基米德首刊」「定理出自 1565 重心著作」「勿延伸 del Monte–伽利略」「克莱孟八世年代矛盾照录」四条口径要点
- 撞曲记录（只记录不改）：§3.5 选定曲目 **PAST** 与德尔·费罗（del Ferro）篇相同；本组三人 Nunes / Commandino / Recorde 组内不撞（Expedition / PAST / Awaken），跨组撞曲留给主控统一协调
- 遗留不确定项：① 克莱孟八世（1592 年即位，晚于 1575 卒年）庇护句系 page.md 原表述，须照录并加小字注记年代存疑，**不得擅自改为其他教宗**；② John Dee 仅为 "putatively met"（据说），不入库、正文须带限定语；③ 恩主链均为 patronage，不入库建关系

## 13. 立传期记录（2026-09-29，math16-b）

- 产出：`Federico_Commandino_zh.tex`（14 页：共享封面 + 人物封面 + 身份信息 + 时间线 + 早年 + 7 贡献页 + 荣誉与传承 + 终章）、`Makefile`（仅改 `MAIN`/`VIDEO_NAME`）。
- 编译：`make distclean && make` 0 error；Overfull 1 处 4.75pt（<10pt 达标）。
- 肖像落地：`commandino_portrait.jpg`；标题页图注「传世版画像」，身份信息页图注「Federico Commandino（传世版画像）」。
- 事实与 page.md 无冲突：1509 / 1575-09-05，享年 66；生卒地均乌尔比诺；封面国籍写「意大利（乌尔比诺公国）」；克莱孟八世庇护句照录并加小字注「1592 即位，晚于卒年 1575，存疑」；John Dee 仅写「putatively met 据说会面」；科门迪诺定理注明首见于 1565 重心著作（非译欧几里得时发现）；恩主链仅叙述不入库；全篇无直接引语（page.md 无）。
- 未做 mp4（按主控统一安排）。

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
