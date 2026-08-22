#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 nobel_chemistry_citations.json 读取 20 世纪诺贝尔化学奖得主（含获奖理由），
参考数学家侧文档形式，生成含「获奖理由 / 立传 / Review」列的结构化 md。

先运行 fetch_nobel_citations.py 生成 nobel_chemistry_citations.json，再运行本脚本。
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "nobel_chemistry_citations.json"
OUT = ROOT / "presentations" / "20th_century" / "OpenChemist_20th_Century_Nobel_Laureates.md"

# 已立传的化学家（姓名需与获奖者名单精确匹配）。
# 新增立传时在此补充姓名。
BIOGRAPHIES_DONE = set()

# 已完成 Review（两轮事实核查）的化学家（姓名需与获奖者名单精确匹配）。
# 完成两轮 Review 后在此补充姓名。
REVIEWS_DONE = set()

# 获奖者英文名 → 中文名（诺贝尔化学奖得主常用中译）。
NAME_ZH = {
    "Jacobus Henricus van 't Hoff": "雅各布斯·亨里克斯·范特霍夫",
    "Hermann Emil Fischer": "赫尔曼·埃米尔·费歇尔",
    "Svante Arrhenius": "斯万特·阿伦尼乌斯",
    "William Ramsay": "威廉·拉姆齐",
    "Adolf von Baeyer": "阿道夫·冯·拜尔",
    "Henri Moissan": "亨利·莫瓦桑",
    "Eduard Buchner": "爱德华·布赫纳",
    "Ernest Rutherford": "欧内斯特·卢瑟福",
    "Wilhelm Ostwald": "威廉·奥斯特瓦尔德",
    "Otto Wallach": "奥托·瓦拉赫",
    "Marie Curie": "玛丽·居里",
    "Victor Grignard": "维克托·格林尼亚",
    "Paul Sabatier": "保罗·萨巴捷",
    "Alfred Werner": "阿尔弗雷德·维尔纳",
    "Theodore William Richards": "西奥多·威廉·理查兹",
    "Richard Willstätter": "里夏德·维尔斯泰特",
    "Fritz Haber": "弗里茨·哈伯",
    "Walther Nernst": "瓦尔特·能斯特",
    "Frederick Soddy": "弗雷德里克·索迪",
    "Francis William Aston": "弗朗西斯·威廉·阿斯顿",
    "Fritz Pregl": "弗里茨·普雷格尔",
    "Richard Adolf Zsigmondy": "理查德·阿道夫·席格蒙迪",
    "Theodor Svedberg": "特奥多尔·斯韦德贝里",
    "Heinrich Otto Wieland": "海因里希·奥托·维兰德",
    "Adolf Windaus": "阿道夫·温道斯",
    "Arthur Harden": "阿瑟·哈登",
    "Hans von Euler-Chelpin": "汉斯·冯·奥伊勒-凯尔平",
    "Hans Fischer": "汉斯·费歇尔",
    "Carl Bosch": "卡尔·博施",
    "Friedrich Bergius": "弗里德里希·贝吉乌斯",
    "Irving Langmuir": "欧文·朗缪尔",
    "Harold Urey": "哈罗德·尤里",
    "Frédéric Joliot-Curie": "弗雷德里克·约里奥-居里",
    "Irène Joliot-Curie": "伊雷娜·约里奥-居里",
    "Peter Debye": "彼得·德拜",
    "Norman Haworth": "诺曼·霍沃思",
    "Paul Karrer": "保罗·卡雷尔",
    "Richard Kuhn": "里夏德·库恩",
    "Adolf Butenandt": "阿道夫·布特南特",
    "Leopold Ružička": "莱奥波德·鲁日奇卡",
    "George de Hevesy": "乔治·德·赫维西",
    "Otto Hahn": "奥托·哈恩",
    "Artturi Ilmari Virtanen": "阿尔图里·伊尔马里·维尔塔宁",
    "James B. Sumner": "詹姆斯·萨姆纳",
    "John Howard Northrop": "约翰·霍华德·诺思罗普",
    "Wendell Meredith Stanley": "温德尔·梅雷迪思·斯坦利",
    "Robert Robinson": "罗伯特·鲁滨逊",
    "Arne Tiselius": "阿尔内·蒂塞利乌斯",
    "William Giauque": "威廉·吉奥克",
    "Otto Diels": "奥托·迪尔斯",
    "Kurt Alder": "库尔特·阿尔德",
    "Edwin McMillan": "埃德温·麦克米伦",
    "Glenn T. Seaborg": "格伦·西奥多·西博格",
    "Archer Martin": "阿彻·马丁",
    "Richard Laurence Millington Synge": "理查德·劳伦斯·米林顿·辛格",
    "Hermann Staudinger": "赫尔曼·施陶丁格",
    "Linus Pauling": "莱纳斯·鲍林",
    "Vincent du Vigneaud": "文森特·迪维尼奥",
    "Cyril Norman Hinshelwood": "西里尔·诺曼·欣谢尔伍德",
    "Nikolay Semyonov": "尼古拉·谢苗诺夫",
    "Alexander R. Todd": "亚历山大·托德",
    "Frederick Sanger": "弗雷德里克·桑格",
    "Jaroslav Heyrovský": "雅罗斯拉夫·海罗夫斯基",
    "Willard Libby": "威拉德·利比",
    "Melvin Calvin": "梅尔文·卡尔文",
    "Max Perutz": "马克斯·佩鲁茨",
    "John Kendrew": "约翰·肯德鲁",
    "Karl Ziegler": "卡尔·齐格勒",
    "Giulio Natta": "朱利奥·纳塔",
    "Dorothy Hodgkin": "多萝西·霍奇金",
    "Robert Burns Woodward": "罗伯特·伯恩斯·伍德沃德",
    "Robert S. Mulliken": "罗伯特·马利肯",
    "Manfred Eigen": "曼弗雷德·艾根",
    "Ronald George Wreyford Norrish": "罗纳德·乔治·雷福德·诺里什",
    "George Porter": "乔治·波特",
    "Lars Onsager": "拉斯·昂萨格",
    "Derek Barton": "德里克·巴顿",
    "Odd Hassel": "奥德·哈塞尔",
    "Luis Federico Leloir": "路易斯·费德里科·莱洛伊尔",
    "Gerhard Herzberg": "格哈德·赫茨贝格",
    "Christian B. Anfinsen": "克里斯蒂安·安芬森",
    "Stanford Moore": "斯坦福·穆尔",
    "William Howard Stein": "威廉·霍华德·斯坦",
    "Ernst Otto Fischer": "恩斯特·奥托·费歇尔",
    "Geoffrey Wilkinson": "杰弗里·威尔金森",
    "Paul Flory": "保罗·弗洛里",
    "John Cornforth": "约翰·康福思",
    "Vladimir Prelog": "弗拉基米尔·普雷洛格",
    "William Lipscomb": "威廉·利普斯科姆",
    "Ilya Prigogine": "伊利亚·普里高津",
    "Peter D. Mitchell": "彼得·米切尔",
    "Herbert C. Brown": "赫伯特·布朗",
    "Georg Wittig": "格奥尔格·维蒂希",
    "Paul Berg": "保罗·伯格",
    "Walter Gilbert": "沃尔特·吉尔伯特",
    "Kenichi Fukui": "福井谦一",
    "Roald Hoffmann": "罗德·霍夫曼",
    "Aaron Klug": "阿龙·克卢格",
    "Henry Taube": "亨利·陶布",
    "Robert Bruce Merrifield": "罗伯特·布鲁斯·梅里菲尔德",
    "Herbert A. Hauptman": "赫伯特·豪普特曼",
    "Jerome Karle": "杰罗姆·卡尔",
    "Dudley R. Herschbach": "达德利·赫施巴赫",
    "Yuan T. Lee": "李远哲",
    "John Polanyi": "约翰·波拉尼",
    "Donald J. Cram": "唐纳德·克拉姆",
    "Jean-Marie Lehn": "让-马里·莱恩",
    "Charles J. Pedersen": "查尔斯·佩德森",
    "Johann Deisenhofer": "约翰·戴森霍费尔",
    "Robert Huber": "罗伯特·胡贝尔",
    "Hartmut Michel": "哈特穆特·米歇尔",
    "Sidney Altman": "西德尼·奥尔特曼",
    "Thomas Cech": "托马斯·切赫",
    "Elias James Corey": "伊莱亚斯·詹姆斯·科里",
    "Richard R. Ernst": "理查德·恩斯特",
    "Rudolph A. Marcus": "鲁道夫·马库斯",
    "Kary Mullis": "凯里·穆利斯",
    "Michael Smith": "迈克尔·史密斯",
    "George Andrew Olah": "乔治·安德鲁·奥拉",
    "Paul J. Crutzen": "保罗·克鲁岑",
    "Mario J. Molina": "马里奥·莫利纳",
    "F. Sherwood Rowland": "弗兰克·舍伍德·罗兰",
    "Robert Curl": "罗伯特·柯尔",
    "Harry Kroto": "哈罗德·克罗托",
    "Richard Smalley": "理查德·斯莫利",
    "Paul D. Boyer": "保罗·博耶",
    "John E. Walker": "约翰·沃克",
    "Jens Christian Skou": "延斯·克里斯蒂安·斯科乌",
    "Walter Kohn": "沃尔特·科恩",
    "John Pople": "约翰·波普尔",
    "Ahmed Zewail": "艾哈迈德·泽维尔",
    "Alan J. Heeger": "艾伦·黑格",
    "Alan MacDiarmid": "艾伦·麦克迪尔米德",
    "Hideki Shirakawa": "白川英树",
}

# 获奖理由（Citation）英文原文 → 中文翻译（诺贝尔奖官方获奖理由中译）。
CITATION_ZH = {
    "in recognition of the extraordinary services he has rendered by the discovery of the laws of chemical dynamics and osmotic pressure in solutions":
        "表彰他因发现化学动力学定律和溶液渗透压定律所作出的杰出贡献",
    "in recognition of the extraordinary services he has rendered by his work on sugar and purine syntheses":
        "表彰他因在糖类和嘌呤合成方面的研究所作出的杰出贡献",
    "in recognition of the extraordinary services he has rendered to the advancement of chemistry by his electrolytic theory of dissociation":
        "表彰他因提出电离理论而对化学进步所作出的杰出贡献",
    "in recognition of his services in the discovery of the inert gaseous elements in air, and his determination of their place in the periodic system":
        "表彰他发现空气中的惰性气体元素，并确定它们在元素周期表中的位置",
    "in recognition of his services in the advancement of organic chemistry and the chemical industry, through his work on organic dyes and hydroaromatic compounds":
        "表彰他通过对有机染料和氢化芳香族化合物的研究，推动有机化学和化学工业的发展",
    "in recognition of the great services rendered by him in his investigation and isolation of the element fluorine, and for the adoption in the service of science of the electric furnace called after him":
        "表彰他研究并分离出元素氟所作出的巨大贡献，以及他为科学服务而采用以他名字命名的电炉",
    "for his biochemical researches and his discovery of cell-free fermentation":
        "表彰他的生物化学研究，以及他发现无细胞发酵",
    "for his investigations into the disintegration of the elements, and the chemistry of radioactive substances":
        "表彰他对元素蜕变及放射性物质化学的研究",
    "in recognition of his work on catalysis and for his investigations into the fundamental principles governing chemical equilibria and rates of reaction":
        "表彰他在催化方面的工作，以及他对支配化学平衡和反应速率基本原理的研究",
    "in recognition of his services to organic chemistry and the chemical industry by his pioneer work in the field of alicyclic compounds":
        "表彰他因在脂环族化合物领域的开创性工作，对有机化学和化学工业所作出的贡献",
    "in recognition of her services to the advancement of chemistry by the discovery of the elements radium and polonium, by the isolation of radium and the study of the nature and compounds of this remarkable element":
        "表彰她因发现镭和钋元素、分离出镭并研究这一非凡元素的性质及化合物，对化学进步所作出的贡献",
    "for the discovery of the so-called Grignard reagent, which in recent years has greatly advanced the progress of organic chemistry":
        "表彰他发现了所谓的格氏试剂，该试剂近年来极大地推动了有机化学的进步",
    "for his method of hydrogenating organic compounds in the presence of finely disintegrated metals whereby the progress of organic chemistry has been greatly advanced in recent years":
        "表彰他提出在精细分散金属存在下对有机化合物进行氢化的方法，该方法近年来极大地推动了有机化学的进步",
    "in recognition of his work on the linkage of atoms in molecules by which he has thrown new light on earlier investigations and opened up new fields of research especially in inorganic chemistry":
        "表彰他关于分子中原子键合的研究，该研究为早期研究带来了新认识，并开辟了新的研究领域，尤其是在无机化学方面",
    "in recognition of his accurate determinations of the atomic weight of a large number of chemical elements":
        "表彰他精确测定了大量化学元素的原子量",
    "for his researches on plant pigments, especially chlorophyll":
        "表彰他对植物色素，尤其是叶绿素的研究",
    "for the synthesis of ammonia from its elements":
        "表彰他由单质合成氨",
    "in recognition of his work in thermochemistry":
        "表彰他在热化学方面的工作",
    "for his contributions to our knowledge of the chemistry of radioactive substances, and his investigations into the origin and nature of isotopes":
        "表彰他对放射性物质化学知识的贡献，以及他对同位素起源和本质的研究",
    "for his discovery, by means of his mass spectrograph, of isotopes, in a large number of non-radioactive elements, and for his enunciation of the whole-number rule":
        "表彰他利用质谱仪在大量非放射性元素中发现同位素，并提出整数规则",
    "for his invention of the method of micro-analysis of organic substances":
        "表彰他发明了有机物质的微量分析方法",
    "for his demonstration of the heterogeneous nature of colloid solutions and for the methods he used":
        "表彰他证明了胶体溶液的异质性，以及他所采用的方法",
    "for his work on disperse systems":
        "表彰他在分散体系方面的工作",
    "for his investigations of the constitution of the bile acids and related substances":
        "表彰他对胆汁酸及相关物质结构的研究",
    "for the services rendered through his research into the constitution of the sterols and their connection with the vitamins":
        "表彰他通过研究甾醇的结构及其与维生素的关系所作出的贡献",
    "for their investigations on the fermentation of sugar and fermentative enzymes":
        "表彰他们对糖发酵和发酵酶的研究",
    "for his researches into the constitution of haemin and chlorophyll and especially for his synthesis of haemin":
        "表彰他对血红素和叶绿素结构的研究，尤其是他合成了血红素",
    "in recognition of their contributions to the invention and development of chemical high pressure methods":
        "表彰他们对化学高压方法的发明和发展所作出的贡献",
    "for his discoveries and investigations in surface chemistry":
        "表彰他在表面化学方面的发现和研究",
    "for his discovery of heavy hydrogen":
        "表彰他发现重氢",
    "in recognition of their synthesis of new radioactive elements":
        "表彰他们合成了新的放射性元素",
    "for his contributions to our knowledge of molecular structure through his investigations on dipole moments and on the diffraction of X-rays and electrons in gases":
        "表彰他通过对偶极矩以及气体中 X 射线和电子衍射的研究，对分子结构知识所作出的贡献",
    "for his investigations on carbohydrates and vitamin C":
        "表彰他对碳水化合物和维生素 C 的研究",
    "for his investigations on carotenoids, flavins and vitamins A and B 2":
        "表彰他对类胡萝卜素、黄素以及维生素 A 和 B2 的研究",
    "for his work on carotenoids and vitamins":
        "表彰他在类胡萝卜素和维生素方面的工作",
    "for his work on sex hormones":
        "表彰他在性激素方面的工作",
    "for his work on polymethylenes and higher terpenes":
        "表彰他在多亚甲基和高级萜烯方面的工作",
    "for his work on the use of isotopes as tracers in the study of chemical processes":
        "表彰他在化学过程研究中利用同位素作为示踪剂的工作",
    "for his discovery of the fission of heavy nuclei":
        "表彰他发现重核裂变",
    "for his research and inventions in agricultural and nutrition chemistry, especially for his fodder preservation method":
        "表彰他在农业化学和营养化学方面的研究和发明，尤其是他的饲料保藏方法",
    "for his discovery that enzymes can be crystallized":
        "表彰他发现酶可以结晶",
    "for their preparation of enzymes and virus proteins in a pure form":
        "表彰他们制备了纯净形式的酶和病毒蛋白质",
    "for his investigations on plant products of biological importance, especially the alkaloids":
        "表彰他对具有生物学重要性的植物产物，尤其是生物碱的研究",
    "for his research on electrophoresis and adsorption analysis, especially for his discoveries concerning the complex nature of the serum proteins":
        "表彰他对电泳和吸附分析的研究，尤其是他关于血清蛋白质复杂本质的发现",
    "for his contributions in the field of chemical thermodynamics, particularly concerning the behaviour of substances at extremely low temperatures":
        "表彰他在化学热力学领域的贡献，尤其是关于物质在极低温度下行为的研究",
    "for their discovery and development of the diene synthesis":
        "表彰他们发现并发展了双烯合成",
    "for their discoveries in the chemistry of transuranium elements":
        "表彰他们在超铀元素化学方面的发现",
    "for their invention of partition chromatography":
        "表彰他们发明了分配色谱法",
    "for his discoveries in the field of macromolecular chemistry":
        "表彰他在高分子化学领域的发现",
    "for his research into the nature of the chemical bond and its application to the elucidation of the structure of complex substances":
        "表彰他对化学键本质的研究，及其在阐明复杂物质结构方面的应用",
    "for his work on biochemically important sulphur compounds, especially for the first synthesis of a polypeptide hormone":
        "表彰他在生物化学上重要的含硫化合物方面的工作，尤其是他首次合成了多肽激素",
    "for their researches into the mechanism of chemical reactions":
        "表彰他们对化学反应机理的研究",
    "for his work on nucleotides and nucleotide co-enzymes":
        "表彰他在核苷酸和核苷酸辅酶方面的工作",
    "for his work on the structure of proteins, especially that of insulin":
        "表彰他对蛋白质结构，尤其是胰岛素结构的研究",
    "for his discovery and development of the polarographic methods of analysis":
        "表彰他发现并发展了极谱分析方法",
    "for his method to use carbon-14 for age determination in archaeology, geology, geophysics, and other branches of science":
        "表彰他利用碳-14 测定考古学、地质学、地球物理学及其他科学领域年代的方法",
    "for his research on the carbon dioxide assimilation in plants":
        "表彰他对植物中二氧化碳同化作用的研究",
    "for their studies of the structures of globular proteins":
        "表彰他们对球状蛋白质结构的研究",
    "for their discoveries in the field of the chemistry and technology of high polymers":
        "表彰他们在高分子化学和技术领域的发现",
    "for her determinations by X-ray techniques of the structures of important biochemical substances":
        "表彰她利用 X 射线技术测定了重要生物化学物质的结构",
    "for his outstanding achievements in the art of organic synthesis":
        "表彰他在有机合成艺术方面的杰出成就",
    "for his fundamental work concerning chemical bonds and the electronic structure of molecules by the molecular orbital method":
        "表彰他利用分子轨道方法，在化学键和分子电子结构方面的基础工作",
    "for their studies of extremely fast chemical reactions, effected by disturbing the equilibrium by means of very short pulses of energy":
        "表彰他们通过极短能量脉冲扰动平衡，对极快速化学反应的研究",
    "for the discovery of the reciprocal relations bearing his name, which are fundamental for the thermodynamics of irreversible processes":
        "表彰他发现以他名字命名的倒易关系，该关系对不可逆过程热力学具有基础意义",
    "for their contributions to the development of the concept of conformation and its application in chemistry":
        "表彰他们对构象概念的发展及其在化学中应用所作出的贡献",
    "for his discovery of sugar nucleotides and their role in the biosynthesis of carbohydrates":
        "表彰他发现糖核苷酸及其在碳水化合物生物合成中的作用",
    "for his contributions to the knowledge of electronic structure and geometry of molecules, particularly free radicals":
        "表彰他对分子电子结构和几何结构，尤其是自由基方面的知识所作出的贡献",
    "for his work on ribonuclease, especially concerning the connection between the amino acid sequence and the biologically active conformation":
        "表彰他在核糖核酸酶方面的工作，尤其是关于氨基酸序列与生物活性构象之间联系的研究",
    "for their contribution to the understanding of the connection between chemical structure and catalytic activity of the active centre of the ribonuclease molecule":
        "表彰他们为理解核糖核酸酶分子活性中心的化学结构与催化活性之间的联系所作出的贡献",
    "for their pioneering work, performed independently, on the chemistry of the organometallic, so called sandwich compounds":
        "表彰他们各自独立开展的关于有机金属化合物（即所谓的夹心化合物）化学的开创性工作",
    "for his fundamental work, both theoretical and experimental, in the physical chemistry of macromolecules":
        "表彰他在高分子物理化学方面的基础工作（理论和实验两方面）",
    "for his work on the stereochemistry of enzyme-catalyzed reactions":
        "表彰他在酶催化反应的立体化学方面的工作",
    "for his research into the stereochemistry of organic molecules and reactions":
        "表彰他对有机分子和反应的立体化学的研究",
    "for his studies on the structure of boranes illuminating problems of chemical bonding":
        "表彰他对硼烷结构的研究，阐明了化学键合问题",
    "for his contributions to non-equilibrium thermodynamics, particularly the theory of dissipative structures":
        "表彰他对非平衡态热力学的贡献，尤其是耗散结构理论",
    "for his contribution to the understanding of biological energy transfer through the formulation of the chemiosmotic theory":
        "表彰他通过提出化学渗透理论，对理解生物能量转移所作出的贡献",
    "for their development of the use of boron- and phosphorus-containing compounds, respectively, into important reagents in organic synthesis":
        "表彰他们分别将含硼化合物和含磷化合物发展成有机合成中的重要试剂",
    "for his fundamental studies of the biochemistry of nucleic acids, with particular regard to recombinant-DNA":
        "表彰他对核酸生物化学的基础研究，尤其是关于重组 DNA 的研究",
    "for their contributions concerning the determination of base sequences in nucleic acids":
        "表彰他们在核酸碱基序列测定方面所作出的贡献",
    "for their theories, developed independently, concerning the course of chemical reactions":
        "表彰他们各自独立提出的关于化学反应进程的理论",
    "for his development of crystallographic electron microscopy and his structural elucidation of biologically important nucleic acid-protein complexes":
        "表彰他发展晶体学电子显微术，并阐明具有生物学重要性的核酸-蛋白质复合物的结构",
    "for his work on the mechanisms of electron transfer reactions, especially in metal complexes":
        "表彰他在电子转移反应机理方面的工作，尤其是在金属配合物中的研究",
    "for his development of methodology for chemical synthesis on a solid matrix":
        "表彰他发展了在固相载体上进行化学合成的方法",
    "for their outstanding achievements in developing direct methods for the determination of crystal structures":
        "表彰他们发展测定晶体结构的直接方法所取得的杰出成就",
    "for their contributions concerning the dynamics of chemical elementary processes":
        "表彰他们在化学基元过程动力学方面所作出的贡献",
    "for their development and use of molecules with structure-specific interactions of high selectivity":
        "表彰他们开发并使用具有高选择性结构特异性相互作用的分子",
    "for their determination of the three-dimensional structure of a photosynthetic reaction centre":
        "表彰他们测定了光合作用反应中心的三维结构",
    "for their discovery of catalytic properties of RNA":
        "表彰他们发现 RNA 的催化性质",
    "for his development of the theory and methodology of organic synthesis":
        "表彰他发展了有机合成的理论和方法学",
    "for his contributions to the development of the methodology of high resolution nuclear magnetic resonance (NMR) spectroscopy":
        "表彰他对高分辨率核磁共振（NMR）波谱方法学发展所作出的贡献",
    "for his contributions to the theory of electron transfer reactions in chemical systems":
        "表彰他对化学体系中电子转移反应理论所作出的贡献",
    "for contributions to the developments of methods within DNA-based chemistry, [especially] for his invention of the polymerase chain reaction (PCR) method":
        "表彰他对基于 DNA 的化学方法发展所作出的贡献，尤其是他发明了聚合酶链式反应（PCR）方法",
    "for contributions to the developments of methods within DNA-based chemistry, [especially] for his fundamental contributions to the establishment of oligonucleotide-based, site-directed mutagenesis and its development for protein studies":
        "表彰他对基于 DNA 的化学方法发展所作出的贡献，尤其是他为建立基于寡核苷酸的定点诱变及其在蛋白质研究中的发展所作出的基础性贡献",
    "for his contribution to carbocation chemistry":
        "表彰他对碳正离子化学的贡献",
    "for their work in atmospheric chemistry, particularly concerning the formation and decomposition of ozone":
        "表彰他们在大气化学方面的工作，尤其是关于臭氧形成和分解的研究",
    "for their discovery of fullerenes":
        "表彰他们发现富勒烯",
    "for their elucidation of the enzymatic mechanism underlying the synthesis of adenosine triphosphate (ATP)":
        "表彰他们阐明了三磷酸腺苷（ATP）合成所依据的酶促机理",
    "for the first discovery of an ion-transporting enzyme, Na +, K + -ATPase":
        "表彰他首次发现一种离子转运酶——钠钾 ATP 酶（Na⁺,K⁺-ATPase）",
    "for his development of the density-functional theory":
        "表彰他发展了密度泛函理论",
    "for his development of computational methods in quantum chemistry":
        "表彰他发展了量子化学中的计算方法",
    "for his studies of the transition states of chemical reactions using femtosecond spectroscopy":
        "表彰他利用飞秒光谱学研究化学反应的过渡态",
    "for their discovery and development of conductive polymers":
        "表彰他们发现并发展了导电聚合物",
}


def _norm_citation(s: str) -> str:
    """规范化获奖理由文本：折叠空白、去掉标点前空格，使其与字典 key 对齐。"""
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s+([.,;:])", r"\1", s)
    return s


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

    # 两度获奖者
    cnt = Counter(names)
    double = {k for k, v in cnt.items() if v > 1}

    # 女性获奖者（20 世纪）
    women = {"Marie Curie", "Irène Joliot-Curie", "Dorothy Hodgkin"}

    # 国籍分布
    country_counter = Counter(r["country"] for r in rows)

    # 立传 / Review 状态
    done_count = sum(1 for r in rows if r["name"] in BIOGRAPHIES_DONE)
    review_count = sum(1 for r in rows if r["name"] in REVIEWS_DONE)

    lines: list[str] = []
    lines.append("# 20 世纪诺贝尔化学奖得主 — OpenChemist 名录\n")
    lines.append(
        "> **本名录收录 1901–2000 年诺贝尔化学奖得主，共 %d 项 / %d 位。**\n"
        ">\n"
        "> 从 van 't Hoff 的化学动力学到 Sanger 的基因测序：一百年间，化学奖见证了现代化学从分子结构走向生命科学的全过程。\n"
        ">\n"
        "> 获奖理由为诺贝尔奖官方获奖理由（中文翻译）；「立传」表示是否已生成立传 Beamer，「Review」表示是否已完成事实核查。\n"
        ">\n"
        "> 数据来源：英文维基百科「List of Nobel laureates in Chemistry」。\n"
        % (total_items, len(unique_people))
    )
    lines.append("---\n")

    lines.append("\n## 一、完整名单（按年份）\n")
    lines.append("\n| 年份 | 获奖者 | 国籍 | 获奖理由 | 立传 | Review |")
    lines.append("|:--:|------|------|------|:--:|:--:|")
    for r in rows:
        name = r["name"]
        zh = NAME_ZH.get(name)
        name_display = f"{name} ({zh})" if zh else name
        country = r["country"] or "—"
        citation_en = _norm_citation(r["citation"])
        citation = CITATION_ZH.get(citation_en, citation_en).replace("|", "/")  # 转义表格竖线
        bio = "✅" if name in BIOGRAPHIES_DONE else "🔲"
        review = "✅" if name in REVIEWS_DONE else "🔲"
        lines.append("| %d | %s | %s | %s | %s | %s |" % (r["year"], name_display, country, citation, bio, review))

    lines.append("\n---\n")
    lines.append("\n## 二、统计说明\n")
    lines.append("\n- **获奖年份跨度**：1901–2000")
    lines.append("- **获奖总项数**：%d 项" % total_items)
    lines.append("- **获奖总人数**：%d 位" % len(unique_people))
    lines.append("- **已立传**：%d 位（%s）" % (done_count, "、".join(sorted(BIOGRAPHIES_DONE)) if BIOGRAPHIES_DONE else "暂无"))
    lines.append("- **已 Review**：%d 位（%s）" % (review_count, "、".join(sorted(REVIEWS_DONE)) if REVIEWS_DONE else "暂无"))
    if double:
        lines.append("- **两度获奖者**：" + "、".join(sorted(double)) + "（唯一两度获诺贝尔化学奖者）")
    if women:
        w = [x for x in sorted(women) if x in unique_people]
        if w:
            lines.append("- **女性获奖者**（20 世纪）：" + "、".join(w))

    lines.append("\n### 国籍分布\n")
    lines.append("\n| 国籍 | 人数 |")
    lines.append("|------|:--:|")
    for c, n in country_counter.most_common():
        lines.append("| %s | %d |" % (c, n))

    lines.append("\n---\n")
    lines.append(
        "\n> **这不是一份排名，而是一部按时间展开的化学历程：每一项获奖都标记着人类对自然认识的一次跃迁。**\n"
    )

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote:", OUT)
    print("总项数:", total_items, "总人数:", len(unique_people), "两度获奖:", sorted(double))
    print("已立传:", done_count, "位", "已 Review:", review_count, "位")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
