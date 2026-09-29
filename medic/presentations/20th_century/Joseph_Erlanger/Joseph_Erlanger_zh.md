# 医学家立传提示词（Joseph Erlanger）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1944 年得主 Joseph Erlanger（约瑟夫·厄尔兰格）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Joseph_Erlanger/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Joseph Erlanger（1874-01-05 生于旧金山 ~ 1965-12-05 逝于密苏里州圣路易斯，享年 91 岁）
- **气质关键词**：**单根神经纤维的听诊者、示波器的改造者、圣路易斯生理学掌门**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1944 条目，与 Gasser 共享同句）：
  > "for their discoveries relating to the highly differentiated functions of single nerve fibres"（因其关于单根神经纤维高度分化功能的发现）
- **设计母题**：**纤维的谱系（the spectrum of fibres）**——动作电位速度与纤维直径成正比、神经元形态与兴奋性各异；用「粗细不一的神经纤维束与其电位尖峰谱」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Joseph_Erlanger/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Joseph_Erlanger/`。Makefile 复制后设 `MAIN=Joseph_Erlanger_zh`、`VIDEO_NAME=Joseph_Erlanger_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Erlanger 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | physiology | 生理学 | 神经纤维功能分化，1944 诺奖核心 | 封面、核心页 |
| 1 | neuroscience | 神经科学 | 动作电位与纤维直径关系 | 核心页 |
| 2 | electrophysiology | 电生理学 | 阴极射线示波器改造与神经电位放大 | 核心页 |
| 3 | cardiology | 心脏病学 | 早期房室传导研究、血压计专利 | 早年页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 正文/infobox 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Herbert Spencer Gasser | Erlanger → 学生 | 威斯康星时期的学生，随迁圣路易斯入其实验室；infobox Notable students 明载（跨批次：batch-10 本人，用 manifest 形式名） |
| co-honored | Herbert Spencer Gasser | 无向 | 1944 诺贝尔生理学或医学奖共享（官方理由句同一）；师生+共同得主双线 |
| advisor-student | William Osler | 对方 → 导师 | 毕业后约翰·霍普金斯医院随 Osler 实习并从事生理实验室工作 |
| colleague | William Henry Howell | 无向 | 约翰·霍普金斯生理学教授：因犬消化系统论文赏识并招募其为助理教授 |
| colleague | Arthur Hirschfelder | 无向 | 约翰·霍普金斯时期心脏病学合作研究者（房室激动传导） |

**不入库但提示词可叙述**：父母（符腾堡犹太移民、淘金热年代加州相识，无名字记载）；六个兄弟姐妹；Western Electric（公司，示波器来源）；一战休克研究团队（与 Gasser 的合作已由两条边承载）。

## 五、配色方案 【人物专属】

- **气质**：神经电信号的锐利、圣路易斯的学术厚重
- **主色**：`#8C1515`（神经电红——示波器尖峰与心电波形）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeFiber` 神经纤维谱系 — 电红 `#8C1515`
  - `badgeScope` 电生理仪器 — 深蓝 `#16324F`
  - `badgeCardio` 心脏病学 — 深金 `#B8860B`
  - `badgeWashU` 圣路易斯建制 — 灰紫 `#46356B`
- **背景母题**：粗细不一的纤维束与逐级升高的电位尖峰谱。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 单根神经纤维的听诊者 / Joseph Erlanger 1874–1965 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、旧金山出身、伯克利化学学士 1895、
    约翰·霍普金斯 MD 1899（班第二）、威斯康星首任生理学主任 1906、华盛顿大学圣路易斯 1910、诺奖 1944）
03  核心贡献概览 — 纤维功能分化 / 电位速度—直径定律 / 示波器改造 / 心脏病学先声
04  旧金山与移民家庭 (1874–1895) — 符腾堡犹太移民、淘金热父母相识、七子之六
05  伯克利与霍普金斯 (1895–1899) — 化学学士；MD 1899 班第二
06  Osler 门下与霍普金斯岁月 (1899–1906) — 实习+生理实验室；血压计专利；与 Hirschfelder 研究房室传导
07  Howell 的招募与威斯康星 (1906–1910) — 犬消化论文→助理教授→首任生理学系主任
08  迁圣路易斯与 Gasser 来投 (1910) — 更充足经费；昔日威斯康星学生加入实验室
09  一战与休克研究 — His 束钳夹致心传导阻滞的动物模型
10  示波器的改造 (1922) — Western Electric 阴极射线示波器低压化；牛蛙坐骨神经电位放大
11  电位速度—直径定律（核心贡献页）— 两相电位（spike + after-spike）；神经元多样兴奋性；速度∝直径
12  1944 共享诺奖 — 与 Gasser（昔日学生）同台；师生双线的叙事高点
13  荣誉与纪念 — NAS 1922 / 美国哲学会 1927；Joseph Erlanger House 国家历史地标 1976；月球环形山 2009
14  遗产与结尾 — 电生理学的现代格局 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1944 共享结构 | 与 Gasser 共享且**官方理由同句**（"for their discoveries relating to..."）；Gasser 是其昔日学生兼长期合作者——学生边与 co-honored 边**双线并存**，勿合并成一条 |
| 跨批次对手方 | Gasser 属 med-batch-10（另一 agent），yaml 对手方名必须用 manifest 形式 **"Herbert Spencer Gasser"**（注意：库内另有 bare stub "Herbert S. Gasser" #3487，系待合并项，勿使用） |
| 获奖理由表述 | 官方句强调 **single nerve fibres 的高度分化功能**，勿写成泛泛的「神经电传导研究」 |
| Osler 关系强度 | page.md 明载 "interned at Johns Hopkins Hospital under William Osler"——实习导师边成立；Osler 是医学史名家，可点明但勿夸大为博士导师 |
| Howell 的角色 | 招募者（伯乐）而非导师——犬消化论文引起其注意、招为助理教授，故用 colleague 不用 advisor-student |
| 卡片iology 转向之谜 | page.md 明载 "It is uncertain why the pair had such a sudden shift in interest"——写「转向原因不详」，禁编造动因 |
| 1931 合作终止 | Gasser 赴康奈尔，搭档关系结束——1944 获奖时已是终止合作 13 年后，时间线勿混 |
| 心血管起源 | 血压计专利（肱动脉测压）、His 束钳夹致心传导阻滞模型——心脏病学是早期身份，勿说成神经科学家出身 |
| 犹太移民背景 | 父母皆符腾堡犹太移民、加州淘金热相识——史实陈述保持克制 |
| 纪念三件套 | Joseph Erlanger House（1976 国家历史地标）、月球 Erlanger 环形山（2009）、NAS 1922/APS 1927——年份勿混 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| single nerve fibres | 单根神经纤维 | 获奖理由核心词，逐字对应 |
| action potential | 动作电位 | 核心测量对象 |
| fibre diameter | 纤维直径 | 与传导速度成正比 |
| oscilloscope (cathode ray) | （阴极射线）示波器 | Western Electric 仪器改造 |
| spike / after-spike | 主峰/后电位 | 两相电位描述 |
| sciatic nerve (bullfrog) | （牛蛙）坐骨神经 | 1922 年放大实验标本 |
| heart block | 心传导阻滞 | His 束钳夹动物模型 |
| bundle of His | His 束 | 心脏传导组织 |
| sphygmomanometer | 血压计 | 其专利发明 |
| shock (circulatory) | （循环）休克 | 一战研究方向 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Last Hope**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：一战战地休克研究与 His 束实验的沉重底色、以及 65 岁圣路易斯实验室里对单根纤维信号的漫长守望——「最后的希望」的深沉感对应把最微弱的神经电信号从噪声中放大的执念；终曲的释然也贴合 70 岁之年师生同台领奖的高点。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Joseph_Erlanger/LastHope.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
