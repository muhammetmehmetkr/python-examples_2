import random
import time

class Kumanda():
    def __init__(self, tv_durum="kapali", tv_ses=0, kanal_listesi=["Trt"], kanal="Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if self.tv_durum == "acik":
            print("tv zaten acik")
        else:
            print("tv aciliyor")
            self.tv_durum = "acik"

    def tv_kapat(self):
        if self.tv_durum == "kapali":
            print("tv zaten kapali")
        else:
            print("tv kapaniyor")
            self.tv_durum = "kapali"

    def ses_duzeyi(self):
        while True:
            cevap = input("Sesi azalt:'<' \nSesi arttir:'>' \nCikis:cikis")
            if cevap == "<":
                if self.tv_ses != 0:
                    self.tv_ses -= 1
                    print("Ses: ", self.tv_ses)
            elif cevap == ">":
                if self.tv_ses != 32:
                    self.tv_ses += 1
                    print("Ses: ", self.tv_ses)
            else:
                print("Ses guncellendi: ", self.tv_ses)
                break

    def kanal_ekle(self, kanal_ismi):
        print("kanal ekleniyor")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("kanal eklendi")

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Su anki kanal: ", self.kanal)

    def __len__(self):

        return len(self.kanal_listesi)

    def __str__(self):

        return "Tv durumu: {}\nTv ses: {}\nKanal listesi: {}\nKanal: {}\n".format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal)


kumanda = Kumanda()  # obje olusturuldu..
print("""
============================
1.TV ac
2.TV kapat
3.Ses ayarlari
4.Kanal ekle
5.Kanal sayisini ogrenme
6.Rastgele kanala gecme
7.Tv bilgileri
8.Cikis 'q'
=============================
""")

while True:
    islem = input("Lutfen islem seciniz: ")

    if islem == "q":
        break
    if islem == "1":
        kumanda.tv_ac()
    elif islem == "2":
        kumanda.tv_kapat()
    elif islem == "3":
        kumanda.ses_duzeyi()
    elif islem == "4":
        kanal_isimleri = input("Kanal isimlerini ',' ile ayirarak giriniz")
        kanal_listesi = kanal_isimleri.split(",")
        for i in kanal_listesi:
            kumanda.kanal_ekle(i)
    elif islem == "5":
        print("kanal sayisi: ", len(kumanda))
    elif islem == "6":
        kumanda.rastgele_kanal()
    elif islem == "7":
        print(kumanda)
    else:
        print("gecersiz islem..")






