a = int(input("1. sayiyi giriniz: "))
b = int(input("2. sayiyi giriniz: "))
c = int(input("3. sayiyi giriniz: "))

if a > b and a > c:
    print("en buyuk sayi 1. sayidir.")
elif b > a and b > c:
    print("en buyuk sayi 2. sayidir.")
elif c > a and c > b:
    print("en buyuk sayi 3. sayidir.")
