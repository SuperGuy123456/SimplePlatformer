import pygame
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

    def draw(self,screen):
        if self.makerect:
            screen.blit(self.image, self.rect)
        else:
            screen.blit(self.image, (self.x,self.y))
