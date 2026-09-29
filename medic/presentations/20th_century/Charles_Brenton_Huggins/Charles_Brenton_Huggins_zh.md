# 医学家立传提示词（Charles Brenton Huggins）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1966 年得主（同届 Peyton Rous 各自半奖、理由不同）。
> 本文件是 Charles Huggins 的人物专属立传提示词：事实基准唯一来源为本地 Wikipedia 页面。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Charles Brenton Huggins（1901-09-22 生于加拿大哈利法克斯 ~ 1997-01-12 逝于芝加哥，享年 95）
- **气质关键词**：**前列腺癌激素疗法的开创者、"发现是我们的本行"、90 岁仍在做实验的外科医生**
- **诺奖获奖理由（1966，逐字引用 medic/nobel_medicine_citations.json）**：
  > "for his discoveries concerning hormonal treatment of prostatic cancer"
  > （因其关于前列腺癌激素治疗的发现）——注意 "his"：Huggins 独得该半奖
- **设计母题**：**激素的双向天平（hormonal balance）**。雄激素推动前列腺生长、雌激素使其萎缩——
  癌症治疗第一次不是"切除更多"而是"调配天平"；视觉母题用天平两端的小圆点与倾斜的杠杆。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Charles_Brenton_Huggins/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 medic 路径执行：页面读 `medic/presentations/pages/20th_century/{Dir}/page.md`，
> 产出放 `medic/presentations/20th_century/Charles_Brenton_Huggins/`，数据库写 greatminds 库（MySQL）。
> 第 0 步核对事实基准 → 第 1 步建目录含 images/ → 第 2 步复制 Makefile 设
> `MAIN=Charles_Brenton_Huggins_zh`、`VIDEO_NAME=Charles_Brenton_Huggins_zh` → 第 3 步收肖像（infobox 载 1966 照，Commons 回退）→
> 第 4~9 步 tex 编写 → 编译循环（0 error、vbox≤10pt、hbox≤50pt）→ pdftoppm 逐页目检 → make images/video → Review。

## 三、研究领域梳理 + 入库（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | physiology | 生理学 | 前列腺功能与激素调控（infobox Fields） | 核心页 |
| 1 | oncology | 肿瘤学 | 前列腺癌/乳腺癌激素疗法，诺奖核心 | 核心页 |
| 2 | urology | 泌尿学 | 芝加哥大学建校即被分配的科室，自修成才 | 职业页 |
| 3 | biochemistry | 生物化学 | 显色底物与磷酸酶比色法 | 方法页 |

## 四、社会关系梳理 + 入库（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Francis Peyton Rous | 无向 | 1966 诺贝尔生理学或医学奖同届各自半奖（Huggins=前列腺癌激素疗法；Rous=致瘤病毒） |
| spouse | Margaret Wellman | 无向 | 手术室护士，1927 年结婚；一子一女 |
| advisor-student | Howard Guy Williams-Ashman | Huggins→学生 | page.md 明载 Notable students |
| advisor-student | Shutsung Liao | Huggins→学生 | page.md 明载 Notable students |
| advisor-student | Paul Talalay | Huggins→学生 | page.md 明载 Notable students |
| advisor-student | A. Hari Reddi | Huggins→学生 | page.md 明载 Notable students |
| advisor-student | Clarence V. Hodges | Huggins→学生 | 1940-41 前列腺癌去势/雌激素疗法三连论文合作学生 |
| advisor-student | William Wallace Scott | Huggins→学生 | 1940-41 前列腺癌去势/雌激素疗法三连论文合作学生 |
| colleague | Dallas Phemister | 无向 | 芝加哥大学外科主席，1927 年招募其为建校元老之一 |
| colleague | Robert Robison | 无向 | 1931 年伦敦李斯特研究所生化进修时的实验室主人 |

> 说明：relations=10 全部 page.md 明载。诺贝尔提名人（Harrison/Warburg/Murphy/Szent-Györgyi）是程序性事实非关系，不入库。
> 自查 SQL：`SELECT COUNT(*) FROM person_relation WHERE from_id=<pid> OR to_id=<pid>;` 预期 = 10。

## 五、配色方案

- **气质**：临床与实验室并重、务实的外科医生型科学家
- **主色**：藏青紫 `#2E1A47`（手术服与芝加哥的深沉）+ 香槟金 `#D4AF37`（诺奖色）
- **四分类色 badge**：`badgeHormone` 激素疗法 — 冷青 `#0E7C7B`；`badgeProstate` 前列腺 — 暖橙 `#E07B30`；`badgeChroma` 显色底物 — 电光蓝 `#4C5FD5`；`badgeAward` 荣誉 — 皇家紫 `#52307C`
- **背景母题**：天平杠杆弧线 + 两端小圆点，稀疏底色

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页
01  封面 — 激素疗法的开山者 / Charles B. Huggins 1901–1997 + 四色 badge + 国籍行（Canada→United States）
02  身份信息页 — 生卒/哈利法克斯出身/Acadia BA 19 + Harvard MD 1924/芝加哥大学 Ben May 实验室/核心领域
03  核心贡献概览 — 前列腺激素调控 / 去势+雌激素疗法 / 乳腺癌模型 / 显色底物
04  加拿大少年 (1901–1924) — 哈利法克斯出生；Acadia 大学 19 岁毕业（哥大暑期补物理/有机化学）；Harvard Medical School MD 1924
05  密歇根与芝加哥建校 (1924–1936) — 密歇根总外科住院训练（Coller 门下）结识护士 Margaret（1927 结婚）；1927 被 Phemister 招入新建芝加哥大学医学院，为八位建校元老之一，被分配泌尿科自修成才
06  伦敦进修与前列腺生理 (1931–1939) — 1931 Lister 研究所 Robison 实验室生化进修；1939 犬前列腺液分离法；前列腺需雄激素维持功能、雌激素可拮抗；老龄犬前列腺增生可被雌激素缩小
07  1940-41：激素治癌（核心贡献页）— 与学生 Hodges/Scott 三连论文：去势或雌激素治疗使转移性前列腺癌患者肿瘤缩小——数日内剧痛缓解；21 例中 4 例存活逾 12 年
08  显色底物与酶测定 — 磷酸酶/葡萄糖醛酸酶/酯酶比色法定量（chromogenic substrates 一词由其首创）——服务于前列腺癌的血液酶学监测
09  乳腺癌的 analogous 发现 (1950s) — 雌激素刺激、雄激素减缓乳腺癌生长；DMBA 口服大鼠模型（100% 成瘤，后世称 Huggins's tumor）；同年逐渐退出手术转向全职研究
10  1966 诺贝尔奖 — 理由逐字；与 Rous 同届各自半奖；"第二个癌症方向诺奖"；提名来自 Harrison/Warburg/Murphy/Szent-Györgyi
11  荣誉与认可 — NAS 与 AAAS 1949 · 美国哲学学会 1962 · Lasker 1963 · Cameron Prize 1956 · Gairdner 1966 · Pour le Mérite · 秘鲁太阳勋章大官佐 · 加拿大医学名人堂 · 爱丁堡 Cameron 讲席
12  Ben May 实验室 — 1951 实业家 Ben E. May 捐建 Ben May 癌症研究实验室，Huggins 任主任至 1969；1962 William B. Ogden 杰出贡献讲席教授
13  "Discovery is our business" — 办公室铭牌箴言（page.md 明载，可引原文+译文）；90 岁仍每周长时间亲手做实验
14  家庭与身后 — 子 Charles E. Huggins 亦为外科医生（麻省总医院血库主任，1990 卒）；妻 Margaret 1983 卒；1997-01-12 逝于芝加哥，享年 95；200+ 篇论文
15  结尾
```

## 七、特殊陷阱表（★ 执行时必须核对）

| # | 陷阱 | 说明 |
|---|------|------|
| 1 | 获奖理由 | 逐字 "for his discoveries concerning hormonal treatment of prostatic cancer"；"his" 独得半奖；与 Rous 同届但理由不同 |
| 2 | 国籍口径 | 生于加拿大哈利法克斯、infobox Citizenship=American；Nobel 官方口径（citation json）为 "Canada United States"——yaml 双籍 Canada+United States，页面国籍行写 "Canada → United States" |
| 3 | 学位 | Harvard **MD 1924**（医学博士），勿写 PhD；Acadia BA 时年 19 岁 |
| 4 | 建校元老 | 1927 年芝加哥大学医学院**八位建校元老之一**，被分配到泌尿科后自修专业——叙事亮点 |
| 5 | 21 例数据 | 1940-41 系列：转移性前列腺癌患者 21 例中 4 例自治疗起存活逾 12 年、数日内疼痛缓解——数字照实 |
| 6 | chromogenic substrates | 该术语由 Huggins **首创**（coined）——细节勿漏 |
| 7 | Huggins's tumor | DMBA 口服大鼠乳腺癌模型，100% 快速成瘤——命名照实 |
| 8 | 引语红线 | 仅 "Discovery is our business."（办公室铭牌箴言）有英文原文可引；其余不得造引语 |
| 9 | 提名人 | 诺贝尔提名由 J. Hartwell Harrison 与 Warburg/Murphy/Szent-Györgyi 提出——程序性事实，不建关系边 |
| 10 | 家庭 | 子 Charles E. Huggins 亦为外科医生、麻省总医院血库主任（1990 卒）——一句带过 |
| 11 | 与 Rous 的关系 | 两人仅为同届得主，page.md 无任何合作记载——只建 co-honored，勿写成同事 |
| 12 | 高龄科研 | 90 多岁仍做实验（page.md 两处明载）——第 13 页素材 |

## 八、术语清单

| 英文 | 中文 | 风险点 |
|------|------|--------|
| hormonal treatment | 激素治疗 | 诺奖理由核心词 |
| orchiectomy | 睾丸切除术 | 1941 疗法一手 |
| estrogen / androgen | 雌激素 / 雄激素 | 拮抗关系勿写反 |
| chromogenic substrate | 显色底物 | Huggins 首创术语 |
| phosphatase | 磷酸酶 | 血液酶学监测指标 |
| DMBA | 二甲基苯并蒽 | 乳腺癌模型诱癌剂 |
| Ben May Laboratory | Ben May 癌症研究实验室 | 1951 捐建 |
| Pour le Mérite | 功勋勋章 | 普鲁士/德国科学与艺术勋章 |

## 九、背景音乐选择

- **选定曲目**：**Shine Like The Sun** — Alex-Productions（manifest 预分配）
- **匹配理由**：明亮笃定的行进感对应"激素调配天平"的临床暖意——其疗法让转移性前列腺癌患者数日内疼痛缓解，
  是医学诺奖史上少有的"以缓解痛苦为主旋律"的叙事；也贴合其 90 岁仍在实验室的阳光式长寿科研。
- **备选（未采用）**：Daylight（明亮感重叠且 batch-07 已用于 M-B Moser）、Expedition（探索感偏"迁徙"，不如本篇"临床之光"贴合）
- **本地路径**：`music_audio/` 曲库按 curated_tracks.md 复制为 `medic/presentations/20th_century/Charles_Brenton_Huggins/Shine_Like_The_Sun.wav`
