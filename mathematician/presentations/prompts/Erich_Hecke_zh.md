# 赫克 (Erich Hecke) 立传提示词

> 严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)。
> 数据库字段梳理见工作指南 §二十一；社会关系入库见 §二十。

---

## 背景信息

- **目标数学家**: Erich Hecke (1887–1947)
- **气质关键词**: **Hecke 算子、模形式理论的奠基人、代数数论的分析大师、Langlands 纲领的数学源头**
- **Wikipedia 页面**: ✅ 已下载
  - 路径: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Erich_Hecke/`
  - Wikipedia 英文条目: `Erich Hecke`
- **Beamer 文件**: `mathematician/presentations/Erich_Hecke/Erich_Hecke_zh.tex` (待创建)
- **参考模板**: `wiener/`, `ramanujan/`, `hardy/` 的完整源码
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/wiener/Norbert_Wiener_zh.tex` — Wiener 完整源码
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/grothendieck/Makefile` — 构建脚本（直接复制）
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Mathematician_Biography_Guide.md`

---

## 第 0 步：核对 Wikipedia 页面 ✅

已下载到 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Erich_Hecke/`

- **全名**: Erich Hecke
- **生卒日期**: 1887-09-20 ~ 1947-02-13，享年 **59** 岁
- **国籍**: 🇩🇪 German Empire（德意志帝国，生于 Posen 省 Buk，今波兰 Poznań）
- **出生地**: Buk, Province of Posen, German Empire（今波兰 Poznań 附近）
- **逝世地**: Copenhagen, Denmark（哥本哈根，丹麦）
- **博士导师**: David Hilbert（大卫·希尔伯特，哥廷根）
- **教育经历**:
  - Friedrich-Wilhelms-Gymnasium of Posen（波森中学）
  - University of Wrocław（布雷斯劳大学，即 Breslau）
  - Frederick William University Berlin（柏林大学）
  - University of Göttingen（哥廷根大学，博士）
- **主要任职机构**:
  - University of Basel（巴塞尔大学）
  - University of Göttingen（哥廷根大学）
  - University of Hamburg（汉堡大学）
- **关键荣誉**:
  - Ackermann–Teubner Memorial Award 1938（阿克曼-托伊布纳纪念奖）
  - 1936 年 ICM（奥斯陆）全会演讲人
- **重要学生**: Kurt Reidemeister、Heinrich Behnke、Hans Petersson、Bruno Schoeneberg、Wilhelm Maak、Hans Maass、Ernst-August Behrens、Erna Witt 等
- **研究领域**: number theory（数论）、modular forms（模形式）、analytic number theory（解析数论）、algebraic number theory（代数数论）

### 关键时间线：

- 1887: 9月20日生于德意志帝国 Posen 省 Buk
- 1910: 哥廷根大学获博士学位，导师 Hilbert
- 1915: 任巴塞尔大学教授
- 1918: 任哥廷根大学教授（接替离开的 Landau 相关职位）
- 1919: 转任汉堡大学（Hamburg 学派的创建者之一）
- 1920s: 建立 Hecke 算子理论、Hecke 特征、Hecke L-函数
- 1933: 签署《德国大学教授对阿道夫·希特勒与国家社会主义的效忠宣誓》，但后世公认其内心反对纳粹
- 1936: ICM 奥斯陆全会演讲
- 1938: 获 Ackermann–Teubner 纪念奖
- 1947: 2月13日逝世于哥本哈根，享年 59 岁

### ★ 叙事亮点：

1. **Hecke 算子** — 模形式理论最核心的工具。Hecke 用一组算子（T_p）给出模形式空间的本征分解，使模形式理论从"个别函数的性质"升级为"谱理论"。
2. **Hecke 特征 / Hecke L-函数** — 将 Dirichlet 特征推广到代数数域上的 idèle 类特征，其 L-函数成为现代解析数论与 Langlands 纲领的桥梁。
3. **Dedekind ζ 函数的函数方程** — 早期工作，用 theta 函数证明了 Dedekind ζ 函数的函数方程。
4. **汉堡学派的缔造者** — 与 Emil Artin 等共同把汉堡打造成 1920-30 年代数论重镇。
5. **Weil 的至高评价** — André Weil 在《Basic Number Theory》前言写道："要在代数数论经典路径上超越 Hecke，是徒劳且不可能的。"
6. **模形式理论奠基** — 他创立了尖点形式（cusp forms）的一般理论，为 Langlands 纲领铺路。

### ★ 史实注意：

- **1933 年效忠宣誓**：Hecke 签署了效忠希特勒的宣誓，但史料普遍认为他内心反对纳粹。表述须谨慎："签署了效忠宣誓，但后世公认其反对纳粹"，不渲染、不洗白。
- **Hecke 算子 ≠ Hecke 代数**：Iwahori–Hecke 代数、affine Hecke 代数等是后世（Hecke 去世后）发展，不属于 Hecke 本人的直接贡献，表述时区分。
- **"模形式理论奠基人"**：Hecke 建立在 Klein、Hurwitz、Ramanujan 等人的早期工作上，用"系统化/奠基性"而非"第一个"。
- **Wiener 过程 ≠ Hecke 工作**：No，Hecke 与 Wiener 无关。注意别串台。

---

## 数据库字段核对表（第 0 步之后必填）

| # | 表 | 字段 | 核对值 |
|:--:|---|------|--------------------------|
| 1 | `people` | qid | `Q687638` |
| 2 | `people` | name_en | `Erich Hecke` |
| 3 | `people` | name_zh | `埃里希·赫克` |
| 4 | `people` | name_variants | `["Hecke 算子的创造者","模形式理论的奠基人"]` |
| 5 | `people` | gender | `male` |
| 6 | `people` | birth_date | `1887-09-20` |
| 7 | `people` | death_date | `1947-02-13` |
| 8 | `people` | description | `German mathematician (1887–1947)` |
| 9 | `people` | primary_occupation | `mathematician` |
| 10 | `person_occupation` | 职业（rank 排序） | `mathematician(0)`、`university teacher(1)` |
| 11 | `person_field` | 领域（rank 排序） | `number theory(0)`、`modular forms(1)`、`analytic number theory(2)` |
| 12 | `award_laureate` | 获奖记录 | `Ackermann–Teubner Memorial Award 1938(edition=?, share_type=独享)` |
| 13 | `person_institution` | 教育/任职 | `education: Göttingen(1910博士)`；`employment: Basel(1915–1918)、Göttingen(1918–1919)、Hamburg(1919–1947)` |
| 14 | `person_nationality` | 国籍 | `German Empire`（出生）→ `Germany` |
| 15 | `person_relation` | 社会关系 | 见 §二十（第 4.5 步） |
| 16 | `rankings` | 榜单 | `OpenMath_20th_Century_51_108`、`rank=58`、`status=🔲/🔲` |

> ★ 奖项列注意：**全部收录**（含追授/政治勋章/名誉类，见 21.2.4）。

---

## 第 4.5 步：社会关系入库（MySQL）

> 已按 §二十 梳理，参考实现 `MySQL/seed_hecke_relations.py`。

**社会关系清单：**

| 关系类型 | 对象 | 方向 | note |
|---------|------|------|------|
| 老师 | David Hilbert | 师→生 | 哥廷根博士导师，Hilbert 学派数论传承 |
| 学生 | Kurt Reidemeister | 师→生 | 拓扑学，布雷斯劳/哥廷根教授 |
| 学生 | Heinrich Behnke | 师→生 | 复分析，明斯特学派 |
| 学生 | Hans Petersson | 师→生 | 模形式与 Hecke 理论传承 |
| 学生 | Bruno Schoeneberg | 师→生 | 汉堡学派 |
| 学生 | Wilhelm Maak | 师→生 | 汉堡学派 |
| 学生 | Hans Maass | 师→生 | Maass 形式，模形式与自守形式 |
| 学生 | Erna Witt | 师→生 | 汉堡学派 |
| 荣誉共同体 | André Weil | 无向 | Weil 在《Basic Number Theory》前言盛赞 Hecke |
| 同事 | Emil Artin | 无向 | 汉堡学派共同缔造者 |

**入库操作：**
1. `people` 表：Hecke 已存在（id=58），补齐 qid/Q687638、name_variants、description、birth/death；`has_social_data` 置 1
2. `fields` 字典：补充 `modular forms`、`analytic number theory`
3. `institutions` 字典：补充 `University of Basel`、`University of Wrocław`
4. `person_relation`：Hilbert（已有）→ Hecke；Hecke → 7 位学生（新建占位，has_biography=0）；Weil ↔ Hecke（同事/荣誉共同体）；Artin ↔ Hecke（同事）
5. 缺失人物先建占位（`has_biography=0`），关系 note 加 `[材料待展开]` 前缀

**校验：**
```sql
SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
FROM person_relation pr
JOIN people a ON a.id=pr.from_id
JOIN people b ON b.id=pr.to_id
JOIN relation_types rt ON rt.relation_key=pr.relation_type
WHERE a.name_en='Erich Hecke' OR b.name_en='Erich Hecke';
```

---

## 第 5 步：设计配色方案

- **建议配色：模形式蓝 + 汉堡港青 + 算子金 + 羊皮纸米** —— 数论与模形式的谱之美 + 汉堡学派的城市气质
- 与已有配色完全不同！

- 主要色值：
  | 用途 | 色名 | 建议色值 | 说明 |
  |------|------|---------|------|
  | 背景 | `bgmain` | `#FAF6EF` | 羊皮纸米 —— 经典数论手稿的气质 |
  | 主色 | `coverprimary` | `#1B3A5C` | 模形式蓝 —— Hecke 算子的谱 |
  | 强调色 | `coveraccent` | `#C9A227` | 算子金 —— Hecke 算子 |
  | 深色文本 | `coverdark` | `#1F2A28` | 深墨色 |
  | 浅色文本 | `covermuted` | `#6B7A85` | 蓝灰 |

- 四个分类色：
  - **badgeOperators** (Hecke 算子) — 算子金 `#C9A227`
  - **badgeModular** (模形式) — 模形式蓝 `#2E5F8A`
  - **badgeLfunc** (L-函数) — 解析青 `#2A7F8A`
  - **badgeHamburg** (汉堡学派) — 港口红 `#B04A4A`

---

## 第 6 步：规划幻灯片序列（12 页）

```
00  OpenMath 项目首页

=== 封面与总览 ===
01  封面 — 《赫克：模形式的谱之大师》 / Erich Hecke 1887–1947
02  Hook — 为什么赫克独一无二：Hecke 算子、Langlands 纲领的源头

=== 生平与核心贡献 ===
03  早年与教育 (1887–1910) — Posen 省·哥廷根·Hilbert 门下·Dedekind ζ 函数方程
04  Hecke 算子 (1920s) — 模形式空间的谱分解·本征形式·从函数到谱
05  Hecke 特征与 L-函数 — Dirichlet 特征推广到 idèle·Hecke L-函数
06  代数数论的分析武器 — 《代数数论讲义》·Weil 的至高评价

=== 学派与传承 ===
07  汉堡学派的缔造者 — 与 Artin 共建汉堡数论重镇
08  学生与传承 — Reidemeister·Behnke·Petersson·Maass·Maass 形式

=== 人格与历史 ===
09  纳粹时代的学者 — 1933 效忠宣誓的复杂性·内心反对纳粹
10  Hecke 的世纪遗产 — 从模形式到 Langlands 纲领·现代数论的骨架

=== 结尾 ===
11  结束页 — "他用一组算子，把模形式变成了谱；一百年后，整个 Langlands 纲领仍在它的坐标里。"
```

---

## 第 9 步：史实审查

### Hecke 特有的史实陷阱

| 陷阱类型 | 高危点 |
|---------|--------|
| **1933 效忠宣誓** | Hecke 确实签署了效忠希特勒的宣誓，但史料普遍认为他内心反对纳粹。表述要平衡："签署了效忠宣誓，但后世公认其反对纳粹" |
| **Hecke 算子 vs Hecke 代数** | Iwahori–Hecke 代数（1964）、affine Hecke 代数、double affine Hecke 代数都是 Hecke 去世后发展，不属于本人直接贡献 |
| **"模形式理论奠基人"** | Hecke 建立在 Klein、Hurwitz、Ramanujan 等人基础上。用"系统化/奠基性"而非"第一个" |
| **Hecke 特征 vs idèle 类特征** | Hecke 1930s 提出的 Hecke 特征，后来被 Tate 用 idèle 语言重写（Tate 论文）。表述注意时间线 |
| **国籍** | 生于德意志帝国 Posen 省（今波兰），逝世于丹麦哥本哈根。国籍写 German Empire → Germany |
| **学生名单** | metadata.json doctoral_student 有 16 人，选取有 Wikipedia 条目的主要学生（Reidemeister、Behnke、Petersson、Schoeneberg、Maak、Maass） |

---

## 第 13 步：Wikipedia 本地文档终审（提交前必做）

### 终审清单
- [ ] 生卒日期与 metadata.json 一致（1887-09-20 ~ 1947-02-13）
- [ ] 国籍 German Empire 正确
- [ ] 博士导师 David Hilbert 正确
- [ ] Hecke 算子理论创建时期 1920s 正确
- [ ] 汉堡大学任职 1919 开始正确
- [ ] ICM 1936 奥斯陆全会演讲正确
- [ ] Ackermann–Teubner 奖 1938 正确
- [ ] 编译: `make distclean && make` — 零错误

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. Hecke 算子是模形式理论的核心工具——谱分解是核心叙事
> 2. Hecke 特征/L-函数是连接数论与表示论的桥梁——Langlands 纲领的源头
> 3. Weil 的评价是极佳的权威背书——"在经典路径上超越 Hecke 是徒劳且不可能的"
> 4. 1933 宣誓是历史复杂性，不是道德审判——平衡表述
> 5. 学生是汉堡学派的延续——Maass 形式、Petersson 度量
> 6. 结尾应回归"从个别函数到谱理论"的思想转变
