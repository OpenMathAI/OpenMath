# 医学家立传提示词（Shinya Yamanaka）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2012 年得主 Shinya Yamanaka（山中伸弥）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Shinya_Yamanaka/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Shinya Yamanaka（山中 伸弥，1962-09-04 生于日本大阪府东大阪市，在世）
- **气质关键词**：**iPS 细胞之父、逆转细胞命运的四因子执灯人、马拉松式的坚持者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2012 条目，与 John Gurdon 共享同一理由）：
  > "for the discovery that mature cells can be reprogrammed to become pluripotent"（因发现成熟细胞可被重编程为多能性细胞）
- **设计母题**：**四把钥匙（four factors）**——Oct4/Sox2/Klf4/c-Myc 四把钥匙开启动画般的细胞"重置"：以四色钥匙/开关点亮卵圆形细胞的图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Shinya_Yamanaka/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Shinya_Yamanaka/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Shinya_Yamanaka_zh`、`VIDEO_NAME=Shinya_Yamanaka_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | induced pluripotent stem cell | 诱导多能干细胞（iPS） | 2006 小鼠/2007 人源 iPS，2012 诺奖核心 |
| 1 | stem cell research | 干细胞研究 | infobox Fields 明载 |
| 2 | cellular reprogramming | 细胞重编程 | 四转录因子逆转细胞命运 |
| 3 | regenerative medicine | 再生医学 | CiRA 使命；2026 首批 iPS 再生医疗产品获批 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Kazutoshi Takahashi | 无向 | 2006 首篇 iPS 论文第一作者，2011 共享 McEwen 创新奖 |
| co-honored | John Gurdon | 无向 | 2012 诺贝尔生理学或医学奖共享（成熟细胞重编程为多能性） |
| co-honored | Rudolf Jaenisch | 无向 | 2011 沃尔夫医学奖共享 |
| co-honored | Linus Torvalds | 无向 | 2012 千年技术奖共享（120 万欧元） |

**不入库但提示词可叙述**：Katsuyuki Miura（frontmatter metadata 列为博士导师，但 infobox 与正文均无载——**metadata-only 不入库**）；Ryōji Noyori（同框照片，无实质关系）；Haruko Obokata（2014 STAP 风波相关人物，见陷阱表，不建边）；Tasuku Honjo（See also 提及，page.md 无关系叙述）。

## 五、配色方案 【人物专属】

- **气质**：克制、精进、把细胞拨回起点的温柔力量
- **主色**：`#1B4D6B`（琵琶湖深青——京都 CiRA 的沉静）+ 香槟金诺奖色
- **badge 四分类色**：`badgeiPS` iPS 细胞 深青 `#1B4D6B`；`badgeFactor` 四因子 玫瑰 `#A63A2B`；`badgeRegen` 再生医学 青绿 `#0E7C7B`；`badgeClinic` 临床转化 琥珀 `#C07A2A`
- **背景母题**：四色钥匙/开关点亮卵圆形细胞，呼应「四把钥匙」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — iPS 细胞之父 / Shinya Yamanaka 1962– + 四色 badge + 右上头像 + 国籍行（Japan）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1962-09-04 东大阪、神户大学 MD 1987、
    大阪市立大学 PhD 1993、京都大学 CiRA 首任所长 2010–2022、诺奖 2012）
03  核心贡献概览 — 四因子 / 2006 小鼠 iPS / 2007 人源 iPS / 再生医学落地
04  东大阪少年与运动 (1962–1981) — 天王寺高中、柔道二段、橄榄球
05  从骨科住院医到科学家 (1987–1993) — 神户大学 MD、"Jamanaka"（障碍）绰号、
    大阪市立大学 PhD 1993
06  旧金山岁月 (1993–1996) — Gladstone 心血管研究所博士后
07  大阪与 NAIST (1996–2004) — 助理教授时期"mostly looking after mice"、
    NAIST 应聘立下阐明 ES 细胞特性的志向
08  2006：四因子重编程（核心贡献页）— 24 候选因子 → Oct3/4、Sox2、Klf4、c-Myc；
    Fbx15/b-geo 筛选；小鼠成纤维细胞 → iPS
09  2007：人源 iPS 与 germline — Oct4/Nanog 筛选获 germline 传递 iPS；全球首组人源 iPS
10  与 Gurdon 的五十年接力 — 1962 Gurdon 核移植范式转变 → 2006 完整细胞直接重编程
11  CiRA 与京都大学 (2004–2022) — 再生医学科学研究所 2004 起、CiRA 首任所长 2010–2022、
    2022-04 退任 director emeritus 保留教授职
12  荣誉与认可 — Meyenburg 2007、Massry/Koch/Shaw 2008、Gairdner/Lasker 2009、
    Balzan/Kyoto Prize 2010、Wolf 2011、Millennium/Nobel/文化勋章 2012、
    Breakthrough 2013、教皇科学院院士
13  从实验室到病床 — 2013 小鼠体内功能化肝脏；2026 厚生劳动省有条件批准两个 iPS
    再生医疗产品（史上首次实际应用）；iPS 疾病建模（ALS 等）
14  遗产与结尾 — 绕开胚胎伦理的第三条路；马拉松跑者 3:25:20 的坚持；CiRA 共同体
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 博士导师不入库 | frontmatter metadata 列 Katsuyuki Miura 为 doctoral_advisor，但 infobox 与正文均无载——**metadata-only 不入库**，立传正文亦不写师承（纪律示范条目） |
| 四因子名称 | Oct3/4（Oct4）、Sox2、Klf4、c-Myc——page.md 两种写法并存（Sox2/Oct4 与 Myc/Oct3/4），立传统一用 Oct4/Sox2/Klf4/c-Myc 并注明 Oct3/4 同物 |
| 时间线 | 2006 小鼠 iPS（成纤维细胞）→ 2007 germline 传递（Oct4/Nanog 筛选）与全球首组人源 iPS——三个里程碑年份勿混 |
| 24 → 4 | 从 24 个 ES 细胞重要转录因子起步，逐步淘汰至四因子——过程叙事亮点，勿写成"直接想到四因子" |
| iPS 风险表述 | 四因子含致癌基因（oncogenic potential）、效率极低、异常 aging——page.md 明载的局限性须如实呈现，勿只写光明面 |
| Obokata 风波 | 2014 年 STAP 论文造假事件中 Yamanaka 因相关早期工作记录不全受到审视，本人否认操纵图像但找不到实验记录；CiRA 声明"无充分证据质疑其诚信是完全不可接受的"——如处理须客观三段式，不建边、不渲染 |
| 2026 落地 | 厚生劳动省对两个 iPS 再生医疗产品发有条件上市许可（conditional marketing authorization）——"史上首次实际应用"的表述以 page.md 为准 |
| 千年技术奖 | 与 Linus Torvalds（Linux 之父）共享 120 万欧元——跨领域趣闻可写，勿与诺贝尔奖混淆 |
| 运动数据 | 柔道二段、2011 大阪马拉松 4:29:53、2018 别府大分马拉松个人最佳 3:25:20——数字勿串 |
| 职务精确 | CiRA 所长 2010–2022，2022-04 退任 director emeritus（不是 2024，也不 retain"所长"） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| induced pluripotent stem cell (iPS) | 诱导多能干细胞 | 获奖工作核心，勿与 ES 细胞混 |
| transcription factor | 转录因子 | 四因子的分子类别 |
| Oct4 / Sox2 / Klf4 / c-Myc | 四因子 | 细胞重编程的钥匙 |
| pluripotent | 多能性 | 获奖理由核心词 |
| fibroblast | 成纤维细胞 | 起始细胞类型 |
| teratoma | 畸胎瘤 | 多能性体内验证 |
| chimeric mouse | 嵌合体小鼠 | germline 传递验证 |
| Fbx15 / b-geo selection | Fbx15/b-geo 筛选体系 | 2006 年 iPS 的筛选原理 |
| CiRA | 京都大学 iPS 细胞研究所 | 2010–2022 任所长 |
| regenerative medicine | 再生医学 | 临床转化方向 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Nostalgia**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：iPS 的本质是让成熟细胞"怀念"并回到最初的起点——"Nostalgia" 的回望感与细胞逆转命运的隐喻天然契合；同时呼应他与 Gurdon 相隔五十年的范式接力。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Shinya_Yamanaka/Nostalgia.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
