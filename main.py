# Importy
import sys
import os

# Přidáme aktuální složku souboru do cesty pro importy
sys.path.append(os.path.dirname(__file__))

from evidence import Evidence

class Rozhrani:
    def __init__(self):
        self.evidence = Evidence()

    def _zadej_text(self, dotaz):
        while True:
            hodnota = input(dotaz).strip()
            if hodnota:
                return hodnota
            print("Chyba: Pole nesmí být prázdné!")

    def _zadej_cislo(self, dotaz, min_hodnota=1, max_hodnota=120):
        while True:
            try:
                cislo = int(input(dotaz))
                if min_hodnota <= cislo <= max_hodnota:
                    return cislo
                print(f"Chyba: Zadejte číslo mezi {min_hodnota} a {max_hodnota}.")
            except ValueError:
                print("Chyba: Zadejte platné číslo!")

    def _zadej_telefon(self, dotaz):
        while True:
            tel = input(dotaz).strip()
            if tel.isdigit():
                return tel
            print("Chyba: Telefon musí obsahovat jen čísla!")

    def menu(self):
        while True:
            print("\n------------------------------")
            print("Evidence pojištěných")
            print("------------------------------")
            print("1 - Přidat pojištěného")
            print("2 - Vypsat všechny")
            print("3 - Vyhledat")
            print("4 - Konec")

            volba = input("Vyberte akci: ")

            if volba == "1":
                jmeno = self._zadej_text("Zadejte jméno: ")
                prijmeni = self._zadej_text("Zadejte příjmení: ")
                telefon = self._zadej_telefon("Zadejte telefon: ")
                vek = self._zadej_cislo("Zadejte věk: ")
                self.evidence.pridej_pojisteneho(jmeno, prijmeni, vek, telefon)
                print("Pojištěný byl uložen.")

            elif volba == "2":
                seznam = self.evidence.vrat_vsechny()
                if seznam:
                    print("\n--- Seznam pojištěných ---")
                    for p in seznam:
                        print(p)
                else:
                    print("Seznam je prázdný.")

            elif volba == "3":
                print("Hledání (ponechte prázdné pole pro ignorování části jména/příjmení)")
                jmeno = input("Zadejte jméno: ").strip()
                prijmeni = input("Zadejte příjmení: ").strip()
                vysledky = self.evidence.najdi_pojisteneho(jmeno, prijmeni)
                if vysledky:
                    print("\n--- Výsledky hledání ---")
                    for p in vysledky:
                        print(p)
                else:
                    print("Pojištěný nebyl nalezen.")

            elif volba == "4":
                print("Ukončuji aplikaci.")
                break

            else:
                print("Neplatná volba!")

# Spouštění
if __name__ == "__main__":
    app = Rozhrani()
    app.menu()