numbers = []
num = 1

while numbers.__len__() < 10001:
    flag = False
    if num > 1:
        for i in range(2, num):
            if flag is True:
                continue
            if (num % i) == 0:
                flag = True
            else:
                flag = False

    if flag is False and num != 1:
        numbers.append(num)

    num += 1

print(numbers.__len__(), max(numbers))
