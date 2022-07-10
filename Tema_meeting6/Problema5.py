# Clasa Factura
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
#
# Constructor: toate atributele, fara serie
#
# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti
#
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | cantitate | pret bucata | Total
# Telefon |      7       |       700       | 49000
#
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/



class Factura:
    #atribute
    serie_factura = "CJ"
    numar_factura = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    #constructor
    def __init__(self, numar_factura, nume_produs, cantitate, pret_buc):
        self.numar_factura = numar_factura
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate_noua):
        self.cantitate = self.cantitate + cantitate_noua

    def schimba_pretul(self, pretul_nou):
        self.pret_buc = pretul_nou

    def schimba_nume_produs(self, nume_produs_nou):
        self.nume_produs = nume_produs_nou

    def genereaza_factura(self):
        print("-------------------------------------------------------------/n",
              "-----222222")



# nume_produs1 = input("Introduceti numele produsului: ")
# cantitate1 = int(input("Introduceti cantitatea produsului: "))
# pret_buc1 = float(input("Introduceti pretul /bucata: "))
#
# factura1 = Factura(1, nume_produs1, cantitate1, pret_buc1)

factura1 = Factura(1, "Telefon", 100, 799.99)
# factura2 = [Factura(2, "Laptop", 50, 1099.99)]
# factura3 = [Factura(3, "Baterii", 1000, 9.99)]

factura1.schimba_pretul(1099.99)
print(factura1.pret_buc)
factura1.genereaza_factura()

