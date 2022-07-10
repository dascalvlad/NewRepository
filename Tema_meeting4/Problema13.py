
# Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitari! Ai ghicit!

import random

numar_secret = random.randint(1, 30)
print("Numarul integer generat utilizand functia random() este: ", numar_secret)

numar_ghicit = int(input("Introduceti numarul dorit de la tastatura!"))

# if numar_ghicit == numar_secret:
#     print("Ati ghicit numarul!")
# elif numar_ghicit > numar_secret:
#     print("Numarul secret este mai mic!")
# else:
#     print("Numarul secret este mai mare!")

while numar_ghicit != numar_secret:
    if numar_ghicit > numar_secret:
        print("Numarul secret este mai mic!")
        break
    else:
        print("Numarul secret este mai mare!")
        break
else:
    print("Ati ghicit numarul!")
