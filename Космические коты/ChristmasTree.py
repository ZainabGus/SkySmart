from random import randint

import pygame as pg
from pygame.examples.go_over_there import screen


size = (500, 500)
screen = pg.display.set_mode(size)

small_rect = pg.Rect(0, 0, 50, 50)
small_rect.center = (size[0] // 2, size[1] // 2)
direction = 'right'

fps = 70

clock = pg.time.Clock()

while True:
    r = randint(0, 255)
    screen.fill(pg.Color(r, 140, 180))

    pg.draw.rect(screen, pg.Color('white'), (0, 400, size[0], size[1]))
    pg.draw.rect(screen, pg.Color('brown'), (225, 410, 50, 40))
    pg.draw.polygon(screen, pg.Color(0, 160, 0), ((size[0] // 2, 70), (150, 200), (350, 200)))
    pg.draw.polygon(screen, pg.Color(0, 160, 0), ((size[0] // 2, 140), (130, 270), (370, 270)))
    pg.draw.polygon(screen, pg.Color(0, 160, 0), ((size[0] // 2, 210), (110, 340), (390, 340)))
    pg.draw.polygon(screen, pg.Color(0, 160, 0), ((size[0] // 2, 280), (90, 410), (410, 410)))
    pg.draw.circle(screen, pg.Color('red'), (230, 200), 20)
    pg.draw.circle(screen, pg.Color('red'), (290, 260), 17)
    pg.draw.circle(screen, pg.Color('red'), (200, 300), 25)
    pg.draw.circle(screen, pg.Color('red'), (265, 370), 15)
    pg.draw.circle(screen, pg.Color('white'), (100, 200), 5)
    pg.draw.circle(screen, pg.Color('white'), (70, 340), 5)
    pg.draw.circle(screen, pg.Color('white'), (50, 50), 5)
    pg.draw.circle(screen, pg.Color('white'), (330, 40), 5)
    pg.draw.circle(screen, pg.Color('white'), (40, 300), 5)
    pg.draw.circle(screen, pg.Color('white'), (400, 390), 5)
    pg.draw.circle(screen, pg.Color('white'), (450, 150), 5)
    pg.draw.circle(screen, pg.Color('white'), (470, 310), 5)
    pg.draw.circle(screen, pg.Color('white'), (400, 220), 5)

    pg.display.flip()
    clock.tick(fps)