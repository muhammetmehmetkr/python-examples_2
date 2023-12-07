liste = []

def bolenler(sayi):
    for i in range(2, sayi):
        if sayi % i == 0:
            liste.append(i)
    return liste

while True:
    sayi = input("sayi giriniz:")
    if sayi == "q":
        break
    else:
        sayi = int(sayi)
        print("sayinin bolenleri:", bolenler(sayi))
