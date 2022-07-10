# Q12: Set zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
#          weekend = {'sambata', 'duminica'}
#      Adaugati in zilele_sapt ‘luni’ ????
#      Afisati zile_sapt

zile_sapt = {"luni", "marti", "miercuri", "joi", "vineri","sambata", "duminica"}
weekend = {"sambata", "duminica"}

print(zile_sapt.add("luni")) # de ce nu merge asa?
zile_sapt.add("luni")
print(zile_sapt)


# Q13: Folositi un if si verificati daca
#      Weekend este un subset al zilelor din sapt
#      Weekend nu este un subset al zilelor din sapt

if weekend.issubset(zile_sapt):
    print("Weekendul face parte din saptamana!")
else:
    print("Weekendul NU face parte din saptamana!")

# Q14: Afisati diferentele dintre aceste 2 seturi
#
intersectia = zile_sapt.intersection(weekend)
intersectia2 = weekend.intersection(zile_sapt)

print("multimea rezultata din intersectia celor 2 seturi:", intersectia)
print("multimea rezultata din intersectia celor 2 seturi:", intersectia2)
#
#
# # Q15: Afisati intersectia elementelor din aceste 2 seturi
#
reuniunea = zile_sapt.union(weekend)
print("multimea rezultata din reuniunea celor 2 seturi este: ", reuniunea)
print(type(reuniunea))