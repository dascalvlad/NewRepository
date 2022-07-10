# Q3: Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

x = int(input('Introdu numarul dorit:'))
if x == 0:
    print('Numarul introdus', x , 'este neutru')
elif x > 0:
    print('Numarul introdus', x, ' este pozitiv!')
else:
    print('Numarul introdus ',x,'este negativ!')