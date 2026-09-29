# 医学家立传提示词（Thomas Hunt Morgan）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1933 年**得主（独享）。
> 本文件是 Morgan 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Thomas Hunt Morgan（1866-09-25 ~ 1945-12-04，享年 79 岁），美国遗传学家、胚胎学家
- **气质关键词**：**蝇室之主、基因染色体论的实证者、现代遗传学的奠基人** —— 1933 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for his discoveries concerning the role played by the chromosome in heredity"（因其关于染色体在遗传中所起作用的发现）
- **设计母题**：**白眼果蝇（the white-eyed fly）**。1910 年红眼群中那只白眼突变雄蝇——以「果蝇群谱中一只异色之眼」作为突变与连锁分析的视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Thomas_Hunt_Morgan/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Thomas_Hunt_Morgan/`；Makefile 复制后设 `MAIN=Thomas_Hunt_Morgan_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | genetics | 遗传学 | 1933 诺奖核心：基因在染色体上、连锁与交换 | 核心页 |
| 1 | embryology | 胚胎学 | 其本职出身：海蜘蛛胚胎、再生研究 | 早年页 |
| 2 | zoology | 动物学 | 约翰霍普金斯动物学博士（1890） | 早年页 |
| 3 | evolutionary biology | 进化生物学 | 《进化与适应》1903、拒自然选择而转向孟德尔主义 | 转向页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | William Keith Brooks | 师→生（博士导师） | 约翰霍普金斯博士导师（1890 海蜘蛛胚胎学论文） |
| spouse | Lilian Vaughan Morgan | 无向 | 果蝇遗传学家，与夫骨灰同迁 Woods Hole |
| advisor-student | Alfred Sturtevant | 生（Morgan→学生） | 学生，1913 绘制首张基因连锁图 |
| advisor-student | Calvin Bridges | 生（Morgan→学生） | 学生，1915 四人专著合著者 |
| advisor-student | Hermann Joseph Muller | 生（Morgan→学生） | 学生，1915 四人专著合著者，后获 1946 诺贝尔奖 |
| advisor-student | Nettie Maria Stevens | 生（Morgan→学生） | 博士生（infobox 明载）；Y 染色体性别决定发现者 |
| advisor-student | John Howard Northrop | 生（Morgan→学生） | 博士生（infobox 明载），后获 1946 诺贝尔化学奖 |
| advisor-student | Chester Ittner Bliss | 生（Morgan→学生） | 博士生（infobox 明载） |
| advisor-student | Tan Jiazhen | 生（Morgan→学生） | 博士生（infobox 明载），中国遗传学奠基人 |
| advisor-student | Harold Henry Plough | 生（Morgan→学生） | 博士生（infobox 明载） |
| colleague | Edmund Beecher Wilson | 无向 | 挚友，邀其转哥伦比亚大学，染色质先驱 |
| colleague | Jacques Loeb | 无向 | 布林莫尔同事，终生挚友 |
| colleague | Hans Driesch | 无向 | 那不勒斯共事，引其转向实验胚胎学 |
| colleague | Fernandus Payne | 无向 | 合作以理化与辐射诱变果蝇 |
| colleague | Theodosius Dobzhansky | 无向 | 加州理工国际研究员，合成理论旗手 |

**方向约定**：`advisor-student` + `direction: advisor` = 对方是导师；`direction: student` = 对方是学生；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：肯塔基绅士的沉静、蝇室的忙碌与欢欣、实证的锋利
- **主色**：`#4A2A6A`（遗传紫，染色体与蝇室）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：
  - `badgeFly` 果蝇与蝇室 — 果蝇红 `#A33A2E`
  - `badgeChromo` 染色体论 — 遗传紫 `#5C3A8C`
  - `badgeMap` 连锁图谱 — 图谱青 `#1B6B6B`
  - `badgeEmbryo` 胚胎学 — 海洋蓝 `#2E5E7E`
- **背景母题**：米白底上散布果蝇侧影（小椭圆翅身），其中一只以白点标眼，错落成谱系网。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 果蝇室的宗师 / Thomas Hunt Morgan 1866–1945 + 四色 badge + 右上肖像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Lexington、肯塔基/约翰霍普金斯、哥伦比亚/加州理工、荣誉）
03  核心贡献概览 — 基因在染色体上 / 连锁与交换 / 果蝇模型 / 首张遗传图谱
04  肯塔基世家 (1866–1886) — Lexington 名门：叔父 John Hunt Morgan 将军、外高祖 Francis Scott Key
05  约翰霍普金斯 (1886–1890) — Brooks 门下海蜘蛛胚胎学、Woods Hole、1890 博士
06  布林莫尔与实验转向 (1891–1904) — Loeb 挚友、那不勒斯 Driesch、Roux-Driesch 之争、再生研究
07  怀疑者的年代 (1900–1908) — 拒自然选择与孟德尔主义、欲证 De Vries 突变论
08  白眼果蝇 (1910)（核心贡献页）— white 基因、伴性遗传、1911 Science 论文三结论
09  连锁与交换 — Janssens chiasmatypy、交叉频率即图距、Sturtevant 1913 首图
10  蝇室群像 — 哥伦比亚 Schermerhorn Hall、1915《孟德尔遗传机制》四人、果蝇成模式生物
11  加州理工 (1928–1942) — 建生物部（后出七位诺奖）、Dobzhansky、NAS 会长 1927-31
12  1933 诺贝尔奖 — 独享、奖金分予 Bridges/Sturtevant/子女、1934 才出席领奖（多线染色体佐证）
13  家族与身后 — 妻 Lilian（果蝇遗传学家）、1945 卒于动脉破裂、2025-08-30 骨灰迁葬 Woods Hole
14  遗产：果蝇飞进每个实验室 — 摩尔根单位、Tan Jiazhen 传中国遗传学、优生学批评者
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒日 | 1866-09-25 生于 Lexington, Kentucky；1945-12-04 卒于 Pasadena；1945 重度心脏病发作死于动脉破裂（多年十二指肠溃疡病史） |
| 获奖理由 | "for his discoveries concerning the role played by the chromosome in heredity"——**his**（1933 独享） |
| 奖金去向 | 自认发现属团队，把奖金分给 Bridges、Sturtevant 与自己的子女——正文明载，团队叙事亮点 |
| 领奖年份 | 未出席 1933 典礼、1934 年才领奖（果蝇唾腺多线染色体新发现或为原因）——勿写错 |
| 怀疑者转向 | 曾长期拒绝孟德尔定律与自然选择（1903《进化与适应》），转向孟德尔主义后才成就诺奖——叙事弧线勿抹掉前半段 |
| white 基因 | 1910 白眼雄蝇、基因名 white 为 Morgan 所命名；1911 Science 论文三结论（伴性/性染色体/其他基因在特定染色体上） |
| 交叉发现归属 | chiasmatypy 现象 1909 由比利时人 Frans Alfons Janssens 描述——Morgan 是借用者与发展者 |
| morgan 单位 | 命名系 J. B. S. Haldane 建议——勿写成 Morgan 自创 |
| Stevens 定位 | Nettie Stevens 的 Y 染色体性别决定工作 Morgan 曾先 dismiss（正文有载）——学生边与学术交锋并存，表述克制 |
| 家庭 | 妻 Lilian Vaughan Morgan 本身是果蝇遗传学家；2025-08-30 夫妇骨灰由 Altadena 迁葬 Woods Hole——新近事实可写 |
| 优生学 | 1915 年后成为优生学运动的坚定批评者——正文明载，客观一句呈现 |
| Ume Tsuda | 1894 与津田梅子合著论文系日本女性首篇英文科学论文——趣味注脚 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| chromosome theory of inheritance | 染色体遗传理论 | Sutton-Boveri 提出、Morgan 学派实证发展 |
| genetic linkage | 基因连锁 | 同染色体基因不独立分配 |
| crossing over | 交叉互换 | 借 Janssens chiasmatypy |
| linkage map | 连锁图 | Sturtevant 1913 首图 |
| white (mutation) | white 基因（白眼突变） | 1910 发现 |
| Drosophila melanogaster | 黑腹果蝇 | 模式生物 |
| polytene chromosome | 多线染色体 | 1933 发现推动其领奖 |
| Entwicklungsmechanik | 发育力学 | 实验胚胎学学派 |
| morgan / centimorgan | 摩尔根 / 厘摩 | 图距单位，Haldane 建议命名 |
| Fly Room | 蝇室 | 哥伦比亚 Schermerhorn Hall |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions（manifest 预分配）
- **风格**：时间感 / 纪录片 / 沉静推进
- **匹配理由**：从怀疑孟德尔的胚胎学家到染色体论的加冕——Morgan 的一生是横跨 40 年的观念长途（第二次使用该曲，首用 Laveran）；The Flow of Time 的时间叙事匹配「蝇室 24 年、每夏迁往 Woods Hole」的岁月节律，也匹配 2025 年骨灰归葬 Woods Hole 的闭环。
- **本地路径**：`music_audio/` 下 The Flow of Time 曲目 → 复制为 `presentations/20th_century/Thomas_Hunt_Morgan/The_Flow_of_Time.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。
