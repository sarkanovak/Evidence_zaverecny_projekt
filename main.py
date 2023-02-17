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

    if vyber == 4:
        print("      / \   ")
        print("     / _ \   ")
        print("    | / \ |")
        print("    ||   || _______")
        print("    ||   || |\     \ ")
        print("    ||   || ||\     \ ")
        print("    ||   || || \    | ")
        print("    ||   || ||  \__/ ")
        print("    ||   || ||   || ")
        print("     \ \_/ \_/ \_// ")
        print("    /   _     _   \ ")
        print("   /               \ ")
        print("   |    O     O    | ")
        print("   |   \  ___  /   |     ")
        print("  /     \ \_/ /     \ ")
        print(" /  -----  |  --\    \ ")
        print(" |     \__/|\__/ \   | ")
        print(" \       |_|_|       / ")
        print("  \_____       _____/ ")
        print("        \     / ")
        print("        |     | ")

        print("\n-> Program Evidence pojištěných BUNNY byl ukončen.")
        break
    elif vyber == 1:
        seznam.pridat()
        pokracuj = input("\nData byla uložena. Pro pokračování stikněte klávesu ENTER...")
    elif vyber == 2:
        seznam.vypis_seznam()
        pokracuj = input("\nPro pokračování stikněte klávesu ENTER...")
    elif vyber == 3:
        seznam.vyhledat()
