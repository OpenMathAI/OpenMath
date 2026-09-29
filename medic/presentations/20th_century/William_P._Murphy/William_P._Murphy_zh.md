# 医学家立传提示词（William P. Murphy）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：William P. Murphy（1934 年诺贝尔生理学或医学奖得主，美国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/William_P._Murphy/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：William Parry Murphy Sr.（威廉·帕里·墨菲，1892-02-06 威斯康星州斯托顿 ~ 1987-10-09 马萨诸塞州布鲁克莱恩，享年 95 岁）
- **气质关键词**：**让恶性贫血从绝症变成可治之症的临床医生、肝疗法三人组的临床担当** —— 1934 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，三人共享）：
  > "for their discoveries concerning liver therapy in cases of anaemia"
  > （因其关于贫血的肝脏疗法的发现）
- **设计母题**：**「一盘肝脏」**。Whipple 用放血犬筛选食物、Minot/Murphy 把半生肝特膳推上病床——视觉隐喻：餐盘上的肝脏切片与爬升的红细胞曲线并置。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/William_P._Murphy/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/William_P._Murphy/`，成目录 `medic/presentations/20th_century/William_P._Murphy/`，Makefile 复制后设 `MAIN=William_P._Murphy_zh`、`VIDEO_NAME=William_P._Murphy_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | hematology | 血液学 | 恶性贫血（巨幼细胞性贫血）的诊治，1934 诺奖核心 | 总览页 |
| 1 | hepatology | 肝脏疗法 | 肝提取物特膳治疗恶性贫血的临床实施 | 肝疗法页 |
| 2 | internal medicine | 内科学 | 哈佛医学院出身的临床研究者 | 生涯页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/William_P._Murphy.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | George Whipple | — | 1934 诺贝尔生理学或医学奖三人共享（肝疗法） |
| co-honored | George Minot | — | 1934 诺奖三人共享，1926 年合著特膳疗法论文，1930 同获 Cameron Prize |
| spouse | Pearl Harriett Adams | — | 1919-09-10 成婚，1980 年卒 |
| parent-child | William P. Murphy Jr. | 子 | 后为发明家与医疗器械企业家 |
| parent-child | Priscilla Adams | 女 | — |
| parent-child | Thomas Francis Murphy | 父 | 公理会牧师 |
| parent-child | Rosa Anna Parry | 母 | 威尔士地主家庭出身 |

> 说明：1934 三人组的第三边（Whipple–Minot 互指）由 George_Whipple/George_Minot 所在批次（med-batch-07）各自建边，本篇只建 Murphy 侧。对手方 name_en 按 manifest 规范形式 George Whipple / George Minot（勿用页内链接全名 George Hoyt Whipple / George Richards Minot，防分裂）。与 Whipple 的「承其工作」关系并入 co-honored note，不另建 influence 边。1951 年 Lindau 首届诺奖得主会为组织性活动，不建边。

## 五、配色方案 【人物专属】

- **气质**：临床、务实、从厨房餐桌到病床的转化医学
- **主色**：深血红 `#6E1F2E`（贫血与血液的视觉主轴）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 血液学 — 红细胞红 `#C0392B`
  - `badgeB` 肝脏疗法 — 肝褐 `#8E4B2E`
  - `badgeC` 内科学 — 听诊蓝 `#33637D`
  - `badgeD` 维生素 B12 — 钴蓝 `#2C5FA8`
- **背景母题**：稀疏的餐盘圆形与上升折线（网织红细胞回升曲线），低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 让绝症可治的临床医生 / William P. Murphy 1892–1987 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、教育、家庭、荣誉、核心领域）
03  核心贡献概览 — 肝疗法三人组分工 / 特膳治疗 / 维生素 B12 的远源
04  早年：威斯康星-俄勒冈 (1892–1914) — 牧师之家、1914 俄勒冈大学 A.B.
05  哈佛医学院 (1914–1922) — 1922 年获 M.D.，战间期的临床训练
06  恶性贫血：当时的绝症 — 巨幼细胞性贫血的致命性与治疗困境
07  Whipple 的犬实验 (1924) — 放血造模、以肝恢复最快；三人组工作的起点
08  Minot & Murphy 的特膳 (1926)（核心页）— 1926 年名论文 Treatment of pernicious anemia by a special diet
09  1934 诺贝尔奖（核心页）— citation 原文（三人共享）、1934-12-12 诺奖演讲 Pernicious Anemia
10  从肝提取物到维生素 B12 — 水溶性提取物→B12 分离的接力（当时尚未完全定性）
11  荣誉与认可 — Nobel 1934 · Cameron Prize 1930（与 Minot 共享）· 1951 首届 Lindau 会议七位诺奖得主之一
12  家庭与晚年 — 1919 年成婚、子 William P. Murphy Jr. 的发明家之路、95 岁高龄辞世
13  遗产：恶性贫血的现代疗法 — 从特膳到 B12 注射/口服的一步之遥
14  三人组的历史坐标 — Whipple 的筛选、Minot 的临床设计、Murphy 的临床执行
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for their discoveries concerning liver therapy in cases of anaemia"（their 三人共享）；勿写成「因发现维生素 B12」——B12 分离是后续化学家的工作，page.md 明载当时 vitamin 尚未完全定性 |
| 2 | 三人分工 | Whipple 犬实验筛选（1924）、Minot&Murphy 特膳临床（1926 论文两人署名）、铁只对失血性贫血有效而恶性贫血的有效成分是水溶性提取物——三层勿混 |
| 3 | 名字 | 本人全名 William Parry Murphy Sr.，manifest/库内规范名 William P. Murphy；其子 William P. Murphy Jr. 是同名不同人，行文必须带 Jr. 区分 |
| 4 | 对手方规范名 | co-honored 边一律用 manifest 形式 George Whipple / George Minot；页内链接全名仅正文首次出现时用一次 |
| 5 | Cameron Prize | 1930 年与 George Minot 共享——是第二个共享荣誉，勿与 1934 诺奖混写 |
| 6 | iron 陷阱 | 肝中的铁治愈的是失血性贫血；恶性贫血的有效成分「纯属意外发现」——此因果链是 page.md 明载要点，勿写成「铁治愈恶性贫血」 |
| 7 | 页面简短 | 本篇 page.md 较短，禁为凑页数编造轶事；时间线以 Education/职业节点与三人组科研叙事展开 |
| 8 | 家庭数据 | 妻 Pearl Harriett Adams（infobox 作 Harriett Adams）取正文全名；女儿 Priscilla Adams 仅名单提及 |
| 9 | Lindau | 1951 年首届 Lindau 诺奖得主会议七位出席者之一——一句带过即可 |
| 10 | metadata 冲突 | metadata.json 与 page.md 无实质冲突；生卒一致 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| pernicious anemia | 恶性贫血 | 巨幼细胞性贫血的典型型 |
| macrocytic anemia | 巨幼细胞性贫血 | 上位概念，勿与缺铁性贫血混淆 |
| liver therapy | 肝脏疗法 | 诺奖理由核心词，指食疗/提取物 |
| antianemic factor | 抗贫血因子 | 后被定性为维生素 B12 |
| vitamin B12 | 维生素 B12（钴胺素） | 三人组时代尚未分离定性 |
| special diet | 特膳（半生肝食疗） | 1926 论文标题用语 |
| intrinsic factor | 内因子 | 背景术语，page 未展开勿深写 |
| reticulocyte | 网织红细胞 | 疗效指标（可作示意） |
| Cameron Prize | 卡梅伦奖 | 爱丁堡大学治疗学奖 |
| Lindau Meeting | 林道诺贝尔奖得主大会 | 1951 年首届 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Tragedy** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「沉重→转机」的结构匹配恶性贫血叙事——终症绝境中靠一盘肝脏逆转，悲剧底色上的救赎
  - 慢板节奏契合临床转化的耐心：从犬实验筛选到病床特膳的十年长跑
- **备选**（未采用）：Last Hope（「希望」意象贴切但留给更绝望的题材）、SEA（过缓，缺转机段落的推进感）
- **本地路径**：按 music_audio/ 内 Alex-Productions Tragedy 曲目复制至 `medic/presentations/20th_century/William_P._Murphy/Tragedy.wav`，ffmpeg `-shortest` 对齐
