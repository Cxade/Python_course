# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import sample

def randomList(x):
    if x < 1:
        return "Введите корректное число"
    list_nums = sample(range(1, x * 2), x)
    return list_nums


def multiplication(list1):
    list2 = []
    for i in range (1, len(list1) - 1):
        multi = list1[i-1] * list1[-i]
        list2.append(multi)
        if len(list1) % 2 == 0  and i == len(list1) // 2:
            break
    return list2
    
List3 = randomList(6)
print(List3)
print(multiplication(List3))
