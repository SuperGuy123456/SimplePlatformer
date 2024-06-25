import pygame
pygame.init()

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y, image,size , friction):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.friction = friction

    def draw(self,screen):
        self.image.fill((0, 255, 0))

        screen.blit(self.image, self.rect)
