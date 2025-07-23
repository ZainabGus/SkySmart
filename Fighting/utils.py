import os
import speech_recognition as sr

class Utils:
    def clear(self):
      return os.system('cls')

    def go_on(self):
      input('\nНажмите Enter, чтобы продолжить\n')
      self.clear()

    def is_valid(self, other, data_range='') -> bool:
      if len(other) <= 0:
        print('Ошибка ввода. Вы ввели пустую строку.')
        return False
      elif (other not in data_range and (data_range != '')) or (other == data_range):
        print('Ошибка ввода. Вы ввели не правильное значение. Введите числа от 1 до 3.')
        return False
      else:
        return True

    def speech_recognition(self) -> str:
        recognizer = sr.Recognizer()
        text = ''

        with sr.Microphone() as sourse:
            print('Слушаю ...')

            while not text:
                audio = recognizer.listen(sourse)
                print('Конец связи.')

                try:
                    text = recognizer.recognize_google(audio, language='ru-RU').capitalize()
                    print(f'Вы сказали: {text}')
                    return text
                except sr.UnknownValueError:
                    print('Ничего не понял :_(')
                except sr.RequestError as e:
                    print(f'Ошибка сервиса распознавания речи {e}')


    def choose_action(self, text: str, action_numbers: str = '12') -> str:
        while True:
            print(text)
            choice = self.speech_recognition()
            if self.is_valid(choice, action_numbers):
                break
        return choice
