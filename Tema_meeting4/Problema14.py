# Alegeti un numar de la tastatura
# Ex:7
# Scrieti un program care sa genereze in consola urmatoarea piramida
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
#
# Ex:3
# 1
# 22
# 333

repetari = int(input("Introduceti un numar intreg pozitiv!"))
#
lista = []

for i in range(1, repetari+1):
    for j in range(1, i+1):
        lista[i] = lista.append(j)
        #lista.append(str(j))
        # lista.insert(j,1)
        print(lista)



# for i in range(1, repetari+1):
#     j=1
#     while j != 5:
#         lista.insert(j,j)
#         j+=1
#     print(lista)




# n = int(input("Enter number of rows: "))
#
# for i in range(1,n+1):
#     for j in range(1, i+1):
#         print(i, end="")
#     print()

# n = int(input('Enter the number till which you want the sequence:'))
# for i in range(1,n+1):
#        print(str(i) * i) # ce face functia asta?
