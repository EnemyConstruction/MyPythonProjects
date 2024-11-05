import random

amount = int(input("Введите число N: "))

arr = [random.randint(1, 100) for _ in range(2*amount + 1)]
arr.sort()

print(arr)
print(arr[amount])