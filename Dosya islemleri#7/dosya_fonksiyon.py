with open("C:/Users/k1r/Desktop/python/bilgiler2.txt", "r") as file:  # with open ile islem bitince dosya kapanir..
    for i in file:
        print(i, end="")

with open("C:/Users/k1r/Desktop/python/bilgiler2.txt", "r") as file:
    file.seek(5)          # icine deger verilmezse dosyanin basina gelir.
    icerik = file.read(10)
    print("\n")
    print(file.tell())     # dosyanin kacinci byte'inda oldugumuzu soyler.
    print(icerik)
