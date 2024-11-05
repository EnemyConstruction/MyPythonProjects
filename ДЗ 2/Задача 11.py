import random

amount = int(input("Введите число N: "))
arr = [random.randint(1, 100) for _ in range(amount)]
print(arr)

print(list(map(lambda x: arr.index(x), filter(lambda x: x % 2 == 0, arr))))