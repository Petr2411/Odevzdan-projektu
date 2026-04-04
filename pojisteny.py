# Vytvoření pojištěného
class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, věk: {self.vek}, tel: {self.telefon}"

    def to_dict(self):
        return {
            "jmeno": self.jmeno,
            "prijmeni": self.prijmeni,
            "vek": self.vek,
            "telefon": self.telefon
        }

    @staticmethod
    def from_dict(data):
        return Pojisteny(data["jmeno"], data["prijmeni"], data["vek"], data["telefon"])