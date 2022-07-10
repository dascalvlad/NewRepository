# Functie care sa aplice o reducere de pret
# Daca produsul costa 100 lei si aplicam reducere de 10%
# Pretul va fi 90
# Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida
from functions import discount_pret
x = float(input("Introduceti pretul original al produsului: "))
if x > 0:
    y = float(input("Introduceti discountul ce doriti sah il aplicati produsului: "))
    discount_pret(x,y)
else:
    print("Pretul introdus nu este valid!")