# 医学家立传提示词（Emil Theodor Kocher）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Emil Theodor Kocher（1909 年诺贝尔生理学或医学奖得主，瑞士）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Emil_Theodor_Kocher/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Emil Theodor Kocher（埃米尔·特奥多尔·科赫尔，1841-08-25 伯尔尼 ~ 1917-07-27 伯尔尼，享年 75 岁）
- **气质关键词**：**甲状腺外科的奠基人、无菌外科的推行者、外科科学化的旗手** —— 1909 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json）：
  > "for his work on the physiology, pathology and surgery of the thyroid gland"
  > （因其关于甲状腺的生理学、病理学与外科学的工作）
- **设计母题**：**「切与留的平衡」**。甲状腺是双刃器官：全切致恶病质、残留致复发——Kocher 以慢、稳、准的手术风格把死亡率从 18% 压到 0.5% 以下，又因「切得太干净」反而率先揭示了甲状腺激素的必需性。视觉隐喻可用「精确的手术器械轮廓 + 甲状腺蝶形轮廓」的对称构图。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Emil_Theodor_Kocher/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`（OpenMedic 统一 `\input`）

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Emil_Theodor_Kocher/`（page.md + metadata.json + images.txt），成目录 `medic/presentations/20th_century/Emil_Theodor_Kocher/`，Makefile 复制后设 `MAIN=Emil_Theodor_Kocher_zh`、`VIDEO_NAME=Emil_Theodor_Kocher_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节；后续步骤（配色→幻灯片→tex→编译循环→逐页目检→Review）照常执行。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | thyroid surgery | 甲状腺外科 | 5000 余例甲状腺切除，死亡率 <0.5%，1909 诺奖核心 | 甲状腺外科页 |
| 1 | aseptic surgery | 抗菌无菌外科 | 推行李斯特抗菌法，逐例追查伤口感染来源 | 无菌外科页 |
| 2 | neurosurgery | 神经外科 | 颅内压、脑震荡、癫痫手术探索；教科书 141 页论神经系统 | 神经外科页 |
| 3 | endocrinology | 内分泌学 | cachexia strumipriva→甲状腺激素替代疗法的先声 | 甲状腺功能页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Emil_Theodor_Kocher.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Marie Witschi-Courant | 无向 | 1869 年成婚，育三子 |
| parent-child | Jakob Alexander Kocher | 父 | 伯尔尼州道路与水务总工程师 |
| parent-child | Maria Kocher | 母 | 摩拉维亚教会虔信教徒 |
| parent-child | Albert Kocher | 子 | 长子，随父任伯尔尼外科诊所助理教授 |
| advisor-student | Anton Biermer | 师 | 博士导师，1865 年伯尔尼以最优等获医学博士 |
| advisor-student | Georg Lücke | 师 | 1867 年返伯尔尼后任其外科助手 |
| influence | Theodor Billroth | — | 1865 年苏黎世随 Biermer 访其主持的医院，深受影响 |
| influence | Bernhard von Langenbeck | — | 1865 年柏林游学期间师从 |
| colleague | Joseph Lister | — | 有书信往来，1868 年起在伯尔尼推行其抗菌缝合法 |
| controversy | Jacques-Louis Reverdin | — | 1882-1883 甲状腺全切除后果发现优先权之争 |
| advisor-student | Harvey Cushing | 生 | 1900 年数月在其实验室从事脑外科研究 |
| advisor-student | Hayazo Ito | 生 | 1896 年来伯尔尼研究癫痫的日本外科医生 |
| advisor-student | Fritz de Quervain | 生 | 门生，后成名于甲状腺外科 |
| advisor-student | César Roux | 生 | 门生，后执教洛桑 |
| advisor-student | Carl Garré | 生 | 门生，后执教波恩 |
| advisor-student | Otto Lanz | 生 | 门生，后执业于阿姆斯特丹 |

> 说明：page.md 学生名单共约 30 人，本表只收有独立条目或叙事明确者（Cushing/Ito/de Quervain/Roux/Garré/Lanz）；其余名单成员与「伯尔尼1874 年报告cretinism 的开业医生 August Fetscherin」等按 metadata/名单噪声处理不入库。与 Virchow 仅「申请职位未果」、与 Pasteur 仅「巴黎拜访」，均不构成明载关系，不入库。

## 五、配色方案 【人物专属】

- **气质**：精准、克制、瑞士式的洁净与虔诚
- **主色**：手术青蓝 `#1B4D5C`（外科器械的冷峻与伯尔尼的沉静）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 甲状腺外科 — 甲状腺朱 `#C0504D`
  - `badgeB` 无菌外科 — 消毒青 `#2E8B8B`
  - `badgeC` 神经外科 — 颅腔紫 `#6B4E8E`
  - `badgeD` 内分泌学 — 激素琥珀 `#D08A2E`
- **背景母题**：稀疏手术器械轮廓线（钳、牵开器）与蝶形甲状腺剪影，低透明度铺底，呼应「精确切除」母题

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 甲状腺外科奠基人 / Emil Theodor Kocher 1841–1917 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒伯尔尼、教育、1872 任教、任职 Inselspital、荣誉、核心领域）
03  核心贡献概览 — 甲状腺外科 / 无菌外科 / 神经外科 / 内分泌学
04  早年：伯尔尼之子 (1841–1865) — 铁路工程师之家、Realschule 第一名、1858 入伯尔尼大学
05  游学欧洲 (1865–1867) — Zürich Billroth、柏林 Langenbeck、伦敦 Hutchinson/Thompson、巴黎 Pasteur
06  伯尔尼讲席 (1872–1917) — 30 岁接任 Lücke、45 年教授、重建 Inselspital、1880 布拉格邀约留人
07  无菌外科：把感染挡在门外（核心页）— Lister 抗菌法、1868 医院报告、逐例追查感染
08  甲状腺外科：从 75% 到 0.5%（核心页）— 慢稳准风格、止血、局麻、5000 余例
09  cachexia strumipriva：意外发现 — 1874 Fetscherin 报告、1882 Reverdin 会面、1883-04-04 柏林演讲
10  神经外科与颅内压 — Cushing 反射、去骨瓣减压、癫痫手术探索、Hayazo Ito
11  门生与传承 — Cushing、de Quervain、Roux、Ito；万余人听课、130+ 博士生
12  荣誉与认可 — Nobel 1909 · Hon FRCS 1900 · 德国外科学会主席 1902 · 布鲁塞尔 1905
13  以 Kocher 命名 — Kocher 钳/Kocher 手法/Kocher 切口/综合征、月球环形山、小行星 2087
14  遗产：外科科学化的百年基石 — Kocher 研究所、《手术学教科书》六版、1913 瑞士外科学会首任主席
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for his work on the physiology, pathology and surgery of the thyroid gland"；勿写成「甲状腺生理学研究的诺奖」之类概括 |
| 2 | 死亡率数字 | page.md 两处口径：从 18%（其本人基线，1872 年他处估计可高达 75%）降到 1912 年 <0.5%；正文另句泛称 below 1%。写「18%→<0.5%（1912）」，勿混用 75% 与 18% |
| 3 | 博士年份双值 | 1865 或 1866（注 1 以 1865 为多数来源）；正文取 1865，陷阱表注明 |
| 4 | 妻子生卒双值 | Marie Witschi-Courant 有 1841–1921 与 1850–1925 两说（注 3/4），立传中只写 1869 年成婚，不写其生卒 |
| 5 | Reverdin 优先权 | Reverdin 1882-09-13 先公开、Kocher 1883-04-04 才演讲，且「Kocher 从未承认 Reverdin 的优先权」——如实写，勿替 Kocher 辩护或写成共同发现 |
| 6 | Halsted 引语 | 比较 Kocher/Billroth 手术风格的大段引语 page.md 有英文原文，可引原文+译文；除此之外正文无其他直接引语，禁编造 |
| 7 | Krupskaya 手术 | 1913 年为列宁之妻 Nadezhda Krupskaya 在伯尔尼手术，page.md 明载；一句带过即可，勿展开政治背景 |
| 8 | 宗教背景 | 摩拉维亚教会虔信教徒、把成败归于上帝、认为唯物主义是恶——page.md 明载可写，但只作人物侧写，不作价值评判 |
| 9 | 「首位」表述 | 「首位获医学诺奖的瑞士公民」「首位获医学诺奖的外科医生」是 page.md 原句，可写；勿引申为「瑞士首位诺奖得主」（那是 1901 Gobat/Dunant 等的和平奖） |
| 10 | metadata 冲突 | metadata.json 与 page.md 冲突时以 page.md 为准（本篇两者基本一致，无特殊冲突） |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| thyroidectomy | 甲状腺切除术 | 勿与「甲状腺切开」混淆 |
| goitre | 甲状腺肿 | 地方病背景（瑞士缺碘） |
| cachexia strumipriva | 甲状腺切除性恶病质 | Kocher 命名，今属术后甲减 |
| cretinism | 克汀病 | 先天甲减，勿写成「痴呆」 |
| aseptic / antiseptic | 无菌的 / 抗菌的 | Lister 系抗菌法，Kocher 推向无菌原则，两词勿混 |
| Kocher manoeuvre | Kocher 手法 | 十二指肠显露手法，勿与切口混淆 |
| Kocher's forceps | Kocher 钳 | 有齿止血钳，1882 年发明 |
| intracranial pressure (ICP) | 颅内压 | Cushing 反射语境 |
| decompressive craniectomy | 去骨瓣减压术 | 降颅内压手段 |
| Inselspital | 因塞尔医院（伯尔尼岛医院） | 伯尔尼大学外科临床所在地 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Tragedy** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「悲剧/沉重」匹配其手术台上的生死重量——甲状腺切除曾是被法兰西医学院禁止的高危手术，Kocher 一生都在与 75% 的死亡率对赌
  - 也匹配 1917 年的落幕：为急诊病人执刀后倒下，四日后辞世——外科医生的句号仍是手术刀
  - 沉稳的叙事节奏契合「慢、稳、准」的 Kocher 风格母题
- **备选**（未采用）：The Flow of Time（时间感强但缺张力）、PAST（历史感合适但已被物理侧多篇占用）
- **本地路径**：按 music_audio/ 内 Alex-Productions Tragedy 曲目复制至 `medic/presentations/20th_century/Emil_Theodor_Kocher/Tragedy.wav`，ffmpeg `-shortest` 对齐
