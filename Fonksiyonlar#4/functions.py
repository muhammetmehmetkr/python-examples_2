def selamla():
    print("merhaba..\nNasilsiniz?")

selamla()     # paramaetresiz fonksiyon cagirma

def print_name(isim):
    print("isminiz:", isim)

print_name("mehmet")

def toplama(a, b, c):
    print("toplam:", a+b+c)

toplama(3, 4, 5)

def faktoriel(sayi):
    faktoriyel = 1
    if faktoriyel == 0 and faktoriyel == 1:
        faktoriyel = 1
    while (sayi >=1 ):
        faktoriyel *= sayi
        sayi -= 1
    print("faktoriyel:", faktoriyel)
faktoriel (6)

def toplam2(a, b):
    return a+b

def carpma(x):
    return 4*x

def bolme(y):
    return y/5

print(bolme(carpma(toplam2(4, 9))))
