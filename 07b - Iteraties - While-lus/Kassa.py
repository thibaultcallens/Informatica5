bedrag = float(input('bedrag: '))
totaalbedrag = 0


while bedrag != 0:
    totaalbedrag += bedrag
    bedrag = float(input('bedrag: '))

print('De totale prijs is € {:.2f}'.format(totaalbedrag))


