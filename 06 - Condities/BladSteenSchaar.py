keuze_speler1 = input('keuze speler 1(blad/steen/schaar) ')
keuze_speler2 = input('keuze speler 2(blad/steen/schaar) ')

if keuze_speler1 == 'blad' and keuze_speler2 == 'schaar':
    print('speler 2 wint')
if keuze_speler1 == 'blad' and keuze_speler2 == 'steen':
    print('speler 1 wint')
if keuze_speler1 == 'schaar' and keuze_speler2 == 'blad':
    print('speler 1 wint')
if keuze_speler1 == 'schaar' and keuze_speler2 == 'steen':
    print('speler 2 wint')
if keuze_speler1 == 'steen' and keuze_speler2 == 'blad':
    print('speler 2 wint')
if keuze_speler1 == 'steen' and keuze_speler2 == 'schaar':
    print('speler 1 wint')
if keuze_speler1 == keuze_speler2:
    print('onbeslist')