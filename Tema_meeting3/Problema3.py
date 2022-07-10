# Q3: Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
#     Gasiti 2 variante sa le uniti intr-o singura lista.

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]

lista1.append(lista2)
print("Prima varianta pentru a face reuniunea celor 2 multimi presupune utilizarea functiei append():", lista1)

#de ce nu functioneaza varianta asta?
lista3 = lista1.append(lista2)
print("Prima varianta pentru a face reuniunea celor 2 multimi presupune utilizarea functiei append():", lista3)

lista4 = lista1+lista2
print("A 2 a varianta de a face reuniunea celor 2 multimi presupune insumarea lor:", lista1+lista2)


for i in range(0, len(lista2)):
    lista1.append(lista2[i])
print("A 3 a varinata de reuniune a celor 2 multimi este:", lista1)

