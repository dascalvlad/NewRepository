# Q4: Verifica si afiseaza daca x este intre -2 si 13

x = int(input('Introdu numarul dorit:'))
if -2 <= x <= 13:
    print('Numarul introdus', x, 'este in intervalul de interes')
else:
    print('Numarul introdus', x, 'NU este in intervalul de interes')