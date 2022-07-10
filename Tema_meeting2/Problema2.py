# Q2: Verifica si afiseaza daca x este numar natural sau nu

x = int(input('Introdu de la tastatura: '))
if isinstance(x, int) and (x >= 0):  # verificare daca numerul este valid
    print('Numarul introdus', x, 'este natural')
    print(isinstance(x, int))
else:
    print('Numarul introdus', x, 'NU este natural si este de tipul', type(x))