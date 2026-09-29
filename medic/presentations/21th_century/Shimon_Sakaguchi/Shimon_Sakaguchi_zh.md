# 医学家立传提示词（Shimon Sakaguchi）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2025 年得主 Shimon Sakaguchi（坂口志文）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Shimon_Sakaguchi/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Shimon Sakaguchi（坂口 志文，1951-01-19 生于日本滋贺县长滨市，在世）
- **气质关键词**：**调节性 T 细胞的发现者、免疫刹车的主人、被质疑二十年后被验证的人**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2025 条目，与 Brunkow、Ramsdell 三人共享同一理由）：
  > "for their discoveries concerning peripheral immune tolerance"（因他们发现外周免疫耐受机制）
- **设计母题**：**免疫的刹车（CD4+CD25+ 刹车细胞）**——CD4+CD25− 细胞引发自身免疫、补回 CD25+ 刹车细胞即恢复平静的意象：以对比图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Shimon_Sakaguchi/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Shimon_Sakaguchi/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Shimon_Sakaguchi_zh`、`VIDEO_NAME=Shimon_Sakaguchi_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | regulatory T cells | 调节性 T 细胞 | 1995 发现 CD4+CD25+ Treg，2025 诺奖核心 |
| 1 | immunology | 免疫学 | infobox Fields 次项 |
| 2 | pathology | 病理学 | infobox Fields 首项；实验病理学讲席 |
| 3 | immune tolerance | 免疫耐受 | 自身免疫抑制与耐受维持 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Mary E. Brunkow | 无向 | 2025 诺贝尔生理学或医学奖三人共享（外周免疫耐受） |
| co-honored | Fred Ramsdell | 无向 | 2025 诺贝尔生理学或医学奖三人共享（外周免疫耐受） |
| co-honored | Ethan M. Shevach | 无向 | 2004 William B. Coley 奖共享 |
| co-honored | Alexander Rudensky | 无向 | 2017 Crafoord 奖共享（与 Ramsdell） |

**在世者关系少为诚实值**（4 条，全为共享奖）：page.md 未载博士导师/学生/配偶——Review 勿补造边。**不入库但提示词可叙述**：Fred Gage（2008 Keio 奖共享，一次性奖项关系）；BALB/c 无胸腺小鼠实验（实验体系非人物）；US 博士后（Johns Hopkins/Stanford/Scripps，导师未具名不建边）。

## 五、配色方案 【人物专属】

- **气质**：隐忍、逆流、二十年守得云开
- **主色**：`#7A1E28`（大阪深红——免疫刹车的警醒之色）+ 香槟金诺奖色
- **badge 四分类色**：`badgeTreg` Treg 发现 深红 `#7A1E28`；`badgeBrake` 免疫刹车 青绿 `#0E7C7B`；`badgeFoxp3` FOXP3 整合 深蓝 `#16324F`；`badgeAuto` 自身免疫 琥珀 `#C07A2A`
- **背景母题**：脱缰细胞群被一组刹车细胞安抚的对比图案，呼应「免疫的刹车」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 免疫刹车的发现者 / Shimon Sakaguchi 1951– + 四色 badge + 右上头像 + 国籍行（Japan）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1951-01-19 长滨、京都大学 MD 1976/PhD 1982、
    大阪大学特任教授、京都大学名誉教授、诺奖 2025）
03  核心贡献概览 — Treg 发现 1995 / 刹车细胞实验 / FOXP3 整合 2003 / 外周耐受图景
04  长滨少年与京都医学 (1951–1976) — 京都大学医学部、MD 1976
05  博士与留美 (1976–1987) — 京都 PhD 1982、Lucille P. Markey Scholar、
    Johns Hopkins 与 Stanford 博士后 1983–87、Scripps 助理教授
06  归国与转向 (1991–1998) — Riken、东京都老人综合研究所免疫病理部部长
07  1995：发现刹车细胞（核心贡献页）— BALB/c 无胸腺小鼠注入剔除 CD25+ 的 CD4+ 细胞
    → 自身免疫病（甲状腺炎/胃炎）；回补 CD4+CD25+ 细胞 → 自身免疫被阻止；
    Treg 作为此前未知的 T 细胞亚群
08  二十年逆流 — Treg 概念长期被质疑、终被 FOXP3（2001/2003）与领域验证
09  2003：FOXP3 掌舵 Treg（核心贡献页）— 与 Brunkow/Ramsdell 的 FOXP3 分子基础合流；
    Sakaguchi 组证明 FOXP3 对 Treg 发育与功能的关键性
10  京都岁月 (1998–2011) — 京都大学再生医学科学研究所实验病理学教授/所长 2007–2011
11  大阪大学 (2011–) — 免疫学前沿研究中心；特任教授
12  荣誉与认可 — Coley 2004（与 Shevach）、Keio 2008（与 Gage）、紫绶褒章 2009、
    朝日奖 2011、NAS 外籍院士 2012、Gairdner 2015、Crafoord 2017、文化勋章 2019、
    Erlich/Koch 2020、Debrecen 2023、Nobel 2025
13  三人分工 — Sakaguchi（Treg 细胞发现）、Brunkow/Ramsdell（FOXP3 基因与 IPEX）——
    citation 同一句、侧重分层
14  遗产与结尾 — 外周耐受医学：自身免疫、移植、癌症免疫的三重回响
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| Treg 发现年份 | 1995 年（CD4+CD25+ 调节性 T 细胞）；2003 年证明 FOXP3 对 Treg 发育与功能的关键性——两个里程碑勿混 |
| 实验逻辑 | 先注 CD4+CD25−（致病）→ 出现自身免疫；再回补 CD4+CD25+（阻止）→ 免疫平静——方向勿写反 |
| FOXP3 归属 | FOXP3 基因鉴定是 Brunkow/Ramsdell（2001）；Sakaguchi 组 2003 证明 FOXP3 主控 Treg——两侧贡献分层，勿互串 |
| 无师承边 | page.md 未载博士导师（京都 MD 1976/PhD 1982 无导师姓名）——师承边为零是诚实值，勿从别处补 |
| 名字 | 坂口 志文（Sakaguchi Shimon）；"Shimon" 非英文名——勿误写 Simon |
| 京都与大阪 | 京都大学：MD/PhD、1998–2011 教授（2007–2011 兼所长）、现名誉教授；大阪大学：2011 起、现特任教授——两校身份勿混 |
| 在世者生卒 | 仅生年 1951-01-19，无卒年——封面用 1951– 开放区间 |
| 获奖理由 | 官方理由三人同一句 "peripheral immune tolerance"；Sakaguchi 个人侧重是 Treg 细胞的发现——引用分层 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| regulatory T cell (Treg) | 调节性 T 细胞 | Sakaguchi 1995 发现 |
| CD4+CD25+ | 双阳性标记 | Treg 的表型标记 |
| athymic mouse | 无胸腺小鼠 | BALB/c 裸鼠实验体系 |
| autoimmune disease | 自身免疫病 | 甲状腺炎/胃炎等示例 |
| immune tolerance | 免疫耐受 | 外周耐受的核心 |
| FOXP3 | FOXP3 转录因子 | Treg 主控基因（2003 整合） |
| peripheral tolerance | 外周耐受 | 胸腺之外的耐受机制 |
| lucille P. Markey Scholar | Markey 学者 | 留美资助身份 |
| Order of Culture | 日本文化勋章 | 2019 |
| experimental pathology | 实验病理学 | 京都讲席名称 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Savage**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：免疫系统的野性攻击被一组"刹车细胞"驯服——"Savage" 的张力对应失控的自身免疫与 Treg 带来的秩序；同时呼应 Sakaguchi 二十年逆流而行的学术韧性。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Shimon_Sakaguchi/Savage.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
