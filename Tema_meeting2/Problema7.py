# Q7: x si y (int)
#     Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare

x = int(input('Introdu numarul dorit: '))
y = int(input('Introdu al 2 lea numar dorit: '))

if x == y:
    print('Numerele introduse sunt egale!')
elif x > y:
    print('Numarul', x, 'este mai mare decat', y)
else:
    print('Numarul', y, 'este mai mare decat', x)