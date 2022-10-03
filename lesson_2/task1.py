# Напишите программу, которая принимает на вход число N и выдает 
# последовательность из N членов.
# Пример:
# для N = 5: 1, -3, 9, -27, 81


def posled(N):
    list = []
    for i in range(N):
        list.append((-3)**i)
    return list


print(posled(5))


# def posled(N):
#     list = []
#     num = 1
#     for i in range(1, N + 1):
#         list.append(num)
#         num *= -3
#     return list

# print(posled(5))

#ещё вариант
def Degree (x):
    for i in range(0, x):
        print((-3)**i, end = ' ')

# Degree(5)