print("""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
""")
sayi = input("sayi giriniz: ")
basamak_sayisi = len(sayi)

toplam = 0
sayi = int(sayi)
sayi2 = sayi

while sayi > 0:
    toplam += (sayi % 10) ** basamak_sayisi
    sayi = int(sayi/10)

print("toplam: {}".format(toplam))
if toplam == sayi2:
    print("Armstrong sayisidir...")
else:
    print("Armstrong sayisi degildir...")
