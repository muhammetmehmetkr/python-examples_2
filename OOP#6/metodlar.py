class Yazilimci():
    def __init__(self, ad, soyad, numara, maas):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.maas = maas
    def bilgileri_goster(self):
        print("""
    Ad: {}
    Soyad: {}
    Numara: {}
    Maas: {}                
        """.format(self.ad, self.soyad, self.numara, self.maas))
    def zam_ekle(self, zam_miktari):
        self.maas += zam_miktari    # maas parametresinde degisiklik yaparken yine 'self' parametresi kullanildi..

yazilimci1 = Yazilimci("Mehmet", "KIR", 34, 5000)

yazilimci1.bilgileri_goster()
yazilimci1.zam_ekle(1000)
yazilimci1.bilgileri_goster()
