# Напишите программу, которая принимает на вход число N и выдает 
# последовательность из N членов.
# Пример:
# для N = 5: 1, -3, 9, -27, 81




# БЫЛО


# def posled(N):
#     list = []
#     for i in range(N):
#         list.append((-3)**i)
#     return list


# print(posled(5))




# СТАЛО

def posled(N):
    list = [(-3)**x for x in range(N)]
    return list


print(posled(5))