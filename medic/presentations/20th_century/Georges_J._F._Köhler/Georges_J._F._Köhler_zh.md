# 医学家立传提示词（Georges J. F. Köhler）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1984 年得主 Georges J. F. Köhler（乔治·让·弗朗茨·克勒）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Georges_J._F._Köhler/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Georges Jean Franz Köhler（1946-04-17 生于德国慕尼黑（盟占时期）~ 1995-03-01 逝于德国弗莱堡，享年 48 岁）
- **气质关键词**：**杂交瘤技术的共同发明人、单克隆抗体时代的开启者、英年早逝的天才**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1984 条目，与 Milstein 共享一半、Jerne 独享另一半）：
  > "for theories concerning the specificity in development and control of the immune system and the discovery of the principle for production of monoclonal antibodies"（因免疫系统发育与控制特异性的理论及单克隆抗体生产原理的发现）
  - Köhler/Milstein 侧对应"单克隆抗体生产原理"（杂交瘤技术 1975）；Jerne 侧为理论——两层务必分层。
- **设计母题**：**细胞融合（hybridoma）**——产抗体 B 细胞与不朽骨髓瘤细胞融合成永续分泌系的意象：以两圆融合成新圆、持续分泌的图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Georges_J._F._Köhler/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Georges_J._F._Köhler/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Georges_J._F._Köhler_zh`、`VIDEO_NAME=Georges_J._F._Köhler_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | immunology | 免疫学 | infobox Fields；抗体多样性主线 |
| 1 | hybridoma technology | 杂交瘤技术 | 1975 Nature 论文，单抗生产原理 |
| 2 | antibody diversity | 抗体多样性 | 博士起的研究主线 |
| 3 | biotechnology | 生物技术 | 单抗的诊断与治疗转化 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Fritz Melchers | 对方 → 导师 | 弗莱堡大学博士导师（免疫应答与抗体产生；infobox Doctoral advisor 明载） |
| advisor-student | César Milstein | 对方 → 导师 | MRC LMB 博士后导师（1974-04 至 1976-03，EMBO 奖学金；杂交瘤合作） |
| colleague | Niels Kaj Jerne | 无向 | 巴塞尔免疫学研究所所长（1976 回所约十年，其下设所） |
| spouse | Claudia Reintjes | 无向 | 1968 结婚，三子女 Katharina/Lucia/Fabian；求学期间曾开出租养家 |
| co-honored | César Milstein | 无向 | 1984 诺贝尔生理学或医学奖共享一半（单克隆抗体生产原理） |
| co-honored | Niels Kaj Jerne | 无向 | 1984 诺贝尔生理学或医学奖（Jerne 独享一半为理论） |

**不入库但提示词可叙述**：父亲 Karl Köhler（德）与母亲 Raymonde（法裔，家世叙述）；1984 Lasker 与 Milstein 共享（一次性奖项关系）。

## 五、配色方案 【人物专属】

- **气质**：年轻的锋芒、实验的巧思、巴塞尔与弗莱堡的沉静
- **主色**：`#37474F`（蓝灰——MRC LMB 实验台的金属色）+ 香槟金诺奖色
- **badge 四分类色**：`badgeHybrid` 杂交瘤 蓝灰 `#37474F`；`badgeMab` 单克隆抗体 深蓝 `#1E4E79`；`badgeBasel` 巴塞尔岁月 青绿 `#0E7C7B`；`badgeMPG` 马普所 琥珀 `#C07A2A`
- **背景母题**：两圆融合成新圆持续分泌的图案，呼应「细胞融合」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 杂交瘤技术的共同发明人 / Georges J. F. Köhler 1946–1995 + 四色 badge + 右上头像 + 国籍行（Germany）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1946-04-17 慕尼黑 ~ 1995-03-01 弗莱堡、
    弗莱堡大学生物学、MRC LMB 博士后 1974–76、马普免疫生物学研究所所长 1986–1995、诺奖 1984）
03  核心贡献概览 — 杂交瘤 / 单抗定义特异性 / 转基因小鼠 / 抗体多样性
04  占领期的慕尼黑婴儿 (1946) — 德父法母的跨国家庭；求学时开出租养家的轶事
05  弗莱堡与 Melchers 门下 — 生物学、博士论文：免疫应答与抗体产生
06  剑桥 MRC LMB (1974–1976)（核心贡献页）— EMBO 奖学金、Milstein 实验室的抗体多样性问题
07  1975：杂交瘤诞生（核心贡献页）— 免疫动物淋巴细胞 × 骨髓瘤细胞 → 杂交瘤；
    预定特异性抗体的连续培养；Nature 论文
08  从多抗到单抗 — 传统抗血清 vs 单抗的均一特异性；鉴定/纯化/定量的精度革命
09  巴塞尔免疫学研究所 (1976–1986) — Jerne 主持的大所；淋巴细胞杂交细胞、
    1980s 转基因小鼠研究自体耐受
10  1984 诺奖 — Jerne（理论）+ Köhler/Milstein（单抗原理）；Nobel 讲演
    "Derivation and diversification of monoclonal antibodies"；Lasker 同年共享
11  马普免疫生物学研究所 (1986–1995) — 弗莱堡所长至终；抗体形成/淋巴细胞/
    免疫调节模型
12  家庭 — 1968 与 Claudia Reintjes 结婚、三子女；家庭与实验室并重
13  英年早逝 — 1995-03-01 弗莱堡辞世（48 岁，心脏疾患——contemporary accounts 口径）
14  遗产与结尾 — 单抗：从试剂到诊断到疗法（抗体工程时代）；马普学会的盖棺定论
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 双导师结构 | 弗莱堡博士导师 **Fritz Melchers**（infobox Doctoral advisor）；MRC LMB 博士后导师 **César Milstein**（frontmatter 亦列；正文 1974-04~1976-03）——两条 advisor 边方向相同、阶段注记不同 |
| 1975 论文 | "Continuous cultures of fused cells secreting antibody of predefined specificity"（Köhler 与 Milstein，Nature 1975）——两人署名对等，叙述勿偏重任何一方 |
| 1984 两半结构 | Jerne 独享一半（理论）；Köhler+Milstein 共享另一半（单抗原理）——citation 是合写一句，Köhler 篇侧重单抗原理 |
| hybridoma 命名 | 术语由 **Leonard Herzenberg** 在 Milstein 实验室休假期间（1976–77）创造——出自 Milstein 篇，Köhler 篇可提可不提，若提须注明命名者 |
| Basel 主管关系 | 巴塞尔研究所由 Jerne 任所长（1969–1980），Köhler 1976 回所为成员——用 colleague（隶属共事），勿写成师生 |
| 年龄对比 | 诺奖时 38 岁（三人中最年轻）；1995 年 48 岁因心脏疾患去世（"contemporary accounts attributed"口径）——英年早逝是本篇情感落点 |
| 国籍 | 生于盟占时期慕尼黑；citations json country=West Germany；manifest=Germany——yaml 用 Germany，正文可交代时代背景 |
| 出租车轶事 | 求学时开出租贴补家用（biographical accounts 口径 "reportedly"）——照页面措辞保留传闻语气 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| hybridoma | 杂交瘤 | B 淋巴细胞 × 骨髓瘤细胞融合体 |
| monoclonal antibody | 单克隆抗体 | 均一特异性抗体 |
| myeloma cell | 骨髓瘤细胞 | 融合用的 immortal 亲本 |
| antibody diversity | 抗体多样性 | 其研究主线 |
| B cell | B 淋巴细胞 | 产抗体细胞 |
| EMBO fellowship | EMBO 奖学金 | 1974 赴剑桥资助 |
| transgenic mouse | 转基因小鼠 | 1980s 巴塞尔新方向 |
| self-tolerance | 自身耐受 | 转基因小鼠研究对象 |
| MRC Laboratory of Molecular Biology | MRC 分子生物学实验室 | 剑桥；杂交瘤诞生地 |
| Max Planck Institute of Immunobiology | 马普免疫生物学研究所 | 弗莱堡 1986 起任所长 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Eternals**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：杂交瘤把短暂的生命变成"永续分泌的细胞系"——"Eternals" 的永恒感正对应单抗技术的长青：发明者英年早逝，而这项技术至今仍在诊断与治疗中生生不息。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Georges_J._F._Köhler/Eternals.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
