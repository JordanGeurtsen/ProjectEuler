for i in range(1, 1000):
    for j in range(i, 1000):
        a = i ** 2
        b = j ** 2
        c = a + b
        if sum([a, b, c]) == 1000 & isinstance(c ** 0.5, int):
            print(a, b, c)
            print(a ** 0.5, b ** 0.5, c ** 0.5)
            print(a * b * c)
            print()
            break
        if sum([a, b, c]) > 1000:
            break
