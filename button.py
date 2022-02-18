import pygame

buttons = pygame.sprite.Group()

class Button(pygame.sprite.Sprite):
    def __init__(self, text, pos, w, h, font, fg = 'white', bg = 'black', text_size = 16):
        super().__init__()
        self.text = text
        self.font = pygame.freetype.SysFont(font, text_size)
        self.text_render = self.font.render(text, True, (0,0,0))
        self.x, self.y, self.w , self.h = *pos, w, h
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.fg = fg
        self.bg = bg
        buttons.add(self)

    def render(self):
        pass
        #screen.blit()

    def check_collision(self, x, y):
        if self.x-self.w <= x <= self.x+self.w:
            if self.y-self.h <= y <= self.y+self.h:
                return True
        return False