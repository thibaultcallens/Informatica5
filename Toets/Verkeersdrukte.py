vdv = float(input('verkeersdichtheid vrachtvervoer: '))
sv = int(input('snelheid vrachtvervoer: '))
vda = float(input('verkeersdichtheid autos: '))
sa = int(input('snelheid autos: '))

pv = min((vdv * sv) / 40, 1)
pa = min((vda * sa) / 40, 1)

if min(pv, pa) > 0.7:
    print('zwart')
elif max(pv, pa) > 0.7 and abs(pv - pa) < 0.2:
    print('rood')
elif abs(pv - pa) > 0.7 :
    print('geel')
else:
    print('groen')



