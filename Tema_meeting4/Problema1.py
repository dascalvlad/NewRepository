# Avand lista
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']


#           0        1       2        3              4           5        6         7         8
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

#   Folositi un for ca sa iterati prin toata lista si sa afisati
#   ‘Masina mea preferata este x’

for i in range(len(masini)):
    print("Masina mea preferata este: ", masini[i])
print("______________________________________")

#   Faceti acelasi lucru cu un for each
for masina in masini:
    print("Masina mea preferata este: ", masina)
print("______________________________________")

#   Faceti acelasi lucru cu un while

x = 0
while x != len(masini):
    print("Masina mea preferata este: ", masini[x])
    x +=1
print("______________________________________")


