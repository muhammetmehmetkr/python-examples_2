a = int(input("a degerini giriniz:"))
b = int(input("b degerini giriniz:"))
c = int(input("c degerini giriniz:"))

delta = b ** 2 - 4 * a * c
x1 = (- b - delta ** 0.5) / (2 * a)
x2 = (- b + delta ** 0.5) / (2 * a)

print("birinci kok: {}\nikinci kok: {}".format(x1, x2))
