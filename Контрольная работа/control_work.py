import random
import time
import matplotlib.pyplot as plt

def quick_sort_results():
# Быстрая сортировка
    def quick_sort(arr):
        if len(arr) <= 1: # на случай, если массив состоит из одного элемента, вернёв массив сразу
            return arr
        else:
            rand_elem = random.choice(arr) # выбираем случайный элемент для дальнейшей сортировки массива
            less_elems = [elem for elem in arr if elem < rand_elem] # далее выбираем в данный массив элементы меньше случайного
            as_elems = [rand_elem] * arr.count(rand_elem) # в данный массив выбираем элементы равные случайному
            more_elems = [elem for elem in arr if elem > rand_elem] # в данный массив выбираем элементы больше случайного
            return quick_sort(less_elems) + as_elems + quick_sort(more_elems) # далее необходимо с помощью рекурсии рассортировать два массива с большими и меньшими элементами по такому же принципу и вернуть итоговый массив

    ten_arr = [random.randint(0, 100) for __ in range(0, 10)]
    hundred_arr = [random.randint(0, 1000) for __ in range(0, 100)]
    thousand_arr = [random.randint(0, 10000) for __ in range(0, 1000)]

    start_time = time.time()  # запоминаем время начала выполнения функции
    quick_sort(ten_arr)  # вызываем функцию
    end_time = time.time()  # запоминаем время окончания выполнения функции
    execution_time1 = end_time - start_time  # вычисляем время выполнения функции
    print(f"Время выполнения на 10 элементах: {execution_time1} секунд")

    start_time = time.time()  # запоминаем время начала выполнения функции
    quick_sort(hundred_arr)  # вызываем функцию
    end_time = time.time()  # запоминаем время окончания выполнения функции
    execution_time2 = end_time - start_time  # вычисляем время выполнения функции
    print(f"Время выполнения на 100 элементах: {execution_time2} секунд")

    start_time = time.time()  # запоминаем время начала выполнения функции
    quick_sort(thousand_arr)  # вызываем функцию
    end_time = time.time()  # запоминаем время окончания выполнения функции
    execution_time3 = end_time - start_time  # вычисляем время выполнения функции
    print(f"Время выполнения на 1000 элементах: {execution_time3} секунд")

    return execution_time1, execution_time2, execution_time3

def selection_results():
    # Сортировка выбором
    def selection(sort_nums):  
        for i in range(len(sort_nums)): # алгоритм делит список на две части: отсортированную и основную. Отсортированная часть находится в крайней части списка
            index = i # выбираем элемент списка по его индексу
            for j in range(i + 1, len(sort_nums)):
                if sort_nums[j] < sort_nums[index]: # находим наименьший элемент среди всех в списке
                    index = j
            sort_nums[i], sort_nums[index] = sort_nums[index], sort_nums[i] # как только нашли наименьший элемент в списке, ставим его вперёд, и повторяем алгоритм

    ten_arr = [random.randint(0, 100) for __ in range(0, 10)]
    hundred_arr = [random.randint(0, 1000) for __ in range(0, 100)]
    thousand_arr = [random.randint(0, 10000) for __ in range(0, 1000)]

    start_time = time.time()  # запоминаем время начала выполнения функции
    selection(ten_arr)  # вызываем функцию
    end_time = time.time()  # запоминаем время окончания выполнения функции
    execution_time1 = end_time - start_time  # вычисляем время выполнения функции
    print(f"Время выполнения на 10 элементах: {execution_time1} секунд")

    start_time = time.time()  # запоминаем время начала выполнения функции
    selection(hundred_arr)  # вызываем функцию
    end_time = time.time()  # запоминаем время окончания выполнения функции
    execution_time2 = end_time - start_time  # вычисляем время выполнения функции
    print(f"Время выполнения на 100 элементах: {execution_time2} секунд")

    start_time = time.time()  # запоминаем время начала выполнения функции
    selection(thousand_arr)  # вызываем функцию
    end_time = time.time()  # запоминаем время окончания выполнения функции
    execution_time3 = end_time - start_time  # вычисляем время выполнения функции
    print(f"Время выполнения на 1000 элементах: {execution_time3} секунд")

    return execution_time1, execution_time2, execution_time3

def bubble_results():
    # Сортировка пузырьком
    def bubble(list_nums):  
        swap_bool = True # переменная введена для того, чтобы алгоритм не выполнялся бесконечно
        while swap_bool:
            swap_bool = False # при отсутствии изменений в списке алгоритм перестанет выполняться
            for i in range(len(list_nums) - 1): # сравниваем попарно элементы списка, меняя их местами, если это нужно
                if list_nums[i] > list_nums[i + 1]: # сравниваем два элемента 
                    list_nums[i], list_nums[i + 1] = list_nums[i + 1], list_nums[i] # если первый больше, то они меняются местами
                    swap_bool = True # если смена местами прошла успешно, алгоритм продолжает работу

    ten_arr = [random.randint(0, 100) for __ in range(0, 10)]
    hundred_arr = [random.randint(0, 1000) for __ in range(0, 100)]
    thousand_arr = [random.randint(0, 10000) for __ in range(0, 1000)]

    start_time = time.time()  # запоминаем время начала выполнения функции
    bubble(ten_arr)  # вызываем функцию
    end_time = time.time()  # запоминаем время окончания выполнения функции
    execution_time1 = end_time - start_time  # вычисляем время выполнения функции
    print(f"Время выполнения на 10 элементах: {execution_time1} секунд")

    start_time = time.time()  # запоминаем время начала выполнения функции
    bubble(hundred_arr)  # вызываем функцию
    end_time = time.time()  # запоминаем время окончания выполнения функции
    execution_time2 = end_time - start_time  # вычисляем время выполнения функции
    print(f"Время выполнения на 100 элементах: {execution_time2} секунд")

    start_time = time.time()  # запоминаем время начала выполнения функции
    bubble(thousand_arr)  # вызываем функцию
    end_time = time.time()  # запоминаем время окончания выполнения функции
    execution_time3 = end_time - start_time  # вычисляем время выполнения функции
    print(f"Время выполнения на 1000 элементах: {execution_time3} секунд")

    return execution_time1, execution_time2, execution_time3

quick_results = quick_sort_results()
select_results = selection_results()
bub_results = bubble_results()

names = ['Быстрая сортировка', 'Сортировка выбором', 'Сортировка пузырьком']

plt.bar(names, [quick_results[0], select_results[0], bub_results[0]], label='Время работы')
plt.xlabel('Метод')
plt.ylabel('Время')
plt.title('Время на массиве в 10 элементов')
plt.legend()
plt.show()

plt.bar(names, [quick_results[1], select_results[1], bub_results[1]], label='Время работы')
plt.xlabel('Метод')
plt.ylabel('Время')
plt.title('Время на массиве в 100 элементов')
plt.legend()
plt.show()

plt.bar(names, [quick_results[2], select_results[2], bub_results[2]], label='Время работы')
plt.xlabel('Метод')
plt.ylabel('Время')
plt.title('Время на массиве в 1000 элементов')
plt.legend()
plt.show()

print('По результатам работы можно сделать вывод, что на массивах с небольшим количеством элементов разница почти не чувствуется. \n А вот с большим количеством элементов быстрая сортировка показала наилучший результат, а сортировка пузырьком - наихудший. \n Можно сделать вывод, что для более эффективной работы программ стоит среди трёх исследованных методов сортировки использовать именно быструю сортировку.')