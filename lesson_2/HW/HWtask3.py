# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.


def Posl(n):
    list = []
    x = 0
    sum = 0
    for i in range(1, n+1):
        x = round((1+1/i) ** i, 3)
        sum += x
        list.append(x)
    return f"Список: {list},\nCумма: {sum}"

print(Posl(6))


#  result = round((1 + 1 / i) ** i, 3)