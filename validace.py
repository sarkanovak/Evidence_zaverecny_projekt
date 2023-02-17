def kontrola_jecislo(zadani_c, chyba_c):
    while True:
        vstup = input(zadani_c)
        if vstup.isdigit():
            return int(vstup)
        else:
            print(chyba_c)


def kontrola_jepismeno(zadani_p, chyba_p):
    while True:
        vstup = input(zadani_p).title()
        if vstup.isalpha():
            return vstup
        else:
            print(chyba_p)
            