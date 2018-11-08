a1 = int(input('worp 1 aanvaller: '))
a2 = int(input('worp 2 aanvaller: '))
a3 = int(input('worp 3 aanvaller: '))
v1 = int(input('worp 1 verdediger: '))
v2 = int(input('worp 2 verdediger: '))

# sorteren
sa1 = max(a1, a2, a3)
sa2 = a1 + a2 + a3 - sa1 - min(a1, a2, a3)

sv1 = max(v1, v2)
sv2 = min(v1, v2)

if sa1 > sv1 and sa2 > sv2:
    mes = 'aanvaller verliest 0, v verliest 2 '
elif sv1 >= sa1 and sv2 >= sa2:
    mes = 'aanvaller verliest 2, v verliest 0'
else:
    mes = 'a verliest 1, v verliest 1'

print(mes)




