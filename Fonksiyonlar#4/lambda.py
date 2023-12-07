# kucuk fonsiyonlar icin kullanilir..(lambda)

def ikiylecarp(x):
    return 2*x

print(ikiylecarp(10))  # def yapisi ile..

ikiylecarp2 = lambda a: a*2

print(ikiylecarp2(30))  # lambda yapisi ile..

toplama = lambda a, b, c: a+b+c

print(toplama(100, 200, 300))
