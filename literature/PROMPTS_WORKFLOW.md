# OpenLiterature 提示词撰写 + 社会关系入库工作流（2026-09 批次）

> 诺贝尔文学奖得主批量「人物专属立传提示词撰写 + 社会关系入库」共享工作流。
> 所有执行 agent 必读本文档 + 各自分批文件（`literature/prompt_batches_lit.json`），然后逐人执行。

## 0. 路径与数据源（OpenMathAI 根 = `/Users/ericksun/workspace/codebuddy/OpenMathAI`）

| 资产 | 路径 |
|------|------|
| 分批清单 | `literature/prompt_batches_lit.json`（batch 1–20，member 含 page/prompt/yaml 路径、qid、year、bgm、color） |
| 每人数据源 | `literature/presentations/pages/20th_century/{Dir}/page.md`（Wikipedia 全文 + YAML frontmatter：qid/生卒/国籍/职业/award_received/educated_at/languages_spoken）+ 同目录 `metadata.json`、`images.txt` |
| 名录（含获奖理由中译） | `literature/presentations/20th_century/OpenLiterature_20th_Century_Nobel_Laureates.md`；官方获奖理由 EN 原文 + 中译亦可从 `literature/generate_20th_century_list.py` 的 `CITATION_ZH`（key=(年份字符串, 姓名)）直接取 |
| 提示词结构母本 | `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（★ 0–11 节骨架照此，内容适配文学家） |
| yaml 字段母本 | `MySQL/data/Kenneth_G_Wilson.yaml` |
| 入库引擎 | `MySQL/seed_person.py`（幂等；按 QID → name_en 匹配人物） |
| BGM 曲库 | `music_audio/curated_tracks.md`（每人 BGM 已预分配，见分批文件） |

## 1. 每人执行步骤

### 1.1 通读数据源

通读该人 `page.md`（frontmatter + infobox + 导语先行，正文各节全覆盖：awards/创作生涯/家庭/晚年），建立事实基准。`metadata.json` properties 可辅助，但**正文优先**（metadata 有噪声，冲突以正文为准并汇报注明）。

### 1.2 撰写提示词 → `literature/presentations/20th_century/{Dir}/{Dir}_zh.md`

190–230 行，结构对齐标杆（把「物理学家」换「文学家」）：

- **一、模板定位**：1-2 句（OpenLiterature + 本人物 + 设计哲学）。
- **二、背景信息【人物专属】**：姓名（中英）、生卒、诺奖年份与**官方获奖理由 EN 原文+中译**（从名录/`CITATION_ZH` 取，禁止改写）、气质关键词（3 短语）、**设计母题**（贴合其文学世界/代表作意象的视觉概念）、本地数据源路径 + Wikipedia URL（肖像第 0 步标「待下载」）。
- **三、任务流程第 0–9 步**：
  - 第 0 步：事实基准——生卒（含享年）、国籍（含变迁）、家庭、教育、**文学师承与影响**（page.md 明载才写）、任职/流亡经历、关键荣誉、核心作品与贡献（4–6 条）、关键时间线（15–20 节点）。
  - 第 4 步：**文学领域表**（4–5 行：rank/领域 name_en/中文/说明/对应页；如 magical realism、modernist poetry、epic novel、social criticism，name_en 英文小写名词短语）。
  - 第 4.5 步：社会关系表（与 yaml 完全一致）。
  - 第 5 步：配色（主色 hex 用分批文件预分配值 + 诺奖香槟金 `C9A227` + badgeA–D 四分类色；批内主色不重复）。
  - 第 6 步：幻灯片序列（10–16 页，含身份信息页★必做；**文学家无公式框——用代表作书影/名句引文框/意象图式替代**）。
  - 第 7–8 步：版式要点 + 该人专属陷阱表（争议归属/易错年份/同名区分/无载禁写清单）。
  - 第 9 步：术语清单（EN/中文/风险点，8–12 条）。
- **四、BGM 建议**：分批文件预分配曲名，写匹配理由（对照 `curated_tracks.md` 标签）。

### 1.3 撰写 yaml → `MySQL/data/{Dir}.yaml`

- `name_en`：**用 page.md frontmatter 的 name**（如 1910=`Paul Heyse` 非 `Paul von Heyse`、1923=`W. B. Yeats`）；库内已有该人记录且 name_en 不同 → **沿用库内形式**（先查 `SELECT id,name_en FROM people WHERE qid='{qid}'`）。
- `qid`：分批文件已给出；`name_zh`/`birth_date`/`death_date`/`description` 来自 frontmatter 与名录。
- `primary_occupation: writer`；`occupations` 1–3 条（writer rank 0 + 明载的 poet/novelist/playwright/essayist/translator）。
- `fields` 4–5 条（与文学领域表一致）；`nationalities` 1–2 条（变迁按 page.md 口径分条）。
- `relations`：与第 4.5 步一致。类型白名单：`advisor-student`（direction: `advisor`=对方是导师 / `student`=对方是学生；文学家少用，仅 page.md 明确师承时）/ `influence`（思想影响）/ `colleague`（同社/同人圈/编辑合作）/ `co-honored`（同年共享诺奖：1904 Mistral↔Echegaray、1917 Gjellerup↔Pontoppidan、1966 Agnon↔Sachs、1974 Johnson↔Martinson）/ `spouse` / `parent-child` / `rival` / `controversy`。**只收 page.md 明载关系**，无载禁写；note 简洁。

## 1.4 入库与验证

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/{Dir}.yaml
```

- 并发撞 fields/occupations 唯一键（Duplicate entry）→ 等 2 秒重跑（幂等）。
- 验证：`python3 -c "from db_mysql import get_conn; conn=get_conn(); cur=conn.cursor(); cur.execute(\"SELECT id,name_en,has_social_data FROM people WHERE qid='{QID}'\"); p=cur.fetchone(); print(p)"`，再数 `person_field`（fields≥4）与 `person_relation`（relations≥2，实在无载者除外并注明）。

## 2. 红线与陷阱

- yaml `note` 含 `: ` 或以引号开头 → 整体用单引号包裹，否则 YAML 解析失败。
- 对手方（影响者/伴侣/对手）入库为 stub：不编造 qid；name_en 用规范全名；库内已有记录先查（如 `Bertrand Russell` 库内几乎必已存在，数学/哲学侧已建，Q33760）。
- 同名区分：J. V. Jensen（丹麦小说家）、两度同姓者 note 写清身份。
- 无载禁写：page.md 没写的一律不写（不编造影响者、不编造弟子、不从颁奖词反推关系）。
- 政治相关内容（如帕斯捷尔纳克/索尔仁尼琴的苏联经历、丘吉尔）：只按 page.md 客观事实简述，**不作政治评价、不展开政治叙事**。
- 中文引号内不写「原话」，除非 page.md 有英文原文。
- **禁止修改** `generate_20th_century_list.py`、名录 md、本工作流文件（主控统一收尾）。

## 3. 汇报

每人完成后向主控 send_message 一行：
`✅ {Name} | prompt✅ | yaml✅ | DB id={id} fields={n} relations={n} | 主色{hex} BGM{曲名}`
全部完成后再发一条汇总（成功/失败清单）。

## ★ 21 世纪批次（2026-09-29 增补，batch 清单 = `literature/prompt_batches_lit_21st.json`，5 批 × 5 人）

- 数据源：`literature/presentations/pages/21st_century/{Dir}/page.md`（frontmatter 含 qid/生卒/国籍/languages_spoken）+ `metadata.json` / `images.txt`
- 提示词落盘：`literature/presentations/21st_century/{Dir}/{Dir}_zh.md`（25 人全部新写，结构同 §1.2）
- yaml 落盘：`MySQL/data/{Dir}.yaml`；`has_biography: false`
- 获奖理由中译：从 `literature/generate_21st_century_list.py` 的 `CITATION_ZH`（key = 规范化英文原文）取；名录 `literature/presentations/21st_century/OpenLiterature_21st_Century_Nobel_Laureates.md` 可对照
- 库内现状：多数人已作为 20 世纪批次（lit-bios-2026）的关系对手方 stub 存在（有 relation 入边、has_social_data=0）；seed_person.py 按 QID→name_en UPD 复用同一记录，**勿另建别名记录**；yaml 关系条目与库内既有行同 (from,to,type) 撞 uq_rel 属正常幂等，跳过即可
- 例外：无共享奖年份（21 世纪文学奖均单人获奖），**无需 co-honored**
- 特殊人物：Mo Yan（政治沉默争议客观简述）、Peter Handke（Milošević 相关只按 page.md 客观事实、不评价）、Bob Dylan（音乐人身份 fields 以 songwriting/lyricism 为主）、Jon Fosse（2023）、Han Kang（2024，韩文 frontmatter 噪声以正文为准）、László Krasznahorkai（2025，获奖口径「2025-03 公布」可注）
- 其余流程（提示词结构/领域表/关系表/yaml 字段/入库/验证/红线/汇报格式）与 §1/§2 完全一致
