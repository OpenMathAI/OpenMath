# 医学家立传提示词（Stanley B. Prusiner）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1997 年得主 Stanley B. Prusiner（斯坦利·本·普鲁西纳）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Stanley_B._Prusiner/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Stanley Ben Prusiner（1942-05-28 生于美国艾奥瓦州得梅因，在世）
- **气质关键词**：**朊毒体的发现者、全新感染原理的提出者、对抗正统二十年终获平反的异端**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1997 条目，**独得**）：
  > "for his discovery of Prions - a new biological principle of infection"（因他发现朊毒体——一种新的感染生物学原理）
- **设计母题**：**错误折叠的复制（misfolded protein templating）**——正常蛋白被错误折叠构象"策反"、沉积成海绵样空洞的意象：以蛋白链折叠翻转+脑组织海绵空洞的图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Stanley_B._Prusiner/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Stanley_B._Prusiner/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Stanley_B._Prusiner_zh`、`VIDEO_NAME=Stanley_B._Prusiner_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | prion diseases | 朊毒体病 | 朊毒体发现，1997 诺奖核心 |
| 1 | neurology | 神经病学 | infobox Fields；UCSF 神经科住院医师出身 |
| 2 | infectious diseases | 感染性疾病 | infobox Fields；羊瘙痒症/疯牛病/CJD |
| 3 | biochemistry | 生物化学 | 朊毒体蛋白的纯化与构象研究 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Earl Stadtman | 对方 → 导师 | NIH 时期（三年）在其实验室研究大肠杆菌谷氨酰胺酶 |

**在世者关系少为诚实值**（1 条）：page.md 未载博导（宾大 BA/MD）、未载配偶姓名与子女姓名（仅 Children 2）——Review 勿补造边；提示词注明防 Review 误判。**不入库但提示词可叙述**：团队专家 D. E. Garfin/D. P. Stites/W. J. Hadlow/C. M. Eklund（"his team of experts" 仅列名）；Tikvah Alper（淀粉样蛋白观念的先行提出者，被 Prusiner 1998 PNAS 引述，思想源流不建边）；Gajdusek/Manuelidis/Bastian（See also 提及，朊毒体争议史人物，不建边）。

## 五、配色方案 【人物专属】

- **气质**：异端的孤勇、神经科的冷静、二十年对抗正统的韧性
- **主色**：`#6E2B2B`（脑髓深红——海绵样脑病的警示之色）+ 香槟金诺奖色
- **badge 四分类色**：`badgePrion` 朊毒体 深红 `#6E2B2B`；`badgeScrapie` 羊瘙痒症 青绿 `#0E7C7B`；`badgeBSE` 疯牛病 深蓝 `#16324F`；`badgeIND` 神经退行疾病研究所 琥珀 `#C07A2A`
- **背景母题**：蛋白链折叠翻转+脑组织海绵空洞图案，呼应「错误折叠的复制」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 朊毒体的发现者 / Stanley B. Prusiner 1942– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1942-05-28 得梅因、宾大 BA/MD、
    UCSF 神经科、IND 创所所长 1999、诺奖 1997）
03  核心贡献概览 — 朊毒体概念 / 羊瘙痒症与疯牛病 / CJD / 蛋白构象致病原理
04  得梅因与辛辛那提 (1942–1960) — 犹太家庭、Walnut Hills 高中"小天才"
    （Boxelder 虫驱避剂研究）、宾大化学 BA 与 MD
05  UCSF 住院医与 NIH (1968–1974) — UCSF 内科实习、NIH 三年
    Stadtman 实验室（大肠杆菌谷氨酰胺酶）、回 UCSF 完成神经科住院医
06  1974 加入 UCSF 神经科 — 遇到一位 CJD 患者开启朊毒体之路（研究转向）；UC Berkeley 兼职
07  异端之说（核心贡献页）— 羊瘙痒症/疯牛病让脑成海绵；Alper 先行提出
    淀粉样蛋白观念；Prusiner 提出"蛋白本身即病原"——挑战核酸作为唯一遗传载体的正统
08  命名 prion — proteinaceous + infectious 的合成词（PREE-on）；1998 PNAS
    综述"truly heretical"引语可引
09  二十年对抗正统 — 被斥为异端、坚持提纯与验证；团队 Garfin/Stites/Hadlow/
    Eklund 自 1970s 早期的工作
10  疾病谱 — 羊瘙痒症、疯牛病（BSE）、人类 CJD 等 TSE；错误折叠蛋白的
    自我扩增机制
11  IND 与神经退行疾病 (1999–) — 创立 UCSF 神经退行疾病研究所：
    CJD/阿尔茨海默/突触核蛋白病/tau 病——错误折叠蛋白的共同逻辑
12  荣誉与认可 — Potamkin/Metlife 1991、Lounsbery/Dickson/Gairdner 1993、
    Lasker 1994、Erlich 1995、Wolf/Keio/Golden Plate 1996、Horwitz 1997、
    Nobel/ForMemRS 1997、富兰克林奖章 1998、国家科学奖章 2010
13  学术身份 — NAS 1992（2007 入理事会）、AAAS 1993、美国哲学会 1998、
    医科院 1992；UCSF/UC Berkeley 各职
14  遗产与结尾 — 朊毒体原理：超越中心法则教条的感染生物学；从异端到教科书的二十年
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1997 独得 | 单独得主（"for his discovery"）；获奖理由含 "Prions - a new biological principle of infection" 逐字呈现 |
| 异端叙事 | page.md 明载 "heretical idea"/"truly heretical when it was introduced"——可写争议史，引语用 1998 PNAS 综述原句；勿渲染成人身攻击战 |
| Tikvah Alper | "amyloidogenic protein" 观念由 **Alper** 先行提出（Prusiner 引述）——思想源流归属写清，勿写成 Prusiner 凭空首创；Alper 不建边 |
| Stadtman 边 | NIH 三年在 **Earl Stadtman** 实验室研究大肠杆菌谷氨酰胺酶——advisor-student（方向 advisor）承载；注意 NASA/NIH 缩写与 Stadtman 夫妇（Earl 与 Noreen）区分 |
| 命名 | prion = proteinaceous + infectious 合成词（读 PREE-on）——命名细节 page.md 明载 |
| 团队成员 | Garfin/Stites/Hadlow/Eklund 仅列名（"team of experts"），无 wiki 链接不入库 |
| 关系=1 | 全批最少；在世者+页面简短（无配偶姓名/导师仅 NIH 一站）——诚实值，提示词注明 |
| 在世者生卒 | 仅生年 1942-05-28，无卒年——封面 1942– 开放区间；2024 年仍活跃（照片年份） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| prion | 朊毒体 | proteinaceous+infectious 合成词 |
| scrapie | 羊瘙痒症 | 绵羊 TSE |
| bovine spongiform encephalopathy (BSE) | 牛海绵状脑病（疯牛病） | TSE |
| Creutzfeldt–Jakob disease (CJD) | 克雅氏病 | 人类朊毒体病 |
| transmissible spongiform encephalopathy | 传染性海绵状脑病 | TSE 总称 |
| amyloidogenic protein | 淀粉样蛋白 | Alper 先行观念 |
| misfolded protein | 错误折叠蛋白 | IND 研究的共同逻辑 |
| Institute for Neurodegenerative Diseases (IND) | 神经退行疾病研究所 | 1999 创立 UCSF |
| synucleinopathies / tauopathies | 突触核蛋白病 / tau 病 | IND 研究谱系 |
| glutaminase | 谷氨酰胺酶 | NIH 时期研究对象 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Lonesome**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：提出"蛋白即病原"的二十年间，Prusiner 站在整座正统的对面——"Lonesome" 的孤寂感承载异端者的长夜；1997 斯德哥尔摩的掌声是孤独者最好的和声。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Stanley_B._Prusiner/Lonesome.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
