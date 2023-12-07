file = open("C:/Users/k1r/Desktop/python/bilgiler.txt", "r")   # read methodu
for i in file:      # for dongusu ile okuma
    print(i, end="")
file.close()    # dosya ile islem bittikten sonra kapatilmalidir.

file = open("C:/Users/k1r/Desktop/python/bilgiler.txt", "r")
icerik = file.read()    # read() fonksiyonu ile okuma
print("dosya icerigi:\n", icerik, sep="")
file.close()

file = open("C:/Users/k1r/Desktop/python/bilgiler.txt", "r")
print(file.readline())    # readline() ile okuma
file.close()

file = open("C:/Users/k1r/Desktop/python/bilgiler.txt", "r")
liste = file.readlines()    # file.readlines() ile okuma
print(liste)
file.close()
