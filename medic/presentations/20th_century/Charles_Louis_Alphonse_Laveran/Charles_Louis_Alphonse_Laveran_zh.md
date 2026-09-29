# 医学家立传提示词（Charles Louis Alphonse Laveran）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1907 年**得主（独享）。
> 本文件是 Laveran 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Charles Louis Alphonse Laveran（1845-06-18 ~ 1922-05-18，享年 76 岁），法国军医、寄生虫学家
- **气质关键词**：**疟原虫的发现者、原生动物致病说的开创者、军旅寄生虫学家** —— 1907 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "in recognition of his work on the role played by protozoa in causing diseases"（因其关于原生动物在致病中所起作用的研究）
- **设计母题**：**血涂片上的新月（crescent in the blood smear）**。1880-10-20 Laveran 在显微镜下看到疟疾患者红细胞间透明的新月体与丝状游动体——以「显微镜视野中的新月与鞭丝」作为全篇视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Charles_Louis_Alphonse_Laveran/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Charles_Louis_Alphonse_Laveran/`；Makefile 复制后设 `MAIN=Charles_Louis_Alphonse_Laveran_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | parasitology | 寄生虫学 | 1907 诺奖核心：原生动物致病 | 核心页 |
| 1 | tropical medicine | 热带医学 | 疟疾/锥虫病/利什曼病，巴斯德研究所热带医学实验室 | 热带病页 |
| 2 | malaria | 疟疾 | 1880 发现疟原虫、Oscillaria malariae 命名 | 疟疾页 |
| 3 | microbiology | 微生物学 | 600 余篇科学通讯、锥虫专著 1904 | 著作页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Émile Küss | 师→生（博士导师） | 斯特拉斯堡博士导师（frontmatter 有载；1867 神经再生论文） |
| spouse | Sophie Marie Pidancet | 无向 | 1885 结婚，无子女 |
| colleague | Camillo Golgi | 无向 | Golgi 以改良显微镜与染色证实其疟原虫发现 |
| colleague | Félix Mesnil | 无向 | 巴斯德研究所同事，合作命名利什曼原虫与锥虫研究 |
| colleague | Charles Donovan | 无向 | 1903 接其马德拉斯标本，合作确认内脏利什曼病病原 |

**方向约定**：`advisor-student` + `direction: advisor` = 对方是导师；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：军旅的克制、显微镜前的耐心、北非的干燥阳光
- **主色**：`#1B4D6B`（军蓝青，军医制服与热带医学）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：
  - `badgeMalaria` 疟疾 — 疟原虫赭红 `#8C3A26`
  - `badgeTrypano` 锥虫病 — 深紫 `#4A3560`
  - `badgeLeish` 利什曼病 — 沙金 `#B08A3E`
  - `badgeMilitary` 军旅生涯 — 军灰蓝 `#5A6B7A`
- **背景母题**：显微镜圆形视野内散布红细胞圆盘，其中一枚带新月形原虫剪影，重复错落。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 看见疟疾之因 / Charles Louis Alphonse Laveran 1845–1922 + 四色 badge + 右上肖像 + 国籍行（France）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、巴黎、斯特拉斯堡、军旅履历、巴斯德研究所、荣誉）
03  核心贡献概览 — 疟原虫 / 锥虫病 / 利什曼病 / 热带医学建制
04  军医之家 (1845–1867) — 父亲 Louis Théodore 任 Val-de-Grâce 军医教授、梅斯/阿尔及尔童年、1867 医学博士
05  普法战争与军旅 (1870–1878) — Gravelotte 与 Saint-Privat、梅茨被围、战俘→里尔医院、巴黎公社期驻军
06  瓦尔-德格拉斯教席 (1874–1878) — 29 岁任军事疾病与流行病学讲席（父亲曾任）
07  君士坦丁的显微镜之夜 (1880)（核心贡献页）— 10-20 观察新月体与丝状体、12-24 报告、1881 论文与 The Lancet
08  从怀疑到确认 — Klebs/Tommasi-Crudeli 杆菌说的阻力、Oscillaria malariae 命名、1954 定名 P. falciparum、Golgi 确证
09  首次证明原生动物致病 — 疟原虫发现是「任何疾病的原生动物病因」首例，验证病菌学说
10  蚊媒疟疾说的支持者 — Manson 1894 理论、Ross 1898 实证、1901 科西嘉报告、1902 科西嘉抗疟联盟名誉主席
11  利什曼病与锥虫病 — Biskra 结节、1903 与 Mesnil 命名 Piroplasma donovanii、1904 锥虫专著 30 余新种
12  1907 诺贝尔奖 — 获奖理由、捐出一半奖金建巴斯德研究所热带医学实验室
13  学术建制与荣誉 — 1893 法国科学院、1908 创立异国病理学会（任主席 12 年）、1912 荣誉军团勋章司令、1915 荣誉所长
14  遗产：LSHTM 浮雕上的名字 — 1926 伦敦卫生与热带医学院 23 人浮雕、1954 阿尔及利亚纪念邮票
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒日 | 1845-06-18 生于巴黎 Boulevard Saint-Michel，1922-05-18 卒于巴黎；葬 Montparnasse 公墓 |
| 获奖理由 | "in recognition of his work on the role played by protozoa in causing diseases"——单数 **his**（1907 独享），勿写成共享 |
| 1880 观察日期 | 1880-10-20 首见原虫；12-24 向巴黎医院医学会报告；勿把发表年份 1881 当发现年 |
| 命名曲折 | 他命名 Oscillaria malariae；1954 国际动物命名委员会定名 P. falciparum——两名勿混用 |
| Golgi 的角色 | Laveran 发现 → 学界怀疑 → **Golgi 用更好显微镜证实**；勿颠倒功劳顺序 |
| 无子女 | 与 Sophie Marie Pidancet 1885 结婚、无子女（正文明载） |
| 博士导师 | Émile Küss 仅 frontmatter 有载（正文只写斯特拉斯堡 1867 论文《神经再生实验研究》）；入库注明来源 |
| Virchow 的误判 | Virchow 1849 已见疟色素细胞但误判为脾内皮/白细胞——背景铺垫勿写成 Virchow 发现疟原虫 |
| 军衔细节 | 退役时为第一类首席军医官（Principal Medical Officer of the First Class）；1896 入巴斯德研究所为荣誉服务部主任 |
| 独身研究者 | 正文明载 "solitary but dedicated researcher"、600 余篇通讯、无直接引语之外的语录勿造 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Plasmodium falciparum | 恶性疟原虫 | 1954 定名；原名 Oscillaria malariae |
| protozoa | 原生动物 | 诺奖理由核心词 |
| exflagellation | 雄配子出丝 | 丝状游动体的本质 |
| gametocyte | 配子体 | 新月体/卵圆体的本质 |
| trophozoite | 滋养体 | 小球体阶段 |
| haemozoin | 疟色素 | 感染红细胞的色素标志 |
| trypanosomiasis | 锥虫病 | 非洲昏睡病病原 Trypanosoma |
| visceral leishmaniasis | 内脏利什曼病 | 黑热病；Leishmania donovani |
| mosquito-malaria theory | 蚊媒疟疾理论 | Manson 提出、Ross 实证、Laveran 支持 |
| miasma theory | 瘴气学说 | 被其发现推翻的旧说 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions（manifest 预分配）
- **风格**：时间感 / 纪录片 / 沉静推进
- **匹配理由**：从普法战争战场到君士坦丁军医院的深夜显微镜——40 余年军旅与科研的时间长河；The Flow of Time 的时间叙事匹配「1880 年 10 月 20 日那一夜」在漫长职业生涯中的分量，也匹配热带医学建制百年传承的余韵。
- **本地路径**：`music_audio/` 下 The Flow of Time 曲目 → 复制为 `presentations/20th_century/Charles_Louis_Alphonse_Laveran/The_Flow_of_Time.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。
