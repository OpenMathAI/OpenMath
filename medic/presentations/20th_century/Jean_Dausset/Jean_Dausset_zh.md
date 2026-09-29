# 医学家立传提示词（Jean Dausset）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1980 年得主（让·多塞，人类白细胞抗原 HLA 系统的发现者）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Jean-Baptiste-Gabriel-Joachim Dausset（1916-10-19 生于图卢兹 ~ 2009-06-06 卒于西班牙马略卡岛帕尔马，享年 92 岁）
- **气质关键词**：**HLA 系统的发现者、人类多态性研究中心 CEPH 的缔造者、从战地输血到人类基因组计划的免疫血液学家** —— 1980 获奖理由（与 Baruj Benacerraf、George Davis Snell 三人共享）：
  > "for their discoveries concerning genetically determined structures on the cell surface that regulate immunological reactions"（因发现细胞表面调控免疫反应的遗传决定结构）
- **设计母题**：**三个捐血者姓名的缩写**。1958 年发现的 MAC 抗体之名来自三位志愿捐血者姓名首字母——"普通人的血液写进了科学命名"。视觉隐喻：三滴血汇成一个抗原标记，延伸为 HLA 基因群图谱。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Jean_Dausset/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/Jean_Dausset/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/Jean_Dausset/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Jean_Dausset_zh`、`VIDEO_NAME=Jean_Dausset_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/Jean_Dausset/images.txt`（2005 照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Jean_Dausset.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | immunology | 免疫学 | HLA 系统发现，1980 诺奖核心 | 核心页 |
| 1 | major histocompatibility complex | 主要组织相容性复合体 | Hu-1→HLA 的命名与家族研究 | 核心页 |
| 2 | immunohematology | 免疫血液学 | MAC 抗体、白细胞凝集、溶血性贫血 | 研究页 |
| 3 | human genetics | 人类遗传学 | CEPH 与 HGDP-CEPH 多样性面板 | 晚年页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Baruj Benacerraf | 无向 | 1980 诺贝尔生理学或医学奖三人共享（细胞表面遗传决定结构调控免疫反应的发现） |
| co-honored | George D. Snell | 无向 | 1980 诺贝尔生理学或医学奖三人共享（细胞表面遗传决定结构调控免疫反应的发现） |
| collaborator | Marcel Bessis | 无向 | 交换输血技术合作；共同发现首个抗原呈递白细胞 |
| collaborator | Felix Rapaport | 无向 | 1963 皮肤移植实验共同发现 HLA 系统（组织相容性决定成败） |
| collaborator | Paul Ivany | 无向 | 布拉格合作，白细胞凝集与淋巴细胞毒性技术发现 Hu-1 抗原 |
| collaborator | Luigi Luca Cavalli-Sforza | 无向 | 合作建立 HGDP-CEPH 世界人群 DNA 多样性面板 |
| colleague | Robert Debré | 无向 | 法国医疗改革共同推动者（1958 Debré 改革：医院联合大学） |
| spouse | Rose Mayoral | 无向 | 1963 结婚，育 Henri 与 Irène |

> relations=8 为诚实值，Review 勿误判虚增。
> 不入库：Gilbert Malinvaud 与 Jacques/Monique Colombani（1952-57 众多合作者，page.md 仅列举）；Georges Marchal（Broussais 免疫血液学实验室主任，雇主）；Cavalli-Sforza 之外 CEPH 机构成员；父母兄姐（背景叙事）。
> 库内当时无上述对手方记录，均由本 yaml 新建 stub；Benacerraf/Snell 由本批各自 yaml 幂等覆盖。**Cavalli-Sforza 全名按 page.md 链接形式 Luigi Luca Cavalli-Sforza。**

## 五、配色方案 【人物专属】

- **气质**：图卢兹的暖石色 + 战地输血的暗红 + CEPH 数据库的秩序蓝
- **主色**：免疫血液红棕 `#7A3B2E`（输血与红细胞的底色）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` HLA 系统 — 免疫血液红棕 `#7A3B2E`
  - `badgeB` MAC 抗体 — 琥珀 `#A0722D`
  - `badgeC` 医疗改革 — 灰蓝 `#4A5A6A`
  - `badgeD` CEPH 与基因组 — 深青 `#0E7C7B`
- **背景母题**：三滴血滴形汇聚成一个抗原圆点，向外辐射 HLA 基因网格线。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — HLA 系统的发现者 / Jean Dausset 1916–2009 + 四色 badge + 右上头像 + 国籍行 France
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生 Toulouse、教育 Lycée Michelet/
    巴黎大学医学院、自由法国部队北非、任职 Saint-Louis 医院/INSERM/CEPH、
    荣誉 Nobel 1980/Wolf 1978/Koch 奖/Gairdner、核心领域）
03  核心贡献概览 — MAC 抗体 / Hu-1→HLA / 移植免疫 / CEPH 与人类基因组
04  图卢兹与战争 (1916–1944) — 幼年 Biarritz（父为 Bayonne 医院主任医生，印象深刻）、
    母家庭教育、19 岁成巴黎医院 extern 时父母双亡、
    入伍北意大利一年、1940 回巴黎考过实习、加入自由法国部队北非
    （摩洛哥→突尼斯）做救护——战地输血初识血液学
05  战后改革者 (1944–1952) — Saint-Antoine 医院地区输血中心、
    激进医生团体推动法国医疗系统改革、任国民教育部内阁顾问、
    与 Robert Debré 共同推动 1958 年 12 月 Debré 改革（医院首次联合大学、医生全职化）
06  波士顿与 Bessis (1948–1952) — 波士顿儿童医院血液实验室实习约四年、
    1950 首篇论文（胰蛋白酶化红细胞检测不完全抗体）、
    与 Bessis 合作交换输血技术、共同发现首个抗原呈递白细胞
07  1958：MAC 抗体 — 1954 首见抗白细胞凝集物质、1958 鉴定白细胞特异同种抗体、
    MAC 缩写来自三位志愿捐血者姓名首字母——诺奖级发现的起点
08  Hu-1 的提出 (1960–1965) — 器官移植技术与受体耐受机制研究、
    1962 白细胞凝集与皮片耐受相关性、1965 与 Ivany（布拉格）发现 Hu-1 与 H-2 抗原、
    提出"所有已知白细胞抗原同属一个复合体"假说并命名 Hu-1
09  HLA 的确立 (1963–1968) — 1963 任 Saint-Louis 医院免疫学主任、
    与 Rapaport 皮肤移植实验证明组织相容性决定移植成败、
    1966-67 家族研究确认单一系统、1968 复合体更名 HLA
10  1980 诺贝尔奖 — 三人共享官方理由逐字引用、1978 Wolf 医学奖为前奏、
    1980-02 获奖前的犹疑（赴魁北克讲学 vs 留巴黎——page.md 轶事可叙事）
11  CEPH 与人类基因组 (1984–) — 用诺奖奖金+法国电视资助创立 CEPH（人类多态性研究中心）、
    61 个大家族 DNA 贡献人类基因组作图、与 Cavalli-Sforza 合作
    HGDP-CEPH 世界人群多样性面板、1993 更名 Foundation Jean Dausset-CEPH
12  荣誉序列 — Wolf 1978、Koch 奖、Gairdner、Landsteiner 奖、CNRS 银章、
    荣誉军团大军官勋章、法兰西科学院院士、法兰西学院教授、
    HUGO 创始理事会副主席、美国 NAS 外籍院士
13  个人生活与身后 — 妻 Rose Mayoral（1963 结婚）、子女 Henri 与 Irène、
    2003 年 87 岁退休并任 CEPH 主席、2009-06-06 卒于马略卡（92 岁）
14  遗产 — 器官移植配型的科学基础、France Transplant 与 France Greffe de Moelle、
    从免疫血液学到基因组资源库的一生、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for their discoveries concerning genetically determined structures on the cell surface that regulate immunological reactions"（三人共享、their） |
| 全名 | Jean-Baptiste-Gabriel-Joachim Dausset——正文通称 Jean Dausset；身份页可写全名 |
| MAC 抗体命名 | MAC = 三位志愿捐血者姓名首字母——命名由来是本篇最人本化的细节，务必保留 |
| Hu-1→HLA 演进 | 1965 提出 Hu-1 复合体假说→1966-67 家族研究确认单一系统→1968 更名 HLA——三段演进勿压缩 |
| Ivany 合作 | 与 Paul Ivany（布拉格）用白细胞凝集与淋巴细胞毒性技术发现 Hu-1 与 H-2 抗原——collaborator 边 |
| Debré 改革 | 1958 年 12 月 11/30 日 Debré 改革（医院联合大学、医生全职化）——Dausset 系推动团体成员、Debré 以 colleague 入库；与儿科医生 Robert Debré 同名人物的语境（此为医政改革者），注意不要与物理学家等混淆 |
| 双重角色 | 战后既是研究者又是医疗改革活动家（激进医生团体→教育部内阁顾问）——两条叙事线并存 |
| CEPH 资金 | 诺奖奖金+法国电视资助创立（page.md 口径）——细节勿改 |
| 诺奖前的犹疑 | 1980-02 赴魁北克讲学与留法的两难权衡轶事——page.md 明载可叙事 |
| 退休年份 | 2003 年 87 岁退休并任 CEPH 主席——"退休后任主席"的表述照 page.md |
| 不入库提醒 | Malinvaud/Colombani 夫妇等多位 1952-57 合作者在 page.md 仅列举——防噪声不入库 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| HLA (human leukocyte antigen) | 人类白细胞抗原 | 1968 由 Hu-1 更名 |
| Hu-1 | Hu-1 复合体 | 其提出的单复合体假说 |
| MAC antibody | MAC 抗体 | 三位捐血者姓名缩写 |
| leuco-agglutination | 白细胞凝集 | 核心实验技术 |
| exchange transfusion | 交换输血 | 与 Bessis 合作的技术 |
| CEPH | 人类多态性研究中心 | 1984 创立 |
| HGDP-CEPH diversity panel | HGDP-CEPH 多样性面板 | 世界人群 DNA 资源 |
| Debré reform | Debré 改革 | 1958 法国医教改革 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**New Lands**（manifest 预分配）
- **风格**：史诗 / 开阔 / 新大陆
- **匹配理由**：从战地输血到 HLA 基因群、再到面向全人类基因组计划的国家资源库——New Lands 的开阔史诗感匹配"每一次转身都打开一片新大陆"的一生：免疫血液学的新大陆、移植医学的新大陆、人类遗传学的新大陆。
- **本地路径**：`music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav` → 复制为 `presentations/20th_century/Jean_Dausset/New-Lands.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；MAC 命名由来与 Hu-1→HLA 演进务必精确。**
