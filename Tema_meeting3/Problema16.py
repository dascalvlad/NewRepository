
# Q16: Ne imaginam o echipa de fotbal pt teren sintetic.
#      3 Schimbari maxime admise
#
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
# Schimbari_max = 3
#
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# Efectuam schimbarea
# Stergem jucatorul scos din lista
# Adaugam jucatorul intrat
# Afisam a intra x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Afisati ‘mai aveti z schimbari’
#
# Testati codul cu diferite valori
#
# Google search hint
# “how to check if item is in list python”
import random
lista_jucatori = ["Hagi", "Dumitrescu", "Popescu", "Stelea", "Sabau"]
schimbari_ramase = 3



# if "Hagi" in lista_jucatori:
#     lista_jucatori.remove("Hagi")
#     lista_jucatori.append("Mutu")
#     schimbari_ramase -= 1
# print("Lista actualizata a jucatorilor din teren este:", lista_jucatori, "\n")
# print("numarul de Schimbari ramase este ", schimbari_ramase)

while schimbari_ramase !=0:
    jucator_schimbat = [input("Introduceti jucatorul care va iesi de pe teren: ")]
    print(jucator_schimbat)
    if jucator_schimbat[0] in lista_jucatori: #care ii cealalta varianta?
        lista_jucatori.remove(jucator_schimbat[0])
        jucator_nou = [input("Introduceti jucatorul care va intra pe teren: ")]
        print(jucator_nou)
        lista_jucatori.append(jucator_nou[0])
        schimbari_ramase -= 1
        print("Lista actualizata a jucatorilor din teren este:", lista_jucatori, "\n")
        print("numarul de Schimbari ramase este ", schimbari_ramase)
    else:
        print("nu se poate efectua schimbarea, deoarece jucatorul nu este pe teren! ")
        break

# for i in range(0,len(lista_jucatori)):
#     print("Lista actualizata de jucatori este: \n")
#     print(lista_jucatori[i])
