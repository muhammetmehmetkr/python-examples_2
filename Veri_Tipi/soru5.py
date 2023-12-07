a = int(input("1.sayiyi giriniz: "))
b = int(input("2.sayiyi giriniz: "))
print("1.sayi: {}  2.sayi: {}".format(a, b))
a, b = b, a
print("sayilarin yeni hali...\n1.sayi: {}  2.sayi: {}".format(a, b))
