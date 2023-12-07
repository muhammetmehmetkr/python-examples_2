a = int(input("vize 1 notunuzu giriniz: "))
b = int(input("vize 2 notunuzu giriniz: "))
c = int(input("fianl notunuzu giriniz: "))

toplam_not = (a*30/100) + (b*30/100) + (c*40/100)

if toplam_not >= 90:
    print("AA")
elif toplam_not >= 85:
    print("BA")
elif toplam_not >= 80:
    print("BB")
elif toplam_not >= 75:
    print("CB")
elif toplam_not >= 70:
    print("CC")
elif toplam_not >= 65:
    print("DC")
elif toplam_not >= 60:
    print("DD")
elif toplam_not >= 55:
    print("FD")
elif toplam_not <= 55:
    print("FF")
