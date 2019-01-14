def hint(gok, woord):

    antwoord = ''
    eerste_letter_gok = gok[0]
    tweede_letter_gok = gok[1]
    derde_letter_gok = gok[2]
    vierde_letter_gok = gok[3]
    vijfde_letter_gok = gok[4]

    eerste_letter_woord = woord[0]
    tweede_letter_woord = woord[1]
    derde_letter_woord = woord[2]
    vierde_letter_woord = woord[3]
    vijfde_letter_woord = woord[4]


    if eerste_letter_gok in woord and eerste_letter_gok == eerste_letter_woord:
        antwoord += eerste_letter_gok.upper()
    elif eerste_letter_gok in woord:
        antwoord += eerste_letter_gok
    else:
        antwoord += '.'
    if tweede_letter_gok in woord and tweede_letter_gok == tweede_letter_woord:
        antwoord += tweede_letter_gok.upper()
    elif tweede_letter_gok in woord:
        antwoord += tweede_letter_gok
    else:
        antwoord += '.'
    if derde_letter_gok in woord and derde_letter_gok == derde_letter_woord:
        antwoord += derde_letter_gok.upper()
    elif derde_letter_gok in woord:
        antwoord += derde_letter_gok
    else:
        antwoord += '.'
    if vierde_letter_gok in woord and vierde_letter_gok == vierde_letter_woord:
        antwoord += vierde_letter_gok.upper()
    elif vierde_letter_gok in woord:
        antwoord += vierde_letter_gok
    else:
        antwoord += '.'
    if vijfde_letter_gok in woord and vijfde_letter_gok == vijfde_letter_woord:
        antwoord += vijfde_letter_gok.upper()
    elif vijfde_letter_gok in woord:
        antwoord += vijfde_letter_gok
    else:
        antwoord += '.'

    return antwoord



