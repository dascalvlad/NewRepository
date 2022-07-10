# Q5: Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5

x = int(input('Introdu primul numar: '))
y = int(input('Introdu al 2 lea numar: '))

if abs(x-y) <= 5:
    print('Valoarea absoluta a diferentei dintre cele 2 numere este mai mica ca si 5')
else:
    print('Valoarea absoluta a diferentei dintre cele 2 numere este mai mare ca si 5')