#!/usr/bin/env python3
"""为 1993-2001 批次前 10 位图灵奖得主备齐立传目录资产：肖像 + BGM + Makefile。"""
from pathlib import Path
import shutil

ROOT = Path('/Users/ericksun/workspace/codebuddy/OpenMathAI')
PAGES = ROOT / 'turing/pages'
AP = ROOT / 'music_audio/alex-productions'
IE = ROOT / 'music_audio/inspiring-electronic'
PRES = ROOT / 'turing/presentations'

PLAN = {
    "Juris_Hartmanis": ("1993/Juris Hartmanis/images/Juris_Hartmanis_2002_.jpg",
                        "Juris_Hartmanis_2002_.jpg",
                        AP / "35-jqIDnltiDRI-The-Flow-of-Time.wav", "TheFlowOfTime.wav"),
    "Richard_E._Stearns": ("1993/Richard E. Stearns/images/500px-Dick_Stearns.jpg",
                           "Dick_Stearns.jpg",
                           AP / "33--_CEmB_dHpA-Expedition.wav", "Expedition.wav"),
    "Edward_Feigenbaum": ("1994/Edward Feigenbaum/images/500px-27._Dr._Edward_A._Feigenbaum_1994-1997.jpg",
                          "Edward_Feigenbaum_1994.jpg",
                          IE / "23-GiwYLGgJw7w-Ghostwriter Music - Pathfinder (Composed by Daniel Beijbom - Recorded in Budapest).wav",
                          "Pathfinder.wav"),
    "Raj_Reddy": ("1994/Raj Reddy/images/500px-AAAI_2026_-_Raj_Reddy_01_cropped_.jpg",
                  "Raj_Reddy_2026.jpg",
                  AP / "74-oK8HN0FsZmc-New-Lands.wav", "NewLands.wav"),
    "Manuel_Blum": ("1995/Manuel Blum/images/Blum_manuel_lenore_avrim.jpg",
                    "Blum_manuel_lenore_avrim.jpg",
                    AP / "42-SyPUvzEkPyc-Timeless.wav", "Timeless.wav"),
    "Amir_Pnueli": ("1996/Amir Pnueli/images/Amir_Pnueli.jpg",
                    "Amir_Pnueli.jpg",
                    IE / "03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav", "FallingApart.wav"),
    "Douglas_Engelbart": ("1997/Douglas Engelbart/images/SRI_Douglas_Engelbart_1968_cropped_.jpg",
                          "SRI_Douglas_Engelbart_1968_cropped_.jpg",
                          AP / "36-aqLUvpAdLNQ-Awaken.wav", "Awaken.wav"),
    "Jim_Gray": ("1998/Jim Gray (computer scientist)/images/500px-Jim_Gray_Computing_in_the_21st_Century_2006.jpg",
                 "Jim_Gray_2006.jpg",
                 AP / "92-WEqfdRXU3IU-SEA.wav", "SEA.wav"),
    "Fred_Brooks": ("1999/Fred Brooks/images/500px-Fred_Brooks_cropped_square_.jpg",
                    "Fred_Brooks_cropped_square_.jpg",
                    AP / "86-5ETNuoDcBg4-Nostalgia.wav", "Nostalgia.wav"),
    "Ole-Johan_Dahl": ("2001/Ole-Johan Dahl/images/Ole-Johan_Dahl.jpg",
                       "Ole-Johan_Dahl.jpg",
                       AP / "34-pILVwyuW3jw-Savage.wav", "Savage.wav"),
}

def main():
    mk = (PRES / 'Marvin_Minsky/Makefile').read_text()
    for d, (src, pname, wsrc, wname) in PLAN.items():
        dd = PRES / d
        (dd / 'images').mkdir(parents=True, exist_ok=True)
        shutil.copy(PAGES / src, dd / 'images' / pname)
        shutil.copy(wsrc, dd / wname)
        (dd / 'Makefile').write_text(
            mk.replace('MAIN        = Marvin_Minsky_zh', 'MAIN        = ' + d + '_zh')
              .replace('VIDEO_NAME  = Marvin_Minsky_zh', 'VIDEO_NAME  = ' + d + '_zh'))
        print(d, 'OK')

if __name__ == '__main__':
    main()
