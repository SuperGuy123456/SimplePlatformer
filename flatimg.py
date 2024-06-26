import pygame

pygame.init()

class Flat(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image = image
        self.x = x
        self.y = y
    
    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))