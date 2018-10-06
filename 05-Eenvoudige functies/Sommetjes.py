a = int(input('a: '))
b = int(input('b: '))
c = a + b
c2 = (a + b) * 10
c3 = (a + b) * 100
c4 = (a + b) * 1000
c5 = (a + b) * 10000

print('{:>6} + {:<6} = {:<6}'.format(a, b, c))
print('{:>6} + {:<6} = {:<6}'.format(a * 10, b * 10, c2))
print('{:>6} + {:<6} = {:<6}'.format(a * 100, b * 100, c3))
print('{:>6} + {:<6} = {:<6}'.format(a * 1000, b * 1000, c4))
print('{:>6} + {:<6} = {:<6}'.format(a * 10000, b * 10000, c5))




