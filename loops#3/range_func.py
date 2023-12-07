print(*range(1, 21))

liste = list(range(1, 5))  # 5 dahil degildir.
print(liste)

print(*range(5, 16, 5))

print(*range(4))  # baslangic degeri vermezsek 0 dan baslar.

print(*range(20, 0, -4))  # geri geri sayar.

for sayi in range(0, 11, 2):  # for dongusu ile dolasma.
    print(sayi)

for sayi in range(1, 6):
    print("# " * sayi)  # carpiyoruz.
