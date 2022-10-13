# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def converter(num):
    list1 = []

    while num > 0:
        list1.insert(0, num % 2)
        num //= 2

    print(*list1, sep="")


converter(int(input('Введите число: ')))


# num = int(input('Введите число: '))
# print(f'{num} в двоичной системе счисления: ', bin(num)[2:])