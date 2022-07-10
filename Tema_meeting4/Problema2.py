# Aceeasi lista  masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# Folositi In for
# Modificati elementele din lista astfel incat sa fie scrise cu majuscule, exceptand primul si ultimul
# Printati varianta finala a listei


#           0        1       2        3              4           5        6         7         8
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']


for i in range(len(masini)):
    if masini[i] != "Audi" and masini[i] != "Opel":
        masini[i] = masini[i].upper()
print(masini)














