value = 600851475143.00

i = 2.00

primeFactors = []

while value != 1.00:
    tempValue = value / i
    if tempValue.is_integer():
        value = tempValue
        primeFactors.append(i)
        i = 2.00
        print(primeFactors)
    else:
        tempValue = value
        i += 1.00
        print(i)

    if value == 1.00:
        break