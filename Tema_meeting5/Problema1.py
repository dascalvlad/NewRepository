# 1. Functie care sa calculeze si sa returneze suma a 2 numere
# Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
# Daca functia are return, printati raspunsul
from functions import suma

a1 = float(input("Introduceti prima valoare: "))
b1 = float(input("Introduceti a 2 a valoare: "))

c1 = suma(a1,b1)


x = [a1, b1]
print("Suma celor 2 numere folosind functia sum() este: ", sum(x))



