# OpenPeace 提示词撰写 + 研究领域/社会关系入库工作流（21 世纪批次，2026-09-29）

> 本文档是诺贝尔和平奖 **21 世纪（2001–2025，36 位，含 12 个组织机构）** 批次的共享工作流。
> 与 20 世纪流程（`peace/PROMPTS_WORKFLOW.md`）完全一致，仅以下差异，20 世纪文档其余条款（红线/引号规则/无载禁写等）全部适用。

## 0. 路径差异

| 资产 | 路径 |
|------|------|
| 分批清单 | `peace/prompt_manifest_21.json`（batch 1–8） |
| 每人数据源 | `peace/presentations/pages/21th_century/{Dir}/page.md` |
| 提示词落盘 | `peace/presentations/21th_century/{Dir}/{Dir}_zh.md` |
| 名录（理由中译照抄） | `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` |
| yaml / 入库 / 验证 | 与 20 世纪相同（`MySQL/data/{Dir}.yaml` + `MySQL/seed_person.py`） |
| 结构标杆 / yaml 母本 | 同 20 世纪（Kenneth_G_Wilson_zh.md / Frederick_Sanger.yaml） |

## 1. ★ 21 世纪专属红线（政治敏感，必须严格执行）

- **2010 刘晓波**：只写获奖事实（年份、官方获奖理由 EN+中译、"狱中无法领奖、颁奖典礼上空座椅"等 page.md 明载事实）；**不写判决书内容细节、不写任何政治评价与呼吁**；关系仅收 page.md 明载者（如 spouse 刘霞），慎之又慎。
- **2022 三人组（白俄罗斯/俄罗斯/乌克兰）**：战争相关内容全部按 page.md 客观事实记录，不作立场表述。
- **2023 伊朗、2025 委内瑞拉**：国内局势仅客观事实，无评价。
- 2009 奥巴马：获奖争议（"为承诺而奖"）按 page.md 两说并陈。
- 涉及当代政治人物（普京/特朗普/内塔尼亚胡等）一律不作评价性语句。

## 2. 其他差异

- 组织机构 12 个：UN(2001)、IAEA(2005)、Grameen Bank(2006)、IPCC(2007)、EU(2012)、OPCW(2013)、突尼斯四方机制(2015)、ICAN(2017)、WFP(2020)、Memorial(2022)、公民自由中心(2022)、Nihon Hidankyo(2024)。按 20 世纪工作流第 2 节机构规则执行（省 gender/nationalities、birth_date 用成立年、机构概览页替代身份信息页）。
- 库内 stub 复用 5 个（manifest 已标 db_id）：United Nations(6777)、Kofi Annan(7347)、Jimmy Carter(7114)、Shirin Ebadi(6763)、ICAN(6808)——yaml `name_en` 沿用 db_name_en，UPD 回填 QID。
- 20 世纪批次为 21 世纪预建的 stub：Shirin Ebadi(6763)、Wangari Maathai(6764)（Jody Williams 的 Nobel Women's Initiative 同侪边）等，UPD 复用勿新建。
- 同批互引：共享年份得主互写 co-honored（2005 IAEA↔ElBaradei、2006 Yunus↔Grameen、2007 IPCC↔Gore、2011 三人组两两、2014 Satyarthi↔Malala、2018 Mukwege↔Murad、2021 Ressa↔Muratov、2022 三人组两两）。
- 2011 三人组（Sirleaf/Gbowee/Karman）理由为共享句；2014/2018/2021/2022 同理，注意 citation 主语 "their"。

## 3. 汇报

每人完成后向主控 send_message 一行：
`✅ {Name} | prompt✅ | yaml✅ | DB id={id} fields={n} relations={n} | 主色{hex} BGM{曲名}`。
全部完成后再发一条汇总（成功/失败清单 + 关键裁定 + 分裂 stub 自查结果）。
