# 2. Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'


import random

# PVP

# def Sweet_1vs1(S: int):

#     player_1 = input("Введите никнейм игрока №1: ")
#     player_2 = input("Введите никнейм игрока №2: ")
#     print(f"Всего конфет: {S}")
#     flag = random.randint(0, 1)
#     turn = 0
#     if flag:
#         print(f"Методом жеребьевки определился ход игрока {player_1}")
#     else:
#         print(f"Методом жеребьевки определился ход игрока {player_2}")

#     while S > 0:
#         if flag:
#             turn = int(input(f"Сколько конфет хочет забрать {player_1}?: "))
#             if 0<turn<29 and turn <= S:
#                 S -= turn
#                 turn = 0
#                 flag = 0
#                 print(f"Осталось конфет: {S}\n")
#             else:
#                 print("Введите число от 1 до 28")
#         else:
#             turn = int(input(f"Сколько конфет хочет забрать {player_2}?: "))
#             if 1<turn<29 and turn <= S:
#                 S -= turn
#                 turn = 0
#                 flag = 1
#                 print(f"Осталось конфет: {S}\n")
#             else:
#                 print("Введите число от 1 до 28")
#     if flag == 0:
#         print(f"Поздравляем с победой игрока {player_1}!")
#     else:
#         print(f"Поздравляем с победой игрока {player_2}!")

#Sweet_1vs1(50)



# С умным ботом

def Sweet_with_bot(S: int):

    player_1 = input("Введите никнейм игрока: ")
    player_bot = random.choice(["Т-800", "Ты_из_будущего", "ВАЛЛ-И", "R2-D2", "Робокоп", "Марвин", "C-3PO", "Бендер"])
    print(f"Твой противник: {player_bot}")
    print(f"Всего конфет: {S}")
    flag = random.randint(0, 1)
    turn = 0
    if flag:
        print(f"Методом жеребьевки определился ход {player_1}")
    else:
        print(f"Методом жеребьевки определился ход  {player_bot}")

    while S > 0:
        if flag:
            turn = int(input(f"Сколько конфет хочет забрать {player_1}?: "))
            if 0<turn<29 and turn <= S:
                S -= turn
                turn = 0
                flag = 0
                print(f"Осталось конфет: {S}\n")
            else:
                print("Введите число от 1 до 28")
        else:
            if S%29 != 0:
                turn = S%29
                S -= turn
                print(f"{player_bot} забирает конфет: {turn}")
                turn = 0
                flag = 1
                print(f"Осталось конфет: {S}\n")
            else:
                turn = random.randint(1, 28)
                print(f"{player_bot} забирает конфет: {turn}")
                S -= turn
                turn = 0
                flag = 1
                print(f"Осталось конфет: {S}\n")
    if flag == 0:
        print(f"Победил {player_1}!")
    else:
        print(f"Победил {player_bot}!")

Sweet_with_bot(50)

