import random

from person import Person
from utils import Utils
from constants import role
utils = Utils()


class Player(Person):
    def __init__(self):
        super().__init__()
        self.set_name()
        self.get_person_class()
        self._set_class_properties()

        self.money = float(random.randint(10, 500))
        self.inventory = ['банан', 'деревянный меч']

        utils.go_on()
        print(f'{self.name} - {self._person_class}.')
        print('У него такие характеристики:')
        print(f'здоровье - {self.health}, \nатака - {self.attack}, \nзащита - {self.defence}')
        utils.go_on()
    def set_name(self):
        while True:
            print('Как зовут твоего героя?: ')
            name = utils.speech_recognition()
            if utils.is_valid(name):
                break
        self.name = name

    # def get_person_class(self):
    #     while True:
    #         print(f'\nВведите роль: 1-Воин, 2-Лучник, 3-Маг\n')
    #         choice = utils.speech_recognition()
    #         if utils.is_valid(choice, '123'):
    #             break
    #     self._person_class = role[choice]

    def increase_money(self, value):
        self.money += value
        print(f'Заработано {value} монетю Осталось: {round(self.money, 2)} монет')

    def dercrease_money(self, value):
        if self.money - value < 0:
            print('Недостаточно денег ಥ_ಥ')
            return False
        else:
            self.money -= value
            print(f'Потрачено {value} монет. Осталось: {round(self.money, 2)} монет')
            return True
