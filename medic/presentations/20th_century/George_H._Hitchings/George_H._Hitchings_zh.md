# 医学家立传提示词（George H. Hitchings）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1988 年得主 George H. Hitchings（乔治·赫伯特·希钦斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/George_H._Hitchings/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：George Herbert Hitchings（1905-04-18 生于华盛顿州霍奎厄姆 ~ 1998-02-27 逝于北卡罗来纳州教堂山，享年 92 岁），美国生物化学家，Wellcome 研究实验室研究副总裁
- **气质关键词**：**理性药物设计之父、核酸拮抗剂的架构师、44 年搭档关系的另一方**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1988 条目，Black/Elion/Hitchings 三人共享；Hitchings 具体为化学治疗工作）：
  > "for their discoveries of important principles for drug treatment"（因其关于药物治疗重要原理的发现）
- **设计母题**：**天然化合物的"假面舞会"（antagonists of nucleic acid derivatives）**——设计类似物混入生物通路，让癌细胞自取灭亡；用「分子戴着天然化合物的面具」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/George_H._Hitchings/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/George_H._Hitchings/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=George_H._Hitchings_zh`、`VIDEO_NAME=George_H._Hitchings_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Hitchings 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | metadata field_of_work 明载 | 全篇 |
| 1 | chemotherapy | 化学治疗 | infobox Known for；诺奖具体引用其化疗工作 | 核心页 |
| 2 | pharmacology | 药理学 | metadata field_of_work 明载 | 全篇 |
| 3 | rational drug design | 理性药物设计 | 拮抗剂策略的开创 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Gertrude B. Elion | Hitchings → 研究助理/被指导者 | 1944 年招入 Wellcome 实验室，指导其嘌呤抗代谢物合成 |
| co-honored | Gertrude B. Elion | 无向 | 1988 诺贝尔生理学或医学奖三人共享 |
| co-honored | James W. Black | 无向 | 1988 同届诺奖三人共享（Black 的β受体阻滞剂/西咪替丁路线） |
| spouse | Beverly Reimer Hitchings | 无向 | 第一任妻子（1985 年去世） |
| spouse | Joyce Carolyn Shaver-Hitchings | 无向 | 医学博士，1989 年再婚（2009 年去世） |

**诚实值说明**：Hitchings 页无博士导师（哈佛 1933 PhD 未载导师）、无具名学生/其他合作者，relations=5 为诚实值；Elion 的 25+ 篇杜克合著学生在 Elion 侧叙述。

**不入库但提示词可叙述**：Triangle Community Foundation 创立（1983，公益非科研关系）；Medicinal Chemistry Hall of Fame 成员身份。

## 五、配色方案 【人物专属】

- **气质**：太平洋西北的雾蓝、分子"假面舞会"的机巧、实验室长桌上的 44 年
- **主色**：`#1F4E5F`（雾蓝绿——普吉特湾与 Wellcome 实验室）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeAntag` 核酸拮抗剂 — 雾蓝绿 `#1F4E5F`
  - `badgeChemo` 化学治疗 — 深蓝 `#1E4E79`
  - `badgeDrugs` 药物谱系 — 赭金 `#B07D2B`
  - `badgeHonor` 荣誉传承 — 暗红 `#7A2430`
- **背景母题**：戴面具的分子与代谢通路岔口，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 理性药物设计之父 / George H. Hitchings 1905–1998 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、霍奎厄姆出身、华盛顿大学/Harvard PhD 1933、
    Wellcome 研究实验室/杜克任职、诺奖 1988、核心领域）
03  核心贡献概览 — 拮抗剂策略 / 药物谱系 / 与 Elion 的 44 年 / 从白血病到 AZT
04  西北少年 (1905–1927) — 多城辗转成长、Franklin 高中致辞代表、华盛顿大学化学 cum laude、
    Friday Harbor 夏季站→1928 硕士
05  哈佛与博士 (1927–1933) — 教学 fellows 起步、哈佛医学院、1933 PhD、Alpha Chi Sigma
06  哈佛—凯斯西储—Wellcome (1933–1944) — 1942 入 Tuckahoe Wellcome 研究实验室
07  1944：Elion 到来 — 理性设计哲学：模仿天然化合物、让癌细胞"误食"人工化合物
08  早期药物：2,6-二氨基嘌呤与叶酸拮抗剂 — 白血病方向的确立
09  药物谱系（核心贡献页）— 诺奖自传引文：乙胺嘧啶（疟疾）/6-MP 与硫鸟嘌呤（白血病）/
    别嘌醇（痛风）/硫唑嘌呤（移植）/复方新诺明（细菌感染）→阿昔洛韦（疱疹）与 AZT（艾滋病）
10  1967 研究副总裁与传承 — Wellcome 研究掌门、1976 荣休科学家、杜克兼职教授 1970-85
11  1988 诺奖：三人共享 — 与 Elion（44 年搭档）、Black 共享，获奖理由逐字呈现
12  荣誉与认可 — Gairdner 1968、Passano 1969、de Villiers 1970、Cameron 1972、ForMemRS 1974、
    Golden Plate 1989、药物化学名人堂
13  公益与家庭 — 创立 Triangle Community Foundation（1983）、两任妻子
14  遗产与结尾 — 理性设计改变制药业、1998 逝世于教堂山 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名口径 | **yaml/入库用 manifest 形式 "George H. Hitchings"**；全名 George Herbert Hitchings |
| 1988 三人结构 | Hitchings 具体贡献为化学治疗（page.md 明文 "Hitchings specifically for his work on chemotherapy"）；Black 是抗高血压/抗溃疡路线——三人贡献勿互相混淆 |
| Elion 边方向 | Hitchings 招其入实验室并指导——advisor-student（Hitchings→Elion 方向）；两人无正式博士项目，note 已注明 |
| 诺奖自传引文 | page.md 以引用块载其诺奖自传药物清单段（pyrimethamine/6-MP/thioguanine/allopurinol/azathioprine/co-trimoxazole→acyclovir/zidovudine）——**英文原文可引**，是本篇最权威的药物谱系表述 |
| 无博士导师边 | 哈佛 1933 PhD 未载导师——**不建 advisor-in 边** |
| 死亡时序 | Elion 1999-02-21 逝世晚于 Hitchings 1998-02-27 一年；第二任妻子 Shaver-Hitchings 2009 年去世（死于他之后）——年表勿串 |
| 私生活口径 | 两任妻子均先于本篇陈述时点去世（Beverly 1985、Joyce 2009）——两条 spouse 边 note 已注明；Triangle Community Foundation 是其公益遗产 |
| 荣誉年份链 | Gairdner 1968、Passano 1969、de Villiers 1970、Cameron 1972、ForMemRS 1974、Nobel 1988、Golden Plate 1989——勿串 |
| 职年链 | 哈佛/凯斯西储博士后段 → 1942 Wellcome Tuckahoe → 1967 研究副总裁 → 1976 Scientist Emeritus → 杜克兼职教授 1970-85——勿串 |
| 引语红线 | 仅诺奖自传引用块（见上）可引；其余无直接引语，禁编 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| important principles for drug treatment | 药物治疗的重要原理 | 获奖理由逐字对应 |
| antagonists of nucleic acid derivatives | 核酸衍生物拮抗剂 | 其研究纲领核心 |
| 2,6-diaminopurine | 2,6-二氨基嘌呤 | 早期抗白血病化合物 |
| folic acid antagonist | 叶酸拮抗剂 | p-氯苯氧基二氨基嘧啶 |
| 6-mercaptopurine | 6-巯基嘌呤 | 与 Elion 共同开发 |
| co-trimoxazole | 复方新诺明 | 甲氧苄啶复方 |
| chemotherapy | 化学治疗 | 其诺奖具体引用领域（广义药物化疗） |
| Burroughs-Wellcome | 宝威公司 | 今 GSK，Tuckahoe 实验室 |
| Triangle Community Foundation | 三角社区基金会 | 1983 创立 |
| Puget Sound Biological Station | 普吉特海湾生物站 | Friday Harbor，硕士论文来源 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Mirage**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Hitchings 的策略像一场精心编排的海市蜃楼——让癌细胞在"看似天然的化合物"幻影中自我毁灭；从霍奎厄姆到哈佛到北卡研究三角，Mirage 的流转感对应其横跨学术界与产业界的一生，也对应"幻影治真病"这一设计哲学的诗意。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/George_H._Hitchings/Mirage.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
