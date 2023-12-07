# in operatoru
print("m" in "mehmet")
print("et" in "mehmet")
print(10 in [1, 2, 3, 4])

# for dongusu
liste = [1, 3, 5, 7, 9]
for i in liste:
    print(i)

liste1 = [2, 4, 6, 8, 10]
toplam = 0
for i in liste1:
    toplam += i
print("toplam = ", toplam)

liste2 = [13, 15, 17, 28, 34, 39, 456]
result = 0
for i in liste2:
    if i % 2 == 0:
        result += i
print("cift sayilarin toplami {}".format(result))
# stringlerde gezinme
kelime = "mehmet"
for i in kelime:
    print(i)

kelime = "mehmet"
for i in kelime:
    print(i*3)
# demet yapilarinda gezinme
demet = (1, 4, 7, 10, 13, 16)
for i in demet:
    print(i)

demet = [(1, 2), (3, 4), (5, 6)]
for i in demet:
    print(i)

demet = [(1, 2), (3, 4), (5, 6)]
for i, j in demet:
    print(i, j)

demet = [(1, 2, 7), (3, 4, 8), (5, 6, 9)]
for i, j, k in demet:
    print(i * j * k)
# sozlukler uzerinde gezinmek
sozluk = {"bir": 1, "iki": 2, "uc": 3, "dort": 4}
print(sozluk.keys())
print(sozluk.values())
print(sozluk.items())

# metodlari kullanmazsak sadece anahtarlari yazdirir.
sozluk = {"bir": 1, "iki": 2, "uc": 3, "dort": 4}
for i in sozluk:
    print(i)

print("*********************")

sozluk = {"bir": 1, "iki": 2, "uc": 3, "dort": 4}
for i in sozluk.keys():
    print(i)

sozluk = {"bir": 1, "iki": 2, "uc": 3, "dort": 4}
for i in sozluk.values():
    print(i)

sozluk = {"bir": 1, "iki": 2, "uc": 3, "dort": 4}
for i, j in sozluk.items():
    print("-keys-: ", i, "values: ", j)

