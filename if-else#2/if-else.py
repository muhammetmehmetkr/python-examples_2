"""# if-else
yas = int(input("yasinizi giriniz: "))
if (yas < 18 ):
    print("bu mekana giremezsiniz...")
else:
    print("bu mekana girebilirsiniz...")
# if-elif-else
islem = int(input("islem seciniz(1-4): "))

if islem == 1:
    print("1. islemi sectiniz.")
elif islem == 2:
    print("2. islemi sectiniz.")
elif islem == 3:
    print("3. islemi sectiniz.")
elif islem == 4:
    print("4. islemi sectiniz.")
else:
    print("gecersiz islem.")"""

note = float(input("notunuzu giriniz: "))

if note >= 90:
    print("AA")
elif note >= 85:
    print("BA")
elif note >= 80:
    print("BB")
elif note >= 75:
    print("CB")
elif note >= 70:
    print("CC")
elif note >= 65:
    print("DC")
elif note >= 60:
    print("DD")
else:
    print("dersten kaldiniz.")
