woord = str(input('Geef het woord: '))
gedraaide_geldbedrag = int(input('Geef bedrag: '))
bedrag = 0
gegokte_letter = str(input('Geef gegokte letter: '))
vreeself = ''

while gegokte_letter in woord and gegokte_letter not in vreeself:
    bedrag += gedraaide_geldbedrag
    vreeself += gegokte_letter
    gegokte_letter = str(input('Geef gegokte letter: '))

print(bedrag)
