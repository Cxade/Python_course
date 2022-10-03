# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11



def SumNumb(num):
    sum = 0

    degree = len(str(num)) - 2
    num *= 10 ** degree

    while num:
        sum += num % 10
        num //= 10
    return int(sum)


print(SumNumb(6782))
print(SumNumb(0.56))

