# ground.py

import pygame
import settings
from camera import Camera

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y, image, friction):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.friction = friction

    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply_position(self.rect))
