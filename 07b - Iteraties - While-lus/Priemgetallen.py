getal = int(input('Geef een getal: '))
if getal > 1:
    for i in range(2, getal):
        if (getal % i) == 0:
            print(getal, "is geen priemgetal")
            break
    else:
        print(getal, "is een priemgetal")
else:
  print('{} is geen priemgetal'.format(getal))