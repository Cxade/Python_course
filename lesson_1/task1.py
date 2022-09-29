
# 1. Напишите программу, которая принимает на вход два числа и 
# проверяет, является ли одно число квадратом другого.
    
#     *Примеры:* 
    
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет


a = int(input('Input number a'))
b = int(input('Input number b'))


def solution(a, b):
    return a**2 == b or b**2 == a

print(solution(a, b))


# def array(m):
#     x = []
#     for i in range(m):
#         a = int(input(f'Введите x{i + 1}: '))
#         x.append(a)
    
#     return x

# def max_el(array):
    
#     maxim = 0

#     for i in range(len(array)):
#         if array[i] > array[maxim]:
#             maxim = i

#     return array[maxim]

# l = int(input('Введите количество элементов: '))
# new_array = array(l)
# maxim = max_el(new_array)
# print(f'Максимальный элемент: {maxim}')


