# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:*

# "2+2" => 4;

# "1+2*3" => 7;

# "1-2*3" => -5;




string = input('Введите выражение: ')

opSelect = {
    "*": lambda x, y: int(x) * int(y),
    "/": lambda x, y: int(x) / int(y),
    "+": lambda x, y: int(x) + int(y),
    "-": lambda x, y: int(x) - int(y)}

string = string.replace(' ', '').strip()
string = string.replace('+', ' + ')\
    .replace('-', ' - ')\
    .replace('*', ' * ')\
    .replace('/', ' / ')
string = string.split()

def deleteElement(string, i):
    string.pop(i + 1)
    string.pop(i)

def operation(string, i, oper):
    if string[i] == oper:
        string[i - 1] = opSelect.get(oper)(int(string[i - 1]), int(string[i + 1]))
        deleteElement(string, i)
        return True

example = ''.join(string)

while len(string)>1:
    if '*' in string or '/' in string:
        for i in range(len(string)):
            if operation(string, i, '*'): break
            if operation(string, i, '/'): break

    elif '+' in string or '-' in string:
        for i in range(len(string)):
            if operation(string, i, '+'): break
            if operation(string, i, '-'): break

print(f'{example}={string[0]}')



# ДРУГОЕ (со скобками)

# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,* приоритет операций стандартный.
# *Добавьте скобки, приорите операций меняется

# actions = {
#     "^": lambda x, y: str(float(x) ** float(y)),
#     "*": lambda x, y: str(float(x) * float(y)),
#     "/": lambda x, y: str(float(x) / float(y)),
#     "+": lambda x, y: str(float(x) + float(y)),
#     "-": lambda x, y: str(float(x) - float(y)),
# }

# res = "( 10 + 5 ) * 3 - 8 / 2"

# def scob(line):
#     lst = []
#     i = 0
#     while i < len(line):
#         if line[i] == '(':
#             m = line.index(")", i)
#             lst.append(line[i+1:m])
#             i = m
#         else:
#             lst.append(line[i])
#         i += 1
#     return lst

# # print(scob(res.split()))


# def in_scob(lst):
#     for i in range(len(lst)):
#         if isinstance(lst[i], list):    #ф-ция проверяет объект на принадлежность классу (вернут True или False)
#             a, b, c = scob(lst[i])
#             lst[i] = actions[b](a, c)
#     return lst

# # print(in_scob(scob(res.split())))

# def result(lst):
#     prior = [i for i, j in enumerate(lst) if j in "*/"]
#     while prior:
#         t = prior[0]
#         a, b, c = lst[t - 1: t + 2]
#         lst.insert(t-1,actions[b](a, c))
#         del lst[t: t + 3]
#         prior = [i for i, j in enumerate(lst) if j in "*/"]
#     while len(lst) > 1:
#         a, b, c = lst[:3]
#         del lst[:3]
#         lst.insert(0, actions[b](a, c))
        

#     return lst

# print(result(in_scob(scob(res.split()))))











# import random

# myList = [random.randint(0,10) for _ in range(10)]
# print (myList)
# # myList = list(map(str, myList))
# # print (myList)
# myList = list(map(lambda x: x + 1, myList))
# print (myList)

# myList1 = [random.randint(-100, 100) for i in range(10)]
# myList2 = [random.randint(-100, 100) for i in range(10)]
# myList3 = [random.randint(-100, 100) for i in range(10)]
# print(myList1)
# print(myList2)
# print(myList3)

# myList = list(zip(myList1, myList2, myList3))

# print(myList)


# mysum = []
# for i in myList:
#     mysum.append(sum(i))
# print(mysum)

# for i in enumerate(myList):
#     if i[1]>40:
#         print(i[0])



# myList = list(map(lambda x: x**2, map(int, input("Введите числа через пробел: ").split())))
# print(myList)