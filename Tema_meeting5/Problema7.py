# Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu
# Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
# Daca functia are return, printati raspunsul
from functions import gaseste_caracter

sir = input("Introduceti sirul de caractere dorit: ")
caracter = input("Introduceti caracterul ce doriti sa il cautati: ")



#print(gaseste_caracter(sir,caracter))
if len(caracter) > 1:
    print("Ati introdus mai mult de un singur caracter! Incercati din nou!")
#print(gaseste_caracter(sir,caracter))
elif gaseste_caracter(sir,caracter):
    print("Caracterul a fost gasit in sirul dat! ")
else:
    print("Caracterul nu a fost gasit in sirul dat! ")
#
# print(sir[0])
# print(caracter[0])


