import pygame as pg
import random
class Character(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Character.png')
        self.image = pg.transform.scale(self.image, (200, 400))
        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 100

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= 1
        if keys[pg.K_RIGHT]:
            self.rect.x += 1

class Butterfly(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('бабочка.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, 500)
        self.rect.y = random.randint(0, 500)

    def update(self):
        if random.randint(0, 1) == 0:
            self.rect.x -= 1
        else:
            self.rect.x += 1

        if random.randint(0, 1) == 0:
            self.rect.x -= 1
        else:
            self.rect.x += 1