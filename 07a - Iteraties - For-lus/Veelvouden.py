r = int(input('Geef een getal kleiner dan 100: '))

som_veelvouden = 0

for i in range(r, 101, r):
    som_veelvouden += i

print(som_veelvouden)
