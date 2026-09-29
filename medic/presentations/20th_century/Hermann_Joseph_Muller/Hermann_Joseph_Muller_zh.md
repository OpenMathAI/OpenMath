# 医学家立传提示词（Hermann Joseph Muller）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1946 年得主 Hermann Joseph Muller 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Hermann_Joseph_Muller/page.md`（唯一事实来源，metadata.json 仅作参考）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（11 节合并为 9 节）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Hermann Joseph Muller（1890-12-21 生于美国纽约 ~ 1967-04-05 逝于印第安纳州印第安纳波利斯，享年 76 岁）
- **气质关键词**：**X 射线诱变的发现者、辐射遗传学的奠基人、核时代最早的预警者** —— 1946 年诺贝尔生理学或医学奖（独享）获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for the discovery of the production of mutations by means of X-ray irradiation"（因其发现用 X 射线照射产生突变）
- **设计母题**：**X 射线下的突变之雨（a rain of mutations）**。X 射线扫过果蝇，隐性的致死突变在雄性后代身上现形——突变第一次从"自然发生"变成"可以制造"。视觉语言：射线束、果蝇谱系树上突然分叉的红点。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Hermann_Joseph_Muller/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1890-12-21 生于纽约（父为金属工匠；先祖来自德国科布伦茨；母系英裔犹太/圣公会背景）
  - 16 岁入哥伦比亚学院；1910 获文学士（BA）
  - 早期接受孟德尔-染色体遗传理论；组建生物社团；一度是优生学支持者
  - 1912 正式加入摩尔根果蝇实验室（此前两年非正式参与；贡献多为理论与预言，因按"结果"计功而自觉受排挤）
  - 1911-1912 在康奈尔研究代谢
  - 1914 Julian Huxley 邀其赴休斯敦 Rice 研究所任教；1915-16 学年上任（学位 1916 补发）
  - 1918 提出 "balanced lethals" 解释月见草突变论；同年受摩尔根召回回哥伦比亚任教
  - 1919 发现交叉抑制突变株（ClB，后知为染色体倒位）
  - 1920-1932 任德克萨斯大学教授；1923 与 Jessie Marie Jacobs 结婚
  - 1923 起使用镭与 X 射线；1926-11 两组剂量实验确立辐射-致死突变定量关系
  - 1927 柏林第五届国际遗传学大会宣读论文，引发轰动；1928 他人于黄蜂/玉米等重复验证
  - 1932 第三届国际优生学大会演讲（H. Bentley Glass 评：几乎终结了优生学会的活动）
  - 1932-09 赴柏林与 Timofeeff-Ressovsky 合作；结识 Bohr 与 Delbrück；因《火花报》事件受 FBI 关注
  - 1933 赴苏联列宁格勒（后莫斯科）建立果蝇实验室；1935 离婚；《Out of the Night》出版
  - 反对李森科主义；斯大林读后下令组织批判，1937 被迫离开
  - 1937-09 携 250 个果蝇品系赴爱丁堡大学；1939-05 娶 Dorothea "Thea" Kantorowicz；1938 撰《遗传学家宣言》
  - 1940 回美任 Amherst 学院无终身教职；曼哈顿计划顾问（不知项目真名）与雷达突变研究
  - 1945 任印第安纳大学动物学教授
  - 1946 获诺贝尔生理学或医学奖（广岛长崎之后，公众聚焦辐射危险）；诺奖演讲提出无阈值剂量→线性无阈值（LNT）模型
  - 1942 美国艺术与科学院；1947 美国哲学学会；1955 Kimber 遗传学奖；1958 Darwin-Wallace 奖章
  - 1955 联署 Russell-Einstein 宣言（11 人之一）；1958 联署 Pauling 致联合国请愿
  - 1956-1958 任美国人道主义协会主席；1963 Humanist of the Year；1958 Gibbs 讲席（美国数学学会）
  - 1964 退休；果蝇染色体臂以 "Muller elements" 命名
  - 1967-04-05 卒于印第安纳波利斯

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Hermann_Joseph_Muller/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Hermann_Joseph_Muller/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Hermann_Joseph_Muller_zh`
> - 肖像：正文含 1952 年肖像（infobox 图）缩略 URL（250px 改 500px，curl 加 `-A "Mozilla/5.0"`，file 验证）；404 用 Commons `Special:FilePath` 回退；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | genetics | 遗传学 | 诺奖核心：X 射线诱变（infobox Fields 之一） | 核心页 |
| 1 | molecular biology | 分子生物学 | 基因的物理本性与预言（infobox Fields 之一；Haber 回顾） | 遗产页 |
| 2 | mutagenesis | 诱变 | 辐射与致死突变的定量研究、自发突变率测量 | 核心页 |
| 3 | radiation genetics | 辐射遗传学 | 辐射危险预警与 LNT 模型 | 公共政策页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Hermann_Joseph_Muller.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Thomas Hunt Morgan | 师→生 | 哥伦比亚摩尔根果蝇实验室（1912 加入），1916 博士 |
| advisor-student | Charlotte Auerbach | 生→ | 博士生（infobox 明载） |
| advisor-student | H. Bentley Glass | 生→ | 博士生，优生学史评述者 |
| advisor-student | Clarence Paul Oliver | 生→ | 博士生（infobox 明载） |
| advisor-student | Elof Axel Carlson | 生→ | 博士生 |
| advisor-student | Wilson Stone | 生→ | 博士生（infobox 明载） |
| advisor-student | Guido Pontecorvo | 生→ | 博士生（infobox 明载；勿与库内 Bruno Pontecorvo 混同） |
| advisor-student | George D. Snell | 生→ | 博士后研究员（后获 1980 诺奖） |
| collaborator | Edgar Altenburg | 无向 | 终生挚友与合作者（致死突变、修饰基因论文） |
| colleague | Nikolay Timofeeff-Ressovsky | 无向 | 1932 柏林共事（辐射遗传学） |
| controversy | Trofim Lysenko | 无向 | 在苏联抵制李森科主义，1937 被迫离开（库内 id=3041） |
| spouse | Jessie Marie Jacobs | — | 1923 结婚（数学教授），1935 离异 |
| spouse | Dorothea Kantorowicz | — | 1939 结婚，德国犹太难民 |
| parent-child | David E. Muller | — | 子，数学家与计算机科学家（2008 卒） |
| parent-child | Helen J. Muller | — | 女，新墨西哥大学荣休教授 |

**不入库裁定**：Alfred Kroeber、Ursula K. Le Guin、Herbert J. Muller 系表亲（cousin 无白名单类型）不入库；Niels Bohr 与 Max Delbrück 仅"在柏林结识"不入库；Julian Huxley（ Rice 职位邀请人）、Otto C. Glaser（Amherst 系主任）、Richard Goldschmidt（基因存在之辩——学术论战非私人恩怨）、Linus Pauling（请愿共同联署）、Rachel Carson（引用其观点）、James F. Crow（LNT 批评者）均不入库；Carl Sagan（本科在其实验室打工）、Raissa L. Berg（notable former students 列表有载）——Sagan 按"本科生打工"不入库，Berg 与 infobox 六博士生重复性低，为防噪声亦不入库（陷阱表注明）。

## 五、配色方案 【人物专属】

- **气质**：锋利、忧郁、先知式的孤独（摩尔根实验室的"理论者"、辐射时代的第一声警报）
- **主色**：诱变深紫 `#4E2A84`（与人物气质呼应——X 射线的不可见锋芒与遗传谱系上的突变之点）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 遗传学（诱变）——突变红 `#B03A2E`
  - `badgeB` 分子生物学——基因青 `#2E7D6B`
  - `badgeC` 辐射遗传学——射线黄 `#C89B3C`
  - `badgeD` 公共政策——警报橙 `#B4632A`
- **背景母题**：射线束与谱系树分叉红点（对应"突变之雨"），badge 四色错落

### 5.1 医学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + 细边框 + 姓名小字注；无真实肖像用装饰圆占位并注明。
2. **封面有国籍**：底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（02 页）：左头像 + 右信息网格，含生卒、出生地、教育、师承、任职、荣誉、核心领域；事实取自 page.md infobox，不得杜撰。
4. **品牌口径统一**：结尾页底部品牌标注写 `OpenMedic`；引号用半角 `" "`。
5. **获奖理由逐字引用** `medic/nobel_medicine_citations.json` 原文 + 中译，不得改写或扩写。

---

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input medic 封面模板）
01  封面 — 辐射时代的预警者 / Hermann Joseph Muller 1890–1967 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、纽约、哥伦比亚/摩尔根实验室、德州/苏联/爱丁堡/印第安纳、荣誉、核心领域）
03  核心贡献概览 — X 射线诱变（1927）/ balanced lethals / ClB 与突变率方法 / LNT 与核预警
04  纽约与摩尔根实验室（1890–1916）— 16 岁入哥伦比亚、"理论者"的委屈、Rice 任教
05  德克萨斯岁月（1920–1932）— 娶 Jessie Jacobs、镭与 X 射线起步、1919 ClB 品系
06  1927 柏林大会（核心贡献页一）— 两组剂量实验、定量关系确立、"The Problem of Genetic Modification" 轰动
07  优生学的终结者 — 1932 大会演讲、Glass 评语、批判反移民倾向、支持 positive eugenics 的复杂立场
08  柏林—列宁格勒—莫斯科（1932–1937）— Timofeeff 合作、苏联果蝇实验室、李森科主义与离境
09  爱丁堡与回归（1937–1945）— 250 个品系、《遗传学家宣言》、Amherst、曼哈顿计划顾问（不知其名）
10  1946 诺贝尔奖（核心贡献页二）— 独享；广岛长崎之后公众聚焦辐射危险；演讲要点
11  LNT 与核预警 — 诺奖演讲"无阈值"论点→线性无阈值模型；Russell-Einstein 宣言联署、Pauling 请愿
12  荣誉与认可 — Nobel 1946、Darwin-Wallace 1958、Kimber 1955、ForMemRS、Humanist of the Year 1963
13  争议与平衡 — Crow "alarmist" 批评、广岛幸存者研究与小鼠研究对 LNT 的质疑、NAS 委员会指控——按正文平衡呈现
14  结尾 — Muller elements：一条染色体上的名字，一个世纪的警告
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | citation json 逐字为 "for the discovery of the production of mutations by means of X-ray irradiation"；page.md 导语同；正文后文引作 "for the discovery that mutations can be induced by X-rays"——**以 citation json 为准**，后者只能在"正文另述"语境出现 |
| 独享年份 | 1946 独享，无共享得主 |
| 摩尔根实验室角色 | Muller 贡献"多为理论与预言"，而团队按结果计功、他自觉被排除在重要论文之外——写师承同时写此张力，勿美化 |
| ClB 与发现 | ClB 品系 1919 年发现（后知为染色体倒位），1926-11 用于第二组 X 射线实验——两个年份勿混 |
| 学位口径 | 博士学位 1916 补发（为赴 Rice 仓促完成）；1915-16 学年已上任——勿写 1915 获博士 |
| 优生学立场 | 复杂：批判优生学运动新方向（反移民等）、相信"positive eugenics"且要求"有意识地为共同善组织的社会"——按正文原句客观呈现，不引申评价；其 1932 演讲被史学视为优生学运动的终结标志（Glass 评语可引） |
| 苏联叙事 | 反对李森科主义、斯大林读《Out of the Night》后"下令组织批判"、1937 被迫离开；《火花报》与 FBI 监视——按正文客观一句，不作政治引申 |
| LNT 争议 | Muller 观点被 Rachel Carson 引用，亦被 Crow 批为 "alarmist"；有研究（广岛幸存者/小鼠）质疑 LNT——**必须平衡呈现**，勿单边写成定论或谬误 |
| 曼哈顿计划 | "adviser ... though he did not know that was what it was"——写"顾问（不知项目真名）" |
| 亲属与名人 | 表亲 Alfred Kroeber / Ursula Le Guin / Herbert J. Muller、本科实验室的 Carl Sagan——均为轶事不入关系；页面可一句话带过 |
| 姓名拼写 | 家族原姓 Müller，1848 年移民时去变音符——勿混写 |
| metadata 噪声 | metadata 无配偶子女载；两任妻子、两名子女（Helen/David）以 page.md 为准；卒日 1967-04-05 一致 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| mutation / mutagenesis | 突变 / 诱变 | 诺奖核心词对 |
| X-ray irradiation | X 射线照射 | citation 原文用语 |
| balanced lethals | 平衡致死（基因） | 1918 理论 |
| ClB | ClB 品系 | 交叉抑制（倒位）标记株 |
| crossing over | 交换（交叉） | 遗传学语义 |
| Drosophila | 果蝇 | 模式生物 |
| Muller elements | Muller 元件 | 果蝇染色体臂命名 |
| linear no-threshold model | 线性无阈值模型（LNT） | 争议焦点 |
| eugenics | 优生学 | 历史语境词，须按正文限定 |
| Lysenkoism | 李森科主义 | 拉马克式遗传论 |
| Muller's ratchet / morphs | Muller 棘轮 / morphs | See also 同名术语，勿混入正文 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Empire Collapse**（manifest 预分配）
- **匹配理由**：帝国的崩解贯穿 Muller 后半生——资本主义的幻灭、纳粹德国的出逃、斯大林苏联的批判与离境；而"崩解"之上是他为核时代敲响的警钟。音乐宜冷峻中有警世的力量感
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/Hermann_Joseph_Muller/Empire Collapse.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐

