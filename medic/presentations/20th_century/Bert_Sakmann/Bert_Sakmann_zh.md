# 医学家立传提示词（Bert Sakmann）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1991 年**得主（与 Erwin Neher 共享）。
> 本文件是 Sakmann 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Bert Sakmann（1942-06-12 生，在世），德国细胞生理学家
- **气质关键词**：**膜片钳的另一半发明者、单通道功能的验证者、从哥廷根到佛罗里达的膜片钳布道者** —— 1991 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for their discoveries concerning the function of single ion channels in cells"（因其关于细胞单离子通道功能的发现）
- **设计母题**：**千欧之封（the gigaohm seal）**。膜片钳的精髓是微吸管与细胞膜之间十亿欧级的密封——以「吸管尖端与膜片之间一道发光的封环」作为视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Bert_Sakmann/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Bert_Sakmann/`；Makefile 复制后设 `MAIN=Bert_Sakmann_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | physiology | 生理学 | 1991 诺奖核心：单离子通道功能 | 核心页 |
| 1 | neurophysiology | 神经生理学 | 视网膜电生理博士、马普神经生物学研究所 | 研究页 |
| 2 | medicine | 医学 | 医学博士（哥廷根 1974） | 早年页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Erwin Neher | 无向 | 1991 诺贝尔生理学或医学奖共享（单离子通道功能；哥廷根共事） |
| advisor-student | Otto Detlev Creutzfeldt | 师→生（神经生理导师） | 1968 慕尼黑马普精神病学所神经生理系入门、1974 随其迁哥廷根 |
| advisor-student | Bernard Katz | 师→生（UCL 导师） | 1971 赴伦敦大学学院生物物理系在其门下（1970 诺奖得主） |

**方向约定**：`advisor-student` + `direction: advisor` = 对方是导师；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：医者转研究员的严谨、 seal 之刻的专注、马普系的厚重
- **主色**：`#5A6B35`（膜片橄榄绿，细胞膜与封接）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：`badgeSeal` 千欧封接 — 封接金 `#A8752F`；`badgeChannel` 离子通道 — 通道青 `#1B7A6B`；`badgeRetina` 视网膜电生理 — 视紫红 `#8C3A5E`；`badgeMPG` 马普所岁月 — 学院灰蓝 `#4E6478`
- **背景母题**：浅绿底上微吸管尖端口吸附的圆形膜片与通道开合小方波，错落成谱。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 千欧之封 / Bert Sakmann b.1942 + 四色 badge + 右上肖像 + 国籍行（Germany）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生、Stuttgart、蒂宾根-弗赖堡-慕尼黑/哥廷根、海德堡/马普、荣誉）
03  核心贡献概览 — 膜片钳 / 单通道功能验证 / 视网膜电生理 / 马普佛罗里达
04  斯图加特剧院之家 (1942–1967) — 父为剧场总监、母为理疗师、五城学医（蒂宾根/弗赖堡/柏林/巴黎/慕尼黑）
05  慕尼黑双重身份 (1968–1971) — LMU 医学助理 + 马普精神病学所神经生理系 Creutzfeldt 门下
06  伦敦 Katz 门下 (1971–1974) — UCL 生物物理系、1970 诺奖得主的传承、1974 哥廷根医学博士（猫视网膜神经明适应电生理）
07  重返 Creutzfeldt (1974–1979) — 随师迁哥廷根马普生物物理化学研究所、1979 加入膜生物学组
08  膜片钳的发明 (1970s)（核心贡献页）— 与 Neher 共创、gigaohm 封接、活细胞单通道电流首次记录
09  单通道功能的生理验证 — 乙酰胆碱受体单通道、通道开合动力学
10  荣誉前哨 — Spencer 奖 1983、Horwitz 奖 1986（与 Neher）、Leibniz 奖 1987、Louis-Jeantet 1988
11  1991 诺贝尔奖 — 与 Neher 共享、同年 Gerard 奖与 Harvey 奖
12  海德堡教授 (1990–2008) — 自然科学医学部教席、马普医学研究所荣休科学成员
13  马普佛罗里达 (2009–) — 科学总监、Jupiter 新前沿
14  遗产：Bert-Sakmann-Stiftung — 基金会、Leopoldina 院士 1993、ForMemRS 1994
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生年 | 1942-06-12 生于 Stuttgart（出生时政体为纳粹德国）——行文用「生于斯图加特」；在世，卒年留白 |
| 获奖理由 | "for their discoveries concerning the function of single ion channels in cells"——**their**（与 Neher 共享）；本页另有 patch clamp 发明表述 |
| 双导师 | Creutzfeldt（慕尼黑→哥廷根神经生理启蒙与复归）与 Bernard Katz（UCL 生物物理，1970 诺奖得主）——正文均明载 under，入库双 advisor-student |
| 与 Neher 汇合点 | 正文：1991 诺奖「with whom he had worked in Göttingen」——共事地在哥廷根，勿写慕尼黑 |
| 页面简短 | 本页无家庭/早年之外的展开——Slide 不得写入 page.md 无载细节 |
| 学位口径 | 医学博士论文在哥廷根大学医学院（1974，猫视网膜神经明适应电生理）——Dr. med. 口径 |
| 无引语 | 本页正文无直接引语——引号内不得出现「原话」 |
| 荣誉并行 | Horwitz 1986 与 Leibniz 1987 均与 Neher 同期——避免与 Neher 篇重复堆砌 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| patch clamp | 膜片钳 | 与 Neher 共同发明 |
| gigaohm seal | 千欧级封接 | 膜片钳技术核心 |
| single ion channel | 单离子通道 | 诺奖理由核心词 |
| cat retina | 猫视网膜 | 其博士论文对象 |
| light adaptation | 明适应 | 论文主题（Helladaptation） |
| Max Planck Institute of Neurobiology | 马普神经生物学研究所 | 2008 起荣休组 |
| Max Planck Florida Institute | 马普佛罗里达研究所 | 2009 起科学总监 |
| Bert-Sakmann-Stiftung | 萨克曼基金会 | 其创立 |
| Leopoldina | 德国国家科学院（利奥波第那） | 1993 院士 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**New Lands** — Alex-Productions（manifest 预分配）
- **风格**：新大陆 / 开拓 / 明亮行进
- **匹配理由**：从斯图加特到伦敦、哥廷根再到佛罗里达的新前沿——New Lands 的开拓行进感匹配其五城学医与跨越大西洋建马普佛罗里达的轨迹，也匹配膜片钳为神经科学开辟的「新大陆」（第二次使用该曲，首用 Ramsay/Rutherford，同为拓疆者）。
- **本地路径**：`music_audio/` 下 New Lands 曲目 → 复制为 `presentations/20th_century/Bert_Sakmann/New_Lands.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。

