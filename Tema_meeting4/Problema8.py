# Aceeasi lista
# Iterati prin ea
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)


numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

print("Cea mai simpla metoda este de a folosi functia sum(). Suma numerelor din lista este:", sum(numere))
print("__________________________")

sum = 0
for i in range (len(numere)):
    sum = sum + numere[i]
print("O alta metoda presupune folosirea unei structuri repetitive de tip for. Suma numerelor din lista este:", sum)
print("__________________________")

x = 0
sum2 =0
while x < len(numere):
    sum2 = sum2 + numere[x]
    x +=1
print("O alta metoda presupune folosirea unei structuri repetitive de tip while. Suma numerelor din lista este:",sum2)
print("__________________________")