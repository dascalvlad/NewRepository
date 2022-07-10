# Avand lista
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

print("Varianta cea mai simpla este folosind functia count ().  Numarul ~3~ apare de :",numere.count(3), "ori")
print("_______________________________")

count =0
for i in range(len(numere)):
    if numere[i] == 3:
        count +=1
print("A 2 a varinata folosind o strucura repetitiva de tip for. Numarul ~3~ apare de :", count, "ori")
print("_______________________________")

x=0
count2 = 0
while x < len(numere):
    if numere[x] == 3:
        x +=1
print(count2)



