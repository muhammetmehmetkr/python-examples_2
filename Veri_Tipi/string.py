# string(karakter dizileri)

""""print('mehmet')
print("mehmet")"""
print("""mehmet""")     # 3 farkli sekilde yazilabiliyor.

print("mehmet'in bugun dersi var")

a = "k1r"
print(a)
print(a[0])

# sondaki eleman -1 den baslar
print(a[-1])
# [baslamaindeksi : bitisindeksi : atlamadegeri]

a = "python programlama dili"
print(a[2:9])  # 9.indeks dahil degildir
print(a[:9])  # b.degeri belirtilmemis ise en bastan
print(a[4:])
print(a[:])
print(a[:-1])  # son karaktere kadar
print(a[::2])
print(a[4:12:3])
print(a[::-1])  # -1den baslar --> string ters cevrilir.

# string length
a = "python"
print(len(a))
a = "python "
b = "programlama "
c = "dili"
print(a+b+c)
a = "mehmet "
a = a+"k1r"   # string birlestirme
print(a)
print("python " * 3)
