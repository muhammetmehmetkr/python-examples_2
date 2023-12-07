print("""
********************************
        ATM PROGRAMI
1. Bakiye sorgulama
2. Para yatirma
3. Para cekme
********************************
""")

bakiye = 2000

while True:
    islem_numarasi = int(input("Islem numarasi giriniz: "))

    if (islem_numarasi == -1):
        print("iyi gunler...")
        break
    elif (islem_numarasi == 1):
        print("bakiyeniz: {} TL'dir".format(bakiye))
    elif (islem_numarasi == 2):
        miktar = int(input("yatirmak istediginiz para miktari: "))
        bakiye += miktar
    elif (islem_numarasi == 3):
        miktar = int(input("cekmek istediginiz para miktari: "))
        if (bakiye - miktar < 0 ):
            print("boyle bir miktar cekemezsiniz...")
            continue
        bakiye -= miktar
    else:
        print("Gecersiz islem...")
