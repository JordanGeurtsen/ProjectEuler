i = 300
j = 300

results = []

while i <= 999:
    while j <= 999:
        print(i, j)
        number = i * j
        result = [int(x) for x in str(number)]
        length = len(str(number))

        if length == 6:
            if [result[0], result[1], result[2]] == [result[5], result[4], result[3]]:
                results.append(number)
                j += 1
            else:
                j += 1
        else:
            j += 1

        if j == 999:
            i += 1
            j = 100

        if i >= 999:
            break

print(max(results))
