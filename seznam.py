from pojistenec import Pojistenec

class Seznam:
    def __init__(self, pojistenci=None):
        self.pojistenci = pojistenci or []

    def menu(self):
        # nabídkové menu akcí, které aplikace umí provést
        print("===============================\n   Evidence pojištěných BUNNY\n===============================")
        print("Možnosti akcí:")
        print("\t1 - Přidat nového pojištěného")
        print("\t2 - Vypsat všechny pojištěné")
        print("\t3 - Vyhledat pojištěného")
        print("\t4 - Konec")

    def pridat(self):
        # přidání nového záznamu do seznamu a kontrola správného datového typu
        while True:
            try:
                jmeno = self.kontrola_jepismeno("Zadejte křestní jméno: ", "-> !POZOR! Nepovolený znak! ")
                prijmeni = self.kontrola_jepismeno("Zadejte příjmení: ", "-> !POZOR! Nepovolený znak! ")
                vek = self.kontrola_jecislo("Zadejte věk: ", "-> !POZOR! Zadejte číselnou hodnotu! ")
                telefon = self.kontrola_jecislo("Zadejte telefonní číslo: +420 ", "-> !POZOR! Zadejte číselnou hodnotu! ")
            except Exception:
                print("!POZOR! Někde jste zadali chybný formát, prosím, zkuste znovu")
                continue
            break

        pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
        self.pojistenci.append(pojistenec)

    def vyhledat(self):
        # vyhledání záznamu ze seznamu, který vypíše pokud je shodné jméno a příjmení
        jmeno = input("Křestní jméno: ")
        prijmeni = input("Příjmení: ")
        vyhledavani = [str(i) for i in self.pojistenci if (str(jmeno) and str(prijmeni)) in str(i)]
        print("\t-----------------------------------------------")
        if vyhledavani:
            for j in vyhledavani:
                print("\t", j)
        else:
            print("\t         Žádné záznamy nenalezeny!")
        print("\t-----------------------------------------------")

    def vypis_seznam(self):
        # vypisování všech uložených dat ze seznamu, pokud jsou nalezena
        # seznam = Seznam()
        vypis = [str(i) for i in self.pojistenci]
        print("Aktuální seznam pojištěnců:")
        print("\t-----------------------------------------------")
        if vypis:
            for pojistenec in self.pojistenci:
                print("\t", pojistenec)
        else:
            print("\t          Žádné záznamy nenalezeny!")
        print("\t-----------------------------------------------")

    def kontrola_jecislo(self, zadani_c, chyba_c):
        while True:
            try:
                cislo = int(input(zadani_c))
            except ValueError:
                print(chyba_c)
            else:
                return cislo

    def kontrola_jepismeno(self, zadani_p, chyba_p):
        p = input(zadani_p).title()
        if p.isnumeric():
            while True:
                try:
                    print(chyba_p)
                    p = (input(zadani_p).title())
                except ValueError:
                    continue
                break
