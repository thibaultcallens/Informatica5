a = float(input('Geef a: '))
b = float(input('Geef b: '))

x = 'x'
fx = '2(x - 3)^2 + 4'

gx = '2' + '(x - ' + str(int(3 + a)) + ')^2' + ' + ' + str(int(4 + b))

print('f(x) = ' + fx)

resultaat = (gx)
print('g(x) = ' + str(resultaat))