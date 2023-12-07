print("""
*********************
  SAYI TAHMIN OYUNU     
*********************
""")
import time
import random

kalan_hak = 7
rastgele_sayi = random.randint(1, 40)   # 1 ve 40 arasi sayi tahmin oyunu

while True:

    sayi = int(input("sayi giriniz:"))

    if sayi < rastgele_sayi:
        print("bilgiler sorgulaniyor...")
        time.sleep(1)
        print("lutfen daha buyuk sayi tahmin ediniz...")
        kalan_hak -= 1
    elif sayi > rastgele_sayi:
        print("bilgiler sorgulaniyor...")
        time.sleep(1)
        print("lutfen daha kucuk sayi tahmin ediniz...")
        kalan_hak -= 1
    else:
        print("bilgiler sorgulaniyor...")
        time.sleep(1)
        print("Tebrikler bildiniz, sayimiz {}".format(rastgele_sayi))
        break
    if kalan_hak == 0:
        print("hakkiniz bitmistir, sayimiz {}".format(rastgele_sayi))
        break

