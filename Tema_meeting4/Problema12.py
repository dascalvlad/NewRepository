# Aceeasi lista
# Ordonati crescator lista fara sa folositi sort
# Va puteti inspira vizual de aici
# https://www.youtube.com/watch?v=lyZQPjUT5B4

#               0  1  2  3  4   5  6   7   8  9
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
alte_numere.sort()
print(alte_numere)


for i in range(0, len(alte_numere)):
    for j in range(i+1, len(alte_numere)):
        if alte_numere[i] >= alte_numere[j]:
            temp = alte_numere[i]
            alte_numere[i] = alte_numere[j]
            alte_numere[j] = temp
print(alte_numere)

