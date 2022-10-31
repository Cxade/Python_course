# Задание 2.2
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# БЫЛО

# def Pro(N):
#     list = []
#     a = 1
#     for i in range(N):
#         a *= i+1
#         list.append(a)
#     return list

# print(Pro(4))
# print(Pro(6))




# СТАЛО

import math

def fact(N):
    list_fact = [math.factorial(i) for i in range(1, N+1)]
    return list_fact

print(fact(4))

