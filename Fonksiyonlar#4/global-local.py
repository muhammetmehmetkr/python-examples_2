c = 20

def yazdir():
    c = 10
    print(c)
yazdir()
print(c)

d = 50
def yazdir2():
    global d
    d = 40
    print(d)
yazdir2()
print(d)
