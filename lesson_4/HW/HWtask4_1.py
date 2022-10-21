# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001


from decimal import Decimal
from math import pi


def precision (prec, num):
    result = Decimal(f'{num}')
    result = result.quantize(Decimal(f'{prec}'))

    return result


print(precision(0.001, pi))
print(precision(0.1, pi))
print(precision(0.00001, pi))