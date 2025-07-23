from player import Player
from enemy import Enemy

player = Player()
enemy = Enemy()

player.fight_for_the_win(player, enemy)

# import speech_recognition as sr
#
# recognizer = sr.Recognizer()
#
# with sr.Microphone() as sourse:
#     print('Слушаю ...')
#     audio = recognizer.listen(sourse)
#     print('Конец связи.')
#
#
# try:
#     text = recognizer.recognize_google(audio, language='ru-RU')
#     print(f'Вы сказали: {text}')
# except sr.UnknownValueError:
#     print('Ничего не понял :_(')
# except sr.RequestError as e:
#     print(f'Ошибка сервиса распознавания речи {e}')
