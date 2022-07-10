# # Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)


class Angajat:
    #atribute
    nume = None
    prenume = None
    salariu = None

    #constructor

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    #metode

    def descrie(self):
        print("Salariatul: ", self.nume.upper(), self.prenume.upper(), "este incadrat cu salariul de: ", self.salariu, "RON")

    def nume_complet(self):
        nume_complet = self.nume.upper()+ " "+ self.prenume.upper()
        print("Numele complet al angajatului este: ", nume_complet)
        print(type(self.nume))
        print(type(nume_complet))

    def salariu_lunar(self, salariu_new):
        self.salariu = salariu_new
        print("Noul salar al angajatului este: ", salariu_new)

    def salariu_anual(self):
        salariu_anual = 12 * self.salariu
        print("Salariul anual este: ", salariu_anual)

    def marire_salariu(self, procent):
        salariu_new = self.salariu * (1 + procent/100)
        print("Noul salar dupa marirea salariala este: ", salariu_new)


angajat1 = Angajat("Popescu", "Ionel", 2500)
angajat1.descrie()
angajat1.nume_complet()
angajat1.salariu_lunar(3700)
angajat1.descrie()
angajat1.salariu_anual()
angajat1.salariu_lunar(4000)
angajat1.salariu_anual()

angajat1.salariu_lunar(1000)
angajat1.marire_salariu(30)

procent = int(input("introdu procentul aplicat pentru marirea salariului: "))
angajat1.marire_salariu(procent)



