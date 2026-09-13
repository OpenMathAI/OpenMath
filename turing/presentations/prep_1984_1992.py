#!/usr/bin/env python3
"""为 1984-1992 批次 10 位图灵奖得主备齐立传目录资产：肖像 + BGM + Makefile。"""
from pathlib import Path
import shutil

ROOT = Path('/Users/ericksun/workspace/codebuddy/OpenMathAI')
PAGES = ROOT / 'turing/pages'
IE = ROOT / 'music_audio/inspiring-electronic'
PRES = ROOT / 'turing/presentations'

PLAN = {
    "Niklaus_Wirth": ("1984/Niklaus Wirth/images/500px-Niklaus_Wirth_UrGU.jpg",
                      "Niklaus_Wirth_UrGU.jpg",
                      "14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav",
                      "ThroughTheDarkness.wav"),
    "Richard_M._Karp": ("1985/Richard M. Karp/images/500px-Karp_mg_7725-b.cr2.jpg",
                        "Karp_2009.jpg",
                        "24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav",
                        "LastHope.wav"),
    "John_Hopcroft": ("1986/John Hopcroft/images/500px-Hopcrofg_cropped2_.jpg",
                      "Hopcroft.jpg",
                      "12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav",
                      "EmpireCollapse.wav"),
    "Robert_Tarjan": ("1986/Robert Tarjan/images/500px-Bob_Tarjan.jpg",
                      "Bob_Tarjan.jpg",
                      "20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav",
                      "Ascension.wav"),
    "John_Cocke": ("1987/John Cocke (computer scientist)/images/John_Cocke_computer_scientist_.jpg",
                   "John_Cocke.jpg",
                   "19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav",
                   "TheInvisibleLight.wav"),
    "Ivan_Sutherland": ("1988/Ivan Sutherland/images/Ivan_Sutherland_at_CHM.jpg",
                        "Ivan_Sutherland_at_CHM.jpg",
                        "25-l3Fsk4R6eys-Really Slow Motion & Giant Apes - Winds Of Freedom (Epic Heroic Orchestral).wav",
                        "WindsOfFreedom.wav"),
    "William_Kahan": ("1989/William Kahan/images/500px-William_Kahan_2008.jpg",
                      "William_Kahan_2008.jpg",
                      "15-w6kT1BfvETI-Really Slow Motion - Shine Like The Sun (Epic Beautiful Uplifting).wav",
                      "ShineLikeTheSun.wav"),
    "Fernando_J._Corbató": ("1990/Fernando J. Corbató/images/Fernando_Corbato.jpg",
                            "Fernando_Corbato.jpg",
                            "04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav",
                            "Mirage.wav"),
    "Robin_Milner": ("1991/Robin Milner/images/Robin_Milner.jpg",
                     "Robin_Milner.jpg",
                     "16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav",
                     "Lonesome.wav"),
    "Butler_Lampson": ("1992/Butler Lampson/images/Butler_Lampson_Royal_Society_cropped_.jpg",
                       "Butler_Lampson_Royal_Society_cropped_.jpg",
                       "17-_DA0mdtL-jI-Nostalgy - by AShamaluevMusic ｜ Sad Cinematic Music For Videos, Documentaries & Films.wav",
                       "Nostalgy.wav"),
}

def main():
    mk = (PRES / 'Marvin_Minsky/Makefile').read_text()
    for d, (src, pname, wsrc, wname) in PLAN.items():
        dd = PRES / d
        (dd / 'images').mkdir(parents=True, exist_ok=True)
        shutil.copy(PAGES / src, dd / 'images' / pname)
        shutil.copy(IE / wsrc, dd / wname)
        (dd / 'Makefile').write_text(
            mk.replace('MAIN        = Marvin_Minsky_zh', 'MAIN        = ' + d + '_zh')
              .replace('VIDEO_NAME  = Marvin_Minsky_zh', 'VIDEO_NAME  = ' + d + '_zh'))
        print(d, 'OK')

if __name__ == '__main__':
    main()
