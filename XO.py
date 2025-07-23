board = list(range(0, 9))
print(board)

cells = 3
dashes = 13
spaces = 14
counter = 0    #ходы
is_Win = False
win_coords = (
  (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
  (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
)
print(win_coords)

player_token = ''
print('Игра "Крестики-Нолики" для 2-их игроков')

# for a in range(cells):
#   print('' * spaces, end='')
#   print('-' * dashes)
#   print('' * spaces, end='')
#   print(f' | {board[0 + a *3]} | {board[1 + a *3]} | {board[2 + a *3]} |')
#   print('' * spaces, end='')
#   print('-' * dashes)


if counter % 2 == 0:
  player_token = 'X'
else:
  player_token = 'O'


while not is_Win:

  for a in range(cells):
    print('' * spaces, end='')
    print('-' * dashes)
    print('' * spaces, end='')
    print(f' | {board[0 + a *3]} | {board[1 + a *3]} | {board[2 + a *3]} |')
    print('' * spaces, end='')
    print('-' * dashes)


  if counter % 2 == 0:
    player_token = 'X'
  else:
    player_token = 'O'

  player_answer = input(f'Куда положить {player_token}? ')
  player_answer = int(player_answer)

  if str(board[player_answer]) not in 'XO':
    board[player_answer] = player_token
  else:
    print('Эта ячейка занята')
    continue


  counter += 1

  if counter > 4:
    for each in win_coords:
      if board[each[0]] == board[each[1]] == board[each[2]]:
        is_Win = True
        break

    if is_Win:
      print(f'Победил {player_token}')
      break

  if counter == 9:
    print('Ничья')
    break






