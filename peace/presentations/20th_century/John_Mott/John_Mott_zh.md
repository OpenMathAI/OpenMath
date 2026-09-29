# 和平奖得主立传提示词（OpenPeace 批次 9：John Raleigh Mott）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 John Raleigh Mott（约翰·雷利·马特，1946 诺贝尔和平奖得主、YMCA 与 WSCF 长期领袖）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用到任何和平奖得主；标注 `【人物专属】` 的部分需按目标人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构，移植到和平事业人物。
- **本实例**：John Raleigh Mott（约翰·雷利·马特，1865–1955），美国布道家、YMCA 与世界基督教学生同盟（WSCF）长期领袖。
- **设计哲学**：和平奖得主立传同样必须有「身份信息页」（Identity / Bio 速览页）与「事业领域」的结构化表达；Mott 的一生有「康奈尔学生 → 学生运动总干事 → 普世教会运动奠基者」的长弧叙事，以「跨国的宗教兄弟会」为思想主轴——把学生组织织成跨越国界的和平网络，这是本篇的灵魂。

---

## 二、背景信息 【人物专属】

- **目标人物**：John Raleigh Mott（1865-05-25 纽约州 Livingston Manor ~ 1955-01-31 佛罗里达州 Orlando，享年 89 岁）
- **气质关键词**：**学生运动的总建筑师、普世教会运动的奠基者、跨国的和平织网人** —— 1946 诺贝尔和平奖获奖理由：
  > "for his contribution to the creation of a peace-promoting religious brotherhood across national boundaries"（表彰他为创建跨越国界、促进和平的宗教兄弟会所做的贡献）
- **设计母题**：**跨越国界的兄弟会（brotherhood across borders）**。从 1895 年 WSCF 的成立、1910 年爱丁堡宣教会议的主席台，到 1948 年世界基督教教会联合会的创立——「组织网络即和平工程」是比「和平鸽」更贴合 Mott 的视觉语言。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/John_Mott/page.md`（含 frontmatter QID Q159726）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库要求**：研究领域（第 4 步）与社会关系（第 4.5 步）已按本提示词写入 `greatminds` 库（MySQL），Beamer 立传与其并行。

### 第 0 步：核对 Wikipedia 页面与事实基准 【人物专属】

- ✅ 已下载 `https://en.wikipedia.org/wiki/John_Mott` 四件套到 `peace/presentations/pages/20th_century/John_Mott/`（**第一轮已核对，事实基准如下**）：
  - 生卒（1865-05-25 生于纽约州 Sullivan County Livingston Manor ~ 1955-01-31 逝于佛罗里达州 Orlando，享年 89 岁；同年 9 月全家迁爱荷华州 Postville；葬华盛顿国家教堂）
  - 家庭（父 John Mott Sr.、母 Elmira née Dodge；1891 年娶教师 Leila Ada White，育二子二女；1952 年 Leila 去世，1953 年续娶 Agnes Peter 1880–1957）
  - 子女（Irene Mott Bose〔印度社会工作者，印度最高法院法官 Vivian Bose 之妻〕、Eleanor Mott Ross〔纽约 Poughkeepsie〕、John Livingstone Mott〔1931 获 Kaisar-i-Hind 银章，YMCA 印度事工〕、Frederick Dodge Mott〔加拿大医疗规划，加拿大驻世界卫生组织代表〕）
  - 教育（Upper Iowa University 攻读历史、获奖辩手；转学 Cornell University 1888 年获学士学位）
  - 任职（美国卫理公会平信徒；YMCA 与 WSCF 长期领袖；WSCF 总干事 1895–1920、主席 1920–1928）
  - 关键荣誉（Nobel Peace Prize 1946，与 Emily Greene Balch 共享；德国联邦功绩勋章指挥官十字〔frontmatter〕；2022 年列入美国圣公会圣历，纪念日 10-03）
  - 核心事业清单（①受 Arthur Tappan Pierson 影响投身学生志愿海外传教运动〔1886 创立〕②协助创立 WSCF 1895 并任总干事 25 年 ③主持 1910 世界宣教会议——现代新教传教运动与普世教会运动的里程碑 ④1912-10 ~ 1913-05 亚洲之行 18 场地区与全国会议（锡兰/印度/缅甸/马来亚/中国/朝鲜/日本）⑤1948 年世界基督教教会联合会（WCC）创立的深度参与者，被选为终身荣誉会长 ⑥1946 诺贝尔和平奖）
  - 关键时间线（15–20 节点，见第 6 步幻灯片序列）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `John_Mott/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目已有成品的 `Makefile`，设置 `MAIN=John_Mott_zh`、`VIDEO_NAME=John_Mott_zh`

### 第 3 步：收集图片 【人物专属】

- ⚠️ 本地 `images.txt` **无单独肖像**——可用集体照插图：
  - `U.S._Mexico_Commission_in_1916.jpg`（1916-09-09 美墨委员会，坐者左一为 Mott）——作插图页，图注写明「坐者左一 John Mott」
- 封面与身份信息页用**装饰圆占位**（主色环 + 姓名首字母或地球经纬意象）；勿把 Commons/Wikisource 徽标误作肖像

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

> 把研究领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。以下 4 条已入库。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | ecumenical movement | 普世教会运动 | 1910 宣教会议主持、1948 WCC 创立与终身荣誉会长 | 普世页 |
| 1 | international student movement | 国际学生运动 | WSCF 总干事 1895–1920、主席 1920–1928；YMCA 领袖 | 学生运动页 |
| 2 | protestant missions | 新教传教运动 | 1910 世界宣教会议、亚洲 18 场会议、《在本代将福音传遍世界》 | 宣教页 |
| 3 | religious peace work | 宗教和平事业 | 建立并强化促进和平的国际新教学生组织（诺奖理由口径） | 诺奖页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 以下 11 条与 yaml 完全一致，已入库（仅收 page.md 明载关系）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Emily Greene Balch | 无向 | 1946 诺贝尔和平奖共同得主 |
| influence | Arthur Tappan Pierson | 无向 | 影响其投身海外传教；学生志愿运动（1886 创立）推动者 |
| colleague | Robert Hallowell Gardiner III | 无向 | 俄国革命后共同维系与俄罗斯正教会及 Tikhon 主教的关系 |
| spouse | Leila Ada White | 无向 | 1891 结婚，育二子二女；1952 去世 |
| spouse | Agnes Peter | 无向 | 1953 续弦；Martha Custis Washington 后裔 |
| parent-child | John Mott Sr. | 无向 | 父亲 |
| parent-child | Elmira Dodge Mott | 无向 | 母亲（née Dodge） |
| parent-child | Irene Mott Bose | 无向 | 长女，印度社会工作者 |
| parent-child | Eleanor Mott Ross | 无向 | 次女，纽约 Poughkeepsie |
| parent-child | John Livingstone Mott | 无向 | 长子，YMCA 印度事工，1931 Kaisar-i-Hind 银章 |
| parent-child | Frederick Dodge Mott | 无向 | 次子，加拿大医疗规划，驻世界卫生组织代表 |

- 方向约定：influence/spouse/parent-child/co-honored/colleague 均无向自动 from<to 归一
- 对手方 name_en 用 manifest 规范名；缺失人物由 seed_person.py 自动建占位记录

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：热忱、行旅、组织家的秩序感
- **配色**：深墨绿（manifest 预分配主色 `#0B5351`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeWSCF` 学生运动 — 靛蓝 `#2E4A7D`
  - `badgeEcumen` 普世教会运动 — 深紫 `#52307C`
  - `badgeMission` 宣教与亚洲行 — 赭金 `#8C6A2F`
  - `badgeNobel` 1946 诺奖 — 香槟金 `#C9A227`
- **背景母题**：柔和气泡 + 低饱和的航海航线与分部节点连线意象，呼应「跨越国界的兄弟会」的设计母题

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面有视觉主体**：右上角装饰圆占位（主色环 + 姓名首字母或地球意象），`draw=coveraccent!50` 细边框。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍（United States），底部状态栏给出 `国籍 | 事业 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧装饰圆 + 右侧信息网格，含至少：生卒、出生地、国籍、家庭（父母/两任妻子/子女）、教育（Upper Iowa/Cornell）、任职（YMCA/WSCF 年份）、主要荣誉、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 跨国兄弟会的织网人 / John Raleigh Mott 1865–1955 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右信息网格（含家庭、教育、任职、荣誉、核心领域）
03  核心贡献概览 — WSCF / 1910 宣教会议 / 亚洲之行 / WCC / 1946 诺奖
04  早年：从 Livingston Manor 到 Postville (1865–1888) — 爱荷华少年、Upper Iowa 获奖辩手、Cornell 1888
05  志愿运动的召唤 (1886–1895) — Arthur Tappan Pierson 影响、学生志愿海外传教运动
06  WSCF 总干事二十五年 (1895–1920) — 协助创立 1895、跨国学生组织网络、1920–1928 任主席
07  泰坦尼克上的缺席者 (1912) — 与同行者婉拒 White Star Line 赠票、改乘 SS Lapland、时人记述的感言
08  亚洲十八城 (1912–1913) — 锡兰/印度/缅甸/马来亚/中国/朝鲜/日本 18 场地区与全国会议
09  1910 世界宣教会议 — 爱丁堡、现代传教运动与普世教会运动的里程碑、Mott 主持
10  俄国企图与教会纽带 — 俄国革命后与 Gardiner 共同维系俄罗斯正教会关系（客观呈现）
11  世界基督教教会联合会 (1948) — 创立的深度参与者、终身荣誉会长
12  1946 诺贝尔和平奖 — 与 Emily Greene Balch 共享、获奖理由、平信徒得奖者的意义
13  晚年与遗产 — 两任婚姻与四个子女的事业、2022 圣历纪念日、Postville 中学以其命名、Yale 文书档案
14  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【模板通用 + 人物专属】

**版式**：每页 `\newcommand{\xxxslide}{...}`；每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

**Mott 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖理由拆分 | 1946 与 Balch 共享但**理由各写各的**——Mott 用 "for his contribution to the creation of a peace-promoting religious brotherhood across national boundaries"，勿混入 Balch 的毕生和平工作句 |
| 共享获奖者 | 与 Balch 事业互不隶属（一位是 YMCA/WSCF 领袖、一位是 WILPF 经济学者），勿写「与 Balch 合作获奖」 |
| YMCA 口径 | Mott 是 YMCA 的**长期领袖**（infobox 描述误称 founder of the YMCA——YMCA 1844 年创于伦敦，勿沿用该口径）；「帮助创立」的明确对象是 WSCF（1895）、1910 宣教会议、WCC（1948） |
| 泰坦尼克引语 | "The Good Lord must have more work for us to do." 系 C. Howard Hopkins 传记转述的时人记述，引用时注明「据 Hopkins 传记」；勿写成 Mott 自传原话 |
| 两任妻子年份 | Leila Ada White 1891 结婚、1952 去世；Agnes Peter 1953 续娶（1880–1957）——勿混淆 |
| 子女口径 | page.md 明确「two sons and two daughters」并列四人姓名与事业；勿增删人数 |
| 教会关系 | 与俄罗斯正教会的维系是「maintain relations with the Russian Orthodox Church and Archbishop Tikhon after the Russian Revolution」的 page.md 口径，客观记录；宗教与政治内容一律不加评价 |
| 同名区分 | 本篇是 John Raleigh Mott（1865–1955）；勿与库内其他 Mott 同名记录混淆 |
| 无载禁写 | 不编造博士导师（无研究生学历记载）、不从诺奖颁奖词反推关系、1916 美墨委员会仅作插图说明不展开叙事、不写 1948 年后 WCC 内部事务细节 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| WSCF | 世界基督教学生同盟 | World Student Christian Federation，1895 协助创立 |
| YMCA | 基督教青年会 | Mott 是长期领袖，非 1844 年创会者 |
| World Missionary Conference (1910) | 1910 世界宣教会议 | 爱丁堡，Mott 主持 |
| World Council of Churches | 世界基督教教会联合会 | 1948 创立，终身荣誉会长 |
| ecumenical movement | 普世教会运动 | 与传教运动（missions movement）互为表里但概念不同 |
| Student Volunteer Movement | 学生志愿海外传教运动 | 1886 创立，Pierson 为推动者 |
| layperson | 平信徒 | 卫理公会平信徒身份，非神职人员 |
| The Evangelization of the World in This Generation | 《在本代将福音传遍世界》 | 1900，20 世纪初的传教口号来源 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Ascension** — Cold Cinema（manifest 预分配，勿改）
- **风格**: 上行 / 恢弘 / 终章感
- **匹配理由**:
  - "Ascension" 呼应 Mott 的事业轨迹——从爱荷华小城的学生辩手到 1948 年普世教会运动的终身荣誉会长，每一步都是组织与视野的攀升
  - 曲名的上行感匹配其「织网」气质：25 年 WSCF 总干事、18 场亚洲会议、50 余年跨国行旅，网络在攀升中铺开
- **本地路径**: `music_audio/inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav` → `presentations/20th_century/John_Mott/Ascension.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/John_Mott/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/pages/20th_century/John_Mott/images.txt` | 插图 URL（无单独肖像，用装饰圆占位） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄，勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/John_Mott.yaml` | 社会关系/领域入库母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
