# 医学家立传提示词（George Minot）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1934 年**得主（与 George Whipple、William P. Murphy 三人共享）。
> 本文件是 Minot 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：George Richards Minot（1885-12-02 ~ 1950-02-25，享年 64 岁），美国医师、血液学研究者
- **气质关键词**：**恶性贫血的征服者、以自身糖尿病续命而成就发现的人、哈佛血液临床学派旗手** —— 1934 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for their discoveries concerning liver therapy in cases of anaemia"（因其关于贫血的肝疗法发现）
- **设计母题**：**特别膳食（the special diet）**。1926 年那篇《以特别膳食治疗恶性贫血》——每日半斤煮熟的肝，把绝症变成慢性病，以「餐盘上的处方」作为视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/George_Minot/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/George_Minot/`；Makefile 复制后设 `MAIN=George_Minot_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | hematology | 血液学 | 1934 诺奖核心：恶性贫血的肝疗法 | 核心页 |
| 1 | internal medicine | 内科学 | 麻省总医院内科主任（1934 起）、哈佛医学教授 | 任职页 |
| 2 | nutrition | 营养学 | 1926 特别膳食疗法、肝浓缩物 | 核心页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | George Whipple | 无向 | 1934 诺贝尔生理学或医学奖共享（贫血肝疗法） |
| co-honored | William P. Murphy | 无向 | 1934 诺贝尔生理学或医学奖共享（贫血肝疗法）；1930 Cameron 奖亦共享 |
| spouse | Marian Linzee Minot (Weld) | 无向 | 1915 结婚，二女一子 |
| colleague | Alice Hamilton | 无向 | 一战同查军工厂 TNT 皮肤接触致病 |
| colleague | Elliott P. Joslin | 无向 | 哈佛同事、其糖尿病主治医生（胰岛素续命） |
| colleague | William Henry Howell | 无向 | 1913-1915 其约翰霍普金斯实验室研究抗凝血酶 |

**方向约定**：`advisor-student` + `direction: advisor` = 对方是导师；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：波士顿世家医者的沉稳、与死亡赛跑的紧张、临床的温暖
- **主色**：`#8C1515`（哈佛绯红，麻省总医院与血液）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：`badgeAnemia` 恶性贫血 — 血液深红 `#6E1E2B`；`badgeDiet` 肝食疗方 — 熟肝赭 `#9A5A2E`；`badgeInsulin` 胰岛素续命 — 医药青 `#1B7A6B`；`badgeHarvard` 哈佛岁月 — 绯红 `#8C1515`
- **背景母题**：米白底上叠印肝片剪影与上升的红细胞计数曲线，一枚血糖仪刻度隐于角落。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 征服恶性贫血 / George Minot 1885–1950 + 四色 badge + 右上肖像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Boston、哈佛 BA/MD、麻省总医院、荣誉）
03  核心贡献概览 — 肝疗法 / 恶性贫血 / 抗凝血酶 / 糖尿病共病人生
04  波士顿医学世家 (1885–1912) — James Jackson 玄孙（麻省总医院创始人之一）、1908 BA / 1912 MD
05  约翰霍普金斯 (1913–1915) — Howell 实验室抗凝血酶研究、1915 回麻省总医院
06  战时与 TNT 中毒调查 — 军医、与 Alice Hamilton 查新泽西弹药厂皮肤病
07  亨廷顿纪念医院 (1917–1923) — 贫血研究主阵地、1923 内科主任
08  1926 特别膳食（核心贡献页）— 与 Murphy《以特别膳食治疗恶性贫血》、每日肝餐、45 例临床
09  三人链条：Whipple→Minot/Murphy — 犬实验先行的 Whipple、机制后知为 B12
10  糖尿病与胰岛素的馈赠 (1921–1922) — Joslin 530 卡限食续命、Banting/Best 胰岛素及时问世（Castle 观察）
11  1934 诺贝尔奖 — 与 Whipple/Murphy 共享、1929 Kober 奖、1930 Cameron 奖（与 Murphy）
12  职务与荣誉 — 1934 physician-in-chief、Thorndike 实验室主任、1935 美哲学会、1937 NAS
13  晚年与身后 — 1940 糖尿病并发症、1947 中风偏瘫、1950-02-25 卒于 Brookline；故居国家历史地标
14  遗产：从肝餐到 B12 — 恶性贫血治疗范式、饮食疗法先声、Unitarian 信仰一笔
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒日 | 1885-12-02 生于 Boston；1950-02-25 卒于 Brookline，享年 64 |
| 获奖理由 | "for their discoveries concerning liver therapy in cases of anaemia"——**their**（与 Whipple/Murphy 三人共享） |
| 糖尿病时间线 | 1921（35 岁）确诊 → Joslin 限食 530 卡/日 → 1921 胰岛素发现、约一年后普及——胰岛素使其存活、间接成全肝疗法发现（经 Castle 观察，正文有载）——年份链条勿错 |
| 1930 Cameron 奖 | 与 Murphy 共享——可并入 co-honored note 或另提；与 1934 诺奖是两回事 |
| B12 后知 | 当时用的是「富 B12 的肝浓缩物」，B12 作为关键成分系**后来**才确定——勿写成当时已知 |
| 家族 | 父 James Jackson Minot 为医师；高祖之一 James Jackson 是麻省总医院共同创始人；曾祖父辈 Charles Sedgwick Minot 为解剖学家——家族线克制一笔 |
| 卒因 | 1940 起糖尿病并发症、1947 严重中风致偏瘫、1950 卒——勿写成死于肝病 |
| 信仰 | Unitarian（一位论派）——正文一笔，无需展开 |
| 配偶姓名 | Marian Linzee Minot (Weld)（1890-1979），1915 结婚，二女一子 |
| 无引语 | 本篇正文无直接引语——引号内不得出现「原话」，忠实转述即可 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| pernicious anemia | 恶性贫血 | 当时不治之症 |
| liver therapy | 肝疗法 | 诺奖理由核心词 |
| liver concentrate | 肝浓缩物 | 后确定关键成分为 B12 |
| vitamin B12 | 维生素 B12 | 后来才确定的 有效成分 |
| special diet | 特别膳食 | 1926 论文标题用语 |
| antithrombin | 抗凝血酶 | 约翰霍普金斯时期研究 |
| insulin | 胰岛素 | 1921 Banting/Best 发现，续其命 |
| diabetes mellitus | 糖尿病 | 1921 确诊 |
| Massachusetts General Hospital | 麻省总医院 | 其主战场 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Savage** — Alex-Productions（manifest 预分配）
- **风格**：张力 / 决断 / 冲刺感
- **匹配理由**：Minot 的发现是一场与死亡的赛跑——自己身患绝症、病床边是成排必死的恶性贫血患者；Savage 的张力匹配 1926 年「以膳食作处方」的破釜沉舟，也匹配其与胰岛素时间赛跑的人生底色（第二次使用该曲，首用 Ehrlich，同为攻坚者）。
- **本地路径**：`music_audio/` 下 Savage 曲目 → 复制为 `presentations/20th_century/George_Minot/Savage.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。
