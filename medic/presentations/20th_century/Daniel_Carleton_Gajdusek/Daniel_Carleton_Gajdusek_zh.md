# 医学家立传提示词（Daniel Carleton Gajdusek）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1976 年得主 Daniel Carleton Gajdusek（丹尼尔·卡尔顿·盖杜谢克）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Daniel_Carleton_Gajdusek/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Daniel Carleton Gajdusek（1923-09-09 生于纽约扬克斯 ~ 2008-12-12 逝于挪威特罗姆瑟，享年 85 岁）
- **气质关键词**：**库鲁病的破译者、「非常规病毒」的命名者、争议与科学遗产并存的复杂人物**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1976 条目，两人共享同句）：
  > "for their discoveries concerning new mechanisms for the origin and dissemination of infectious diseases"（因其关于传染病起源与传播新机制的发现）
- **设计母题**：**慢性的谜（the slow mystery）**——库鲁病漫长潜伏、不引发免疫应答的「非常规病毒」；用「新几内亚山地轮廓与一条缓慢延伸的潜伏线」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Daniel_Carleton_Gajdusek/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Daniel_Carleton_Gajdusek/`。Makefile 复制后设 `MAIN=Daniel_Carleton_Gajdusek_zh`、`VIDEO_NAME=Daniel_Carleton_Gajdusek_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Gajdusek 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学 | 库鲁病传染性证明，1976 诺奖核心 | 封面、核心页 |
| 1 | prion disease research | 朊病毒病研究 | 库鲁/羊瘙痒症/克雅病的早期发现（Known for） | 核心页 |
| 2 | neurology | 神经病学 | 库鲁的首份医学描述 | 核心页 |
| 3 | anthropology | 人类学 | Fore 人群的田野工作与流行病学调查 | 视野页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 正文/infobox 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Baruch Samuel Blumberg | 无向 | 1976 诺贝尔生理学或医学奖两人共享（官方理由句同一） |
| colleague | Vincent Zigas | 无向 | 新几内亚 Fore 地区医官：将其引入库鲁问题，1957 年起共同调查，1977 合著论文 |
| colleague | Michael Alpers | 无向 | 共同证明库鲁可传播；转达 Lindenbaum/Glasse 人类学假说并鼓励黑猩猩接种实验 |
| colleague | Clarence Gibbs Jr | 无向 | 共同证明库鲁可传播；1966 Nature / 1969 Science 论文合作者 |

**不入库但提示词可叙述**：父母 Karol Gajdusek（斯洛伐克裔）/Ottilia Dobróczki（匈牙利裔，仅具名）；Shirley Lindenbaum 与 Robert Glasse、John D. Mathews（食人俗传播假说的真正提出者与整合者——归属澄清，非其合作者）；Stanley Prusiner（朊蛋白的后续鉴定者，1997 诺奖——知识线仅叙述）；Chris Brand（为其量刑鸣不平者）；Bosse Lindquist（纪录片导演）；56 名带美抚养的儿童（事件叙述，非白名单关系）。

## 五、配色方案 【人物专属】

- **气质**：新几内亚的山雾、慢病毒的暗流、光环与阴影并存
- **主色**：`#52307C`（高地暗紫——山国迷雾与道德的灰域）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeKuru` 库鲁与慢感染 — 暗紫 `#52307C`
  - `badgePrion` 朊病毒前夜 — 深红 `#8C1F28`
  - `badgeField` 田野与人类学 — 苔绿 `#175E54`
  - `badgeShade` 罪与罚 — 军灰 `#37474F`
- **背景母题**：山地轮廓与缓慢延伸的潜伏线，终点是一枚问号。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 库鲁病的破译者 / D. Carleton Gajdusek 1923–2008 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、扬克斯出身、罗切斯特大学 1943、哈佛 MD 1946、
    NINDS 中枢神经系统研究实验室主任 1970–1996、诺奖 1976、核心领域）
03  核心贡献概览 — 库鲁的传染性 / 非常规病毒 / 朊病毒病群谱 / 争议人生
04  扬克斯与移民家庭 (1923–1946) — 斯洛伐克裔父、匈牙利裔母；罗切斯特理化生数；哈佛 MD 1946
05  博士后与军旅 (1946–1954) — 哥伦比亚/加州理工/哈佛博士后；Walter Reed 病毒学家
06  墨尔本与转折 (1954) — Walter and Eliza Hall 研究所访问研究员：诺奖工作的起点
07  Zigas 与库鲁 (1957)（核心贡献页一）— 被引入库鲁问题；首份医学描述；「笑病」讹称与 risus sardonicus
08  排除法 (1957–1965) — 无常规病原、无营养缺乏、无毒素（1977 论文回溯）
09  传播性实验 (1965)（核心贡献页二）— 与 Alpers/Gibbs：黑猩猩脑组织接种致病；确立可传播
10  「非常规病毒」 (1977) — 长潜伏、不引发免疫应答、无可见核酸；与羊瘙痒症/克雅病同群
11  1976 共享诺奖 — 与 Blumberg；官方理由句；朊蛋白后由 Prusiner 鉴定（1997 诺奖）
12  假说归属的澄清 — 食人俗传播假说属 Lindenbaum/Glasse/Mathews（1968 Lancet）；Gajdusek 最初抵触；其引语前后矛盾如实呈现
13  罪与罚 (1996–1998)（克制页）— 1996 指控、1997 认罪、12 个月监禁；自放逐欧洲；同行求情与纪录片的追问
14  遗产与结尾 — 2008 卒于特罗姆瑟；科学贡献与道德阴影的双重遗产 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1976 两人共享同句理由 | 与 Blumberg 共享且官方理由同句（"for their discoveries concerning new mechanisms for the origin and dissemination of infectious diseases"）——引用以 citations json 逐字为准 |
| 犯罪事实的处理（★ 全篇最大纪律点） | page.md 明载其为「convicted child sex offender」：1996 起诉、1997 认罪、判 12 个月监禁（辩诉交易）、1998 获释后自我流放欧洲、2008 卒于特罗姆瑟——**事实必须完整呈现、不可省略亦不可渲染**；涉及未成年人的细节一律不复述 |
| 假说归属 | 食人俗（cannibalism）传播假说由 **Lindenbaum/Glasse** 夫妇首先提出、1968 与 Mathews 在 Lancet 整合证据——page.md 明载 Gajdusek「常被错误记功」，立传必须写清归属 |
| 引语的前后矛盾 | 其 2000s 称「完全喝醉的人也会得出结论」，诺奖演讲却说「slow virus 经结膜/鼻/皮肤接触传播」——两面如实呈现 |
| Zigas 的角色 | 引入者+共同调查者（colleague），非下属；「laughing sickness」是大众媒体讹称 |
| 实验伦理 | 黑猩猩接种实验（颅骨钻孔置入脑组织匀浆）——方法学如实陈述 |
| 56 名儿童 | 「brought 56 mostly male children back to live with him」——与犯罪事实相关，克制陈述数字与背景即可，禁止细节化 |
| 求情与批评 | 同行求情（认为罪轻于贡献）与 Brand 的「反精英论」批评——两面呈现，勿单边 |
| Prusiner 衔接 | Gajdusek 提出「非常规病毒」未鉴定核酸；朊蛋白由 Prusiner 鉴定（1997 诺奖）——知识递进线仅叙述 |
| 晚年 | 阿姆斯特丹居住、特罗姆瑟过冬（极夜助其工作）；2008-12-12 卒于特罗姆瑟（探望同事期间） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| kuru | 库鲁病 | Fore 人群的传染病 |
| unconventional virus | 非常规病毒 | 其 1977 命名（后证实为朊蛋白） |
| slow virus | 慢病毒 | 其诺奖演讲用语 |
| prion | 朊病毒/朊蛋白 | Prusiner 后续鉴定 |
| scrapie | 羊瘙痒症 | 同群动物病 |
| Creutzfeldt–Jakob disease | 克雅病 | 同群人类病 |
| risus sardonicus | 痉笑 | 「笑病」讹称的来源症状 |
| Fore people | 弗雷人 | 新几内亚研究人群 |
| cross-perfusion… inoculation | （脑组织）接种实验 | 1965 传播性确立方法 |
| incubation period | 潜伏期 | 非常规病毒特征之一 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Ascension**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从纽约移民家庭到新几内亚高地、从被质疑的「非常规病毒」假说到诺贝尔奖——「攀升」对应其科学轨迹；而乐曲的暗色段落也承载其人生的道德阴影——双重遗产的音乐化。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Daniel_Carleton_Gajdusek/Ascension.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
