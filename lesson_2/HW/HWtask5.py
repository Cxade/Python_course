# Реализуйте алгоритм перемешивания списка.

import random as r

# Легкий путь

# def Mix():
#   list_1 = []
#   for i in range(10):
#       list_1.append(r.randint(1, 10))
#   print(list_1)
#   r.shuffle(list_1)
#   print(list_1)



# Путь через дебри

def Mix(N):
    lst = list(range(N))
    lst_len = len(lst)

    print(lst)

    for i in range(lst_len):
        x1 = r.randrange(lst_len)
        x2 = r.randrange(lst_len)
        lst[x1], lst[x2] = lst[x2], lst[x1]

    return(lst)
print(Mix(10))