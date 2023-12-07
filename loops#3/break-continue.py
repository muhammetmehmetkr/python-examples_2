# break
while True:     # sartli sonsuz dongu...
    sayi = int(input("lutfen sayi giriniz(-1 to end): "))
    if (sayi == -1):
        print("programdan cikiliyor...")
        break
    print("girdiginiz sayi: ", sayi)
# continue
for i in range(11):
    if(i == 5 or i == 7):  # bu degerleri atlayip dongu basina doner..
        continue
    print("i: ", i)

