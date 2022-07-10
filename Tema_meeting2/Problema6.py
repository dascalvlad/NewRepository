# Q6:Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)

x = int(input('Introdu numarul dorit: '))
if not x in range(5,28):
    print('Numarul introdus nu este in intervalul dorit!')
else:
    print('Numarul introdus este in intervalul dorit!')