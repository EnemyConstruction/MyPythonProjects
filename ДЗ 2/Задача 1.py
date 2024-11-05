from functools import reduce
import operator as op

arr = list(range(1, 11, 1))
print(arr)
arr = reduce(op.add, list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, arr))))

print(arr)