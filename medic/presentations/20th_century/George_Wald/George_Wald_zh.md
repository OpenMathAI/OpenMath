# 医学家立传提示词（George Wald）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1967 年得主（与 Granit、Hartline 三人共享）。
> 本文件是 George Wald 的人物专属立传提示词：事实基准唯一来源为本地 Wikipedia 页面。

---

## 一、背景信息 【人物专属】

- **目标医学家**：George Wald（1906-11-18 生于纽约 ~ 1997-04-12 逝于剑桥麻省，享年 90）
- **气质关键词**：**视色素化学的破译者、视黄醛循环的发现人、从视网膜里称出维生素 A 的人**
- **诺奖获奖理由（1967，逐字引用 medic/nobel_medicine_citations.json）**：
  > "for their discoveries concerning the primary physiological and chemical visual processes in the eye"
  > （因其关于眼内初级生理与化学视觉过程的发现）——"their"：与 Granit、Hartline 三人共享；Wald 承担"化学"一半
- **设计母题**：**视黄醛循环（visual cycle）**。光把视紫红质漂白为视蛋白+含维生素 A 的化合物，
  暗处再循环复原——视觉母题用一枚分子在"光/暗"两个色域间的环形轨道，象征"看见与复原的化学循环"。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/George_Wald/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 medic 路径执行：页面读 `medic/presentations/pages/20th_century/{Dir}/page.md`，
> 产出放 `medic/presentations/20th_century/George_Wald/`，数据库写 greatminds 库（MySQL）。
> 第 0 步核对事实基准 → 第 1 步建目录含 images/ → 第 2 步复制 Makefile 设
> `MAIN=George_Wald_zh`、`VIDEO_NAME=George_Wald_zh` → 第 3 步收肖像（page.md 正文载 Commons 照 Ruth_Hubbard_and_George_Wald_1967.jpg 夫妻合影、Cone-absorbance-en.svg 吸收曲线图，优先抓取）→
> 第 4~9 步 tex 编写 → 编译循环（0 error、vbox≤10pt、hbox≤50pt）→ pdftoppm 逐页目检 → make images/video → Review。

## 三、研究领域梳理 + 入库（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neurobiology | 神经生物学 | 视色素与视觉循环（infobox Fields） | 核心页 |
| 1 | biochemistry | 生物化学 | 维生素 A/视黄醛的化学证据 | 核心页 |
| 2 | physiology | 生理学 | 光感受器波长响应 | 核心页 |
| 3 | zoology | 动物学 | 哥伦比亚大学 1932 博士学位科目 | 教育页 |

## 四、社会关系梳理 + 入库（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Ragnar Granit | 无向 | 1967 诺贝尔生理学或医学奖三人共享（眼内初级生理与化学视觉过程） |
| co-honored | Haldan Keffer Hartline | 无向 | 1967 诺贝尔生理学或医学奖三人共享（眼内初级生理与化学视觉过程） |
| colleague | Otto Heinrich Warburg | 无向 | 1932-33 在其实验室博士后访问研究，期间发现视网膜中的维生素 A；库内 id=4628（既有行沿用）
| colleague | Paul Karrer | 无向 | 赴苏黎世与维生素 A 发现者合作；库内 id=3317 |
| colleague | Otto Fritz Meyerhof | 无向 | 海德堡短期合作，1933 年因纳粹上台离欧赴美；库内 id=4621 |
| spouse | Frances Kingsley | 无向 | 1931 年结婚，后离异；育二子 Michael/David |
| spouse | Ruth Hubbard | 无向 | 生物化学家，1958 年结婚；育子 Elijah（音乐学家）女 Deborah |

> 说明：relations=7 全部 page.md 明载。政治/社会活动段落（见陷阱 12）不入库不展开。
> 自查 SQL：`SELECT COUNT(*) FROM person_relation WHERE from_id=<pid> OR to_id=<pid>;` 预期 = 7。

## 五、配色方案

- **气质**：化学家的精准 + 犹太移民之子的坚韧 + 公共知识人的热忱
- **主色**：深紫红 `#5B2A86`（视紫红质漂白反应的品红-紫过渡）+ 香槟金 `#D4AF37`（诺奖色）
- **四分类色 badge**：`badgeRhodopsin` 视紫红质 — 猩红 `#C4204F`；`badgeVitA` 维生素 A — 暖橙 `#E07B30`；`badgeSpectro` 分光光度 — 电光蓝 `#4C5FD5`；`badgeAward` 荣誉 — 皇家紫 `#52307C`
- **背景母题**：视紫红质吸收曲线（黑）+ 红/绿/蓝三条锥细胞曲线（page.md 正文即有此插图），渐变过渡

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页
01  封面 — 看见的化学 / George Wald 1906–1997 + 四色 badge + 国籍行（United States）
02  身份信息页 — 生卒/纽约出身/Brooklyn Tech 首届 1923 + NYU BS 1927 + Columbia 动物学 PhD 1932/Harvard 1934–/核心领域
03  核心贡献概览 — 视网膜维生素 A / 视紫红质漂白 / 锥细胞三色素 / 诺奖
04  移民之家 (1906–1932) — 父 Ernestine (Rosenmann) 与 Isaac Wald 为犹太移民；Brooklyn Technical High School 首届毕业生（1923）；NYU 1927 BS；Columbia 动物学 PhD 1932
05  德国游学 (1932–1933) — NRC 旅行资助：柏林 Warburg 实验室鉴定视网膜中的维生素 A；苏黎世 Karrer（维生素 A 发现者）；海德堡 Meyerhof 短期合作
06  离欧赴美 (1933–1934) — 希特勒上台、欧洲对犹太人趋危——1933 芝加哥大学、1934 哈佛（instructor→professor）
07  视紫红质与维生素 A（核心贡献页）— 视紫红质见光分解为视蛋白+含维生素 A 的化合物→维生素 A 为视网膜功能必需——"Wald's visual cycle"（Known for 词）
08  分光光度法测定 (1950s) — 化学萃取视网膜色素 + 分光光度计测吸收峰——吸收峰=最佳响应波长；视杆主测视紫红质；微分光光度术（microspectrophotometry）直接测单细胞——锥细胞三色素确定（红/绿/蓝吸收曲线）
09  1967 诺贝尔奖 — 理由逐字；三人分工一句（Granit 电生理/Hartline 神经脉冲/Wald 化学）
10  荣誉前奏 — Eli Lilly 1939 · Lasker 1953 · AAAS 1948 · NAS 1950 · 美国哲学学会 1958 · Rumford Prize 1959 · Guggenheim 1963 · Frederic Ives Medal 1966（OSA）· Paul Karrer 金奖 1967（苏黎世大学）· Massey Lecture 1970 · 1992 OSA 荣誉会员
11  1967 诺贝尔奖（若与第 9 页合并可调整）— 诺奖演讲与致谢一句
12  公共事务（中性一笔）— 作为诺奖得主积极参与公共讨论、传播科学理性（page.md 政治段落按裁定禁写，仅此中性句）
13  家庭 — 两段婚姻：Frances Kingsley（1931，后离异，二子 Michael/David）；Ruth Hubbard（1958，生物化学家，子 Elijah 音乐学家、女 Deborah 律师）；1997-04-12 逝于 Cambridge, Massachusetts
14  遗产 — 视黄醛循环成为视觉化学的通用框架；锥细胞三色素的化学测定巩固色觉理论；微分光光度术开单细胞光谱研究之先
15  结尾
```

## 七、特殊陷阱表（★ 执行时必须核对）

| # | 陷阱 | 说明 |
|---|------|------|
| 1 | 获奖理由 | 逐字 "for their discoveries concerning the primary physiological and chemical visual processes in the eye"；三人共享；Wald 对应"chemical"一半 |
| 2 | 三站欧洲游学 | Warburg（柏林，维生素 A 鉴定）→Karrer（苏黎世）→Meyerhof（海德堡）——顺序照实；Warburg/Karrer/Meyerhof 均诺奖得主 |
| 3 | 离欧年份 | 1933 年因希特勒上台离开欧洲（芝加哥大学）、1934 入哈佛——因果与年份照实，反犹背景一句即可、不展开 |
| 4 | 学位口径 | Columbia **动物学 PhD 1932**；NYU 学士 1927；Brooklyn Tech 为首届毕业生（1923）——三层教育线勿混 |
| 5 | 漂白化学 | 视紫红质→视蛋白+含维生素 A 的化合物；"视黄醛"（retinal）一词 page.md 仅见 See also 链接——正文以"含维生素 A 的化合物"表述为限，勿展开现代细节 |
| 6 | 测量对象 | 视杆占视网膜多数→早期测的是视紫红质；锥细胞三色素靠微分光光度术直接测单细胞——方法论递进讲清 |
| 7 | ★政治段落禁写 | page.md 载：越战反对与 1969 MIT 演说、1980 Ramsey Clark 伊朗之行、1986 莫斯科见戈尔巴乔夫谈萨哈罗夫、割礼立场、无神论——**全部禁写**（项目政治敏感先例），至多第 12 页中性一句"积极参与公共讨论"；1970 "文明将在 15/30 年内终结"预言亦不引 |
| 8 | 引语红线 | 无安全可引的原话（唯一近引语系政治演说）——全篇不得出现"原话"式引语 |
| 9 | 妻子 | Ruth Hubbard 系生物化学家、与其 1958 结婚——夫妻合影（1967）可作插图；两段婚姻按时间线讲清 |
| 10 | 与 Granit/Hartline | 三人仅同届共享，page.md 无合作记载——只建 co-honored |
| 11 | 国籍 | United States 单籍 |

## 八、术语清单

| 英文 | 中文 | 风险点 |
|------|------|--------|
| rhodopsin | 视紫红质 | 视杆主色素，见光漂白 |
| opsin | 视蛋白 | 漂白产物之一 |
| vitamin A | 维生素 A | 视网膜功能必需 |
| visual cycle / Wald's visual cycle | 视觉循环 | Known for 词 |
| spectrophotometer | 分光光度计 | 1950s 方法核心 |
| microspectrophotometry | 微分光光度术 | 单细胞直接测定 |
| cone cell / rod cell | 锥细胞 / 视杆细胞 | 三色素 vs 视紫红质 |
| Frederic Ives Medal | 艾夫斯奖章 | OSA 1966 |

## 九、背景音乐选择

- **选定曲目**：**Last Hope** — Alex-Productions（manifest 预分配）
- **匹配理由**：Last Hope 的深沉与微光感对应"黑暗中复原的色素"意象——视紫红质在暗处再生、
  让眼睛在黑夜中重获视觉；也贴合 1933 年离欧赴美、在哈佛重建生涯的移民科学家叙事弧线。
- **备选（未采用）**：Through the Darkness（暗感重叠但已被占用）、Lonesome（孤寂感偏"童年叙事"，不如本篇"黑暗中的化学微光"）
- **本地路径**：`music_audio/` 曲库按 curated_tracks.md 复制为 `medic/presentations/20th_century/George_Wald/Last_Hope.wav`
