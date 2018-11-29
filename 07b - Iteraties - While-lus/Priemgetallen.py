getal = int(input('Geef een getal: '))
n = 2
i = 1
while n < getal:
    if (getal % n) == 0:
        antw = '{} is geen priemgetal'.format(getal)
        i = 0
    n += 1
if i and getal != 1:
    antw = '{} is een priemgetal'.format(getal)
elif getal == 1:
    antw = '1 is geen priemgetal'
print(antw)

##########################################

getal = int(input('getal: '))

# zolang je het niet kan delen door 2,3,4 is het een priegetal

deler = 2

while getal % deler != 0 and getal != 1:
    deler += 1

if deler == getal:
    print('priemgetal')
else:
    print('geen priemgetal')

###########################################
