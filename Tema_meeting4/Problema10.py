# Aceeasi lista
# Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista

#         0  1  2  3  4  5  6  7   8  9
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

for i in range(len(numere)):
    if numere[i] >= 0:
        numere[i] = -abs(numere[i])
    else:
        numere[i] = abs(numere[i])
print("Prima metoda folosing functiile abs() si -abs(). Numerele ~inversate~ sunt ", numere)
print("_______________________________")


for j in range(len(numere)):
    if numere[j] >= 0:
        numere[j] = 0 - numere[j]
    else:
        numere[j] = 0 - numere[j]
print("A 2 a varianta folosind for. Numerele ~inversate~ sunt ", numere)
print("_______________________________")

k = 0
while k != len(numere):
    numere[k] = 0 - numere[k]
    k+=1
print("A 3 a varianta folosind while. Numerele ~inversate~ sunt ", numere)
print("_______________________________")