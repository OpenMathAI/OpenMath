# Camille Jordan（卡米尔·若尔当）立传提示词

> 榜单：#95 · qid=Q310755 · 1838-01-05 – 1922-01-22 · 法国数学家
> 数据库主记录：id=95（群论奠基人之一）

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Marie Ennemond Camille Jordan
- **生卒**：1838-01-05 里昂 → 1922-01-22 巴黎，享年 84
- **国籍**：法国
- **身份**：数学家、工程师（土木工程 Corps des Ponts）、教授
- **机构轨迹**：
  - 教育：École polytechnique（综合理工）→ 巴黎理学院 → Mines ParisTech
  - 任职：综合理工教师 → 法兰西公学院（Collège de France）教授
- **研究领域**：群论、线性代数、测度论、拓扑学

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **Jordan 曲线定理**：简单闭曲线把平面分为内外两部分——拓扑学最直观又最深刻的定理（Schoenflies 推广）。
2. **Jordan 标准形**：线性代数核心——复矩阵的准对角分解，现代数值线性代数的基础。
3. **Jordan–Hölder 定理**：群合成列的唯一性——群论基本定理。
4. **Jordan 测度（Jordan content）**：Lebesgue 测度之前的面积概念——测度论先驱。
5. **Jordan 定理（有限线性群）**：有限线性群的正规子群理论。
6. **Galois 理论的主流化**：1870《Traité des substitutions》使置换群/Galois 理论进入主流，获 Poncelet 奖。
7. **Mathieu 群研究**：最早研究的散在单群（sporadic groups）。
8. **《Cours d'analyse》**：综合理工分析教材，影响深远（奇特的记号选择著称）。
9. **有界变差与 Fourier 级数**：Jordan 检验（有界变差函数的 Fourier 级数收敛条件）。

## 3. 配色方案

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（巴黎红） | #8B1A1A | 综合理工/法兰西传统 |
| 辅助（群论青） | #1E6E6E | 群论 |
| 强调（标准形金） | #B8860B | Jordan 标准形 |
| 背景 | #FAF6EF | 米白纸色 |

## 4. 12 页 Slide 规划

1. 封面：大标题 + 副标题「Jordan 曲线定理 · Jordan 标准形 · 群论奠基人」
2. 生平总览：时间轴（1838 → 1860 论文 → 1870 Traité → 1882 Cours d'analyse → 1922 去世）
3. Jordan 曲线定理：拓扑学的直觉
4. Jordan 标准形：线性代数核心
5. Jordan–Hölder 定理：合成列
6. Jordan 测度：Lebesgue 之前
7. Galois 理论主流化：1870 Traité
8. Mathieu 群与散在群
9. 《Cours d'analyse》：综合理工教材
10. 有界变差与 Fourier 级数
11. 工程与数学的双重人生
12. 终章：84 岁、小行星 25593、历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **三个"Jordan"**：Camille Jordan（本文，数学家）、Wilhelm Jordan（大地测量学家，Gauss–Jordan 消元）、Pascual Jordan（物理学家，Jordan 代数）——**正文明确提示勿混淆**，脚本/提示词中注明。
- **Jordan 标准形 vs Jordan 曲线定理 vs Jordan 测度 vs Jordan–Hölder**：不同领域多个命名——slide 中区分。
- **Jordan 曲线定理归属**：定理直观但证明艰深，Jordan 1887 给出（早期证明有争议，后人完善）——表述谨慎。
- **Galois 理论**：Jordan 1870 使其主流化——不写 Jordan 发明 Galois 理论。
- **Mathieu 群**：Mathieu 1860s 发现，Jordan 深入研究——归属清晰。
- **生卒核对**：1838-01-05 / 1922-01-22，metadata 与正文一致。
- **工程师身份**：正规教育是工程师，数学是"业余"转正——双重人生叙事。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q310755 | 需更新（当前 NULL） |
| name_zh | 卡米尔·若尔当 | 需更新（当前 若尔当） |
| birth_date | 1838-01-05 | 需更新 |
| death_date | 1922-01-22 | 需更新 |
| has_biography | 0 | 保持 |
| has_social_data | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20，已由 seed 脚本完成）

- 导师：Victor Puiseux（新建）、Joseph Alfred Serret（新建）
- 学生：Marie Georges Humbert（新建）
- 学术影响：Émile Picard（78，后继）、Édouard Goursat（746，学生辈）

## 8. 奖项清单（全部收录）

- Poncelet Prize 1870（67）
- Officer of the Legion of Honour（114）
- Foreign Member of the Royal Society（45）

## 9. 机构清单

- 教育：École Polytechnique（6）、Mines ParisTech（7）
- 任职：École Polytechnique（6）、Collège de France（47）、Corps des Ponts et Chaussées（桥梁道路工程兵团，新建）

## 10. 终审清单

- [ ] 三个 Jordan 不混淆
- [ ] 多个 Jordan 命名区分
- [ ] Galois 理论"主流化"非发明
- [ ] Mathieu 群归属
- [ ] 工程师双重人生
- [ ] has_biography 保持 0
## 11. Review 流程规范（两轮 Review，§16 Wikipedia 终审 + 项目标准）

> 立传完成后按此规范执行两轮 Review（参照 #73 Fredholm Review-1 执行标准）。

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/<Name>/page.md` 建立事实基准，逐页对照 Beamer tex 的全部事实（生卒/机构/年份/奖项/荣誉/家族/引语）
- [ ] **头像**：优先使用 Wikipedia infobox 照片（`images.txt` 或 infobox `image` 字段），下载原图到 `images/<name>_portrait.jpg`；无照片时用装饰圆替代
- [ ] **国籍**：封面顶部徽章明确国籍（`\faIcon{globe}\enspace <Country>`），与 Cartan/Borel/Fredholm 立传格式一致
- [ ] **引语核对**：tex 引语必须能在 Wikipedia 原文找到（§14.6 伪引语红线）；找不到则改为忠实转述
- [ ] **编译验证**：`make distclean && make`（latexmk 自动多遍编译；remember picture 需要多遍）
- [ ] **更新提示词**：Review 修正（头像来源/国籍/新细节）写回 `prompts/<Name>_zh.md`
- [ ] **更新排行榜**：`✅/🔲` → `✅/✅✅`

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 结束页时间线 ≥7 段拆两行（避免溢出）
- [ ] 中文标点/断行/间距统一
- [ ] 与同榜数学家格式对齐（封面/配色/结构）
- [ ] 排行榜标记 `✅✅/🔲` → `✅✅/✅✅`

