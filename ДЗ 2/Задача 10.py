arr = [8, 3, -1, 5, 16, -23, -18, 56, 15, -3, 2]

arrB = list(filter(lambda x: x < 0, arr))
arrC = list(filter(lambda x: x > 0, arr))

print(arrB, arrC)