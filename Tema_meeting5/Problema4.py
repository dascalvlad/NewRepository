from functions import aria_dreptunghi
x = float(input("Introduceti prima latura a dreptunghiului: "))
y = float(input("Introduceti a 2 a latura a dreptunghiului: "))

if (x <= 0) or (y <= 0):
    print("Datele introduse nu sunt valide! Incercati din nou! ")
else:
    aria_dreptunghi(x,y)