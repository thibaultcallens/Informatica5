windsnelheid = int(input('De windsnelheid is gelijk aan: '))

if windsnelheid < 154 and windsnelheid > 118:
    print('categorie 1')
elif windsnelheid < 178 and windsnelheid > 118:
    print('categorie 2')
elif windsnelheid < 210 and windsnelheid > 118:
    print('categorie 3')
elif windsnelheid < 250 and windsnelheid > 118:
    print('categorie 4')
elif windsnelheid >= 250 and windsnelheid > 118:
    print('categorie 5')
else:
    print('geen orkaan')
