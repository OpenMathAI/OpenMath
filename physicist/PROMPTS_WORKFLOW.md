# OpenPhysicist 提示词撰写 + 社会关系入库工作流（2026-09 批次）

> 本文档是 20 世纪诺贝尔物理学奖得主（161 位）批量「人物专属立传提示词撰写 + 社会关系入库」的共享工作流。
> 所有执行 agent 必读本文档 + 各自分批文件，然后逐人执行。

## 0. 路径与数据源（全部绝对路径，OpenMathAI 根 = `/Users/ericksun/workspace/codebuddy/OpenMathAI`）

| 资产 | 路径 |
|------|------|
| 分批清单 | `physicist/prompt_batches_2026.json`（batch 1–30，member 含 page/prompt/yaml 相对 OpenMathAI 根的路径、qid、need_prompt/need_relations） |
| 每人数据源 | `physicist/presentations/20th_century/20th_century/{Dir}/page.md`（Wikipedia 全文 + YAML frontmatter：wikidata QID / 生卒 / 国籍 / 职业award_received / doctoral_advisor / educated_at） |
| 提示词模板 | `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` |
| 标杆提示词 | `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（★ 结构母本，0–11 节照此结构） |
| yaml 标杆 | `MySQL/data/Kenneth_G_Wilson.yaml`（★ 字段母本） |
| 入库引擎 | `MySQL/seed_person.py`（幂等；按 QID → name_en 匹配人物） |
| BGM 曲库 | `music_audio/curated_tracks.md` |

## 1. 每人执行步骤（need_prompt=true 的人）

### ★ 先查存量提示词（2026-09-28 增补，必做）

**137/145 人的提示词已由 2026-09-09 先前会话产出**，但目录名常为缩短形式（如 `Arthur_Compton/`、`Louis_de_Broglie/`、`Karl_Siegbahn/`）。执行前先做 token 匹配定位：

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/20th_century
ls -d */ | grep -i "{姓氏关键词}"   # 或按名字 token 逐个 ls 比对
```

匹配规则：既有目录的 token 序列是本人全名 token 序列的子序列且首尾 token 相同（如 `Arthur_Holly_Compton` ↔ `Arthur_Compton`）。

- **已存在**：读存量提示词，以其事实基准/社会关系清单为底稿，核对 page.md 后只补缺失小节（如缺 §术语清单/§陷阱表则补齐，格式对齐标杆），**不要整篇重写**；yaml 按其 §4.5 社会关系表 + page.md 核对后撰写。汇报里注明「prompt 沿用存量{目录名}」。
- **不存在**：按下述完整步骤新写。

### 完整撰写步骤（无存量时）

1. **通读** 该人 `page.md`（先读 frontmatter + infobox 表 + 导语，再读正文各节；长文可分段读，但 awards/教学/任职/家庭/晚年各节必须覆盖），建立事实基准。
2. **撰写人物专属提示词** → `physicist/presentations/20th_century/{Dir}/{Dir}_zh.md`，190–230 行，结构对齐标杆（Kenneth_G_Wilson_zh.md）：
   - 一、模板定位（1-2 句：项目 + 本人物 + 设计哲学）
   - 二、背景信息【人物专属】：姓名（中英）、生卒、诺奖年份与**官方获奖理由英文原文+中译**（取自名录或 page.md，禁止改写）、气质关键词（3 个短语）、设计母题（贴合其物理思想的视觉概念）、本地数据源路径（指向 `20th_century/20th_century/{Dir}/page.md`，**注意：这批人尚无 {Dir}.html 与 images/，第 0 步要写「待下载」并给出 Wikipedia URL `https://en.wikipedia.org/wiki/{Name}`**）
   - 三、任务流程第 0–9 步【模板通用骨架 + 人物专属内容】：
     - 第 0 步：事实基准——生卒（含享年）、国籍（含变迁）、父母/家庭、教育（学校/专业/年份）、博士导师与论文题目（page.md 明载才写，否则标「page.md 无载」）、博士后、任职机构（含年份）、关键荣誉（含年份，从 award_received + 正文）、知名学生（明载才写）、核心贡献清单（4-6 条）、关键时间线（15–20 节点）
     - 第 4 步：研究领域表（4–5 行：rank/name_en/中文/说明/对应页）
     - 第 4.5 步：社会关系表（与 yaml 完全一致）
     - 第 5 步：配色方案（主色 hex + 诺奖香槟金 `C9A227` + badgeA–D 四分类色 hex；**批内主色不得重复**）
     - 第 6 步：幻灯片序列（10–16 页规划，含身份信息页★必做；注明哪些页用高斯表格版式、公式框放什么公式——选该人最标志性公式，page.md 无公式则选概念图式并注明）
     - 第 7–8 步：版式要点 + 该人专属陷阱表（归属争议/易错年份/同名区分/无载禁写清单）
     - 第 9 步：术语清单（英文/中文/风险点，8–12 条）
   - 四、BGM 建议：从 `music_audio/curated_tracks.md` 按气质选 1 曲（给文件名），批内尽量不重复
3. **撰写 yaml** → `MySQL/data/{Dir}.yaml`（字段母本 = Kenneth_G_Wilson.yaml）：
   - `name_en`：用 page.md frontmatter 的 name；若库内已有该人记录且 name_en 形式不同，**沿用库内形式**（先 `SELECT id,name_en FROM people WHERE name_en LIKE '%关键词%'` 查重）
   - `qid`：page.md frontmatter 的 wikidata（分批文件已给出）
   - `name_zh` / `birth_date` / `death_date` / `description`：来自 frontmatter 与名录；在世者 `death_date` 省略
   - `primary_occupation: physicist`；`has_biography: false`（本批均未做 Beamer）
   - `occupations`：1–3 条（physicist rank 0 + page.md 明载的其他职业）
   - `fields`：4–5 条（与提示词第 4 步一致；name_en 用英文小写名词短语）
   - `nationalities`：1–2 条（含变迁则多条，如「Germany」「Switzerland / United States」分条写主要归属国）
   - `relations`：与提示词第 4.5 步一致。类型白名单：`advisor-student`（direction: `advisor`=对方是导师 / `student`=对方是学生）/ `colleague` / `co-honored`（共享诺奖/沃尔夫等，注明年份与奖项）/ `spouse` / `parent-child` / `rival` / `controversy` / `influence`。**只收 page.md 明载的关系**（frontmatter doctoral_advisor + 正文师生/合作/共同获奖），无载禁写；note 简洁（对方身份/成就/合作背景）
4. **入库**：
   ```bash
   cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/{Dir}.yaml
   ```
   若并发撞字典表唯一键（fields/occupations Duplicate entry），等 2 秒重跑一次即可（幂等）。
5. **验证**：
   ```bash
   cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 -c "
   from db_mysql import get_conn
   conn=get_conn(); cur=conn.cursor()
   cur.execute(\"SELECT id,name_en,has_social_data FROM people WHERE qid='{QID}'\")
   p=cur.fetchone(); print(p)
   cur.execute('SELECT COUNT(*) FROM person_field WHERE person_id=%s',(p[0],)); print('fields:',cur.fetchone()[0])
   cur.execute('SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s',(p[0],p[0])); print('relations:',cur.fetchone()[0])"
   ```
   要求 `has_social_data=1` 且 fields≥4、relations≥3（实在无载者除外，note 说明）。

## 2. 仅关系入库的人（need_prompt=false，共 7 位）

其 {Dir}_zh.md 提示词已存在于成品目录（如 `Antoine_Henri_Becquerel/`），**不要新写提示词**，只做步骤 3–5；yaml 中 `has_biography: true`（Beamer 已完成）。

## 3. 红线与陷阱（历批沉淀）

- yaml `note` 含 `: ` 或以引号开头 → 整体用单引号包裹，否则 YAML 解析失败。
- 对手方人物（导师/学生/合作者）入库为 stub：不给对方编造 qid；对方 name_en 用规范全名，与库内已有记录形式一致（如库内已有 `Eugene Wigner` 就勿用 `Eugene Paul Wigner`）。
- 同名区分：J.J. Thomson vs G.P. Thomson、C.T.R. Wilson vs Kenneth Wilson、Otto Stern 家族等，note 里写清身份。
- 师承方向：frontmatter `doctoral_advisor` 的人 → direction: advisor；正文「他的学生 XXX」→ direction: student。
- 无载禁写：page.md 没写的一律不写（不编造导师、不编造学生、不从诺奖颁奖词反推关系）。
- 中文引号内不写「原话」，除非 page.md 有英文原文。
- **禁止修改** `generate_20th_century_list.py`、名录 md、Physicist_Bio_Prompt_Template.md（主控统一收尾）。

## 4. 汇报

每人完成后向主控 send_message 一行：`✅ {Name} | prompt✅/— | yaml✅ | DB id={id} fields={n} relations={n} | 主色#{hex} BGM{曲名}`。全部完成后再发一条汇总（成功/失败清单）。
