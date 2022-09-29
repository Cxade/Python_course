# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

num = float((input('Input number: ')))

number = int(num * 10 % 10)

if num % 1 == 0:
    print('No')
else:
    print(number)



_____________________________________________


num = float(input('Input number: '))

if num == int(num):
    print('Целое')
else: print('Дробное')