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
