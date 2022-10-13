# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет их в расчет не берем

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform


def RandomFloatList(x):
    if x < 1:
        return "Введите корректное число"
    list_nums = []
    for i in range(x):
        list_nums.append(round(uniform(1, 10), 2))
    return list_nums


def MaxMinDif(list1):
    max = min = list1[0] % 1

    for i in range(1, len(list1)):
        num = round(list1[i] % 1, 2)
        if num > max:
            max = num
        elif num < min and min != 0:
            min = num

    result = round(max - min, 2)
    print(f"Min: {min}\nMax: {max}\nDifference: {result}")
    return result


list2 = RandomFloatList(5)
print(list2)
MaxMinDif(list2)
