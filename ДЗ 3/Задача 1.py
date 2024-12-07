import operator
import random

def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

amount = int(input("Введите длину массива: "))
arr = []
even_count = 0
odd_count = 0
for i in range(amount):
    tmp_elem = random.randint(0, 100)
    even_count = even_count + 1 if (i%2 == 1 and tmp_elem % 2 == 0) else even_count + 0
    odd_count = odd_count + 1 if (i%2 == 0 and tmp_elem % 2 == 1) else odd_count + 0
    arr.append(tmp_elem)
    if i == amount - 1 and even_count > odd_count:
        arr = merge_sort(arr)
    elif i == amount - 1 and even_count < odd_count:
        arr = merge_sort(arr)
        arr.sort(reverse=True)

print(arr)