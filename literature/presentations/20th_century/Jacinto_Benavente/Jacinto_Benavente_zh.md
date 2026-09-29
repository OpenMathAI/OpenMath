# 文学家立传提示词（OpenLiterature 实例：Jacinto Benavente）

## 一、模板定位

- **目标项目**：OpenLiterature —— 诺贝尔文学奖得主人物史（OpenMathAI 共享仓库）。
- **本实例**：Jacinto Benavente（哈辛特·贝纳文特，1922 诺贝尔文学奖，20 世纪西班牙戏剧复兴旗手）。
- **设计哲学**：文学家立传以「作品意象 + 名句引文框/舞台图式」替代公式框；身份信息页与领域结构化表达保留。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Jacinto Benavente y Martínez（1866-08-12 生于马德里 ~ 1954-07-14 卒于 Aldeaencabo de Escalona（Toledo 省），享年 87 岁）
- **1922 官方获奖理由**（禁止改写）：
  > EN: "for the happy manner in which he has continued the illustrious traditions of the Spanish drama"
  > 中译（CITATION_ZH, key=("1922","Jacinto Benavente")）：表彰其以精妙的方式延续了西班牙戏剧的辉煌传统
- **气质关键词**：**剧场革新者、社会风俗的解剖者、假面喜剧的宗师**
- **设计母题**：**面具与丝绳（Comedy of Masks）**。其最著名作《Los intereses creados》以意大利即兴喜剧面具群演「利益牵着世界走」——以假面、提线与舞台框为视觉母题。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Jacinto_Benavente/page.md`（事实基准）
  - `literature/presentations/pages/20th_century/Jacinto_Benavente/metadata.json`、`images.txt`
  - Wikipedia URL：https://en.wikipedia.org/wiki/Jacinto_Benavente
  - 肖像（第 0 步待下载）：**page.md/images.txt 无真实肖像**（仅马德里丽池公园雕像照片 Retiro_Park_Statues）——无肖像则用装饰圆占位；雕像照可作插图页但不可充肖像

---

## 三、任务流程 【逐步执行，每步汇报】

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- **生卒**：1866-08-12 生于马德里；1954-07-14 卒于 Aldeaencabo de Escalona（Toledo 省），享年 87 岁（注意：infobox 死亡地为 Toledo 省村镇，非马德里）
- **国籍**：西班牙
- **家庭**：马德里著名儿科医生之子；**终身未婚**；据多方记载为同性恋者（page.md 口径 "According to many sources"——转述须保留限定语）
- **教育**：Complutense University of Madrid（frontmatter educated_at；正文未展开——提示词按 frontmatter 一笔带过即可）
- **文学师承与影响**：page.md 无师承记载（勿编造）；其革新对象明确——以散文与心理对话取代宣言式韵文与情节剧
- **关键荣誉**：Nobel 1922；frontmatter 另载「马德里爱子」（Dearest Son of Madrid）、Alfonso 十二/十三世民事勋章大十字、劳动功绩金奖章等
- **核心作品与贡献（4–6 条）**：
  1. 《El nido ajeno》（1894）——三幕喜剧，剧坛登场
  2. 《Gente conocida》（1896）——上流社会讽刺四幕
  3. 《Los intereses creados》（1907）——假面喜剧，意大利即兴喜剧底色，**最著名且常演**之作
  4. 《Señora ama》（1908）——乡村剧，嫉妒主妇的心理剖析
  5. 《La malquerida》（1913）——乡村心理剧三幕，1921 改编电影 The Passion Flower（Norma Talmadge 主演）
  6. 一生共写 **172 部剧作**（page.md 明载总数）
- **戏剧革新主张**：「让戏剧回到现实」——宣言式韵文让位于散文、情节剧让位于喜剧、程式让位于经验、冲动动作让位于对话与心智交锋；早年关心美学，后期转向伦理
- **关键时间线（15 节点）**：
  1. 1866-08-12 生于马德里，儿科医生之家
  2. 就读 Complutense University of Madrid
  3. 1894 《El nido ajeno》
  4. 1896 《Gente conocida》
  5. 1901 《La Gobernadora》
  6. 1903 《La noche del sábado》
  7. 1905 《Rosas de otoño》
  8. 1907 《Los intereses creados》——代表作
  9. 1908 《Señora ama》
  10. 1909 《El príncipe que todo lo aprendió en los libros》
  11. 1913 《La malquerida》
  12. 1916 《La ciudad alegre y confiada》（《Los intereses creados》续篇）与《Campo de armiño》
  13. 1922 获诺贝尔文学奖
  14. 1936 名字被民族派报纸假新闻牵入洛尔卡遇害事件（本人无涉）
  15. 1954-07-14 卒于 Aldeaencabo de Escalona，享年 87
  16. 丽池公园立纪念雕像（后世纪念）

### 第 1 步：建立目录 【模板通用】

- 创建 `literature/presentations/20th_century/Jacinto_Benavente/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 设 `MAIN=Jacinto_Benavente_zh`、`VIDEO_NAME=Jacinto_Benavente_zh`

### 第 3 步：收集图片 【人物专属】

- 无真实肖像（images.txt 仅雕像/站点图标）：主肖像用**装饰圆占位**；Retiro 公园雕像照与《Rekopis》类书影可作插图页素材（图注注明非肖像）

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | modern Spanish drama | 现代西班牙戏剧 | 获奖理由核心「延续西班牙戏剧传统」 | 核心页 |
| 1 | social comedy | 社会喜剧 | 上流社会与风俗讽刺 | 讽刺页 |
| 2 | psychological drama | 心理剧 | 对话与心智交锋取代动作 | 心理页 |
| 3 | rural drama | 乡村剧 | Señora ama / La malquerida | 乡村页 |

- 入库：`MySQL/data/Jacinto_Benavente.yaml` → `python3 seed_person.py data/Jacinto_Benavente.yaml`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| controversy | Federico García Lorca | 无向 | 1936 民族派报纸（Estampa 等）伪造「洛尔卡之死系为贝纳文特报仇」假新闻；本人与案无涉，仅名字被牵连 |

**说明（诚实值）**：page.md 极简——无师承、无同人社、无婚姻（终身未婚），可入库社会关系仅此一条；relations=1 属「实在无载」的例外情形，汇报时注明。**禁写**：法朗哥政权态度只客观一句（reluctant supporter as only viable alternative——转述其原话立场，不作政治评价）；同性恋记载用转述限定语，不渲染；「与社会主义论战」不建 rival 关系（对手方未具名）。

### 第 5 步：设计配色方案 【人物专属】

- **主色**：#1E4E79（马德里蓝——剧场正色）+ 诺奖香槟金 `C9A227`
- **badgeA** 现代西班牙戏剧 — 蓝 `#1E4E79`；**badgeB** 社会喜剧 — 琥珀 `#E07B30`；**badgeC** 心理剧 — 玫瑰 `#C4204F`；**badgeD** 乡村剧 — 青绿 `#0E7C7B`
- **背景母题**：假面与提线剪影 + 舞台框线条（呼应 Los intereses creados）

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页（共享封面 \input）
01  封面 — 西班牙戏剧传统的续写者 / Jacinto Benavente 1866–1954 + badge + 国籍行
02  身份信息页（★ 必做）— 装饰圆占位 + 信息网格（生卒、教育、医生之子、未婚、荣誉）
03  核心贡献概览 — 现代西班牙戏剧 / 社会喜剧 / 心理剧 / 乡村剧
04  马德里起步（1866–1894）— 医生之子、革新宣言
05  早期讽刺（1894–1905）— El nido ajeno / Gente conocida / La Gobernadora
06  代表作：Los intereses creados（1907）— 假面喜剧（舞台图式页）
07  乡村与心理（1908–1913）— Señora ama / La malquerida（含 1921 电影改编）
08  高产世纪（1916–1954）— 172 部剧作的长跑（选段表）
09  1922 诺贝尔奖 — 官方获奖理由 EN + 中译
10  争议页 — 1936 洛尔卡假新闻事件（客观还原，注明本人无涉）
11  晚年与身后 — Toledo 省辞世、丽池公园雕像
12  遗产：西班牙剧场的现代化
13  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 身份信息页用装饰圆变体（无肖像）；代表作用舞台图式/书影框

### 第 8 步：布局检查 【模板通用】

- 每页 make + pdftoppm 目检；修复优先级同标杆

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Benavente 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 死亡地 | infobox 作 Aldeaencabo de Escalona（Toledo 省），勿写成马德里 |
| 172 部 | page.md 明载 wrote 172 works，勿写成「百余部」或夸大 |
| 洛尔卡事件 | 是报纸**假新闻**将其名牵连；本人未参与、无指控成立——措辞必须「名字被牵连」 |
| 政治立场 | 自由派君主主义者、社会主义批评者、法朗哥的勉为其难支持者——只按原文客观一句，不作政治评价 |
| 私生活 | 终身未婚；同性恋记载用「according to many sources」限定转述 |
| 获奖理由 | 官方强调「happy manner…continued the illustrious traditions」，勿改写为「开创」——他是延续者 |
| 无肖像 | 严禁拿雕像照、公园照充当肖像 |
| La malquerida 电影 | 1921 年 The Passion Flower，Norma Talmadge 主演，勿写成年份/人名错位 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| comedy of masks | 假面喜剧 | Los intereses creados 的体裁定位 |
| commedia dell'arte | 意大利即兴喜剧 | 1907 名作的底色 |
| social criticism | 社会批评 | 其戏剧革新核心 |
| declamatory verse | 宣言式韵文 | 被他革新的旧传统 |
| melodrama | 情节剧 | 同上，勿译成「音乐剧」 |
| rural drama | 乡村剧 | Señora ama / La malquerida |
| stage romance | 舞台罗曼司 | La noche del sábado 副体裁 |
| psychological study | 心理剖析 | Señora ama 的定位原文 |
| Spanish drama | 西班牙戏剧 | 获奖理由关键词 |
| Retiro Park | 丽池公园 | 纪念雕像所在 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**The Flow of Time**（分批文件预分配）
- **匹配理由**：1866–1954 近九十年人生、172 部剧作的漫长写作生涯，是「时间之流」的最好注脚；曲名的绵延感匹配「延续西班牙戏剧辉煌传统」的获奖理由——他不是断裂的革新者，而是传统的精妙续写者。
- **本地路径**：按 `music_audio/curated_tracks.md` 对应文件复制为本目录 `The Flow of Time.wav`
- **时长**：以曲目实际长度与成片页数对齐（ffmpeg `-shortest`）
