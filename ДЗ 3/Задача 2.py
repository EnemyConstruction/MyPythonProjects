import random

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        x = array[i]
        j = i

        while j > 0 and array[j - 1] > x:
            array[j] = array[j - 1]
            j -= 1

        array[j] = x

    return array

amount = int(input("Введите длину массива: "))
arr = []
minus = False
for i in range(amount):
    tmp_elem = random.randint(-20, 20)
    if tmp_elem < 0:
        minus = True
    arr.append(tmp_elem)
    if i == amount - 1 and minus:
        arr = insertion_sort(arr)
    elif i == amount - 1:
        arr = insertion_sort(arr)
        arr.sort(reverse=True)

print(arr)