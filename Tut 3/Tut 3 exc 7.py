import random
n = int(input("Enter length of array: "))

numbers = [0] * n
for i in range(n):
    numbers[i] = random.randint(0, 100)

print(numbers)
