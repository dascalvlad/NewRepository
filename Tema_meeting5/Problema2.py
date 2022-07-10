#2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
# Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
# Daca functia are return, printati raspunsul
from functions import paritate

a = float(input("Introduceti numarul dorit: "))

if paritate(a):
    print("Numarul introdus este un numar par! ")
else:
    print("numarul introdus este un numar impar!")


