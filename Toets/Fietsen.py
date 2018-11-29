snelheid_stijn = int(input('Geef snelheid stijn: '))
snelheid_kaat = int(input('Geef snelheid kaat: '))
afstand = int(input('Geef afstand: '))
ontmoetingstijdstip = 0

while afstand > 0:
    ontmoetingstijdstip += 1
    afstand -= snelheid_kaat + snelheid_stijn

print('Na {} s hebben Stijn en Kaat elkaar ontmoet.'.format(ontmoetingstijdstip))