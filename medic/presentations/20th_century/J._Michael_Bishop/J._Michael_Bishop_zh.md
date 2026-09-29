# 医学家立传提示词（J. Michael Bishop）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1989 年得主 J. Michael Bishop（约翰·迈克尔·毕晓普）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/J._Michael_Bishop/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：John Michael Bishop（1936-02-22 生于宾夕法尼亚州约克 ~ 2026-03-20 逝于旧金山，享年 90 岁，肺炎），美国免疫学家与微生物学家，UCSF 第八任校长（1998-2009）
- **气质关键词**：**癌基因细胞起源的证明者、v-src 之谜的解答者、学者型校长**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1989 条目，Bishop/Varmus 两人共享）：
  > "for their discovery of the cellular origin of retroviral oncogenes"（因其发现逆转录病毒癌基因的细胞起源）
- **设计母题**：**被病毒"劫走"的细胞基因（c-src → v-src）**——癌基因不是病毒自带的，而是细胞自己的基因被病毒复制带走；用「细胞基因被病毒颗粒掳走」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/J._Michael_Bishop/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/J._Michael_Bishop/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=J._Michael_Bishop_zh`、`VIDEO_NAME=J._Michael_Bishop_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。**注意**：2026-03-20 刚逝世——生卒口径 1936–2026。

## 三、研究领域梳理 + 入库 【人物专属】

**Bishop 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学（逆转录病毒） | infobox Fields；1989 诺奖核心 | 核心页 |
| 1 | oncology | 肿瘤学（癌基因） | c-src/原癌基因 | 核心页 |
| 2 | immunology | 免疫学 | 职业起点的学科身份 | 身份页 |
| 3 | microbiology | 微生物学 | metadata field_of_work 明载 | 身份页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Harold E. Varmus | 无向 | 1989 诺贝尔生理学或医学奖共享（逆转录病毒癌基因的细胞起源） |
| colleague | Harold E. Varmus | 无向 | 长期科学伙伴（notably long scientific partnership），c-Src/v-Src 发现搭档 |

**诚实值说明（★ 本批最简）**：Bishop 页正文极简——无配偶/子女段、无具名学生、frontmatter doctoral_advisor=Gebhard Koch **正文无载**（汉堡 Heinrich Pette 研究所一年，未点名导师）——按纪律不入库；relations=2 为诚实值，Review 勿补边。

**不入库但提示词可叙述**：Peyton Rous（1910 年分离劳氏肉瘤病毒——文献渊源，c-src 之 v-src 出处）；Gebhard Koch（frontmatter 有载、正文无载——汉堡阶段仅叙述研究所）。

## 五、配色方案 【人物专属】

- **气质**：宾州小镇的沉静、UCSF 的学院蓝、揭开癌基因之谜的克制锋芒
- **主色**：`#2F5D50`（学院深绿——宾州丘陵与旧金山湾区的常青）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeSrc` c-src/v-src — 学院深绿 `#2F5D50`
  - `badgeOnco` 原癌基因 — 深青 `#0E7490`
  - `badgeChan` 校长岁月 — 深蓝 `#1E4E79`
  - `badgeHonor` 荣誉传承 — 暗红 `#7A2430`
- **背景母题**：细胞基因被病毒颗粒带走的示意图线条，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 癌基因细胞起源的证明者 / J. Michael Bishop 1936–2026 + 四色 badge + 头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、约克镇出身、葛底斯堡学院/哈佛 MD 1962、
    NIAID/汉堡 Heinrich Pette 研究所/UCSF 任职、诺奖 1989、核心领域）
03  核心贡献概览 — c-src 细胞基因鉴定 / 原癌基因家族 / 逆转录病毒致癌机制 / UCSF 校长
04  约克镇与葛底斯堡 (1936–1958) — 本科岁月、医学志向
05  哈佛 MD 与 NIH (1958–1967) — 1962 MD、NIAID 免疫与微生物学
06  汉堡一年 (1967–1968) — Heinrich Pette 研究所
07  UCSF 与 Varmus 相遇 (1968–) — 1968 加入 UCSF 教职、与 Varmus 的长期科学伙伴关系开始
08  v-src 之谜（核心贡献页）— Rous 1910 年分离的劳氏肉瘤病毒携带的 v-src 癌基因从何而来
09  c-src 的鉴定（核心页）— 细胞基因 c-src 是 v-src 的源头、原癌基因家族的发现潮
10  癌症的新图景 — 恶性肿瘤源于正常基因改变：病毒/辐射/化学物质皆可触发
11  1989 诺奖：与 Varmus 共享 — 获奖理由逐字呈现
12  UCSF 校长岁月 (1998–2009) — 第八任校长、Mission Bay 扩展、首个全校多样性战略规划、
    "advancing health worldwide" 新使命
13  荣誉与认可 — Dickson 1986、Lasker/Gairdner/Sloan 奖、Nobel 1989、ASCB 公共服务奖 1998、
    NMS 2003、ForMemRS 2008、Clark Kerr 2020
14  遗产与结尾 — 《How to win the Nobel Prize》、癌症分子机制的奠基 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生卒口径 | 1936-02-22 约克镇 ~ **2026-03-20** 逝于旧金山（肺炎），90 岁——刚逝世得主，生卒双写 |
| 无博士导师边 | frontmatter doctoral_advisor=Gebhard Koch 但**正文仅载"汉堡 Heinrich Pette 研究所一年"未点名导师**——按纪律不入库；哈佛 MD 亦无研究导师 |
| Varmus 边方向 | 两人是"长期科学伙伴"（colleague）+共享诺奖（co-honored）；Varmus 1970 年以其**博士后**身份加入——师生边建在 Varmus yaml（advisor 方向），Bishop 侧不重复建 |
| Rous 不建边 | v-src 出自 Rous 1910 年分离的劳氏肉瘤病毒——文献渊源，不建 influence 边 |
| 发现权表述 | "working with Varmus in the 1980s, discovered the first human oncogene c-Src"——两人共同，勿单归 |
| 页面极简 | page.md 无 Personal life 段、无引语、无学生名单——**全篇禁编引语/家人/学生**；书 How to Win the Nobel Prize（2003）可叙述 |
| 荣誉年份链 | Dickson 1986、Nobel 1989、ASCB 公共服务奖 1998、NMS 2003、ForMemRS 2008、Clark Kerr 2020——Lasker/Gairdner/Sloan 年份未载按名单呈现勿编年份 |
| 校长顺位 | UCSF 第八任校长（1998-2009）——Mission Bay 扩展、多样性规划、"advancing health worldwide"使命 |
| 学科身份 | 职业起点是免疫学家/微生物学家（NIAID），后转肿瘤病毒学——转轨叙事勿倒置 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| cellular origin of retroviral oncogenes | 逆转录病毒癌基因的细胞起源 | 获奖理由逐字对应 |
| c-src | 细胞 src 基因 | 病毒 v-src 的细胞源头 |
| v-src | 病毒 src 癌基因 | 劳氏肉瘤病毒携带 |
| proto-oncogene | 原癌基因 | 病毒癌基因的祖先、人类癌症突变靶点 |
| Rous sarcoma virus | 劳氏肉瘤病毒 | 1910 年 Rous 自鸡肉瘤分离 |
| Heinrich Pette Institute | 海因里希·佩特研究所 | 汉堡，1967-68 一年 |
| chancellor | （UCSF）校长 | 第八任，1998-2009 |
| Mission Bay | 米申湾校区 | 任内 UCSF 扩展工程 |
| NIAID | 国家过敏与传染病研究所 | 职业起点机构 |
| How to Win the Nobel Prize | 《如何赢得诺贝尔奖》 | 2003 年出版 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Falling Apart**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Bishop 与 Varmus 的发现把"癌症从何而来"这个庞然大物拆解到基因层面——肿瘤不是天谴，而是正常基因的"分崩离析"；Falling Apart 的解构感对应癌基因起源假说把疾病还原为分子事件的范式力量，也对应九十岁高龄谢幕的静默终章。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/J._Michael_Bishop/FallingApart.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
