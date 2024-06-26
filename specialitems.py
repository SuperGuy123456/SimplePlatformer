import pygame
import settings
from time import time
pygame.init()

class decor(pygame.sprite.Sprite):
    def __init__(self, x, y, image, rect = True):
        super().__init__()
        self.image = image
        self.makerect = rect
        if rect:
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        else:
            self.x = x
            self.y = y
        self.anistarted = False
        if self.image == settings.crate:
            self.frames = [settings.cratef1, settings.cratef2, settings.cratef3, settings.cratef4]
            self.index = 0
            self.anistarted = False
            self.lasttime = time()

    def draw(self,screen):
        if self.anistarted == False:
            if self.makerect:
                screen.blit(self.image, self.rect)
            else:
                screen.blit(self.image, (self.x,self.y))
        else:
            screen.blit(self.frames[self.index], self.rect)

        self.update()

    def update(self):
        if self.image == settings.sign:
            pass #print("sign interaction")
        else:
            if self.anistarted:
                self.animate()

    def animate(self):
        now = time()
        if now - self.lasttime > 0.2 and self.index < 3:
            self.lasttime = now
            self.index += 1

    def crate(self):
        self.anistarted = True