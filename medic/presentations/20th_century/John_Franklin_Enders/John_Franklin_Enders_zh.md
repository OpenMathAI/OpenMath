# 医学家立传提示词（John Franklin Enders）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1954 年**得主（与 Thomas Huckle Weller、Frederick Chapman Robbins 三人共享）。
> 本文件是 Enders 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：John Franklin Enders（1897-02-10 ~ 1985-09-08，享年 88 岁），美国病毒学家，「现代疫苗之父」
- **气质关键词**：**让脊灰病毒在试管里生长的人、麻疹疫苗的缔造者、谦逊让功的波士顿绅士** —— 1954 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for their discovery of the ability of poliomyelitis viruses to grow in cultures of various types of tissue"（因其发现脊髓灰质炎病毒能在多种组织培养物中生长）
- **设计母题**：**试管里的病毒牧场（a virus farm in the flask）**。脊灰病毒首次离开活体宿主、在组织培养中繁殖——以「培养瓶中成群的病毒颗粒」作为全篇视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/John_Franklin_Enders/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/John_Franklin_Enders/`；Makefile 复制后设 `MAIN=John_Franklin_Enders_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学 | 1954 诺奖核心：脊灰病毒组织培养 | 核心页 |
| 1 | vaccinology | 疫苗学 | 麻疹疫苗研制、被称「现代疫苗之父」 | 疫苗页 |
| 2 | bacteriology | 细菌学 | 哈佛博士（1930）与传染病方向起点 | 早年页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Thomas Huckle Weller | 无向 | 1954 诺贝尔生理学或医学奖三人共享 |
| co-honored | Frederick Chapman Robbins | 无向 | 1954 诺贝尔生理学或医学奖三人共享 |
| colleague | Thomas C. Peebles | 无向 | 1954 合作自 11 岁男孩 Edmonston 分离麻疹病毒 |
| colleague | Jonas Salk | 无向 | 应用其组织培养技术大量繁殖脊灰病毒研制疫苗（1952） |

**方向约定**：无向关系 from<to 自动归一。

## 五、配色方案 【人物专属】

- **气质**：新英格兰绅士的从容、波士顿儿童医院的暖色、疫苗带来的希望
- **主色**：`#1B5E8C`（疫苗蓝，培养瓶与希望）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：`badgePolio` 脊灰病毒 — 病毒青 `#1B7A6B`；`badgeCulture` 组织培养 — 培养瓶蓝 `#2E5E7E`；`badgeMeasles` 麻疹疫苗 — 麻疹红 `#A33A2E`；`badgeYale` 耶鲁与空军岁月 — 军蓝 `#4E6478`
- **背景母题**：浅蓝底上培养瓶剪影与瓶内悬浮的病毒小圆群，错落连成网络。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 现代疫苗之父 / John Franklin Enders 1897–1985 + 四色 badge + 右上肖像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、West Hartford、耶鲁/哈佛、波士顿儿童医院、荣誉）
03  核心贡献概览 — 脊灰病毒培养 / 麻疹病毒分离 / 麻疹疫苗 / 谦逊让功
04  富家子的曲折起点 (1897–1930) — 银行 CEO 之父留 1900 万美元遗产、耶鲁→一战飞行教官→地产→传染病方向
05  哈佛与波士顿儿童医院 (1930–1948) — 1930 博士、加入儿童医院教席
06  1949 突破（核心贡献页）— 与 Weller/Robbins 报告动物病毒首例体外培养、1954 三人诺奖
07  技术的果实：Salk 疫苗 — Salk 1952 应用其技术量产病毒、1954 现场试验成功、Salk 未谢诸家的风波
08  分离麻疹病毒 (1954) — 与 Peebles、供体男孩 David Edmonston、疫苗株之名的由来
09  对 Salk 灭活疫苗的失望 — 个别病例致瘫致死（Enders 归因于 Salk 技术）→ 转向研制麻疹疫苗
10  麻疹疫苗试验 (1960–1963) — 纽约 1500 名儿童 + 尼日利亚 4000 名儿童、1963 灭活/减毒双疫苗上市
11  谦逊的一封信 (1961) — NYT 宣布疫苗有效次日，致信列名全体合作者——人格注脚
12  1954 诺贝尔奖与荣誉 — Lasker 同年、Polio Hall of Fame 1958、Koch 奖 1962、总统自由勋章 1963
13  迟来的承认 — 1967 皇家学会外籍会员；13 所大学荣誉博士
14  遗产与身后 — 波士顿儿童医院 Enders 实验室（1970 落成）、1985 卒于 Waterford 夏宅
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒日 | 1897-02-10 生于 West Hartford, Connecticut；1985-09-08 卒于 Waterford, Connecticut 夏宅，享年 88 |
| 获奖理由 | "for their discovery of the ability of poliomyelitis viruses to grow in cultures of various types of tissue"——**their**（与 Weller/Robbins 三人共享） |
| 三人分工 | 1949 年报告以 Enders 实验室为主；三人同年同奖——Weller/Robbins 各自页面另有分工表述，本篇忠于本人页面 |
| Salk 风波 | Salk 应用其技术造疫苗但「failed to credit the many other researchers」而被学界疏远；Enders 把灭活疫苗致瘫致死个案归因于 Salk 技术——两处均正文有载，客观呈现不裁决 |
| 麻疹疫苗试验对象 | 纽约 1500 名智力障碍儿童 + 尼日利亚 4000 名儿童（1960-10 起）——史实须如实，表述克制 |
| 让功之信 | 1961-09-17 NYT 宣布疫苗有效，Enders 次日致信承认全体合作者与协作性质——人格亮点，可作收束页 |
| 家庭 | 妻（未具名）2000 年卒——无具名不建 spouse 边，陷阱表注明 |
| 「现代疫苗之父」 | 正文称 "has been called"——转述语气保留，勿写成官方头衔 |
| 曲折前半生 | 耶鲁肄业→一战飞行教官→地产（1922）→多番转行才入生物医学——叙事亮点勿删 |
| 引语 | 本篇正文无直接引语——引号内不得出现「原话」，忠实转述即可 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| poliomyelitis virus | 脊髓灰质炎病毒 | 诺奖理由核心词 |
| tissue culture | 组织培养 | 病毒体外增殖载体 |
| in vitro culture | 体外培养 | 1949 动物病毒首例 |
| polio vaccine | 脊灰疫苗 | Salk 1952 应用其技术 |
| measles virus | 麻疹病毒 | 1954 与 Peebles 分离 |
| Edmonston strain | Edmonston 株 | 以供体男孩 David Edmonston 命名 |
| attenuated vaccine | 减毒疫苗 | 1963 Merck 上市 |
| inactivated vaccine | 灭活疫苗 | 1963 Pfizer 上市 |
| Polio Hall of Fame | 脊灰名人堂 | 1958 入选 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Cinematic Experience** — Alex-Productions（manifest 预分配）
- **风格**：史诗感 / 电影配乐 / 大叙事
- **匹配理由**：从 1900 万遗产的富家子到让全人类儿童远离脊灰与麻疹——Enders 的一生自带电影弧光；Cinematic Experience 的史诗感匹配 1949 突破的银幕时刻与 1961 让功之信的高潮。
- **本地路径**：`music_audio/` 下 Cinematic Experience 曲目 → 复制为 `presentations/20th_century/John_Franklin_Enders/Cinematic_Experience.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。

