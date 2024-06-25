import pygame
pygame.init()

class item(pygame.sprite.Sprite):
    def __init__(self, x, y, image,size):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self,screen):

        screen.blit(self.image, self.rect)
