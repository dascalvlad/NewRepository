# 13. Functie care primeste o lista de cifre (adica doar 0-9)
# Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un DICT care ne spune de cate ori apare fiecare cifra
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
from functions import dictionar_elemente_unice
x = [1, 3, 1, 5, 9, 7, 7, 5, 5, 9, 4, 7, 2]

dictionar_elemente_unice(x)

