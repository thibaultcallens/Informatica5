getal = 0
while getal < 5:
    print(getal)
    getal +=

for i in range(0, 5):
    print(i)

###############################

vorst_periode = 0
temperatuur = int(input('Dagtemperatuur: '))

while temperatuur <= 0:
    vorst_periode += 1
    temperatuur = int(input('Dagtemperatuur: '))

print(vorst_periode)

#####################################

from random import randint
temp = randint(-10, 30)
vorst_periode = 0

while temp < 0:
    vorst_periode += 1
    temp = randint(-10, 30)

print(vorst_periode, 'dagen')

######################################

bod = float(input('startprijs: '))
doorgedraaid = float(input('doorgedraaid onder: '))

akkoord = int(input('€{:.2f}? (0/1): '.format(bod)))

while (not akkoord) and (bod >= doorgedraaid + 0.01):
    bod -= 0.01
    akkoord = int(input('€{:.2f}? (0/1): '.format(bod)))

if akkoord:
    print('verkocht aan {:.2f}'.format(bod))
else:
    print('doorgedraaid')