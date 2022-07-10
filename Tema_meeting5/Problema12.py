# Functie calculator care sa returneze 4 valori
# Suma, diferenta, inmultirea, impartirea a 2 numere
# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

from functions import calculator_nou
x = float(input("Introdu primul numar: "))
y = float(input("Introdu cel de-al doilea numar: "))

calculator_nou(x,y)