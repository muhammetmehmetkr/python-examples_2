boy = float(input("boyunuzu metre cinsinden giriniz: "))
kilo = int(input("kilonuzu giriniz: "))
bki = (kilo/boy**2)

if bki > 0 and bki < 18.5:
    print("zayif")
elif bki >= 18.5 and bki < 25:
    print("normal")
elif bki > 25 and bki < 30:
    print("fazla kilolu")
elif bki >= 30:
    print("obez")
elif bki < 0:
    print("gecersiz deger")