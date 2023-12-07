toplam = 0
while True:
    sayi = input("lutfen sayi giriniz: ")
    if (sayi == "q"):
        break
    toplam += int(sayi)
    print("toplam: {}".format(toplam))
