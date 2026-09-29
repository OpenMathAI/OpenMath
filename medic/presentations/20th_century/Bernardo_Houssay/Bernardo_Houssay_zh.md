# 医学家立传提示词（Bernardo Houssay）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Bernardo Houssay（1947 年诺贝尔生理学或医学奖得主，阿根廷）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Bernardo_Houssay/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Bernardo Alberto Houssay（贝尔纳多·奥赛，1887-04-10 布宜诺斯艾利斯 ~ 1971-09-21 布宜诺斯艾利斯，享年 84 岁）
- **气质关键词**：**拉丁美洲首位科学诺奖得主、垂体激素糖代谢效应的发现者、两度被军政府解职而不辍的科学生态建设者** —— 1947 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json；与 Cori 夫妻同年各得一半）：
  > "for his discovery of the part played by the hormone of the anterior pituitary lobe in the metabolism of sugar"
  > （因其发现垂体前叶激素在糖代谢中的作用）
- **设计母题**：**「切除与回灌」**。切除犬的垂体前叶糖尿病减轻、提取物回注糖尿病加重——视觉隐喻：垂体腺小剪影与血糖曲线的升降双枝。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Bernardo_Houssay/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Bernardo_Houssay/`，成目录 `medic/presentations/20th_century/Bernardo_Houssay/`，Makefile 复制后设 `MAIN=Bernardo_Houssay_zh`、`VIDEO_NAME=Bernardo_Houssay_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库：本人记录复用他批已建 stub（库内 id=3458）UPD 回填 QID Q237160，`has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | physiology | 生理学 | 布宜诺斯艾利斯生理学讲席（1919–1943），1947 诺奖核心 | 总览页 |
| 1 | endocrinology | 内分泌学 | 垂体前叶 diabetogenic 效应、激素反馈机制 | 垂体页 |
| 2 | diabetes research | 糖尿病研究 | 垂体切除缓解糖尿病的实验证明（1930s） | 糖尿病页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Bernardo_Houssay.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Carl Ferdinand Cori | — | 1947 同年共享，科里夫妻得糖代谢一半 |
| co-honored | Gerty Cori | — | 1947 同年共享，科里夫妻得糖代谢一半 |
| spouse | María Angélica Catán | — | 妻 |
| parent-child | Albert Houssay | 父 | 法国移民 |
| parent-child | Clara Houssay | 母 | 法国移民 |
| advisor-student | Eduardo Braun-Menéndez | 生 | 门生，后成著名生理学家 |
| advisor-student | Miguel Rolando Covian | 生 | 门生，后为巴西神经生理学之父 |

> 说明：门生仅收 page.md 点名的两位（Eduardo Braun-Menéndez、Miguel Rolando Covian），「many disciples」其余不具名者不入库；与两门生合写西语/葡语《人体生理学》教科书并入叙事。1943/1945 两次解职系军政府/庇隆政府行为，不建个人 controversy 边；JFK 可的松治疗仅遗产叙事。另有他批（Leloir 侧）先建的 Houssay→其博士生边共存于库，不冲突。

## 五、配色方案 【人物专属】

- **气质**：南美的热忱与严谨、体制逆境中的 builder 气质
- **主色**：潘帕斯深绿 `#2F5D3A`（拉美科学自立的地气）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 生理学 — 实验室青 `#1F7A6D`
  - `badgeB` 内分泌学 — 激素紫 `#5B4E8E`
  - `badgeC` 糖尿病研究 — 胰岛蓝 `#33637D`
  - `badgeD` 垂体研究 — 前叶琥珀 `#C08A2E`
- **背景母题**：垂体腺剪影与血糖升降曲线、稀疏犬类实验剪影（Houssay 犬），低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 拉美首位科学诺奖得主 / Bernardo Houssay 1887–1971 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、法国移民家庭、神童履历、任职、荣誉、核心领域）
03  核心贡献概览 — 垂体前叶 diabetogenic 效应 / 激素反馈 / 门生网络与教科书
04  神童 (1887–1904) — 14 岁入药学院、17 岁入医学院、三年级即任生理学助教
05  早熟的学者 (1908–1919) — 1911 垂体提取物 M.D. 论文定终身方向、兽医学院生理学教授、医院行医
06  布宜诺斯艾利斯讲席 (1919–1943) — 把生理学系建成国际水准研究重镇
07  1930s：垂体与糖尿病（核心页）— 前叶提取物致糖尿效应、垂体切除减轻糖尿病
08  1947 诺贝尔奖（核心页）— citation 原文、与 Cori 夫妻同年各半、拉美首位科学诺奖
09  1943：被军政府逐出大学 — 自由派思想获罪、自建 Instituto de Biología y Medicina Experimental
10  1945/1955：第二次解职与复职 — 庇隆政府再解职、1955 庇隆倒台后重返布大
11  门生与教科书 — Braun-Menéndez、Covian（巴西神经生理学之父）、西语葡语《人体生理学》行销全洲
12  科学生态的建设者 — 600+ 论文、1957 起执掌国家科技研究理事会（CONICET）、众多学会职务
13  荣誉与认可 — James Cook 1948 · Dale Medal 1960 · NAS 1940 · ForMemRS 1943 · 哈佛剑桥牛津巴黎等 15+ 荣誉博士
14  遗产 — 激素反馈机制成为现代内分泌学中枢；JFK 肾上腺功能不全治疗的思想源头；2013 Google Doodle
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for his discovery of the part played by the hormone of the anterior pituitary lobe in the metabolism of sugar"（his 独享一半）；与 Cori 夫妻的理由不同，勿写成三人同理由 |
| 2 | 「一半」结构 | 1947 年奖分两半：Cori 夫妻（糖原催化转化）+ Houssay（垂体激素糖代谢）——份额必须写清 |
| 3 | 「首位」口径 | 「拉丁美洲首位科学诺奖得主」（sciences）——勿扩为「拉美首位诺奖得主」（和平奖/文学奖另有更早者） |
| 4 | 解职叙事 | 1943 军政府（liberal political ideas 获罪）与 1945 Peronist 政府两次解职、1955 复职——史实克制记载，只述事件不评价政治体制，不建政治人物关系边 |
| 5 | 私立研究所 | Instituto de Biología y Medicina Experimental 是其被逐后自建的私立机构——与研究连续性的关键节点，勿写成国家机构 |
| 6 | JFK 段 | 其激素反馈研究是 1947 年确诊的 JFK 肾上腺功能不全可的松疗法的基础——遗产叙事一句带过，勿展开肯尼迪病史 |
| 7 | 引语红线 | 本篇 page.md 无直接引语，禁编造；诺奖演讲题 The Role of the Hypophysis in Carbohydrate Metabolism and in Diabetes 可用作页面标题 |
| 8 | 神童年份 | 14 岁入药学院、17 岁入医学院（1904-1910 在读）、1908 助讲、1911 论文发表——数字链勿错 |
| 9 | 门生口径 | 仅 Braun-Menéndez 与 Covian 具名入库；Covian 的「巴西神经生理学之父」称号 page 明载可用 |
| 10 | metadata 冲突 | frontmatter occupation 含 entomologist 噪声；yaml 主职业 physiologist。Google Doodle 2013-04-08（126 岁诞辰）可作结尾彩蛋 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| anterior pituitary / hypophysis | 垂体前叶 | 诺奖理由核心词，两写法并存 |
| diabetogenic effect | 致糖尿病效应 | 前叶提取物的效应名 |
| hypophysectomy | 垂体切除术 | 缓解糖尿病的实验手段 |
| hormonal feedback | 激素反馈 | 现代内分泌学中枢概念 |
| carbohydrate metabolism | 糖代谢 | 与 Cori 夫妻领域的交界面 |
| diabetes mellitus | 糖尿病 | 语境为实验性糖尿病 |
| Instituto de Biología y Medicina Experimental | 生物学与实验医学研究所 | 1943 年自建 |
| CONICET | 阿根廷国家科技研究理事会 | 1957 起任主任 |
| Dale Medal | 戴尔奖章 | 内分泌学会 1960 授予 |
| Houssay animal | Houssay 动物（去垂体-去胰动物） | 教科书术语，本页未载慎用 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**New Lands** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「新大陆」双关贴切：既是地理上的拉丁美洲首次登顶科学诺奖，也是两次解职后在废墟上重建研究所的开疆气概
  - 开阔上行的曲式匹配「从被逐者到国父级科学家」的反弹叙事
- **备选**（未采用）：Expedition（探险感偏地理叙事）、Awaken（本批 Hess 已用）
- **本地路径**：按 music_audio/ 内 Alex-Productions New Lands 曲目复制至 `medic/presentations/20th_century/Bernardo_Houssay/New_Lands.wav`，ffmpeg `-shortest` 对齐
