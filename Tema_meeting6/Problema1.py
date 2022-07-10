# Clasa Cerc
# Atribute: raza, culoare
# Constructor pt ambele atribute
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()

import math

class Cerc:
    # atributes/fields
    raza = None
    culoare = None

    #constructor
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    #metode
    def descrie(self):
        print("Cercul existent are raza egala cu: ", self.raza, "si are culoarea: ",self.culoare)

    def aria_cercului(self,):
        aria = math.pi * self.raza * self.raza
        print("Aria cercului este: ", aria)

    def diametru(self):
        diametru = self.raza/2
        print("Diametrul cercului are valoarea: ", diametru)

    def circumfwrinta(self):
        circumferinta = 2 * self.raza * math.pi
        print("Circumferinta cercului are valoarea egala cu : ", circumferinta)

cerc1 = Cerc(10, "rosie")
cerc1.descrie()

cerc1.aria_cercului()
cerc1.diametru()
cerc1.circumfwrinta()


