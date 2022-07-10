
# Aceeasi lista
# Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)

#         0  1  2  3  4  5  6  7   8  9
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

print("Cea mai simpla solutie este prin folosirea functiei max(). Numarul cel mai mare nurmar din lista este:", max(numere))
print("_______________________________")


max_number = 0
for i in range(len(numere)):
    if numere[i] > max_number:
        max_number = numere[i]
print("A 2 a varianta utilizand cicluri repetitive for/if. Numarul cel mai mare nurmar din lista este: ",max_number)