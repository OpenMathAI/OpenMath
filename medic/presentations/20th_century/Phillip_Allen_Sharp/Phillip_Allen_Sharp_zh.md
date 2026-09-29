# 医学家立传提示词（Phillip Allen Sharp）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1993 年得主 Phillip Allen Sharp 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Phillip_Allen_Sharp/page.md`（唯一事实来源，metadata.json 仅作参考）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（11 节合并为 9 节）。
> ★ 库内已有 stub 'Phillip Allen Sharp'（id=6062，无 qid），yaml 走 UPD 回填 Q312977；另有分裂 stub 'Phillip Sharp'(id=3791) 已上报主控。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Phillip Allen Sharp（1944-06-06 生于美国肯塔基州法尔茅斯，在世）
- **气质关键词**：**RNA 剪接的共同发现者、MIT 生物系的掌舵人、mRNA 可变剪接的开辟者** —— 1993 年诺贝尔生理学或医学奖（与 Richard J. Roberts 共享）获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for their discoveries of split genes"（因其关于断裂基因的发现）
- **设计母题**：**一段 DNA 的三种读法（one gene, many readings）**。剪接使同一 DNA 序列可以产出不同蛋白质——基因不是一条铁轨，而是一座可切换的道岔。视觉语言：同一母带剪辑出三部影片、铁轨道岔的分流。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Phillip_Allen_Sharp/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1944-06-06 生于法尔茅斯（父 Joseph Walter Sharp；母 Kathrin，原姓 Colvin）
  - Union College（今 Union Commonwealth University）化学与数学双主修 BA
  - 1969 伊利诺伊大学厄巴纳-香槟分校化学博士
  - 加州理工博士后至 1971（质粒研究）
  - 冷泉港实验室高级科学家，在 James D. Watson 麾下研究人类细胞基因表达
  - 1974 应 Salvador Luria 之邀获 MIT 教职
  - 1985-1991 任 MIT 癌症研究中心主任（今 Koch 研究所）；1991-1999 任生物系主任；2000-2004 创立并领导 McGovern 脑研究所
  - 1999 起 MIT Institute Professor（最高教职）；现为名誉教授、Koch 研究所成员、Jameel Clinic 顾问委员会主席
  - 1993 与 Roberts 共享诺贝尔奖；获奖工作=真核基因含内含子、mRNA 剪接可多方式发生产出不同蛋白
  - 现研究方向：小 RNA/非编码 RNA/microRNA 靶点与血管新生、细胞应激
  - 与 Ann Holcombe 结婚（1964），育三女
  - 荣誉：NAS 分子生物学奖 1980、Golden Plate 1981、Horwitz 奖 1988（与 Thomas R. Cech 共享）、Dickson 奖 1991、诺贝尔奖 1993、Benjamin Franklin 奖章 1999、Novartis-Drew 奖 2003、国家科学奖章 2004、Othmer 金质奖章 2015、ForMemRS 2011、AAAS 会长 2012 等
  - 1995 FBI 证实收到 Unabomber（Ted Kaczynski）的威胁信
  - 联合创办 Biogen、Alnylam Pharmaceuticals、Magen Biosciences
  - 2016 协助组织"支持精准农业公开信"（反对 Greenpeace 禁 GMO/黄金大米）
  - 2025 纪录片《Cracking the Code: Phil Sharp and the Biotech Revolution》

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Phillip_Allen_Sharp/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Phillip_Allen_Sharp/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Phillip_Allen_Sharp_zh`
> - 肖像：正文含 2007 Winthrop-Sears 奖章照与 2006 国家科学奖章照缩略 URL（250px 改 500px，curl 加 `-A "Mozilla/5.0"`，file 验证）；404 用 Commons `Special:FilePath` 回退；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | molecular biology | 分子生物学 | infobox Fields；诺奖核心：RNA 剪接与断裂基因 | 核心页 |
| 1 | RNA splicing | RNA 剪接 | 剪接的多方式发生=可变剪接 | 核心页 |
| 2 | non-coding RNA biology | 非编码 RNA 生物学 | 现研究方向：miRNA 靶点、血管新生与应激 | 现研究页 |
| 3 | genetics | 遗传学 | occupation 之首；基因表达调控 | 研究页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Phillip_Allen_Sharp.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Richard J. Roberts | 无向 | 1993 诺贝尔生理学或医学奖共享（断裂基因的发现）；冷泉港旧同僚 |
| colleague | James Dewey Watson | 无向 | 冷泉港高级科学家阶段在其麾下研究人类细胞基因表达 |
| advisor-student | Connie Cepko | 生→ | 博士生（infobox 明载） |
| advisor-student | Andrew Fire | 生→ | 博士生（infobox 明载，2006 诺奖得主，库内 id=4781） |
| advisor-student | Melissa J. Moore | 生→ | 博士生（infobox 明载） |
| advisor-student | Richard Carthew | 生→ | 博士生（infobox 明载） |
| spouse | Ann Holcombe | — | 1964 结婚 |
| parent-child | Kathrin Colvin | — | 母 |
| parent-child | Joseph Walter Sharp | — | 父 |

**不入库裁定**：Salvador Luria（1974 供 MIT 职位的邀请人）系职务引荐，正文无师承/共事叙事，不入库（循 Flexner 先例）；三名女儿仅记数量；创办企业与顾问职务非关系。

---

## 五、配色方案 【人物专属】

- **气质**：学界与产业的双栖掌舵人——把剪接的发现锻造成生物技术时代
- **主色**：剪接道岔蓝 `#14647E`（与人物气质呼应——MIT 的工程蓝与 RNA 图谱的冷峻）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 分子生物学——断裂带橙 `#B4632A`
  - `badgeB` RNA 剪接——剪接青 `#2E7D6B`
  - `badgeC` 非编码 RNA——miRNA 紫 `#6B4E9E`
  - `badgeD` 生物技术——创业金 `#C89B3C`
- **背景母题**：铁轨道岔与三种剪辑成品（对应"一段 DNA 的三种读法"），badge 四色错落

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
01  封面 — 可变剪接的开辟者 / Phillip Allen Sharp 1944– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、法尔茅斯、Union/UIUC、冷泉港/MIT、荣誉、核心领域）
03  核心贡献概览 — RNA 剪接 / 断裂基因 / miRNA 与非编码 RNA / 生物技术创业
04  肯塔基与双主修（1944–1969）— Union College 化学+数学、1969 UIUC 化学博士
05  Caltech 质粒与冷泉港（1969–1974）— 博后、Watson 麾下高级科学家
06  1977：剪接的发现（核心贡献页）— 与 Roberts 独立抵达同一图景
07  MIT 掌舵（1974–2004）— Luria 之邀、癌症研究中心主任、生物系主任、McGovern 创始所长
08  一段 DNA 的三种读法 — alternative splicing：同一序列产出不同蛋白
09  1993 诺贝尔奖 — 与 Roberts 共享；citation 中的长句释义可引
10  小 RNA 时代 — miRNA 靶点、血管新生与细胞应激的现研究
11  荣誉与认可 — NAS 分子生物学奖 1980、Horwitz 1988（与 Cech）、NMS 2004、Othmer 2015、ForMemRS 2011、AAAS 会长 2012
12  学界与产业 — Biogen/Alnylam/Magen 联合创办；2025 纪录片
13  阴影与勇气 — 1995 Unabomber 威胁信（正文一句客观）；2016 精准农业公开信
14  结尾 — 在世（1944– ）：剪接仍在继续
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for their discoveries of split genes"——共享短句；page.md 导语另载长句释义（"genes in eukaryotes are not contiguous strings but contain introns..."）可引但须注明系导语释义 |
| 库内分裂 | 库内同时存在 'Phillip Sharp'(id=3791) 与 'Phillip Allen Sharp'(id=6062) 两条——本批 yaml 用 manifest 全名 UPD 6062；3791 分裂已上报主控合并，勿引用短名 |
| Watson 关系 | "senior scientist under James D. Watson"——麾下共事用 colleague（非师承，其博士在 UIUC）；库内规范记录为 **'James Watson'**（id=3787）——yaml 用库内名（误建 stub 已合并删除） |
| Luria 不入库 | 1974 邀其赴 MIT 系职务引荐（循 Flexner 先例不入库）；页面叙事页可一句提及 |
| Horwitz 双奖 | 1988 Horwitz 奖与 Thomas R. Cech 共享——与诺奖 co-honored 不同人，不另建第二行（uq_rel 按 type 去重），陷阱表注明 |
| Unabomber | 1995 FBI 证实收到 Ted Kaczynski 威胁信（"it would be beneficial to your health to stop your research in genetics"）——正文明载可引一句，客观处理 |
| 学会职务 | AAAS 会长 2012（美国科学促进会）勿与 American Academy of Arts and Sciences 混 |
| 创办公司 | Biogen/Alnylam/Magen 联合创办并任董事——产业身份页素材，非关系 |
| metadata 噪声 | metadata 无配偶/子女载；妻子 Ann Holcombe（1964）、三女以 page.md 为准；在世无卒日 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| split genes | 断裂基因 | 诺奖核心词 |
| RNA splicing | RNA 剪接 | 与 Roberts 共享的发现 |
| intron | 内含子 | 被剪除片段 |
| alternative splicing | 可变剪接 | 同一基因多种产物 |
| microRNA (miRNA) | 微 RNA | 现研究方向 |
| non-coding RNA | 非编码 RNA | 现研究方向 |
| plasmid | 质粒 | Caltech 博后对象 |
| Koch Institute | 科赫研究所（MIT 癌症研究中心后身） | 1985-91 任主任 |
| McGovern Institute | 麦戈文脑研究所 | 2000-04 创始所长 |
| Unabomber | 大学航空炸弹客 | 1995 威胁信事件 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Expedition**（manifest 预分配）
- **匹配理由**：从肯塔基小镇到 MIT 之巅再到生物技术远征——"远征"贴合其学界-产业双线开拓；剪接的道岔意象亦自带探索感
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/Phillip_Allen_Sharp/Expedition.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐
