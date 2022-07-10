# # Q1: # Declara o lista note_muzicale in care sa pui do re mi etc pana la do
#
# #                 0      1     2    3     4      5     6     7
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]

# 1. Afiseaz-o
print("Notele muzicale salvate in lista sunt: ", note_muzicale)
print(type(note_muzicale))

# 2. Inverseaza ordinea folosind slicing si suprascrie aceasta lista

note_muzicale = note_muzicale[::-1]

# 3. Printeaza varianta actuala (inversata)
print("Notele muzicale afisate in ordine inversa (folosind slicing) sunt: ", note_muzicale)

#print("Notele muzicale afisate in ordine inversa (folosind slicing) sunt: ", note_muzicale[len(note_muzicale)-1:0:-1])
#de ce nu afiseaza corect toata lista invers?

# 4. Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea.
#    (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)

note_muzicale.reverse()

# 5. Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
print("Notele muzicale inversate sunt folosind metoda reverse(): ", note_muzicale)

#print(note_muzicale.reverse())
# De ce nu merge aceasta metoda?

# Q2: De cate ori apare ‘do’?

print("Nota ~do~ apare de :", note_muzicale.count("do"), "ori")