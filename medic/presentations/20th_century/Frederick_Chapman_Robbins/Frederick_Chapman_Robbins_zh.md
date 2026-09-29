# 医学家立传提示词（Frederick Chapman Robbins）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1954 年**得主（与 John Franklin Enders、Thomas Huckle Weller 三人共享）。
> 本文件是 Robbins 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Frederick Chapman Robbins（1916-08-25 ~ 2003-08-04，享年 86 岁），美国儿科医生、病毒学家
- **气质关键词**：**阿拉巴马出生的唯一诺奖得主、组织培养里养脊灰病毒的人、凯斯西储医学院的终身守望者** —— 1954 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for their discovery of the ability of poliomyelitis viruses to grow in cultures of various types of tissue"（因其发现脊髓灰质炎病毒能在多种组织培养物中生长）
- **设计母题**：**旋转培养管（the roller tube）**。Robbins 用旋转培养管让脊灰病毒在各种组织上生长——以「缓缓旋转的细管中生长的病毒斑」作为视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Frederick_Chapman_Robbins/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Frederick_Chapman_Robbins/`；Makefile 复制后设 `MAIN=Frederick_Chapman_Robbins_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学 | 1954 诺奖核心：脊灰病毒组织培养 | 核心页 |
| 1 | pediatrics | 儿科学 | 凯斯西储儿科教授（1952 起）、终身方向 | 任职页 |
| 2 | microbiology | 微生物学 | 病毒培养的微生物学方法 | 研究页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | John Franklin Enders | 无向 | 1954 诺贝尔生理学或医学奖三人共享 |
| co-honored | Thomas Huckle Weller | 无向 | 1954 诺贝尔生理学或医学奖三人共享 |
| spouse | Alice N. Robbins | 无向 | 2016 卒；诺奖得主 Northrop 之女 |
| parent-child | John Howard Northrop | 辈分（岳父） | 妻 Alice 系其女；Northrop 为 1946 诺贝尔化学奖得主 |

**方向约定**：`parent-child` + `direction: parent` = 对方是长辈（岳父，沿用 Ehrlich–Landau 先例）；其余无向。

## 五、配色方案 【人物专属】

- **气质**：儿科医生的温和、旋转培养管的耐心、86 岁扎根一校的持重
- **主色**：`#6E2B2B`（红砖暗红，凯斯西储红砖楼与血液）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：`badgePolio` 脊灰病毒 — 病毒青 `#1B7A6B`；`badgePeds` 儿科 — 儿童暖橙 `#C0722E`；`badgeCWRU` 凯斯西储岁月 — 红砖 `#6E2B2B`；`badgeIoM` 医科院院长 — 石板蓝 `#3A5A6E`
- **背景母题**：浅色底上一排缓旋培养管剪影，管内病毒斑以小圆点表示，错落连缀。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 旋转管里的突破 / Frederick Chapman Robbins 1916–2003 + 四色 badge + 右上肖像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Auburn/Columbia 密苏里、密苏里/哈佛、凯斯西储、荣誉）
03  核心贡献概览 — 脊灰病毒组织培养 / 旋转管技术 / 疫苗铺路 / 医学教育
04  密苏里少年 (1916–1936) — 生于 Auburn 阿拉巴马、长于 Columbia 密苏里、Hickman 高中
05  密苏里与哈佛 (1936–1940s) — 密苏里大学本科、哈佛医学院
06  波士顿岁月与三人组 (1948–1952) — 加入 Enders 实验室、1949 动物病毒体外培养首例
07  旋转培养管（核心贡献页）— 各种组织培养物上培养脊灰病毒、为 Salk/Sabin 疫苗铺路
08  1952 回西部 — 受聘凯斯西储儿科教授、克利夫兰扎根
09  1953 E. Mead Johnson 奖 — 诺奖前哨
10  1954 诺贝尔奖 — 三人共享、阿拉巴马出生的唯一诺奖得主
11  凯斯西储院长 (1966–1980) — 医学院院长、1972 NAS 院士、1980-85 医科院（IOM）院长
12  荣归与终身守望 (1985–2003) — 荣休院长与杰出大学教授、Robbins Society 以其命名
13  荣誉 — 1962 美艺科学院院士、1972 美哲学会、1999 富兰克林奖章
14  遗产：疫苗时代的基石 — 脊灰疫苗两系（Salk/Sabin）的铺垫、Robbins Society 传承
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒日 | 1916-08-25 生于 Auburn, Alabama；2003-08-04 卒于 Cleveland, Ohio，享年 86——正文明载其为**阿拉巴马出生的唯一诺奖得主** |
| 获奖理由 | "for their discovery of the ability of poliomyelitis viruses to grow in cultures of various types of tissue"——**their**（与 Enders/Weller 三人共享） |
| 生日同日趣事 | 8 月 25 日生日、8 月 4 日卒日同为八月——无需过度发挥 |
| 成长地 | 生于阿拉巴马 Auburn、**成长于密苏里 Columbia**——两地勿混 |
| 「唯一」表述 | 「阿拉巴马出生的唯一诺奖得主」正文有载；勿扩大为「南方诸州唯一」等说法 |
| 疫苗铺路 | 正文明载其工作为 **Salk 与 Sabin** 两系疫苗铺路——两人并列，勿只提 Salk |
| 家庭 | 妻 Alice N. Robbins 2016 卒，系 1946 诺奖得主 **John Howard Northrop** 之女——岳父边沿用 Ehrlich–Landau 的 parent-child 先例；夫妻自身信息正文单薄，spouse 边仅作存目 |
| 职务年代 | 儿科教授 1952 起、院长 1966-1980、IOM 院长 1980-85、1985 荣归凯斯西储——年份链勿错 |
| 引语 | 本篇正文无直接引语——引号内不得出现「原话」，忠实转述即可 |
| 三人分工 | 本人页面只讲三人合作与病毒分离培养；Enders 实验室主导叙事在 Enders 篇——本篇忠于本人页面 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| poliomyelitis virus | 脊髓灰质炎病毒 | 诺奖理由核心词 |
| tissue culture | 组织培养 | 多种类型组织均可 |
| roller tube culture | 旋转管培养 | 其代表性技术（本篇母题） |
| poliovirus isolation | 脊灰病毒分离培养 | 疫苗研发前提 |
| Salk vaccine | Salk 灭活疫苗 | 1955 问世 |
| Sabin vaccine | Sabin 减毒疫苗 | 口服减毒系 |
| pediatrics | 儿科学 | 其本职与凯斯西储教席 |
| Institute of Medicine | 美国医学科学院（IOM） | 1980-85 任院长 |
| Case Western Reserve | 凯斯西储大学 | 终身归属地 |
| Benjamin Franklin Medal | 富兰克林奖章 | 1999 美哲学会授予 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Lonesome** — Alex-Productions（manifest 预分配）
- **风格**：孤寂 / 深情 / 回望
- **匹配理由**：在诺奖三人组中，Robbins 是早早离开波士顿、独守克利夫兰一校近半个世纪的那一位——Lonesome 的孤寂回望匹配其「一人一校」的持重人生，也匹配密苏里少年到医科院院长的漫长独行者剪影。
- **本地路径**：`music_audio/` 下 Lonesome 曲目 → 复制为 `presentations/20th_century/Frederick_Chapman_Robbins/Lonesome.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。

