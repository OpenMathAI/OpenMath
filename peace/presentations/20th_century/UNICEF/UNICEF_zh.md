# 诺贝尔和平奖得主立传提示词（UNICEF，1965）

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享仓库，与 physicist/chemist/medic/literature 侧同构）。
- **本篇对象**：联合国儿童基金会 United Nations Children's Fund（UNICEF），1965 年诺贝尔和平奖得主，**本篇是组织机构条目（is_org=true）**。
- **设计哲学**：机构立传不做"生平叙事"，而做"使命叙事"——从二战救济的临时应急基金到覆盖 190 多个国家和地区的常设联合国机构，以"儿童优先"为贯穿母题；第 6 步用「机构概览页」替代人物身份信息页。

## 二、背景信息 【人物专属】

- **机构全称**：United Nations Children's Fund（UNICEF），原名 United Nations International Children's Emergency Fund（联合国国际儿童紧急基金会），1953 年起用现名但保留缩写；中文：联合国儿童基金会
- **成立**：1946-12-11，纽约，联合国大会第 57(I) 号决议设立
- **1965 年诺贝尔和平奖，官方获奖理由（EN 原文照抄 Nobel 名录，禁止改写）**：
  > "for its effort to enhance solidarity between nations and reduce the difference between rich and poor states."
  > 中译（照抄 `OpenPeace_20th_Century_Nobel_Laureates.md`）：表彰其为增进国家间团结、缩小贫富国家差距所做的努力
- **气质关键词**：**战火中的儿童守护者、从紧急救济到长期发展、全球最大的人道主义品牌之一**
- **设计母题**：**橙色补给箱（School in a box）**——从战后食品衣物配给到"一盒一师四十生"的便携学校，视觉语言用救援物资箱、地球、儿童剪影。
- **本地数据源**：`peace/presentations/pages/20th_century/UNICEF/page.md`（Wikipedia 全文 + frontmatter）

## 三、任务流程

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 成立时间：1946-12-11（infobox 明载"11 December 1946"）；1953 年成为联合国体系常设机构并改现名
- 性质：联合国机构（UN agency），总部纽约；2024 年收入 86.1 亿美元（公共部门伙伴 49.2 亿）
- 创始人：Ludwik Rajchman（波兰公共卫生专家，infobox Founder + See also 明载 "founder of UNICEF and its first Chairman"）
- 首任执行主任：Maurice Pate（Rajchman 选定，page.md 明载）
- 其他明载人物：Fiorello La Guardia、Herbert Hoover（支持决议）；James P. Grant（第三任执行主任，See also 明载）
- 覆盖范围：192 个国家和地区；150 个国家办公室、7 个地区办公室、34 个国家委员会；员工 15,354（2024）
- 关键荣誉：Nobel Peace Prize 1965；Indira Gandhi Prize 1989；Princess of Asturias Award 2006；Wateler Peace Prize；Atatürk International Peace Prize
- 核心事业清单：①免疫接种与疾病预防 ②儿童与母亲 HIV 治疗 ③儿童与母婴营养 ④环境卫生改善 ⑤教育促进 ⑥灾难紧急救援
- 关键时间线（15–20 节点）：1943 Rajchman 提议国际卫生服务 → 1946-12-11 联大 57(I) 决议成立（UNRRA 主持创建）→ 1946 首批救济二战受害儿童与母亲 → 1948 UNRRA 解散、Rajchman 提议以剩余资金开展儿童喂养计划 → 1950 费城儿童万圣节募捐（$17）开启 Trick-or-Treat 传统 → 1950 授权扩展至发展中国家儿童与妇女长期需求 → 1953 成为联合国体系常设机构、更名 United Nations Children's Fund → 1950s 起 Supply Division（哥本哈根+纽约）→ 1965 诺贝尔和平奖（12 月 11 日诺奖演讲 *UNICEF: Achievement and Challenge*）→ 1988 Innocenti 研究中心（佛罗伦萨）成立 → 1989 Indira Gandhi Prize → 1994 Cartoons for Children's Rights 动画峰会 → 2006 Princess of Asturias Award；FC Barcelona 首次俱乐部赞助机构 → 2015 Kid Power 计划 → 2018 年度数据：协助接生 2700 万婴儿、为 6550 万儿童接种五联疫苗、1200 万儿童获得教育、400 万重度急性营养不良儿童获治、90 国 285 起人道紧急响应 → 2024 收入 86.1 亿美元

### 第 4 步：使命领域梳理 + 入库 【与 yaml fields 完全一致】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | humanitarian aid | 人道主义援助 | 机构使命核心，战后人道救济起家 |
| 1 | child welfare | 儿童福利 | 儿童健康、营养、保护的长期纲领 |
| 2 | public health | 公共卫生 | 免疫接种、HIV 治疗、妇幼健康 |
| 3 | emergency relief | 紧急救援 | 灾害与冲突响应，2018 年 90 国 285 起 |
| 4 | children's education | 儿童教育 | 学校教育促进与 School in a box |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml relations 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| founder | Ludwik Rajchman | 创始人→机构 | 波兰公共卫生专家，首任主席 |
| colleague | Maurice Pate | 无向 | Rajchman 选定的首任执行主任 |
| colleague | James P. Grant | 无向 | 第三任执行主任 |
| other | United Nations | 无向 | 联大 1946 年决议设立，1953 年成为常设机构 |
| other | United Nations Relief and Rehabilitation Administration | 无向 | 1946 年由 UNRRA 主持创建 |

- 入库规则：org 条目无 gender/nationalities；`type: other` 用于联合国体系隶属与 UNRRA 创建来源（工作流第 2 节）。

### 第 5 步：设计配色方案 【manifest 预分配，勿改主色】

- **主色**：`#5C3A1E`（深棕——救援箱与大地色，机构的物资与田野气质）
- **辅助**：诺奖香槟金 `#C9A227` + 四分类色（badgeA–D 自定语义）：
  - badgeA 人道救援 — 赭石 `#B4552D`
  - badgeB 儿童福利 — 天蓝 `#3A7CA5`
  - badgeC 公共卫生 — 橄榄绿 `#6A8532`
  - badgeD 紧急响应 — 玫瑰 `#C4204F`
- **背景母题**：柔和圆点（呼应地球与补给箱圆角），稀疏大圆错落。

### 第 6 步：幻灯片序列（10–16 页规划）

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 联合国儿童基金会 / UNICEF · 1965 诺贝尔和平奖 + 四色 badge + 机构徽记位
02  机构概览页（★ 替代身份信息页）— 成立/总部/性质/规模/使命六格信息
03  使命概览 — 人道援助 / 儿童福利 / 公共卫生 / 紧急救援 / 教育
04  缘起：战火中的儿童 (1943–1946) — Rajchman 提议、UNRRA、联大 57(I) 决议
05  创建者 Ludwik Rajchman 与首任执行主任 Maurice Pate
06  从应急基金到常设机构 (1946–1953) — 授权扩展、更名、进联合国体系
07  机构概览：治理与网络 — 36 人执行局、150 国办公室、7 地区办、34 国别委员会
08  核心事业 — 免疫/营养/教育/紧急救援六领域
09  全球供给线 — Supply Division（哥本哈根/纽约）、School in a box、世界仓库
10  募捐与公众参与 — Trick-or-Treat（加拿大 C$9100 万/美国 US$1.67 亿）、国别委员会
11  1965 诺贝尔和平奖 — 官方理由原文 + 中译 + 12-11 诺奖演讲
12  数据里的 UNICEF — 2018 年度六项数字、2024 收入
13  荣誉与认可 — Nobel 1965 · Indira Gandhi 1989 · Asturias 2006
14  遗产：一个为儿童的机构
15  结尾
```

### 第 7 步：版式要点 【模板通用骨架 + 人物专属】

- 每页 `\newcommand{\xxxslide}{...}`；机构概览页参照成品 `\profileslide` 双栏信息网格实现。
- 配色宏统一 `mainclr/accentclr/badgeA..D/panelA..D`，注释写语义。
- 表格页安全负间距：顶部 -0.35cm、`arraystretch 0.78–0.82`。

### 第 8 步：本机构专属陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 名称演变 | 1946 全称 United Nations International Children's Emergency Fund，1953 年改现名但保留 UNICEF 缩写；"C stands for children" 口号可写 |
| 创始人归属 | Founder=Ludwik Rajchman（infobox+See also 双处明载）；**勿把执行主任/领导人（Pate/Russell 等）写成创始人** |
| 成立日期 | 1946-12-11（联大 57(I) 决议）；勿写 UNRRA 解散的 1948 |
| 隶属关系 | UNICEF 是联合国机构（联大设立、经社理事会治理），非独立 NGO；34 国别委员会是独立 NGO 但隶属 UNICEF 募捐体系 |
| 名录口径 | 名录 country 列写 "International organization"，诺奖 citation 主语是 "its"（机构） |
| 争议内容 | page.md 载 Controversies（肯尼亚 1995 挪用、德国 2008、刚果金 2018/2020 性侵指控等）：只可作客观事实简述或不写，**禁作评价性引申**；英国 2020 食品资助涉英国政党言论，**政治敏感，整段禁用** |
| 数字口径 | 2018 年六项年度数据与 2024 年收入是两组口径，勿混；"操作于 192 国家和地区"与"191 国"两说，以正文 192 为准 |
| 赞助史实 | FC Barcelona 2006 起赞助是"俱乐部赞助机构"（首次反向），方向勿写反 |
| 无载禁写 | page.md 未载的历任执行主任名单、内部预算明细、对某国政策评价一律不写 |

### 第 9 步：术语清单

| 英文 | 中文 | 风险点 |
|------|------|------|
| United Nations Children's Fund | 联合国儿童基金会 | 1953 前勿用现名 |
| UNRRA | 联合国善后救济总署 | 创建推动方，勿写"母组织" |
| executive board | 执行局 | 36 国政府代表，非秘书处 |
| national committee | 国家委员会 | 34 个独立 NGO，募捐职能 |
| Supply Division | 供应司 | 哥本哈根+纽约双基地 |
| School in a box | 一盒学校 | 1 师 + 40 生教具箱 |
| Trick-or-Treat for UNICEF | 万圣节募捐 | 1950 费城 $17 起源 |
| Innocenti Research Centre | 因诺琴蒂研究中心 | 1988，佛罗伦萨 |
| pentavalent vaccine | 五联疫苗 | 2018 年 6550 万儿童 |
| humanitarian emergency | 人道紧急事件 | 2018 年 90 国 285 起 |

---

## 四、背景音乐 ✅ 【manifest 预分配，勿改】

- **选定曲目**：**Eternals** — Alex-Productions
- **匹配理由**："宏大/深远" 匹配机构横跨 80 年、覆盖 190+ 国的持续使命；1965 年获奖至今的长期人道纲领与"Eternals"的永恒气质天然契合。
- **本地路径**：`music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/UNICEF/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

---

## 六、执行清单

1. 建 `peace/presentations/20th_century/UNICEF/` 目录 + `images/`；下载机构徽记/项目照片（images.txt 无 URL 则用装饰圆占位，机构无肖像）。
2. 复制同项目已完成的 Beamer Makefile，设 `MAIN=UNICEF_zh`、`VIDEO_NAME=UNICEF_zh`。
3. 按 §三 第 6 步序列写 tex；每写一页 make 检查溢出（vbox≤10pt、hbox≤50pt）。
4. `pdftoppm` 逐页目检 → make images/video。
5. yaml 入库：`cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/UNICEF.yaml`；验证 has_social_data=1。

---

## 七、版式补遗

- 机构条目封面无个人肖像：用机构徽记/地球图形 + 装饰圆占位，图注写明"机构徽记位"。
- 结尾页底部品牌统一 `OpenMathAI`；引号用半角 `" "`。
- \foreach 时间线分隔符必须 ASCII 逗号；宏名禁数字。
