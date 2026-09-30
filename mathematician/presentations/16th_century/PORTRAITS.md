# PORTRAITS — 16 世纪 14 位数学家肖像核实结论（主控，2026-09-29）

> 核实方法：`https://en.wikipedia.org/api/rest_v1/page/summary/<title>` 取条目首图（originalimage），
> 并结合各人 `pages/<Name>/page.html` 图注与 `images.txt` 交叉核对。
> **以本文件为准**：标「无肖像」者一律用装饰圆 `\faIcon{user}` 占位，禁止拿书影 / 雕像 / 纪念碑 / 文献扉页冒充头像。
> 下载（500px 缩略图，可直接 curl；失败时改 `https://commons.wikimedia.org/wiki/Special:FilePath/<文件名>?width=600`）：
> ```bash
> curl -sL -A "Mozilla/5.0" -o "images/<x>_portrait.jpg" "<URL>" && file "images/<x>_portrait.jpg"
> ```

## 结论表

| # | 人物 | 目录 | 肖像 | 文件名 |
|:--:|------|------|:--:|------|
| 1 | 德尔·费罗 | `1465–Scipione_del_Ferro` | 有（2026-09-30 用户补充，非 REST 来源） | `ferro_portrait.jpg` |
| 2 | 塔尔塔利亚 | `1500–Niccolò_Tartaglia` | 有 | `tartaglia_portrait.jpg` |
| 3 | 卡尔达诺 | `1501–Gerolamo_Cardano` | 有 | `cardano_portrait.jpg` |
| 4 | 努内斯 | `1502–Pedro_Nunes` | 有 | `nunes_portrait.png` |
| 5 | 科门迪诺 | `1509–Federico_Commandino` | 有 | `commandino_portrait.jpg` |
| 6 | 雷科德 | `1512–Robert_Recorde` | **无** | 装饰圆占位 |
| 7 | 费拉里 | `1522–Lodovico_Ferrari` | **无** | 装饰圆占位 |
| 8 | 邦贝利 | `1526–Rafael_Bombelli` | **无** | 装饰圆占位 |
| 9 | 克拉维乌斯 | `1538–Christopher_Clavius` | 有 | `clavius_portrait.jpg` |
| 10 | 韦达 | `1540–François_Viète` | 有 | `viete_portrait.jpg` |
| 11 | 斯蒂文 | `1548–Simon_Stevin` | 有 | `stevin_portrait.jpg` |
| 12 | 纳皮尔 | `1550–John_Napier` | 有 | `napier_portrait.jpg` |
| 13 | 哈里奥特 | `1560–Thomas_Harriot` | 有（★ 须加「传为」） | `harriot_portrait.jpg` |
| 14 | 布里格斯 | `1561–Henry_Briggs` | 有 | `briggs_portrait.jpg` |

## URL 明细与图注建议

### 1. 德尔·费罗（Scipione del Ferro）— 2026-09-30 补录
- 来源：**用户提供** `images/Scipione del Ferro.jpeg`（273×320），主控用 `sips -s format jpeg -s dpiHeight 72 -s dpiWidth 72` 转存为 `images/ferro_portrait.jpg`，原文件已移出工作区。非 REST/Commons 来源，故不在上表 URL 之列。
- 图注：封面写短形式 `Scipione del Ferro`（4.8pt，防右侧越界），身份信息页写 `Scipione del Ferro（1465–1526）`。
- 口径：传世无确证的同时代肖像，此为后世版画像性质——图注只写姓名，**不写「同时代肖像」**。

### 2. 塔尔塔利亚（Niccolò Tartaglia）
- URL：`https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Portret_van_Niccolo_Tartaglia_Nicolavs_Tartaglia_Brixianvs_%28titel_op_object%29_Portretten_van_beroemde_Europese_geleerden_%28serietitel%29_Virorum_doctorum_de_Disciplinis_benemerentium_effigies_%28serietitel%29%2C_RP-P-1909-4459.jpg/500px-Portret_van_Niccolo_Tartaglia_Nicolavs_Tartaglia_Brixianvs_%28titel_op_object%29_Portretten_van_beroemde_Europese_geleerden_%28serietitel%29_Virorum_doctorum_de_Disciplinis_benemerentium_effigies_%28serietitel%29%2C_RP-P-1909-4459.jpg`
- 图注：`Niccolò Tartaglia（版画像，Rijksmuseum 藏）`

### 3. 卡尔达诺（Gerolamo Cardano）
- URL：`https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Girolamo_Cardano._Stipple_engraving_by_R._Cooper._Wellcome_V0001004.jpg/500px-Girolamo_Cardano._Stipple_engraving_by_R._Cooper._Wellcome_V0001004.jpg`
- 图注：`R. Cooper 点刻版画（Wellcome Collection V0001004）`

### 4. 努内斯（Pedro Nunes）
- URL：`https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Pedro_Nunes.png/500px-Pedro_Nunes.png`
- 图注：`Pedro Nunes 像（1843 年 Panorama 杂志所刊）`
- 备选（纪念碑雕像，**只能当插图不可当头像**）：`https://thumb.wikimedia.org/wikipedia/commons/thumb/a/ad/Pedro_Nunes_April_2009-1a.jpg/500px-Pedro_Nunes_April_2009-1a.jpg`

### 5. 科门迪诺（Federico Commandino）
- URL：`https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Federico_Commandino.jpg/500px-Federico_Commandino.jpg`
- 图注：`Federico Commandino（传世版画像）`

### 9. 克拉维乌斯（Christopher Clavius）
- URL：`https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Portret_van_astronoom_Christoph_Clavius%2C_RP-P-OB-38.439_%28cropped%29.jpg/500px-Portret_van_astronoom_Christoph_Clavius%2C_RP-P-OB-38.439_%28cropped%29.jpg`
- 图注：`Clavius 版画像（Rijksmuseum 藏 RP-P-OB-38.439）`

### 10. 韦达（François Viète）
- URL：`https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Francois_Viete.jpg/500px-Francois_Viete.jpg`
- 图注：`François Viète（后世版画像）`

### 11. 斯蒂文（Simon Stevin）
- URL：`https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Simon-stevin.jpeg/500px-Simon-stevin.jpeg`
- 图注：`Simon Stevin（传世版画像）`

### 12. 纳皮尔（John Napier）
- URL：`https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/John_Napier_of_Merchiston%2C_1616.jpg/500px-John_Napier_of_Merchiston%2C_1616.jpg`
- 图注：`John Napier of Merchiston，1616 年肖像`

### 13. 哈里奥特（Thomas Harriot）
- URL：`https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/ThomasHarriot.jpg/500px-ThomasHarriot.jpg`
- 图注：**必须**写 `传为 Thomas Harriot（1602 年像，Trinity College, Oxford 藏）`
- 依据：条目图注原文 "Portrait often claimed to be Thomas Harriot (1602) ... The provenance of this portrait is not known, and there is little evidence to link it to Harriot."

### 14. 布里格斯（Henry Briggs）
- URL：`https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Henry-Briggs.jpg/500px-Henry-Briggs.jpg`
- 图注：`John Faber Jr 依 Isaac Seeman 所作 1738 年美柔汀版画（英国国家肖像馆藏）`

## 无肖像三人（装饰圆占位，图注写「无存世肖像」或对应依据）

> 原为 4 人；德尔·费罗已于 2026-09-30 由用户补充版画像 `ferro_portrait.jpg`（273×320，非 REST/Commons 来源，传世无确证同期肖像，图注只写姓名），转入「有肖像」名单。

| 人物 | 依据 |
|---|---|
| 雷科德 | REST 首图为威尔士 Tenby 圣玛丽教堂纪念碑照片（234×276），非肖像；`page.md` 无肖像 |
| 费拉里 | 唯一图为 Tartaglia《Terza risposta》（1547）檄文封面，非肖像 |
| 邦贝利 | 仅《代数》1572/1579 书影与扉页，非肖像 |
