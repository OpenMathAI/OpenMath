# 医学家立传提示词（E. Donnall Thomas）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1990 年**得主（与 Joseph Murray 共享）。
> 本文件是 Thomas 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Edward Donnall "Don" Thomas（1920-03-15 ~ 2012-10-20，享年 92 岁），美国血液学家
- **气质关键词**：**骨髓移植之父、与妻子并肩的实验家、西雅图 Fred Hutch 的奠基者** —— 1990 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for their discoveries concerning organ and cell transplantation in the treatment of human disease"（因其关于器官与细胞移植治疗人类疾病的发现）
- **设计母题**：**第二次造血（a second marrow）**。致命辐照后输注骨髓细胞让生命重启——以「骨髓穿刺针下重新充盈的血细胞」作为视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/E._Donnall_Thomas/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/E._Donnall_Thomas/`；Makefile 复制后设 `MAIN=E_Donnall_Thomas_zh`（宏名禁句点，文件名保持 manifest 原名）；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | hematology | 血液学 | 1990 诺奖核心：骨髓细胞移植 | 核心页 |
| 1 | transplantation | 移植医学 | 器官与细胞移植治疗人类疾病 | 核心页 |
| 2 | oncology | 肿瘤学 | 白血病的骨髓移植疗法 | 研究页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Joseph Murray | 无向 | 1990 诺贝尔生理学或医学奖共享（器官与细胞移植；Murray 器官、Thomas 细胞） |
| advisor-student | Eloise Giblett | 生（Thomas→学生） | 知名学生（infobox 明载） |
| spouse | Dottie Thomas | 无向 | 妻兼研究搭档，共研骨髓移植；本名 Dorothy Martin |

**方向约定**：`advisor-student` + `direction: student` = 对方是学生；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：德州乡村医生的朴实、三十年移植长跑的韧性、西雅图的沉静
- **主色**：`#7E2D26`（髓血红，骨髓与重生）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：`badgeMarrow` 骨髓移植 — 髓血红 `#7E2D26`；`badgeGVH` 移植物抗宿主 — 免疫紫 `#4A3560`；`badgeFredHutch` Fred Hutch 岁月 — 常青绿 `#2E5E4E`；`badgeTexas` 德州早年 — 原野褐 `#8C6A3A`
- **背景母题**：浅色底上骨髓穿刺针剪影与重新充盈的血细胞圆点群，错落连缀。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 骨髓移植之父 / E. Donnall Thomas 1920–2012 + 四色 badge + 右上肖像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Mart 德州、德州大学/哈佛 MD、Bassett/西雅图、荣誉）
03  核心贡献概览 — 骨髓移植 / 移植物抗宿主病 / 白血病疗法 / Fred Hutch
04  随父行医的少年 (1920–1943) — Mart 德州、影子父亲的全科诊所、德州大学化学与化工 BA/MA
05  哈佛与战时 (1943–1955) — 1946 MD、Peter Bent Brigham 住院医、驻德军医、1955 Bassett 内科主任
06  啮齿类模型的困境 — 致死辐照后输髓存活，人体却死于感染与免疫反应——转向犬模型
07  夫妻实验室（核心贡献页）— Dottie 辞记者做技师贴补家用、终身搭档、骨髓移植成为白血病疗法
08  西雅图与 Fred Hutch (1963–1993) — 公共卫生研究院、临床研究部荣誉主任
09  移植物抗宿主病的攻坚 — GVHD 机制与对策
10  1990 诺贝尔奖 — 与 Murray 共享、同年国家科学奖章；Murray 器官移植/Thomas 细胞移植两翼
11  荣誉年表 — Gairdner 1990、Kober 1992、Kettering 1981、血液学会主席 1987-88
12  阴暗的一页 (1981–1993) — 85 人试验 84 死、财务利益冲突未告知、IRB 反对下继续——正文明载，客观呈现
13  人文主义者 — 2003 年 22 位诺奖得主联署《人文主义宣言》
14  遗产与身后 — 全球骨髓移植网络、2012-10-20 心衰卒于西雅图
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒日 | 1920-03-15 生于 Mart, Texas；2012-10-20 卒于西雅图（心衰），享年 92 |
| 获奖理由 | "for their discoveries concerning organ and cell transplantation in the treatment of human disease"——**their**（与 Murray 共享）；分工：Murray 器官移植、Thomas 细胞（骨髓）移植 |
| 对手方规范名 | 库内既有 'Joseph Murray'（Q192282，他批先建）——勿用 citation json 的 'Joseph E. Murray'，防分裂 |
| 夫妻搭档 | Dottie（Dorothy Martin）为本篇主题亮点：为支持家庭改做实验技师、此后终身研究搭档——spouse 一行 note 概括 |
| 1981-1993 争议试验 | 85 人中 84 死、研究者潜在财务利益冲突未告知受试者、IRB 成员反对仍继续——正文明载，必须客观呈现，勿美化也勿渲染 |
| 荣誉年表长 | 本页荣誉极多——幻灯片只取主链（Kettering 1981 / Gairdner 1990 / Nobel 1990 / 国家科学奖章 1990 / Kober 1992），勿堆砌 |
| 无引语 | 本页正文无直接引语——引号内不得出现「原话」 |
| 家庭 | 三子；2003 年 22 位诺奖得主联署《人文主义宣言》——可写一句 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| bone marrow transplantation | 骨髓移植 | 诺奖理由核心词（细胞移植） |
| graft-versus-host disease | 移植物抗宿主病（GVHD） | 移植最大并发症 |
| leukemia | 白血病 | 首要适应症 |
| organ transplantation | 器官移植 | Murray 一侧 |
| stem cell transplantation | 造血干细胞移植 | 现代称谓 |
| Fred Hutchinson Cancer Research Center | 弗雷德·哈金森癌症研究中心 | 西雅图主阵地 |
| radiation lethality | 致死辐照 | 犬模型前提 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless** — Alex-Productions（manifest 预分配）
- **风格**：沉稳 / 纪录片 / 长期纲领
- **匹配理由**：从 1950s 辐照小鼠到 1990 诺奖，骨髓移植是四十年如一日的长期纲领——Timeless 的沉稳纪录片感匹配「夫妻实验室三十年」与全球移植网络的时代遗产（第二次使用该曲，首用 Kenneth G. Wilson，同为纲领型学者）。
- **本地路径**：`music_audio/` 下 Timeless 曲目 → 复制为 `presentations/20th_century/E._Donnall_Thomas/Timeless.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。

