# Q9: Citeste o litera de la tastatura
#     Verifica si afiseaza daca este vocala sau nu

vocale = "aeiou"
x = input('Introdu caracterul dorit: ')
print(x)
print(vocale.find(x))
if vocale.find(x):
    print('da')
else:
    print('nu')