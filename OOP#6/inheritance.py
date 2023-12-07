class Calisan():
    def __init__(self, ad, maas, departman):
        print("calisan sinifi init fonksiyonu")
        self.ad = ad
        self.maas = maas
        self.departman = departman
    def bilgileri_goster(self):
        print("Ad: {}\nMaas: {}\nDepartman: {}\n".format(self.ad, self.maas, self.departman))
    def departman_degistir(self, yeni_departman):
        self.departman = yeni_departman

calisan1 = Calisan("mehmet", 3000, "bilisim")
calisan1.bilgileri_goster()

class Yonetici(Calisan):   # miras aktarilmistir...
    def zam_ekle(self, zam_miktari):    # eger class altinda method tanimlanmazsa 'pass' komutu yaz.boylece class hatasi vermez..
        self.maas += zam_miktari

yonetici1 = Yonetici("ali", 7000, "muhasebe")
yonetici1.bilgileri_goster()

yonetici1.departman_degistir("insan kaynaklari")
yonetici1.bilgileri_goster()

yonetici1.zam_ekle(1000)
yonetici1.bilgileri_goster()

# OVERRIDING --> mirasi iptal etme
class Yonetici(Calisan):
    def __init__(self, ad, maas, departman, kisi_sayisi):
        print("Yonetici sinifi init fonksiyonu")
        self.ad = ad
        self.maas = maas
        self.departman = departman
        self.kisi_sayisi = kisi_sayisi

    def bilgileri_goster(self):
        print("Ad: {}\nMaas: {}\nDepartman: {}\nSorumlu oldugu kisi sayisi: {}\n".format(self.ad, self.maas, self.departman, self.kisi_sayisi))

    def zam_ekle(self, zam_miktari):
        self.maas += zam_miktari

yonetici2 = Yonetici("Omer", 14000, "Bilisim", 20)
yonetici2.bilgileri_goster()

# super anahtar kelimesi --> istedigimiz ozellikleri miras alma..
class Calisan():
    def __init__(self, ad, maas, departman):
        print("calisan sinifi init fonksiyonu")
        self.ad = ad
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print("Ad: {}\nMaas: {}\nDepartman: {}\n".format(self.ad, self.maas, self.departman))

    def departman_degistir(self, yeni_departman):
        self.departman = yeni_departman

class Yonetici(Calisan):
    def __init__(self, ad, maas, departman, kisi_sayisi):
        super().__init__(ad, maas, departman)
        print("Yonetici sinifi init fonksiyonu")
        self.kisi_sayisi = kisi_sayisi

    def bilgileri_goster(self):
        print("Ad: {}\nMaas: {}\nDepartman: {}\nSorumlu oldugu kisi sayisi: {}\n".format(self.ad, self.maas, self.departman, self.kisi_sayisi))

    def zam_ekle(self, zam_miktari):
        self.maas += zam_miktari

yonetici3 = Yonetici("Ahmet", 6000, "muhasebe", 5)
yonetici3.bilgileri_goster()
