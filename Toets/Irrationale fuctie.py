from math import sqrt

x = (input('geef x ∈ R: '))

fx = sqrt(int(x) - 2)



if int(x) == 2:
    print('{:.2f}'.format(int(x)) + ' is nulpunt van f')
elif int(x) > 2:
    print(f('{:.2f}'.format(int(x)) + '=' + ' {:.f2}'.format(fx)))
else:
    print('{:.2f}'.format(int(x)) + ' ∉ dom(f)')





