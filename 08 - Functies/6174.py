def splits(getal):
    getal = int(getal)
    eerste_getal = int(getal / 1000)
    tweede_getal = int((getal - eerste_getal * 1000) / 100)
    derde_getal = int((getal - eerste_getal * 1000 - tweede_getal * 100) / 10)
    vierde_getal = int(getal - eerste_getal * 1000 - tweede_getal * 100 - derde_getal * 10)
    return eerste_getal, tweede_getal, derde_getal, vierde_getal

def oplopende_cijfers(eerste_getal, tweede_getal, derde_getal, vierde_getal):
    getal = eerste_getal, tweede_getal, derde_getal, vierde_getal
    gesorteerd_getal = tuple(sorted(getal))
    return gesorteerd_getal

def op_af_getallen(eerste_getal, tweede_getal, derde_getal, vierde_getal):
    oplopend_getal = ''
    aftellend_getal = ''
    oplopend_getal += str(eerste_getal) + str(tweede_getal) + str(derde_getal) + str(vierde_getal)
    aftellend_getal += str(vierde_getal) + str(derde_getal) + str(tweede_getal) + str(eerste_getal)
    return oplopend_getal, aftellend_getal

def verschil (eerste_getal, tweede_getal):
    verschil = str(int(eerste_getal) - int(tweede_getal))
    return verschil

def kaprekar(n):
    mes = ''
    a = n // 1000
    b = (n - (a * 1000)) // 100
    c = (n - (a * 1000) - (b * 100)) // 10
    d = n - (a * 1000) - (b * 100) - (c * 10)
    g1 = min(a, b, c, d)
    g2 = max(min(a, b, c), min(b, c, d), min(a, b, d), min(a, c, d))
    g3 = min(max(a, b, c), max(b, c, d), max(a, b, d), max(a, c, d))
    g4 = max(a, b, c, d)
    oprij = str(g1) + str(g2) + str(g3) + str(g4)
    afrij = str(g4) + str(g3) + str(g2) + str(g1)

    if int(afrij) - int(oprij) == 6174:
        mes = '{} - {} = {}'.format(afrij, oprij, int(afrij) - int(oprij))
    else:

        while int(afrij) - int(oprij) != 6174:
            mes += '{} - {} = {}\n'.format(afrij, oprij, int(afrij) - int(oprij))
            n = int(afrij) - int(oprij)
            a = n // 1000
            b = (n - (a * 1000)) // 100
            c = (n - (a * 1000) - (b * 100)) // 10
            d = n - (a * 1000) - (b * 100) - (c * 10)
            g1 = min(a, b, c, d)
            g2 = max(min(a, b, c), min(b, c, d), min(a, b, d), min(a, c, d))
            g3 = min(max(a, b, c), max(b, c, d), max(a, b, d), max(a, c, d))
            g4 = max(a, b, c, d)
            oprij = str(g1) + str(g2) + str(g3) + str(g4)
            afrij = str(g4) + str(g3) + str(g2) + str(g1)
        a = n // 1000
        b = (n - (a * 1000)) // 100
        c = (n - (a * 1000) - (b * 100)) // 10
        d = n - (a * 1000) - (b * 100) - (c * 10)
        g1 = min(a, b, c, d)
        g2 = max(min(a, b, c), min(b, c, d), min(a, b, d), min(a, c, d))
        g3 = min(max(a, b, c), max(b, c, d), max(a, b, d), max(a, c, d))
        g4 = max(a, b, c, d)
        oprij = str(g1) + str(g2) + str(g3) + str(g4)
        afrij = str(g4) + str(g3) + str(g2) + str(g1)
        mes += '{} - {} = {}'.format(afrij, oprij, int(afrij) - int(oprij))
    return mes

####################################################################################

def splits(getal):
    d = getal % 10
    getal = getal // 10
    c = getal % 10
    getal = getal // 10
    b = getal % 10
    getal = getal // 10
    a = getal % 10
    getal = getal // 10
    return a, b, c, d

def oplopende_cijfers(a, b, c, d):
    s1 = min(a, b, c, d)
    s4 = max(a, b, c, d)

    k23 = max(min(a, b), min(b, c), min(a, c))
    k32 = a + b + c + d - s1 - s4 - k23

    s2 = min(k23, k32)
    s3 = max(k23, k32)

    return s1, s2, s3, s4

def op_af_getallen(a, b, c, d):
    return str(a) + str(b) + str(c) + str(d), str(d) + str(c) + str(b) + str(a)

def verschil(af, op):
    uitkost = str(int(af) - int(op))

    while len(uitkomst) < 4:
        uitkomst = '0' + uitkomst

        return uitkomst

def kaprekar(getal):

    uitkomst =''
    while getal != 6174:
        a, b, c, d = splits(getal)
        w, x, y, z = oplopende_cijfers(a, b, c, d)
        op, af = op_af_getallen(w, x, y, z)
        v = verschil(af,op)
        uitkomst += af + ' - ' + op + ' - ' + v

        getal = int(v)

        if getal != 6174:
            uitkomst += '\n'

    return uitkomst


