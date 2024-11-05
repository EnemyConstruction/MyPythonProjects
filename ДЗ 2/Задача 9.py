from functools import reduce
import operator as op

count = int(input("Введите нечетное число n: "))
print(reduce(op.mul,filter(lambda x: x % 2 == 0, range(1, count+1))))