from pygame import *
from pygame.locals import *

init()

x = 600
y = 500
screen = display.set_mode((x, y))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

background = WHITE

run = True

while run:
    for tasks in event.get():
        if tasks.type == QUIT:
            run = False
        if tasks.type == KEYDOWN:
            if tasks.key == K_w:
                background = WHITE
            if tasks.key == K_r:
                background = RED
            if tasks.key == K_g:
                background = GREEN
        
        title = "Color of background is " + str(background)
        screen.fill(background)
        display.set_caption(title)
        display.update()
quit()