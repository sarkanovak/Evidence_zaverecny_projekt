from pojistenec import Pojistenec
from validace import kontrola_jepismeno, kontrola_jecislo


class Seznam:

    def __init__(self, pojistenci=None):
        self.pojistenci = pojistenci or []

    @staticmethod
    def menu():
        # nabídkové menu akcí, které aplikace umí provést
        print("=================================\n   *Evidence pojištěných BUNNY*\n=================================")
        print("Možnosti akcí:")
        print("\t1 - Přidat nového pojištěného")
        print("\t2 - Vypsat všechny pojištěné")
        print("\t3 - Vyhledat pojištěného")
        print("\t4 - Konec")

    def pridat(self):
        # přidání nového záznamu do seznamu a kontrola správného datového typu
        jmeno = kontrola_jepismeno("Zadejte křestní jméno: ", "-> !POZOR! Nepovolený znak! ")
        prijmeni = kontrola_jepismeno("Zadejte příjmení: ", "-> !POZOR! Nepovolený znak! ")
        vek = kontrola_jecislo("Zadejte věk: ", "-> !POZOR! Zadejte číselnou hodnotu! ")
        telefon = kontrola_jecislo("Zadejte telefonní číslo: +420 ", "-> !POZOR! Zadejte číselnou hodnotu! ")

        pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
        self.pojistenci.append(pojistenec)

    def vypsat(self):
        # vypisování všech uložených dat ze seznamu, pokud jsou nalezena
        vypis = [str(i) for i in self.pojistenci]
        print("Aktuální seznam pojištěnců:")
        print("\t-----------------------------------------------")
        if vypis:
            for pojistenec in self.pojistenci:
                print("\t", pojistenec)
        else:
            print("\t          Žádné záznamy nenalezeny!")
        print("\t-----------------------------------------------")

    def vyhledat(self):
        # vyhledání záznamu ze seznamu, který vypíše pokud je shodné jméno a příjmení
        jmeno = kontrola_jepismeno("Zadejte křestní jméno: ", "-> !POZOR! Nepovolený znak! ")
        prijmeni = kontrola_jepismeno("Zadejte příjmení: ", "-> !POZOR! Nepovolený znak! ")
        vyhledavani = [str(i) for i in self.pojistenci if (str(jmeno) and str(prijmeni)) in str(i)]
        print("\t-----------------------------------------------")
        if vyhledavani:
            for j in vyhledavani:
                print("\t", j)
        else:
            print("\t         Žádné záznamy nenalezeny!")
        print("\t-----------------------------------------------")

    @staticmethod
    def konec():
            print("""
                         /  \ 
                        /  _ \ 
                       | /  \ |
                       ||    ||  _______
                       ||    ||  |\     \ 
                       ||    ||  ||\     \ 
                       ||    ||  || \    | 
                       ||    ||  ||  \__/
                       ||    ||  ||   || 
                       \ \_/  \_/ \_/ /
                       /    _     _    \ 
                      /                 \ 
                      |     O     O     | 
                     |     \  ___  /     |
                    /       \ \_/ /       \ 
                   /    -----  |  --\      \ 
                   |       \__/|\__/ \     | 
                    \        |_|_|         / 
                     \_____          _____/ 
                          \         / 
                          |         | 
                    """)
            print("\n-> Program Evidence pojištěných BUNNY byl ukončen. \n ____________________KONEC_______________________")
            quit()
