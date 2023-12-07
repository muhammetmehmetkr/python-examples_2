# demet veri tipi --> tuple
demet1 = (3, 4, 5, 6)
print(demet1)

# count ve index metodu

demet1 = (1, 2, 4, 5, "mehmet")
print(demet1.index("mehmet"))  # index ini bulur.
demet2 = (1, 1, 1, 3, 3, 3, 3, 4, 4, 4, 4, 4)
print(demet2.count(1))  # kac tane oldugunu soyler. sayac mantigi

# demetler kesinlikle degistirilemez veya deger atanamaz.

# sozlukler --> dict

sozluk1 = {"bir": 1, "iki": 2, "uc": 3}
sozluk2 = {}
print(sozluk1["bir"])
sozluk1["bes"] = 5  # deger atayabiliyoruz.
print(sozluk1)
sozluk3 = {"bir": [1, 3], "iki": [[2, 4], [8, 10]], "uc": [6, 9]}
print(sozluk3)
print(sozluk3["uc"])
print(sozluk3["iki"][0][1])

# ic ice sozlukler

sozluk1 = {"sayilar": {"bir": 1, "iki": 2}, "meyveler": {"kiraz": "yaz", "portakal": "kis"}}
print(sozluk1["sayilar"]["bir"])
print(sozluk1["meyveler"]["kiraz"])

# temel sozluk metodlari

yeni_sozluk = {"bir": 1, "iki": 2, "üç": 3}
print(yeni_sozluk.values())   # values() metodu sözlüğün değerlerini(value) bir liste olarak döner.
print(yeni_sozluk.keys())     # keys() metodu sözlüğün anahtarlarını(key) bir liste olarak döner.
print(yeni_sozluk.items())   # items() metodu sözlüğün anahtar ve değerlerini bir liste içinde demet olarak döner.
