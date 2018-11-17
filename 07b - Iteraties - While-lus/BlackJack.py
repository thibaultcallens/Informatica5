tot_kaarten = 0
kaart = int(input('Geef getal (1 - 11): '))

while kaart != 0 and tot_kaarten < 21:
    tot_kaarten += kaart
    if tot_kaarten < 21:
        kaart = int(input('Geef getal(0 - 11): '))

if tot_kaarten == 21:
    print('Gewonnen!')
elif tot_kaarten > 21:
    print('Verbrand ({})'.format(tot_kaarten))
else:
    print('Voorzichtig gespeeld ({})'.format(tot_kaarten))