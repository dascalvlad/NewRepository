# Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)


class Cont:
    #atribute
    titular_cont = None
    cont_iban = None
    sold_existent = 0

    #constructor
    def __init__(self, titular_cont, cont_iban, sold_existent):
        self.titular_cont = titular_cont
        self.cont_iban = cont_iban
        self.sold_existent = sold_existent

    #metode
    def afisare_sold(self):
        print("clientul: ", self.titular_cont.upper(), "are contul IBAN: ", self.cont_iban, "si are un sold de: ", self.sold_existent, "RON")

    def debitare_cont(self, suma):
        self.sold_existent = self.sold_existent - suma
        print("Noua suma disponibila in cont este: ", self.sold_existent)

    def creditare_cont(self, suma):
        self.debitare_cont(-suma)


# nume = input("Introduceti numele clientului: ")
# iban = input("Introduceti contul IBAN: ")
# client1 = Cont(nume, iban, 0)
# client1.afisare_sold()

client1 = Cont("Dascal Paul Vladut", "RO66BTRL43242342300XX", 10000)
client1.afisare_sold()

suma = int(input("Introdu suma debitata: "))
client1.debitare_cont(suma)
suma2 = int(input("Introdu suma creditata: "))
client1.creditare_cont(suma2)





