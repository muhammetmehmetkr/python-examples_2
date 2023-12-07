class Kitap():
    def __init__(self, isim, sayfa_sayisi, tur):
        self.isim = isim
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur

    def __str__(self):
        return "Isim: {}\nSayfa sayisi:{}\nTur:{}\n".format(self.isim, self.sayfa_sayisi, self.tur)

    def __len__(self):
        return self.sayfa_sayisi

    def __del__(self):
        print("Kitap objesi siliniyor...")  # silindigini gormek icin..

kitap1 = Kitap("Donusum", 150, "roman")
print(kitap1)    # str methodu

print(len(kitap1))  # len methodu

# del kitap1  # dersek kitap1 objesi silinir ve print(kitap1) dersek kitap1 is undefined hatasi aliriz.
