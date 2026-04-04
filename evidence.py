# Vytvoření evidence
from pojisteny import Pojisteny
import json
import os

class Evidence:
    def __init__(self, soubor="pojisteni.json"):
        self.pojisteni = []
        self.soubor = soubor
        self.nacti_data()

    def pridej_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        novy = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.pojisteni.append(novy)
        self.uloz_data()

    def vrat_vsechny(self, seradit=True):
        if seradit:
            return sorted(self.pojisteni, key=lambda p: (p.prijmeni.lower(), p.jmeno.lower()))
        return self.pojisteni

    def najdi_pojisteneho(self, jmeno="", prijmeni=""):
        vysledky = []
        jmeno = jmeno.lower()
        prijmeni = prijmeni.lower()
        for p in self.pojisteni:
            if jmeno in p.jmeno.lower() and prijmeni in p.prijmeni.lower():
                vysledky.append(p)
        return vysledky

    def uloz_data(self):
        data = [p.to_dict() for p in self.pojisteni]
        with open(self.soubor, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def nacti_data(self):
        if os.path.exists(self.soubor):
            try:
                with open(self.soubor, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.pojisteni = [Pojisteny.from_dict(d) for d in data]
            except (json.JSONDecodeError, KeyError):
                self.pojisteni = []