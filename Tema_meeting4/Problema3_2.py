# Aceeasi lista,
# Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin for each
# Daca masina e mercedes (if)
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel
#    Printam Am gasit masina X. Mai cautam
def search(lista, item):
    for i in range(len(lista)):
        if list[i] == item:
            return True
    return False


# #           0        1       2        3              4           5        6         7         8
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lasting', 'Fiat', 'Trabant', 'Opel']

masina = "BMW"
print(type(masina))

if search(masini, masina):
    print("Da")
else:
    print("Nu")
