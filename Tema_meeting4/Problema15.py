# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# Iterati prin lista 2d
# Printati ‘Cifra curenta este x’
# (hint: nested for - adica for in for)


tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
# for i in range(len(tastatura_telefon)-1):
#     for j in range(0,3):
#         tasta = tastatura_telefon[i][j] # cum pot sa folosesc range (0, i)??
#         print("Cifra curenta de pe tastatura este: ", tasta)
print(len(tastatura_telefon))
for i in range(0,len(tastatura_telefon)):
# for i in range(0, len(tastatura_telefon) - 1): dc asa nu afisez tasta 0?
    for j in range(0,len(tastatura_telefon[i])):
        tasta = tastatura_telefon[i][j] # cum pot sa folosesc range (0, i)??
        print("Cifra curenta de pe tastatura este: ", tasta)

# t=[]
# for item in tastatura_telefon:
#     t.append(len(item))
# print(t)
# print(len(t[0])






