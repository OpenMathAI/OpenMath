# 医学家立传提示词（Erwin Neher）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1991 年**得主（与 Bert Sakmann 共享）。
> 本文件是 Neher 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Erwin Neher（1944-03-20 生，在世），德国生物物理学家
- **气质关键词**：**膜片钳的发明者之一、听见单离子通道的人、哥廷根膜生物物理部长** —— 1991 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for their discoveries concerning the function of single ion channels in cells"（因其关于细胞单离子通道功能的发现）
- **设计母题**：**玻璃微管下的单通道（one channel under the pipette）**。膜片钳把一平方米级的噪声压到一枚通道——以「微吸管尖端口吸附的细胞膜小片与单一电流方波」作为视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Erwin_Neher/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Erwin_Neher/`；Makefile 复制后设 `MAIN=Erwin_Neher_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biophysics | 生物物理学 | 1991 诺奖核心：单离子通道记录 | 核心页 |
| 1 | cell physiology | 细胞生理学 | 膜片钳方法学与其应用 | 核心页 |
| 2 | membrane biophysics | 膜生物物理 | 哥廷根马普所膜生物物理系主任 | 任职页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Bert Sakmann | 无向 | 1991 诺贝尔生理学或医学奖共享（单离子通道功能） |
| advisor-student | Charles F. Stevens | 师→生（博士后导师） | 耶鲁其实验室中膜片钳方法获强力鼓励与发展 |
| spouse | Eva-Maria Neher | 无向 | 1978 结婚，五子；马普所实验官认识的科学家 |

**方向约定**：`advisor-student` + `direction: advisor` = 对方是导师；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：物理学家进入生理学的精密、微吸管下的极静、哥廷根的学院气质
- **主色**：`#24557E`（微管蓝，玻璃电极与电流）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：`badgePatch` 膜片钳 — 微管蓝 `#24557E`；`badgeChannel` 离子通道 — 通道青 `#1B7A6B`；`badgeCurrent` 单通道电流 — 电脉冲橙 `#D07B2A`；`badgeMPG` 马普所岁月 — 学院灰蓝 `#4E6478`
- **背景母题**：深蓝底上微吸管尖端剖面与方波电流脉冲序列，错落成谱。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 听见单通道的人 / Erwin Neher b.1944 + 四色 badge + 右上肖像 + 国籍行（Germany）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生、Landsberg、慕尼黑工大/威斯康星、哥廷根马普所、荣誉）
03  核心贡献概览 — 膜片钳 / 单离子通道电流 / 分泌与钙信号 / 计算神经科学共治
04  巴伐利亚物理少年 (1944–1966) — 慕尼黑工大物理 1963-66、1966 富布赖特奖学金赴美
05  威斯康星与哥廷根 (1966–1970s) — 生物物理硕士、马普生物物理化学研究所、遇见 Eva-Maria
06  耶鲁 Stevens 实验室 — 方法论在其实验室获强力鼓励发展（infobox 列其为学术导师）
07  膜片钳的发明 (1970s)（核心贡献页）— 与 Sakmann 共创、首次记录活细胞单离子通道电流
08  单通道的世界 — 脂双层法对比、通道开合的方波、噪声中的量子事件
09  从方法到生理学 — 分泌、钙信号与通道功能的生理图景
10  荣誉前哨 — Horwitz 奖 1986（与 Sakmann）、Leibniz 奖 1987（德国最高研究荣誉）
11  1991 诺贝尔奖 — 与 Sakmann 共享、Gerard 奖同年
12  哥廷根膜生物物理部 (1983–2011) — 所长、哥廷根大学荣休教授、Bernstein 计算神经中心联席
13  国际学界 — 皇家学会外籍会士 1994、十余所荣誉博士（含华中科技大学 1994、牛津 2025）
14  遗产：膜片钳走进每个电生理实验室 — 2003 年 22 位诺奖得主联署《人文主义宣言》
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生年双值 | frontmatter nationality 有 "Nazi Germany"（出生时政体）——行文用「生于巴伐利亚 Landsberg am Lech」；1944-03-20 生，在世，卒年留白 |
| 获奖理由 | "for their discoveries concerning the function of single ion channels in cells"——**their**（与 Sakmann 共享）；引号内为诺奖原句，可整句引用 |
| Stevens 双重身份 | infobox 列其为 academic advisor，正文记耶鲁实验室「强力鼓励」方法论发展——入库 advisor-student direction=advisor，note 兼顾 |
| 妻子本名 | Eva-Maria Neher（本姓 Ruhr），马普所实验官认识、1978 结婚、五子（含 Richard A. Neher）——spouse 一行；不建 parent-child 边 |
| 荣誉极多 | 本页奖项 20+、荣誉博士 10+——幻灯片只取主链（Horwitz 1986 / Leibniz 1987 / Nobel 1991 / ForMemRS 1994 / 牛津荣誉博士 2025） |
| 首次记录口径 | 正文：首次记录**活细胞**单离子通道电流（此前用脂双层法）——表述保留这一限定 |
| 无争议条目 | 本页无诉讼/争议——叙事保持明快 |
| 引语 | 本页仅诺奖自述一段长引语（lambda 转导语境不含）——正文无个人语录，引号内不得自造 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| patch clamp | 膜片钳 | 与 Sakmann 共同发明 |
| single ion channel | 单离子通道 | 诺奖理由核心词 |
| lipid bilayer method | 脂双层法 | 先行记录技术 |
| pipette | 微吸管（玻璃电极） | 膜片钳工具 |
| cell physiology | 细胞生理学 | 其专业领域 |
| Max Planck Institute for Biophysical Chemistry | 马普生物物理化学研究所 | 1983 起所长 |
| membrane biophysics | 膜生物物理 | 其执掌的系 |
| Bernstein Center | Bernstein 计算神经科学中心 | 哥廷根联席主席 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**PAST** — Alex-Productions（manifest 预分配）
- **风格**：历史感 / 深沉 / 回溯
- **匹配理由**：膜片钳把电生理学带回「单分子事件」的原点——PAST 的历史感匹配从 1970s 手工微吸管到今日全实验室标配的方法学溯源，也匹配哥廷根学派的厚重传承（第二次使用该曲，首用 Anderson/Mott，同为回望型学者）。
- **本地路径**：`music_audio/` 下 PAST 曲目 → 复制为 `presentations/20th_century/Erwin_Neher/PAST.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。

