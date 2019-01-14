def is_letter(l):

    if l in 'azertyuiopqsdfghjklmwxcvbn' or l in 'AZERTYUIOPQSDFGHJKLMWXCVBN':

        return True
    else:

        return False

def roteer_letter(x, y):

    if x in 'azertyuiopqsdfghjklmwxcvbn':

        if (ord(x) + y) > ord('z'):

            k = (ord(x) + y) - ord('z')

            letter = chr(ord('a') - 1 + k)

        else:

            letter = chr(ord(x) + y)

    else:

        if (ord(x) + y) > ord('Z'):

            k = (ord(x) + y) - ord('Z')

            letter = chr(ord('A') - 1 + k)

        else:

            letter = chr(ord(x) + y)

    return letter

def versleutel(x, y):

    tekst = x

    nieuwe_tekst = ''

    for letter in tekst:

        if is_letter(letter) == True:

            nieuwe_letter = roteer_letter(letter, y)

            nieuwe_tekst += nieuwe_letter

        else:

            nieuwe_tekst += letter

    return nieuwe_tekst