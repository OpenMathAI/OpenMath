#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 nobel_physics_citations.json 读取 20 世纪诺贝尔物理学奖得主（含获奖理由），
参考数学家侧文档形式，生成含「获奖理由 / 立传 / Review」列的结构化 md。

先运行 fetch_nobel_citations.py 生成 nobel_physics_citations.json，再运行本脚本。
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "nobel_physics_citations.json"
OUT = ROOT / "presentations" / "20th_century" / "OpenPhysicist_20th_Century_Nobel_Laureates.md"

# 已立传的物理学家（姓名需与获奖者名单精确匹配）。
# 新增立传时在此补充姓名。
BIOGRAPHIES_DONE = {
    "Eugene Paul Wigner",
    "Kenneth G. Wilson",
}

# 获奖者英文名 → 中文名（诺贝尔物理学奖得主常用中译）。
NAME_ZH = {
    "Wilhelm Conrad Röntgen": "威廉·康拉德·伦琴",
    "Hendrik Antoon Lorentz": "亨德里克·安东·洛伦兹",
    "Pieter Zeeman": "彼得·塞曼",
    "Antoine Henri Becquerel": "安托万·亨利·贝克勒尔",
    "Pierre Curie": "皮埃尔·居里",
    "Marie Curie": "玛丽·居里",
    "Lord Rayleigh": "瑞利勋爵",
    "Philipp Eduard Anton von Lenard": "菲利普·爱德华·安东·冯·莱纳德",
    "Joseph John Thomson": "约瑟夫·约翰·汤姆孙",
    "Albert Abraham Michelson": "阿尔伯特·亚伯拉罕·迈克耳孙",
    "Gabriel Lippmann": "加布里埃尔·李普曼",
    "Guglielmo Marconi": "古列尔莫·马可尼",
    "Karl Ferdinand Braun": "卡尔·费迪南德·布劳恩",
    "Johannes Diderik van der Waals": "约翰内斯·迪德里克·范德瓦耳斯",
    "Wilhelm Wien": "威廉·维恩",
    "Nils Gustaf Dalén": "尼尔斯·古斯塔夫·达伦",
    "Heike Kamerlingh Onnes": "海克·卡末林·昂内斯",
    "Max von Laue": "马克斯·冯·劳厄",
    "William Henry Bragg": "威廉·亨利·布拉格",
    "William Lawrence Bragg": "威廉·劳伦斯·布拉格",
    "Charles Glover Barkla": "查尔斯·格洛弗·巴克拉",
    "Max Karl Ernst Ludwig Planck": "马克斯·普朗克",
    "Johannes Stark": "约翰内斯·斯塔克",
    "Charles Édouard Guillaume": "夏尔·爱德华·纪尧姆",
    "Albert Einstein": "阿尔伯特·爱因斯坦",
    "Niels Henrik David Bohr": "尼尔斯·玻尔",
    "Robert Andrews Millikan": "罗伯特·安德鲁斯·密立根",
    "Karl Manne Georg Siegbahn": "卡尔·曼内·乔治·西格班",
    "James Franck": "詹姆斯·弗兰克",
    "Gustav Ludwig Hertz": "古斯塔夫·路德维希·赫兹",
    "Jean Baptiste Perrin": "让·巴蒂斯特·佩兰",
    "Arthur Holly Compton": "阿瑟·霍利·康普顿",
    "Charles Thomson Rees Wilson": "查尔斯·汤姆森·里斯·威尔逊",
    "Owen Willans Richardson": "欧文·威廉斯·理查森",
    "Louis-Victor Pierre Raymond de Broglie": "路易·维克多·德布罗意",
    "Chandrasekhara Venkata Raman": "钱德拉塞卡拉·文卡塔·拉曼",
    "Werner Karl Heisenberg": "维尔纳·海森堡",
    "Erwin Schrödinger": "埃尔温·薛定谔",
    "Paul Adrien Maurice Dirac": "保罗·狄拉克",
    "James Chadwick": "詹姆斯·查德威克",
    "Victor Franz Hess": "维克托·弗朗茨·赫斯",
    "Carl David Anderson": "卡尔·戴维·安德森",
    "Clinton Joseph Davisson": "克林顿·约瑟夫·戴维森",
    "George Paget Thomson": "乔治·佩吉特·汤姆孙",
    "Enrico Fermi": "恩里科·费米",
    "Ernest Orlando Lawrence": "欧内斯特·奥兰多·劳伦斯",
    "Otto Stern": "奥托·斯特恩",
    "Isidor Isaac Rabi": "伊西多·艾萨克·拉比",
    "Wolfgang Pauli": "沃尔夫冈·泡利",
    "Percy Williams Bridgman": "珀西·威廉姆斯·布里奇曼",
    "Edward Victor Appleton": "爱德华·维克托·阿普顿",
    "Patrick Maynard Stuart Blackett": "帕特里克·梅纳德·斯图尔特·布莱克特",
    "Hideki Yukawa": "汤川秀树",
    "Cecil Frank Powell": "塞西尔·弗兰克·鲍威尔",
    "John Douglas Cockcroft": "约翰·道格拉斯·考克饶夫",
    "Ernest Thomas Sinton Walton": "欧内斯特·托马斯·辛顿·沃尔顿",
    "Felix Bloch": "费利克斯·布洛赫",
    "Edward Mills Purcell": "爱德华·米尔斯·珀塞尔",
    "Frits Zernike": "弗里茨·泽尔尼克",
    "Max Born": "马克斯·玻恩",
    "Walther Bothe": "瓦尔特·博特",
    "Willis Eugene Lamb": "威利斯·尤金·兰姆",
    "Polykarp Kusch": "波利卡普·库什",
    "William Bradford Shockley": "威廉·肖克利",
    "John Bardeen": "约翰·巴丁",
    "Walter Houser Brattain": "沃尔特·豪泽·布拉顿",
    "Chen Ning Yang": "杨振宁",
    "Tsung-Dao Lee": "李政道",
    "Pavel Alekseyevich Cherenkov": "帕维尔·阿列克谢耶维奇·切伦科夫",
    "Il'ja Mikhailovich Frank": "伊利亚·米哈伊洛维奇·弗兰克",
    "Igor Yevgenyevich Tamm": "伊戈尔·叶夫根耶维奇·塔姆",
    "Emilio Gino Segrè": "埃米利奥·吉诺·塞格雷",
    "Owen Chamberlain": "欧文·张伯伦",
    "Donald Arthur Glaser": "唐纳德·阿瑟·格拉泽",
    "Robert Hofstadter": "罗伯特·霍夫施塔特",
    "Rudolf Ludwig Mössbauer": "鲁道夫·路德维希·穆斯堡尔",
    "Lev Davidovich Landau": "列夫·达维多维奇·朗道",
    "Eugene Paul Wigner": "尤金·保罗·维格纳",
    "Maria Goeppert Mayer": "玛丽亚·格佩特-梅耶",
    "J. Hans D. Jensen": "汉斯·丹尼尔·延森",
    "Charles Hard Townes": "查尔斯·哈德·汤斯",
    "Nicolay Gennadiyevich Basov": "尼古拉·根纳季耶维奇·巴索夫",
    "Aleksandr Mikhailovich Prokhorov": "亚历山大·米哈伊洛维奇·普罗霍罗夫",
    "Sin-Itiro Tomonaga": "朝永振一郎",
    "Julian Schwinger": "朱利安·施温格",
    "Richard P. Feynman": "理查德·费曼",
    "Alfred Kastler": "阿尔弗雷德·卡斯特勒",
    "Hans Albrecht Bethe": "汉斯·阿尔布雷希特·贝特",
    "Luis Walter Alvarez": "路易斯·沃尔特·阿尔瓦雷斯",
    "Murray Gell-Mann": "默里·盖尔曼",
    "Hannes Olof Gösta Alfvén": "汉尼斯·阿尔文",
    "Louis Eugène Félix Néel": "路易·欧仁·费利克斯·内尔",
    "Dennis Gabor": "丹尼斯·加博尔",
    "Leon Neil Cooper": "利昂·库珀",
    "John Robert Schrieffer": "约翰·罗伯特·施里弗",
    "Leo Esaki": "江崎玲于奈",
    "Ivar Giaever": "伊瓦尔·贾埃弗",
    "Brian David Josephson": "布赖恩·约瑟夫森",
    "Martin Ryle": "马丁·赖尔",
    "Antony Hewish": "安东尼·休伊什",
    "Aage Niels Bohr": "奥格·尼尔斯·玻尔",
    "Ben Roy Mottelson": "本·罗伊·莫特森",
    "Leo James Rainwater": "利奥·詹姆斯·雷恩沃特",
    "Burton Richter": "伯顿·里克特",
    "Samuel Chao Chung Ting": "丁肇中",
    "Philip Warren Anderson": "菲利普·沃伦·安德森",
    "Nevill Francis Mott": "内维尔·弗朗西斯·莫特",
    "John Hasbrouck Van Vleck": "约翰·哈斯布鲁克·范弗莱克",
    "Pyotr Leonidovich Kapitsa": "彼得·列昂尼多维奇·卡皮察",
    "Arno Allan Penzias": "阿尔诺·彭齐亚斯",
    "Robert Woodrow Wilson": "罗伯特·伍德罗·威尔逊",
    "Sheldon Lee Glashow": "谢尔登·李·格拉肖",
    "Abdus Salam": "阿卜杜勒·萨拉姆",
    "Steven Weinberg": "史蒂文·温伯格",
    "James Watson Cronin": "詹姆斯·沃森·克罗宁",
    "Val Logsdon Fitch": "瓦尔·洛格斯登·菲奇",
    "Nicolaas Bloembergen": "尼古拉斯·布洛姆伯根",
    "Arthur Leonard Schawlow": "阿瑟·伦纳德·肖洛",
    "Kai M. Siegbahn": "凯·西格班",
    "Kenneth G. Wilson": "肯尼斯·威尔逊",
    "Subrahmanyan Chandrasekhar": "苏布拉马尼扬·钱德拉塞卡",
    "William Alfred Fowler": "威廉·福勒",
    "Carlo Rubbia": "卡洛·鲁比亚",
    "Simon van der Meer": "西蒙·范德梅尔",
    "Klaus von Klitzing": "克劳斯·冯·克利青",
    "Ernst Ruska": "恩斯特·鲁斯卡",
    "Gerd Binnig": "格尔德·宾宁",
    "Heinrich Rohrer": "海因里希·罗雷尔",
    "J. Georg Bednorz": "格奥尔格·贝德诺尔茨",
    "K. Alexander Müller": "卡尔·亚历山大·缪勒",
    "Leon M. Lederman": "利昂·莱德曼",
    "Melvin Schwartz": "梅尔文·施瓦茨",
    "Jack Steinberger": "杰克·斯坦伯格",
    "Norman F. Ramsey": "诺曼·拉姆齐",
    "Hans G. Dehmelt": "汉斯·德默尔特",
    "Wolfgang Paul": "沃尔夫冈·保罗",
    "Jerome I. Friedman": "杰罗姆·弗里德曼",
    "Henry W. Kendall": "亨利·肯德尔",
    "Richard E. Taylor": "理查德·泰勒",
    "Pierre-Gilles de Gennes": "皮埃尔-吉勒·德热纳",
    "Georges Charpak": "乔治·沙尔帕克",
    "Russell A. Hulse": "拉塞尔·赫尔斯",
    "Joseph H. Taylor Jr.": "约瑟夫·泰勒",
    "Bertram N. Brockhouse": "伯特伦·布罗克豪斯",
    "Clifford G. Shull": "克利福德·沙尔",
    "Martin L. Perl": "马丁·佩尔",
    "Frederick Reines": "弗雷德里克·莱因斯",
    "David M. Lee": "戴维·李",
    "Douglas D. Osheroff": "道格拉斯·奥谢罗夫",
    "Robert C. Richardson": "罗伯特·理查森",
    "Steven Chu": "朱棣文",
    "Claude Cohen-Tannoudji": "克洛德·科昂-塔努吉",
    "William D. Phillips": "威廉·菲利普斯",
    "Robert B. Laughlin": "罗伯特·劳克林",
    "Horst L. Störmer": "霍斯特·施特默",
    "Daniel C. Tsui": "崔琦",
    "Gerardus 't Hooft": "杰拉德·特霍夫特",
    "Martinus J. G. Veltman": "马丁努斯·韦尔特曼",
    "Zhores I. Alferov": "若雷斯·阿尔费罗夫",
    "Herbert Kroemer": "赫伯特·克勒默",
    "Jack S. Kilby": "杰克·基尔比",
}

# 获奖理由（Citation）英文原文 → 中文翻译（诺贝尔奖官方获奖理由中译）。
CITATION_ZH = {
    "In recognition of the extraordinary services he has rendered by the discovery of the remarkable rays subsequently named after him.":
        "表彰他发现后来以他的名字命名的非凡射线（X 射线）所作出的杰出贡献",
    "In recognition of the extraordinary service they rendered by their researches into the influence of magnetism upon radiation phenomena.":
        "表彰他们研究磁对辐射现象的影响所作出的杰出贡献",
    "In recognition of the extraordinary services he has rendered by his discovery of spontaneous radioactivity.":
        "表彰他发现天然放射性所作出的杰出贡献",
    "In recognition of the extraordinary services they have rendered by their joint researches on the radiation phenomena discovered by Professor Henri Becquerel.":
        "表彰他们基于亨利·贝克勒尔教授所发现的辐射现象进行的联合研究所作出的杰出贡献",
    "For his investigations of the densities of the most important gases and for his discovery of argon in connection with these studies.":
        "表彰他对最重要气体密度的研究，以及在此研究中发现了氩",
    "For his work on cathode rays.":
        "表彰他在阴极射线方面的研究",
    "In recognition of the great merits of his theoretical and experimental investigations on the conduction of electricity by gases.":
        "表彰他在气体导电的理论和实验研究方面的巨大功绩",
    "For his optical precision instruments and the spectroscopic and metrological investigations carried out with their aid.":
        "表彰他发明的光学精密仪器，以及借助这些仪器进行的光谱学和计量学研究",
    "For his method of reproducing colours photographically based on the phenomenon of interference.":
        "表彰他基于干涉现象发明的彩色摄影方法",
    "In recognition of their contributions to the development of wireless telegraphy.":
        "表彰他们对无线电报发展所作出的贡献",
    "For his work on the equation of state for gases and liquids.":
        "表彰他对气体和液体状态方程的研究",
    "For his discoveries regarding the laws governing the radiation of heat.":
        "表彰他关于热辐射定律的发现",
    "For his invention of automatic regulators for use in conjunction with gas accumulators for illuminating lighthouses and buoys.":
        "表彰他发明用于与储气器配合、为灯塔和浮标照明的自动调节器",
    "For his investigations on the properties of matter at low temperatures which led, inter alia, to the production of liquid helium.":
        "表彰他对低温下物质性质的研究，这些研究尤其促成了液氦的制备",
    "For his discovery of the diffraction of X-rays by crystals.":
        "表彰他发现晶体对 X 射线的衍射",
    "For their services in the analysis of crystal structure by means of X-rays.":
        "表彰他们利用 X 射线分析晶体结构所作出的贡献",
    "For his discovery of the characteristic Röntgen radiation of the elements.":
        "表彰他发现元素的特征伦琴辐射",
    "In recognition of the services he rendered to the advancement of Physics by his discovery of energy quanta.":
        "表彰他发现能量子而对物理学进步所作出的贡献",
    "For his discovery of the Doppler effect in canal rays and the splitting of spectral lines in electric fields.":
        "表彰他发现极隧射线中的多普勒效应，以及电场中光谱线的分裂",
    "In recognition of the service he has rendered to precision measurements in Physics by his discovery of anomalies in nickel steel alloys.":
        "表彰他因发现镍钢合金的异常而对物理学精密测量所作出的贡献",
    "For his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect.":
        "表彰他对理论物理学的贡献，尤其是他发现光电效应定律",
    "for his services in the investigation of the structure of atoms and of the radiation emanating from them.":
        "表彰他在研究原子结构及其辐射方面所作出的贡献",
    "For his work on the elementary charge of electricity and on the photoelectric effect.":
        "表彰他在基本电荷和光电效应方面的研究",
    "For his discoveries and research in the field of X-ray spectroscopy.":
        "表彰他在 X 射线光谱学领域的发现与研究",
    "For their discovery of the laws governing the impact of an electron upon an atom.":
        "表彰他们发现电子与原子碰撞所遵循的定律",
    "For his work on the discontinuous structure of matter, and especially for his discovery of sedimentation equilibrium.":
        "表彰他对物质不连续结构的研究，尤其是他发现沉降平衡",
    "For his discovery of the effect named after him.":
        "表彰他发现以他名字命名的效应（康普顿效应）",
    "For his method of making the paths of electrically charged particles visible by condensation of vapour.":
        "表彰他通过蒸汽凝结使带电粒子径迹可见的方法",
    "For his work on the thermionic phenomenon and especially for the discovery of the law named after him.":
        "表彰他在热电子现象方面的研究，尤其是发现以他名字命名的定律",
    "For his discovery of the wave nature of electrons.":
        "表彰他发现电子的波动性",
    "For his work on the scattering of light and for the discovery of the effect named after him.":
        "表彰他在光的散射方面的研究，以及发现以他名字命名的效应",
    "For the creation of quantum mechanics, the application of which has, inter alia, led to the discovery of the allotropic forms of hydrogen.":
        "表彰他创立量子力学，其应用尤其促成了氢的同素异形体的发现",
    "For the discovery of new productive forms of atomic theory.":
        "表彰他发现原子理论的新颖且富有成效的形式",
    "For the discovery of the neutron.":
        "表彰他发现中子",
    "For his discovery of cosmic radiation.":
        "表彰他发现宇宙辐射",
    "For his discovery of the positron.":
        "表彰他发现正电子",
    "For their experimental discovery of the diffraction of electrons by crystals.":
        "表彰他们通过实验发现晶体对电子的衍射",
    "For his demonstrations of the existence of new radioactive elements produced by neutron irradiation, and for his related discovery of nuclear reactions brought about by slow neutrons.":
        "表彰他证明中子辐照所产生的新放射性元素的存在，以及与此相关的由慢中子引起的核反应的发现",
    "For the invention and development of the cyclotron and for results obtained with it, especially with regard to artificial radioactive elements.":
        "表彰他发明并发展回旋加速器，以及利用它取得的成果，尤其是关于人工放射性元素的成果",
    "For his contribution to the development of the molecular ray method and his discovery of the magnetic moment of the proton.":
        "表彰他对分子射线方法发展的贡献，以及他发现质子的磁矩",
    "For his resonance method for recording the magnetic properties of atomic nuclei.":
        "表彰他用共振方法记录原子核磁性的方法",
    "For the discovery of the Exclusion Principle, also called the Pauli Principle.":
        "表彰他发现不相容原理，又称泡利原理",
    "For the invention of an apparatus to produce extremely high pressures, and for the discoveries he made therewith in the field of high pressure physics.":
        "表彰他发明产生超高压的装置，以及借此在高压物理领域作出的发现",
    "For his investigations of the physics of the upper atmosphere especially for the discovery of the so-called Appleton layer.":
        "表彰他对高层大气物理的研究，尤其是发现所谓的阿普顿层",
    "For his development of the Wilson cloud chamber method, and his discoveries therewith in the fields of nuclear physics and cosmic radiation.":
        "表彰他发展威尔逊云室方法，以及借此在核物理和宇宙辐射领域的发现",
    "For his prediction of the existence of mesons on the basis of theoretical work on nuclear forces.":
        "表彰他基于核力理论研究预言了介子的存在",
    "For his development of the photographic method of studying nuclear processes and his discoveries regarding mesons made with this method.":
        "表彰他发展研究核过程的照相方法，以及利用该方法获得的关于介子的发现",
    "For their pioneer work on the transmutation of atomic nuclei by artificially accelerated atomic particles.":
        "表彰他们利用人工加速的原子粒子实现原子核嬗变的开创性工作",
    "For their development of new methods for nuclear magnetic precision measurements and discoveries in connection therewith.":
        "表彰他们发展核磁精密测量的新方法以及与之相关的发现",
    "For his demonstration of the phase contrast method, especially for his invention of the phase contrast microscope.":
        "表彰他论证相衬法，尤其是他发明相衬显微镜",
    "For his fundamental research in quantum mechanics, especially for his statistical interpretation of the wavefunction.":
        "表彰他在量子力学方面的基础研究，尤其是他对波函数的统计诠释",
    "For the coincidence method and his discoveries made therewith.":
        "表彰他提出符合方法以及借此作出的发现",
    "For his discoveries concerning the fine structure of the hydrogen spectrum.":
        "表彰他关于氢光谱精细结构的发现",
    "For his precision determination of the magnetic moment of the electron.":
        "表彰他精确测定电子的磁矩",
    "For their researches on semiconductors and their discovery of the transistor effect.":
        "表彰他们对半导体的研究以及发现晶体管效应",
    "For their penetrating investigation of the so-called parity laws which has led to important discoveries regarding the elementary particles.":
        "表彰他们对所谓的宇称定律进行的深入探究，由此带来了关于基本粒子的重要发现",
    "For the discovery and the interpretation of the Cherenkov effect.":
        "表彰他们对切伦科夫效应的发现与解释",
    "For their discovery of the antiproton.":
        "表彰他们发现反质子",
    "For the invention of the bubble chamber.":
        "表彰他发明气泡室",
    "For his pioneering studies of electron scattering in atomic nuclei and for his thereby achieved discoveries concerning the structure of the nucleons.":
        "表彰他开创性地研究原子核中的电子散射，并由此获得关于核子结构的发现",
    "For his researches concerning the resonance absorption of gamma radiation and his discovery in this connection of the effect which bears his name.":
        "表彰他关于伽马辐射共振吸收的研究，以及在此研究中发现以他名字命名的效应",
    "For his pioneering theories for condensed matter, especially liquid helium.":
        "表彰他关于凝聚态物质、尤其是液氦的开创性理论",
    "For his contributions to the theory of the atomic nucleus and the elementary particles, particularly through the discovery and application of fundamental symmetry principles.":
        "表彰他对原子核和基本粒子理论的贡献，尤其是发现并应用基本对称原理",
    "For their discoveries concerning nuclear shell structure.":
        "表彰他们关于核壳层结构的发现",
    "For fundamental work in the field of quantum electronics, which has led to the construction of oscillators and amplifiers based on the maser - laser principle.":
        "表彰他们在量子电子学领域的基础工作，这些工作促成了基于微波激射-激光原理的振荡器和放大器的建造",
    "For their fundamental work in quantum electrodynamics, with deep-ploughing consequences for the physics of elementary particles.":
        "表彰他们在量子电动力学方面的基础工作，对基本粒子物理学产生了深远影响",
    "For the discovery and development of optical methods for studying Hertzian resonances in atoms.":
        "表彰他发现并发展研究原子中赫兹共振的光学方法",
    "For his contributions to the theory of nuclear reactions, especially his discoveries concerning the energy production in stars.":
        "表彰他对核反应理论的贡献，尤其是他关于恒星中能量产生的发现",
    "For his decisive contributions to elementary particle physics, in particular the discovery of a large number of resonance states, made possible through his development of the technique of using hydrogen bubble chamber and data analysis.":
        "表彰他对基本粒子物理学的决定性贡献，尤其是通过发展氢气泡室技术和数据分析方法发现了大量共振态",
    "For his contributions and discoveries concerning the classification of elementary particles and their interactions.":
        "表彰他关于基本粒子分类及其相互作用的贡献和发现",
    "For fundamental work and discoveries in magnetohydro-dynamics with fruitful applications in different parts of plasma physics.":
        "表彰他在磁流体动力学方面的基础工作和发现，并在等离子体物理学的不同领域得到卓有成效的应用",
    "for fundamental work and discoveries concerning antiferromagnetism and ferrimagnetism which have led to important applications in solid state physics.":
        "表彰他关于反铁磁性和亚铁磁性的基础工作和发现，这些工作带来了固体物理学中的重要应用",
    "For his invention and development of the holographic method.":
        "表彰他发明并发展全息术方法",
    "For their jointly developed theory of superconductivity, usually called the BCS-theory.":
        "表彰他们共同发展的超导理论，通常称为 BCS 理论",
    "For their experimental discoveries regarding tunneling phenomena in semiconductors and superconductors, respectively.":
        "表彰他们分别关于半导体和超导体中隧穿现象的实验发现",
    "For his theoretical predictions of the properties of a supercurrent through a tunnel barrier, in particular those phenomena which are generally known as the Josephson effects.":
        "表彰他对隧穿势垒中超电流性质的理论预言，尤其是通常称为约瑟夫森效应的那些现象",
    "For their pioneering research in radio astrophysics: Ryle for his observations and inventions, in particular of the aperture synthesis technique, and Hewish for his decisive role in the discovery of pulsars.":
        "表彰他们在射电天体物理学方面的开创性研究：赖尔因其观测和发明，尤其是孔径综合技术；休伊什因在发现脉冲星中起决定性作用",
    "For the discovery of the connection between collective motion and particle motion in atomic nuclei and the development of the theory of the structure of the atomic nucleus based on this connection.":
        "表彰他们发现原子核中集体运动与粒子运动之间的联系，并基于此联系发展原子核结构理论",
    "For their pioneering work in the discovery of a heavy elementary particle of a new kind.":
        "表彰他们在发现一种新型重基本粒子方面的开创性工作",
    "For their fundamental theoretical investigations of the electronic structure of magnetic and disordered systems.":
        "表彰他们对磁性和无序系统电子结构的基础理论研究",
    "For his basic inventions and discoveries in the area of low-temperature physics.":
        "表彰他在低温物理领域的基本发明和发现",
    "For their discovery of cosmic microwave background radiation.":
        "表彰他们发现宇宙微波背景辐射",
    "For their contributions to the theory of the unified weak and electromagnetic interaction between elementary particles, including, inter alia, the prediction of the weak neutral current.":
        "表彰他们对基本粒子间弱相互作用与电磁相互作用统一理论的贡献，其中尤其包括预言弱中性流",
    "For the discovery of violations of fundamental symmetry principles in the decay of neutral K-mesons.":
        "表彰他们在中性 K 介子衰变中发现基本对称原理的破坏",
    "For their contribution to the development of laser spectroscopy.":
        "表彰他们对激光光谱学发展的贡献",
    "For his contribution to the development of high-resolution electron spectroscopy.":
        "表彰他对高分辨率电子光谱学发展的贡献",
    "For his theory for critical phenomena in connection with phase transitions.":
        "表彰他关于与相变相关的临界现象的理论",
    "For his theoretical studies of the physical processes of importance to the structure and evolution of the stars.":
        "表彰他对恒星结构和演化具有重要意义的物理过程的理论研究",
    "For his theoretical and experimental studies of the nuclear reactions of importance in the formation of the chemical elements in the universe.":
        "表彰他对宇宙中化学元素形成具有重要意义的核反应的理论和实验研究",
    "For their decisive contributions to the large project, which led to the discovery of the field particles W and Z, communicators of weak interaction.":
        "表彰他们对大型项目的决定性贡献，该项目促成了弱相互作用传递者 W 和 Z 场粒子的发现",
    "For the discovery of the quantized Hall effect.":
        "表彰他发现量子化霍尔效应",
    "For his fundamental work in electron optics, and for the design of the first electron microscope.":
        "表彰他在电子光学方面的基础工作，以及设计第一台电子显微镜",
    "For their design of the scanning tunneling microscope.":
        "表彰他们设计扫描隧道显微镜",
    "For their important break-through in the discovery of superconductivity in ceramic materials.":
        "表彰他们在陶瓷材料超导电性发现方面的重要突破",
    "For the neutrino beam method and the demonstration of the doublet structure of the leptons through the discovery of the muon neutrino.":
        "表彰他们提出中微子束方法，并通过发现 μ 子中微子证明轻子的二重态结构",
    "For the invention of the separated oscillatory fields method and its use in the hydrogen maser and other atomic clocks.":
        "表彰他发明分离振荡场方法，并将其用于氢微波激射器及其他原子钟",
    "For the development of the ion trap technique.":
        "表彰他们发展离子阱技术",
    "For their pioneering investigations concerning deep inelastic scattering of electrons on protons and bound neutrons, which have been of essential importance for the development of the quark model in particle physics.":
        "表彰他们对电子在质子和束缚中子上的深度非弹性散射进行的开创性研究，这些研究对粒子物理学中夸克模型的发展至关重要",
    "For discovering that methods developed for studying order phenomena in simple systems can be generalized to more complex forms of matter, in particular to liquid crystals and polymers.":
        "表彰他发现研究简单体系中有序现象的方法可以推广到更复杂的物质形态，尤其是液晶和聚合物",
    "For his invention and development of particle detectors, in particular the multiwire proportional chamber.":
        "表彰他发明并发展粒子探测器，尤其是多丝正比室",
    "For the discovery of a new type of pulsar, a discovery that has opened up new possibilities for the study of gravitation.":
        "表彰他们发现一种新型脉冲星，这一发现为引力研究开辟了新的可能性",
    "For the development of neutron spectroscopy.":
        "表彰他发展中子光谱学",
    "For the development of the neutron diffraction technique.":
        "表彰他发展中子衍射技术",
    "For the discovery of the tau lepton.":
        "表彰他发现 τ 轻子",
    "For the detection of the neutrino.":
        "表彰他探测到中微子",
    "For their discovery of superfluidity in helium-3.":
        "表彰他们发现氦-3 的超流性",
    "For development of methods to cool and trap atoms with laser light.":
        "表彰他们发展用激光冷却和囚禁原子的方法",
    "For their discovery of a new form of quantum fluid with fractionally charged excitations.":
        "表彰他们发现具有分数电荷激发的新型量子流体",
    "For elucidating the quantum structure of electroweak interactions in physics.":
        "表彰他们阐明物理学中电弱相互作用的量子结构",
    "For developing semiconductor heterostructures used in high-speed- and opto-electronics.":
        "表彰他们发展用于高速电子学和光电子学的半导体异质结构",
    "For his part in the invention of the integrated circuit.":
        "表彰他在集成电路发明中的贡献",
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
    women = {"Marie Curie", "Maria Goeppert Mayer"}

    # 国籍分布
    country_counter = Counter(r["country"] for r in rows)

    # 立传 / Review 状态
    done_count = sum(1 for r in rows if r["name"] in BIOGRAPHIES_DONE)

    lines: list[str] = []
    lines.append("# 20 世纪诺贝尔物理学奖得主 — OpenPhysicist 名录\n")
    lines.append(
        "> **本名录收录 1901–2000 年诺贝尔物理学奖得主，共 %d 项 / %d 位。**\n"
        ">\n"
        "> 从 Röntgen 的 X 射线到 Kilby 的集成电路：一百年间，物理学奖见证了现代物理从经典走向量子的全过程。\n"
        ">\n"
        "> 获奖理由为诺贝尔奖官方获奖理由（中文翻译）；「立传」表示是否已生成立传 Beamer，「Review」表示是否已完成事实核查。\n"
        ">\n"
        "> 数据来源：英文维基百科「List of Nobel laureates in Physics」。\n"
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
        review = "🔲"
        lines.append("| %d | %s | %s | %s | %s | %s |" % (r["year"], name_display, country, citation, bio, review))

    lines.append("\n---\n")
    lines.append("\n## 二、统计说明\n")
    lines.append("\n- **获奖年份跨度**：1901–2000")
    lines.append("- **获奖总项数**：%d 项" % total_items)
    lines.append("- **获奖总人数**：%d 位" % len(unique_people))
    lines.append("- **已立传**：%d 位（%s）" % (done_count, "、".join(sorted(BIOGRAPHIES_DONE)) if BIOGRAPHIES_DONE else "暂无"))
    lines.append("- **已 Review**：0 位")
    if double:
        lines.append("- **两度获奖者**：" + "、".join(sorted(double)) + "（唯一两度获诺贝尔物理学奖者）")
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
        "\n> **这不是一份排名，而是一部按时间展开的物理学历程：每一项获奖都标记着人类对自然认识的一次跃迁。**\n"
    )

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote:", OUT)
    print("总项数:", total_items, "总人数:", len(unique_people), "两度获奖:", sorted(double))
    print("已立传:", done_count, "位")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
