# Avand dict
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina xLastun
# Iterati prin lista


pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

# buget_achizitie = abs(int(input("Introduceti bugetul avut pentru achizitia masinii: ")))
#
#
# for key, value in pret_masini.items():
#     if value <= buget_achizitie:
#         print("Pentru un buget de sub: ", buget_achizitie, ", masina disponibila este: ", key, " si are pretul: ", value)

# model_dorit = input("introduceti modelul dorit: ")
# for key, value in pret_masini.items():
#     if model_dorit == key:
#         print("Avem Masina pe stoc")
#     else:
#         print("Avem alte modele mai interesante!")


for key, values in pret_masini.items():
    print(values)
    print(key)
pret_masini.pop("Dacia")
print(pret_masini)








