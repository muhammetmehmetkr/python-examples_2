def name(isim="bilgi yok..."):
    print("isminiz:", isim)

name()  # syntax error almamak icin parametre girilmezse 'bilgi yok' yazdirilir...
name("mehmet")

def show_inf(ad="bilgi yok", soyad="bilgi yok", numara="bilgi yok"):
    print("ad:", ad, "soyad:", soyad, "numara:", numara)

show_inf("mehmet", "kir", 34)
show_inf("mehmet", "kir")
show_inf(numara=34)  # sadece numara bilgisi varsa..

# Esnek sayida degerler
def yazdir(*a):  # '*' sayesinde istedigimiz kadar parametre girebiliriz..demet yapisi olusturur.
    print(a)

yazdir(1, 2, 3, 4, 5, 6)

def toplama(*b):
    toplam = 0
    for i in b:
        toplam += i
    print(toplam)

toplama(10, 20, 30)
