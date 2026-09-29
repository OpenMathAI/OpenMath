# 医学家立传提示词（Allvar Gullstrand）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Allvar Gullstrand（1911 年诺贝尔生理学或医学奖得主，瑞典）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Allvar_Gullstrand/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Allvar Gullstrand（阿尔瓦·古尔斯特兰德，1862-06-05 兰斯克鲁纳 ~ 1930-07-28 斯德哥尔摩，享年 68 岁）
- **气质关键词**：**用数学照亮眼球的人、生理光学的立法者、诺奖委员会里的「守门人」** —— 1911 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json）：
  > "for his work on the dioptrics of the eye"
  > （因其关于眼睛屈光学的工作）
- **设计母题**：**「光线的几何」**。把物理数学方法引入眼内光路与屈光成像——视觉隐喻：一束光线穿过晶状体剖面后的聚焦路径，用参数化曲线与焦点标记构成背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Allvar_Gullstrand/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Allvar_Gullstrand/`，成目录 `medic/presentations/20th_century/Allvar_Gullstrand/`，Makefile 复制后设 `MAIN=Allvar_Gullstrand_zh`、`VIDEO_NAME=Allvar_Gullstrand_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | ophthalmology | 眼科学 | 乌普萨拉教授（1894–1927），1911 诺奖核心 | 总览页 |
| 1 | physiological optics | 生理光学 | 眼屈光系统的数学模型（Gullstrand 模型眼） | 屈光页 |
| 2 | optics | 光学 | 后期转任乌普萨拉光学教授；非球面镜面研制 | 光学页 |
| 3 | astigmatism | 散光研究 | 散光研究与检眼镜、白内障术后矫正镜片改进 | 散光页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Allvar_Gullstrand.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Signe Breitholtz | — | 1885 年成婚 |
| controversy | Albert Einstein | — | 1921 年任物理学诺贝尔委员会委员，阻挠相对论获奖 |
| colleague | Paul Painlevé | — | 各自独立解静态单体问题，坐标以两人命名 |

> 说明：page.md 叙事极简，仅此三条明载关系；Horatio Burt Williams（1926 年感叹其论文难读）、Carl Wilhelm Oseen（1922 年接替其委员会席位）、Niels Bohr（1922 同届物理奖）均只是叙事提及，不入库。

## 五、配色方案 【人物专属】

- **气质**：精密、冷冽、北欧的理性之光
- **主色**：屈光蓝 `#24506E`（镜片折射的深海蓝）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 眼科学 — 巩膜白青 `#7FB3C8`
  - `badgeB` 生理光学 — 光路金 `#D9A441`
  - `badgeC` 光学 — 棱镜紫 `#6E5AA0`
  - `badgeD` 散光研究 — 像散橙 `#C4622D`
- **背景母题**：稀疏的同心弧线与焦点光斑（模拟角膜-晶状体屈光面），低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 用数学照亮眼球的人 / Allvar Gullstrand 1862–1930 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒兰斯克鲁纳/斯德哥尔摩、乌普萨拉、家庭、荣誉、核心领域）
03  核心贡献概览 — 眼屈光数学模型 / 散光 / 检眼镜改进 / 光学教授任期
04  早年与乌普萨拉 (1862–1894) — 兰斯克鲁纳出身、医学训练、1894 眼科治疗学教授
05  生理光学的数学化（核心页）— 物理数学方法引入眼内成像、模型眼
06  散光与临床器械 — 散光研究、检眼镜改进、白内障术后矫正镜片
07  1911 诺贝尔奖（核心页）— citation 原文 "for his work on the dioptrics of the eye"、1911-12-10 宴会致辞
08  双重教席：从眼科到光学 (1894–1927) — 先眼科治疗学后光学教授的罕见轨迹
09  瑞典皇家科学院与物理学委员会 — 1905 当选院士、任物理学诺奖委员会委员
10  1921：挡下爱因斯坦的守门人 — 五十页报告、当年物理奖空缺、1922 改授光电效应的来龙去脉
11  广义相对论的业余攻坚 — 1922 静态单体问题解、Gullstrand–Painlevé 坐标
12  曲高和寡 — 1926 Williams 感叹：能读其论文的眼科学家寥寥（引语原文+译文）
13  以 Gullstrand 命名 — Gullstrand 模型眼、Gullstrand–Painlevé 坐标、诺奖邮票（1971 系列）
14  遗产：视光学的几何基石 — 从模型眼到现代 IOL 计算公式
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for his work on the dioptrics of the eye"；勿写成「因眼科研究贡献」之类泛化 |
| 2 | 1911 双奖背景 | 1911 年物理学奖（Wilhelm Wien）与他同年，勿混淆；他获的是生理学或医学奖，是「眼科医生获医学诺奖」而非物理奖 |
| 3 | 阻挠爱因斯坦 | 1921 年他以委员会委员身份用五十页报告反对相对论获奖、当年物理奖空缺、1922 年 Einstein 改以光电效应补得 1921 奖——page.md 明载可写；报告引语 "Einstein's work is not useful enough for the human race...we should wait for measurable evidence" 有英文原文，可引 |
| 4 | 争议的写法 | 该争议只陈述事实与时间线，不作褒贬评价；标题用「守门人」式中性表述，勿写「固执/错误之人」定性 |
| 5 | Gullstrand–Painlevé 坐标 | 1922 年他独立发表静态单体问题解，与 Paul Painlevé 结果相似而共同得名；这是广义相对论语境下的工作，与获诺奖的眼科工作分开叙述 |
| 6 | 身后归类 | page.md 无独立「师承/门生」叙事，禁编造导师或学生 |
| 7 | 配偶信息 | 仅 Signe Breitholtz（1862–1946，1885 年成婚）一条；无子女叙事，禁杜撰 |
| 8 | Works 年份 | Works 列表有 1905 条目排在 1906/1908 之间（原文排序如此），幻灯片引用时按真实年份归位，勿照抄列表顺序 |
| 9 | 死亡地 | 逝于斯德哥尔摩，葬 Norra begravningsplatsen；勿与出生地兰斯克鲁纳混淆 |
| 10 | metadata 冲突 | metadata.json 与 page.md 一致（Björkén Prize 1906、Graefe medal 荣誉可提，年份以 infobox 为准） |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| dioptrics | 屈光学 | 诺奖理由用词，勿译「屈光度」 |
| schematic eye / Gullstrand eye | 模型眼（Gullstrand 模型眼） | 光学参数化人眼模型 |
| astigmatism | 散光 | 与「老视」区分 |
| ophthalmoscope | 检眼镜 | 他做过改进，非发明人 |
| cataract | 白内障 | 术后矫正镜片语境 |
| optical aberration | 光学像差 | 与像散（astigmatism）区分 |
| Gullstrand–Painlevé coordinates | Gullstrand–Painlevé 坐标 | 史瓦西度规的另一坐标系 |
| Schwarzschild metric | 史瓦西度规 | 静态单体问题所指 |
| slit lamp | 裂隙灯 | See also 提及，勿写为其发明 |
| corneal topography | 角膜地形图 | See also 提及的下游领域 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Eternals** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「永恒/冷峻」匹配其工作对象——眼球的光学结构亘古不变，他用数学为它写下永恒参数
  - 也匹配其「守门人」形象：在诺奖历史中留下不可磨灭（且争议持久）的一笔
- **备选**（未采用）：Timeless（气质相近但物理侧高频占用）、New Lands（开拓感偏冒险叙事）
- **本地路径**：按 music_audio/ 内 Alex-Productions Eternals 曲目复制至 `medic/presentations/20th_century/Allvar_Gullstrand/Eternals.wav`，ffmpeg `-shortest` 对齐
