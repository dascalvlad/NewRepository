# Functie care sa calculeze si sa returneze suma a 2 numere

def suma(a, b):
    c = a + b
    print("Suma celor 2 numere introduse este: ", c)


# Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

def paritate(a):
    if a % 2 == 0:
        return True
    return False


# Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)

def contorizare_caractere(x):
    numar_caractere = 0
    numar_spatii = 0
    for i in range(len(x)):
        numar_caractere += 1
        if x[i] == " ":
            numar_spatii += 1
    numar_caractere = numar_caractere - numar_spatii
    print("numarul de spatii din numele intreg introdus este: ", numar_spatii)
    print("Numarul de caractere este: ", numar_caractere)


# Functie care returneaza aria dreptunghiului

def aria_dreptunghi(a, b):
    aria = a * b
    print("Aria dreptunghiului este: ", aria)


# Functie care returneaza aria cercului
def aria_cerc(r):
    import math
    aria = math.pi * r * r
    print("Valoarea lui PI este: ", math.pi)
    print("Aria cercului este: ", aria)


# Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu

def gaseste_caracter(sir_caractere, caracter):
    # caracter =""
    # sir_caractere = ""
    # for i in range(0,len(sir_caractere)):
    #     if sir_caractere[i] == caracter:
    #         return True
    #     return False
    caracter = ""
    sir_caractere = ""
    if caracter in sir_caractere:
        return True
    return False


#  Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.

def maximul_dintre_2_numere(input1, input2):
    if input1 == input2:
        print("Numerele introduse sunt egale!")
    elif input1 > input2:
        print("Primul numar ", input1, " este mai mare decat al doilea", input2)
    else:
        print("Al doilea numar", input2, "este mai mare decat primul numar", input1)


# Functie calculator care sa returneze 4 valori
# Suma, diferenta, inmultirea, impartirea a 2 numere
# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

def calculator_nou(a, b):
    print("Suma celor 2 numere este: ", a + b)
    print("Diferenta celor doua numere este: ", a - b)
    print("Inmultirea celor doua numere este: ", a * b)
    print("Impartirea celor doua numere este: ", a / b)


# Functie care primeste 3 numere
# Returneaza valoarea maxima dintre ele

def maximul_dintre_3_numere(a, b, c):
    if a == b == c:
        print("Numerele sunt egale!. Numarul maxim este: ", a)
    elif (a > b) and (a > c):
        print("Numarul maxim este: ", a)
    elif b > c:
        print("Numarul maxim este: ", b)
    else:
        print("Numarul maxim este: ", c)


# Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar

def suma_primelor_n_numere_naturale(n):
    sumanew = 0
    for i in range(n + 1):
        sumanew = sumanew + i
        i += 1
    print("Suma primelor n numere este: ", sumanew)


def suma_primelor_n_numere_naturale_v2(n):
    sumanew2 = n * (n + 1) / 2
    print("Suma primelor n numere naturale folosind formula clasica n(n+1)/2 este: ", sumanew2)


# Functie care primesete 2 liste de numere (numerele pot fi dublate)
# Returnati numerele comune

def elemente_comune_unice_lista(list1, list2):
    elemente_comune_temp = []
    elemente_unice = []
    for element in list1:
        if element in list2:
            elemente_comune_temp.append(element)
    print("Elementele comune ale celor 2 multimi este: ", elemente_comune_temp)
    for i in range(len(elemente_comune_temp)):
        if elemente_comune_temp[i] not in elemente_unice:
            elemente_unice.append(elemente_comune_temp[i])
    print("Elementele comune unice ale celor 2 multimi este:", elemente_unice)


# Functie care converteste un string de elemente intr-o lista de elemente int

# def conversie_string_to_int(string1):
#     lista_new = []
#     for element in range(len(string1)):
#         lista_new.append(string1[element])
#         print(type(element))
#         if element == ",":
#             lista_new.pop(element)
#     print("conversia ii", lista_new)

# Functie care sa aplice o reducere de pret
def discount_pret(pret_produs, discount):
    if discount in range(0, 100):
        pret_produs = pret_produs - discount * pret_produs / 100
        print("Noul pret al produsului este: ", pret_produs)
    else:
        print("Discuntul introdus nu este valid!")


# Functie care primeste o lista de cifre (adica doar 0-9)
# # Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# # Returneaza un DICT care ne spune de cate ori apare fiecare cifra

# def dictionar_elemente_unice(newlist):
#     dictionar = {}
#     for i in range(len(newlist)):
#         dictionar[newlist[i]] = newlist.count(newlist[i])
#     for key, value in dictionar.items():
#         print(key, ":", value)

def dictionar_elemente_unice(newlist):
    dictionar = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
    }
    for key, value in dictionar.items():
        for i in range(len(newlist)):
            if key == newlist[i]:
                dictionar[key] = newlist.count(newlist[i])
    for key1, value1 in dictionar.items():
        print(key1, ":", value1)
