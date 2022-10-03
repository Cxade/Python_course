#3. Напишите программу, в которой пользователь будет задавать две строки,
#  а программа - определять количество вхождений одной строки в другой.

# x1 = str(input("Введите 1 строку: "))
# x2 = str(input("Введите 2 строку: "))

# print(x1)
# print(x2)

# count = 0

# for i in range(len(x2)+1):
#     l = len(x1) + i
#     if x1 == x2[i:l]:
#         count +=1
# print(count)





# count = 0
# dlina = int(len(x2))
# for i in range(len(x1) - dlina + 1):
#     if x1[i : dlina +1] == x2:
#         count += 1
# print(count)

textFirst = input('Введите первую строку: ')
textSecond = input('Введите вторую строку: ')

string = ''
subString = ''

if len (textFirst) > len(textSecond):
    string = textFirst
    subString = textSecond
else:
    string = textSecond
    subString = textFirst

print(string.count(subString))