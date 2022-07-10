# Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pt toate atributele
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
# Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare.
# Puteti verifica schimbarea culorii prin apelarea metodei descrie().


class Dreptunghi:
    #atribute
    lungime = None
    latime = None
    culoare = None

    #constructor
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    # metode

    def descrie(self):
        print("Dreptunghiul are lungimea: ", self.lungime, ", latimea:", self.latime, "si are culoarea: ", self.culoare)

    def aria_dreptunghiului(self):
        if self.lungime <= 0 or self.latime <= 0:
            print("Datele introduse nu sunt valide!")
        elif self.lungime == self.latime:
            aria = self.lungime * self.latime
            print("Aria patratului este: ", aria)
        else:
            aria = self.lungime * self.latime
            print("Aria dreptunghiului este:  ", aria)

    def schimba_culoarea(self, culoarea_noua):
        self.culoare = culoarea_noua

dreptunghi1 = Dreptunghi(10.1, 10, "Rosie")
dreptunghi1.aria_dreptunghiului()
dreptunghi1.schimba_culoarea("alba")
dreptunghi1.descrie()


