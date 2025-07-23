from random import randint

import pygame as pg
from pygame.examples.go_over_there import screen


size = (500, 500)
screen = pg.display.set_mode(size)

fps = 50
clock = pg.time.Clock()

class Starship(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((150, 150))
        self.image = pg.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 250

    def resize(self):
        #  напиши код здесь
        self.image = pg.transform.scale(self.image, (400, 500))

    def info(self):
        #  напиши код здесь
        print('Координаты:', self.rect.x, self.rect.y)

a = Starship()

small_rect = pg.Rect(0, 0, 100, 100)
small_rect.center = (size[0] // 2, size[1] // 2)

left_eye = pg.Rect(0, 0, 20, 30)
right_eye = pg.Rect(0, 0, 20, 30)
left_eye.midright = (size[0] // 2 - 10, size[1] // 2)
right_eye.midleft = (size[0] // 2 + 10, size[1] // 2)

direction = 'close'

while True:
    screen.fill(pg.Color('purple'))
    a.update()
    a.info()

    # for event in pg.event.get():
    #     if event.type == pg.KEYDOWN:
    #         if event.key == pg.K_e:
    #
    #             if left_eye.height == 0:
    #                 direction = 'open'
    #             if left_eye.height == 30:
    #                 direction = 'close'
    #
    #             if direction == 'close':
    #                 left_eye.height -= 30
    #                 right_eye.height -= 30
    #             if direction == 'open':
    #                 left_eye.height += 30
    #                 right_eye.height += 30


    screen.blit(a.image, a.rect)
    pg.draw.rect(screen, pg.Color('red'), small_rect)
    pg.draw.rect(screen, pg.Color('white'), left_eye)
    pg.draw.rect(screen, pg.Color('white'), right_eye)

    pg.display.flip()
    clock.tick(fps)