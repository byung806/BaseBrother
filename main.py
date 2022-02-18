import pygame, sys
from button import Button, buttons
from screen_manager import ScreenManager

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen_manager = ScreenManager()
clock = pygame.time.Clock()
buttons.add(Button('hi', (0,0), 100, 100, 'Cambria'))

while True:
    # 823654019/1048575 b32
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for b in buttons:
                b.render()
            
    screen.fill('#DCDDD8')
    pygame.display.flip()
    clock.tick(60)