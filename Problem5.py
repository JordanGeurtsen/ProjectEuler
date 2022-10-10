dividers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
tempValues = []
found = False

number = 1

while found == False:
    for i in dividers:
        tempNumber = number / i
        tempValues.append(tempNumber)

    tempBools = [True if x == int(x) else False for x in tempValues]

    print(number, tempBools)

    if all(tempBools):
        print(number)
        found = True
        break
    else:
        number += 1
        tempValues = []

    if found:
        break
