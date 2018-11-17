x = int(input('Geef een getal: '))

if x == 0:
    print('0')
elif x == 1 or x == 2:
    print('1')
elif x > 2:
    def fib(n):
        a,b = 1,1
        for i in range(n - 1):
            a,b = b,a+b
        return a
    print(fib(x))

##############################################

n = int(input('Hoeveelste getal van Fibonacci: '))

vorige, huidige = 1, 1

for i in range (n - 2):
    vorige, huidige = huidige, huidige + vorige

print(huidige)

