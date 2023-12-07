# while dongulerinde degisken degerini artirmazsan dongu sonsuza girer.
i = 0
while i < 10:
    print("i nin degeri {}".format(i+1))
    i += 1

i = 2
while i < 20:
    print(i)
    i += 2

# liste uzerinde index ile gezinme
liste = [1, 2, 3, 4, 5]
a = 0
while a < len(liste):
    print("index: {} eleman: {}".format(a, liste[a]))
    a += 1

# sonsuz dongu
"""i = 0
while i != 1:
    print("k1r")"""
