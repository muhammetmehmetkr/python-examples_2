while True:
    sayi = int(input("Lutfen pozitif bir tam sayi giriniz(-1 to end): "))

    if (sayi == -1):
        break
    else:
        faktoriyel = 1
        for i in range(2, sayi+1):
            faktoriyel *= i
        print("faktoriyel: {}".format(faktoriyel))
