aantal = int(input('Geef getal: '))
base = str(input('Geef een base: '))
basen = base
soorten_basen = ''
for i in range(1, aantal):
    base = str(input('Geef een base: '))
    soorten_basen += basen
    if base not in soorten_basen:
        basen = basen + ' ' + base

if len(basen) - 3 == 4:
    mes = 'De DNA-keting bevat 4 verschillende soorten basen: {} '.format(basen)
elif len(basen) - 2 == 3:
    mes = 'De DNA-keting bevat 3 verschillende soorten basen: {} '.format(basen)
elif len(basen) - 1 == 2:
    mes = 'De DNA-keting bevat 2 verschillende soorten basen: {} '.format(basen)
else:
    mes = 'De DNA-keting bevat 1 soort base: {} '.format(basen)
print(mes)
