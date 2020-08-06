# MyQuickBMSCollection
My collection of [QuickBMS](https://aluigi.altervista.org/quickbms.htm) scripts that decrypt &amp; unpack files of some underground games

| Script | Game | Unpacks | Notes
| -- | -- | -- | -- |
| [apuk.bms](apuk.bms) | Tajemnicza Wyspa (Mysterious Island) | main.hal ("APUK" - \x41\x50\x55\x4B) | - |
| [moorhuhn_kart.bms](moorhuhn_kart.bms) | Wyścigi Kurczaków XXL (Moorhuhn Kart XXL) | mhk.dat (\x5C\x73) | highscor.dat has the same xor key |
| [maluchracer.bms](maluchracer.bms) | Maluch Racer / Czeski Rajd (possibly Trabi Racer and others on the same engine) | menu.dat, misc.dat, sound.dat, track/\*.dat | intro.dat is not packed, it is normal video file.
| [carl_caveman.bms](carl_caveman.bms) | Karol Jaskiniowiec (Carl the Caveman) | data.hdp, pack\*.lp | - |
| [doubledigger.bms](doubledigger.bms) | Double Digger | fonts.pak, interface.pak, \*.lev, \x78\x19 | - |
| [stand_o_food.bms](stand_o_food.bms) | Stand o Food (Szalone Bistro) | \*.mjp | two .jpg inside each file |
| [maluch_v1.bms](maluch_v1.bms) | Maluch Racer (v1/Delux) and others on the same engine | \*.mar | - |
| [turtle.bms](turtle.bms) | Żółwik i Skarb Piratów (Turtle) | Data.Pak | The same pack method as in Maluch Racer v2, other keys |
| [gunship_tankkiller.bms](gunship_tankkiller.bms) | Gunship - Tank killer | Data.Pak | - |
| [midnight_racing.bms](midnight_racing.bms) | Polskie Derby (Midnight Racing Extended Edition) | mr.dat, ct.dat "This is an internal binary data file, and should not be deleted or modified" | 

Additionaly I made simple python script that can extract two keys needed to unpack files used in Blitz3D engine [blitz_extractor.py](blitz_extractor.py). You can use the keys by replacing the existing keys placed in turtle.bms or maluchracer.bms with those you got from blitz_extractor.py.
