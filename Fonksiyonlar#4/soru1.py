liste = []

def perfect(liste):
    for i in range(2, 1000):
        toplam = 0
        for j in range(1, int(i+1/2)):
            if i % j == 0:
                toplam += j
        if toplam == i:
            liste.append(i)
    return liste

print(perfect(liste))
