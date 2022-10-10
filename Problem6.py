squareSum = []
numbers = []

for i in range(1, 101):
    squareSum.append(i ** 2)
    numbers.append(i)

sumSqaure = sum(numbers) ** 2

result = sumSqaure - sum(squareSum)
print(result)
