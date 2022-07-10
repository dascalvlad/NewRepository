# Q8: X, y, z - laturile unui triunghi
# Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.

x = int(input('Intrudu latura X a triunghiului: '))
y = int(input('Intrudu latura Y a triunghiului: '))
z = int(input('Intrudu latura Z a triunghiului: '))

if x <=0 or y<=0 or z<=0:
    print('Laturile introduse trebuie sa fie numere naturale!')
elif x == y == z:
    print("Triunghiul este ECHILATERAL!")
elif x == y or y == z or x == z:
    print('Triunghiul este ISOSCEL!')
else:
    print('Triunghiul este OARECARE!')