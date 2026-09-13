#!/usr/bin/env python3
"""为最后一批 8 位图灵奖得主备齐立传目录资产：肖像 + BGM + Makefile（本批仅出 pdf，不出 mp4）。"""
from pathlib import Path
import shutil

ROOT = Path('/Users/ericksun/workspace/codebuddy/OpenMathAI')
PAGES = ROOT / 'turing/pages'
AP = ROOT / 'music_audio/alex-productions'
IE = ROOT / 'music_audio/inspiring-electronic'
PRES = ROOT / 'turing/presentations'

PLAN = {
    # Jeffrey_Ullman：无肖像，装饰圆占位（提示词 §11 已写明）
    "Jeffrey_Ullman": (None, None,
                       AP / "44-JoyIRE5k2Yo-Daylight.wav",
                       "Daylight.wav"),
    "Jack_Dongarra": ("2021/Jack Dongarra/images/500px-Jack-dongarra-2022.jpg",
                      "Jack_Dongarra_2022.jpg",
                      AP / "89-geyy8_WXDK0-PAST.wav",
                      "PAST.wav"),
    "Robert_Metcalfe": ("2022/Robert Metcalfe/images/With_Bob_Metcalfe_cropped_.jpg",
                        "With_Bob_Metcalfe_cropped_.jpg",
                        IE / "14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav",
                        "ThroughTheDarkness.wav"),
    "Avi_Wigderson": ("2023/Avi Wigderson/images/Avi_Wigderson_London_2012_Cropped.jpg",
                      "Avi_Wigderson_London_2012_Cropped.jpg",
                      IE / "24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav",
                      "LastHope.wav"),
    # Andrew_Barto：无肖像，装饰圆占位（提示词 §11 已写明）
    "Andrew_Barto": (None, None,
                     IE / "12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav",
                     "EmpireCollapse.wav"),
    "Richard_S._Sutton": ("2024/Richard S. Sutton/images/500px-SD_2025_-_Richard_Sutton_01_cropped_.jpg",
                          "Richard_Sutton_SD2025.jpg",
                          IE / "20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav",
                          "Ascension.wav"),
    "Charles_H._Bennett": ("2025/Charles H. Bennett (physicist)/images/500px-Dr._Charles_Bennett_IBM_Fellow.jpg",
                           "Dr_Charles_Bennett_IBM_Fellow.jpg",
                           IE / "19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav",
                           "TheInvisibleLight.wav"),
    "Gilles_Brassard": ("2025/Gilles Brassard/images/500px-Gilles_Brassard_2019_.jpg",
                        "Gilles_Brassard_2019.jpg",
                        IE / "25-l3Fsk4R6eys-Really Slow Motion & Giant Apes - Winds Of Freedom (Epic Heroic Orchestral).wav",
                        "WindsOfFreedom.wav"),
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
