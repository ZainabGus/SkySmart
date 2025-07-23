from random import randint

import pygame as pg
from sprites import *
from pygame.examples.go_over_there import screen
pg.mixer.init()


size = (500, 500)
screen = pg.display.set_mode(size)

small_rect = pg.Rect(0, 0, 20, 20)
# small_rect.center = (size[0] // 2, size[1] // 2)
#
# left_eye = pg.Rect(0, 0, 20, 30)
# right_eye = pg.Rect(0, 0, 20, 30)
# left_eye.midright = (size[0] // 2 - 10, size[1] // 2)
# right_eye.midleft = (size[0] // 2 + 10, size[1] // 2)
#direction = 'right'

character = Character()

butterflies = pg.sprite.Group()
butterflies.add(Butterfly())
butterflies.add(Butterfly())
butterflies.add(Butterfly())
butterflies.add(Butterfly())
butterflies.add(Butterfly())
butterflies.add(Butterfly())
butterflies.add(Butterfly())
butterflies.add(Butterfly())
butterflies.add(Butterfly())
butterflies.add(Butterfly())
butterflies.add(Butterfly())
butterflies.add(Butterfly())
#character = pg.transform.scale(character, (200, 400))

#character2 = pg.transform.flip(character, False, True)
# character_rect = character.get_rect(center=(size[0] // 2, size[1] // 2))
# character_rect.center = (size[0] // 2, size[1] // 2)


background = pg.image.load('Фон для игры на pygame.png')
background = pg.transform.scale(background, size)

pg.mixer.music.load('Музыка для игры на pygame.mp3')
pg.mixer.music.set_volume(0.02)
#pg.mixer.music.play()

hello_sound = pg.mixer.Sound('Мой голос.mp3')
hello_sound.play()

# cat = pg.image.load('Без названия.jpg')
# cat = pg.transform.scale(cat, (400, 400))
fps = 70

clock = pg.time.Clock()
rect = pg.Rect(50, 50, 400, 400)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        # if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_SPACE:
        #         hello_sound.play()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.pos)
                small_rect.center = event.pos

    # keys = pg.key.get_pressed()
    # if keys[pg.K_LEFT]:
    #     character_rect.x -= 1
    # if keys[pg.K_RIGHT]:
    #     character_rect.x += 1

    # mouse_pos = pg.mouse.get_pos()
    # mouse_keys = pg.mouse.get_pressed()
    # if mouse_keys[0]:
    #     character_rect.center = mouse_pos

    r = randint(0, 255)
    screen.fill(pg.Color(r, 140, 180))
    character.update()
    butterflies.update()

    screen.blit(background, (0, 0))
    screen.blit(character.image, character.rect)
    butterflies.draw(screen)
    pg.draw.rect(screen, pg.Color('red'), small_rect)
    #screen.blit(character2, (100, 100))

    pg.display.flip()
    clock.tick(fps)
    #Смайлик
    # pg.draw.rect(screen, pg.Color('red'), rect)
    # pg.draw.rect(screen, pg.Color('white'), (100, 70, 100, 150))
    # pg.draw.rect(screen, pg.Color('white'), (300, 70, 100, 150))
    # pg.draw.line(screen, pg.Color('white'), (100, 350), (250, 300), 10)
    # pg.draw.line(screen, pg.Color('white'), (250, 300), (400, 350), 10)

    #Луна
    # pg.draw.circle(screen, pg.Color('yellow'), (400, 400), 300)
    # pg.draw.circle(screen, pg.Color('orange'), (500, 150), 20)
    # pg.draw.circle(screen, pg.Color('orange'), (600, 400), 60)
    # pg.draw.circle(screen, pg.Color('orange'), (200, 500), 60)
    # pg.draw.circle(screen, pg.Color('orange'), (400, 370), 20)
    # pg.draw.circle(screen, pg.Color('orange'), (300, 200), 50)
    # pg.draw.circle(screen, pg.Color('orange'), (500, 640), 20)


    # small_rect.height += 1
    # small_rect.width += 1
    #small_rect.x += 1
    # if small_rect.x == 0:
    #     direction = 'right'
    # if small_rect.right == size[0]:
    #     direction = 'left'
    #
    # if direction == 'right':
    #     small_rect.x += 1
    #     left_eye.x += 1
    #     right_eye.x += 1
    # if direction == 'left':
    #     small_rect.x -= 1
    #     left_eye.x -= 1
    #     right_eye.x -= 1
    # # if direction == 'up':
    #     small_rect.y -= 1
    # if direction == 'down':
    #     small_rect.y += 1

    # pg.draw.rect(screen, pg.Color('red'), small_rect)
    # pg.draw.rect(screen, pg.Color('white'), left_eye)
    # pg.draw.rect(screen, pg.Color('white'), right_eye)

