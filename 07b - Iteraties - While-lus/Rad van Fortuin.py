woord = str(input('Geef het woord: '))
gedraaide_geldbedrag = int(input('Geef bedrag: '))
bedrag = 0
gegokte_letter = str(input('Geef gegokte letter: '))

while gegokte_letter in woord:
    bedrag += gedraaide_geldbedrag
    gegokte_letter = str(input('Geef gegokte letter: '))

print(bedrag)
