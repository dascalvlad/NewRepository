# Q3: Sortati si afisati lista generata la ex anterior
#     Stergeti numarul 0 folosind o functie
#     Afisati iar lista

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]

lista1.sort()
print("Elementele din lista sunt sortate ASC folosind functia sort():", lista1)
#de ce nu merg urmatoarele variante:?
lista7=lista1.sort()
#print(lista7) sau print(lista1.sort())

lista1.remove(lista1[0])
print(lista1)








