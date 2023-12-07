print("""********************************
GEOMETRIK SEKIL HESAPLAMA ISLEMI
1. DORTGEN HESAPLAMA
2. UCGEN HESAPLAMA
********************************
""")
islem = int(input("islem numarasi giriniz: "))

if islem < 1 or islem > 2:
    print("gecersiz islem")
if islem == 1:
    a = int(input("dortgenin 1. kenarini giriniz: "))
    b = int(input("dortgenin 2. kenarini giriniz: "))
    c = int(input("dortgenin 3. kenarini giriniz: "))
    d = int(input("dortgenin 4. kenarini giriniz: "))
    if a == b == c == d:
        print("kare")
    elif a == c and b == d and a < b or a > b:
        print("dikdortgen")
    elif a != b != c != d:
        print("cesitkenar dortgen")
if islem == 2:
    a = int(input("ucgenin 1. kenarini giriniz: "))
    b = int(input("ucgenin 2. kenarini giriniz: "))
    c = int(input("ucgenin 3. kenarini giriniz: "))
    if abs(b-c) < a < b+c and abs(a-c) < b < a+c and abs(a-b) < c < a+b:
        print("ucgendir.")
        if a == b == c:
            print("eskenar ucgen")
        elif a == b or a == c and b != c:
            print("ikizkenar ucgen")
    else:
        print("ucgen degildir.")