# Задание 3.1
# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# БЫЛО

# def odd_sum():
#     list1 = [2, 3, 5, 9, 3]
#     sum = 0
#     for i in range(0, len(list1), 2):
#         sum += list1[i]
#     return sum

# print(odd_sum())


# СТАЛО


def oddSum(N):
    list1 = N.split()
    return(sum(int(list1[i]) for i in range(0, len(list1), 2)))

print(oddSum('2 3 5 9 3'))