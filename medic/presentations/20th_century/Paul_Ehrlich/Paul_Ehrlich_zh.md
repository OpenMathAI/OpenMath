# 医学家立传提示词（Paul Ehrlich）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1908 年**得主（与 Élie Metchnikoff 共享）。
> 本文件是 Ehrlich 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Paul Ehrlich（1854-03-14 ~ 1915-08-20，享年 61 岁），德国医师、科学家，"免疫学之父"
- **气质关键词**：**魔弹的构想者、化疗之父、侧链学说奠基人、首个特效抗菌药的缔造者** —— 1908 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "in recognition of their work on immunity"（因其对免疫的研究）
- **设计母题**：**魔弹（magic bullet / Zauberkugel）**。一颗子弹只命中病原而不伤宿主——以「靶心与飞行轨迹」作为化疗选择性毒力的视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Paul_Ehrlich/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Paul_Ehrlich/`；Makefile 复制后设 `MAIN=Paul_Ehrlich_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | immunology | 免疫学 | 1908 诺奖核心：侧链学说、血清效价 | 核心页 |
| 1 | chemotherapy | 化学治疗 | 概念命名者；Salvarsan 606 号化合物 | 化疗页 |
| 2 | hematology | 血液学 | 白细胞分类、肥大细胞、红细胞前体 | 染色页 |
| 3 | bacteriology | 细菌学 | 革兰染色改良、结核菌染色改进 | 染色页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Julius Cohnheim | 师→生（博士导师） | 莱比锡大学博士导师（1878 组织染色论文） |
| influence | Karl Weigert | 无向 | 表兄，首个以苯胺染料染细菌者，引其走上染色研究 |
| colleague | Robert Koch | 无向 | 1882 结缘，1891 邀入传染病研究所，结为挚友 |
| colleague | Emil von Behring | 无向 | 1894 合作白喉血清（Behring-Ehrlich 制剂） |
| controversy | Emil von Behring | 无向 | 利润分成缩至 8% 结怨，Behring 于文化部作梗，1900 后拒绝合作 |
| spouse | Hedwig Pinkus | 无向 | 1883 结婚，育二女 Stephanie 与 Marianne |
| advisor-student | Hans Schlossberger | 生（Ehrlich→学生） | 知名学生（infobox 明载） |
| advisor-student | Ernest Witebsky | 生（Ehrlich→学生） | 学生，后证明自身免疫可致人类疾病 |
| colleague | Sahachiro Hata | 无向 | 助手，1909 共同发现 606 号化合物 Salvarsan 治梅毒 |
| colleague | Julius Morgenroth | 无向 | 法兰克福研究所最重要同事 |
| co-honored | Élie Metchnikoff | 无向 | 1908 诺贝尔生理学或医学奖共享（免疫研究） |

**方向约定**：`advisor-student` + `direction: advisor` = 对方是导师；`direction: student` = 对方是学生；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：化学家的精确、德意志的严谨、染料的斑斓
- **主色**：`#7A1E28`（魔弹绛红，染料与靶心）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：
  - `bulletStain` 染色化学 — 亚甲蓝 `#2B5D8C`
  - `bulletImmune` 侧链学说 — 免疫青 `#1E7A6B`
  - `bulletSalv` Salvarsan — 砷紫 `#5C3A6E`
  - `bulletFrankfurt` 法兰克福岁月 — 砖红 `#8C4A2B`
- **背景母题**：深红底上稀疏同心靶环（细线圆环 + 命中点亮点），呼应 magic bullet 选择性命中。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 魔弹之父 / Paul Ehrlich 1854–1915 + 四色 badge + 右上肖像 + 国籍行（Germany）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Strehlen、布雷斯劳/斯特拉斯堡/莱比锡、法兰克福、荣誉）
03  核心贡献概览 — 血液染色 / 侧链学说 / 血清标准化 / Salvarsan
04  染色少年 (1854–1878) — 表兄 Weigert 的切片机、Breslau 结识 Neisser、1878 莱比锡博士（组织染色论文）
05  Charité 与肥大细胞 (1878–1888) — Frerichs 之下、肥大细胞命名（Mast=催肥饲料）、白细胞分类、Ehrlich 试剂
06  活体染色与结核染色改良 (1885–1890) — 氧需求专著、亚甲蓝染神经与疟原虫、Koch 结核演讲次日改进染色法
07  与 Koch 的友谊 (1882–1891) — 「科学生涯最伟大经历」、结核素风波中力挺、1891 邀入传染病研究所
08  白喉血清与 Behring 恩怨 — 1894 临床成功、Hoechst 上市、分成被压至 8%、Behring 在文化部作梗
09  血清效价标准化 (1895–1899) — 毒素会变质、以 Behring 血清粉为标准、豚鼠四日死亡判据、德国质控法走向世界
10  侧链学说（核心贡献页）— 侧链=受体、免疫即再生训练、补体概念、为免疫学奠基理论框架
11  1908 诺贝尔奖 — 与 Metchnikoff 共享、细胞派与体液派同台、此前 Metchnikoff 曾尖锐攻击 Ehrlich
12  Georg-Speyer 屋与 606 — 1906 出任所长、筛选化学合成物、1909 与 Hata 发现 Salvarsan 治梅毒、1910 上市
13  Salvarsan 战争 — 道德恐慌、反犹指控、Uhlenhuth 优先权之争、1914 诽谤罪定谳但抑郁缠身
14  遗产与身后 — 免疫学之父、Paul-Ehrlich-Institut（1947 更名）、200 马克钞票、Ehrlichia 属、1940 电影《Dr. Ehrlich's Magic Bullet》
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒日 | 1854-03-14 生于普鲁士西里西亚 Strehlen（今波兰 Strzelin），1915-08-20 卒于 Bad Homburg；1915-08-17 心脏病发作 |
| 获奖理由 | "in recognition of their work on immunity"——**their**（与 Metchnikoff 共享）；Ehrlich 侧重点是体液免疫/侧链学说 |
| 博士导师裁定 | frontmatter doctoral_advisor 列 Karl Weigert 与 Robert Koch，但正文均非导师——**以正文为准**：博士导师是 **Julius Cohnheim**（随其转莱比锡）；Weigert 是表兄/启蒙者（influence），Koch 是挚友与东家（colleague），均非师承 |
| horror autotoxicus | Ehrlich 提出机体有防止自免攻击的机制（1906 原话正文明载，可引）；学生 Witebsky 后证明自免可致病——师徒观点演进可写 |
| 结核素风波 | Ehrlich 在 tuberculin scandal 中力挺 Koch、强调其诊断价值——事实陈述，勿写成 Ehrlich 认可结核素疗效 |
| 白喉血清功劳链 | 血清疗法原理由 Behring 与北里柴三郎建立；Ehrlich 自认首个做出可用人血清者——三层功劳勿混 |
| 8% 分成 | 合同数次被改、最终被迫接受 8% 利润分成——正文明载，可写其怨 |
| Salvarsan 时间 | 1909 发现 Compound 606 有效，1910 末上市、1911 被 Neosalvarsan 改良——「1909 发现/1910 上市」勿混 |
| 癌症研究 | Wilhelm II 私人嘱托 + Speyer 捐资建癌症研究部；「转移瘤恶性递增」发现——可作副线页 |
| Manifesto 93 | 1914 签署《九三宣言》为德国一战政策辩护——历史事实，客观一句带过即可 |
| 犹太身份与身后 | 纳粹时期成就被抹杀、1938水晶之夜肖像被毁、1940 好莱坞电影在德被禁——背景叙事可写，克制呈现 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| magic bullet | 魔弹 | Zauberkugel，其自创术语 |
| side-chain theory | 侧链学说 | 受体理论前身 |
| Salvarsan / arsphenamine | 洒尔佛散 / 砷凡纳明 | 606 号化合物；首个抗菌化疗药 |
| mast cell | 肥大细胞 | Mast=德语催肥饲料，命名由来 |
| chemotherapy | 化学治疗 | Ehrlich 命名并开创 |
| amboceptor | 双受体（桥体） | 侧链学说术语，今已不用 |
| complement | 补体 | 其假设的「附加」免疫分子 |
| serum valency | 血清效价 | 豚鼠四日死亡判定标准 |
| horror autotoxicus | 自身毒性恐惧 | 1906 提出，自免保护机制 |
| Ehrlich's reagent | 埃尔利希试剂 | 尿检用对二甲氨基苯甲醛试剂 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Savage** — Alex-Productions（manifest 预分配）
- **风格**：张力 / 决断 / 冲刺感
- **匹配理由**：Ehrlich 的科研是「以化学合成物做地毯式筛选」的攻坚战役——606 号化合物的第 606 次尝试本身就是冲刺；Savage 的张力匹配 Salvarsan 战争的论战岁月与「魔弹」一词的决绝意象，也匹配其与 Behring 恩怨的戏剧性。
- **本地路径**：`music_audio/` 下 Savage 曲目 → 复制为 `presentations/20th_century/Paul_Ehrlich/Savage.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。
