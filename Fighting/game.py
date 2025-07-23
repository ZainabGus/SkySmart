import random

from player import Player
from utils import Utils
Utils = Utils()

class Game:
    def __init__(self):
        self.player = Player()
        self.enemies = []
        self.days = random.randint(100, 200)
        self.game_loop()

    def game_loop(self):
        # Играем до тех пор, пока персонаж здоров
        while self.player.is_alive:
            Utils.clear()

            print(f"Осталось {self.days} дней! Чем займется {self.player.name}?")
            print(f"(Здоровье: {self.player.health})")

            # Выбор дальнейшего действия, в один игровой день можно сделать только 3 действия
            for act in range(3):
                # Предложит выбрать действие, провалидирует ввод и вернет только нужный ответ
                action = Utils.choose_action(
                    f"{self.player.name} собирается:\n 1 - Пойти на вылазку;\n 2 - Чилить в таверне;\n 3 - Спать;\n 4 - Сдаться;\n 5 - Проверить семью;\n 6 - Строить убежище;",
                    "123456"
                )

                if act == '1':
                    pass
                elif act == '2':
                    pass
                elif act == '3':
                    pass
                elif act == '4':
                    pass
                elif act == '5':
                    pass
                elif act == '6':
                    pass

                # На случай, если персонаж пострадал
                if not self.player.is_alive:
                    pass


if __name__ == '__main__':
    game = Game()