import pygame
import settings
pygame.init()

class Checkpoint(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [settings.checkpoint,settings.active_checkpoint]
        self.index = 0
        self.rect = self.images[self.index].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

    def draw(self, screen, camera):
        self.rect = self.images[self.index].get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.images[self.index], camera.apply_position(self.rect))

    def update(self):
        if self.rect.colliderect(self.player.rect):
            self.index = 1
            self.player.checkpoint = self
    def set_player(self,player):
        self.player = player