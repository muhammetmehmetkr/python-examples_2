print("""
***********************
    PERFECT NUMBER      6, 28, 496 --> 1 ile 1000 arasi 
***********************
""")

toplam = 1  # butun sayilar 1'e bolunur...
sayi = int(input("Lutfen sayi giriniz: "))

for i in range(2, int(sayi+1/2)):
    if (sayi % i == 0):
        toplam += i     # sayinin bolenlerinin toplandigi kisim...
if (toplam == sayi):
        print("mukemmel sayidir...")
else:
    print("mukemmel sayi degildir...")
