# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


# БЫЛО

# import math

# def Distance(x1, y1, x2, y2):
#     return round(math.sqrt(pow(x1 - x2,2) + pow(y1 - y2,2)),3)

# print(Distance(3, 6, 2, 1))



# СТАЛО

import math

S = lambda x1, y1, x2, y2: round(math.sqrt(pow(x1 - x2,2) + pow(y1 - y2,2)),3)

print(S(3, 6, 2, 1))