# ornek-1
liste = ["345", "sadas", "324a", "14", "kemal"]
for i in liste:
    try:
        i = int(i)
        print(i)
    except:
        pass
# ornek-2
def tek_cift(a):
    if a % 2 == 0:
        return a
    else:
        raise ValueError

sayi = int(input("sayi giriniz:"))
print(tek_cift(sayi))

liste2 = [2, 3, 4, 5, 6, 7, 8]
try:
    for i in liste2:
        if i % 2 == 0:
            print(tek_cift(i))
except ValueError:
    pass
