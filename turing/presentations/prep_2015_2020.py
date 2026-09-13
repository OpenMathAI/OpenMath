#!/usr/bin/env python3
"""为 2015-2020 批次 10 位图灵奖得主备齐立传目录资产：肖像 + BGM + Makefile。"""
from pathlib import Path
import shutil

ROOT = Path('/Users/ericksun/workspace/codebuddy/OpenMathAI')
PAGES = ROOT / 'turing/pages'
AP = ROOT / 'music_audio/alex-productions'
IE = ROOT / 'music_audio/inspiring-electronic'
PRES = ROOT / 'turing/presentations'

PLAN = {
    "Martin_Hellman": ("2015/Martin Hellman/images/Martin-Hellman.jpg",
                       "Martin-Hellman.jpg",
                       AP / "42-SyPUvzEkPyc-Timeless.wav",
                       "Timeless.wav"),
    "Tim_Berners-Lee": ("2016/Tim Berners-Lee/images/250px-Tim_Berners-Lee.jpg",
                        "Tim_Berners-Lee.jpg",
                        IE / "03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav",
                        "FallingApart.wav"),
    "John_L._Hennessy": ("2017/John L. Hennessy/images/500px-John_L._Hennessy_by_Christopher_Michel_in_2024_01.jpg",
                         "John_L._Hennessy_2024.jpg",
                         AP / "36-aqLUvpAdLNQ-Awaken.wav",
                         "Awaken.wav"),
    "David_Patterson": ("2017/David Patterson (computer scientist)/images/David_A_Patterson_cropped_.jpg",
                        "David_A_Patterson_cropped_.jpg",
                        AP / "92-WEqfdRXU3IU-SEA.wav",
                        "SEA.wav"),
    "Yoshua_Bengio": ("2018/Yoshua Bengio/images/500px-SD_2025_-_Yoshua_Bengio_04_cropped_.jpg",
                      "Yoshua_Bengio_SD2025.jpg",
                      AP / "86-5ETNuoDcBg4-Nostalgia.wav",
                      "Nostalgia.wav"),
    "Geoffrey_Hinton": ("2018/Geoffrey Hinton/images/500px-Geoffrey_Hinton_in_2026.jpg",
                        "Geoffrey_Hinton_in_2026.jpg",
                        AP / "34-pILVwyuW3jw-Savage.wav",
                        "Savage.wav"),
    "Yann_LeCun": ("2018/Yann LeCun/images/500px-Laura_Chaubard_Yann_Le_Cun_-_2024_53814052697_cropped_.jpg",
                   "Yann_LeCun_2024.jpg",
                   AP / "80-K5f65-22sY4-Tragedy.wav",
                   "Tragedy.wav"),
    "Edwin_Catmull": ("2019/Edwin Catmull/images/500px-Ed_Catmull_at_Web_Summit_2015_cropped_.jpg",
                      "Ed_Catmull_WebSummit2015.jpg",
                      AP / "83-DXAblXgCK-k-With-Me.wav",
                      "WithMe.wav"),
    "Pat_Hanrahan": ("2019/Pat Hanrahan/images/500px-Pat_Hanrahan_Tableau_Customer_Conference_2009.jpg",
                     "Pat_Hanrahan_Tableau_2009.jpg",
                     AP / "76-V5T_kW2PH_s-Eternals.wav",
                     "Eternals.wav"),
    # Alfred_Aho：无肖像，仅 BGM + Makefile（提示词 §11 已写明装饰圆占位）
    "Alfred_Aho": (None, None,
                   AP / "48-QL3O8MUFAm4-Cinematic-Experience.wav",
                   "CinematicExperience.wav"),
}

def main():
    mk = (PRES / 'Marvin_Minsky/Makefile').read_text()
    for d, (src, pname, wsrc, wname) in PLAN.items():
        dd = PRES / d
        (dd / 'images').mkdir(parents=True, exist_ok=True)
        if src:
            shutil.copy(PAGES / src, dd / 'images' / pname)
        shutil.copy(wsrc, dd / wname)
        (dd / 'Makefile').write_text(
            mk.replace('MAIN        = Marvin_Minsky_zh', 'MAIN        = ' + d + '_zh')
              .replace('VIDEO_NAME  = Marvin_Minsky_zh', 'VIDEO_NAME  = ' + d + '_zh'))
        print(d, 'OK')

if __name__ == '__main__':
    main()
