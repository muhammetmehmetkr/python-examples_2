a = 1
b = 1
fibonacci = [1, 1]
print("a: ", a, "b: ", b)

for i in range(10):
    a, b = b, a+b
    print("a: ", a, "b: ", b)
    fibonacci.append(b)  # yeni olusan degerleri bu methodla listeye ekledik...
print(fibonacci)
