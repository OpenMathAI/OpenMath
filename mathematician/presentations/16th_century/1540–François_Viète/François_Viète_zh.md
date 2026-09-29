# François Viète（弗朗索瓦·韦达）立传提示词

> qid=Q188623 · 1540 – 1603-02-23 · 法国数学家、密码学家、律师 · 16 世纪（现代代数记法之父）
> 本地 Wikipedia 数据源：`mathematician/presentations/16th_century/pages/François_Viète/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。Wikipedia infobox 本体无真实肖像（仅签名与 1646 年《Opera》书影），`images.txt` 肖像候选为 Charles Meryon 1861 年蚀刻版画 `François_Viète_MET_DP813249.jpg`（MET 馆藏）——立传时下载该图；若印刷质量不可用则用装饰圆 `\faIcon{user}` 占位，并在页脚注明「后世版画」。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 法兰西`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名（拉丁名 Franciscus Vieta）、国籍、出生地、职业、教育、代表著作、核心领域。事实取自 Wikipedia infobox 与 page.md，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），呼应「字母符号 / 密码转盘」母题——韦达把代数从「文字叙述」变成「字母运算」。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：François Viète（法语发音 [fʁɑ̃swa vjɛt]），拉丁名 **Franciscus Vieta**（Other name），中文惯称：弗朗索瓦·韦达
- **生卒**：1540 生于 Fontenay-le-Comte（Kingdom of France，今 Vendée 省）→ 1603-02-23 逝于巴黎，享年 62–63；**出生月日 page.md 无载**
- **国籍**：法兰西（Kingdom of France；metadata nationality = France）
- **身份**：数学家、密码学家（cryptographer）、律师（lawyer by trade）；先后任**亨利三世与亨利四世的枢密顾问**（privy councillor）与 maître des requêtes——**业余数学家**，数学研究在夜间与闲暇进行
- **家庭**：祖父为 La Rochelle 商人；父 Etienne Viète 是 Fontenay-le-Comte 律师兼 Le Busseau 公证人；母亲是 Barnabé Brisson（法官、天主教联盟当政时期议会首任主席）的姑母；两个女儿——Jeanne（母 Barbe Cottereau，嫁布列塔尼议会议员 Jean Gabriau，1628 卒）与 Suzanne（母 Julienne Leclerc，1618-01 卒于巴黎）；配偶无载
- **教育轨迹**：
  - 方济各会（Franciscan）学校
  - 1558 年入 Poitiers 学法律
  - 1559 年获法学士（LL.B.）
  - 1560 年起在故乡当执业律师，从接手要案开始（曾为弗朗索瓦一世遗孀处理普瓦图租金案、照管苏格兰女王玛丽的利益）
- **导师**：page.md 无载（**禁写任何导师**）
- **研究领域**：代数（新代数/符号代数）、三角学、几何、天文学、密码学

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **新代数（New Algebra）——第一个符号代数**：用字母作方程参数，辅音表已知量、元音表未知量；因此被称为「现代代数记法之父」（the father of modern algebraic notation）。
2. **《In artem analyticem isagoge》（1591）**：又称 *Algebra Nova*，献给 Catherine de Parthenay；提出 species logistic（符号逻辑术）三步法——**Zetetic（列方程）→ Poristic（析解）→ Exegetic（回到几何/数值构造）**；宣称 `nullum non problema solvere`（无不可解之题）。
3. **韦达定理（Vieta's formulas）**：多项式根与系数的关系（和与积），最初仅就正根陈述。
4. **二项式公式**：后被帕斯卡与牛顿采用。
5. **韦达公式（Viète's formula，1593）**：数学史上**第一个无穷乘积**——π 的嵌套根式表达式；用阿基米德方法取 6×2^16 = 393,216 边形得 10 位小数。
6. **两朝密码破译者**：1589 年起为亨利三世破译天主教联盟密信；亨利四世时代 1590 年破解西班牙 500+ 字符密码；Moreo 司令致西班牙国王信件的破译揭穿马耶讷公爵谋立，促成宗教战争和解；**西班牙国王指控韦达「使用魔法」**。
7. **van Roomen 挑战（1593）**：荷兰大使讥法国无数学家，Adriaan van Roomen 提出全欧征解 45 次方程；韦达倚窗几分钟即看出它是 sin(x) 与 sin(x/45) 的关系，「Ut legit, ut solvit」（一读即解），次日交出其余 22 问；1595 年出版回应并回赠阿波罗尼奥斯问题，1600 年以 *Apollonius Gallus*（相似中心法）解决，两人反成挚友。
8. **格里高利历论战**：1600 年发表系列小册子指责克拉维乌斯（Clavius）任意改动历法计算，提出自己的历表；克拉维乌斯在韦达死后以 *Explicatio*（1603）反驳。
9. **倍角正弦公式**：由单角正弦导出多倍角正弦的公式（1593 年已知）。
10. **齐次性原理（homogeneity）**：方程中量须同纲（线/面/体），超前于时代；身后著述由学生 Anderson、Ghetaldi 等整理出版，笛卡尔、费马、牛顿、哈里奥特均使用其符号体系。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（法兰西宫廷深蓝） | `#1F3A5F` | 瓦卢瓦/波旁宫廷、两朝枢密顾问 |
| 强调色（文艺复兴鎏金） | `#B8860B` | 16 世纪印刷术与人文主义黄金时代 |
| 分类色 1（新代数 — 靛蓝） | `#3A5BA0` | 符号化 / Isagoge / 韦达定理 |
| 分类色 2（密码破译 — 深红） | `#8C2F2F` | 两朝密码战 / 西班牙密信 |
| 分类色 3（三角与 π — 青绿） | `#0F766E` | 无穷乘积 / Canon mathematicus / 倍角公式 |
| 分类色 4（历法论战与律师生涯 — 琥珀） | `#C77B30` | 格里高利历之争 / 律师与枢密院 |
| 背景 | `#F7F5F2` | 米白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「字母符号 / 密码转盘」的母题。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **选定曲目**：**Cinematic Experience**（AShamaluevMusic 系之外，Inspiring Electronic 合辑，`music_audio/alex-productions/...` 对应 `48-QL3O8MUFAm4-Cinematic-Experience.wav`，3:22 量级、电影感/高张力）
- **风格定调**：**电影感 / 高张力 / 宫廷悬疑**
- **匹配理由**：
  - 韦达一生三重叙事张力极强：宫廷（两朝枢密顾问）、密码战（破译西班牙密码被指控魔法）、全欧数学挑战（倚窗即解 45 次方程）——需要**电影感、高张力**的配乐撑起「章节高潮」
  - 「Cinematic Experience」的张力曲线匹配「密码破译→宗教战争和解→数学决斗」的段落推进
  - 与本批次另一人 Simon Stevin 的 **Expedition**（探索/史诗）互不重复
- 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐高斯模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「代数的符号化者 · 两朝密码破译者」+ François Viète 1540–1603 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 Franciscus Vieta / 国籍 / 出生地 / 职业 / 教育 / 代表著作 / 核心领域）
3. **韦达的一生：时间线**（`\timelineslide`）：1540 丰特奈勒孔特出生 → 1559 LL.B. → 1564 入 Parthenay 家族任家庭教师 → 1573 雷恩高等法院参事 → 1580 maître des requêtes → 1585–89 被迫去职、四年专研数学 → 1591 《Isagoge》 → 1593 π 无穷乘积与 van Roomen 挑战 → 1594 专属破译 → 1600 Apollonius Gallus 与历法论战 → 1602 去职 → 1603-02-23 逝于巴黎
4. **早年与法律生涯**（`\earlyslide`）：丰特奈勒孔特、Poitiers 法学、为 Soubise 家族服务、Catherine de Parthenay 的家庭教师（为其写天文/三角讲义、用小数早于 Stevin 二十年、行星椭圆轨道早于 Kepler 四十年）
5. **新代数：符号革命**（核心贡献页，表格 + 公式框）：辅音=已知参数、元音=未知量；`nullum non problema solvere`
6. **《Isagoge》1591 与 species logistic 三步法**（核心贡献页，表格 + 公式框）：Zetetic / Poristic / Exegetic；示例 `X^2+Xb=c`、`X^3+aX=b`（约化为二次）
7. **韦达定理与二项式公式**（核心贡献页，表格 + 公式框）：根与系数（和/积，正根口径）；二项式公式后传 Pascal/Newton
8. **韦达公式：π 的第一个无穷乘积**（核心贡献页，公式框）：`π = 2 × 2/√2 × 2/√(2+√2) × …`，393,216 边形、10 位小数
9. **三角学贡献**（核心贡献页，表格）：*Canon mathematicus*（1579，超越 Regiomontanus 与 Rheticus 的表）、倍角正弦公式（1593）
10. **两朝密码破译**（表格）：亨利三世联盟密信 → 1590 西班牙 500+ 字符密码 → Moreo 信件与马耶讷阴谋 → 宗教战争和解 → 西班牙国王指控「魔法」；1594 起专属破译；临终密码论文使当时一切加密方法过时
11. **van Roomen 挑战与 Apollonius Gallus**（表格）：荷兰大使之讥 → 倚窗即解 → 回赠阿波罗尼奥斯问题 → 1600 相似中心法 → 挚友（van Roomen 骑马赴丰特奈住一月学新代数）
12. **格里高利历论战：对克拉维乌斯**（表格）：1600 小册子指控任意改动 → 自拟历表 → Clavius 1603 *Explicatio* 反驳 → page.md 明载「据说韦达错了」；De Thou 记其对 Clavius 的贬评（引语按原文）
13. **晚年与身后传承**（表格）：1602-12 去职获 20,000 埃居 → 1603-02-23 逝（死因未知，Anderson 称「a praeceps et immaturum autoris fatum」）→ Anderson/Ghetaldi/van Schooten 出版遗产 → 笛卡尔「I began, where Vieta finished」、费马/牛顿/哈里奥特用其符号
14. **终章**：「现代代数记法之父」的历史地位——结束中世纪代数（花拉子米到 Stevin）、开启近代代数

## 5. 史实陷阱与敏感点（终审必须检查）

- **生卒**：出生**仅有年份 1540，月日无载——禁写具体出生日**；metadata.json `date_of_death` 有双值噪声 `["1603-12-13","1603-02-23"]`，**以 page.md「23 February 1603」为准**（yaml/prompt 统一 1603-02-23，§5 记录裁定）。享年 62–63。
- **姓名与 QID**：metadata.json `label` 为 **null**，name_en 取 `name` 字段 **"François Viète"**（Q188623）；拉丁名 Franciscus Vieta 是 Other name，勿作 name_en；别名拼写 Vieta/Viete 勿混用。
- **职业口径**：韦达**本业是律师与王室顾问**（attorney → Parlement of Rennes 参事 → maître des requêtes → 枢密顾问），数学是夜间与闲暇的「业余」研究（De Thou 记其悬肘伏案三日不解的轶事）——封面 badge 可写「数学家 · 密码学家 · 律师」，但**禁写「职业数学家」**。
- **代数记法的局限**：辅音/元音选择后为笛卡尔 a,b,c / x,y,z 惯例取代；韦达不知「=」号（Recorde 1557 已用）、不知乘法记法（Oughtred 1631）；坚持齐次性原理、须以几何构造复核代数解——这些都是 page.md 明载的时代局限，可如实写，但**「第一个符号代数」「结束中世纪代数、开启近代」是 page.md 原口径，可用**。
- **韦达定理**：page.md 口径为「多项式系数与根的和与积之关系，called Viète's formula(s)」，当时只认正根——勿写「完整韦达定理（含复根）」。
- **π 无穷乘积**：page.md 明载「数学史上第一个无穷乘积」——此语可用；勿加「第一个无穷级数/第一个连分数」等页外说法。
- **密码破译口径**：为亨利三世（破联盟密信）与亨利四世服务属实；「西班牙国王指控其用魔法」是 page.md 原文，可写；Moreo 信件内容促成宗教战争和解是 page.md 原口径。**1594 起「专属破译敌方密码」**。
- **Clavius 论战口径**：Viète 指控 Clavius「任意引入改正与间日、误解其前人（Lilius）著作、尤其月球周期计算」；Clavius 在**韦达死后**以 *Explicatio*（1603）巧妙反驳；page.md 明载 **"It is said that Viète was wrong"**——必须如实写韦达败于此役，禁写韦达「纠正了格里高利历」。
- **宗教敏感点**：被天主教联盟指控同情新教，但**并非 Huguenot**；1574-04-06 入布列塔尼法院时公开宣读天主教信仰声明；终身保护新教徒，属「Politicals」（以国家稳定为先）；临终不愿告解，友人以「否则你女儿将嫁不出去」相劝；其是否信教「有争议」——**客观简述，不做单侧评价**。
- **与 van Roomen**：先挑战后成友（De Thou 记其骑马赴 Fontenay-le-Comte 同住一月、学新代数，韦达承担其全部开销）——**禁写宿敌**。
- **Descartes 影响**：page.md 明载 **"Current research has not shown the extent of the direct influence"**；笛卡尔 1639 致 Mersenne 信否认读过韦达，又被传记家 Adam 指出矛盾；「I began, where Vieta finished」——influence 关系 note 必须带「直接影响程度未明」限定。
- **引语白名单**（其余一律禁编引语）：①Isagoge 献词英译「These things which are new are wont in the beginning to be set forth rudely and formlessly…」；②De Thou 记其「伏案三日、悬肘而食」；③De Thou 转述其对 Clavius「善释原理、辑而不注出处」的评价；④"Ut legit, ut solvit"；⑤笛卡尔「I began, where Vieta finished」与 1639-02 致 Mersenne 信；⑥Anderson "praeceps et immaturum autoris fatum"。
- **家庭口径**：两个女儿的母亲（Barbe Cottereau、Julienne Leclerc）page.md 有名，但**无配偶记载**—— daughters 入 parent-child，两位母亲不入 spouse（无婚姻载）；父 Etienne Viète 入 parent-child。
- **学历**：仅 LL.B.（1559），无更高学位；**无导师记载，禁写导师**。
- **死因**：未知（page.md 原文 "The cause of Viète's death is unknown"）——留白勿猜。
- **无奖项记载**（§8 写无）。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q188623 | 待写入 |
| name_zh | 弗朗索瓦·韦达 | 待写入 |
| name_en | François Viète | 待写入 |
| birth_date | 1540 | 待写入（年，月日无载） |
| death_date | 1603-02-23 | 待写入（metadata 双值取 page.md） |
| nationality | France / Kingdom of France（era_note: historical） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / algebra / trigonometry / geometry / astronomy / cryptography | 待写入 |
| has_social_data | 1 | 本次入库置 1 |
| has_biography | 0 | 本次仅入库社会关系，立传未做 |

## 7. 社会关系入库清单

- **学生**：Catherine de Parthenay（12 岁起家庭教师，教科学与数学，Isagoge 献给她）；Alexander Anderson（notable student，身后著作整理出版者）；Jacques Aleaume；Marino Ghetaldi（身后出版 Supplementum Apollonii Galli）；Jean de Beaugrand（库内既有 stub，后将其著作译为拉丁文）
- **思想影响**：René Descartes（库内既有 id=1296；笛卡尔《几何》建在其工作之上并取消齐次性要求；「I began, where Vieta finished」；直接影响程度研究未明——note 必须带此限定）
- **论战**：Christopher Clavius（格里高利历，1600 Expostulatio；C 组写对侧，INSERT IGNORE 自动去重）；Joseph Juste Scaliger（1589–1590 Viète 胜出、1596 再攻 1597 终答）；Adriaan van Roomen（1593 45 次方程挑战；后成挚友、van Roomen 同住一月学新代数——note 注明）
- **家庭**：父 Etienne Viète（Fontenay-le-Comte 律师、Le Busseau 公证人）；长女 Jeanne（母 Barbe Cottereau）；次女 Suzanne（母 Julienne Leclerc）
- **挚友/史料**：Jacques de Thou（友人，其著述保存韦达钻研轶事、对 Clavius 的评价等核心史料）
- **不入库**：Nathaniel Tarporley（秘书，非师生非同事，无对应类型）；雇主亨利三世/亨利四世（无对应类型，正文叙述）；两位女儿的母亲（无婚姻载）；Antoinette d'Aubeterre（雇主，同上）；Coligny/Condé 等（仅同处环境）

## 8. 奖项清单

- 无（page.md 无任何奖项记载——禁编造宫廷荣誉为奖项）

## 9. 机构清单

- 教育：University of Poitiers（普瓦捷大学，1558 入学、1559 LL.B.）
- 任职：Parlement of Rennes（雷恩高等法院，1573 参事）；Parlement of Paris（巴黎高等法院，1580 起 maître des requêtes，服务于王）；parlement at Tours（图尔高等法院参事，亨利四世时代）——入库取 Rennes 与 Paris 两机构

## 10. 终审清单

- [ ] 生卒 1540（仅年）/ 1603-02-23，享年 62–63，出生地 Fontenay-le-Comte、卒地 Paris
- [ ] metadata 死亡日期双值噪声已按 page.md 裁定为 1603-02-23
- [ ] 职业口径「律师/枢密顾问为本业、业余数学家」表述准确
- [ ] 辅音=已知/元音=未知、第一个符号代数、结束中世纪代数口径忠实 page.md
- [ ] π 无穷乘积「数学史上第一个」口径忠实 page.md
- [ ] 密码破译两朝 + 「魔法指控」按原文；Clavius 论战「据说韦达错了」不回避
- [ ] van Roomen「先挑战后成友」；Descartes influence 带未明限定
- [ ] 引语全部命中白名单；宗教段客观简述
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/François_Viète/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：优先 Meryon 1861 版画（`images.txt` 第 7 条 MET 图）；不可用则装饰圆占位并注明「后世版画缺肖像」
- [ ] **国籍**：封面顶部徽章明示「法兰西」
- [ ] **引语核对**：仅白名单五+一处引语，逐条在 page.md 找到原文
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次 Simon_Stevin 及 17 世纪卷（Johann_Bernoulli）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
