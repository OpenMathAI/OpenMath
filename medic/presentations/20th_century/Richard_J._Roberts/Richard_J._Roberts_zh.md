# 医学家立传提示词（Richard J. Roberts）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1993 年得主 Richard J. Roberts 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Richard_J._Roberts/page.md`（唯一事实来源，metadata.json 仅作参考）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（11 节合并为 9 节）。
> ★ 库内已有同名 stub 'Richard J. Roberts'（id=6063，无 qid），yaml 走 UPD 回填 Q309816。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Richard John Roberts（1943-09-06 生于英格兰德比，在世）
- **气质关键词**：**断裂基因的共同发现者、RNA 剪接的揭示者、限制酶与计算分子生物学的推手** —— 1993 年诺贝尔生理学或医学奖（与 Phillip Allen Sharp 共享）获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for their discoveries of split genes"（因其关于断裂基因的发现）
- **设计母题**：**被剪辑的基因（the edited gene）**。1977 年的腺病毒实验显示：基因并非连续的字符串，而是被内含子打断的片段集——DNA 像一部需要剪辑的电影。视觉语言：一条 DNA 胶片被剪开、中间抽出的暗段（内含子）与重新拼接的表达序列。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Richard_J._Roberts/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1943-09-06 生于德比（父 John 为汽车修理工；母 Edna，原姓 Allsop）；4 岁随家迁巴斯
  - 童年理想先是侦探，得到一套化学玩具后改立志化学家
  - City of Bath Boys' School（今 Beechen Cliff School）就读
  - 1965 谢菲尔德大学化学 BSc；1969 博士（新黄酮类与异黄酮类的植物化学研究）
  - 1969-1972 哈佛大学博士后
  - 由 James Dewey Watson 招入冷泉港实验室（CSHL）；期间首访 MRC 分子生物学实验室，与 Frederick Sanger 共事
  - 1977 发表 RNA 剪接的发现（腺病毒研究——基因以不连续片段存在）
  - 1992 转入 New England Biolabs（业界）至今
  - 1993 与冷泉港旧同僚 Phillip Allen Sharp 共享诺贝尔奖
  - 荣誉：乌普萨拉荣誉博士 1992、Bath 荣誉博士 1994、Golden Plate 1994、FRS 1995、EMBO 1995、Knight Bachelor 2008（生日荣誉）、Lomonosov 金质奖章 2021、意大利 Chieti-Pescara 大学荣誉成员 2025
  - 2005 谢菲尔德大学化学系扩建以其命名；亦捐出可观诺奖奖金给 Beechen Cliff School（科学系以其命名）
  - 无神论者、《人道主义宣言 II》签署人；2016 与多位诺奖得主联署"支持精准农业（GMO）公开信"，倡导转基因与黄金大米
  - The Laureate Science Alliance 主席；Patient Innovation 顾问委员会成员
  - 诺贝尔演讲题为《An Amazing Distortion in DNA Induced by a Methyltransferase》

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Richard_J._Roberts/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Richard_J._Roberts/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Richard_J._Roberts_zh`
> - 肖像：正文含 2007 年肖像缩略 URL（250px 改 500px，curl 加 `-A "Mozilla/5.0"`，file 验证）；404 用 Commons `Special:FilePath` 回退；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | molecular biology | 分子生物学 | infobox Fields；诺奖核心：断裂基因 | 核心页 |
| 1 | RNA splicing | RNA 剪接 | 1977 发现；alternative splicing | 核心页 |
| 2 | restriction enzymology | 限制酶学 | 限制性内切酶与 DNA 甲基化研究 | 贡献页 |
| 3 | computational biology | 计算分子生物学 | infobox Known for 之一 | 贡献页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Richard_J._Roberts.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Phillip Allen Sharp | 无向 | 1993 诺贝尔生理学或医学奖共享（断裂基因的发现）；冷泉港旧同僚 |
| colleague | James Dewey Watson | 无向 | CSHL 的招聘者（DNA 双螺旋共同发现者） |
| colleague | Frederick Sanger | 无向 | 首访 MRC 分子生物学实验室时共事（库内规范名 id=1122） |
| parent-child | Edna Allsop | — | 母 |
| parent-child | John Roberts | — | 父，汽车修理工 |

**不入库裁定**：哈佛博后导师未载不入库；无配偶子女载；GMO 公开信、基金会职务均非个人关系。

---

## 五、配色方案 【人物专属】

- **气质**：务实的实验家转身的产业科学家——把发现变成工具与产品
- **主色**：胶片剪接蓝 `#0F4C5C`（与人物气质呼应——测序胶片与限制酶图谱的冷峻）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 分子生物学——断裂带橙 `#B4632A`
  - `badgeB` RNA 剪接——剪接青 `#2E7D6B`
  - `badgeC` 限制酶学——酶切紫 `#6B4E9E`
  - `badgeD` 计算分子生物学——代码蓝 `#3A6FA8`
- **背景母题**：DNA 胶片剪口与拼接亮段（对应"被剪辑的基因"），badge 四色错落

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
01  封面 — 断裂基因的发现者 / Richard J. Roberts 1943– + 四色 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、德比、谢菲尔德、冷泉港/New England Biolabs、荣誉、核心领域）
03  核心贡献概览 — 断裂基因 / RNA 剪接 / 限制酶与 DNA 甲基化 / 计算分子生物学
04  德比与巴斯（1943–1965）— 修理工之子、化学玩具立志、谢菲尔德化学 BSc
05  博士与哈佛（1965–1972）— 1969 新黄酮类论文、哈佛博后
06  冷泉港岁月 — Watson 招聘、MRC LMB 与 Sanger 共事
07  1977：腺病毒中的发现（核心贡献页）— 基因以不连续片段存在、RNA 剪接
08  断裂基因的冲击 — 从病毒到人类：遗传学的根本转向
09  限制酶与甲基化 — New England Biolabs 的工具箱（1992 转入业界）
10  1993 诺贝尔奖 — 与 Sharp 共享同一句理由；冷泉港旧同僚再聚奖台
11  荣誉与认可 — FRS/EMBO 1995、Knight Bachelor 2008、Lomonosov 2021、三校荣誉博士
12  回馈与命名 — 谢菲尔德化学系、Beechen Cliff 科学系（捐出可观诺奖奖金）
13  公共立场 — 《人道主义宣言 II》、2016 GMO/黄金大米公开信（正文客观呈现）
14  结尾 — 在世（1943– ）：一部继续被剪辑的基因之书
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for their discoveries of split genes"——注意 **their**（与 Sharp 共享），是全部五个词的极短理由 |
| 诺奖演讲题目 | 演讲题为《An Amazing Distortion in DNA Induced by a Methyltransferase》（DNA 甲基转移酶主题）——与获奖工作不同题，勿误标为"断裂基因演讲" |
| 机构时序 | 谢菲尔德 BSc 1965 / PhD 1969 → 哈佛博后 1969-72 → CSHL（Watson 招聘）→ 1992 转 New England Biolabs（业界至今）——勿把 NEB 写成大学 |
| Sanger 规范名 | 正文作 "Fred Sanger"；库内规范名为 **Frederick Sanger**（id=1122）——yaml 用库内名，页面可从正文写 Fred |
| Watson 规范名 | 正文写全名 James Dewey Watson；库内规范记录为 **'James Watson'**（id=3787，Q83333）——yaml 用库内名（曾误建 'James Dewey Watson' stub 已合并删除）；页面散文可从正文写全名 |
| 发现年份 | 1977 年发表 RNA 剪接发现（腺病毒）；alternative splicing 是其深远影响——两个概念勿混为一 |
| 在世口径 | b. 1943，无卒日——生卒页留白卒年，勿写"至今"以外猜测 |
| 公共立场 | GMO/黄金大米倡导与《人道主义宣言 II》签署均 page.md 明载——客观一句呈现，不引申争论 |
| metadata 噪声 | metadata 无死亡日期（在世）；occupation 无 physician；父母姓名以 page.md 为准 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| split genes | 断裂基因 | 诺奖核心词 |
| intron / exon | 内含子 / 外显子 | 被剪掉/被保留的片段 |
| RNA splicing | RNA 剪接 | 1977 发现 |
| alternative splicing | 可变剪接 | 同一基因多种蛋白 |
| adenovirus | 腺病毒 | 1977 实验材料（普通感冒病毒之一） |
| restriction endonuclease | 限制性内切酶 | 其工具箱主线 |
| DNA methylation | DNA 甲基化 | 诺奖演讲主题 |
| neoflavonoid / isoflavonoid | 新黄酮 / 异黄酮 | 博士论文对象 |
| Cold Spring Harbor Laboratory | 冷泉港实验室 | CSHL 缩写 |
| Golden Rice | 黄金大米 | 公共倡导对象 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**SEA**（manifest 预分配）
- **匹配理由**：从德比工坊家庭到冷泉港的海岸线，再到业界工具箱的开阔水域——"海"的辽阔贴合其跨越学界与产业的一生；音乐宜开阔而有行进感
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/Richard_J._Roberts/SEA.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐
