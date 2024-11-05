from functools import reduce

arr = [1, 2, 3, 4, 4, 4, 5, 6, 6, 7, 6, 1, 1]

arr = list(filter(lambda x: x is not None,reduce(lambda y, x: y.append(x) or y if x != y[-1] else y, arr, [None])))

print(arr)