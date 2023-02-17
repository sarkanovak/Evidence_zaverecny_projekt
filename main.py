from seznam import Seznam
seznam = Seznam()

while True:
    seznam.menu()
    try:
        vyber = int(input("Zadejte číslo akce, kterou chcete provést:\n -> "))
        if vyber < 1 or vyber > 4:
            raise Exception("\nZvolená akce neexistuje.")
    except Exception as e:
        print(e)
        print("Prosím, zvolte validní číslo z menu.")

    if vyber == 1:
        seznam.pridat()
        pokracuj = input("\nData byla uložena. Pro pokračování stikněte klávesu ENTER...")

    elif vyber == 2:
        seznam.vypsat()
        pokracuj = input("\nPro pokračování stikněte klávesu ENTER...")

    elif vyber == 3:
        seznam.vyhledat()

    elif vyber == 4:
        seznam.konec()
        
