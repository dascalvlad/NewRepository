# Modernizati parcul de masini
# Creati o lista goala, masini_vechi

# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# Salvati aceste masini in masini_vechi
# Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x


masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

masina = input("Introduceti masina care sa fie scoasa din lista!  ")
masina_new = input("Introduceti masina care sa fie introdusa in lista!  ")
masini_vechi = []
for i in range(len(masini)-1):
    if masini[i] == masina:
        print("Masina ~", masina, "~ a fost gasita in lista!")
        masini_vechi.append(masina)
        masini.remove(masina)
        masini.append(masina_new)
        print("Lista de masini scoase din uz este: ",masini_vechi)
        print("Lista de masini noi/actualizate este: ", masini)
# else:
#     print("test ") # cum fac sa am un singur mesaj de eroare?

