# 医学家立传提示词（Ardem Patapoutian）

> OpenMedic 项目、21 世纪诺贝尔生理学或医学奖 2021 年得主（阿德姆·帕塔普蒂安，机械力感受通道 PIEZO1/2 的发现者）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Ardem Patapoutian（1967-10-01 生于黎巴嫩贝鲁特，在世；亚美尼亚裔）
- **气质关键词**：**触觉通道 PIEZO1/2 的发现者、从贝鲁特战火走出的难民科学家、首位亚美尼亚裔诺贝尔奖得主** —— 2021 获奖理由（与 David Julius 两人共享）：
  > "for the discovery of receptors for temperature and touch"（因发现温度与触觉的受体）
- **设计母题**：**被按下的离子通道**。细胞被触碰时，PIEZO 通道像一扇被推开的门让电流涌入——"压力"（Piezo 源自希腊语）是它的名字。视觉隐喻：一枚被指尖按出形变的膜圆盘，电流自 pore 迸发。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Ardem_Patapoutian/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/21th_century/Ardem_Patapoutian/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准——生日双值裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/21th_century/Ardem_Patapoutian/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Ardem_Patapoutian_zh`、`VIDEO_NAME=Ardem_Patapoutian_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/21th_century/Ardem_Patapoutian/images.txt`（2022 照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。插图可用 2022 亚美尼亚邮票照。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Ardem_Patapoutian.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | molecular biology | 分子生物学 | PIEZO1/2 基因失活筛选，2021 诺奖核心 | 核心页 |
| 1 | neuroscience | 神经科学 | 触觉/本体感觉/痛觉的通道基础 | 核心页 |
| 2 | mechanotransduction | 机械力转导 | 机械敏感离子通道的功能基因组学 | 研究页 |
| 3 | ion channels | 离子通道 | 温度/机械力/细胞体积敏感通道 | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Barbara Wold | 导师 | Caltech 博士导师（1996，MyoD 家族基因与小鼠发育） |
| advisor-student | Louis F. Reichardt | 导师 | UCSF 博士后导师 |
| co-honored | David Julius | 无向 | 2021 诺贝尔生理学或医学奖两人共享（发现温度与触觉受体） |
| spouse | Nancy Hong | 无向 | 风险投资人，居加州 Del Mar |

> 在世者，relations=4 为诚实值（page.md 无学界师承以外的私人关系记载），**Review 勿误判缺漏**。
> 不入库：父亲 Sarkis Patapoutian（笔名 Sarkis Vahakn，诗人兼会计师，非学界人物——page.md 明载但不入库防噪声，家庭叙事入幻灯片）；母亲 Haiguhi Adjemian（贝鲁特亚美尼亚学校校长，同上）；兄 Ara、妹 Houry；儿子 Luca；幼时好友记者 Vicken Cheterian。
> 库内当时无 Barbara Wold / Louis F. Reichardt / Nancy Hong 记录，均由本 yaml 新建 stub；David Julius 已由本批 Julius yaml 规范化（#4837 UPD）。

## 五、配色方案 【人物专属】

- **气质**：地中海的暖沙 + 亚美尼亚石刻的赭色 + 机械力的一声脆响
- **主色**：赭石橙 `#8C5A2B`（亚美尼亚石刻与"压力"的厚重）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` PIEZO1/2 — 赭石橙 `#8C5A2B`
  - `badgeB` 温度通道 — 辣椒红 `#B03030`
  - `badgeC` 机械转导生理（血压/呼吸/膀胱） — 深青 `#0E7C7B`
  - `badgeD` 亚美尼亚与难民之路 — 灰紫 `#5C5470`
- **背景母题**：同心圆波纹（按压薄膜的形变）从版面一角扩散，badge 圆点嵌于波纹上。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 机械力感受通道的发现者 / Ardem Patapoutian 1967– + 四色 badge + 右上头像 + 国籍行 USA/Lebanon/Armenia
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生贝鲁特、教育 AUB/UCLA BS 1990/
    Caltech PhD 1996、导师 Wold、博后 Reichardt、任职 Scripps/HHMI、
    荣誉 Nobel 2021/Kavli 2020、核心领域）
03  核心贡献概览 — PIEZO1/2 的发现 / 触觉与本体感觉 / 生理调控 / 从贝鲁特到拉霍亚
04  贝鲁特战火童年 (1967–1986) — 黎巴嫩亚美尼亚家庭、祖辈经亚美尼亚种族灭绝幸存
    自 Hadjin 定居黎巴嫩、内战 8 岁爆发、高中年级仅 5 名学生、
    Demirdjian 与 Hovagimian 亚美尼亚学校
05  "最后一根稻草" — AUB 医预科一年、跨越东西贝鲁特时被武装分子挟持险遭枪击获释、
    1986 与兄 Ara 以难民身份赴美、送披萨/为亚美尼亚报纸写星座专栏攒 residency
06  UCLA 与 Caltech (1986–1996) — UCLA 细胞与发育生物学 BS 1990、
    Caltech 生物学 PhD 1996（Barbara Wold 门下，MyoD 家族基因与小鼠发育）
07  UCSF 博后与 Scripps 起步 (1996–2000) — Louis F. Reichardt 实验室博后、
    2000 Scripps 助理教授、2000-2014 Novartis Research Foundation 兼职、2014 起 HHMI 研究员
08  基因失活筛选：找出"触觉基因" — 逐个灭活基因、锁定使细胞对触碰不敏感的基因、
    命名 PIEZO1（希腊语"压力"）、经序列相似性发现 PIEZO2——2010 Science 论文
09  PIEZO2：更重要的触觉通道 — 机械感受通道的主力、2014 Nature 系列
    （Merkel 细胞机械转导、小鼠触觉主要转换器）
10  PIEZO 的生理疆域 — 调控血压、呼吸与膀胱控制；温度/痛觉/本体感觉/血管张力中的
    离子通道角色；近年功能基因组学推进 mechanotransduction
11  2020 Kavli → 2021 Nobel — 2020 Kavli 神经科学奖与 Julius 共享（诺奖前奏）、
    2021 两人共享 "for the discovery of receptors for temperature and touch"
12  亚美尼亚的荣光 (2022) — 首位亚美尼亚裔诺奖得主、2022-06 首访受英雄礼遇、
    Pashinyan 授 Order of St. Mesrop Mashtots、NAAS 荣誉会员、
    埃里温医科大学荣誉博士、诺奖奖章复制品赠亚美尼亚历史博物馆、HayPost 邮票
13  其他荣誉 — W. Alden Spencer 2017、Rosenstiel 2019、BBVA 前沿奖 2020、
    黎巴嫩功绩勋章（Aoun 授，2021-10）、Great Immigrants 2022、
    AAAS Fellow 2016/NAS 2017/AAA&S 2020、h-index 68
14  遗产与现在 — 触觉与机械力生物学的分子基石、慢性疼痛治疗的通道靶点、
    Scripps 教授与 HHMI 研究员的在途研究、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for the discovery of receptors for temperature and touch"（与 Julius 两人共享） |
| 生日双值 ★ | metadata date_of_birth 1967-10-02；infobox 与正文均为 **1 October 1967**——以 page.md 为准取 10-01，yaml 已按此填写，陷阱表记录 |
| 国籍三列 ★ | 总表/manifest 仅 United States；Nobel 官方 citation json "Lebanon United States"；page.md citizenship Armenia/Lebanon/US 三列；yaml 取 United States(0)+Lebanon(1)+Armenia(2)（"首位亚美尼亚裔诺奖得主"为 page.md 明载核心身份），供主控统一口径 |
| 难民叙事 | 1986 兄弟二人以难民身份赴美、送披萨/写星座专栏——page.md 明载励志线，客观呈现勿煽情 |
| 挟持事件 | 被武装分子挟持险遭膝部枪击、自称"压断骆驼的最后一根稻草"（page.md 引语）——可引原文+译文，客观 |
| 亚美尼亚种族灭绝 | 祖辈幸存背景一笔带过（page.md 措辞），不展开历史叙述 |
| PIEZO 命名 | PIEZO1 源自希腊语"压力"（transl. pressure）；PIEZO2 经序列相似性发现——命名链勿错 |
| 通道分工 | 触觉主力是 **PIEZO2**（page.md "the more important of the two"）；血压/呼吸/膀胱调控为两者共同生理功能——勿写反 |
| Kavli 前奏 | 2020 Kavli 神经科学奖与 Julius 共享——先于诺奖；本页无与 Julius 的合作论文记载，仅 co-honored 边 |
| 在世者关系 | relations=4 为诚实值；父母虽 page.md 明载但非学界人物，不入库（防噪声裁定记录于此） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| PIEZO1 / PIEZO2 | 压力激活离子通道 | 希腊语 piezo = 压力 |
| mechanotransduction | 机械力转导 | 触觉的分子基础 |
| proprioception | 本体感觉 | PIEZO 相关感觉之一 |
| nociception | 伤害感受 | 慢性疼痛研究的入口 |
| vascular tone | 血管张力 | PIEZO 生理功能之一 |
| h-index | h 指数 | 68（Google Scholar, 2020-05 口径） |
| HHMI investigator | 休斯医学研究所研究员 | 2014 起 |
| Order of St. Mesrop Mashtots | 圣梅斯罗布勋章 | 亚美尼亚 2022 授予 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**PAST**（manifest 预分配）
- **风格**：历史感 / 深沉 / 回望
- **匹配理由**：祖辈穿越种族灭绝定居贝鲁特、少年穿越内战、青年穿越大西洋——PAST 的历史纵深感匹配"三代人的流亡与抵达"叙事；触觉研究本身也是对"过去被按压的记忆"的分子解读。
- **本地路径**：`music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav` → 复制为 `presentations/21th_century/Ardem_Patapoutian/PAST.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；生日/国籍裁定与 PIEZO 命名链务必精确。**
