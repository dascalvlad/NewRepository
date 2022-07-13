# import math
# # Q1: In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila
# # R1: variabila - reprezinta un sector de memorie in care se stocheaza un continut/valoare ce poate fi de mai multe feluri: string, int, float,
# #     si al carei continut/tip poate sa varieze in timp (prin suprascriere)
#
# # Q2: Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri: string, int, float, bool
# #     Valorile le alegeti voi dupa preferinte
# # Q3: Utilizat functia type pentru a verifica daca au tipul de date asteptat
# # Q5: Folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
# #     (rezolvati nepotrivirile de tip prin ce modalitate doriti)
#
# x = 'x = Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri: string, int, float, bool'
# print(x)
# print('Variabila X este de tipul', type(x))
#
# y = len(x)
# print('Variabila Y are valoarea', y, ' si este de tipul: ',type(len(x)))
#
# PI = math.pi
# print('Numarul PI are valoarea ', PI, 'si este de tipul', type(PI))
#
# t = False
# print('variabila T este de tipul:', type(t))
#
# # Q4: Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
# #     Verificati tipul acesteia
#
# print('Rotunjirea la 3 zecimale a numarului PI este',round(PI,3))
#
# # Q6: citeste de la tastatura numele. citeste de la tastatura prenumele
# #     afiseaza 'Numele complet are x caractere'
#
# nume = input('Care este numele tau: ?')
# prenume = input('Care este prenumele tau: ?')
#
# #print('Numele complet furnizat de la tastatura este:', nume.upper(), prenume.upper(),'si are', len(nume+prenume),'caractere')
#
# # Q7: citeste de la tastatura lungimea
# #     citeste de la tastatura latimea
# #     afiseaza 'Aria dreptunghiului este x'
#
# # lungime = float(input('Lungimea este:'))
# # latime = float(input('Latimea este:'))
# # print('Aria dreptunghiului este:',lungime*latime)
# # ipotenuza = math.sqrt(pow(lungime,2)+pow(latime,2))
# # print('Aria cercului circumscris este:',PI*pow((ipotenuza*0.5),2))
#

# Q8: Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
#     cititi de la tastatura un int x
#     afiseaza stringul fara ultimele x caractere

#string1 = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input('Introduceti valoarea pentru X: '))
# print('Noul string fara X caractere, este:',string1[0:(len(string1)-x)])
# print(string1[0:(len(string1)+1)])


# Q9: acelasi string
#     declara un string nou care sa fie format din primele 5 caractere + ultimele 5

# string2 = string1[0:5]+string1[-5:]
# print("Afiseaza primele 5 caractere si ultimele 5 caractere:", string2)


# Q10: acelasi string
#      afisati de cate ori apare cuvantul 'the'

# string3='the'
# count1 = string1.count(string3)
# print('Cuvantul ~the~ apare de :', count1, ' ori')

# Q11: acelasi string. # inlocuieste the cu THE peste tot
#      printeaza rezultatul

# string4 = string1.replace('the','THE',2)
# print('Inlocuieste doar primele 2 cuvinte ~the~ cu ~THE~ :', string4)

# Q12: acelasi string
#      salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
#      (hint: este o functie care te ajuta sa faci asta)
#      folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
#      output: 'Coral is either the stupidest animal or the smartest '

# string5 = 'rock'
# c = string1.find(string5)
# print('Indexul de start al cuvantului ~rock~ este:',c )
# #print('Indexul de start al cuvantului ~rock~ este:', c) // care ii mai corecta???
# print(string1[0:53])

# Q13: citeste de la tastatura un string
#      verifica daca primul si ultimul caracter sunt la fel
#      se va folosi un assert
#      atentie: se doreste ca programul sa fie case insensitive
#      'apA' e acceptat

# string6 = input('Introdu un string de la tastatura:')
# print(string6)
# if string6[0] == string6[len(string6)-1]:
#     print('Primul si ultimul caracter este identic')
# else:
#     print('Primul si ultimul caracter nu este identic')
# assert string6[0].capitalize() == string6[len(string6)-1].capitalize()
# print('Primul caracter (', string6[0],') si ultimul caracter (', string6[len(string6)-1], ') din sir este identic')
#
# assert string6[0] != string6[len(string6)-1]
# print('Primul si ultimul caracter din sir NU este identic')