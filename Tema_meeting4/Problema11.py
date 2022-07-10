# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterati prin lista alte_numere
# Populati corect celelalte liste
# Afisati cele 4 liste la final

#               0  1  2  3  4   5  6   7  8   9
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for i in range(len(alte_numere)):
    if alte_numere[i] >= 0:
        numere_pozitive.append(alte_numere[i])
    else:
        numere_negative.append(alte_numere[i])
    if alte_numere[i] % 2 == 0:
        numere_pare.append(alte_numere[i])
    else:
        numere_impare.append(alte_numere[i])
print("Numere pare", numere_pare)
print("Numere impare", numere_impare)
print("Numere pozitive", numere_pozitive)
print("Numere negative", numere_negative)

# cum se poate optimiza altfel?



