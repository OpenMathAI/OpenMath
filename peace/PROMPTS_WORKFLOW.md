# OpenPeace 提示词撰写 + 研究领域/社会关系入库工作流（2026-09-29 批次）

> 本文档是诺贝尔和平奖得主（20 世纪 104 位，含 16 个组织机构）批量
> 「人物专属立传提示词撰写 + 研究领域与社会关系入库」的共享工作流。
> 所有执行 agent 必读本文档 + 自己的 `peace/prompt_manifest.json` 对应 batch，然后逐人执行。

## 0. 路径与数据源（全部绝对路径，OpenMathAI 根 = `/Users/ericksun/workspace/codebuddy/OpenMathAI`）

| 资产 | 路径 |
|------|------|
| 分批清单 | `peace/prompt_manifest.json`（batch 1–21，member 含 page_md/prompt_md/yaml 相对 OpenMathAI 根的路径、qid、is_org、need_prompt/need_relations、主色、BGM） |
| 每人数据源 | `peace/presentations/pages/20th_century/{Dir}/page.md`（Wikipedia 全文 + frontmatter：wikidata QID / 生卒 / 国籍 / 职业 / award_received / educated_at 等） |
| 结构标杆 | `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（★ 0–11 节结构母本，照此结构） |
| yaml 标杆 | `MySQL/data/Frederick_Sanger.yaml`（★ 字段母本） |
| 名录 | `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md`（官方获奖理由中译在此） |
| 入库引擎 | `MySQL/seed_person.py`（幂等；按 QID → name_en 匹配人物） |
| BGM 曲库 | `music_audio/curated_tracks.md`（每人曲目已在 manifest 预分配，勿改） |

## 1. 每人执行步骤

1. **通读** 该人 `page.md`（先 frontmatter + infobox + 导语，再正文各节；长文可分段读，但早年/主要活动/获奖/晚年各节必须覆盖），建立事实基准。
2. **撰写人物专属提示词** → `peace/presentations/20th_century/{Dir}/{Dir}_zh.md`，190–230 行，结构对齐标杆（Kenneth_G_Wilson_zh.md 的一~五节）：
   - 一、模板定位（1-2 句：OpenPeace 项目 + 本人物 + 设计哲学）
   - 二、背景信息【人物专属】：姓名（中英）、生卒、诺奖年份与**官方获奖理由英文原文+中译**（照抄名录 `OpenPeace_20th_Century_Nobel_Laureates.md`，禁止改写）、气质关键词（3 个短语）、设计母题（贴合其和平事业的视觉概念）、本地数据源路径（指向 `peace/presentations/pages/20th_century/{Dir}/page.md`）
   - 三、任务流程第 0–9 步【模板通用骨架 + 人物专属内容】：
     - 第 0 步：事实基准——生卒（含享年）、国籍（含变迁）、家庭、教育（学校/专业/年份）、任职机构（含年份）、关键荣誉（含年份）、核心事业清单（4–6 条）、关键时间线（15–20 节点）
     - 第 4 步：研究领域/事业领域表（4–5 行：rank/name_en/中文/说明/对应页；name_en 用英文小写名词短语，如 `peace education`、`international arbitration`、`humanitarian aid`）
     - 第 4.5 步：社会关系表（与 yaml 完全一致）
     - 第 5 步：配色方案（manifest 预分配主色 hex + 诺奖香槟金 `C9A227` + badgeA–D 四分类色；勿改主色）
     - 第 6 步：幻灯片序列（10–16 页规划，含身份信息页★必做；组织机构改为「机构概览页」）
     - 第 7–8 步：版式要点 + 该人专属陷阱表（归属争议/易错年份/同名区分/无载禁写清单）
     - 第 9 步：术语清单（英文/中文/风险点，8–12 条）
   - 四、BGM：manifest 预分配曲目（写曲名 + 匹配理由 + bgm_path）
3. **撰写 yaml** → `MySQL/data/{Dir}.yaml`（字段母本 = Frederick_Sanger.yaml）：
   - `name_en`：用 manifest 的 `name` 字段（DATA 规范名）；若 manifest `db_name_en` 非空，**沿用 db_name_en**（库内既有记录）
   - `qid`：manifest 的 qid
   - `name_zh` / `birth_date` / `death_date` / `description`：来自 frontmatter 与名录；在世者 `death_date` 省略
   - `gender`：male/female（组织机构省略）
   - `primary_occupation`：按主业英文小写（politician / lawyer / diplomat / peace activist / humanitarian / journalist / economist / clergyman 等；**组织机构**用 `peace organization` / `humanitarian organization` / `un agency` 等）
   - `has_biography: false`（本批均未做 Beamer）
   - `occupations`：1–3 条（主业 rank 0 + page.md 明载的其他职业）
   - `fields`：4–5 条（与提示词第 4 步一致）
   - `nationalities`：1–2 条（含变迁则多条；组织机构省略 nationalities）
   - `relations`：与提示词第 4.5 步一致。类型白名单：`advisor-student`（direction: `advisor`=对方是导师 / `student`=对方是学生）/ `colleague` / `co-honored`（共享诺奖，注明年份）/ `spouse` / `parent-child` / `rival` / `controversy` / `influence` / `founder`（创始人→机构）。**只收 page.md 明载的关系**，无载禁写；note 简洁
4. **入库**：
   ```bash
   cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/{Dir}.yaml
   ```
   并发撞字典表唯一键（fields/occupations Duplicate entry）时等 2 秒重跑一次（幂等）。
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
   要求 `has_social_data=1` 且 fields≥4、relations≥2（实在无载者除外，note 说明）。

## 2. 组织机构特别规则（manifest `is_org: true` 的 16 个）

- yaml：省略 `gender` / `nationalities`；`primary_occupation` 用机构性质；`birth_date` 用成立年份所在年（格式 `YYYY` 或忽略，page.md 明载成立日期才写 `YYYY-MM-DD`）
- `fields` = 使命领域（humanitarian aid / international law / disarmament / peace education 等 4–5 条）
- `relations`：
  - 创始人/缔造者 → `type: founder`（如 Henry Dunant → 红十字国际委员会）
  - 同年共同得主 → `type: co-honored`
  - page.md 明载的继承/前身机构关系 → `type: other`（note 写清「前身/继承」）
  - 与联合国体系的关系（如 UNICEF 是联合国机构）→ `type: other`
  - 知名首任领导人若 page.md 明载且关系紧密 → `type: colleague`
- 提示词：第 6 步机构概览页替代身份信息页；陷阱表写「勿把机构领导人写成创始人」等

## 3. 红线与陷阱（历批沉淀，必须遵守）

- yaml `note` 含 `: ` 或以引号开头 → 整体用单引号包裹，否则 YAML 解析失败。
- 对手方人物（导师/学生/共同得主/创始人）name_en 一律用 **manifest 的 `name` 字段（DATA 规范名）**，与库内已有记录形式一致时用库内形式（先 `SELECT id,name_en FROM people WHERE name_en LIKE '%关键词%'` 查重）；不给对方编造 qid。
- 师承方向：frontmatter `doctoral_advisor` 的人 → direction: advisor；正文「他的学生 XXX」→ direction: student。
- 无载禁写：page.md 没写的一律不写（不编造导师、不编造学生、不从诺奖颁奖词反推关系）。
- 中文引号内不写「原话」，除非 page.md 有英文原文。
- **政治敏感红线**：涉及宗教、领土、主权、当代政治评价的内容一律只作 page.md 明载的客观事实性记录，不加任何评价性语句；1989 达赖喇嘛条目只写「1989 获诺贝尔和平奖、获奖理由」等事实，禁写任何政治背景与评价。
- **禁止修改** `peace/generate_peace_list.py`、名录 md、`peace/peace_list_data.py`、`peace/build_manifest.py`（主控统一收尾）。
- 同一批内共享年份的得主（如 1901 Dunant+Passy）互写 `co-honored`；对方 name_en 用 manifest `name` 字段。

## 4. 汇报

每人完成后向主控 send_message 一行：
`✅ {Name} | prompt✅ | yaml✅ | DB id={id} fields={n} relations={n} | 主色{hex} BGM{曲名}`。
全部完成后再发一条汇总（成功/失败清单）。
