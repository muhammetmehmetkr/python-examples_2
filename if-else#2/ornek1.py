print("""********************
---HESAP MAKINESI---
1. TOPLAMA ISLEMI
2. CIKARMA ISLEMI
3. CARPMA ISLEMI
4. BOLME ISLEMI
********************
""")
a = int(input("1. sayiyi giriniz: "))
b = int(input("2. sayiyi giriniz: "))

islem = (input("islem seciniz: "))

if islem == "1":
    print("{} + {} nin sonucu: {} dir".format(a, b, a+b))
elif islem == "2":
    print("{} - {} nin sonucu: {} dir".format(a, b, a-b))
elif islem == "3":
    print("{} * {} nin sonucu: {} dir".format(a, b, a*b))
elif islem == "4":
    print("{} / {} nin sonucu: {} dir".format(a, b, a/b))
else:
    print("gecersiz islem...")
