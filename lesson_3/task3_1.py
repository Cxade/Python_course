# Задайте список. Напишите программу, которая определит, присутствует ли
# в заданом списке строк некое число. Если есть то в каком элементе.




num = input('Введите число: ')
list = ['sadwadaw422', 'sad222ad422', 'awggaw521']

# while item in range(list):
#     if item.find(num)!= -1:
#         print('FOund the string')
#     else:
#         print("Not found")

listOFindex = []
for i in range(len(list)):
    if list[i].find(num)!= -1:
        listOFindex.append(i)

if len(listOFindex) > 0:
    print(f'Элементы с индексами {listOFindex} содержат символ {num}')
else:
    print(f'Элементы списка не содержат символ {num}')



# что-то нерабочее
# num = input('Введите число: ')
# list = ['sadwadaw422', 'sad222ad422', 'awggaw521']    

# positionList = []
# for element in range(len(list)):
#     for position in list[i]:
#         if position.isdigit() == num:
#             positionList.append(i)
# print(positionList)



# Ещё вариант
# num = input('Введите число: ')
# list = ['sadwadaw422', 'sad222ad422', 'awggaw521']

# positinList = []
# for i in range(len(list)):
#     if num in list[i]:
#         positinList.append(i)
# print(positinList)