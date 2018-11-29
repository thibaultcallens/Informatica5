def welkom(naam):
    print('Welkom terug ' + naam)

welkom('lieve sint')
welkom('Zwarte piet')

#####################################
def discriminant(a, b, c):
    return (b ** 2) - (4 * a * c)

########################################

def is_priem(n):

    i = 2
    while i <= floor(sqrt(n)) and n % i != 0:
        i += 1
    return i == floor(sqrt(n)) + 1
############################################"
appel = 'appel'
banaan = 'banaan'
kers = 'kers'
def print_fruit():
    appel = 'olifant'
    banaan = 'aapje'
    kers = 'goudvis'
    print(appel, banaan, kers)
print_fruit()
print(appel, banaan, kers)

