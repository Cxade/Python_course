# Создайте программу для игры в 'Крестики-нолики'.

board = list(range(1,10))


def draw_board(board):
    print('-' * 11)
    for i in range(3):
        for k in range(3):
            print(f"{board[k + i * 3]:^3}", end=" ")
        print(f"\n{'-' * 11}")
    print()


def take_input(player_token):
   valid = False
   while not valid:
      player_turn = input("Куда поставим " + player_token+"?\n")
      try:
         player_turn = int(player_turn)
      except:
         print("Ошибка. Введите число от 1 до 9")
         continue
      if 0 < player_turn < 10:
         if(str(board[player_turn-1]) not in "XO"):
            board[player_turn-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Ошибка. Введите число от 1 до 9")

def check_win(board):
   win_cond = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_cond:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           chck = check_win(board)
           if chck:
              print(chck, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


main(board)
