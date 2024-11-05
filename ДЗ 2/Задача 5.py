import random

amount = int(input("Введите число N: "))
arr = [random.randint(1, 100) for _ in range(2*amount + 1)]
arr.sort()
arrB = arr[:amount]
arrC = arr[amount:2*amount]

print(arrB, arrC)