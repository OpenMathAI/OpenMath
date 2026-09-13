#!/usr/bin/env python3
"""为 2007-2015 批次前 10 位图灵奖得主备齐立传目录资产：肖像 + BGM + Makefile。"""
from pathlib import Path
import shutil

ROOT = Path('/Users/ericksun/workspace/codebuddy/OpenMathAI')
PAGES = ROOT / 'turing/pages'
AP = ROOT / 'music_audio/alex-productions'
IE = ROOT / 'music_audio/inspiring-electronic'
PRES = ROOT / 'turing/presentations'

PLAN = {
    "E._Allen_Emerson": ("2007/E. Allen Emerson/images/500px-E-allen-emerson_3x4_cropped_.jpg",
                         "E-allen-emerson_3x4_cropped_.jpg",
                         IE / "19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav",
                         "TheInvisibleLight.wav"),
    "Joseph_Sifakis": ("2007/Joseph Sifakis/images/500px-Joseph_Sifakis_2018.jpg",
                       "Joseph_Sifakis_2018.jpg",
                       IE / "25-l3Fsk4R6eys-Really Slow Motion & Giant Apes - Winds Of Freedom (Epic Heroic Orchestral).wav",
                       "WindsOfFreedom.wav"),
    "Barbara_Liskov": ("2008/Barbara Liskov/images/500px-Barbara_Liskov_MIT_computer_scientist_2010.jpg",
                       "Barbara_Liskov_MIT_2010.jpg",
                       IE / "15-w6kT1BfvETI-Really Slow Motion - Shine Like The Sun (Epic Beautiful Uplifting).wav",
                       "ShineLikeTheSun.wav"),
    "Charles_P._Thacker": ("2009/Charles P. Thacker/images/500px-Chuckthacker_cropped_.jpg",
                           "Chuckthacker_cropped_.jpg",
                           IE / "04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav",
                           "Mirage.wav"),
    "Leslie_Valiant": ("2010/Leslie Valiant/images/500px-Leslie_Valiant_34913684313_.jpg",
                       "Leslie_Valiant.jpg",
                       IE / "16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav",
                       "Lonesome.wav"),
    "Judea_Pearl": ("2011/Judea Pearl/images/500px-Judea_Pearl_at_NIPS_2013_11781981594_.jpg",
                    "Judea_Pearl_NIPS_2013.jpg",
                    IE / "17-_DA0mdtL-jI-Nostalgy - by AShamaluevMusic ｜ Sad Cinematic Music For Videos, Documentaries & Films.wav",
                    "Nostalgy.wav"),
    "Shafi_Goldwasser": ("2012/Shafi Goldwasser/images/500px-Shafi_Goldwasser.JPG",
                         "Shafi_Goldwasser.jpg",
                         AP / "35-jqIDnltiDRI-The-Flow-of-Time.wav",
                         "TheFlowOfTime.wav"),
    "Silvio_Micali": ("2012/Silvio Micali/images/500px-Silvio_Micali.jpg",
                      "Silvio_Micali.jpg",
                      AP / "33--_CEmB_dHpA-Expedition.wav",
                      "Expedition.wav"),
    "Michael_Stonebraker": ("2014/Michael Stonebraker/images/500px-Michael_Stonebraker_P1120062.jpg",
                            "Michael_Stonebraker_P1120062.jpg",
                            IE / "23-GiwYLGgJw7w-Ghostwriter Music - Pathfinder (Composed by Daniel Beijbom - Recorded in Budapest).wav",
                            "Pathfinder.wav"),
    "Whitfield_Diffie": ("2015/Whitfield Diffie/images/500px-Whitfield_Diffie_Royal_Society.jpg",
                         "Whitfield_Diffie_Royal_Society.jpg",
                         AP / "74-oK8HN0FsZmc-New-Lands.wav",
                         "NewLands.wav"),
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
