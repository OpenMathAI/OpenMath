# 医学家立传提示词（Elizabeth Blackburn）

> OpenMedic 项目、21 世纪诺贝尔生理学或医学奖 2009 年得主（伊丽莎白·布莱克本，端粒酶共同发现者、首位澳洲女性诺奖得主）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Elizabeth Helen Blackburn（1948-11-26 生于塔斯马尼亚霍巴特，在世）
- **气质关键词**：**端粒与端粒酶的发现者、染色体"保护帽"的解密者、首位澳大利亚女性诺贝尔奖得主** —— 2009 获奖理由（与 Carol W. Greider、Jack W. Szostak 三人共享）：
  > "for the discovery of how chromosomes are protected by telomeres and the enzyme telomerase"（因发现染色体如何受端粒和端粒酶保护）
- **设计母题**：**染色体的鞋带头**。端粒是染色体末端的"塑料头"——每分裂一次就磨损一点，端粒酶则负责修补。视觉隐喻：一条渐次磨损又不断被补全的双螺旋线，配以四膜虫显微意象。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Elizabeth_Blackburn/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/21th_century/Elizabeth_Blackburn/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/21th_century/Elizabeth_Blackburn/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Elizabeth_Blackburn_zh`、`VIDEO_NAME=Elizabeth_Blackburn_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/21th_century/Elizabeth_Blackburn/images.txt`；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。插图可用 2016 斯德哥尔摩照。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Elizabeth_Blackburn.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | telomere biology | 端粒生物学 | 端粒酶发现，2009 诺奖核心 | 核心页 |
| 1 | molecular biology | 分子生物学 | infobox Fields；Sanger 门下测序方法起步 | 早年页 |
| 2 | genetics | 遗传学 | 端粒重复序列的进化保守性 | 研究页 |
| 3 | medical ethics | 医学伦理 | 总统生物伦理委员会经历与干细胞立场 | 伦理页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Frederick Sanger | 导师 | 剑桥 Darwin College 博士导师，MRC 分子生物学实验室（1975 PhD，ΦX174 测序） |
| advisor-student | Joseph G. Gall | 导师 | 博士后（Yale，Gall 实验室），四膜虫端粒研究起点 |
| advisor-student | Carol W. Greider | 学生 | 博士生，1984-85 共同发现端粒酶（1985 Cell 论文） |
| co-honored | Carol W. Greider | 无向 | 2009 诺贝尔生理学或医学奖三人共享（端粒与端粒酶保护染色体） |
| co-honored | Jack W. Szostak | 无向 | 2009 诺贝尔生理学或医学奖三人共享（端粒与端粒酶保护染色体） |
| colleague | Jack W. Szostak | 无向 | 1982 合作证明四膜虫端粒重复序列保护酵母不稳定质粒 |
| spouse | John Sedat | 无向 | 剑桥 MRC 相识，Yale 博后期间成婚，育一子（1986） |

> 在世者，page.md 未载其他师生/同事关系，relations=7 为诚实值（Review 勿误判缺漏）。
> 不入库：Elissa S. Epel（《The Telomere Effect》合著者，科普合作非科研师生）；Irwin M. Jacobs（Salk 主席引用语）；Bush 当局官员（伦理委员会事件为机构冲突）；父母（家庭医生，未具名科研合作）。
> 库内既有 Frederick Sanger（#1122, Q151564）与 Blackburn 本人 stub（#1130，Sanger 侧预建，本 yaml UPD 回填 QID）；Carol W. Greider / Jack W. Szostak / Joseph G. Gall / John Sedat 由本 yaml 新建 stub（Greider/Szostak 用 manifest 全名，其本人 yaml 将回填）。

## 五、配色方案 【人物专属】

- **气质**：塔斯马尼亚的清冽 + 实验室的克制 + 生命绵延的绿意
- **主色**：端粒青绿 `#0F6B5C`（染色体末梢的保护色，亦呼应"修补与延续"）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 端粒酶发现 — 端粒青绿 `#0F6B5C`
  - `badgeB` 四膜虫与酵母实验 — 琥珀 `#A0722D`
  - `badgeC` 细胞衰老与癌症 — 暗红 `#8C2F1B`
  - `badgeD` 伦理与政策 — 灰蓝 `#4A5A6A`
- **背景母题**：一条贯穿版面的双螺旋细线，末端以渐淡圆点表示"磨损-修补"循环。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 端粒酶的共同发现者 / Elizabeth Blackburn 1948– + 四色 badge + 右上头像 + 国籍行 Australia/USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生 Hobart、教育 Melbourne/Cambridge PhD 1975、
    导师 Sanger、任职 Berkeley/UCSF/Salk、荣誉 Nobel 2009/Lasker 2006/Royal Medal 2015、核心领域）
03  核心贡献概览 — 端粒重复序列 / 端粒酶的发现 / 端粒-衰老-癌症 / 科研伦理
04  塔斯马尼亚少女 (1948–1970) — Hobart 出生、七孩之二、双亲为家庭医生、Launceston 女校、
    Melbourne 大学 BSc 1970/MSc 1972（生物化学）
05  剑桥与 Sanger (1972–1975) — Darwin College、MRC 分子生物学实验室、RNA 介导的 DNA 测序方法、
    ΦX174 噬菌体、1975 PhD；剑桥结识 John Sedat
06  Yale 博后：四膜虫的馈赠 (1975–1978) — 因爱情选择 Gall 实验室（page.md 引语）、
    四膜虫 rDNA 末端 TTAGGG 串联重复与回文结构
07  1982：端粒保护染色体的证明 — 与 Szostak 合作：四膜虫端粒序列保护酵母不稳定质粒、
    端粒重复序列的进化保守性
08  1984-85：端粒酶的发现 — 预言"转移酶样酶"、博士生 Greider 加入、1984-12-25 关键凝胶、
    1985-12 Cell 论文、酶含 RNA 模板 + 蛋白组分、命名 telomerase
09  Berkeley 与 UCSF 岁月 — 1978 入 Berkeley、1990 转 UCSF、1993-99 系主任、
    Herzstein 讲席教授、2015 荣休
10  端粒与衰老、癌症 — 端粒缩短即细胞衰老之钟、癌细胞借端粒酶不死、
    胰腺/骨/前列腺/膀胱/肺/肾/头颈癌关联、Telomere Health 公司创立与退出
11  2009 诺贝尔奖 — 三人共享、首位澳大利亚女性诺奖得主、端粒研究成为分子生物学革命催化剂
12  科研伦理的风波 — 2002 入总统生物伦理委员会、支持胚胎干细胞研究、
    2004-02-27 被白宫解职、170 位科学家公开信、《联邦咨询委员会法》争议——客观呈现各方表述
13  压力与端粒 — 正念冥想研究、慢性压力加速细胞衰老、亲密伴侣暴力与端粒缩短、
    《The Telomere Effect》(2017, 与 Epel 合著) 与其对保健品炒作的警示
14  遗产 — Salk Institute 主席（2016-2017）、Time 100（2007）、 Companion of the Order of Australia、
    从端粒酶到衰老医学的百年视野、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for the discovery of how chromosomes are protected by telomeres and the enzyme telomerase"；三人共享，勿写成"两人" |
| 发现年份双说 | intro 作 1984 co-discovered（Greider infobox 1984-12-25 得关键结果），正文作 1985 discovery（1985-12 Cell 论文）——表述用 "1984-85 发现、1985 年发表" 自洽处理 |
| 国籍裁定 ★ | 总表/manifest 仅 United States；Nobel 官方 citation json 作 "Australia United States"；page.md citizenship "Australian and American"——yaml 双列（Australia rank0 + United States rank1，因"首位澳洲女性诺奖得主"为其核心身份标签），幻灯片国籍行写 Australia & USA，供主控统一口径 |
| 伦理事件呈现 | 被 Bush 当局解职系 page.md 明载：她自认因干细胞立场被解职、170 科学家联署、有学者援引 FACA——须客观转述各方说法，"她认为/科学家认为" vs 白宫口径并列，不渲染 |
| 引语可用 | 2016 访谈 "Ah! This could be very big. This looks just right."（page.md 有英文原文，可引原文+译文）；《科学被政治操纵》信件引语同理 |
| 导师链条 | 博士导师 Frederick Sanger（两届诺奖得主）；博士后在 Joseph G. Gall 实验室（Yale）——两条都入库，note 区分博士/博后 |
| Greider 角色 | Greider 是其博士生（infobox Doctoral students 明载）——师生 + co-honored 双边 |
| Telomere Health | co-founded 后 severed ties——商业关系须带"后断绝"注记，勿写成"在任创始人" |
| Salk 主席任期 | 2015 宣布就任、 elected 口径 2016–2017、2017 宣布次年起退休——三个年份勿混 |
| 在世者关系 | relations=7 为诚实值；page.md 未载子女姓名（仅"一子，1986 年生"）等，勿杜撰 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| telomere | 端粒 | 染色体末端的保护结构，勿与着丝粒混淆 |
| telomerase | 端粒酶 | 含 RNA 模板 + 蛋白组分的逆转录酶 |
| Tetrahymena thermophila | 嗜热四膜虫 | 大量端粒的模型原生动物 |
| tandem repeat | 串联重复 | TTAGGG 六核苷酸重复 |
| end-replication problem | 末端复制问题 | 端粒酶解决的经典难题 |
| senescence | 细胞衰老 | 端粒缩短的后果 |
| reverse transcriptase activity | 逆转录酶活性 | 端粒酶的作用机制 |
| President's Council on Bioethics | 总统生物伦理委员会 | 2002 入、2004 被解职 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Pathfinder**（manifest 预分配）
- **风格**：开拓 / 前行 / 沉稳史诗
- **匹配理由**：从霍巴特到剑桥 Sanger 门下、再到发现"细胞不朽之钥"——Pathfinder 的行进感匹配"首位澳洲女性诺奖得主"的拓荒叙事；修补端粒、延续生命亦是"为后来者开路"的隐喻。
- **本地路径**：`music_audio/inspiring-electronic/23-GiwYLGgJw7w-Ghostwriter Music - Pathfinder (Composed by Daniel Beijbom - Recorded in Budapest).wav` → 复制为 `presentations/21th_century/Elizabeth_Blackburn/Pathfinder.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；伦理风波务必客观、忠实 page.md 各方表述。**
