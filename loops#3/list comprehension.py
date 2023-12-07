# ekstra kolaylik saglar..
liste1 = [1, 2, 3, 4]
liste2 = list()

for i in liste1:
    liste2.append(i)   # liste1 i liste2 nin icine attik.
print(liste2)       # normalde boyle yazilir..
# list comprehension
liste3 = [3, 4, 5, 6]
liste4 = [i for i in liste3]    # i ve for dan sonra 2 kisim olarak dusunulmelidir.
print(liste4)

liste1 = [1, 2, 3]
liste2 = [i*2 for i in liste1]  # carpma islemi yapip deger atadik.
print(liste2)

liste3 = [(1, 2), (3, 4), (5, 6)]
liste4 = [i*j for i, j in liste3]
print(liste4)

liste1 = [(1, 2, 3, 4), (5, 6, 7, 8)]   # normal method
liste2 = list()
for i in liste1:
    for j in i:
        liste2.append(j)
print(liste2)

print("***********")

liste1 = [(1, 2, 3, 4), (5, 6, 7, 8)]    # list comprehension
liste2 = [j for i in liste1 for j in i]  # ic ice dongu mantigi
print(liste2)

