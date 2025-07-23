import random


print('Привет! Я загадал слово, твоя задача - угадать его по буквам')
print('Нажми Enter чтобы продолжить')
print('Поехали')
letters = []
words = ['пирожок', 'чебурек', 'огурец', 'сосиска', 'котик', 'квокка', 'корабль', 'самолет', 'автомобиль', 'дирижабль', 'кролик', 'программа', 'список']
word =random.choice(words)
isWin = True

hp = 10
while hp > 0:
  isWin = True
  letter = input('Введите букву: ')
  letters.append(letter)
  print(letters)
  for symb in word:
    print(letter, end = ' ')
    print('*', end = ' ')
  if symb == letters:
    if symb in letters:
      print(symb, end = ' ')
    else:
      print('*', end = ' ')
      isWin = False

  print()

  if isWin:
    print('Ты угадал! Молодец!')


  if letter not in word:
    hp -= 1
    print('Кол-во жизней:', hp)
if hp == 0:
  print('У тебя закончились жизни. Ты проиграл!')
  print('Загаданое слово:', word)



