#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 nobel_literature_citations.json 读取 20 世纪诺贝尔文学奖得主（含获奖理由），
参考物理学家侧文档形式，生成含「获奖理由 / 立传 / Review / 社会关系入库」列的结构化 md。

先运行 fetch_nobel_citations.py 生成 nobel_literature_citations.json，再运行本脚本。
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "nobel_literature_citations.json"
OUT = ROOT / "presentations" / "20th_century" / "OpenLiterature_20th_Century_Nobel_Laureates.md"

# 已立传的文学家（姓名需与获奖者名单精确匹配）。
# 新增立传时在此补充姓名。
BIOGRAPHIES_DONE: set[str] = set()

# 已完成 Review（两轮事实核查）的文学家（姓名需与获奖者名单精确匹配）。
REVIEWS_DONE: set[str] = set()

# 已完成社会关系入库（研究领域 + 社会关系写入 greatminds 库）的文学家。
# 2026-09-29 批次（lit-bios-2026，20 批 agent）已全部入库，此处按 citations json 自动取全集。
def _relations_done() -> set[str]:
    try:
        data = json.loads((ROOT / "nobel_literature_citations.json").read_text(encoding="utf-8"))
        return {r["name"] for r in data if r.get("year") and r["year"] <= 2000}
    except Exception:
        return set()

RELATIONS_DONE: set[str] = _relations_done()

# 获奖者英文名 → 中文名（诺贝尔文学奖得主常用中译）。
NAME_ZH = {
    "Sully Prudhomme": "苏利·普吕多姆",
    "Theodor Mommsen": "特奥多尔·蒙森",
    "Bjørnstjerne Bjørnson": "比昂斯滕·比昂松",
    "Frédéric Mistral": "弗雷德里克·米斯特拉尔",
    "José Echegaray": "何塞·埃切加赖",
    "Henryk Sienkiewicz": "亨利克·显克维支",
    "Giosuè Carducci": "乔苏埃·卡尔杜齐",
    "Rudyard Kipling": "拉迪亚德·吉卜林",
    "Rudolf Christoph Eucken": "鲁道夫·克里斯托弗·奥伊肯",
    "Selma Lagerlöf": "塞尔玛·拉格洛夫",
    "Paul von Heyse": "保尔·海泽",
    "Maurice Maeterlinck": "莫里斯·梅特林克",
    "Gerhart Hauptmann": "格哈特·豪普特曼",
    "Rabindranath Tagore": "拉宾德拉纳特·泰戈尔",
    "Romain Rolland": "罗曼·罗兰",
    "Verner von Heidenstam": "韦尔纳·冯·海登斯塔姆",
    "Karl Adolph Gjellerup": "卡尔·阿道夫·耶勒鲁普",
    "Henrik Pontoppidan": "亨利克·蓬托皮丹",
    "Carl Spitteler": "卡尔·施皮特勒",
    "Knut Hamsun": "克努特·汉姆生",
    "Anatole France": "阿纳托尔·法朗士",
    "Jacinto Benavente": "哈辛特·贝纳文特",
    "William Butler Yeats": "威廉·巴特勒·叶芝",
    "Władysław Reymont": "弗瓦迪斯瓦夫·雷蒙特",
    "George Bernard Shaw": "萧伯纳",
    "Grazia Deledda": "格拉齐亚·黛莱达",
    "Henri Bergson": "亨利·柏格森",
    "Sigrid Undset": "西格丽德·温塞特",
    "Thomas Mann": "托马斯·曼",
    "Sinclair Lewis": "辛克莱·刘易斯",
    "Erik Axel Karlfeldt": "埃里克·阿克塞尔·卡尔费尔德",
    "John Galsworthy": "约翰·高尔斯华绥",
    "Ivan Bunin": "伊万·蒲宁",
    "Luigi Pirandello": "路伊吉·皮兰德娄",
    "Eugene O'Neill": "尤金·奥尼尔",
    "Roger Martin du Gard": "罗歇·马丁·杜·加尔",
    "Pearl Buck": "赛珍珠",
    "Frans Eemil Sillanpää": "弗兰斯·埃米尔·西兰帕",
    "Johannes Vilhelm Jensen": "约翰内斯·威廉·延森",
    "Gabriela Mistral": "加夫列拉·米斯特拉尔",
    "Hermann Hesse": "赫尔曼·黑塞",
    "André Gide": "安德烈·纪德",
    "Thomas Stearns Eliot": "托马斯·斯特恩斯·艾略特",
    "William Faulkner": "威廉·福克纳",
    "Bertrand Russell": "伯特兰·罗素",
    "Pär Lagerkvist": "帕尔·拉格奎斯特",
    "François Mauriac": "弗朗索瓦·莫里亚克",
    "Winston Churchill": "温斯顿·丘吉尔",
    "Ernest Hemingway": "欧内斯特·海明威",
    "Halldór Laxness": "哈尔多尔·拉克斯内斯",
    "Juan Ramón Jiménez": "胡安·拉蒙·希梅内斯",
    "Albert Camus": "阿尔贝·加缪",
    "Boris Pasternak": "鲍里斯·帕斯捷尔纳克",
    "Salvatore Quasimodo": "萨瓦多尔·夸西莫多",
    "Saint-John Perse": "圣琼·佩斯",
    "Ivo Andrić": "伊沃·安德里奇",
    "John Steinbeck": "约翰·斯坦贝克",
    "Giorgos Seferis": "乔治·塞菲里斯",
    "Jean-Paul Sartre": "让-保罗·萨特",
    "Mikhail Sholokhov": "米哈伊尔·肖洛霍夫",
    "Shmuel Yosef Agnon": "萨缪尔·约瑟夫·阿格农",
    "Nelly Sachs": "内莉·萨克斯",
    "Miguel Ángel Asturias": "米格尔·安赫尔·阿斯图里亚斯",
    "Yasunari Kawabata": "川端康成",
    "Samuel Beckett": "塞缪尔·贝克特",
    "Aleksandr Solzhenitsyn": "亚历山大·索尔仁尼琴",
    "Pablo Neruda": "巴勃罗·聂鲁达",
    "Heinrich Böll": "海因里希·伯尔",
    "Patrick White": "帕特里克·怀特",
    "Eyvind Johnson": "埃温德·约翰逊",
    "Harry Martinson": "哈里·马丁松",
    "Eugenio Montale": "欧金尼奥·蒙塔莱",
    "Saul Bellow": "索尔·贝娄",
    "Vicente Aleixandre": "维森特·阿莱克桑德雷",
    "Isaac Bashevis Singer": "艾萨克·巴什维斯·辛格",
    "Odysseas Elytis": "奥季修斯·埃利蒂斯",
    "Czesław Miłosz": "切斯瓦夫·米沃什",
    "Elias Canetti": "埃利亚斯·卡内蒂",
    "Gabriel García Márquez": "加夫列尔·加西亚·马尔克斯",
    "William Golding": "威廉·戈尔丁",
    "Jaroslav Seifert": "雅罗斯拉夫·塞弗尔特",
    "Claude Simon": "克洛德·西蒙",
    "Wole Soyinka": "沃莱·索因卡",
    "Joseph Brodsky": "约瑟夫·布罗茨基",
    "Naguib Mahfouz": "纳吉布·马哈福兹",
    "Camilo José Cela": "卡米洛·何塞·塞拉",
    "Octavio Paz": "奥克塔维奥·帕斯",
    "Nadine Gordimer": "纳丁·戈迪默",
    "Derek Walcott": "德里克·沃尔科特",
    "Toni Morrison": "托妮·莫里森",
    "Kenzaburō Ōe": "大江健三郎",
    "Seamus Heaney": "谢默斯·希尼",
    "Wisława Szymborska": "维斯瓦娃·辛波丝卡",
    "Dario Fo": "达里奥·福",
    "José Saramago": "若泽·萨拉马戈",
    "Günter Grass": "君特·格拉斯",
    "Gao Xingjian": "高行健",
}

# 官方获奖理由中译（key = (年份字符串, 姓名)，共享奖年份各人理由不同）。
CITATION_ZH = {
    ("1901", "Sully Prudhomme"): "表彰其诗作展现出崇高的理想主义与艺术上的完美，并罕见地兼具心灵与智慧两种品质",
    ("1902", "Theodor Mommsen"): "表彰其为当今最伟大的历史写作艺术大师，尤以其巨著《罗马史》为代表",
    ("1903", "Bjørnstjerne Bjørnson"): "表彰其高贵、宏伟而多样的诗歌，始终以灵感的清新与精神的罕见纯粹著称",
    ("1904", "Frédéric Mistral"): "表彰其诗作的新颖独创与真切灵感，忠实反映了其民族的自然风光与本土精神；并表彰其作为普罗旺斯语文学家的杰出工作",
    ("1904", "José Echegaray"): "表彰其大量辉煌的创作，以个人化而独创的方式复兴了西班牙戏剧的伟大传统",
    ("1905", "Henryk Sienkiewicz"): "表彰其作为史诗作家的杰出功绩",
    ("1906", "Giosuè Carducci"): "不仅因其深厚的学识与批判性研究，更致敬其诗歌杰作所体现的创造力、清新风格与抒情力量",
    ("1907", "Rudyard Kipling"): "表彰这位举世闻名作家作品中展现的观察力、独创的想象力、思想的活力与非凡的叙事才能",
    ("1908", "Rudolf Christoph Eucken"): "表彰其对真理的热切求索、深邃的思想力与开阔的视野，以及在众多著作中以温暖而有力的表述捍卫并发展理想主义人生哲学",
    ("1909", "Selma Lagerlöf"): "表彰其作品所体现的崇高理想主义、生动的想象力与心灵的洞见",
    ("1910", "Paul von Heyse"): "致敬其在漫长创作生涯中，作为抒情诗人、剧作家、小说家与世界闻名的短篇小说家所展现的渗透理想主义的圆熟艺术",
    ("1911", "Maurice Maeterlinck"): "表彰其多方面的文学活动，尤以其戏剧著作为最——想象力丰富、诗意盎然，时而以童话的面貌传达深刻灵感，以神秘的方式触动读者的情感并激发其想象",
    ("1912", "Gerhart Hauptmann"): "主要表彰其在戏剧艺术领域丰硕、多样而杰出的创作",
    ("1913", "Rabindranath Tagore"): "因其诗意深邃、清新而美丽，并以高超的技巧使其以英文表达的诗思成为西方文学的一部分",
    ("1915", "Romain Rolland"): "表彰其文学作品中的崇高理想主义，以及其描写各类人物时所怀有的同情心与对真理的热爱",
    ("1916", "Verner von Heidenstam"): "表彰其作为我们文学新时代主要代表的意义",
    ("1917", "Karl Adolph Gjellerup"): "表彰其受崇高理想启迪的多样而丰富的诗歌",
    ("1917", "Henrik Pontoppidan"): "表彰其对当代丹麦生活的真实描写",
    ("1919", "Carl Spitteler"): "特别表彰其史诗《奥林匹斯的春天》",
    ("1920", "Knut Hamsun"): "表彰其不朽巨著《大地的生长》",
    ("1921", "Anatole France"): "表彰其辉煌的文学成就，以风格的高贵、深切的人类同情、优雅与真正的高卢气质为特征",
    ("1922", "Jacinto Benavente"): "表彰其以精妙的方式延续了西班牙戏剧的辉煌传统",
    ("1923", "William Butler Yeats"): "表彰其始终充满灵感的诗歌，以高度艺术化的形式表达了整个民族的精神",
    ("1924", "Władysław Reymont"): "表彰其伟大的民族史诗《农民》",
    ("1925", "George Bernard Shaw"): "表彰其作品兼具理想主义与人道主义，其犀利的讽刺常浸润着独特的诗意之美",
    ("1926", "Grazia Deledda"): "表彰其理想主义启迪下的写作，以鲜明的笔触描绘故乡岛屿的生活，并以深度与同情处理普遍的人类问题",
    ("1927", "Henri Bergson"): "表彰其丰富而有生命力的思想，以及阐述这些思想的辉煌技巧",
    ("1928", "Sigrid Undset"): "主要表彰其对中世纪北方生活的有力描写",
    ("1929", "Thomas Mann"): "主要表彰其伟大小说《布登勃洛克一家》，该书已被稳步公认为当代文学的经典之作",
    ("1930", "Sinclair Lewis"): "表彰其强劲而生动的描写艺术，以及以机智与幽默创造新型人物的能力",
    ("1931", "Erik Axel Karlfeldt"): "埃里克·阿克塞尔·卡尔费尔德的诗歌",
    ("1932", "John Galsworthy"): "表彰其卓越的叙事艺术，其最高成就体现于《福尔赛世家》",
    ("1933", "Ivan Bunin"): "表彰其以严谨的艺术性承续俄国古典散文写作的传统",
    ("1934", "Luigi Pirandello"): "表彰其大胆而巧妙地复兴了戏剧与舞台艺术",
    ("1936", "Eugene O'Neill"): "表彰其戏剧作品的力量、真诚与深切情感，体现了独创的悲剧观念",
    ("1937", "Roger Martin du Gard"): "表彰其小说系列《蒂博一家》以艺术的力量与真实描绘了人的冲突以及当代生活的某些基本面貌",
    ("1938", "Pearl Buck"): "表彰其对中国农民生活的丰富而真正的史诗式描写，以及其传记性的杰作",
    ("1939", "Frans Eemil Sillanpää"): "表彰其对本国农民的深刻理解，以及描绘他们的生活方式及其与自然之关系的精湛艺术",
    ("1944", "Johannes Vilhelm Jensen"): "表彰其诗歌想象力的罕见力量与丰饶，兼有广博的求知欲与大胆而清新的创造性风格",
    ("1945", "Gabriela Mistral"): "表彰其由强烈情感所激发的抒情诗，使其名字成为整个拉丁美洲世界理想主义抱负的象征",
    ("1946", "Hermann Hesse"): "表彰其富于灵感的写作，在胆识与洞察力不断深化的同时，体现了古典的人道主义理想与高超的风格",
    ("1947", "André Gide"): "表彰其广博而具艺术意义的写作，以无畏的爱真理之心与敏锐的心理洞察呈现人的问题与处境",
    ("1948", "Thomas Stearns Eliot"): "表彰其对当代诗歌的杰出开创性贡献",
    ("1949", "William Faulkner"): "表彰其对现代美国小说有力而在艺术上独树一帜的贡献",
    ("1950", "Bertrand Russell"): "表彰其多样而重要的著述，在其中他捍卫人道主义理想与思想自由",
    ("1951", "Pär Lagerkvist"): "表彰其在诗歌中力求回答人类面临的永恒问题时所展现的艺术活力与真正独立的精神",
    ("1952", "François Mauriac"): "表彰其小说深入人生之戏剧所体现的精神洞察与艺术强度",
    ("1953", "Winston Churchill"): "表彰其对历史与传记描述的精湛掌握，以及捍卫崇高人类价值的辉煌演说",
    ("1954", "Ernest Hemingway"): "表彰其叙事艺术的精湛，近作《老人与海》尤为明证；并表彰其对当代文风的影响",
    ("1955", "Halldór Laxness"): "表彰其生动的史诗力量，更新了冰岛伟大的叙事艺术",
    ("1956", "Juan Ramón Jiménez"): "表彰其抒情诗，以西班牙语构成崇高精神与艺术纯粹的典范",
    ("1957", "Albert Camus"): "表彰其重要的文学创作，以清明的认真态度照亮我们时代人类良知的问题",
    ("1958", "Boris Pasternak"): "表彰其在当代抒情诗与伟大的俄罗斯史诗传统领域的重要成就",
    ("1959", "Salvatore Quasimodo"): "表彰其抒情诗，以古典的火焰表达我们时代生活的悲剧性经验",
    ("1960", "Saint-John Perse"): "表彰其诗歌的高扬气势与引人遐想的意象，以先知般的方式反映我们时代的境况",
    ("1961", "Ivo Andrić"): "表彰其史诗般的力量，从其国家的历史中提炼主题并描绘人类命运",
    ("1962", "John Steinbeck"): "表彰其现实主义与想象性兼备的写作，将同情的幽默与敏锐的社会洞察融为一体",
    ("1963", "Giorgos Seferis"): "表彰其杰出的抒情写作，由对希腊文化世界的深厚感情所激发",
    ("1964", "Jean-Paul Sartre"): "表彰其思想丰富、充满自由精神与求真意志的著作，对我们时代产生了深远影响",
    ("1965", "Mikhail Sholokhov"): "表彰其《静静的顿河》史诗所展现的艺术力量与完整性，表达了俄罗斯人民生活中的一个历史阶段",
    ("1966", "Shmuel Yosef Agnon"): "表彰其深具个性的叙事艺术，以犹太人民的生活为主题",
    ("1966", "Nelly Sachs"): "表彰其杰出的抒情与戏剧写作，以感人的力量诠释以色列的命运",
    ("1967", "Miguel Ángel Asturias"): "表彰其鲜明的文学成就，深深植根于拉丁美洲印第安民族的特质与传统",
    ("1968", "Yasunari Kawabata"): "表彰其精湛的叙事艺术，以高度的感受性表现了日本精神的精髓",
    ("1969", "Samuel Beckett"): "表彰其写作——以小说与戏剧的新形式——在现代人赤贫的境况中获得升华",
    ("1970", "Aleksandr Solzhenitsyn"): "表彰其追求俄罗斯文学不可或缺的传统时所体现的道德力量",
    ("1971", "Pablo Neruda"): "表彰其诗歌，以原初之力般的行动唤醒了一个大陆的命运与梦想",
    ("1972", "Heinrich Böll"): "表彰其写作以其对时代的广阔视野与敏感的人物刻画相结合，促成了德国文学的更新",
    ("1973", "Patrick White"): "表彰其史诗性而深入心理的叙事艺术，将一片新大陆引入了文学",
    ("1974", "Eyvind Johnson"): "表彰其视野纵览诸邦与时代的叙事艺术，服务于自由",
    ("1974", "Harry Martinson"): "表彰其捕捉露珠而映照宇宙的写作",
    ("1975", "Eugenio Montale"): "表彰其独特的诗歌，以巨大的艺术敏感性在无幻觉的人生观之下阐释人的价值",
    ("1976", "Saul Bellow"): "表彰其作品中融合的对人的理解与对当代文化的精微分析",
    ("1977", "Vicente Aleixandre"): "表彰其创造性的诗歌写作，照亮了人在宇宙与当代社会中的境况，同时代表了两战之间西班牙诗歌的伟大革新",
    ("1978", "Isaac Bashevis Singer"): "表彰其充满激情的叙事艺术，根植于波兰-犹太文化传统，使普遍的人类境况栩栩如生",
    ("1979", "Odysseas Elytis"): "表彰其诗歌，以希腊传统为背景，以感性的力量与理智的清明描绘了现代人为自由与创造而进行的抗争",
    ("1980", "Czesław Miłosz"): "表彰其以毫不妥协的清明，道出人在严酷冲突的世界中毫无遮蔽的境况",
    ("1981", "Elias Canetti"): "表彰其视野开阔、思想丰富而具艺术力量的写作",
    ("1982", "Gabriel García Márquez"): "表彰其小说与短篇故事，将奇幻与现实结合于构造丰富的想象世界之中，反映了一个大陆的生活与冲突",
    ("1983", "William Golding"): "表彰其小说，以现实主义叙事艺术的明晰与神话的多样性及普遍性，照亮了当今世界中的人类境况",
    ("1984", "Jaroslav Seifert"): "表彰其诗歌，以清新与丰富的独创性呈现出人类不屈精神与多面性的解放形象",
    ("1985", "Claude Simon"): "表彰其小说将诗人与画家的创造力融为一体，在对人类境况的描绘中深化了对时间的意识",
    ("1986", "Wole Soyinka"): "表彰其以广阔的文化视野与诗意色彩塑造了存在之戏剧",
    ("1987", "Joseph Brodsky"): "表彰其包罗万象的写作，充满思想的清明与诗性的强度",
    ("1988", "Naguib Mahfouz"): "表彰其作品意蕴丰富——时而清明写实，时而唤起朦胧——形成了适用于全人类的阿拉伯叙事艺术",
    ("1989", "Camilo José Cela"): "表彰其丰富而凝练的散文，以克制的怜悯构成了对人之脆弱性的挑战性审视",
    ("1990", "Octavio Paz"): "表彰其视野开阔、充满激情的写作，以感性的智慧与人道的完整为特征",
    ("1991", "Nadine Gordimer"): "表彰其宏伟的史诗性写作，用阿尔弗雷德·诺贝尔的话说——「对人类有莫大裨益」",
    ("1992", "Derek Walcott"): "表彰其光彩夺目的诗歌创作，由历史视野所支撑，是多元文化承诺的结晶",
    ("1993", "Toni Morrison"): "表彰其小说以先知般的力量与诗意内涵，赋予美国现实的一个本质面向以生命",
    ("1994", "Kenzaburō Ōe"): "表彰其以诗性力量创造的想象世界，生活与神话在其中凝结成今日人类困境的扰人图景",
    ("1995", "Seamus Heaney"): "表彰其兼具抒情之美与伦理深度的作品，颂扬日常的奇迹与活着的过去",
    ("1996", "Wisława Szymborska"): "表彰其诗歌以反讽的精确，让历史与生命的语境在人类现实的碎片中显现",
    ("1997", "Dario Fo"): "表彰其效仿中世纪的弄臣，鞭笞权威，维护受压迫者的尊严",
    ("1998", "José Saramago"): "表彰其以想象、同情与反讽支撑的寓言，使我们一再重新把握那难以捉摸的现实",
    ("1999", "Günter Grass"): "表彰其嬉戏般的黑色寓言，描绘了历史被遗忘的面貌",
    ("2000", "Gao Xingjian"): "表彰其具有普遍价值、刻骨洞察与语言巧思的作品，为中国小说与戏剧开辟了新的道路",
}

# 女性获奖者（20 世纪）
WOMEN = {
    "Selma Lagerlöf",
    "Grazia Deledda",
    "Sigrid Undset",
    "Pearl Buck",
    "Gabriela Mistral",
    "Nelly Sachs",
    "Nadine Gordimer",
    "Toni Morrison",
    "Wisława Szymborska",
}

# 国籍列切分用的国家/地区词表（含多词国名；匹配时忽略大小写，要求词边界）。
COUNTRY_VOCAB = [
    "Trinidad and Tobago", "United Kingdom", "United States", "Soviet Union",
    "South Korea", "South Africa", "Saint Lucia", "West Germany", "Austria-Hungary",
    "Czechoslovakia", "Switzerland", "Netherlands", "Yugoslavia", "Guatemala",
    "France", "Germany", "Norway", "Spain", "Poland", "Italy", "Sweden",
    "Belgium", "Denmark", "India", "Ireland", "Chile", "Finland", "Iceland",
    "Israel", "Greece", "Japan", "Australia", "Austria", "Colombia", "Nigeria",
    "Egypt", "Mexico", "Portugal", "Turkey", "Hungary", "Canada", "Bulgaria",
    "Romania", "Mauritius", "Peru", "China", "Tanzania", "Belarus", "Stateless",
]


def clean_country(s: str) -> str:
    """清洗国籍列：去掉脚注与括号（语言/出生地），再按国家词表切分多国籍串。"""
    if not s:
        return ""
    s = re.sub(r"\[\s*\d+\s*\]", "", s)          # 去脚注 [ 30 ]
    s = re.sub(r"\([^)]*\)", " ", s)              # 去括号（语言 / born in X）
    s = s.strip()
    out: list[str] = []
    i = 0
    while i < len(s):
        hit = None
        for c in COUNTRY_VOCAB:
            if s[i:].lower().startswith(c.lower()):
                j = i + len(c)
                if j == len(s) or s[j] == " ":
                    hit = c
                    break
        if hit:
            if not out or out[-1] != hit:
                out.append(hit)
            i += len(hit)
        else:
            i += 1
    return " / ".join(out) if out else s


def main() -> int:
    if not SRC.exists():
        print(f"✗ 缺少获奖理由数据：{SRC}")
        print("  请先运行：python3 fetch_nobel_citations.py")
        return 1

    data = json.loads(SRC.read_text(encoding="utf-8"))
    # 仅保留 20 世纪（1901–2000）
    rows = [r for r in data if r.get("year") and r["year"] <= 2000]
    rows.sort(key=lambda r: r["year"])

    total_items = len(rows)
    names = [r["name"] for r in rows]
    unique_people = set(names)

    # 两度获奖者（文学奖 20 世纪暂无）
    cnt = Counter(names)
    double = {k for k, v in cnt.items() if v > 1}

    # 国籍分布
    country_counter = Counter(clean_country(r["country"]) for r in rows)

    # 立传 / Review / 社会关系入库 状态
    done_count = sum(1 for r in rows if r["name"] in BIOGRAPHIES_DONE)
    review_count = sum(1 for r in rows if r["name"] in REVIEWS_DONE)
    relations_count = sum(1 for r in rows if r["name"] in RELATIONS_DONE)

    lines: list[str] = []
    lines.append("# 20 世纪诺贝尔文学奖得主 — OpenLiterature 名录\n")
    lines.append(
        "> **本名录收录 1901–2000 年诺贝尔文学奖得主，共 %d 项 / %d 位。**\n"
        ">\n"
        "> 从普吕多姆的诗句到格拉斯的黑色寓言：一百年间，文学奖见证了现代文学从古典传统走向现代主义的全程。\n"
        ">\n"
        "> 获奖理由为诺贝尔奖官方获奖理由（中文翻译）；「立传」表示是否已生成立传 Beamer，「Review」表示是否已完成事实核查，「社会关系入库」表示是否已将研究领域与社会关系写入 greatminds 数据库（people / person_relation / person_field）。\n"
        ">\n"
        "> 数据来源：英文维基百科「List of Nobel laureates in Literature」。\n"
        % (total_items, len(unique_people))
    )
    lines.append("---\n")

    lines.append("\n## 一、完整名单（按年份）\n")
    lines.append("\n| 年份 | 获奖者 | 国籍 | 获奖理由 | 立传 | Review | 社会关系入库 |")
    lines.append("|:--:|------|------|------|:--:|:--:|:--:|")
    for r in rows:
        name = r["name"]
        zh = NAME_ZH.get(name)
        name_display = f"{name} ({zh})" if zh else name
        country = clean_country(r["country"]) or "—"
        citation = CITATION_ZH.get((str(r["year"]), name), r["citation"])
        citation = re.sub(r"\s+", " ", citation).replace("|", "/").strip().strip('"')
        bio = "✅" if name in BIOGRAPHIES_DONE else "🔲"
        review = "✅" if name in REVIEWS_DONE else "🔲"
        relation = "✅" if name in RELATIONS_DONE else "🔲"
        lines.append("| %d | %s | %s | %s | %s | %s | %s |" % (r["year"], name_display, country, citation, bio, review, relation))

    lines.append("\n---\n")
    lines.append("\n## 二、统计说明\n")
    lines.append("\n- **获奖年份跨度**：1901–2000")
    lines.append("- **获奖总项数**：%d 项" % total_items)
    lines.append("- **获奖总人数**：%d 位" % len(unique_people))
    lines.append("- **未颁奖年份**：1914、1918、1935、1940–1943（两次世界大战期间）")
    lines.append("- **已立传**：%d 位（%s）" % (done_count, "、".join(sorted(BIOGRAPHIES_DONE)) if BIOGRAPHIES_DONE else "暂无"))
    lines.append("- **已 Review**：%d 位（%s）" % (review_count, "、".join(sorted(REVIEWS_DONE)) if REVIEWS_DONE else "暂无"))
    lines.append("- **已社会关系入库**：%d 位（%s）" % (relations_count, "、".join(sorted(RELATIONS_DONE)) if RELATIONS_DONE else "暂无"))
    if double:
        lines.append("- **两度获奖者**：" + "、".join(sorted(double)))
    if WOMEN:
        w = [x for x in sorted(WOMEN) if x in unique_people]
        if w:
            lines.append("- **女性获奖者**（20 世纪，%d 位）：%s" % (len(w), "、".join(w)))

    lines.append("\n### 国籍分布\n")
    lines.append("\n| 国籍 | 人数 |")
    lines.append("|------|:--:|")
    for c, n in country_counter.most_common():
        lines.append("| %s | %d |" % (c, n))

    lines.append("\n---\n")
    lines.append(
        "\n> **这不是一份排名，而是一部按时间展开的文学百年：每一项获奖都标记着人类对自身处境的一次书写。**\n"
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote:", OUT)
    print("总项数:", total_items, "总人数:", len(unique_people), "两度获奖:", sorted(double))
    print("已立传:", done_count, "位", "已 Review:", review_count, "位", "已社会关系入库:", relations_count, "位")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
