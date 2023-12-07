# liste veri tipi
liste1 = [1, 4, "elma", 3.14, 5.31231]
print(liste1)

empty_list = []
print(empty_list)  # bos liste

# list() fonksiyonu
empty_list = list()
print(empty_list)

# len() fonksiyonu
print(len(liste1))

# Bir string list() fonksiyonu yardımıyla listeye dönüştürülebilir.
kelime = "mehmet"
liste2 = list(kelime)
print(liste2)

""" Listeleri Indeksleme ve Parçalama """
liste3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(liste3)
print(liste3[0])
print(liste3[:4])
print(liste3[5:])
print(liste3[::2])
print(liste3[::-1])

""" Temel Liste Metodları ve İşlemleri """
liste1 = [1, 2, 3, 4]
liste2 = [5, 6, 7, 8]
print(liste1 + liste2)

liste3 = [5, 10, 15]
liste3 = liste3 + ["mehmet"]
print(liste3)
print(liste3 * 3)
print(liste3)  # liste degismiyor.
liste3 = liste3 * 3
print(liste3)  # esitleme yaptigimiz icin degisti.

""" append metodu """
# append metodu, verdiğimiz değeri listeye eklememizi sağlar.
liste1 = [1, 4, 7, 10]
liste1.append(13)
print(liste1)

# pop metodu

""" Bu metod, içine değer vermezsek listenin son indeksindeki elemanı,
değer verirsek verdiğimiz değere karşılık gelen indeksteki elemanı listeden atar ve attığı elemanı ekrana basar """
liste2 = [1, 2, 3, 4, 5]
liste2.pop()
print(liste2)
liste2.pop(0)
print(liste2)

# sort metodu

liste1 = [45, 320, 210, 75, 10, 99]
liste1.sort()   # kucukten buyuge
print(liste1)
liste1.sort(reverse=True)  # buyukten kucuge
print(liste1)
liste2 = ["muz", "elma", "armut", "kiraz"]
liste2.sort()
print(liste2)
liste2.sort(reverse=True)
print(liste2)

# ic ice listeler

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste3 = [7, 8, 9]
yeni_liste = [liste1, liste2, liste3]
print(yeni_liste)
print(yeni_liste[0])
print(yeni_liste[1][1])
