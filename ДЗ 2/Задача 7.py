import random

amount = int(input("Введите число N: "))
arr = [[random.randint(1, 100)] for _ in range(amount)]
for i in range(len(arr)):
    arr[i].append(i)
arr.sort()

print(arr)