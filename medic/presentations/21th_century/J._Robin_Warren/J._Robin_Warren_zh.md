# 医学家立传提示词（J. Robin Warren）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2005 年得主（与 Barry Marshall 共享）。
> 本文件是 J. Robin Warren 的人物专属立传提示词：事实基准唯一来源为本地 Wikipedia 页面，
> 执行方按本提示词产出 15 页 Beamer 立传（本阶段不写 tex，仅沉淀事实与规范）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：John Robin Warren（1937-06-11 生于阿德莱德 ~ 2024-07-23 逝于珀斯，享年 87 岁）
- **气质关键词**：**显微镜下的守望者、幽门螺杆菌的再发现者、耐心等待时代追上发现的人**
- **诺奖获奖理由（2005，逐字引用 medic/nobel_medicine_citations.json）**：
  > "for their discovery of the bacterium Helicobacter pylori and its role in gastritis and peptic ulcer disease"
  > （因其发现幽门螺杆菌及其在胃炎和消化性溃疡病中的作用）——注意 "their"：与 Barry Marshall 共享
- **设计母题**：**切片与视野（the slide and the eye）**。病理学家的工作是俯身显微镜读胃黏膜切片——
  视觉母题用显微镜视野圆形光斑中一道弯曲的菌影，象征"在公认无菌的器官里看见生命"。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/J._Robin_Warren/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 medic 路径执行：页面读 `medic/presentations/pages/21th_century/{Dir}/page.md`，
> 产出放 `medic/presentations/21th_century/J._Robin_Warren/`，数据库写 greatminds 库（MySQL）。

- **第 0 步**：核对本地 page.md 事实基准（本提示词第三、四、七节已沉淀，执行时再逐句复核）
- **第 1 步**：建目录 `medic/presentations/21th_century/J._Robin_Warren/`（含 `images/`）
- **第 2 步**：复制 Makefile，设 `MAIN=J_Robin_Warren_zh`、`VIDEO_NAME=J_Robin_Warren_zh`（宏名禁数字与点号）
- **第 3 步**：收集肖像（page.md 无 infobox 肖像 URL 时用 Commons Special:FilePath 回退，404 则装饰圆占位）
- **第 4~9 步**：tex 编写 → 编译循环（0 error、vbox≤10pt、hbox≤50pt）→ pdftoppm 逐页目检 → make images/video → Review

## 三、研究领域梳理 + 入库（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | pathology | 病理学 | 皇家珀斯医院资深病理学家，主业身份 | 身份页 |
| 1 | microbiology | 微生物学 | 1979 年再发现幽门螺杆菌 | 核心页 |
| 2 | gastroenterology | 胃肠病学 | 胃炎与溃疡的细菌病因 | 核心页 |
| 3 | medicine | 医学 | MBBS（阿德莱德大学）出身 | 身份页 |

## 四、社会关系梳理 + 入库（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Barry Marshall | 无向 | 2005 诺贝尔生理学或医学奖共享（发现幽门螺杆菌及其在胃炎和消化性溃疡中的作用） |
| spouse | Winifred Warren | 无向 | 妻子 Winifred Teresa Warren（娘家姓 Williams），1960 年代初结婚，1997 年去世后沃伦退休 |

> 说明：relations 仅 2 条为诚实值（page.md 明载关系就这两条），防 Review 误判。
> 小行星 254863 Robinwarren 命名、发现者 Silvano Casulli 均非社会关系，不入库。
> 自查 SQL：`SELECT COUNT(*) FROM person_relation WHERE from_id=<pid> OR to_id=<pid>;` 预期 = 2。

## 五、配色方案

- **气质**：沉静、严谨、大器晚成的耐心
- **主色**：灰绿 `#2F4F4F`（病理切片的显微镜视野与病理学家的克制）+ 香槟金 `#D4AF37`（诺奖色）
- **四分类色 badge**：
  - `badgeScope` 显微视野 — 冷青 `#0E7C7B`
  - `badgeHp` 幽门螺杆菌 — 螺旋银蓝 `#4C5FD5`
  - `badgeBiopsy` 活检与切片 — 暖赭 `#E07B30`
  - `badgeAward` 荣誉 — 皇家紫 `#52307C`
- **背景母题**：大圆光斑（显微镜视野）+ 细小弯钩曲线（菌体轮廓），疏密错落

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover 共享首页）
01  封面 — 显微镜下的守望者 / J. Robin Warren 1937–2024 + 四色 badge + 国籍行（Australia）
02  身份信息页（★ 必做）— 左头像 + 右信息网格：生卒/北阿德莱德出身/教育阿德莱德大学 MBBS/任职皇家珀斯医院/核心领域
03  核心贡献概览 — 再发现幽门螺杆菌 / 与 Marshall 的假说 / 尿素呼气试验 / 诺奖
04  早年与教育 (1937–1963) — 北阿德莱德、St Peter's College、阿德莱德大学 MBBS；父为酿酒师、母为护士
05  病理学之路 (1963–1967) — 皇家阿德莱德医院、IMVS 血液实验室、墨尔本皇家医院；1967 入选澳大利亚皇家病理学家学院
06  皇家珀斯医院 (1967– ) — 资深病理学家，职业生涯主阵地
07  1979：切片上的螺旋菌（核心贡献页）— 胃黏膜活检中再发现弯曲杆菌，挑战"胃内无菌"教条
08  与 Marshall 结盟 (1981–1982) — 1981 内科 fellow 训练中相遇；1982 首次培养成功（第 31 号样本）
09  尿素呼气试验 — Warren 参与开发的便捷诊断（14C-urea breath test）
10  从讥笑到承认 — H. pylori 学说被医学界接受的漫长过程（克制呈现，勿渲染成迫害叙事）
11  2005 诺贝尔奖 — Karolinska 授奖，理由逐字；诺奖演讲 "Helicobacter - The Ease and Difficulty of a New Discovery"
12  荣誉与认可 — Paul Ehrlich 1997 · Nobel 2005 · Companion of the Order of Australia 2007 · 小行星 254863 Robinwarren（2016 命名）
13  个人生活与谢幕 — 妻 Winifred（精神科医生）1997 去世后退休，五名子女；2024-07-23 逝于珀斯
14  遗产：胃炎即感染 — "胃里的细菌"改写消化病学教科书
15  结尾
```

## 七、特殊陷阱表（★ 执行时必须核对）

| # | 陷阱 | 说明 |
|---|------|------|
| 1 | 获奖理由 | 逐字 "for their discovery of the bacterium Helicobacter pylori and its role in gastritis and peptic ulcer disease"；"their" 表共享 |
| 2 | 全名 | John Robin Warren，常用名 Robin Warren；"J. Robin Warren" 为目录/库名形式，正文首现写全名 |
| 3 | "再发现" | page.md 用词是 **1979 re-discovery**——螺旋菌此前有人描述过，沃伦是"再发现"者，勿写"首次发现细菌" |
| 4 | 生卒 | 1937-06-11 阿德莱德 ~ 2024-07-23 珀斯，享年 87；卒日 2024 勿漏（2005 得主中最晚去世者之一） |
| 5 | 机构 | 职业生涯主体在**皇家珀斯医院**（Royal Perth Hospital）；教育在**阿德莱德大学**——勿把 UWA 写成其母校（那是 Marshall） |
| 6 | 尿素呼气试验 | page.md 载 "Warren helped develop"（14C-urea breath test），措辞是"参与开发"，勿写成独立发明 |
| 7 | 配偶 | Winifred Teresa Warren（娘家姓 Williams），1960 年代初结婚；她后来成为**精神科医生**（accomplished psychiatrist）；1997 年她去世后沃伦从医学界退休——退休年份与诺奖 2005 的关系勿倒置 |
| 8 | 子女 | 五名子女；Marshall 篇是四名——两人家庭信息勿互串 |
| 9 | 小行星 | 254863 Robinwarren 由意大利业余天文学家 Silvano Casulli 2005 年发现，2016-04-22 公布命名——"2005 发现"勿写成"2005 命名" |
| 10 | 纪录片 | 2006 年澳大利亚纪录片 "The Winner's Guide to the Nobel Prize" 讲述两人之路，可作尾声素材 |
| 11 | 引语红线 | page.md **无任何直接引语**——全篇不得出现"原话"式引号引语，只可忠实转述 |
| 12 | 诺奖演讲标题 | "Helicobacter - The Ease and Difficulty of a New Discovery"（Nobelprize.org 外链载明），可作第 11 页素材 |

## 八、术语清单

| 英文 | 中文 | 风险点 |
|------|------|--------|
| Helicobacter pylori | 幽门螺杆菌 | 沃伦 1979 年再发现时的旧分类为弯曲菌属 |
| re-discovery | 再发现 | 强调"在被遗忘的文献之后重新看见"，非首创 |
| biopsy | 活检 | 病理学证据来源（胃黏膜活检） |
| urea breath test | 尿素呼气试验 | 14C 标记的诊断方法 |
| Royal College of Pathologists of Australasia | 澳大利亚皇家病理学家学院 | 1967 年当选 |
| gastritis | 胃炎 | 沃伦读片中观察到的慢性活动性胃炎背景 |
| pathologist | 病理学家 | 其 fields 行身份，勿写成 physician 泛称 |
| MBBS | 内外全科医学士 | 阿德莱德大学，勿写成 PhD |

## 九、背景音乐选择

- **选定曲目**：**With Me** — Alex-Productions（manifest 预分配）
- **匹配理由**：With Me 的温和陪伴感对应两位搭档二十年相互支撑的叙事（病理学家提供眼睛、内科医生提供行动），
  也贴合沃伦晚年沉静谢幕（妻子去世后退休、87 岁辞世）的克制气质——不煽情，有暖意。
- **备选（未采用）**：Timeless（沉稳但更适合"纲领型"人物，沃伦是"守望型"）、Nostalgia（怀旧感可用但已被多篇占用，避开撞曲）
- **本地路径**：`music_audio/` 下 alex-productions 曲库按 curated_tracks.md 对应条目复制为
  `medic/presentations/21th_century/J._Robin_Warren/With_Me.wav`
