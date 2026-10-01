import re
from pathlib import Path

ZH_17 = {
    'Marin_Mersenne': '马兰·梅森',
    'René_Descartes': '勒内·笛卡尔',
    'Bonaventura_Cavalieri': '博纳文图拉·卡瓦列里',
    'Pierre_de_Fermat': '皮埃尔·德·费马',
    'Evangelista_Torricelli': '埃万杰利斯塔·托里拆利',
    'John_Wallis': '约翰·沃利斯',
    'Blaise_Pascal': '布莱兹·帕斯卡',
    'Christiaan_Huygens': '克里斯蒂安·惠更斯',
    'Isaac_Barrow': '艾萨克·巴罗',
    'James_Gregory': '詹姆斯·格雷戈里',
    'Isaac_Newton': '艾萨克·牛顿',
    'Gottfried_Wilhelm_Leibniz': '戈特弗里德·威廉·莱布尼茨',
    'Jacob_Bernoulli': '雅各布·伯努利',
    'Johann_Bernoulli': '约翰·伯努利',
}

ZH_18 = {
    'Abraham_de_Moivre': '亚伯拉罕·棣莫弗',
    'Brook_Taylor': '布鲁克·泰勒',
    'Colin_Maclaurin': '科林·麦克劳林',
    'Daniel_Bernoulli': '丹尼尔·伯努利',
    'Leonhard_Euler': '莱昂哈德·欧拉',
    'Alexis_Clairaut': '亚历克西·克莱罗',
    "Jean_le_Rond_d'Alembert": '让·勒朗·达朗贝尔',
    'Johann_Heinrich_Lambert': '约翰·海因里希·兰伯特',
    'Étienne_Bézout': '艾蒂安·贝祖',
    'Edward_Waring': '爱德华·华林',
    'Joseph-Louis_Lagrange': '约瑟夫-路易·拉格朗日',
    'Gaspard_Monge': '加斯帕尔·蒙日',
    'Pierre-Simon_Laplace': '皮埃尔-西蒙·拉普拉斯',
}


def build_dict(d):
    lines = ['ZH_NAMES = {']
    for k, v in d.items():
        lines.append(f"    {k!r}: {v!r},")
    lines.append('}')
    return '\n'.join(lines)


def gen(src_path, zh_dict, century_zh, century_en):
    s = Path(src_path).read_text(encoding='utf-8')
    s = re.sub(r"ZH_NAMES = \{.*?\n\}", build_dict(zh_dict), s, flags=re.DOTALL)
    s = s.replace('19 世纪数学家 · 页面索引', f'{century_zh}数学家 · 页面索引')
    s = s.replace('19th Century Mathematicians', f'{century_en} Mathematicians')
    Path(src_path).write_text(s, encoding='utf-8')
    print('updated', src_path)


gen('presentations/17th_century/pages/generate_index.py', ZH_17, '17 世纪', '17th Century')
gen('presentations/18th_century/pages/generate_index.py', ZH_18, '18 世纪', '18th Century')
