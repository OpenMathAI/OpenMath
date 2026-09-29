# 医学家立传提示词（Michael Rosbash）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2017 年得主（三人共享之一） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Michael Morris Rosbash（1944-03-07 生于堪萨斯城，在世）
- **气质关键词**：**period 基因的克隆者、昼夜节律 TTFL 模型的提出者、时间生物学的分子解牛者** —— 2017 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，三人共享同一句）：
  > "for their discoveries of molecular mechanisms controlling the circadian rhythm"
  > （因他们发现了控制昼夜节律的分子机制）
- **设计母题**：**分子齿轮与振荡曲线（TTFL feedback loop）**。PER 蛋白浓度约 24 小时的振荡曲线、转录-翻译负反馈环的环形箭头——"生命自带一只 24 小时的表"。
- **本地 Wikipedia 路径**：medic/presentations/pages/21th_century/Michael_Rosbash/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/21th_century/Michael_Rosbash/page.md`；目录 `medic/presentations/21th_century/Michael_Rosbash/`；Makefile 改 `MAIN=Michael_Rosbash_zh`；肖像优先 images.txt 所列 Commons 图（2017 诺奖发布会照、2024 诺奖周对话照），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Michael_Rosbash.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | chronobiology | 时间生物学 | 昼夜节律分子机制，诺奖核心 | 核心页 |
| 1 | genetics | 遗传学 | 正向遗传学克隆钟基因 | 发现页 |
| 2 | molecular biology | 分子生物学 | mRNA 加工研究出身 | mRNA 页 |
| 3 | neuroscience | 神经科学 | LNV 起搏神经元、脑节律 | 神经元页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Sheldon Penman | 师→本人 | MIT 博士导师（1970，生物物理） |
| influence | Norman Davidson | 无向 | Caltech 本科暑期进其实验室，转向生物研究 |
| colleague | Jeffrey C. Hall | 无向 | Brandeis 合作者，1984 共克隆 period 基因 |
| collaborator | Paul Hardin | 无向 | 博士后；1990 三人提出 TTFL 模型 |
| spouse | Nadja Abovich | 无向 | 同为科学家，育有继女 Paula 与女儿 Tanya |
| co-honored | Jeffrey C. Hall | 无向 | 2017 诺贝尔生理学或医学奖三人共享（昼夜节律分子机制） |
| co-honored | Michael W. Young | 无向 | 2017 诺贝尔生理学或医学奖三人共享（昼夜节律分子机制） |

> 对手方规范名：均无库内记录按 page.md 形式新建 stub；`Jeffrey C. Hall` 与 Young 篇同形式（Hall 本人批次写镜像边）；`Sheldon Penman` 以 infobox 为准（metadata 的 doctoral_advisor 是 QID 噪声 Q41531807，弃用）。

## 五、配色方案

- **气质**：果蝇瓶旁的四十年 + 精密振荡曲线 + 红袜队球迷的松弛
- **主色**：生物钟蓝 `#1E4E79`（深夜与黎明的过渡色）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` period/TTFL — 节律青 `#2E7D8C`
  - `badgeB` 钟基因家族（clock/cycle/cry）— 基因紫 `#5E4B8B`
  - `badgeC` mRNA 加工 — 转录橙 `#C97B2D`
  - `badgeD` 脑节律与神经元 — 突触绿 `#3E6B4F`
- **背景母题**：低透明度 24 小时振荡正弦曲线 + 环形反馈箭头。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 昼夜节律分子机制的破译者 / Michael Rosbash 1944– + 三人共享 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生年堪萨斯城、Caltech 1965、MIT 博士 1970、Brandeis 1974 起、HHMI 研究员、诺奖 2017）
03  核心贡献概览 — period 克隆 / TTFL 模型 / clock·cycle·cryptochrome / LNV 起搏器
04  难民之子与红袜队 (1944–1965) — 犹太难民家庭 1938 离德、父为领唱、两岁迁波士顿、本想学数学、Caltech 生物课与 Norman Davidson 实验室暑期转向生物
05  巴黎与 MIT 博士 (1965–1971) — Fulbright 奖学金巴黎一年、MIT 生物物理博士（Penman 门下，HeLa 细胞膜结合蛋白合成）、爱丁堡三年遗传学博士后
06  Brandeis 与 Hall 联手 (1974–1984) — 1974 入 Brandeis、与同事 Jeffrey Hall 合研果蝇活动-休息节律
07  1984：克隆 period 基因 — 首个果蝇钟基因克隆；Hardin 发现 per mRNA/PER 蛋白周期性波动
08  1990：TTFL 模型（核心页）— 转录-翻译负反馈环：PER 蛋白反馈抑制 per mRNA；perS/perL1 突变体相位移动、per0 挽救实验；1992 转录调控确证
09  1998 三连击与 1999 起搏器 — dClock（Jrk 突变）、cycle（bmal1 同源）、cryptochrome（cryb 突变=果蝇昼夜感光）；1999 LNV 神经元为主起搏器、PDF 为主要递质
10  TTFL 的挑战（诚实一页）— Akhilesh Reddy 组：不表达钟基因的 S2 细胞亦有节律，TTFL 不足以解释全部——模型仍在演进（page.md 明载）
11  现在的研究 — 七个神经元群、黎明细胞促觉醒/黄昏细胞促睡眠、mRNA 加工与阿尔茨海默关联
12  2017 诺贝尔奖 — 与 Hall、Young 共享；官方理由全句；2009 Gruber/2011 Horwitz/2012 Massry+Gairdner/2013 Wiley 五奖预演
13  建制与家庭 — HHMI 研究员 1989 起、Brandeis 行为基因组学中心主任、首任 Peter Gruber 讲席、Hypnion 联合创始人；妻 Nadja Abovich（科学家）、NAS 2003
14  遗产：从果蝇到人类睡眠医学 — 昼夜节律成为现代生理学的支柱之一
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 2017 三人共享同一句理由（Hall/Rosbash/Young）；三人分工：Hall+Rosbash=period/TTFL，Young=timeless/doubletime——勿混写 |
| 博士导师 | 以 infobox **Sheldon Penman** 为准（MIT 生物物理 1970）；metadata 的 doctoral_advisor 为 QID 噪声 Q41531807 已弃用；Paris 一年系 Fulbright 博士前，勿写"巴黎读博" |
| Norman Davidson | 仅本科暑期实验室经历"转向生物研究"——influence，勿写导师 |
| Hardin 角色 | per mRNA 波动系博士后 Paul Hardin 发现，1990 TTFL 是 Rosbash/Hall/Hardin 三人提出——归属勿全归 Rosbash |
| TTFL 争议 | Reddy 组挑战实验须诚实呈现（TTFL 不能解释 S2 细胞节律）——勿把 TTFL 写成盖棺定论 |
| Konopka/Benzer | per 突变体最初发现者是 Konopka/Benzer（Rosbash 页仅提及 Young 受其影响）；Rosbash 篇可提"站在前人肩膀上"，勿写成 Rosbash 发现突变体 |
| 在世留白 | 在世者：无卒日；relations=7 诚实值（两子/继女仅家庭页提及，不建边） |
| 生平政治 | 父母 1938 逃离纳粹德国仅一句背景，不展开 |
| 引语红线 | page.md 无整句直接引语（"amusing reflection"仅为书名转述）——全部转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| circadian rhythm | 昼夜节律 | 约 24 小时，非"日周期"泛称 |
| period gene (per) | period 基因 | 1984 克隆，果蝇首个钟基因 |
| TTFL | 转录-翻译负反馈环 | 昼夜钟核心模型（有边界） |
| Drosophila melanogaster | 黑腹果蝇 | 模式生物 |
| cryptochrome | 隐花色素 | 1998 确证为果蝇昼夜感光体 |
| dClock / cycle | 果蝇 Clock/cycle 基因 | 哺乳动物 Clock/bmal1 同源 |
| LNV neurons | 腹侧外侧神经元 | 果蝇主起搏器 |
| forward genetics | 正向遗传学 | 表型→基因 |
| Zeitgeber Time | 授时时间 | 光暗循环相位参照 |

## 九、背景音乐选择

- **选定曲目**：**The Invisible Light** — Alex-Productions（manifest 预分配）
- **匹配理由**："不可见之光"贴合"看不见却无处不在的生物钟"——节律不占空间却统治生理；沉稳推进的曲式匹配 40 年耐心解构分子齿轮的叙事。
- **本地路径**：music_audio/ 下 Alex-Productions The Invisible Light 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
