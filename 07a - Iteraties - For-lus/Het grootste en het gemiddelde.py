aantal_getallen = int(input('Geef aantal getallen: '))

max = 0
som = 0

for i in range(aantal_getallen):
    getal = int(input('Geef een getal: '))
    if i == 0:
        max = getal
    elif getal > max:
        max = getal
    som += getal

gemiddelde = round((som / aantal_getallen), 2)

print('{} {:d} {} {:.2f}'.format('Het grootste getal is', max , 'en het gemiddelde is', gemiddelde))