# OpenMathAI 奖项数据维护指南与后续建议

> 汇总 Fields / Wolf / Abel / Chern（数学四大奖）、Turing（图灵奖，计算机）、COPSS Presidents' Award（考普斯会长奖，统计学）以及诺贝尔家族、京都奖、哥德尔奖等交叉荣誉的数据维护规范。
> 本文档记录当前管理决策、数据资产清单与后续增量维护建议。

---

## 一、当前决策（2026-08 确认）

**维持文本 + 脚本管理，不引入数据库。**

评估结论（当时的对比）：
- **继续文本管理**：数据为固定结构化文本（奖项名册、交叉名录、HONORS 字典），增量小、可 `git diff` 逐行 review、验证脚本可复用；与现有生成器（`gen_turing.py` / `gen_turing_beamer.py`）耦合紧密。
- **引入数据库**：收益（查询、去重、关系建模）在当前规模下不显著，且需要新增迁移、同步、生成器改造等成本。
- **结论**：保持现状，用「单一事实来源 + 验证脚本」弥补文本管理的不足。

---

## 二、数据资产清单（单一事实来源）

| 文件 | 作用 | 维护时机 |
|---|---|---|
| `medal_list_allinone/all_cross_reference.md` | **全奖项交叉名录（唯一交叉源）** | 新增/修正交叉荣誉时 |
| `medal_list_allinone/awards_list.md` | 奖项名册 + Wikipedia 链接 | 新增奖项时 |
| `medal_list_allinone/math_awards_tiers.md` | 奖项体系全景分级 | 奖项体系变化时 |
| `medal_list_allinone/laurate_cross.md` | 得主交叉清单 | 与交叉名录同步 |
| `turing/gen_turing.py` | 图灵奖视频生成器（含 `HONORS` 字典） | 图灵视频内容改动时 |
| `medal_list_allinone/turing_beamer/gen_turing_beamer.py` | 「双料与大满贯」beamer 生成器（含 `BADGE_DEFS`） | beamer 视频改动时 |
| `medal_list_allinone/cross_verify.py` | 交叉名录自动核对 | 每次改交叉数据后 |
| `medal_list_allinone/verify_honors.py` | `HONORS` 字典校验 | 每次改 HONORS 后 |
| `medal_list_allinone/fetch_awards_wiki.py` | 奖项 Wikipedia 离线页下载 | 新增奖项时 |
| `medal_list_allinone/extract_laureates.py` / `extract_full_laureates.py` | 得主信息提取 | 数据采集时 |
| `turing/pages/`、`medal_list_allinone/pages/` | 本地离线 Wikipedia 页 | 数据核实时参照 |

> ⚠️ **原则**：所有交叉荣誉以 `all_cross_reference.md` 为唯一事实来源，其余交叉文档（`laurate_cross.md`、`turing_cross_reference.md`）由脚本从它派生，避免多份文档漂移。

---

## 三、后续增量维护建议

### 1. 统一 `winners.md` 模板

各奖项目录（`Fields_Medal/`、`Wolf_Prize/`、`Abel_Prize/`、`Chern_Medal/`、`COPSS/`、`turing/`）的得主名录格式不一致。建议统一为同一模板：

```markdown
| 姓名（中文） | 英文名 | 获奖年份 | 届次 | 国籍 | 机构 | 生卒（享年） | 领域 |
|---|---|---|---|---|---|---|---|
```

- 生卒统一「1922–1990（享年68）」单行格式，避免换行破坏排版；
- 年份统一用「获奖年份」（而非颁奖年份）；
- 统一后可用一个脚本批量校验「年份 / 届次 / 姓名」与 Wikipedia 离线页的一致性。

### 2. 以 `all_cross_reference.md` 为唯一交叉源

- 新增交叉荣誉（如某得主新获京都奖）只改这一份文档；
- 派生文档（`laurate_cross.md`、beamer 数据、`turing_cross_reference.md`）由脚本读取它生成，禁止手工编辑派生文档；
- 生成后跑 `cross_verify.py` 复核。

### 3. 复用验证脚本做增量更新

改任何数据后按顺序执行：

```bash
python3 medal_list_allinone/cross_verify.py     # 交叉名录核对
python3 medal_list_allinone/verify_honors.py    # HONORS 字典校验
python3 turing/gen_turing.py                     # 图灵视频重新生成（如需）
python3 medal_list_allinone/turing_beamer/gen_turing_beamer.py  # beamer 重新生成（如需）
```

> 已知经验：交叉提取匹配失败多因 **Unicode 或中间名**（Sergei→Novikov、Gregory/Grigory、David B. Mumford 等），属正常现象，核对后结论正确即可，不误报为错误。

### 4. beamer 视频排版微调注意事项

- **编译**：beamer 用 XeLaTeX 编译两遍；若 `latexmk` 卡死，改用 `timeout 180 xelatex -interaction=nonstopmode` 两遍；
- **清理**：用 `latexmk -c <main>.tex` 清理中间文件，**不要用 `rm -f *.aux *.log`**（会触发 IDE 危险命令确认框）；
- **徽标**：`badge` 用 `\raisebox{0.55ex}{\tiny\color{...}...}`，避免 `\textsuperscript` 触发 15.4pt 数学字体缺失警告；
- **空值判断**：honorbar 用 `\gdef\personhonors` + `\detokenize\expandafter`（注意放 slide 宏内部，勿放序言，否则会被全局覆盖）；
- **`\edef` 展开 `\color` 会导致 xelatex 卡死** → 用惰性参数；
- 生卒年 / 国籍与机构之间出现过间隔过大问题 → 已通过列宽与单行格式修复，后续改动保持「生卒单行、不换行」；
- 主要荣誉若换行，需「标题单独一行、内容下一行、每个荣誉占一行」，并注意与上方元素间距。

### 5. 数据核实工作流

- 优先使用本地离线 Wikipedia 页（`turing/pages/`、`medal_list_allinone/pages/`）交叉验证，不依赖网络；
- 无独立页的奖项（如 Dijkstra Prize 重定向 PODC、C. R. Rao 等）→ 脚本回退到人物页/总页，并在 metadata 注明；
- 新增奖项时：先在 `awards_list.md` 登记（含 Wikipedia 链接）→ `fetch_awards_wiki.py` 下载离线页 → 再更新交叉名录。

### 6. 编译与提交流程（沿用现有惯例）

1. 改生成器（`.py`）→ 重新生成 `.tex`；
2. XeLaTeX 编译两遍 → `pdftoppm` 渲染 PNG 预览 → 用户确认；
3. 用户确认后 `git add` 提交（提交前检查 `mathematician/` 目录不被误包含）；
4. 提交内容通常包含：生成器脚本、对应 `.tex`、`all_cross_reference.md` / `awards_list.md` 等 md、校准头像图片。

---

## 四、待办 / 可选优化

- [ ] 统一各奖项目录的 `winners.md` 模板（见「三、1」）；
- [ ] 将 `laurate_cross.md`、`turing_cross_reference.md` 改为从 `all_cross_reference.md` 自动派生；
- [ ] 为「交叉名录 + 得主信息」写一个聚合校验脚本（合并 `cross_verify.py` 与 `verify_honors.py` 的功能）；
- [ ] beamer 双料与大满贯视频的封面/总结帧布局再微调（列宽、生卒单行已做，可继续按预览效果迭代）。
