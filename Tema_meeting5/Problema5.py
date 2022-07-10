# 5. Functie care returneaza aria cercului
# Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
# Daca functia are return, printati raspunsul
from functions import aria_cerc

r = float(input("Introduceti raza cercului: "))
if r > 0:
    aria_cerc(r)
else:
    print("Datele introduse nu sunt valide: ")