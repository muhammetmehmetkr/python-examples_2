a = 5
b = 14
print(a+b)
print("mehmet", 34)

# type fonksiyonu
print(type(a))

# sep parametresi
print("20", "10", "1999", sep="/")   # sep --> separate fonksiyonu olmasi lazim.
print("mehmet", "k1r", sep="\n")

# yildizli parametreler
print(*"python")  # karakterlerin arasina bosluk koyar.
print(*"python", sep="\n")
print(*"TBMM", sep=".")

# formatlama
print("{}  {}  {}".format(3.14, 3.19, 4.3))
a = 10
b = 12
print("{}+{}'nin toplami {}'dir.".format(a, b, a+b))
print("{1} {0} {2}".format(23, "mehmet", 34))  # index ile yazdirma
print("{:.2f}  {:.3f}  {:.1f}".format(5.4394, 6.456934, 9.4773224))
