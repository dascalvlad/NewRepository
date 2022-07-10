# Q8: Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
#     Folositi o functie ca sa afisati Elevii (cheile)

catalog = {
    "Ana": 8,
    "Gigel": 10,
    "Dorel": 5
}
print(catalog)
print("Functia keys() permite afisarea cheilor (partea stanga din dictionar): ", catalog.keys())

# Q9: Printati cei 3 elevi si notele lor
#     Ex: ‘Ana a luat nota {x}’
#     Doar nota o veti lua folosindu-va de cheie

lista_chei =[]
for cheie in catalog.keys():
    lista_chei.append(cheie)
print(lista_chei)
# de ce nu merge: lista_cheie = lista_cheie.append(cheie)

for i in range(0, len(catalog)):
    print(lista_chei[i]," are nota", catalog[lista_chei[i]])

# Q10: Dorel a facut contestatie si a primit 6
#      Modificati nota lui Dorel in 6
#      Printati nota dupa modificare

nota_dorel = int(input("Introduceti noua nota a lui Dorel: "))
catalog.update({ "Dorel": nota_dorel })

for i in range(0, len(catalog)):
    print(lista_chei[i]," are nota", catalog[lista_chei[i]])

# Q11: Gigel se transfera din clasa
#      Cautati o functie care sa il stearga
#      Vine un coleg nou. Adaugati Ionica, cu nota 9
#      Printati noii elevi

catalog.pop("Gigel")
catalog.update({"Ionica":9})

lista_chei =[]
for cheie in catalog.keys():
    lista_chei.append(cheie)
print("Lista chei actualizate pentru dictionarul ~catalog~ :", lista_chei)

for i in range(0, len(catalog)):
    print(lista_chei[i]," are nota", catalog[lista_chei[i]])