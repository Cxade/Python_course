# Дан список чисел. Создайте список, в который попадают числа, описывающие возрастающую
# последовательность. Порядок элементов менять нельзя.


import random

list = [x for x in range(1, 10)]
random.shuffle(list)
print(list)

listOfLists = []
for i in range(len(list) - 1):
    subList = [list[i]]
    for j in range(i, len(list) - 1):
        if list[j] < list[j + 1]:
            subList.append(list[j + 1])
        else:
            break
    if len(subList) > 1 and subList not in listOfLists:
        listOfLists.append(subList)

print(listOfLists)
    