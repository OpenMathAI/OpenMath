# 医学家立传提示词（Niels Kaj Jerne）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1984 年得主 Niels Kaj Jerne（尼尔斯·凯·耶恩）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Niels_Kaj_Jerne/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Niels Kaj Jerne（1911-12-23 生于英国伦敦 ~ 1994-10-07 逝于法国 Castillon-du-Gard，享年 82 岁）
- **气质关键词**：**免疫学的三位理论家、抗体天然选择说的提出者、免疫网络理论的筑造者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1984 条目，三人共享同一句；Jerne 独享**一半**，对应理论部分）：
  > "for theories concerning the specificity in development and control of the immune system and the discovery of the principle for production of monoclonal antibodies"（因免疫系统发育与控制特异性的理论及单克隆抗体生产原理的发现）
  - 结构：Jerne＝免疫系统特异性的理论（天然抗体选择说/耐受学习在胸腺/免疫网络）；Köhler+Milstein＝单克隆抗体生产原理（杂交瘤）——两层务必分层。
- **设计母题**：**免疫网络（idiotypic network）**——抗体独特位互锁成网、抗原打破平衡的意象：以互锁环网被一点扰动的图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Niels_Kaj_Jerne/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Niels_Kaj_Jerne/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Niels_Kaj_Jerne_zh`、`VIDEO_NAME=Niels_Kaj_Jerne_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | immunology | 免疫学 | infobox Fields |
| 1 | immune network theory | 免疫网络理论 | 1974 独特位网络学说 |
| 2 | antibody formation | 抗体形成理论 | 天然选择说（1955 PNAS） |
| 3 | immune tolerance | 免疫耐受 | 自我耐受"学习"发生于胸腺的假说 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Tjek Jerne | 无向 | 画家，育二子 Ivar（1936）与 Donald（1941） |
| spouse | Gertrud Wettstein | 无向 | 第三段婚姻，1971 育三子 Andreas Wettstein |
| co-honored | Georges J. F. Köhler | 无向 | 1984 诺贝尔生理学或医学奖共享（Jerne 理论占一半，Köhler/Milstein 杂交瘤占另一半） |
| co-honored | César Milstein | 无向 | 1984 诺贝尔生理学或医学奖共享（同上结构） |

**在世者关系少为诚实值**（4 条，已故者无师生记录）：Jerne page.md 未载博士导师（莱顿物理两年转哥本哈根医学，1947 毕业/1951 博士论文未载导师名）——Review 勿补造边。**不入库但提示词可叙述**：James Watson"theory stinks"轶话（反对声举例，事件非关系）；第二段妻子 page.md 未载姓名（只写 married three times）；Basil Institute 同侪未具名。

## 五、配色方案 【人物专属】

- **气质**：理论的孤独、北欧的冷峻、网络交织的深意
- **主色**：`#173F5F`（北海深蓝——哥本哈根与巴塞尔之间的理论航程）+ 香槟金诺奖色
- **badge 四分类色**：`badgeNetwork` 免疫网络 深蓝 `#173F5F`；`badgeNatural` 天然选择说 青绿 `#0E7C7B`；`badgeThymus` 胸腺耐受 苔绿 `#175E54`；`badgeBasel` 巴塞尔研究所 琥珀 `#C07A2A`
- **背景母题**：互锁环网被一点扰动的图案，呼应「免疫网络」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 免疫网络的理论家 / Niels Kaj Jerne 1911–1994 + 四色 badge + 右上头像 + 国籍行（Denmark）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1911-12-23 伦敦 ~ 1994-10-07 法国
    Castillon-du-Gard、哥本哈根大学医学 1947/博士 1951、巴塞尔免疫学研究所所长
    1969–1980、诺奖 1984）
03  核心贡献概览 — 天然抗体选择说 / 胸腺耐受学习 / 免疫网络理论 / 1984 三人结构
04  伦敦出生的丹麦人 (1911–1929) — Fanø 祖籍、一战迁荷兰、鹿特丹少年、
    莱顿物理两年转哥本哈根医学
05  血清研究所岁月 (1943–1956) — 丹麦国家血清研究所研究员、 Langebro 桥上的
    灵感（骑车回家途中）、1951 白喉毒素-抗毒素 avidity 博士论文
06  天然选择说 (1955)（核心贡献页）— 免疫系统天然已有对付抗原的特异性抗体，
    抗原只是"选择"扩增——取代诱导说的范式革命
07  WHO 与匹兹堡 (1956–1966) — 日内瓦 WHO 生物标准与免疫学部门主任六年、
    匹兹堡大学微生物系教授兼主任四年、WHO 免疫学专家顾问团
08  法兰克福与巴塞尔 (1966–1980) — 法兰克福实验治疗学教授、Paul-Ehrlich 研究所所长、
    1969 巴塞尔免疫学研究所所长至 1980 退休
09  免疫网络理论 (1974)（核心贡献页）— 抗体独特位彼此互锁成网、
    抗原打破平衡激发应答；Watson"stinks"的反对轶话（客观引述）
10  1984：三人两半 — Jerne 独享一半（理论）；Köhler+Milstein 共享另一半
    （杂交瘤单抗原理）——citation 同一句、两层结构
11  荣誉与认可 — Gairdner 1970、Marcel Benoist 1978、Erlich-Darmstaedter 1982、
    FRS 1980、NAS 外籍院士 1975、法兰西科学院 1981、五校荣誉博士
12  家庭 — 三段婚姻：Tjek（画家，Ivar/Donald）、Gertrud Wettstein（Andreas 1971）；
    第二段妻子 page.md 未载姓名
13  诺奖讲演 — "The Generative Grammar of the Immune System"（1984-12-08）：
    免疫系统的生成语法隐喻
14  遗产与结尾 — 理论免疫学的骨架：从选择说到网络说；巴塞尔学派的黄金年代
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1984 两半结构 | Jerne 独享一半（三大理论：天然抗体选择说/胸腺耐受学习/T-B 协同概念）；Köhler+Milstein 共享另一半（单抗原理）——citation 是合写一句，个人侧重务必分层 |
| 三大理论归纳 | page.md 概括为三点：①抗体天然预存而非应答生成；②自我耐受"学习"发生在胸腺；③网络理论（独特位互锁）——第三点与 ①② 并列，勿把网络理论当全部贡献 |
| 天然选择说年份 | 1955 PNAS "The Natural-Selection Theory of Antibody Formation"；灵感据说来自 Langebro 桥骑车——"it is said" 措辞照页面保留 |
| 网络理论论文 | 1974 Annales d'immunologie "Towards a network theory of the immune system"——1970s-80s 先驱期，"met by skepticism"、Watson "stinks" 轶话客观引述勿渲染 |
| 国籍与出生地 | 生于伦敦、长于鹿特丹、丹麦人——citations json country=Denmark；yaml 单国籍 Denmark，正文交代三地轨迹 |
| 博士导师 | page.md 未载（哥本哈根医学毕业与 1951 博士均无导师名）——师承边为零是诚实值 |
| 卒地 | 逝于法国 Castillon-du-Gard（1994-10-07），非丹麦——别写成"逝于哥本哈根" |
| 家庭 | 三段婚姻但 page.md 只具名 Tjek Jerne 与 Gertrud Wettstein 两位；第二段妻子不入库不具名 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| natural-selection theory | 抗体形成的（天然）选择说 | 1955；"天然抗体预存+抗原选择" |
| immune network theory | 免疫网络理论 | 1974；独特位互锁 |
| idiotype | 独特型 | 抗体结合位本身的抗原性 |
| clonal selection | 克隆选择 | Burnet 学说，与 Jerne 选择说相承但勿混同 |
| monoclonal antibody | 单克隆抗体 | 1984 另一半是 Köhler/Milstein 的杂交瘤原理 |
| avidity | 亲和力 | 博士论文主题（白喉毒素-抗毒素） |
| Statens Serum Institut | 丹麦国家血清研究所 | 1943–1956 |
| Basel Institute for Immunology | 巴塞尔免疫学研究所 | 1969–1980 任所长 |
| generative grammar | 生成语法 | 诺奖讲演隐喻 |
| Paul-Ehrlich-Institut | 保罗·埃尔利希研究所 | 法兰克福 1966–69 任所长 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**With Me**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Jerne 的理论是"抗体彼此相伴成网"的图景——独特位互锁、平衡与扰动；"With Me" 的陪伴感呼应免疫网络中抗体互为镜像的哲学意象，也承载理论家独行半生终被理解的回响。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Niels_Kaj_Jerne/With_Me.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
