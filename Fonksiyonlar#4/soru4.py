birler = ["", "bir", "iki", "uc", "dort", "bes", "alti", "yedi", "sekiz", "dokuz"]
onlar = ["", "on", "yirmi", "otuz", "kirk", "elli", "altmis", "yetmis", "seksen", "doksan"]

def sayi_yazdir(sayi):
    birinci = sayi % 10
    ikinci = int(sayi / 10)

    return onlar[ikinci]+" "+birler[birinci]

sayi = int(input("sayi giriniz:"))
print(sayi_yazdir(sayi))
