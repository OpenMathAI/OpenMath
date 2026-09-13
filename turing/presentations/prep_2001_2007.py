#!/usr/bin/env python3
"""为 2001-2007 批次前 10 位图灵奖得主备齐立传目录资产：肖像 + BGM + Makefile。"""
from pathlib import Path
import shutil

ROOT = Path('/Users/ericksun/workspace/codebuddy/OpenMathAI')
PAGES = ROOT / 'turing/pages'
AP = ROOT / 'music_audio/alex-productions'
IE = ROOT / 'music_audio/inspiring-electronic'
PRES = ROOT / 'turing/presentations'

PLAN = {
    "Kristen_Nygaard": ("2001/Kristen Nygaard/images/Kristen-Nygaard-SBLP-1997-head.png",
                        "Kristen-Nygaard-SBLP-1997-head.png",
                        AP / "80-K5f65-22sY4-Tragedy.wav", "Tragedy.wav"),
    "Ron_Rivest": ("2002/Ron Rivest/images/500px-Ronald_L_Rivest_photo.jpg",
                   "Ronald_L_Rivest_photo.jpg",
                   AP / "83-DXAblXgCK-k-With-Me.wav", "WithMe.wav"),
    "Adi_Shamir": ("2002/Adi Shamir/images/500px-Adi_Shamir_Royal_Society.jpg",
                   "Adi_Shamir_Royal_Society.jpg",
                   AP / "76-V5T_kW2PH_s-Eternals.wav", "Eternals.wav"),
    "Leonard_Adleman": ("2002/Leonard Adleman/images/500px-Len-mankin-pic.jpg",
                        "Len-mankin-pic.jpg",
                        AP / "48-QL3O8MUFAm4-Cinematic-Experience.wav", "CinematicExperience.wav"),
    "Alan_Kay": ("2003/Alan Kay/images/500px-Alan_Kay_-_Receiving_the_Kyoto_Prize.jpg",
                 "Alan_Kay_Kyoto.jpg",
                 AP / "44-JoyIRE5k2Yo-Daylight.wav", "Daylight.wav"),
    "Vint_Cerf": ("2004/Vint Cerf/images/500px-Dr_Vint_Cerf_ForMemRS_cropped_.jpg",
                  "Vint_Cerf_ForMemRS.jpg",
                  AP / "89-geyy8_WXDK0-PAST.wav", "PAST.wav"),
    "Robert_Kahn": ("2004/Robert Kahn (computer scientist)/images/500px-Bob_Kahn.jpg",
                    "Bob_Kahn.jpg",
                    IE / "14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav", "ThroughTheDarkness.wav"),
    "Peter_Naur": ("2005/Peter Naur/images/500px-Peternaur.JPG",
                   "Peternaur.jpg",
                   IE / "24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav",
                   "LastHope.wav"),
    "Frances_Allen": ("2006/Frances Allen/images/500px-Allen_mg_2528-3750K-b.jpg",
                      "Allen_mg_2528-3750K-b.jpg",
                      IE / "12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav",
                      "EmpireCollapse.wav"),
    "Edmund_M._Clarke": ("2007/Edmund M. Clarke/images/Edmund_Clarke_FLoC_2006.jpg",
                         "Edmund_Clarke_FLoC_2006.jpg",
                         IE / "20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav",
                         "Ascension.wav"),
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
