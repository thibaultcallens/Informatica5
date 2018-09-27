r = float(input('Geef afstand: '))

Q1 = 2.0 * 10 ** -6
Q2 = 1.0 * 10 ** -6
k = 8.99 * 10**9

coulombkracht = k * (Q1 * Q2 ) / ( (r * 10 ** -2) ** 2)

resultaat = coulombkracht

print(resultaat)