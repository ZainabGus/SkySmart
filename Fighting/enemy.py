import random

from person import Person
from utils import Utils
from constants import role
utils = Utils()

class Enemy(Person):
  def __init__(self):
    super().__init__()
    self.__set_name()
    self._person_class = role[random.choice(list(role.keys()))]
    self._set_class_properties()
    self.max_health = self.health

  def __set_name(self):
      from random import choice
      first_names = ['Доктор', 'Летающий', 'Светящийся', 'Профессор', 'Неимоверный', 'Мега', 'Железный', 'Голодный',
                     'Капитан', 'Быстрый', 'Мистер', 'Горячий', 'Звездный', 'Космический', 'Стойкий', 'Восхитительный',
                     'Непопедимый']
      second_names = ['слесарь', 'мухомор', 'пепел', 'лемур', 'шаман', 'пельмень', 'слизень', 'алхимик', 'крот',
                      'фикус', 'господин', 'кролик', 'танцор', 'пингвин', 'викинг', 'паук', 'плащ']
      self.name = f"{choice(first_names)} {choice(second_names)}"
