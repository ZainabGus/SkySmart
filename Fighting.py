import colorama
import random
import time

import os


white = colorama.Fore.WHITE
green = colorama.Fore.GREEN
red = colorama.Fore.RED
blue = colorama.Fore.BLUE
yellow = colorama.Fore.YELLOW
cyan = colorama.Fore.CYAN

delay = 2
role = {
    '1': 'Ведьма',
    '2': 'Эльф',
    '3': 'Фея'
}

classes = {
    'Ведьма': {
        'здоровье': 70,
        'атака': 20,
        'защита': 50,
        'навыки': {
            'полёт на метле': 60,
            'зельеваренье': 80
        }
    },
    'Эльф': {
        'здоровье': 60,
        'атака': 70,
        'защита': 45,
        'навыки': {
            'стрельба из лука': 80
        }
    },
    'Фея': {
        'здоровье': 50,
        'атака': 30,
        'защита': 35,
        'навыки': {
            'полёт': 100,
            'магия': 85
        }
    }
}


def init_person(name: str, is_enemy: bool = False) -> dict[str, str | dict[str, int | dict]]:
    if is_enemy:
        person = {'класс': role[random.choice(list(role.keys()))]}
    else:
        while True:
            choice = input(f'{blue} Введите роль: 1-Воин, 2-Лучник, 3-Маг\n {white}')
            if is_valid(choice, True):
                break
        person = {'класс': role[choice]}

    person.update({'характеристики': classes[person['класс']]})
    person.update({'имя': name})

    print(f"{green}{person['имя']} - {yellow}{person['класс']}, имеет характеристики: {person['характеристики']}")
    return person


def attack_enemy(enemy1: dict[str, str | dict], enemy2: dict[str, str | dict]) -> None:
    print(f"{red}{enemy1['имя']} {white}атакует {red}{enemy2['имя']}!")

    time.sleep(delay)

    apply_skill(enemy2)

    damage = enemy1['характеристики']['атака'] - enemy2['характеристики']['защита']
    if damage < 0:
        damage = 1

    enemy2['характеристики']['здоровье'] -= damage
    print(
        f"{red}{enemy1['имя']} {white}наносит {damage} урона и у {red}{enemy2['имя']} остается {white}{enemy2['характеристики']['здоровье']} здоровья!")


def get_random_name() -> str:
    from random import choice
    first_names = ['Доктор', 'Летающий', 'Светящийся', 'Профессор', 'Неимоверный', 'Мега', 'Железный', 'Голодный',
                   'Капитан', 'Быстрый', 'Мистер', 'Горячий', 'Звездный', 'Космический', 'Стойкий', 'Восхитительный',
                   'Непопедимый']
    second_names = ['слесарь', 'мухомор', 'пепел', 'лемур', 'шаман', 'пельмень', 'слизень', 'алхимик', 'крот', 'фикус',
                    'господин', 'кролик', 'танцор', 'пингвин', 'викинг', 'паук', 'плащ']
    return f"{choice(first_names)} {choice(second_names)}"


def is_valid(other: str, is_role: bool = False) -> bool:
    if len(other) <= 0:
        print('Ошибка ввода. Вы ввели пустую строку.')
        return False
    elif other not in '123' and is_role:
        print('Ошибка ввода. Вы ввели не правильное значение. Введите числа от 1 до 3.')
        return False
    else:
        return True


def apply_skill(enemy):
    rand = random.randint(0, 9)
    if rand > 6:
        skill = random.choice(list(enemy['характеристики']['навыки'].keys()))  # Выбирает случайный навык
        enemy['характеристики']['здоровье'] += enemy['характеристики']['навыки'][skill]

        print(f"{enemy['имя']} {white}применяет способность{blue} {skill}!")


def get_player_name() -> str:
    while True:
        player_name = input('Как зовут твоего героя?\n')
        if is_valid(player_name):
            break
    return player_name


def fight_for_the_win(attacker: dict[str, str | dict], defender: dict[str, str | dict]) -> bool:
    while True:
        time.sleep(delay)
        clear()

        if attacker['характеристики']['здоровье'] > 0:
            attack_enemy(attacker, defender)
        else:
            print(f"{attacker['имя']} потерпел поражение")
            return False

        if defender['характеристики']['здоровье'] > 0:
            attack_enemy(defender, attacker)
        else:
            print(f"{defender['имя']} потерпел поражение")
            return True
        proceed()


def proceed():
    input('Нажмите Enter, чтобы продолжить')


def clear(): return os.system('cls')


clear()

player = init_person(name=get_player_name())
enemy = init_person(name=get_random_name(), is_enemy=True)
# attack_enemy(player, enemy)

proceed()
clear()

fight_for_the_win(player, enemy)
