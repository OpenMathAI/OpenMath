# 医学家立传提示词（Charles Nicolle）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1928 年得主 Charles Nicolle 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Charles_Nicolle/page.md`（唯一事实来源，metadata.json 仅作参考）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（11 节合并为 9 节）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Charles Jules Henri Nicolle（1866-09-21 生于法国鲁昂 ~ 1936-02-28 逝于法属突尼斯突尼斯城，享年 69 岁）
- **气质关键词**：**斑疹伤寒媒介的破解者、突尼斯巴斯德研究所的营建者、细菌学家与小说家** —— 1928 诺贝尔生理学或医学奖获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for his work on typhus"（因其关于斑疹伤寒的工作）
- **设计母题**：**隐形的媒介（hidden vector）**。临床观察发现斑疹伤寒病人热浴更衣后便不再传染他人——致命的载体藏在衣料缝隙的虱子身上。视觉语言：衣纹间隐现的微小病原、放大镜下的"看不见的凶手"，比泛泛的"显微镜"更贴合 Nicolle 的发现叙事。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Charles_Nicolle/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1866-09-21 生于鲁昂（父 Eugène 为鲁昂医院医生；兄 Maurice 后为微生物学家、弟 Marcel 为艺术评论家）
  - 就读 Lycée Pierre Corneille（鲁昂）
  - 1893 获巴黎巴斯德研究所医学学位
  - 1895 与 Alice Avice 结婚；1896/1898 子女 Marcelle、Pierre 出生
  - 1893-1896 鲁昂医学院成员；1896-1902 任细菌学实验室主任；其间渐失聪
  - 1903 任突尼斯巴斯德研究所所长（携 Hélène Sparrow 任实验室主任），直至 1936 卒于任上
  - 1906 疟疾流行、1907 霍乱爆发时任法国政府关键联络人
  - 1909-06 黑猩猩实验证实虱子为流行性斑疹伤寒媒介；后改用豚鼠
  - 查明主要传播途径为虱粪（擦皮肤或眼感染），并区分鼠型斑疹伤寒（跳蚤传播）
  - 碎虱+康复血清的疫苗尝试失败（1930 由 Rudolf Weigl 接棒）；氟化钠灭菌法制成淋病/葡萄球菌/霍乱疫苗
  - 1928 获诺贝尔生理学或医学奖（独享）
  - 1933-1936 出版《传染病的命运》等四部论著；另有三部小说
  - 1935-08 与天主教会和解（12 岁时离开）
  - 1936-02-28 卒于突尼斯

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Charles_Nicolle/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Charles_Nicolle/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Charles_Nicolle_zh`
> - 肖像：优先用 images.txt 内 Wikimedia 缩略图 URL（250px 改 500px，curl 加 `-A "Mozilla/5.0"`，file 验证）；404 则 Commons `Special:FilePath/<文件名>?width=600` 或 Wikipedia REST API 查 infobox 原图名；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | bacteriology | 细菌学 | 诺奖核心：斑疹伤寒传播机制的发现 | 核心页 |
| 1 | parasitology | 寄生虫学 | 鉴定刚地弓形虫、研究热带利什曼原虫 | 成就页 |
| 2 | tropical medicine | 热带医学 | 北非地方病防治与疫苗生产 | 突尼斯页 |
| 3 | epidemiology | 流行病学 | 斑疹伤寒传播链与流行干预（1906 疟疾、1907 霍乱） | 传播页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Charles_Nicolle.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Eugène Nicolle | — | 父，鲁昂医院医生，最早的启蒙者 |
| parent-child | Aline Louvrier | — | 母 |
| spouse | Alice Avice | — | 1895 结婚 |
| parent-child | Marcelle Nicolle | — | 长女（1896 生），后进入医学界 |
| parent-child | Pierre Nicolle | — | 次子（1898 生），后进入医学界 |
| colleague | Hélène Sparrow | 无向 | 1903 随其赴突尼斯巴斯德研究所任实验室主任 |

**不入库裁定**：兄 Maurice Nicolle（微生物学家）与弟 Marcel Nicolle（艺术评论家）为兄弟关系，类型白名单无 sibling，不入库；Rudolf Weigl 1930 接棒疫苗研究系学术接力，无个人关系记载，不入库；三次 Montyon 科学奖、荣誉军团指挥官勋章为荣誉非关系。

---

## 五、配色方案 【人物专属】

- **气质**：深蓝、克制、殖民地科学前哨的沉静坚守
- **主色**：突尼斯地中海深蓝 `#0E4D64`（与人物气质呼应——北非海岸、实验室长夜、33 年坚守一职）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 细菌学（斑疹伤寒）——病媒深红 `#8C1F28`
  - `badgeB` 寄生虫学——原虫紫 `#6B4E9E`
  - `badgeC` 热带医学——绿洲绿 `#2E7D6B`
  - `badgeD` 流行病学——沙金 `#B4872A`
- **背景母题**：柔和衣纹弧线与稀疏微点（对应"隐形的媒介"——衣料纹理间传递的微粒），四种 badge 色错落

### 5.1 医学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + 细边框 + 姓名小字注；无真实肖像用装饰圆占位并注明。
2. **封面有国籍**：底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（02 页）：左头像 + 右信息网格，含生卒、出生地、教育、师承、任职、荣誉、核心领域；事实取自 page.md infobox，不得杜撰。
4. **品牌口径统一**：结尾页底部品牌标注写 `OpenMathAI`；引号用半角 `" "`。
5. **获奖理由逐字引用** `medic/nobel_medicine_citations.json` 原文 + 中译，不得改写或扩写。

---

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input medic 封面模板）
01  封面 — 斑疹伤寒的追猎者 / Charles Nicolle 1866–1936 + 四色 badge + 右上头像 + 国籍行（France）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地鲁昂、教育、突尼斯研究所 33 年、荣誉、核心领域）
03  核心贡献概览 — 斑疹伤寒媒介 / 疫苗与氟化钠灭菌 / 原虫与寄生虫 / 突尼斯研究所营建
04  鲁昂早年（1866–1893）— 医生世家、Lycée Pierre Corneille、1893 巴黎巴斯德研究所医学学位
05  失聪与转向实验室（1893–1902）— 鲁昂医学院成员、1896-1902 细菌学实验室主任、失聪促成转型
06  突尼斯巴斯德研究所所长（1903–1936）— 33 年经营、医疗收入反哺科研的经费自主、Archives de l'Institut de Tunis
07  斑疹伤寒之谜 — 病人热浴更衣后不再传染他人的临床观察
08  1909 黑猩猩实验：虱子是媒介（核心贡献页）— 媒介实验设计与重复验证、后改用豚鼠
09  传播机制与鉴别 — 经虱粪（擦皮肤或眼）而非叮咬感染、与鼠型斑疹伤寒（跳蚤传播）区分
10  疫苗尝试与氟化钠灭菌 — 碎虱+康复血清自体试验、失败、Weigl 1930 接棒；淋病/葡萄球菌/霍乱疫苗行销全球
11  其他成就 — 刚地弓形虫鉴定、热带利什曼原虫、马尔他热（布鲁氏菌病）疫苗、蜱热传播
12  荣誉与认可 — Nobel 1928、三度 Montyon 科学奖、荣誉军团指挥官勋章
13  写作与哲思 — 《传染病的命运》等论著与三部小说、1935 年与天主教会和解
14  结尾 — 遗产（衣虱灭斑疹伤寒、突尼斯研究所的国际地位）
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for his work on typhus"（斑疹伤寒的工作），勿扩写成"发现虱子传播斑疹伤寒"的长句；后者是 Wikipedia 正文转述 |
| 独享年份 | 1928 年为独享，无共享得主，勿杜撰 co-honored |
| 学位口径 | 正文作 "medical degree from the Pasteur Institute of Paris in 1893"；infobox Education 写 University of Paris；frontmatter 有 Paris Medical Faculty——页面上写"1893 获医学学位（巴黎巴斯德研究所）"即可，勿编造"医学博士"头衔 |
| 失聪动机 | 正文明载失聪妨碍问诊、促成其转向实验室研究——这是叙事主线，勿遗漏、勿改成因 |
| 实验动物 | 1909 首验用黑猩猩，后续改用豚鼠（更小更便宜且同样易感）——两阶段勿混 |
| 传播方式 | 主要传播途径是虱粪（擦到皮肤或眼即感染）而非叮咬——正文明载，勿写成叮咬传播 |
| 疫苗结局 | 自制斑疹伤寒疫苗尝试失败（受试儿童患病后康复）；实用疫苗 1930 由 Rudolf Weigl 实现——勿写成 Nicolle 制成疫苗 |
| 同名混淆 | 兄 Marcel Nicolle（艺术评论家）≠ 女儿 Marcelle Nicolle；子 Pierre（1898 生）；兄弟属 sibling 无类型不入库 |
| metadata 噪声 | metadata.json 无配偶/子女/导师记载；婚姻（Alice Avice 1895）、子女、父母以 page.md 为准 |
| 鼠型斑疹伤寒 | 由跳蚤传播的 murine typhus 与虱传流行性斑疹伤寒的区分是 Nicolle 工作的附带贡献 |
| 奖项细节 | Montyon 科学奖三次（frontmatter 重复列三条）；荣誉军团勋章为 Commander 级 |
| 年代锚点 | 1906 疟疾流行、1907 霍乱爆发时任法国政府关键联络人；1903 任所长、1936 卒于任上 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| epidemic typhus | 流行性斑疹伤寒 | 与鼠型斑疹伤寒区分 |
| louse / lice | 虱（子） | 媒介昆虫，非病原体本身 |
| vector | （传播）媒介 | 流行病学语义 |
| excrement | 排泄物（虱粪） | 真正的感染途径 |
| murine typhus | 鼠型斑疹伤寒 | 跳蚤传播，勿与虱传混淆 |
| guinea pig | 豚鼠 | 后期实验动物 |
| Toxoplasma gondii | 刚地弓形虫 | 宿主为 gundi（梳趾鼠） |
| Leishmania tropica | 热带利什曼原虫 | 致东方疖 |
| sodium fluoride | 氟化钠 | 灭菌且保结构的试剂 |
| Malta fever | 马耳他热（布鲁氏菌病） | 疫苗针对对象之一 |
| trachoma | 沙眼 | 研究病种之一 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless**（manifest 预分配）
- **风格**：沉稳 / 纪录片 / 长期纲领
- **匹配理由**：33 年经营一座研究所、一项改变斑疹伤寒防治格局的工作——"长期纲领"与"沉稳"正贴合 Nicolle 鲁昂→突尼斯一线一生的静默坚守；纪录片气质匹配"临床观察→实验证实→机制阐明"的传记叙事
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/Charles_Nicolle/Timeless.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐
